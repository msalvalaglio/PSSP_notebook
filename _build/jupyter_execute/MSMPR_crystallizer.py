#!/usr/bin/env python
# coding: utf-8

# # 10. MSMPR Crystallizer: population balance 

# Let us consider an Mixed Suspension Mixed Product removal crystallizer operating at steady state at constant temperature. 
# In these notes we will derive the analystical expression of the steady state particle size distribution by introducing a monodimensional population balance, and we will discuss its coupling with the global material balance.
#          

# ## 10.0 Material Balance
# 
# Let us begin by considering the global material balance for an MSMPR crystallizer. The operation of an ideal MSMPR crystallizer is characterised by the following set of hypotheses: 
# 
# - The crystalliser operates continuously
# - Operation is at steady state
# - The crystalliser is perfectly mixed (both with respect to the liquid and the solid phases)
# - The outlet has a composition identical in all respects to the crystallizer content
# - There are no crystals in the feed
# - The growth rate G=dL/dt is independent from the crystal size (L)
# - All crystals have the same shape
# - The system is not subject to agglomeration or breakage
# 
# At steady state the mass balance for the solute precipitating in an MSMPR crystallizer can be written as: 
# 
# $$
# Q_{IN}C_{IN}=Q_{OUT}C_{OUT}+Q_{OUT}M_T
# $$(MSMPReq0)
# 
# where $Q_{IN}$ is the volumetric inlet flowrate of the liquid phase, $Q_{OUT}$ is the volumetric outlet flowrate of the liquid phase (mother liquor), $C_{IN}$ is the solute density in the feed, $C_{OUT}$ is the solute density int he outlet stream, and $M_T$ is the mass of crystals precipitated per unit volume of liquid phase. 
# Typically $Q_{IN}\simeq{Q_{OUT}}=Q$ and thus $M_T=C_{IN}-C_{OUT}$. 
# 
# It should be noted that $M_T$ is determined by the process of precipitation producing a certain particles population and can be computed from the kinetics of crystal nucleation and growth, based on the population balance discussed in the next section. 
# 
# 

# ## 10.1 Number and number population density

# Let us begin by defining $N(L)$ as the __number__ of  crystals of characteristic length $L$ per unit volume. 
# The __number population density__ $n$, or in short number density, is defined as: 
# 
# $$
# \lim_{\Delta{L}\to{0}}\frac{\Delta{N(L)}}{\Delta{L}}=\frac{d{N(L)}}{d{L}}=n(L)
# $$(MSMPReq1)
# 
# and represents the number of crystals of length $L$ __per unit length__, per unit volume. 
# The number of crystals per unit volume with dimension comprised between $L_1$ and $L_2$ can thus be computed as a definite integral of the population density: 
# 
# $$
# N_{1,2}=\int_{L_1}^{L_2}n(L)dL
# $$(MSMPReq2)
# 
# Similarly the total number of crystals per unit volume is obtained as: 
# 
# $$
# N_{T}=\int_{0}^{\infty}n(L)dL
# $$(MSMPReq3)

# ## 10.2 Population Balance in an MSMPR crystallizer

