# %% [markdown]
# Q3, a. Use Matlab (or any other computational environment of your choice) and simulate a one
# dimensional random walk where the probability to step to the right is α and to the left is β,
# such that α + β = 1. Plot the mean and standard deviation of the walker as a function of time
# and fit the data to obtain an analytic expression for the mean and standard deviation. Tune
# α, β to explore different regimes including the symmetric walk where α = β = 0.5

# %%
import matplotlib.pyplot as plt
import numpy as np
from random import choice
from scipy.optimize import curve_fit


def choice(probability):
    r = np.random.random()
    if r > probability:
        return 1
    else:
        return -1


def walk1d(n):

    walk=[]
    for j in range(n):
        position=[0]
        pos=0
        for i in range(n):
            pos+=choice(0.6)
            position.append(pos)
        walk.append(position)
        #print("walk=",walk)
    mean=np.mean(np.array(walk), axis=0)
    std=np.std(np.array(walk), axis=0)
    #print("mean=", mean)
    plt.plot(mean)
    plt.plot(std)
    plt.legend(['Mean', 'Standard Deviation'])
    plt.show()
    return mean, std


# def func1(x, a, b, c):
#     return a * x ** 2 + b * x + c
#
#
# def fit(mean, std):
#     params, covs = curve_fit(func1, x, y)
#     params, _ = curve_fit(func1, x, y)
#     a, b, c = params[0], params[1], params[2]
#     yfit1 = a*x**2+b*x+c
#     plt.plot(yfit1)





mean, std = walk1d(1000)


# %% [markdown]
# Q3, c. Next, simulate the symmetric random walk on a two-dimensional lattice (∆x, ∆y), with equal
# probabilities to choose any of their four nearest neighbour points for their next step after time
# ∆t. Plot the mean and standard deviation of the walker as a function of time and fit the data to
# obtain an analytic expression for the mean and standard deviation.

# %%
import matplotlib.pyplot as plt
import numpy as np
import random

def choice_2d():
    dx, dy = random.choice([(0,1),(0,-1),(1,0),(-1,0)])
    return dx, dy

def walk2d(n):
    walk2d=[]
    for j in range(n):
        position=[]
        posx=0
        posy=0
        for i in range(n):
            x, y = choice_2d()
            posx+=x
            posy+=y
            pos = np.sqrt((posx**2)+(posy**2))
            position.append(pos)
        walk2d.append(position)
    mean=np.mean(np.array(walk2d), axis=0)
    std=np.std(np.array(walk2d), axis=0)
    #print("mean=", mean)
    plt.plot(mean)
    plt.plot(std)
    plt.legend(['Mean', 'Standard Deviation'])
    plt.show()

walk2d(1000)


# %%
def walk2d_map(n):
    x_list=[]
    y_list=[]
    posx=0
    posy=0
    for i in range(n):
        x, y = choice_2d()
        posx+=x
        posy+=y
            #pos = np.sqrt((posx**2)+(posy**2))
        x_list.append(posx)
        y_list.append(posy)
    plt.plot(x_list,y_list, '.', markersize=2)
    plt.show()

walk2d_map(1000)

# %%
print()


