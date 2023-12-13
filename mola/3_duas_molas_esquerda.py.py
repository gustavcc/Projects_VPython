from visual import *

scene.background=color.white
scene.width=1080
scene.height=720
scene.range=(20,20,20)
scene.center=(0,0,0)

#------------------------------------------------------------------
#FUGURAS

bloco = box(pos=(7,1,0), size=(4,4,4), color=color.blue)

piso = box(pos=(0,-1.25,0), size=(20,0.5,10), color=color.cyan)

parede_esquerda = box(pos=(-9.75,2,0), size=(0.5,6,10), color=color.cyan)

mola_esquerda = helix(pos=(-9.75,1,0), axis=(7.75,0,0), radius=0.5,
    thickness=0.1, coils=10, color=color.red)

mola_direita = helix(pos=(-2,1,0), axis=(7.75,0,0), radius=0.5,
    thickness=0.1, coils=10, color=color.yellow)
