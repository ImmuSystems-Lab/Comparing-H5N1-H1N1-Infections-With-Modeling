#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.lines as mlines
import math
from matplotlib.ticker import StrMethodFormatter
from scipy.integrate import odeint
import scipy.stats as stats

# load data
tvec = np.genfromtxt('data/data_h1n1_logged.csv', usecols = 0, delimiter = ',',
                     skip_header = 1) # timepoints
data1 = np.genfromtxt('data/data_h1n1_logged.csv', usecols = [1,2,3,4], delimiter = ',',
                     skip_header = 1) # data

std1 =  np.genfromtxt('data/std_h1n1_logged.csv', usecols = [1,2,3,4], delimiter = ',',
                     skip_header = 1)#std dev of data
data5 = np.genfromtxt('data/data_h5n1_logged.csv', usecols = [1,2,3,4], delimiter = ',',
                     skip_header = 1) # data

std5 =  np.genfromtxt('data/std_h5n1_logged.csv', usecols = [1,2,3,4], delimiter = ',',
                     skip_header = 1)#std dev of data

ic =  np.genfromtxt('data/logged_4state_init.csv', usecols = [2,3,4], delimiter = ',',
                     skip_header = 1)#unlogged IC's of data

#load parameters
sychain = np.genfromtxt('data/fig 2/shared_min_ychainh1n1.csv', delimiter = ",", usecols = np.arange(0,10))[0,:]
print(np.shape(sychain))
sychain = np.genfromtxt('data/fig 2/shared_min_ychainh5n1.csv', delimiter = ",", usecols = np.arange(0,10))[0,:]

ychainh1n1 = np.genfromtxt('data/fig 2/min_ychainh1n1.csv', delimiter = ",", usecols = np.arange(0,10))[0,:]
print(np.shape(ychainh1n1))
ychainh5n1 = np.genfromtxt('data/fig 2/min_ychainh5n1.csv', delimiter = ",", usecols = np.arange(0,10))[0,:]


def f4(u, t, p, ic):
    """2 state ODE model of Virus and IFN"""
    k, big_k, r_ifn_v, d_v, p_v_ifn, d_ifn, k1, k2, d_mcp1, n1 = p
    v, ifn, mcp1 = u
    v0, ifn0, mcp10 = ic
    dv = k*v*(1-v/big_k) - r_ifn_v*(ifn-ifn0)*v - d_v*v
    difn = p_v_ifn*v - d_ifn*(ifn - ifn0)
    dmcp1 = (k1*(ifn-ifn0)**n1)/(k2+(ifn-ifn0)**n1)-(mcp1-mcp10)*d_mcp1
    return [dv, difn, dmcp1]

def g(model, t, u0, p):
    """Return integration of model"""
    sol = odeint(model, u0, t, args=(p,u0))
    return sol

u01 = ic[0,:]
u05 = ic[1,:]
tmax = 5
tspan = np.arange(0,tmax+.05,0.05)

vsolh1n1 = g(f4, tspan, u01, sychain)[:,0]
isolh1n1 = g(f4, tspan, u01, sychain)[:,1]
msolh1n1 = np.log2(g(f4, tspan, u01, sychain)[:,2])
vsolh5n1 = g(f4, tspan, u05, sychain)[:,0]
isolh5n1 = g(f4, tspan, u05, sychain)[:,1]
msolh5n1 = np.log2(g(f4, tspan, u05, sychain)[:,2])

vsolh1n1 = np.transpose(vsolh1n1)
vsolh5n1 = np.transpose(vsolh5n1)
isolh1n1 = np.transpose(isolh1n1)
isolh5n1 = np.transpose(isolh5n1)
msolh1n1 = np.transpose(msolh1n1)
msolh5n1 = np.transpose(msolh5n1)


ivsolh1n1 = g(f4, tspan, u01, ychainh1n1)[:,0]
iisolh1n1 = g(f4, tspan, u01, ychainh1n1)[:,1]
imsolh1n1 = np.log2(g(f4, tspan, u01, ychainh1n1)[:,2])
ivsolh5n1 = g(f4, tspan, u05, ychainh5n1)[:,0]
iisolh5n1 = g(f4, tspan, u05, ychainh5n1)[:,1]
imsolh5n1 = np.log2(g(f4, tspan, u05, ychainh5n1)[:,2])

ivsolh1n1 = np.transpose(ivsolh1n1)
ivsolh5n1 = np.transpose(ivsolh5n1)
iisolh1n1 = np.transpose(iisolh1n1)
iisolh5n1 = np.transpose(iisolh5n1)
imsolh1n1 = np.transpose(imsolh1n1)
imsolh5n1 = np.transpose(imsolh5n1)

title_font = {'size':'26', 'color':'black', 'weight':'bold',
              'verticalalignment':'bottom'} # Bottom vertical alignment for more space
