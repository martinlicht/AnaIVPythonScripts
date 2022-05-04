#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np
import time 

# geometry 
L = 20
N = 1000
h = L / N

xs = [ i * h - L/2 for i in range(0,N+1) ]


# series

K = 25
A0 = 0.5
As = [ 0 for k in range(0,K) ]
Bs = [ 0 for k in range(0,K) ]
Bs = [ -1/( np.pi * k ) for k in range(1,K+1) ]

us = [ A0 for x in xs ]



# original function 

def f(x):
    # if x < 0:
    #     x = -x
    y = x % ( 2*np.pi )
    return y / ( 2*np.pi )
    if y < np.pi:
        return y
    else:
        return 0.

fs = [ f(xs[i]) for i in range(0,N+1) ]

es = [ 0.5 for i in range(0,N+1) ]


for k in range(1,K+1):
    
    Ak = As[k-1]
    Bk = Bs[k-1]
    
    for i in range(0,N+1):
        us[i] = us[i] + Ak * np.cos( (k) * xs[i] )
        us[i] = us[i] + Bk * np.sin( (k) * xs[i] )

    # if k%2 == 0:
    #     es[i] = es[i] + np.sin( k * xs[i] ) / k


    line_u = plt.plot( xs, us, color='red',  label='approx'   )
    line_f = plt.plot( xs, fs, color='blue', label='function' )
    
    
    plt.xlim(-L/2,L/2)
    plt.ylim(-0.2,1.2)
    plt.title ( "a_0 = 0,   a_k = 0,   b_k = -1/( pi k )\nN = {}".format(k) )
    plt.legend( loc = "upper right")
    plt.pause(1.000)
    
    if k != K:
        line_u.pop(0).remove()
        line_f.pop(0).remove()
    
# plt.show()


