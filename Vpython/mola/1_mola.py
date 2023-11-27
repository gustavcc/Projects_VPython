from visual import *

# CENA
# cor de fundo da cena:
scene.background=color.white

# tamanho da tela da cena e vizualização:
scene.width=800
scene.height=800
scene.range=(12,12,12)

#------------------------------------------------------------------
#FUGURAS

bloco = box(pos=(0,0,0), size=(2,2,2), color=color.red)
piso = box(pos=(0,-1.25,0), size=(15,0.5,10), color=color.orange)
parede = box(pos=(-7.25,1,0), size=(0.5,4,10), color=color.orange)
mola = helix(pos=(-7,0,0), axis=(7,0,0), radius=0.5,
    thickness=0.1, coils=10, color=color.yellow)

# MOLA:
        # exis: eiro da mola, em linha
        # thickness: espessura
        # coils: quantidade de aneis

#-------------------------------------------------------------------
# GRANDEZAS DO PROBLEMA

m = 10
k = 10
x = 2
x0 = 0
v = 0
v0 = 0
t = 0
dt = 0.07 # -> aqui temos o quão raoido o códiro irá rodar, definir a wquantidade de
         # de erros, pois o código não é contínuo, mas é dividido em pontos.

#-------------------------------------------------------------------
#ANIMAÇÃO - FÍSICA + PRPGRAMAÇÃ

while True:
    rate(100) #aqui temos o quão raoido o códiro irá rodar, definir a wquantidade de
              # de erros, pois o código não é contínuo, mas é dividido em pontos.
              
    a = -(k/m)*bloco.pos.x # ACELERAÇÃO: posição do bloco
    v += v0 + a*dt # VELOCIDADE
    x += x0 + v*dt # POSIÇÃO

    bloco.pos.x = x # relacionando as equações ao bloco
    mola.axis = bloco.pos - parede.pos + (0,1,0)
    # - parede.pos: a mola fica fixa na parede, anula a distancia da parede
    # o bloco está se movimentando apenas até a pos 0





