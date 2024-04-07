"""
    hydrogen_atom.py
    ~~~~~~~~~~~~~~~~
    description: draw illustrations of wave functions of hydrogen atom, according to the quantum numbers n, l, m.
    
    created by Kai-Po Chang on 2024/01/26 and powered by github copilot. 
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import colors
from mpl_toolkits.mplot3d import Axes3D
from scipy.special import sph_harm
from scipy.special import genlaguerre
from scipy.special import factorial
from scipy.special import assoc_laguerre
from scipy.special import eval_genlaguerre
from scipy.special import eval_hermite
from scipy.special import hermite
import sys 

def hydrogen_wave_func(n, l, m, roa, Nx, Ny, Nz):
    """
    calculate the wave function of hydrogen atom with quantum numbers n, l, m.
    """
    # set up the grid
    x = np.linspace(-roa, roa, Nx)
    y = np.linspace(-roa, roa, Ny)
    z = np.linspace(-roa, roa, Nz)
    R = np.sqrt(x**2 + y**2 + z**2)
    Theta = np.arccos(z / R)
    Phi = np.arctan2(y, x)    
    # calculate the wave function
    R_nl = 2 * R * np.exp(-R / n) * (R / n)**l * eval_genlaguerre(n - l - 1, 2 * l + 1, R / n)
    Y_lm = sph_harm(m, l, Phi, Theta)
    Psi = R_nl * Y_lm
    return Psi, x, y, z

def probability_density(Psi):
    """
    calculate the probability density of the wave function.
    """
    return np.abs(Psi * np.conj(Psi))

def plot_probability_density(Psi, X, Y, Z):
    """
    plot the probability density of the wave function.
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_aspect("equal")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.scatter(X, Y, Z, c=probability_density(Psi), cmap='viridis', linewidth=0.5)
    plt.show()

def main():
    """
    if len(sys.argv) != 4:
        print("Usage: python3 hydrogen_atom.py n l m")
        sys.exit(1)
    n = int(sys.argv[1])
    l = int(sys.argv[2])
    m = int(sys.argv[3])
    if n < 1 or l < 0 or m < 0 or l > n - 1 or abs(m) > l:
        print("Invalid quantum numbers")
        sys.exit(1)
    """
    n = 1
    l = 0
    m = 0
    print("n = ", n)
    print("l = ", l)
    print("m = ", m)
    print("Plotting...")
    Psi, X, Y, Z = hydrogen_wave_func(n, l, m, 10, 100, 100, 100)
    plot_probability_density(Psi, X, Y, Z)
    print("Done!")
    
if __name__ == "__main__":
    main()