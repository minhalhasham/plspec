from scipy.optimize import curve_fit as cf
import numpy as np 





def gauss(x,a,m,s): 
    """
    Gaussian function for fitting
    """

    return a * np.exp(-(x - m) ** 2 / (2 * s ** 2))

def twogauss(x,a1,m1,s1,a2,m2,s2): 
    """
    Two Gaussian function for fitting
    """

    return a1 * np.exp(-(x - m1) ** 2 / (2 * s1 ** 2)) + a2 * np.exp(-(x - m2) ** 2 / (2 * s2 ** 2))

def line(x,a,b): 
    """
    Just a line...
    Sometimes I use this to remove a sloping background"""

    return a*x+b

def fit(f,x,y,p0=None): 
    """
    Fit the data to the function f
    """

    p,c=cf(f,x,y,p0)
    return p,c