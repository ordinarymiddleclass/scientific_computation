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

def hydrogen_plot(n, l, m):
    """
    plot the wave function of hydrogen atom with quantum numbers n, l, m.
    """
    # set up the grid
    r = np.linspace(0, 20, 100)
    theta = np.linspace(0, np.pi, 100)
    phi = np.linspace(0, 2*np.pi, 100)    
    # calculate the wave function
    R_nl = 2 * r * np.exp(-r / n) * (r / n)**l * eval_genlaguerre(n - l - 1, 2 * l + 1, r / n)
    Y_lm = sph_harm(m, l, phi, theta)
    Psi = R_nl * Y_lm
    # transform psi to cartesian coordinates
    X = 
    Y = R * np.sin(Theta) * np.sin(Phi)
    Z = R * np.cos(Theta)    
    # plot the wave function in spherical coordinates
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(R * np.sin(Theta) * np.cos(Phi), R * np.sin(Theta) * np.sin(Phi), R * np.cos(Theta), rstride=1, cstride=1, facecolors=cm.jet(Psi.real), norm=colors.Normalize(vmin=-0.5, vmax=0.5))
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_title("Hydrogen atom wave function")
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
    n = 3
    l = 2
    m = 0
    print("n = ", n)
    print("l = ", l)
    print("m = ", m)
    print("Plotting...")
    hydrogen_plot(n, l, m)
    print("Done!")
    
if __name__ == "__main__":
    main()