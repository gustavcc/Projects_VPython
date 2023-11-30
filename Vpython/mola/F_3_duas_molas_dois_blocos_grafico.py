from visual import *
from visual.graph import * # pacote de visualiza��o dos gr�ficos

scene.background=color.white
scene.width=800
scene.height=400
scene.range=(20,20,20)
scene.center=(0,0,0)

#------------------------------------------------------------------
#FUGURAS

bloco_1 = box(pos=(0,0,0), size=(2,2,2), color=color.blue)
bloco_2 = box(pos=(9.75,0,0), size=(2,2,2), color=color.black)

piso = box(pos=(0,-1.25,0), size=(20,0.5,10), color=color.orange)
parede_esquerda = box(pos=(-9.75,2,0), size=(0.5,6,10), color=color.orange)

mola_esquerda = helix(pos=(-9.75,0,0), axis=(8.75,0,0), radius=0.5,
    thickness=0.1, coils=10, color=color.red)

mola_direita = helix(pos=bloco_1.pos, axis=(8.75,0,0), radius=0.5,
    thickness=0.1, coils=10, color=color.yellow)


#CASO (ii)
#-------------------------------------------------------------------
# GRANDEZAS DO PROBLEMA

m = 5.

k = 1.

x1 = 2.
x2 = 2.

v1 = 0.
v2 = 0.


t = 0.
dt = 0.05

caixa_texto1 = label(pos=(3,5,0), text='x1 = %1.1f' % x1)
caixa_texto3 = label(pos=(9,5,0), text='x2 = %1.1f' % x2)
caixa_texto2 = label(pos=(-3,5,0), text='t = %1.1f' % t)

#-------------------------------------------------------------------
# ANIMACAO

while True:
    rate(100)

    t += dt

    a1 = (k/m)*(x2 - 2*x1)
    v1 += a1*dt
    x1 += v1*dt

    a2 = -(k/m)*(x2 - x1)
    v2 += a2*dt
    x2 += v2*dt

    bloco_1.pos.x = x1-4
    bloco_2.pos.x = x2+4

    mola_direita.pos.x = bloco_1.pos.x
    mola_esquerda.axis = bloco_1.pos.x - parede_esquerda.pos.x
    mola_direita.axis = bloco_2.pos.x - bloco_1.pos.x

    caixa_texto1.text='x1 = %1.2f' % x1
    caixa_texto3.text='x2 = %1.2f' % x2

    if t <= 20:
         caixa_texto2.text='t = %1.2f' % t

