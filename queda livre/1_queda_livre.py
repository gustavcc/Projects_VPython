from visual import *

particula = sphere(pos=(0,0,0),radius=1, color = color.red)

piso = box(pos=(0,-20,0),size=(25,0.5,25), color = color.orange)

v = vector(0,0,0) #velocidade
y = particula.pos #posicao
g = vector(0,-10,0) #gravidade/acelera��o
dt = 0.01 #variacao do tempo

while True:
    rate(100)
    v += g*dt
    y += v*dt + 0.5*g*dt**2
    
    if particula.pos.y < (piso.pos.y + 1):
        v.y = -v.y
        while True:
            rate(100)
            v += -g*dt
            y += v*dt + 0.5*g*dt**2
            if particula.pos.y < vector(0,0,0):
                break