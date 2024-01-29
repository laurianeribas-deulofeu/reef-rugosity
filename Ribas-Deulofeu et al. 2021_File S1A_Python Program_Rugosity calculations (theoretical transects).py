'''--------------------------------------------------------------------------------------------------
Name:		File S1A_Python Program_Rugosity calculations (theoretical transects)
Purpose:	Draws and export the rugosity index for a given degree of polynomial
Author:		P.-A. Chateau
Created:	10/07/2017
Ex use: 	python File S1A_Python Program_Rugosity calculations (theoretical transects).py 1
--------------------------------------------------------------------------------------------------'''
from matplotlib import pyplot
pyplot.style.use('ggplot')
from pandas import read_csv
from scipy.optimize import curve_fit
from scipy.stats.stats import pearsonr
from sys import argv
import numpy as np


def polyfunc(x, *params):
    return sum([p*x**i for i, p in enumerate(params)])


d = int(argv[1])
data = read_csv('File S2_Data_Depth profiles (theoretical transects).csv')
sites = range(3)
transects = range(3)
fig, ax = pyplot.subplots(len(sites), len(transects), figsize=(3*len(transects), 2*len(transects)))
CHN, RUG = [], []
i = 0
for s in sites:
    j = 0
    mean_rug = 0.
    for t in transects:
        y = data["T"+str(s*3+t+1)]
        x = np.linspace(0, len(y), len(y))
        valid = ~(np.isnan(x) | np.isnan(y))
        popt, pcov = curve_fit(polyfunc, x[valid], -y[valid], p0 = [1]*(d+1))
        rug = 0.
        length = 20./len(y[valid])
        for z in range(len(y[valid])):
            rug += length*(-y[z]-polyfunc(x[z], *popt))**2
        chn = sum([((y[z]-y[z-1])**2+length**2)**.5 for z in range(1, len(y[valid]))])/20.
        rug /= 20.
        rug = rug**.5
        ax[i, j].plot(x[valid], -y[valid], 'b', lw=2)
        ax[i, j].plot(x[valid], polyfunc(x[valid], *popt), 'r', lw=1)
        ax[i, j].set_xlim(0, len(x[valid]))
        ax[i, j].set_ylim(-12, 2)
        ax[i, j].grid(False)
        if i < 2:
            ax[i, j].set_xticks([])
            ax[i, j].set_xticklabels([])
        else:
            ax[i, j].set_xticks([len(x[valid])/4, len(x[valid])/2, 3*len(x[valid])/4])
            ax[i, j].set_xticklabels([5, 10, 15])
            ax[i, j].set_xlabel('Transect length (m)', size=10)
        if j == 0:
            ax[i, j].set_yticks([-4, -8])
            ax[i, j].set_yticklabels([4, 8])
            ax[i, j].set_ylabel('Depth (m)', size=10)
        else:
            ax[i, j].set_yticks([])
        ax[i, j].text(.05, .9, 'Theo'+str(s*3+t+1)+': '+'Rq'+str(d)+' = '+str(round(rug, 2))+' ('+str(round(chn, 2))+')', transform=ax[i, j].transAxes, size=10)
        j += 1
        CHN.append(chn)
        RUG.append(rug)
    i += 1
pyplot.tight_layout()
fig.savefig('th'+argv[1]+'.png', dpi=200)
count = 0
with open('./th'+argv[1]+'.csv','w') as logfile:
    logfile.write('Transect,Rugosity,Chain\n')
    for s in range(3):
        for t in range(3):
            logfile.write('T'+str(s*3+t+1)+','+str(RUG[count])+','+str(CHN[count])+'\n')
            count += 1
print('correlation th'+str(d)+'-chain:', pearsonr(CHN, RUG))
