#######################################
#######################################
#######################################
#######################################
#######################################
# @author: Minhal
# @date: 2024-03-21
# @version: 0.2
# @last-update: 2024-03-24
# @license: Free to use for all, modify, distribute, re-package, use as part of something else. No commericalize, yes give credit.
# @disclaimer: This is a simple script to load and plot PL data from our PicoQuant setup. Use at your own risk
#######################################
#######################################
#######################################
#######################################
#######################################

# Constants for if/when we eventually conver to units of photon energy
h=6.626*10**-34 # planck, J*s
c=299792458 # light, m/s

import numpy as np
import plotter as pltr
import sys
import fit_funcs
import matplotlib.pyplot as plt

def load(file,peaks=0,to_ev=0): 
    """
    Load data from a file and return the wavelength and intensity values.
    If peaks=1, also return the peak wavelength and peak position.
    Currently, the data must be from our PicoQuant setup.
    """
    data=np.genfromtxt(str(file), delimiter='\t',skip_header=71)
    waves,y=split(data)
    y_sub=bg(y)
    if peaks==1:
        peak_wave, peak_pos=peak(waves,y)
        print("Peak Wavelength = %.3d" % peak_wave + " nm" , "Peak Index = %d" % peak_pos)
        #return waves, y_sub, peak_wave, peak_pos
    if to_ev==1:
        E, PL_ev=energy(waves,y_sub)
        return E, PL_ev
    return waves,y_sub

def split(x): 
    """
    Split the data into wavelength and PL intensity values
    """
    waves=x[:,0]
    y=x[:,1]
    return waves, y

def bg(y): 
    """
    Subtract the background from the data and peak normalize the intensity values.
    WARNING: This assumes the background is the last 25 points of the data. Change if your data is different.
    """
    subbed=y-np.mean(y[-25:-1])
    subbed=subbed/np.max(subbed)
    return subbed

def peak(waves,y):
    """
    Find the peak wavelength and peak index for further processing
    """
    peak_wave=waves[np.argmax(y)]
    peak_pos=np.argmax(y)
    return peak_wave, peak_pos

def energy(waves,y): 
    """Converts PL intensity values (your y-axis) into units of photon energy
    If you're reading this and you don't understand why and you're not Minhal, see here:
    https://pubs.acs.org/doi/10.1021/jz401508t
    """


    waves_m=waves*10**-9 # Wavelength: nm -> m
    E=h*c/waves_m # Wavelength -> Energy: m -> J
    E_ev=E*(6.242*10**18) # Energy: J -> eV
    jac = (h*c)/(E_ev**2) # Jacobian for the conversion
    PL_ev=y*jac # Convert the PL intensity values to eV
    return E_ev, PL_ev

#### Used during testing.
wave=0
ev=1
fit=1

if __name__=='__main__':
    if len(sys.argv)>1: 
        file=sys.argv[1]
    else:
        file=input("Path and filename: ")
    x,y=load(file,peaks=1,to_ev=1)
        
    if wave==1: 
        pltr.plot(x,y,label=file[-8:-4])
    if fit ==1:
        p,c=fit_funcs.fit(fit_funcs.gauss,x,y)
        plt.plot(x,fit_funcs.gauss(x,*p),'--',color='red',label='fit')
        plt.plot(x,y,label=file[-8:-4])
        plt.show()
    else:
        pltr.plot(x,y,label=file[-8:-4],xlabel='Energy (eV)')
