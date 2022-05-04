#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np
import time 

T=20

N = 100
K = T*N

h = 1 / N
k = T / K


def u0(x):
    return np.sin( 2 * np.pi * x )

def v0(x):
    return 0


xs = [ i * h for i in range(0,N+1) ]
ts = [ i * k for i in range(0,K+1)  ]


posi_then = [ u0(x) for x in xs ]
posi_now  = [ u0(x)+k*v0(x) for x in xs ]
posi_next = [ u0(x)+k*v0(x) for x in xs ]

line_wave = plt.plot( xs, posi_then, color='red',   label='displacement' )
plt.xlim(0,1)
plt.ylim(-1,1)
plt.title ( "Wave equation with Dirichlet boundary conditions\nt = 0" )
plt.legend( loc = "upper right")
plt.pause(1.05)
line_wave.pop(0).remove()


for j in range(0,K+1):
    
    if j % 2 == 0 or j==K:
        line_wave = plt.plot( xs, posi_now, color='red',   label='wave' )
        plt.xlim(0,1)
        plt.ylim(-1,1)
        plt.pause(0.01)
        plt.title ( "Wave equation with Dirichlet boundary conditions\nt = {:10.6f}".format( ts[j] ) )
        plt.legend( loc = "upper right")

        if j != K:
            line_wave.pop(0).remove()

    for i in range(1,N):
        posi_next[i] = np.sin( 2 * np.pi * xs[i] ) * np.cos( 2 * np.pi * ts[j] )
        # posi_next[i] = (k**2) / (h**2) * ( posi_now[i+1] - 2*posi_now[i] + posi_now[i-1] ) + 2 * posi_now[i] - posi_then[i]


    posi_then = posi_now
    posi_now  = posi_next

    
    
# plt.show()


