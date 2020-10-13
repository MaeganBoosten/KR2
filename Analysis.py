import numpy as np
import seaborn as sns
import seaborn.timeseries
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

def calcstat(x,y,str):
    t = stats.ttest_ind(x,y)
    print(str)
    print('test statistic:', t.statistic)
    print('p-value:', t.pvalue, '\n')

axiomsize1 = pd.read_csv('results\output_axiom_size.csv', header=None)
axiomsize2 = pd.read_csv('results\output_axiom_size2.csv', header=None)
axiomsize3 = pd.read_csv('results\output_axiom_size3.csv', header=None)
axsize1 = axiomsize1.values
axsize2 = axiomsize2.values
axsize3 = axiomsize3.values

axioms1 = pd.read_csv('results\output_axioms.csv', header=None)
axioms2 = pd.read_csv('results\output_axioms2.csv', header=None)
axioms3 = pd.read_csv('results\output_axioms3.csv', header=None)
ax1 = axioms1.values
ax2 = axioms2.values
ax3 = axioms3.values

definer1 = pd.read_csv('results\output_definers.csv', header=None)
definer2 = pd.read_csv('results\output_definers2.csv', header=None)
definer3 = pd.read_csv('results\output_definers3.csv', header=None)
def1 = definer1.values
def2 = definer2.values
def3 = definer3.values

restriction1 = pd.read_csv('results\output_restrictions.csv', header=None)
restriction2 = pd.read_csv('results\output_restrictions2.csv', header=None)
restriction3 = pd.read_csv('results\output_restrictions3.csv', header=None)
res1 = restriction1.values
res2 = restriction2.values
res3 = restriction3.values


fig, axs = plt.subplots(2,2,figsize=(30,30))
axs[0,0].plot(axsize1, label='ALCHTBoxForgetter')
axs[0,0].plot(axsize2, label='SHQTBoxForgetter')
axs[0,0].plot(axsize3, label='ALCOntologyForgetter')
axs[0,0].set_xlabel('Number of forgotten symbols')
axs[0,0].set_title('Axiom sizes for different forgetting methods')
axs[0,0].legend()

axs[1,0].plot(ax1, label='ALCHTBoxForgetter')
axs[1,0].plot(ax2, label='SHQTBoxForgetter')
axs[1,0].plot(ax3, label='ALCOntologyForgetter')
axs[1,0].set_xlabel('Number of forgotten symbols')
axs[1,0].set_title('Number of axioms for different forgetting methods')
axs[1,0].legend()

axs[0,1].plot(def1, label='ALCHTBoxForgetter')
axs[0,1].plot(def2, label='SHQTBoxForgetter')
axs[0,1].plot(def3, label='ALCOntologyForgetter')
axs[0,1].set_xlabel('Number of forgotten symbols')
axs[0,1].set_title('Number of definers for different forgetting methods')
axs[0,1].legend()

axs[1,1].plot(res1, label='ALCHTBoxForgetter')
axs[1,1].plot(res2, label='SHQTBoxForgetter')
axs[1,1].plot(res3, label='ALCOntologyForgetter')
axs[1,1].set_xlabel('Number of forgotten symbols')
axs[1,1].set_title('Number of restrictions for different forgetting methods')
axs[1,1].legend()

plt.show()

calcstat(ax1,ax2,'#axioms 1 vs #axioms 2')
calcstat(ax1,ax3,'#axioms 1 vs #axioms 3')
calcstat(ax2,ax3,'#axioms 2 vs #axioms 3')

calcstat(axsize1,axsize2,'axiomsize 1 vs axiomsize 2')
calcstat(axsize1,axsize3,'axiomsize 1 vs axiomsize 3')
calcstat(axsize2,axsize3,'axiomsize 2 vs axiomsize 3')

calcstat(def1,def2,'#definers 1 vs #definers 2')
calcstat(def1,def3,'#definers 1 vs #definers 3')
calcstat(def2,def3,'#definers 2 vs #definers 3')

calcstat(res1,res2,'#restrictions 1 vs #restrictions 2')
calcstat(res1,res3,'#restrictions 1 vs #restrictions 3')
calcstat(res2,res3,'#restrictions 2 vs #restrictions 3')