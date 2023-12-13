from visual import *
from visual.graph import *

#------------------------------------------------------------------
#CENA

scene.range=(20,20,20) # zoom em reala��o ao centro da tela
scene.center=(0,4,0)# centro da tela
scene.background=color.white #cor de fundo
scene.width = 800 # comprimento
scene.height = 400 #altura

#------------------------------------------------------------------
#TELA GR�FICO - INFORMA��ES PARA A TELA DO GR�FICO

grafico1 = gdisplay(width=800, height=400, 
          title='E vs. y', xtitle='y(m)', ytitle='E(J)',
                    
          xmax=3., xmin=-3., ymax=20, ymin=0, 
          foreground=color.black, background=color.white) #ENERGIA CINETICA

grafico2 = gdisplay(width=800, height=400, 
          title='E vs. t', xtitle='t(s)', ytitle='E(J)', 
          xmax=20, xmin=0, ymax=20, ymin=0, 
          foreground=color.black, background=color.white) #ENERGIA POTENCIAL

grafico3 = gdisplay(width=800, height=400, 
          title='Y vs. t | V vs. t', xtitle='t(s)', ytitle='Y(m) | V(m/s)', 
          xmax=20, xmin=0, ymax=2.6, ymin=-2.6, 
          foreground=color.black, background=color.white) #TEMPO

#------------------------------------------------------------------
#PLOTAR FUN��ES - INFORMA��ES PARA A CURVA DO GR�FICO

funcao1_y = gdots(gdisplay=grafico1,color=color.red) #energia cin�tica
funcao2_y = gdots(gdisplay=grafico1,color=color.green) #energia potencial
funcao3_y = gdots(gdisplay=grafico1,color=color.black) #energia mecanica

funcao1_t = gdots(gdisplay=grafico2,color=color.red) #energia cin�tica
funcao2_t = gdots(gdisplay=grafico2,color=color.green) #energia potencial
funcao3_t = gdots(gdisplay=grafico2,color=color.black) #energia mecanica

funcao1_metros = gdots(gdisplay=grafico3, color=color.red) #distancia em função do tempo
funcao2_velocidade = gdots(gdisplay=grafico3, color=color.green) #velocidade em função do tempo

#------------------------------------------------------------------
#FUGURAS

bola = sphere(pos=(0,0,0), radius=2, material = materials.earth, color = color.cyan)

teto = box(pos=(0,10,0), size=(20,0.5,10), color=color.cyan)

mola = helix(pos=(0,9.75,0), axis=(0,-8,0), radius=0.5,
    thickness=0.1, coils=10, color=color.red)

#-------------------------------------------------------------------
# GRANDEZAS DO PROBLEMA

m = 10
k = 10
y = 2 #posi��o de deslocamento da mola
y0 = 0 #posi��o de equilibrio da mola
v0 = 0 #velocidade inicial 
v = 0 #declarando a velocidade
t = 0 # instante de tempo inicial
dt = 0.009 #incremnto de tempo

caixa_texto1 = label(pos=(3,5,0), text='y = %1.1f' % y)
caixa_texto2 = label(pos=(-3,5,0), text='t = %1.1f' % t)

#-------------------------------------------------------------------
#ANIMA��O - F�SICA + PRPGRAMA��

while True:
    rate(100)

    t += dt
    a = -(k/m)*bola.pos.y #ACELERA��O
    v += v0 + a*dt #VELOCIDADE
    y += y0 + v*dt #POSI��O

    bola.pos.y = y #MOVIMENTO DO BLOCO
    mola.axis = bola.pos - teto.pos + (0,0.5,0) #MOVIMENTO DA MOLA
    
    Ec = (m*v**2)/2 #ENERGIA CINETICA
    Epe = (k*y**2)/2 #ENERGIA POTENCIAL ELASTICA
    E = Ec + Epe #ENERGIA MECANICA

    caixa_texto1.text='y = %1.2f' % y

    if t <= 20:
        funcao1_y.plot(pos=(y,Ec)) #plotando a energia cinetica em funcao de x
        funcao2_y.plot(pos=(y,Epe)) #plotando a energia potencial em funcao de x
        funcao3_y.plot(pos=(y,E)) #plotando a energia meconica em funcao de x

        funcao1_t.plot(pos=(t,Ec)) #plotando a energia cinetica em funcao de t
        funcao2_t.plot(pos=(t,Epe)) #plotando a energia potencial em funcao de t
        funcao3_t.plot(pos=(t,E)) #plotando a energia meconica em funcao de t

        funcao1_metros.plot(pos=(t,y)) #plotando a distancia em funçao do tempo
        funcao2_velocidade.plot(pos=(t,v)) #plotando a distancia em funçao do tempo

        caixa_texto2.text='t = %1.2f' % t