axis_font = {'size':'28'}
cbPalette2 = ["#000000","#56B4E9", "#009E73", "#E69F00", "#0072B2", "#D55E00", "#CC79A7", "#999999","#9d5bc9", "#F0E442", "5bc989"]
plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.1f}'))
plt.rcParams.update({'font.size': 20, 'font.family': 'serif'})

## PLOT 
fig,ax = plt.subplots(2,3, figsize=(18.0, 12.0))# 15.0, 10.0))
plt.rcParams.update({'font.size': 26, 'font.family': 'serif', 'axes.labelsize': 30, 'axes.titlesize': 30})
ax[0,0].errorbar(tvec, data1[:,0], std1[:,0], marker = 'o', linestyle = 'None', zorder=10000,color='black',markersize=12, elinewidth =2)
ax[0,0].plot(tspan,vsolh1n1,color="#0072B2", linewidth =2)
ax[0,0].plot(tspan,ivsolh1n1,color='black', linewidth =2)
ax[0,0].legend(labels=['NSSD','AD','Shoemaker et al'], prop={"size":16, })
plt.ylabel('log10(PFU/mg)')
for label in (ax[0,0].get_xticklabels() + ax[0,0].get_yticklabels()):
	label.set_fontsize(22)
ax[0,0].set_xticks(np.arange(0, 6, 1))
ax[0,0].set(xlabel='Days',ylabel='log10(PFU/g)',title=('V - H1N1'))

## 

ax[0,1].errorbar(tvec, data1[:,1], std1[:,1], marker = 'o', linestyle = 'None', zorder=10000,color='black',markersize=12, elinewidth =2)
ax[0,1].plot(tspan,isolh1n1,color="#0072B2", linewidth =2)
ax[0,1].plot(tspan,iisolh1n1,color='black', linewidth =2)
for label in (ax[0,1].get_xticklabels() + ax[0,1].get_yticklabels()):
        label.set_fontsize(22)
ax[0,1].set_xticks(np.arange(0, 6, 1))
ax[0,1].set(xlabel='Days',ylabel='Gene expression',title=('I - H1N1'))

##

ax[0,2].errorbar(tvec, data1[:,2], std1[:,2], marker = 'o', linestyle = 'None', zorder=10000,color='black',markersize=12, elinewidth =2)
ax[0,2].plot(tspan,msolh1n1,color="#0072B2", linewidth =2)
ax[0,2].plot(tspan,imsolh1n1,color='black', linewidth =2)
for label in (ax[0,2].get_xticklabels() + ax[0,2].get_yticklabels()):
        label.set_fontsize(22)
ax[0,2].set_xticks(np.arange(0, 6, 1))
ax[0,2].set(xlabel='Days',ylabel='log10(Cell Count)',title=('M - H1N1'))

##

ax[1,0].errorbar(tvec, data5[:,0], std5[:,0], marker = 'o', linestyle = 'None', zorder=10000,color='black',markersize=12, elinewidth =2)
ax[1,0].plot(tspan,vsolh5n1,color="#0072B2", linewidth =2)
ax[1,0].plot(tspan,ivsolh5n1,color='black', linewidth =2)
plt.ylabel('log10(PFU/mg)')
for label in (ax[1,0].get_xticklabels() + ax[1,0].get_yticklabels()):
        label.set_fontsize(22)
ax[1,0].set_xticks(np.arange(0, 6, 1))
ax[1,0].set(xlabel='Days',ylabel='log10(PFU/g)',title=('V - H5N1'))

## 

ax[1,1].errorbar(tvec, data5[:,1], std5[:,1], marker = 'o', linestyle = 'None', zorder=10000,color='black',markersize=12, elinewidth =2)
ax[1,1].plot(tspan,isolh5n1,color="#0072B2", linewidth =2)
ax[1,1].plot(tspan,iisolh5n1,color='black', linewidth =2)
for label in (ax[1,1].get_xticklabels() + ax[1,1].get_yticklabels()):
        label.set_fontsize(22)
ax[1,1].set_xticks(np.arange(0, 6, 1))
ax[1,1].set(xlabel='Days',ylabel='Gene expression',title=('I - H5N1'))

##

ax[1,2].errorbar(tvec, data5[:,2], std5[:,2], marker = 'o', linestyle = 'None', zorder=10000,color='black',markersize=12, elinewidth =2)
ax[1,2].plot(tspan,msolh5n1,color="#0072B2", linewidth =2)
ax[1,2].plot(tspan,imsolh5n1,color='black', linewidth =2)
for label in (ax[1,2].get_xticklabels() + ax[1,2].get_yticklabels()):
        label.set_fontsize(22)
ax[1,2].set_xticks(np.arange(0, 6, 1))
ax[1,2].set(xlabel='Days',ylabel='log10(Cell Count)',title=('M - H5N1'))


plt.tight_layout()
plt.savefig(fname="Fig4.svg",transparent=True,bbox_inches='tight')
plt.clf() 
