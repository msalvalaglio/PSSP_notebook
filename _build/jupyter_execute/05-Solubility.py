# 5. Thermodynamic definition of solubility

Let us begin by writing the solid-liquid equilibrium conditions at temperature $T$ and pressure $P$, between a pure crystalline phase and a multicomponent liquid phase characterised by composition $\vec{x}$. 
Equilibrium conditions is stated by the equality of chemical potentials: 
\begin{equation}
\mu_i^s(T,P)=\mu_i^\ell(T,P,\vec{x})
{\tag{1}}
\end{equation}
which is equivalent to the equality of the fugacity in the two phases: 
\begin{equation}
f_i^s(T,P)=f_i^\ell(T,P,\vec{x})
\label{eq:fugacities}{\tag{2}}
\end{equation}
Focusing on the right hand of Eq. \eqref{eq:fugacities}, the fugacity in the liquid phase can be rewritten as a function of the fugacity of the pure liquid phase as follows:
\begin{equation}
f_i^\ell(T,P,\vec{x})=f_i^\ell(T,P)x_i\gamma_i(T,P,\vec{x})
\label{eq:solubility}{\tag{3}}
\end{equation}
where $x_i$ is the molar fraction of the solute and $\gamma_i(T,P,\vec{x})$ is the activity coefficient of that specie in the liquid phase.  

Let us now focus on the left hand side of Eq. \eqref{eq:fugacities}. The fugacity of the pure solid phase can also be written as a function of the fugacity of the pure liquid: 

\begin{equation}
\int^{T,P,s}_{T,P,\ell}d\mu_i=\int^{T,P,s}_{T,P,\ell}RTd\ln{f_i}
{\tag{4}}
\end{equation}

\begin{equation}
\Delta{\mu}_{i,\ell\rightarrow{s}}=RTln\left(\frac{f_i^s(T,P)}{f_i^\ell(T,P)}\right)
{\tag{5}}
\end{equation}

\begin{equation}
f_i^s(T,P)=f_i^\ell(T,P)e^{\frac{\Delta{\mu}_{i,\ell\rightarrow{s}}}{RT}}
{\tag{6}}
\end{equation}

The change in chemical potential can be written for a pure substance as the partial molar change in free energy $\Delta{g_i(T,P)}$:

\begin{equation}
\Delta\mu_{i,\ell\rightarrow{s}}=\Delta{g}_i^s(T,P)=\Delta{h}_i(T,P)-T\Delta{s}_i(T,P)
{\tag{7}}
\end{equation}


The molar enthalpy change is: 

\begin{equation}
\Delta{h}_i(T,P)=-\Delta{h_{fus}\left(T_f\right)}+\int_T^{T_f}Cp^{\ell}dT+\int_T^{T_f}Cp^{s}dT\simeq-\Delta{h_{fus}\left(T_f\right)}+\left(Cp^{\ell}-Cp^{s}\right)\left(T_f-T\right)
{\tag{8}}
\end{equation}

while the molar entropy change is written as: 

\begin{equation}
\Delta{s}_i(T,P)=-\frac{\Delta{h_{fus}\left(T_f\right)}}{T_f}+\int_T^{T_f}\frac{Cp^{\ell}}{T}dT+\int_T^{T_f}\frac{Cp^{s}}{T}dT \simeq -\frac{\Delta{h_{fus}}}{T_f}+\left(Cp^{\ell}-Cp^{s}\right)\ln{\left(\frac{T_f}{T}\right)}
{\tag{9}}
\end{equation}

Defining $\Delta{Cp}_{\ell\rightarrow{s}}=\left(Cp^{\ell}-Cp^{s}\right)$

\begin{equation}
\Delta{g}_i^s(T,P)=-\Delta{h_{fus}\left(1-\frac{T}{T_f}\right)}+\Delta{Cp}_{\ell\rightarrow{s}}\left(T_f-T-T\ln{\left(\frac{T_f}{T}\right)}\right)
{\tag{10}}
\end{equation}

Since $\Delta{Cp}_{\ell\rightarrow{s}}$ is usually small compared the above expression is typically simplified to: 

\begin{equation}
\Delta{g}_i^s(T,P)\simeq-\Delta{h_{fus}\left(1-\frac{T}{T_f}\right)}
{\tag{11}}
\end{equation}

Inserting this equation into the equality of fugacities yields:

\begin{equation}
f_i^\ell(T,P)x_i\gamma_i(T,P,\vec{x})=f_i^\ell(T,P)e^{\frac{\Delta{\mu}_{i,\ell\rightarrow{s}}}{RT}}
{\tag{12}}
\end{equation}

hence the solubility of component $i$, $x_i$ is:  

\begin{equation}
x_i=\frac{1}{\gamma_i(T,P,\vec{x})}e^{-\frac{\Delta{h_{fus}}}{R}\left(\frac{1}{T}-\frac{1}{T_f}\right)}
{\tag{13}}
\end{equation}