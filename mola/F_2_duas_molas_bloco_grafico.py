from visual import *
from visual.graph import * # pacote de visualiza��o dos gr�ficos

scene.background=color.white
scene.width=800
scene.height=400
scene.range=(20,20,20)
scene.center=(0,0,0)

#------------------------------------------------------------------
#TELA GR�FICO - INFORMA��ES PARA A TELA DO GR�FICO

grafico1 = gdisplay(width=800, height=400, 
          title='E vs. x', xtitle='x(m)', ytitle='E(J)',
                    
          xmax=3., xmin=-3., ymax=20, ymin=0, 
          foreground=color.black, background=color.white) #ENERGIA CINETICA

grafico2 = gdisplay(width=800, height=400, 
          title='E vs. t', xtitle='t(s)', ytitle='E(J)', 
          xmax=20, xmin=0, ymax=20, ymin=0, 
          foreground=color.black, background=color.white) #ENERGIA POTENCIAL

grafico3 = gdisplay(width=800, height=400, 
          title='X vs. t | V vs. t', xtitle='t(s)', ytitle='X(m) | V(m/s)', 
          xmax=20, xmin=0, ymax=5, ymin=-5, 
          foreground=color.black, background=color.white) #TEMP

#------------------------------------------------------------------
#PLOTAR FUN��ES - INFORMA��ES PARA A CURVA DO GR�FICO

funcao1_x = gdots(gdisplay=grafico1,color=color.red) #energia cin�tica
funcao2_x = gdots(gdisplay=grafico1,color=color.green) #energia potencial
funcao3_x = gdots(gdisplay=grafico1,color=color.black) #energia mecanica

funcao1_t = gdots(gdisplay=grafico2,color=color.red) #energia cin�tica
funcao2_t = gdots(gdisplay=grafico2,color=color.green) #energia potencial
funcao3_t = gdots(gdisplay=grafico2,color=color.black) #energia mecanica

funcao1_metros = gdots(gdisplay=grafico3, color=color.red) #distancia em função do tempo
funcao2_velocidade = gdots(gdisplay=grafico3, color=color.green) #velocidade em função do tempo

#------------------------------------------------------------------
#FIGURAS

bloco = box(pos=(0,0,0), size=(2,2,2), color=color.blue)
piso = box(pos=(0,-1.25,0), size=(20,0.5,10), color=color.cyan)
parede_esquerda = box(pos=(-9.75,2,0), size=(0.5,6,10), color=color.cyan)
parede_direita = box(pos=(9.75,2,0), size=(0.5,6,10), color=color.cyan)
mola_esquerda = helix(pos=(-9.75,0,0), axis=(9.75,0,0), radius=0.5,
    thickness=0.1, coils=10, color=color.orange)
mola_direita = helix(pos=(9.75,0,0), axis=(-9.75,0,0), radius=0.5,
    thickness=0.1, coils=10, color=color.orange)

#-------------------------------------------------------------------
#DOIS CASOS: (i) k1 = k2 | (ii) k1 != k2
#-------------------------------------------------------------------

#CASO (ii)
#-------------------------------------------------------------------
# GRANDEZAS DO PROBLEMA

m = 10
k1 = 5
k2 = 5
x = 2
x0 = 0
v = 0
v0 = 0
t = 0
dt = 0.009

caixa_texto = label(pos=(3,5,0), text='x = %1.1f' % x)
caixa_texto2 = label(pos=(-3,5,0), text='t = %1.1f' % t)

#-------------------------------------------------------------------
# ANIMACAO

while True:
    rate(100)

    t += dt
    a = -((k1+k2)/m)*bloco.pos.x
    v += v0 + a*dt
    x += x0 + v*dt

    caixa_texto.text='x = %1.2f' % x

    bloco.pos.x = x
    mola_esquerda.axis = bloco.pos - parede_esquerda.pos + (0,2,0)
    mola_direita.axis = bloco.pos - parede_direita.pos + (0,2,0)

    Ec = (m*v**2)/2
    Epe = ((k1 + k2)*x**2)/2
    E = Ec + Epe

    if t <= 20:
        funcao1_x.plot(pos=(x,Ec)) #plotando a energia cinetica em funcao de x
        funcao2_x.plot(pos=(x,Epe)) #plotando a energia potencial em funcao de x
        funcao3_x.plot(pos=(x,E)) #plotando a energia meconica em funcao de x

        funcao1_t.plot(pos=(t,Ec)) #plotando a energia cinetica em funcao de t
        funcao2_t.plot(pos=(t,Epe)) #plotando a energia potencial em funcao de t
        funcao3_t.plot(pos=(t,E)) #plotando a energia meconica em funcao de t

        funcao1_metros.plot(pos=(t,x)) #plotando a distancia em funçao do tempo
        funcao2_velocidade.plot(pos=(t,v)) #plotando a distancia em funçao do tempo

        caixa_texto2.text='t = %1.2f' % t





    

