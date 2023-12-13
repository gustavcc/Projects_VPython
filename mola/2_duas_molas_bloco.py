from visual import *
from visual.graph import * # pacote de visualiza��o dos gr�ficos

scene.background=color.white
scene.width=800
scene.height=400
scene.range=(20,20,20)
scene.center=(0,0,0)

#------------------------------------------------------------------
#FIGURAS

bloco = box(pos=(0,0,0), size=(2,2,2), color=color.blue)
piso = box(pos=(0,-1.25,0), size=(20,0.5,10), color=color.cyan)
parede_esquerda = box(pos=(-9.75,2,0), size=(0.5,6,10), color=color.cyan)
parede_direita = box(pos=(9.75,2,0), size=(0.5,6,10), color=color.cyan)
mola_esquerda = helix(pos=(-9.75,0,0), axis=(9.75,0,0), radius=0.5,
    thickness=0.1, coils=15, color=color.orange)
mola_direita = helix(pos=(9.75,0,0), axis=(-9.75,0,0), radius=0.5,
    thickness=0.1, coils=15, color=color.orange)

#-------------------------------------------------------------------
#DOIS CASOS: (i) k1 = k2 | (ii) k1 != k2
#-------------------------------------------------------------------

#CASO (i)
#-------------------------------------------------------------------
# GRANDEZAS DO PROBLEMA

m = 10
k1 = 10
k2 = 10
x = 4
x0 = 0
v = 0
v0 = 0
t = 0
dt = 0.04

caixa_texto = label(pos=(0,5,0), text='x = %1.1f' % x)

#-------------------------------------------------------------------
# ANIMACAO

while True:
    rate(100)

    a = -((k1+k2)/m)*bloco.pos.x
    v += v0 + a*dt
    x += x0 + v*dt

    caixa_texto.text='x = %1.2f' % x

    bloco.pos.x = x
    mola_esquerda.axis = bloco.pos - parede_esquerda.pos + (0,2,0)
    mola_direita.axis = bloco.pos - parede_direita.pos + (0,2,0)



#CASO (ii)
#-------------------------------------------------------------------
# GRANDEZAS DO PROBLEMA

    