# Let us write a steady state population balance for particles with size comprised between $L_1$ and $L_2$. 
# 
# $$
# {\Delta{N}}V=n_1G_1V\Delta{t}-n_2G_2V\Delta{t}-Q\overline{n}\Delta{L}\Delta{t}
# $$(MSMPReq4)
# 
# where $\Delta{N}V$ is the change in the number of particles within the length interval $\Delta{L}=L_2-L_1$ per unit volume, accumulated in time $\Delta{t}$. 
# The term $n_1G_1V\Delta{t}$ captures the number of crystals that outgrow length $L_1$ in time $\Delta{t}$, where $G_1$ is the growth rate of particles of length $L_1$, $V$ is the total volume. 
# Similarly, the term $n_2G_2V\Delta{t}$ takes into account particles leaving the length  interval $\Delta{L}$, outgrowing length $L_2$. 
# Finally the term $Q\overline{n}\Delta{L}\Delta{t}$ accounts for the removal of particles with size comprised in  $\Delta{L}$ from the crystalliser due to the magma flowrate with volumetric flowrate $Q$, where $\overline{n}$ represents the average population density within the length interval $\Delta{L}$.  
# 
# Eq. {eq}`MSMPReq4` can be rearranged to obtain on the left side a discrete accumulation term, i.e. the number of particles with size compriused in $\delta{L}$ accumulated in time $\Delta{t}$:
# 
# $$
# \frac{\Delta{N}}{\Delta{t}}=n_1G_1-n_2G_2-\frac{Q}{V}\overline{n}\Delta{L}
# $$(MSMPReq5)
# 
# At steady state there is no accumulation and Eq. {eq}`MSMPReq5` can be rewritten as:
# 
# $$
# \frac{n_2G_2-n_1G_1}{\Delta{L}}=-\frac{Q}{V}\overline{n}
# $$(MSMPReq6)
# 
# Noting that the residence time $\tau=V/Q$, and taking the limit for $\Delta{L}\rightarrow{0}$ we get: 
# $$
# \frac{dn}{dL}=\frac{n}{G\tau}
# $$(MSMPReq7)
# 
# Whic can be solved analytically, yielding the steady state number population density n(L): 
# 
# $$
# n(L)=n_0\exp\left(-\frac{L}{G\tau}\right)
# $$(MSMPReq8)
# 
# where $n_0$ is an integration constant, determined from the boundary conditions, that has the physical meaning of population density of nuclei in the crystallizer at steady state. 
# 
# In this formulation of the population balance we consider particles to be born as nuclei at length $L=0$. 
# The nucleation rate $J$, i.e. the number of nuclei generated per unit time per unit volume can be written as: 
# 
# $$
# J={\frac{dN}{dt}}\vert_{L=0}
# $$(MSMPReq9)
# 
# by applying the chain rule we can rewrite the nucleation rate as: 
# 
# $$
# J=\frac{dN}{dL}\vert_{L=0}\frac{dL}{dt}\vert_{L=0}=n_0G
# $$(MSMPReq10)
# 
# where, by definition $\frac{dN}{dL}\vert_{L=0}=n_0$, and $\frac{dL}{dt}=G$. We shall note that here we are considering the growth rate to be independent from the crystal size. 
# 
# This expression allows us to determine the integration constant $n_0$ based on characteristic rates of crystal nucleation and growth, yielding:
# 
# $$
# n_0=\frac{J}{G}
# $$(MSMPReq11)

# ## 10.3 Particle size distribution and process parameters: $\tau$, $G$, $J$

# In[1]:


import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.pyplot import cm

#Plotting
figure=plt.figure()
axes = figure.add_axes([0.1,0.1,1.2,1.2])
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

# Data
G=1
J=1
tau=np.array([0.1, 1, 2, 5, 10, 50, 100, 500]);
N = 500 #number of points
L = np.linspace(0,100, N)

color=iter(cm.coolwarm(np.linspace(0,1,np.size(tau))))

for i in range(0,np.size(tau)):     
    c=next(color)
    n= J / G * np.exp(-L/G/tau[i])
    axes.plot(L,n, marker=' ' , c=c)    
    
plt.title('n(L) vs. residence time', fontsize=18);
axes.set_xlabel('$L$', fontsize=18);
axes.set_ylabel('$n$',fontsize=18);

#########################################################
# Plotting
figure=plt.figure()
axes = figure.add_axes([0.1,0.1,1.2,1.2])
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

# Data
G=np.array([1, 2, 5, 10, 50, 100, 500]);
J=1;
tau=5;
N = 500 #number of points
L = np.linspace(0,50, N);

color=iter(cm.coolwarm(np.linspace(0,1,np.size(G))));

for i in range(0,np.size(G)):     
    c=next(color)
    n= J / G[i] * np.exp(-L/G[i]/tau)
    axes.plot(L,n, marker=' ' , c=c)    
    
plt.title('n(L) vs. growth rate', fontsize=18);
axes.set_xlabel('$L$', fontsize=18);
axes.set_ylabel('$n$',fontsize=18);


#########################################################
# Plotting
figure=plt.figure()
axes = figure.add_axes([0.1,0.1,1.2,1.2])
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

# Data
G=1;
J=np.array([1, 2, 5, 10, 50, 100, 500]);
tau=5;
N = 500 #number of points
L = np.linspace(0,50, N);

color=iter(cm.coolwarm(np.linspace(0,1,np.size(J))));

for i in range(0,np.size(J)):     
    c=next(color)
    n= J[i] / G * np.exp(-L/G/tau)
    axes.plot(L,n, marker=' ' , c=c)    
    
plt.title('n(L) vs. nucleation rate', fontsize=18);
axes.set_xlabel('$L$', fontsize=18);
axes.set_ylabel('$n$',fontsize=18);


# ## 10.4 Moments of the PSD in a MSMPR crystallizer

