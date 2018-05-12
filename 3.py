import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as mtick
from matplotlib.legend_handler import HandlerLine2D

# t = range(1, 11)
t = [1,2,3,4,5,6,7,8,9,10]
data1 = [7.22E+05,1.44E+06,2.17E+06,2.89E+06,3.61E+06,4.33E+06,5.06E+06,5.78E+06,6.50E+06,7.22E+06]
data1_1 = [1.20E+06,2.40E+06,3.60E+06,4.80E+06,6.00E+06,7.20E+06,8.40E+06,9.60E+06,1.08E+07,1.20E+07]
data2 = [62.42,62.42,62.42,62.42,62.42,62.42,62.42,62.42,62.42,62.42]


color1_1 = '#EE9A49'
# color1_1 = 'tab:blue'
color1 = '#3A5FCD'
color2 = '#4D4D4D'

fig, ax1 = plt.subplots()
patch1 = mpatches.Patch(color=color1, label='Weights (static)')
patch1_1 = mpatches.Patch(color=color1_1, label='Activations(dynamic)')
patch2 = mpatches.Patch(color=color2, label='Pct. of Activations', capstyle='butt', linestyle='solid')
plt.legend(handles=[patch1, patch1_1,patch2])


ax1.set_xlabel('Number of layers')
ax1.set_ylabel('Amount of data')
ax1.bar(t, data1, width=0.5, label='Weights (static)', color=color1)
ax1.bar(t, data1_1, bottom=data1, width=0.5, label='Activations(dynamic)', color=color1_1)
ax1.tick_params(axis='y')


ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
ax2.set_ylabel('Pct. of Activations')

ymajorLocator   = mtick.MultipleLocator(10)
ax2.yaxis.set_major_locator(ymajorLocator)
fmt='%.2f%%'
yticks = mtick.FormatStrFormatter(fmt)
ax2.yaxis.set_major_formatter(yticks)

patch3, = ax2.plot(t, data2, color=color2, linewidth=2, marker='.')
plt.ylim(10, 100)
ax2.tick_params(axis='y')




fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()
