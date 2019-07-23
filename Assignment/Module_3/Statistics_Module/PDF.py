from scipy.stats import norm  ##This allows us to create a normalized probability density function
from scipy import stats       ##import poisson from scipy.stats
import numpy as np            ##This means that we reference the numpy module with the keyword, np
import scipy
import matplotlib.pyplot as plt #going to plot the data
import seaborn as sns
##PDF
x = np.arange(-4,4,0.001)
plt.plot(x,norm.pdf(x))      ##plot a normalized probability density function
plt.show()