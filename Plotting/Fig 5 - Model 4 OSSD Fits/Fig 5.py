#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.ticker import StrMethodFormatter
from scipy.integrate import odeint
import scipy.stats as stats

# load data
tvec = np.genfromtxt('./data/data_h1n1_logged.csv', usecols = 0, delimiter = ',',
                     skip_header = 1) # timepoints
data1 = np.genfromtxt('./data/data_h1n1_logged.csv', usecols = [1,2,3,4], delimiter = ',',
                     skip_header = 1) # data

std1 =  np.genfromtxt('./data/std_h1n1_logged.csv', usecols = [1,2,3,4], delimiter = ',',
                     skip_header = 1)#std dev of data
data5 = np.genfromtxt('./data/data_h5n1_logged.csv', usecols = [1,2,3,4], delimiter = ',',
                     skip_header = 1) # data

std5 =  np.genfromtxt('./data/std_h5n1_logged.csv', usecols = [1,2,3,4], delimiter = ',',
                     skip_header = 1)#std dev of data

ic =  np.genfromtxt('./data/logged_4state_init.csv', usecols = [2,3,4], delimiter = ',',
                     skip_header = 1)#unlogged IC's of data


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

pars1 = np.zeros([10,10])
sols1 = np.zeros([101,3,10])  
pars5 = np.zeros([10,10])
sols5 = np.zeros([101,3,10])
dirs = ['k_solo', 'bigk_solo', 'rifnv_solo', 'dv_solo', 'pvifn_solo', 'difn_solo','k1_solo', 'k2_solo', 'dmcp1_solo', 'n_solo']

for i in np.arange(0,10):
    p = np.genfromtxt('./data/fig 4/' + dirs[i] + '_min_ychainh1n1.csv', delimiter = ',')
    pars1[i,:] = p[0,:]
    sols1[:,:,i] = g(f4, tspan, u01, pars1[i,:])
    p = np.genfromtxt('./data/fig 4/' + dirs[i] + '_min_ychainh5n1.csv', delimiter = ',')
    pars5[i,:] = p[0,:]
    sols5[:,:,i] = g(f4, tspan, u05, pars5[i,:])

title_font = {'size':'20', 'color':'black', 'weight':'normal',
              'verticalalignment':'bottom'} # Bottom vertical alignment for more space
axis_font = {'size':'16'}
plt.rcParams.update({'font.size': 20, 'font.family': 'serif'})
params = {'mathtext.default': 'regular' }
plt.rcParams.update(params)
lab = np.array([r'$k$', r'$K$', r'$r_{IFN, V}$', r'$d_V$', r'$p_{V, IFN}$', r'$d_{IFN}$', r'$k_1$', r'$k_2$', r'$d_{MCP1}$', r'$n$'])
lab = np.array([r'$r_{V,V}$', r'$K_{V,V}$', r'$r_{V,I}$', r'$d_V$', r'$r_{I,V}$', r'$d_{I}$', r'$r_{M,I}$', r'$K_{M,I}$', r'$d_{M}$', r'$n$'])
cbPalette2 = ["#000000","#56B4E9", "#009E73", "#E69F00", "#0072B2", "#D55E00", "#CC79A7", "#999999","#9d5bc9", "#F0E442", "5bc989"]

#Total FIG
fig,ax = plt.subplots(2,3, figsize=(18.0, 12.0))# 15.0, 10.0))
plt.rcParams.update({'font.size': 26, 'font.family': 'serif', 'axes.labelsize': 30, 'axes.titlesize': 30})
for i in np.arange(0,10): 
    ax[0,0].plot(tspan,sols1[:,0,i], color = cbPalette2[i], linewidth = 2.5)
    for label in (ax[0,0].get_xticklabels() + ax[0,0].get_yticklabels()):
        label.set_fontsize(22)
    ax[0,0].set_xticks(np.arange(0, 6, 1))
    ax[0,0].errorbar(tvec, data1[:,0], std1[:,0], marker = 'o', linestyle = 'None', zorder=10000,color='black',markersize=12)
    ax[0,0].set(xlabel='Days',ylabel='$log_{10}$(PFU/mg)',title=('V - H1N1'))

for i in np.arange(0,10):
    ax[0,1].plot(tspan,sols1[:,1,i], color = cbPalette2[i], linewidth = 2.5)
    for label in (ax[0,1].get_xticklabels() + ax[0,1].get_yticklabels()):
        label.set_fontsize(22)
    ax[0,1].set_xticks(np.arange(0, 6, 1))
    ax[0,1].errorbar(tvec, data1[:,1], std1[:,1], marker = 'o', linestyle = 'None', zorder=10000,color='black',markersize=12)
    ax[0,1].set(xlabel='Days',ylabel='Gene expression',title=('I - H1N1'))

for i in np.arange(0,10):
    ax[0,2].plot(tspan,np.log2(sols1[:,2,i]), color = cbPalette2[i], linewidth = 2.5)
    for label in (ax[0,2].get_xticklabels() + ax[0,2].get_yticklabels()):
        label.set_fontsize(22)
    ax[0,2].set_xticks(np.arange(0, 6, 1))
    ax[0,2].errorbar(tvec, data1[:,2], std1[:,2], marker = 'o', linestyle = 'None', zorder=10000,color='black',markersize=12)
    ax[0,2].set(xlabel='Days',ylabel='$log_{10}$(Cell Count)',title=('M - H1N1'))

for i in np.arange(0,10):
    ax[1,0].plot(tspan,sols5[:,0,i], color = cbPalette2[i], linewidth = 2.5)
    for label in (ax[1,0].get_xticklabels() + ax[1,0].get_yticklabels()):
        label.set_fontsize(22)
    ax[1,0].set_xticks(np.arange(0, 6, 1))
    ax[1,0].errorbar(tvec, data5[:,0], std5[:,0], marker = 'o', linestyle = 'None', zorder=10000,color='black',markersize=12)
    ax[1,0].set(xlabel='Days',ylabel='$log_{10}$(PFU/mg)',title=('V - H5N1'))

for i in np.arange(0,10):
    ax[1,1].plot(tspan,sols5[:,1,i], color = cbPalette2[i], linewidth = 2.5)
    for label in (ax[1,1].get_xticklabels() + ax[1,1].get_yticklabels()):
        label.set_fontsize(22)
    ax[1,1].set_xticks(np.arange(0, 6, 1))
    ax[1,1].errorbar(tvec, data5[:,1], std5[:,1], marker = 'o', linestyle = 'None', zorder=10000,color='black',markersize=12)
    ax[1,1].set(xlabel='Days',ylabel='Gene expression',title=('I - H5N1'))

for i in np.arange(0,10):
    ax[1,2].plot(tspan,np.log2(sols5[:,2,i]), color = cbPalette2[i], linewidth = 2.5)
    for label in (ax[1,2].get_xticklabels() + ax[1,2].get_yticklabels()):
        label.set_fontsize(22)
    ax[1,2].set_xticks(np.arange(0, 6, 1))
    ax[1,2].errorbar(tvec, data5[:,2], std5[:,2], marker = 'o', linestyle = 'None', zorder=10000,color='black',markersize=12)
    ax[1,2].set(xlabel='Days',ylabel='$log_{10}$(Cell Count)',title=('M - H5N1'))

box = ax[0,2].get_position()
ax[0,2].set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax[0,2].legend(labels = lab,loc='center left', bbox_to_anchor=(1, .5), prop={"size":18})
plt.tight_layout()
plt.savefig(fname="Fig5.svg",transparent=True,bbox_inches='tight')
plt.clf() 
