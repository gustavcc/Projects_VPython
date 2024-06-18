# -*- coding: utf-8 -*-

from visual import *

scene.background=color.white

scene.width=800
scene.height=800
scene.range=(12,12,12)

bloco = box(pos=(0,0,0), size=(2,2,2), color=color.red)
piso = box(pos=(0,-1.25,0), size=(15,0.5,10), color=color.orange)
parede = box(pos=(-7.25,1,0), size=(0.5,4,10), color=color.orange)
mola = helix(pos=(-7,0,0), axis=(7,0,0), radius=0.5,
    thickness=0.1, coils=10, color=color.yellow)

m = 10
k = 10
x = 2
x0 = 0
v = 0
v0 = 0
t = 0
dt = 0.07

while True:
    rate(100)
    
    a = -(k/m)*bloco.pos.x
    v += v0 + a*dt 
    x += x0 + v*dt 

    bloco.pos.x = x
    mola.axis = bloco.pos - parede.pos + (0,1,0)