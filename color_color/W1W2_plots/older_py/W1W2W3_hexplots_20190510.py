'''
Making the 'famous' W2-W3 vs. W1-W2 WISE color-color plot
e.g. Figure 12 of Wright et al. (2010) and lots of other
places too...
'''

import numpy as np
from astropy.io    import fits
from astropy.io    import ascii
from astropy.table import Table

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

##
## DR14Q
##
path = '/cos_pc19a_npr/data/SDSS/DR14Q/'
filename ='DR14Q_v4_4.fits'
#filename ='DR14Q_v4_4_W4good.fits'
infile = path+filename
data = fits.getdata(infile, 1)
dr14q = Table(data)
dr14q_W1minW2 = (dr14q['W1MAG'] - dr14q['W2MAG'])
dr14q_W2minW3 = (dr14q['W2MAG'] - dr14q['W3MAG'])

##
##  V H z Q    data
##
path = '/cos_pc19a_npr/programs/quasars/highest_z/data/'
filename = 'VHzQs_ZYJHK_WISE.dat'
table=path+filename
VHzQ = ascii.read(table)


##  Making the plot(s)
## 
##  W2-W3  vs.  W1-W2 
##
plt.rcParams.update({'font.size': 14})
## For one colour bar...
fig, ax = plt.subplots(figsize=(10, 10), num=None, dpi=80, facecolor='w', edgecolor='k')
## For two colour bars, outside the plotted axes
#fig, ax = plt.subplots(figsize=(14, 10), num=None, dpi=80, facecolor='w', edgecolor='k')


## Blain et al. (2013), Figure 1:: 
xmin =  1.7; xmax =  5.4; ymin = -0.4; ymax =  2.0 
## Wright et al. (2010), Figure 
#xmin = -1.0; xmax=7.0;    ymin=-0.5; ymax=4.0

## Some plotting defaults
ls              = 28
ticklength      = 18
tickwidth       = 2.0
pointsize       = 100
pointsize_large = pointsize*1.2
fontsize        = 28

##
##  Plotting the   D R 1 4 Q    hexbins
##
cmap = plt.cm.Greys
hb = ax.hexbin( dr14q_W2minW3, 
                dr14q_W1minW2,
                C=dr14q['Z'],
#                gridsize=180, mincnt=25, marginals=False, cmap=cmap, vmin=0.00, vmax=3.00)
                 gridsize=220, mincnt=10, marginals=False, cmap=cmap, vmin=0.00, vmax=3.00)
##  [left, bottom, width, height], 
cbaxes = fig.add_axes([0.3, 0.3, 0.40, 0.025])
#cb = fig.colorbar(hb, ax=ax)
cb = fig.colorbar(hb, ax=ax, cax=cbaxes, orientation='horizontal', ticklocation = 'top')
#cb.set_label('')

w = dr14q[np.where(    (dr14q['W2MAG'] >= xmin))]
print('Number of DR14Q objects plotted:: ', len(w))

##
##  Plotting the   V H z Q    points
##
#cmap = plt.cm.inferno
cmap = plt.cm.seismic
hb_VHzQ = ax.scatter((VHzQ['unW2mag'] -  VHzQ['w3mpro']),
                     (VHzQ['unW1mag'] - VHzQ['unW2mag']),
                     c=VHzQ['redshift'],
                     s=pointsize, cmap=cmap)
## need this just for the objects that have e.g. null detections
ax.scatter(0,0, color='w', s=pointsize_large)

cbaxes = fig.add_axes([0.2, 0.2, 0.20, 0.025]) 
cb = fig.colorbar(hb_VHzQ,  ax=ax, cax=cbaxes, orientation='horizontal',ticklocation = 'top')
cb.set_label('redshift', labelpad=20)


## The vertical dashed line at W 2 − W3 = 5.3 is one of the selection
## criteria for W1W2-dropouts; some are bluer than this because they
## satisfied the W2 − W4 > 8.2 criterion.
lw = 2.0
#ax.axvline(x=5.3, linewidth=lw,linestyle='dotted', color='k')

ax.axis([xmin, xmax, ymin, ymax])

ax.tick_params(axis='both', which='major', labelsize=ls, top='on', right='on', direction='in', length=ticklength,   width=tickwidth)
ax.tick_params(axis='both', which='minor', labelsize=ls, top='on', right='on', direction='in', length=ticklength/2, width=tickwidth)

majorLocator = MultipleLocator(2.0)
minorLocator = MultipleLocator(0.5)
ax.xaxis.set_major_locator(majorLocator)
ax.xaxis.set_minor_locator(minorLocator)

majorLocator = MultipleLocator(1.0)
minorLocator = MultipleLocator(0.1)
ax.yaxis.set_major_locator(majorLocator)
ax.yaxis.set_minor_locator(minorLocator)


## Grid lines to compare with Wright et al. (2010) Fig. 12
## Vertical lines
ax.axvline(x=0.0, ymin=0, ymax=1, ls=':', color='grey')
ax.axvline(x=1.0, ymin=0, ymax=1, ls=':', color='grey')
ax.axvline(x=2.0, ymin=0, ymax=1, ls=':', color='grey')
ax.axvline(x=3.0, ymin=0, ymax=1, ls=':', color='grey')
ax.axvline(x=4.0, ymin=0, ymax=1, ls=':', color='grey')
ax.axvline(x=5.0, ymin=0, ymax=1, ls=':', color='grey')
ax.axvline(x=6.0, ymin=0, ymax=1, ls=':', color='grey')

## Horizontal lines
ax.axhline(y=0.0, xmin=0, xmax=1, ls=':', color='grey')
ax.axhline(y=0.5, xmin=0, xmax=1, ls=':', color='grey')
ax.axhline(y=1.0, xmin=0, xmax=1, ls=':', color='grey')
ax.axhline(y=1.5, xmin=0, xmax=1, ls=':', color='grey')
ax.axhline(y=2.0, xmin=0, xmax=1, ls=':', color='grey')
ax.axhline(y=2.5, xmin=0, xmax=1, ls=':', color='grey')
ax.axhline(y=3.0, xmin=0, xmax=1, ls=':', color='grey')
ax.axhline(y=3.5, xmin=0, xmax=1, ls=':', color='grey')

ax.set_xlabel(r" W2 - W3 ", fontsize=fontsize)
ax.set_ylabel(r" W1 - W2 ", fontsize=fontsize)

plt.savefig('W1W2W3_hexplots_temp.png', format='png')
#plt.show()
#plt.close()
