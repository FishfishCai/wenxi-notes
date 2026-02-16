# Embedding
## Time Embedding
```python
class TimestepEmbedder(nn.Module):
    """Embed scalar timesteps into fixed-width vector representations."""

    ## Initialize MLP that maps sinusoidal features to `hidden_size`.
    def __init__(self, hidden_size, frequency_embedding_size=256):
        """
        Construct a timestep embedding module based on sinusoidal features and an MLP.
        The module first builds sinusoidal features of size `frequency_embedding_size` and then
        projects them to `hidden_size` using a two-layer MLP.

        Parameters
        ----------
        hidden_size : int
            Output embedding dimension produced by the MLP.
        frequency_embedding_size : int
            Dimension of the sinusoidal feature vector used as MLP input.

        Returns
        -------
        None : NoneType
            This initializer does not return a value.
        """
        super().__init__()
        self.mlp = nn.Sequential(
            nn.Linear(frequency_embedding_size, hidden_size, bias=True),
            nn.SiLU(),
            nn.Linear(hidden_size, hidden_size, bias=True),
        )
        self.frequency_embedding_size = frequency_embedding_size

    @staticmethod
    def timestep_embedding(t, dim, max_period=10000):
        """
        Compute sinusoidal embeddings for timesteps using cosine and sine features.
        The output has shape (N, dim), where N is the batch size and frequencies are log-spaced
        between 1 and 1 / max_period.

        Parameters
        ----------
        t : torch.Tensor
            1-D tensor of shape (N,) containing timestep values; values may be fractional.
        dim : int
            Embedding dimension D of the returned tensor.
        max_period : float
            Maximum period used to set the minimum frequency; larger values yield lower minimum frequency.

        Returns
        -------
        embedding : torch.Tensor
            Tensor of shape (N, dim) containing the sinusoidal embeddings on the same device as `t`.
        """
        # Build log-spaced frequencies on `t.device`.
        half = dim // 2
        freqs = torch.exp(
            -math.log(max_period) * torch.arange(start=0, end=half, dtype=torch.float32) / half
        ).to(device=t.device)
        # Compute phase arguments and concatenate cosine/sine features.
        args = t[:, None].float() * freqs[None]
        embedding = torch.cat([torch.cos(args), torch.sin(args)], dim=-1)
        # Pad with zeros if `dim` is odd.
        if dim % 2:
            embedding = torch.cat([embedding, torch.zeros_like(embedding[:, :1])], dim=-1)
        return embedding

    def forward(self, t):
        """
        Embed timesteps by computing sinusoidal features and applying the MLP.
        The returned tensor has shape (N, hidden_size), where N is the length of `t`.

        Parameters
        ----------
        t : torch.Tensor
            1-D tensor of shape (N,) containing timestep values.

        Returns
        -------
        t_emb : torch.Tensor
            Tensor of shape (N, hidden_size) containing timestep embeddings.
        """
        # Compute sinusoidal features and project with the MLP.
        t_freq = self.timestep_embedding(t, self.frequency_embedding_size)
        t_emb = self.mlp(t_freq)
        return t_emb
```