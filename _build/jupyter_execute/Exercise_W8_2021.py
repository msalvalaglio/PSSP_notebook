# Week 8 - Exercise

## Problem Statement 1

- In a system with two monotropic polymorphs, is it true that the polymorph with the lowest solubility is thermodynamically more stable?

- Can you demonstrate it using the definition of solubility? 

## Solution Trace 
_[contributed by Nikita Gusev, 9/March/2021]_

- Crystal polymorphs are defined as substances that are chemically identical but exist in more than one crystal form. A polymorphic transition is a reversible transition of a solid crystalline phase at a certain temperature and pressure (the inversion point) to another phase of the same chemical composition with a different crystal structure. 
For a monotropic system, plots of the solubility of the various polymorphs against temperature do not cross, meaning that different polymorphs always have different solubilities, and different stability.
Solution of a crystal is favored if the energy of dissolution is greater than the lattice energy, i.e., by dissolving, a compound forms a more thermodynamically stable state. In that sense, if the solubility of a polymorph is greater, means that this polymorph is less stable in its
crystalline state, and vice versa, the polymorph with the lowest solubility is thermodynamically more stable in its crystalline state.

- The chemical potential of a solid crystalline phase is given by:

$$
\mu_{i}^s\simeq\mu_0+RT\ln{x_i^*}
$$

where $x_i^*$ is the solubility.

From the equation above it can be seen than the lower is the solubility, the lower is the chemical potential and we know that the phase with the lowest chemical potential at any temperature is the most stable phase at that temperature. This again shows that a less soluble polymorph is more stable.



## Problem Statement 2
An aqueous feed of 10000 kg h$^{-1}$, saturated with $BaCl_2$ at 100$^o$C, enters a crystallizer that can be simulated with the MSMPR model. The slurry leaves the crystallizer at 20$^o$C with crystals of the dihydrate. The crystallizer has a volume of 2.0 $m^3$. From laboratory experiments, the crystal growth rate is essentially constant at $4.0\times{10^{-7}}$ m/s. The solubility of $BaCl_2$ is 58.3 g/100 g water at 100$^o$ C and 35.7 g/100 g water at 20$^o$ C. The molar mass of $BaCl_2$ is 208.27 g/mol, the the dihydrate, $BaCl_22H_2O$ has a molar mass of 244.31 g/mol. The density of the crystals is 3097 $kg/m^3$, the density of the solution in the crystallizer is 1279 $kg/m^3$ 

- Determine the mass flow rate of crystals in the product stream.
- Compute the predominant crystal size $L_D$ in mm.

## Solution Trace
_[Nikita Gusev and Guilherme Pizarro Werner, 9/March/2021]_

A total material balance around the crystallizer (assuming steady state):

$$
F=V+L+S
$$
where: 
- $F$ = total feed rate (kg/h) 
- $V$ = evaporation rate
- $L$ = Liquid phase flow rate kg/h of liquid
- $S$ = Crystals flow rate kg/h of crystals

Assuming evaporation is negligible and rearranging for $L$:

$$L=F-S$$ 

Material balance for $BaCl_2$:

$$
x_F{F} = x_LL + x_SS
$$

- where $x_F$, $x_L$, $x_S$ are the mass fractions of $BaCl_2$ in feed, liquid and crystals, respectively.

F is known, and mass fractions can be found from the data, so we have two equations and two unknowns (L and S), and so there is 0 degrees of freedom and the problem can be solved.

Solving simultaneously using the expressions above:

$$
x_FF= x_L(F - S) + x_SS
$$

Rearranging:

$$
S = F \frac{x_F-x_L}{x_S-x_L}
$$


Now finding the mass fractions:

$$
x_{F,L}=\frac{w_{F,L}}{w_{F,L} + 100}
$$

where $w_{F,L}$ is the solubility mass of solute per 100 g of water. 

$$
x_S=\frac{MM_{BaCl_2}}{MM_{BaCl_22H_2O}}
$$

## Solution trace
# Variables
wF=58.3 #g/100 g water 
wL=35.7 #g/100 g water 
MMBaCl2= 208.27 #g/mol
MMBaCl22H2O=244.31 #g/mol
F=1E4 #kg/h


xF=wF/(wF+100);
xL=wL/(wL+100);
xS=MMBaCl2/MMBaCl22H2O;

S=F*(xF-xL)/(xS-xL)

L=F-S

print("\nFeed mass fraction ", f"{xF:.4}", " [-]")
print("Liquid phase mass fraction ", f"{xL:.4}", "[-]")
print("Crystal mass fraction ", f"{xS:.4}", "[-]")
print("Crystals flowrate: ", f"{S:.4}", " [kg/h]")
print("Liquid phase flowrate: ", f"{L:.4}",  " [kg/h]")

The modal or dominant particle size can be computed as:

$$
L=3G\tau
$$

where:

- $\tau$ = average residence time 
- $G$ = growth rate

We need to find the average residence time:

$$
\tau = \frac{V}{Q} 
$$

where:

- $V$  = volume of the crystallizer 
- $Q$  = outlet volumetric flowrate 

But first we need to calculate the outlet volumetric flowrate:

$$
Q=\frac{S}{\rho_S}+\frac{L}{\rho_L}
$$

## Solution trace
# Variables
rho_C=3097 
rho_L=1290
V=2 #m3
G=4E-7 #m/s

Q=L/rho_L+S/rho_C #m3/h

tau=V/Q*3600 #s

LD=3*G*tau*1E3 #mm

print("\nThe volumetric flowrate ", f"{Q:.4}", "[m3/h]")
print("The residence time ", f"{tau:.4}", "[s]")
print("The predominant crystal size is ", f"{LD:.4}", " [mm]")