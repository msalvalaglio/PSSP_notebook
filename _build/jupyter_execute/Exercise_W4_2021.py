# Week 4 - Exercise

## Problem Statement

The downstream processing of an aqueous stream containing therapeutic proteins produced in a bioreactor is carried out through an ultrafiltration membrane process. 
The volumetric flow to be processed is 200 $\mathrm{m^3\,day^{-1}}$, with a suspended protein concentration of 0.5 $\mathrm{kg\,m^{-3}}$. 
In order to be used in subsequent formulation stages the protein stream needs to be concentrated to 20 $\mathrm{kg\,m^{-3}}$. 

Tubular membrane modules with an exchange surface of 5 $\mathrm{m^2}$ are used to carry out the ultrafiltration process. 

Due to fouling, the water flow through these membranes decreases when protein concentration (C) increases following the empirical law: 

$$
J(C)=3.8\times10^{-2}\ln\left(\frac{145}{C}\right) \mathrm{[m\,h^{-1}]}
$$

## Requests 

- Based on steady state calculations compute the number of membrane modules necessary for the operation of this process in a single-stage feed-and-bleed configuration.
- Consider now a cascade of two stages. Compute the optimal number of membrane modules and their arrangement in stages in order to achieve the specifics required. Compute all the concentrations and volumetric flows in your process configuration of choice.  Define clearly your chosen criterion for optimality.
