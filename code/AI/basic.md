#### warning
```
if kwargs:
	warnings.warn(
		f"FNO.forward() received unexpected keyword arguments: {list(kwargs.keys())}. "
		"These arguments will be ignored.",
		UserWarning,
		stacklevel=2,
	)
```