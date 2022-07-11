# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 12:25:42 2022

@author: DaveW

Implementation of a n order high-pass with w0 threshold frequency filter to a sin function
"""

import numpy as np
import matplotlib.pyplot as plt

# The sin function will be tha one that provides numpy


#%% Defining a function that will provide the Amplitude given by the filter 

def An(n, w_0, freq_list):
    # n is the order of the filter
    # w_0 is the threshold frequency
    # Freq_list is a list with the frequencies
    Amplitude_list = []
    for freq in freq_list:
        if freq >= w_0:
            Amplitude = 0
        else:
            Amplitude = 20*np.log(freq/w_0)
        Amplitude_list.append(Amplitude)
    return Amplitude_list


#%% Defining the Sweep function

def Sweep(Amplitude, freq_list):
    # Amplitude is the factor by which will be multiplied
    # Freq_list is a list with the frequencies
    Sin_list = []
    for i in range(len(freq_list)):
        Sin = Amplitude[i]*np.sin(2*np.pi*freq_list[i])
        Sin_list.append(Sin)
    return Sin_list

#%% Creation of the frequency list

Frequency = np.linspace(1e-6,20000, 20001)


#%% Creation of the parameters to plot

Amplitude = An(1,10,Frequency)
Sweep_list = Sweep(Amplitude, Frequency)


#%% Ho grafiquem a veure


plt.figure(1)
plt.subplot(121)
plt.plot(Frequency, Amplitude)
plt.xscale('log')
plt.subplot(122)
plt.plot(Frequency, Sweep_list) 
plt.xscale('log')
plt.tight_layout()











