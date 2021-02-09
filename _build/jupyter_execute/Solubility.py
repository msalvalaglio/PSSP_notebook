# 9. Solubility

Let us begin by writing the solid-liquid equilibrium conditions at temperature $T$ and pressure $P$, between a pure crystalline phase and a multicomponent liquid phase characterised by composition $\vec{x}$. 
Equilibrium conditions is stated by the equality of chemical potentials: 

$$
\mu_i^s(T,P)=\mu_i^\ell(T,P,\vec{x})
$$(SOLeq1)

which is equivalent to the equality of the fugacity in the two phases: 

$$
f_i^s(T,P)=f_i^\ell(T,P,\vec{x})
$$(SOLeq2)

Focusing on the right hand of Eq. \eqref{eq:fugacities}, the fugacity in the liquid phase can be rewritten as a function of the fugacity of the pure liquid phase as follows:

$$
f_i^\ell(T,P,\vec{x})=f_i^\ell(T,P)x_i\gamma_i(T,P,\vec{x})
$$(SOLeq3)

where $x_i$ is the molar fraction of the solute and $\gamma_i(T,P,\vec{x})$ is the activity coefficient of that specie in the liquid phase.  

Let us now focus on the left hand side of Eq. {eq}`eq2`. The fugacity of the pure solid phase can also be written as a function of the fugacity of the pure liquid: 

$$
\int^{T,P,s}_{T,P,\ell}d\mu_i=\int^{T,P,s}_{T,P,\ell}RTd\ln{f_i}
$$(SOLeq4)

$$
\Delta{\mu}_{i,\ell\rightarrow{s}}=RTln\left(\frac{f_i^s(T,P)}{f_i^\ell(T,P)}\right)
$$(SOLeq5)

$$
f_i^s(T,P)=f_i^\ell(T,P)e^{\frac{\Delta{\mu}_{i,\ell\rightarrow{s}}}{RT}}
$$(SOLeq6)

The change in chemical potential can be written for a pure substance as the partial molar change in free energy $\Delta{g_i(T,P)}$:

$$
\Delta\mu_{i,\ell\rightarrow{s}}=\Delta{g}_i^s(T,P)=\Delta{h}_i(T,P)-T\Delta{s}_i(T,P)
$$(SOLeq7)


The molar enthalpy change is: 

$$
\Delta{h}_i(T,P)=-\Delta{h_{fus}\left(T_f\right)}+\int_T^{T_f}Cp^{\ell}dT+\int_T^{T_f}Cp^{s}dT\simeq-\Delta{h_{fus}\left(T_f\right)}+\left(Cp^{\ell}-Cp^{s}\right)\left(T_f-T\right)
$$(SOLeq8)

while the molar entropy change is written as: 

$$
\Delta{s}_i(T,P)=-\frac{\Delta{h_{fus}\left(T_f\right)}}{T_f}+\int_T^{T_f}\frac{Cp^{\ell}}{T}dT+\int_T^{T_f}\frac{Cp^{s}}{T}dT \simeq -\frac{\Delta{h_{fus}}}{T_f}+\left(Cp^{\ell}-Cp^{s}\right)\ln{\left(\frac{T_f}{T}\right)}
$$(SOLeq9)

Defining $\Delta{Cp}_{\ell\rightarrow{s}}=\left(Cp^{\ell}-Cp^{s}\right)$

$$
\Delta{g}_i^s(T,P)=-\Delta{h_{fus}\left(1-\frac{T}{T_f}\right)}+\Delta{Cp}_{\ell\rightarrow{s}}\left(T_f-T-T\ln{\left(\frac{T_f}{T}\right)}\right)
$$(SOLeq10)

Since $\Delta{Cp}_{\ell\rightarrow{s}}$ is usually small compared the above expression is typically simplified to: 

$$
\Delta{g}_i^s(T,P)\simeq-\Delta{h_{fus}\left(1-\frac{T}{T_f}\right)}
$$(SOLeq11)

Inserting this equation into the equality of fugacities yields:

$$
f_i^\ell(T,P)x_i\gamma_i(T,P,\vec{x})=f_i^\ell(T,P)e^{\frac{\Delta{\mu}_{i,\ell\rightarrow{s}}}{RT}}
$$(SOLeq12)

hence the solubility of component $i$, $x_i$ is:  

$$
x_i=\frac{1}{\gamma_i(T,P,\vec{x})}e^{-\frac{\Delta{h_{fus}}}{R}\left(\frac{1}{T}-\frac{1}{T_f}\right)}
$$(SOLeq13)