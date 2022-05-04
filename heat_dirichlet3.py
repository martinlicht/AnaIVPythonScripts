#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np
import time 


N = 100
K  = 2*N*N

h = 1 / N
k = 1 / K


def f(x):
    [x1,x2] = divmod( x, 1.0 )
    if 0.4 < x2 < 0.6:
        return 0.005
    else: return 0

def u0(x):
    return 0

def u(x,t):
    return u0( x - t );


xs = [ i * h for i in range(0,N+1) ]
ts = [ i * k for i in range(0,K+1)  ]

fs = [ f(x) for x in xs ]

u_heat_new = [ u0(x) for x in xs ]
u_heat_old = u_heat_new

line_heat = plt.plot( xs, fs, color='blue',   label='heat' )
plt.xlim(0,1)
plt.ylim(-0.5,2)
plt.title ( "Dirichlet heat flow with constant source term\nt = 0" )
plt.legend( loc = "upper right")
plt.pause(4.05)
line_heat.pop(0).remove()


for t in ts:
    
    u_heat_old = u_heat_new
    for i in range(1,N):
        u_heat_new[i] = u_heat_old[i] + k / (h**2) * ( u_heat_old[i+1] - 2*u_heat_old[i] + u_heat_old[i-1] ) + fs[i]

    line_heat = plt.plot( xs, u_heat_old, color='red',   label='heat' )
    
    
    plt.xlim(0,1)
    plt.ylim(-0.5,2)
    plt.pause(0.05)
    plt.title ( "Dirichlet heat flow with constant source term\nt = {:10.6f}".format(t) )
    plt.legend( loc = "upper right")

    if t != ts[K-1]:
        line_heat.pop(0).remove()

    if t > 0.015:
        break
    
# plt.show()


