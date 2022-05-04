#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np
import time 


N = 100
K  = 2*N*N

h = 1 / N
k = 1 / K


def u0(x):
    return 2*( 0.5-abs(0.5-x) )

def u(x,t):
    return u0( x - t );


xs = [ i * h for i in range(0,N+1) ]
ts = [ i * k for i in range(0,K+1)  ]

u_heat_new = [ u0(x) for x in xs ]
u_heat_old = u_heat_new

line_heat = plt.plot( xs, u_heat_old, color='red',   label='heat' )
plt.xlim(0,1)
plt.ylim(-0.5,2)
plt.title ( "Dirichlet heat flow with initial heat peak\nt = 0" )
plt.legend( loc = "upper right")
plt.pause(4.05)
line_heat.pop(0).remove()


for t in ts:
    
    u_heat_old = u_heat_new
    for i in range(1,N):
        u_heat_new[i] = u_heat_old[i] + k / (h**2) * ( u_heat_old[i+1] - 2*u_heat_old[i] + u_heat_old[i-1] ) 

    line_heat = plt.plot( xs, u_heat_old, color='red',   label='heat' )
    
    
    plt.xlim(0,1)
    plt.ylim(-0.5,2)
    plt.pause(0.05)
    plt.title ( "Dirichlet heat flow with initial heat peak\nt = {:10.6f}".format(t) )
    plt.legend( loc = "upper right")

    if t != ts[K-1]:
        line_heat.pop(0).remove()

    if t > 0.015:
        break
    
# plt.show()


