from visual import *

scene.background=color.white
scene.width=1080
scene.height=720
scene.range=(20,20,20)
scene.center=(0,5,0)

#------------------------------------------------------------------
#FUGURAS

bloco = box(pos=(0,0,0), size=(4,4,4), color=color.blue)

teto = box(pos=(0,10,0), size=(20,0.5,10), color=color.cyan)

mola = helix(pos=(0,9.75,0), axis=(0,-8,0), radius=0.5,
    thickness=0.1, coils=10, color=color.red)
