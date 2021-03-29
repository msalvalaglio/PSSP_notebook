# Week 11 - Exercise

## Problem Statement

Water (density 1000 kg m$^{-3}$, viscosity 1 mN s m$^{-2}$) is used to fluidise a bed of packed spheres characterised by a diameter of 0.5 mm and a density of 1500 kg m$^{-3}$.

### Tasks
- Demonstrate that, in laminar regime, the minimum fluidization velocity is alway smaller than the terminal falling velocity. 
- Compute the minimum fluidisation velocity and the terminal falling velocity of the bed particles.
- Sketch a plot of the $\Delta{P}$ as a function of the fluid velocity, clearly indicating the minimum fluidisation velocity.
- How would your result change if particles were twice as large?
- What does the terminal falling velocity represent in the context of fluidisation? 

### Solution


In the laminar regime, for spherical particles of diameter $d$ the minimum fluidization velocity is given by: 

$$
v_{mf}=\frac{1}{180}\frac{e^3}{(1-e)}\frac{d^2(\rho_s-\rho_f)g}{\mu}
$$

where, $e$ is the void fraction, $d$ the diameter of the particles, $\rho_s$ is the density of the particles,  $\rho_f$ is the density of the fluidising fluid, $g$ is the gravity acceleration constant, and $\mu$ the viscosity of the fluid. 

The terminal falling velocity, conversely is determined by the steady state force balance on a single particle: 

$$
v_t^2=Cd^{-1}\frac{(\rho_s-\rho_f)}{\rho_f}\frac{4d}{3}g
$$

where $Cd$ is the drag coefficient. 

If we introduce the definition of the drag coefficient in laminar regime given by the Stokes relation: 

$$
Cd=\frac{24}{Re_p}=\frac{24\mu}{\rho_fdv}
$$

where $Re_p$ is the Reynolds number and $v$ the velocity of the fluid, we get: 

$$
v_t=\frac{\rho_fd}{24\mu}\frac{(\rho_s-\rho_f)}{\rho_f}\frac{4d}{3}g=\frac{1}{18}\frac{d^2(\rho_s-\rho_f)g}{\mu}
$$

Now, if we take the ratio between $v_{mf}$ and $v_t$ we get: 


$$
\frac{v_{mf}}{v_t}=\frac{\frac{1}{180}\frac{e^3}{(1-e)}\frac{d^2(\rho_s-\rho_f)g}{\mu}}{\frac{1}{18}\frac{d^2(\rho_s-\rho_f)g}{\mu}}=\frac{1}{10}\frac{e^3}{(1-e)}
$$

Since the void fraction $0<e<1$ by definition, with a lower theoretical limit at $\approx{0.36}$ (corresponding to a close-packing of equal spheres),  the term $\frac{e^3}{(1-e)}$ is dof order $e^2$ and smaller than 1. 

Hence 
$$
\frac{v_{mf}}{v_t}<1
$$

and the minimum fluidization velocity is always smaller than the terminal Falling velocity, irrespective of $d$, $\rho_p$, $\rho_f$ or $\mu$.



import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.pyplot import cm

dens_fluid=1000 #
dens_particles=1500



