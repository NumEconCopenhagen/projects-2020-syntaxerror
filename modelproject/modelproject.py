import numpy as np
from scipy import optimize
#%matplotlib inline
import matplotlib.pyplot as plt


def keynesian_cross(T, I, G, C):
    """ Draws the Keynesian cross with the 45-degree line and 
    the planned total spending as a function of total production.
    
    Args:
        T (float): Taxs
        a (float): Constant consumption, a>0
        G (float): Public consumption
        I (float): Investment
        C (float): Consumption
       
    Return: Figure
    """
    # The data vector to be plotted for production and aggregate expenditure:
    Y_arrey = np.linspace(0,300)
    PE_arrey = (C * (Y_arrey - T) + I + G)
    degree = Y_arrey

    # The figure
    fig = plt.figure(figsize=(10,5))
    ax = fig.add_subplot(1,1,1)

    ax.plot(Y_arrey, degree, label="45-degree line", color='lightblue',linewidth=3)
    ax.plot(Y_arrey, AD_arrey, label="AD=C+I+G+NX", color='darkorange',linewidth=3)

    ax.set_xlabel("Y")
    ax.set_ylabel("PE")
    ax.legend(loc="upper left")

    ax.grid()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    return
