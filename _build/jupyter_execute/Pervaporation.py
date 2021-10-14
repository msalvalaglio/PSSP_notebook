# 2. Pervaporation

## 2.1 Vapour-Liquid Equilibrium in a Pervaporation unit

In pervaporation processes the feed/retentate is liquid, while the permeate is in the vapour phase. 
In this process, evaporation and permeation of different chemical through a semipermeable membrane take place simultaneously.    

In order to tame the complexity of the processes taking place in this unit, a typical modelling assumption is that Vapour liquid equilibrioum is established on the feed retentate side and permeation through the membrane takes place in the vapour phase.  

Hence, pervaporation can be treated as a gas permeation problem by introducing a _virtual vapour phase_ in equilibrium with the liquid on the retentate side of the membrane. 

The driving force for a specie $i$ can thus be written as the difference in the partial pressure for component $i$ in this virtual vapour phase, and in the real vapour phase on the permeate side. 

## 2.2 Vapour-Liquid Equilibrium conditions

To express the partial pressure of component $i$ in a vapour phase in equilibrium with the liquid on the retentate side we shall begin by expressing the fundamental condition that has to be fulfilled by all species at thermodynamic equilibrium: 

$$
\mu_i^L(T,P,\vec{x})=\mu_i^V(T,P,\vec{y})
$$(PVAPeq:fund)

where $\mu_i^L(T,P,\vec{x})$ and $\mu_i^V(T,P,\vec{y})$ are the chemical potentials for specie $i$ in the liquid and vapour phase, respectively. 

For mixtures of ideal gases the chemical potential is conveniently expressed in differential form as a function of the partial pressure of component $i$, $p_i$ as $d\mu_i=RTd\ln{p_i}$.  
In analogy with this expression in the case of real gases fugacity $f_i$ is introduced, leading to the differential expression $d\mu_i=RTd\ln{f_i}$. 
Integrating this expression between the phases in equilibrium yields: 

$$
\int_{L,T,P,\vec{x}}^{V,T,P,\vec{y}}d\mu_i=\int_{L,T,P,\vec{x}}^{V,T,P,\vec{y}}RTd\ln{f_i}
$$
$$
\mu_i^V(T,P,\vec{y})-\mu_i^L(T,P,\vec{x})=RT\ln\frac{f_i^V(T,P,\vec{y}}{f_i^L(T,P,\vec{x})}
$$(PVAPeq:chempot)


Hence, the equilibrium condition expressed by Eq. {eq}`PVAPeq:fund` can be conveniently stated as: 

$$
f_i^V(T,P,\vec{y})=f_i^L(T,P,\vec{x})
$$(PVAPeq:EQUI)

The left-hand term can be written as: 

$$
f_i^V(T,P,\vec{y})=\phi(T,P,\vec{y})Py_i
$$(PVAPeq:vapour)

where $\phi(T,P,\vec{y})$ is the fugacity coefficient, $P$ the pressure and $y_i$ the molar fraction in the vapour phase. 

The right hand side term can instead be written as: 

$$
f_i^L(T,P,\vec{x})=\gamma_i(T,P,\vec{x})x_i\phi(T,P^o(T))P^o(T)e^{\frac{v_i(P-P^o(T))}{RT}}
$$(PVAPeq:liquid)

where $x_i$ is the molar fraction of component $i$ in the liquid phase, $\gamma_i(T,P,\vec{x})$ is the activity coefficient for component i in the liquid mixture, $P^o(T)$ is the equilibrium vapour pressure of the pure component $i$, $\phi(T,P^o(T))$ is the fugacity coefficient for the pure component $i$ at $T$ and $P^o(T)$, and the term $e^{\frac{v_i(P-P^o(T))}{RT}}$ is the Poynting correction. For a discussion on the origin of the Poynting correction please refer to the notes on osmosis. 

Introducing Eq.{eq}`PVAPeq:vapour` and Eq. {eq}`PVAPeq:liquid` in Eq.{eq}`PVAPeq:EQUI`, while considering negligible the Poynting correction, and ideal gas approximation applicable yields: 

$$
Py_i=\gamma_i(T,P,\vec{x})P^o(T)x_i
$$(PVAPeq:final)

It should be noted that introducing the further hypothesis of ideal liquid mixture yields the Raoult law: 

$$
Py_i=P^o(T)x_i
$$(PVAPeq:Raoult)


## 2.3 Flux Equation in a pervaporation Unit

Considering now a binary mixture of components $i$ and $j$, the flux equation for species $i$ in a pervaporation unit is: 

$$
J_i=\frac{P_i}{l}\left(\gamma_i(T,P,\vec{x})x^r_ip_i^o(T)-p_py^p_i\right)
$$(PVAPeq:flux)

where $P_i$ is the permeability of species $i$ through the membrane, $l$ the thickness of the membrane, $\gamma_i(T,P,\vec{x})x^r_ip_i^o(T)$ is the partial pressure in the virtual vapour phase in equilibrium with the liquid on the retentate side, $p_p$ the pressure on the permeate side, and $y^p_i$ the molar fraction of component $i$ in the real vapour phase on the permeate side.

The flux equation of component $j$ can be expressed as a function of the molar fractions of component $i$ taking advantage of the stoichiometric constraints $\sum_{i=1}^{N}x^r_i=1$, $\sum_{i=1}^{N}y^p_i=1$. 

$$
J_j=\frac{P_j}{l}\left(\gamma_j(T,P,\vec{x})(1-x^r_i)p_j^o(T)-p_p(1-y^p_i)\right)
$$(PVAPeq:flux2)

