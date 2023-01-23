#!/usr/bin/env python
# coding: utf-8

# # Week 3 - Exercise

# ## Problem Statement

# Compute the total membrane area necessary to produce 10 l/h purified water (0.03 wt% NaCl) through a single stage Reverse Osmosis separation of seawater (water 4 wt% NaCl). 
# The feed pressure is 100 bar and the composition in the retentate stream is 7 wt%.  
# The permeate stream is at ambient pressure (1 bar), all streams are at 25$^o$ C, and the osmotic pressure in bar is captured by the semiempirical expression: 
# 
# $$
# \pi=\frac{1.12}{14.5}T\sum_{i=1}^Nc_i
# $$
# 
# Where T is the temperature in K,  $N$ is the total number of ionic species in solution, and ci is the concentration expressed in $[mol/l]$. 
# 
# The asymmetric membrane used for the separation has a permeance of $10^{-5}\,[m h^{-1} bar^{-1}]$.
# 
# Once you have solved the problem consider the following questions:
# 
# - Can you evaluate the salt rejection in this process, and salt passage? 
# - How would you modify the operation of the system to increase the productivity of the process? 
# 

# ## Solution trace
# 
# __Data:__
# 
# NaCl weigth percentage:<br>
# $w_{NaCl,P}=0.03$<br>
# $w_{NaCl,F}=4$<br>
# $w_{NaCl,R}=7$<br>
# 
# __Water density:__ 
# $\rho_{H_2O}$=1$\times$10$^3$ [g/l]<br>
# 
# __Working expression:__
# 
# $$
# c_{NaCl,i}=\frac{w_{NaCl,i}}{100}\times\frac{\rho_{Solution,i}}{MM_{NaCl}}
# $$
# 
# Where: $i$ indicates the stream we are referring to, $\rho_{Solution,i}$  is the mass density of the NaCl solution in each stream, and $MM_{NaCl}$ is the molar mass of NaCl. <br>
# The mass density of the solution $\rho_{Solution}$ can be computed known the NaCl weight percentage and the density of  water as: 
# 
# $$
# \rho_{solution}=\frac{\rho_{H_2O}}{1-\frac{w_{NaCl,i}}{100}}
# $$
# 
# __Computing the Osmotic pressure difference across the membrane__<br>
# The expression provided in the exercise assignment allows to compute the osmotic pressure associated with an assigned concentration of NaCl in a solution of assigned NaCl concentration. 
# _Note that the concentration appearing in such expression is the total ionic concentration, which can be computed from the NaCl concentration knowing the unit formula of NaCl._ 
# 
# $$
# c_{TOT,i}=c_{Na^+,i}+c_{Cl^-,i}=2c_{NaCl,i}
# $$
# 
# Note that in this case it is typically reasonable to assume the concentration on the feed/retentate side of the membrane to be the average between concentrations in the feed and retentate.
# 
# $$
# c_{TOT,F/R}=2 \left({\frac{c_{NaCl,F}+c_{NaCl,R}}{2}}\right)
# $$
# 
# Alternatively one can consider the feed/retentate side to be perfectly mixed and its composition constant and equal to the retentate one.
# 
# The difference in the osmotic pressure can thus be computed as: 
# 
# $$
# \Delta{\pi}=\frac{1.12}{14.5}T\left(c_{TOT,F/R}-c_{TOT,P}\right)
# $$
# 
# __Computing the membrane area__<br>
# The flow rate through the membrane is computed by the expression:
# 
# $$
# F_{p,wat}=J\times{A}=A\,P_{wat}\,\left(\Delta{P}-\Delta{\pi}\right)
# $$
# 
# hence: 
# 
# $$
# A=\frac{F_{p,wat}}{P_{wat}\,\left(\Delta{P}-\Delta{\pi}\right)}
# $$
# 
# __Salt rejection__<br>
# Given the concentrations computed earlier salt rejection can be computed from its definition:
# 
# $$
# R_s=1-\frac{c_{NaCl,P}}{c_{NaCl,R}}
# $$
# 
# Salt passage is given by:<br> 
# 
# $$
# P_s=\frac{c_{NaCl,P}}{c_{NaCl,R}}
# $$

# In[1]:


import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.pyplot import cm

#
PM=1E-5; #[m/h/bar]
MMNaCl=58.5; #[g/mol]

#Feed Retentate Permeate
wtp=np.array([4, 7, 0.03])/100; #mass fractions
water_density=1E3; #[g/l]

c=wtp*water_density/(MMNaCl*(1-wtp));  #[mol/l]

C=1.12/14.5;
T=298;
pi_P=2*C*T*c[2];
pi_R=2*C*T*np.mean(c[0:2]);
Dpi=pi_R-pi_P; # [bar]

DP=100-1; # [bar]
Fpwat=10E-3; # [m3/h]

A=Fpwat/PM/(DP-Dpi)

SP=c[2]/c[1]
SR=(1-SP)

print("\nPermeate concentration: ", f"{c[2]:.4}", " [mol/l]")
print("Feed concentration: ", f"{c[0]:.4}", " [mol/l]")
print("Retentate concentration: ", f"{c[1]:.4}", " [mol/l]")

print("\nOsmotic pressure: ", f"{Dpi:.4}", " [bar]")

print("\nMembrane area: ", f"{A:.4}", " [m^2]")
print("Salt rejection: ", f"{SR:.4}", "[-]")
print("Salt passage: ", f"{SP:.2}", "[-]")


# ## Contributions
# 
# Debugged by Nikita Gusev, 29 Jan 2021 

# In[ ]:




