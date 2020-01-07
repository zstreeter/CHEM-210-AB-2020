import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import complex_ode

HBAR = 1.

def hamiltonian(t=0):
    velocity = 1.
    interaction = 0.1
    epsilon = velocity * t
    return np.array([[epsilon, interaction], [interaction, -epsilon]])

def rhs(t, psi):
    return -1.0j / HBAR * hamiltonian(t).dot(psi)

def plot_evolution(times, psi_t):
    plt.plot(times, psi_t[:, 0].real, label='$C_0$ (real)')
    plt.plot(times, psi_t[:, 0].imag, label='$C_0$ (imag)')
    plt.plot(times, psi_t[:, 1].real, label='$C_1$ (real)')
    plt.plot(times, psi_t[:, 1].imag, label='$C_1$ (imag)')
    plt.plot(times, psi_t.dot(psi_t.T.conj()).diagonal().real, label='normalization')
    plt.xlabel('t')
    plt.grid(True)
    plt.legend()
    plt.show()


t0 = 0.0
c_0_initial = 0.1
c_1_initial = np.sqrt(1 - c_0_initial ** 2)
psi_0 = np.array([c_0_initial, c_1_initial]).astype(np.complex)

# Create the array `t` of time values at which to compute
# the solution, and create an array to hold the solution.
# Put the initial value in the solution array.
MAX_TIME = 10
N_TIMES = 100
times = np.linspace(t0, MAX_TIME, N_TIMES)

# Crank Nicolson propagator
psi_t = np.zeros((N_TIMES, 2)).astype(np.complex)
psi_t[0] = psi_0
one = np.eye(psi_0.shape[0])
for t in range(1, np.shape(times)[0]):
    time = times[t]
    delta_t = times[t] - times[t-1]
    propagator = np.linalg.inv(one + 1j * delta_t / 2 * hamiltonian(time - delta_t / 2.0))
    propagator = propagator.dot(one - 1j * delta_t / 2 * hamiltonian(time - delta_t / 2.0))
    psi_t[t] = propagator.dot(psi_t[t-1])

plot_evolution(times, psi_t)


# Create a complex_ode instance to solve the system of differential
# equations defined by `hamiltonian`, and set the solver method to dopri5 (an alternative more precise RK-8 is dop853)
solver = complex_ode(rhs)
solver.set_integrator('dopri5')
solver.set_initial_value(psi_0, t0)

psi_t = np.zeros((N_TIMES, 2)).astype(np.complex)
psi_t[0] = psi_0

# Repeatedly call the `integrate` method to advance the
# solution to time t[k], and save the solution in sol[k].
for i in range(1, times.shape[0]):
    time = times[i]
    if not solver.successful():
        break
    psi_t[i] = solver.integrate(time)


# Plot the solution...
plot_evolution(times, psi_t)
