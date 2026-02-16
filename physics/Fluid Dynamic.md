### Unit
- $1\text{psi} = 1 \frac{\text{lb}}{\text{in}^{2}}=144\frac{\text{lb}}{\text{ft}^{2}}$ 
- $1\text{lb}=1\text{slug}*1\frac{\text{ft}}{\text{s}^{2}}$
- $1\text{ ft}=12\text{ in}$
- $^\circ F=\frac{9}{5}^\circ C+32$
- $^\circ R=\frac{9}{5}(^\circ C+273.15)$
- $^\circ K=^\circ C+273.15$
### Parameter
- $g = 9.81\frac{\text{m}}{\text{s}^{2}}=32.174\frac{\text{ft}}{\text{s}^{2}}$
- $1 \text{mmHg} = 1 \text{ Torr} = 133 \text{Pa}$
- $\rho_{\text{air}} = 1.23~\mathrm{kg/m^3}$ at $15\,^\circ\mathrm{C}$
- $\rho_{w} = 1000~\mathrm{kg/m^3}$ at $4\,^\circ\mathrm{C}$ $(999~\mathrm{kg/m^3}$ at $15\,^\circ\mathrm{C})$
- $\rho_{\text{glycerin}} = 1260~\mathrm{kg/m^3}$ at $20\,^\circ\mathrm{C}$
- $\rho_{\mathrm{Hg}} = 13600~\mathrm{kg/m^3}$ at $20\,^\circ\mathrm{C}$
- $E_{v,\text{water},\,60^\circ\mathrm{F}} = 3.12 \times 10^{5}\ \mathrm{psi}$
- $E_{v,\text{water},\,20^\circ\mathrm{C}} = 2.19 \times 10^{9}\ \mathrm{N/m^2}$
### Definitions
- Specific volume $\nu := \frac{1}{\rho}$
- Specific weight $\gamma:=\rho g$
- Specific gravity $\text{SG}:= \frac{\rho}{\rho_{w,\,4^\circ\mathrm{C}}}$
- Bulk modulus $E_{v}:= -\frac{dp}{\frac{dV}{V}}=\frac{dp}{\frac{d\rho}{\rho}}$
- Knudsen number: $Kn = \frac{\lambda}{l}$. If $Kn\ll1$, continuum assumption is valid.
- Mach number $Ma:=\frac{u}{c}$. If $Ma<0.3$, we can treat gases as incompressible.
- Dynamic viscosity $\mu:= \frac{\tau}{\frac{d \gamma}{dt}}$, whose unit is $Pa * s$
- Kinematic viscosity $\nu :=\frac{\mu}{\rho}$, whose unit is $m^{2}/s$
- Surface tension $\sigma \, (F/m)$ 
### Equations
- Ideal gas: $pV=nR_{u}T$ and $p=\rho RT = \frac{\rho R_{u} T}{M}$
- Speed of sound: $c=\sqrt{\frac{dp}{d \rho}}=\sqrt{\frac{E_{v}}{\rho}}=\sqrt{kRT}$
- Stress decomposition: $\sigma = -pI+\tau$
- Pressure: $p=-\frac{1}{3}\mathrm{Tr}(\sigma)$
- Newton’s law of viscosity: $\tau_{ij} = \mu (\frac{\partial u_{i}}{x_{j}} + \frac{\partial u_{j}}{x_{i}})$
- Young–Laplace equation: $p_{i}-p_{o}=\sigma (\frac{1}{r_{1}}+\frac{1}{r_{2}})$
![[Pasted image 20260205004425.png]]
- Non-flowing fluid: $-\nabla p + \rho \vec{g} = \rho \vec{a}$
![[Pasted image 20260205010053.png]]
- $F_R=\rho g\sin\theta y_C A$