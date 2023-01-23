## Solution trace
import scipy as sp


# Variables
A=15 * 1E4 # [m^2 * cm^2 / m^2]
P_r=5.5 * 101325 # [atm] * [Pa / atm]
P_p=1.01 * 101325 # [atm] * [Pa / atm] 
l=2.0*1E-4 # cm
rho_STP=1/22.4E3 # / [mol/cm3(stp)]
PCO2=0.034E-13 * 3600 # [cm3(STP) * cm/cm2/s/Pa] * [s/h]
PN2=0.089E-14 * 3600#  [cm3(STP) * cm/cm2/s/Pa] * [s/h]
# Permeate Composition
#y=0.43
# Feed Composition
z = 0.56

alpha=PCO2/PN2
Fin=0.02832

def equations(vars):
    x, y, Fp, Fr, theta = vars
    eq1 = ((theta - 1) / theta) * x + (z / theta) - y
    eq2 = x - (y * (1 + P_p/P_r * (1-y) * (alpha - 1)) / (alpha - (alpha - 1) * y))
    eq3 = Fin - Fr - Fp
    eq4 = Fp*y-A*PCO2*rho_STP / l * (x*P_r-y*P_p)
    eq5 = Fin - (Fp/theta)
    #eq4 = Fp*(1-y)-A*PN2*rho_STP / l * ((1-x)*P_r-(1-y)*P_p)
    return [eq1, eq2, eq3, eq4, eq5]

x, y, Fp, Fr, theta =  sp.optimize.fsolve(equations, (0.1, 0.1, 0.1, 0.1, 0.1))

print(equations([x, y, Fp, Fr, theta]))

print("\nFeed composition: ", f"{z:.4}", " [-]")
print("Permeate composition: ", f"{y:.4}", " [-]")
print("Retentate composition: ", f"{x:.4}", " [-]")
print("Cut: ", f"{theta:.4}", "[-]")
print("Permeate flowrate: ", f"{Fp:.4}", " [mol/h]")
print("Feed flowrate: ", f"{Fin:.4}",  " [mol/h]")
print("Retentate flowrate: ", f"{Fr:.4}", " [mol/h]\n")

