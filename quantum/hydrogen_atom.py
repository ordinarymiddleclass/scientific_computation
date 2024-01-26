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


