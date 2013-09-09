# This is the code generated for the model using the CellML-API, modified slightly for inclusion in the rest of the app.
# Size of variable arrays:
from math import *
from numpy import *


    
sizeAlgebraic = 1
sizeStates = 3
sizeConstants = 5



def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "Time in component Environment (second)"
    legend_states[0] = "CO2 in component Flux (mM)"
    legend_states[1] = "HCO3 in component Flux (mM)"
    legend_states[2] = "H in component Flux (mM)"
    legend_constants[0] = "kf in component Flux (per_second)"
    legend_constants[1] = "kb in component Flux (per_mM_per_second)"
    legend_algebraic[0] = "J in component Flux (mM_per_second)"
    legend_constants[2] = "CO2source in component Flux (mM_per_second)"
    legend_constants[3] = "CO2sink in component Flux (mM_per_second)"
    legend_constants[4] = "protonSource in component Flux (mM_per_second)"
    legend_rates[0] = "d/dt CO2 in component Flux (mM)"
    legend_rates[1] = "d/dt HCO3 in component Flux (mM)"
    legend_rates[2] = "d/dt H in component Flux (mM)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 2
    states[1] = 0
    states[2] = 0
    constants[0] = 0.15
    constants[1] = 0.5
    constants[2] = 0
    constants[3] = 0
    constants[4] = 0
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[0] = constants[0]*states[0]-constants[1]*states[1]*states[2]
    rates[0] = (-algebraic[0]+constants[2])-constants[3]
    rates[1] = algebraic[0]
    rates[2] = algebraic[0]+constants[4]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = constants[0]*states[0]-constants[1]*states[1]*states[2]
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
    states = array([[0.0] * len(voi)] * sizeStates)
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

def plot_model(voi, states, algebraic):
    """Plot variables against variable of integration"""
    import pylab
    (legend_states, legend_algebraic, legend_voi, legend_constants) = createLegends()
    pylab.figure(1)
    pylab.plot(voi,vstack((states,algebraic)).T)
    pylab.xlabel(legend_voi)
    pylab.legend(legend_states + legend_algebraic, loc='best')
    pylab.show()

if __name__ == "__main__":
    (voi, states, algebraic) = solve_model()
    plot_model(voi, states, algebraic)
