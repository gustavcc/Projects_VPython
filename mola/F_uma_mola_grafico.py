from visual import* #pacote para visualiza��o da anima��o
from visual.graph import * # pacote de visualiza��o dos gr�ficos

#------------------------------------------------------------------
#CENA

scene.range=(12,12,12) # zoom em reala��o ao centro da tela
scene.center=(0,0,0)# centro da tela
scene.background=color.white #cor de fundo
scene.width = 800 # comprimento
scene.height = 400 #altura

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
          foreground=color.black, background=color.white) #TEMPO

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
#FUGURAS

bloco = box(pos=(0,0,0), size=(2,2,2),color=color.red)
piso = box(pos=(0,-1.25,0), size=(15,0.5,10), color=color.orange)
parede = box(pos=(-7.25,1,0), size=(0.5,4,10), color=color.orange)# parede esquerda
mola = helix(pos=vector(-7,0,0), axis=vector(7,2,0), radius=0.5, color=color.yellow,thickness=0.1, coils=10)

#-------------------------------------------------------------------
# GRANDEZAS DO PROBLEMA

m = 10
k = 10
x = 2 #posi��o de deslocamento da mola
x0 = 0 #posi��o de equilibrio da mola
v0 = 0 #velocidade inicial 
v = 0 #declarando a velocidade
t = 0 # instante de tempo inicial
dt = 0.01 #incremnto de tempo

caixa_texto1 = label(pos=(3,5,0), text='x = %1.1f' % x)
caixa_texto2 = label(pos=(-3,5,0), text='t = %1.1f' % t)

#-------------------------------------------------------------------
#ANIMA��O - F�SICA + PRPGRAMA��

while True:
    rate(100)

    t += dt
    a = -(k/m)*bloco.pos.x #ACELERA��O
    v += v0 + a*dt #VELOCIDADE
    x += x0 + v*dt #POSI��O

    bloco.pos.x = x #MOVIMENTO DO BLOCO
    mola.axis = bloco.pos - parede.pos + (0,1,0) #MOVIMENTO DA MOLA
    
    Ec = (m*v**2)/2 #ENERGIA CINETICA
    Epe = (k*x**2)/2 #ENERGIA POTENCIAL ELASTICA
    E = Ec + Epe #ENERGIA MECANICA

    caixa_texto1.text='x = %1.2f' % x

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
