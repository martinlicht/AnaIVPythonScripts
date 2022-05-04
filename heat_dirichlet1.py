#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np
import time 


N = 100
K  = 2*N*N

h = 1 / N
k = 1 / K


def u0(x):
    # return 1 + 0.2 * np.sin( 2 * np.pi * (x) )
    
    [x1,x2] = divmod( x, 1.0 )
    if 0.251 < x2 < 0.749:
        return 0.5
    else: return 0

def u(x,t):
    return u0( x - t );


xs = [ i * h for i in range(0,N+1) ]
ts = [ i * k for i in range(0,K+1)  ]

u_heat_new = [ u0(x) for x in xs ]
u_heat_old = u_heat_new

line_heat = plt.plot( xs, u_heat_old, color='red',   label='heat' )
plt.xlim(0,1)
plt.ylim(-0.5,1)
plt.title ( "Dirichlet heat flow with initial heat block\nt = 0" )
plt.legend( loc = "upper right")
plt.pause(4.05)
line_heat.pop(0).remove()


for t in ts:
    
    line_heat = plt.plot( xs, u_heat_old, color='red',   label='heat' )
    
    plt.xlim(0,1)
    plt.ylim(-0.5,1)
    plt.pause(0.05)
    plt.title ( "Dirichlet heat flow with initial heat block\nt = {:10.6f}".format(t) )
    plt.legend( loc = "upper right")

    if t != ts[K]:
        line_heat.pop(0).remove()

    

    u_heat_old = u_heat_new
    for i in range(1,N):
        u_heat_new[i] = u_heat_old[i] + k / (h**2) * ( u_heat_old[i+1] - 2*u_heat_old[i] + u_heat_old[i-1] ) 

    if t > 0.015:
        break
    
# plt.show()