# The number population density $n(L)$ can be used to derive other properties of the population of particles through the calculation of the moments of the distribution. 
# The $i^{th}$ order moment of the number population density is defined as: 
# 
# $$
# m_i=\int_0^{\infty}L^indL
# $$(MSMPReq12)
# 
# Based on this definition we note that the moments from order 0 to 3 have a well defined physical meaning: 
# 
# - $m_0=\int_0^{\infty}L^0ndL=N_L$ represents the number of particles per unit volume of liquid phase  with size smaller or equal than size L. For $L\rightarrow{\infty}$ $N_L$ tends to the total number of particles per unit volume of liquid phase in the crystallizer: 
# 
# $$
# N_T=n_0G\tau
# $$(MSMPReq13)
# 
# - $m_1=\int_0^{\infty}L^1ndL=\mathcal{L}$ represents the total length of particles per unit volume of liquid phase with size smaller or equal than size $L$. For $L\rightarrow{\infty}$, $\mathcal{L}$ tends to the total length of particles per unit volume of liquid phase in the crystallizer: 
# 
# $$
# \mathcal{L}_T=n_0(G\tau)^2
# $$(MSMPReq14) 
# 
# - $m_2=\int_0^{\infty}L^2ndL\propto{A}$ is proportional to the total area of particles per unit volume of liquid phase with size smaller or equal than size $L$. For $L\rightarrow{\infty}$, $A$ tends to the total area of the particles per unit volume of liquid phase contained in the crystallizer: 
# 
# $$
# A_T=2{\beta}n_0(G\tau)^3
# $$(MSMPReq15) 
# 
# where $\beta$ is the surface shape factor of the particles. 
# 
# - $m_3=\int_0^{\infty}L^3ndL\propto{V}$ is proportional to the total volume of particles with size smaller or equal than size $L$. For $L\rightarrow{\infty}$, $V$ tends to the total volume of the particles per unit volume contained in the crystallizer: 
# 
# $$
# V_T=6{\alpha}n_0(G\tau)^4
# $$(MSMPReq16)
# 
# where $\alpha$ is the volumetric shape factor of the particles.
# 
# 
# It should be noted that the total volume of the particles per unit volume of liquid phase allows to compute the total mass of particles per unit volume of liquid phase in the system: 
# 
# $$
# M_T=\rho_c{V_T}=6\rho_c{\alpha}n_0(G\tau)^4
# $$(MSMPReq17)
# 
# where $\rho_c$ is the density of the crystalline phase. 
# 
# This expression for $M_T$ allows to couple the population balance and the gobal material balance in an MSMPR crystallizer since $M_T=C_{in}-C_{out}$, where $C_{in}$ and $C_{out}$ are the inlet and outlet concentrations of solute in the liquid phase. 
#  

# ## 10.5 Adimensional Mass distribution and dominant crystal size

# In order to obtain a general relationship between the crystallization process and an average indicator of the crystalline particles size obtained in an MSMPR crystallizer it is convenient to write the cumulative mass distribution in a dimensionless form. To this aim we introduce the dimensionless length $x=L/G\tau$, where $G$ is the growth rate and $\tau$ is the residence time. 
# 
# The cumulative mass distribution can thus be written as: 
# 
# $$
# M(x)=\frac{M}{M_T}=\frac{\int_0^{x}x^3\exp(-x)dx}{\int_0^{\infty}x^3\exp(-x)dx}=1-\left(1+x+\frac{1}{2}x^2+\frac{1}{6}x^3\right)\exp(-x)
# $$(MSMPReq18)
# 
# The corresponding mass population density is computed differentiating $M(x)$with respect to $x$: 
# 
# $$
# m(x)=\frac{dM(x)}{dx}=\frac{1}{6}x^3\exp(-x)
# $$(MSMPReq19)
# 
# The mass-based population density m(x) has a maximum for $x=3$, hence the most probable - often referred to as the modal or dominant particle size can be computed as: 
# 
# $$
# L_D=3G\tau
# $$(MSMPReq20)

# In[2]:


import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.pyplot import cm

#Plotting
figure=plt.figure()
axes = figure.add_axes([0.1,0.1,1.2,1.2])
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

# Data
x = np.linspace(0,20, N)

color=iter(cm.coolwarm(np.linspace(0,1,2)))
  
c=next(color)
M=1-(1+x+0.5*np.power(x,2)+1/6*np.power(x,3))*np.exp(-x)
axes.plot(x,M, marker=' ' , c=c) 
c=next(color)
m=1/6*np.power(x,3)*np.exp(-x)
axes.plot(x,m, marker=' ' , c=c)    
axes.plot(np.array([3,3]),np.array([0, 1/6*np.power(3,3)*np.exp(-3)]),'--',)

axes.set_xlabel('$x$', fontsize=18);
axes.set_ylabel('$M(x)/m(x)$',fontsize=18);
axes.legend(['M(x)','m(x)'], fontsize=18);


# ## Contributions
# 
# Guilherme Pizarro Werner, 23 February 2021
# 
# Ahmad Eblagh, 13 March 2021
