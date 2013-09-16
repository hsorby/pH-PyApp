# This is the code generated for the model using the CellML-API, modified slightly for inclusion in the rest of the app.
# Size of variable arrays:
   
import numpy as np

sizeAlgebraic = 4
sizeStates = 3
sizeConstants = 16

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_constants = [""] * sizeConstants
    legend_voi = "Time in component Environment (second)"
    legend_states[0] = "CO2 in component Flux (mM)"
    legend_states[1] = "HCO3 in component Flux (mM)"
    legend_states[2] = "H in component Flux (mM)"
    legend_constants[10] = "kf in component Flux (per_second)"
    legend_constants[6] = "kb in component Flux (per_mM_per_second)"
    legend_algebraic[0] = "J in component Flux (mM_per_second)"
    legend_constants[0] = "CO2source in component Flux (mM_per_second)"
    legend_constants[1] = "CO2sink in component Flux (mM_per_second)"
    legend_constants[2] = "protonSource in component Flux (mM_per_second)"
    legend_algebraic[1] = "pH in component Flux (dimensionless)"
    legend_constants[3] = "c1 in component Flux (mM)"
    legend_constants[11] = "initialH in component Flux (mM)"
    legend_constants[4] = "initialPh in component Flux (dimensionless)"
    legend_constants[13] = "Cx in component PPresToConc (M)"
    legend_constants[5] = "initialCO2mmHg in component Flux (mmHg)"
    legend_algebraic[2] = "Px in component ConcToPPres (pascal)"
    legend_algebraic[3] = "CO2mmHg_proxy in component Flux (mmHg)"
    legend_constants[12] = "sCO2 in component Flux (mM_per_mmHg)"
    legend_constants[7] = "pK in component Flux (dimensionless)"
    legend_constants[9] = "K in component Flux (dimensionless)"
    legend_constants[14] = "initialHCO3mM in component Flux (dimensionless)"
    legend_constants[8] = "Px_proxy in component PPresToConc (pascal)"
    legend_rates[0] = "d/dt CO2 in component Flux (mM)"
    legend_rates[1] = "d/dt HCO3 in component Flux (mM)"
    legend_rates[2] = "d/dt H in component Flux (mM)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 0
    constants[1] = 0
    constants[2] = 0
    constants[3] = 1000
    constants[4] = 7.4
    constants[5] = 40
    constants[6] = 1.00000
    constants[7] = 6.10000
    constants[8] = constants[5]*133.322
    constants[15] = constants[0]-constants[1]
    constants[9] = np.power(10.0000, -constants[7])
    constants[10] = constants[9]*1.00000
    constants[11] = (np.power(10.0000, -constants[4]))*constants[3]
    constants[12] = 0.0300000
    constants[13] = (constants[5]*133.322)*(constants[12]*7.50062e-06)
    constants[14] = ((constants[13]*1000.00)*constants[9])/constants[11]
    states[0] = constants[13]*1000.00
    states[1] = constants[14]
    states[2] = constants[11]
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = constants[15]
    algebraic[0] = constants[10]*states[0]-constants[6]*states[1]*states[2]
    rates[1] = algebraic[0]
    rates[2] = algebraic[0]+constants[2]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = np.array([[0.0] * len(voi)] * sizeAlgebraic)
    states = np.array(states)
    voi = np.array(voi)
    algebraic[0] = constants[10]*states[0]-constants[6]*states[1]*states[2]
    algebraic[1] = -np.log10(states[2]/constants[3])
    algebraic[2] = (states[0]*0.00100000)/(constants[12]*7.50062e-06)
    algebraic[3] = algebraic[2]*0.00750062
    return algebraic

def solve_model(init_states, constants, voi):
    """Solve model with ODE solver"""
    from scipy.integrate import ode
    # Initialise constants and state variables
    # (init_states, constants) = initConsts()

    # Set timespan to solve over
    #voi = linspace(0, 10, 500)

    # Construct ODE object to solve
    r = ode(computeRates)
    r.set_integrator('vode', method='bdf', atol=1e-06, rtol=1e-06, max_step=1)
    r.set_initial_value(init_states, voi[0])
    r.set_f_params(constants)

    # Solve model
    states = np.array([[0.0] * len(voi)] * sizeStates)
    states[:,0] = init_states
    for (i,t) in enumerate(voi[1:]):
        if r.successful():
            r.integrate(t)
            states[:,i+1] = r.y
        else:
            break

    # Compute algebraic variables
    algebraic = computeAlgebraic(constants, states, voi)
    return (voi, states, algebraic)
