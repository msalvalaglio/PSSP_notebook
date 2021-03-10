# Week 8 - Exercise

## Problem Statement 1

- In a system with two monotropic polymorphs, is it true that the polymorph with the lowest solubility is thermodynamically more stable?

- Can you demonstrate it using the definition of solubility? 

## Solution

#### Contributed by Nikita Gusev, on 9/March/2021

- Crystal polymorphs are defined as substances that are chemically identical but exist in more than one crystal form. A polymorphic transition is a reversible transition of a solid crystalline phase at a certain temperature and pressure (the inversion point) to another phase of the same chemical composition with a different crystal structure. 
For a monotropic system, plots of the solubility of the various polymorphs against temperature do not cross, meaning that different polymorphs always have different solubilities, and different stability.
Solution of a crystal is favored if the energy of dissolution is greater than the lattice energy, i.e., by dissolving, a compound forms a more thermodynamically stable state. In that sense, if the solubility of a polymorph is greater, means that this polymorph is less stable in its
crystalline state, and vice versa, the polymorph with the lowest solubility is thermodynamically more stable in its crystalline state.

- The chemical potential of a solid crystalline phase is given by:
$$
\mu_{i}^s\simeq\mu_0+RT\ln{\x_i^*}
$$
where $$\x_i^*$$ is the solubility.
From the equation above it can be seen than the lower is the solubility, the lower is the chemical potential and we know that the phase with the lowest chemical potential at any temperature is the most stable phase at that temperature. This again shows that a less soluble polymorph is more stable.


## Problem Statement 2
An aqueous feed of 10000 kg h$^{-1}$, saturated with $BaCl_2$ at 100$^o$C, enters a crystallizer that can be simulated with the MSMPR model. The slurry leaves the crystallizer at 20$^o$C with crystals of the dihydrate. The crystallizer has a volume of 2.0 $m^3$. From laboratory experiments, the crystal growth rate is essentially constant at $4.0\times{10^{-7}}$ m/s. The density of the dihydrate crystals is 3.097 g cm$^{-3}$. The density of an aqueous, saturated solution of barium chloride at 20$^o$C is 1.29 g cm$^{-3}$. The solubility of $BaCl_2$ is 58.3 g/100 g water at 100$^o$ C and 35.7 g/100 g water at 20$^o$ C. The molar mass of $BaCl_2$ is 208.27 g/mol, the the dihydrate, $BaCl_22H_2O$ has a molar mass of 244.31 g/mol. The density of the crystals is 3097 $kg/m^3$, the density of the solution in the crystallizer is 1279 $kg/m^3$ 

- Determine the mass flow rate of crystals in the product stream.
- Compute the predominant crystal size $L_D$ in mm.

## Solution Trace

#### Contributed by Nikita Gusev and Guilherme Pizarro Werner, on 9/March/2021

A total material balance around the crystallizer (assuming steady state):
$$
F=V+L+S
$$

- where: $F$ = total feed rate (kg/h); $V$ = evaporation rate; $L$ = kg/h of liquid; and $S$ = kg/h of crystals.

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
𝑥% =
58.3 [𝑔 𝐵𝑎𝐶𝑙(]
(58.3 + 100) [𝑔 𝑠𝑜𝑙𝑢𝑡𝑖𝑜𝑛] = 0.3683 G
𝑔
𝑔 𝑠𝑜𝑙𝑢𝑡𝑖𝑜𝑛
H
𝑥& =
35.7 [𝑔]
(35.7 + 100) [𝑔 𝑠𝑜𝑙𝑢𝑡𝑖𝑜𝑛] = 0.2631 G
𝑔
𝑔 𝑠𝑜𝑙𝑢𝑡𝑖𝑜𝑛
H
𝑥' =
208.27 G 𝑔 𝐵𝑎𝐶𝑙(
𝑚𝑜𝑙 𝐵𝑎𝐶𝑙( ∙ 2𝐻(0H
244.31 G 𝑔 𝐵𝑎𝐶𝑙( ∙ 2𝐻(0
𝑚𝑜𝑙 𝐵𝑎𝐶𝑙( ∙ 2𝐻(0H
= 0.8525 G
𝑔 𝐵𝑎𝐶𝑙(
𝑔 𝐵𝑎𝐶𝑙( ∙ 2𝐻(0
H
Then we can calculate the mass flowrates:
𝑆 = 𝐹
(𝑥% − 𝑥&)
(𝑥' − 𝑥&) = 10000 G
𝑘𝑔
ℎ
H ∗
(0.3683 − 0.2631)
(0.8525 − 0.2631) = 1785
𝑘𝑔
ℎ
𝐿 = 10000 G
𝑘𝑔
ℎ
H − 1785 G
𝑘𝑔
ℎ
H = 8215
𝑘𝑔
ℎ


