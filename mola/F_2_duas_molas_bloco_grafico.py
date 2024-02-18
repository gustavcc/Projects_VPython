#---------------------------------------------#
# MASSA - DUAS MOLAS FIXAS
#---------------------------------------------#

from visual import * # biblioteca para atribuir as formas 3D
from visual.graph import * # biblioteca de visualizacao dos greficos

#---------------------------------------------#
# CENA - TAMNHO E POSICAO DA JANELA
#---------------------------------------------#
scene.background=color.white
scene.width=800
scene.height=400
scene.range=(20,20,20)
scene.center=(0,0,0)

#---------------------------------------------#
# GRAFICO - INFORMACOES PARA A TELA DO GRAFICO
#---------------------------------------------#
grafico1 = gdisplay(width=800, height=400, 
    title='Ec vs. x | Ep vs. x | E vs. x', xtitle='x(m)', ytitle='Energia(J)', 
    xmax=3., xmin=-3., ymax=20, ymin=0, 
    foreground=color.black, background=color.white) # ENERGIA EM FUNCAO DO POSICAO

grafico2 = gdisplay(width=800, height=400, 
    title='Ec vs. t | Ep vs. t | E vs. t', xtitle='t(s)', ytitle='Energia(J)', 
    xmax=20, xmin=0, ymax=20, ymin=0, 
    foreground=color.black, background=color.white) # ENERGIAS EM FUNCAO DO TEMPO

grafico3 = gdisplay(width=800, height=400, 
    title='X vs. t | V vs. t | a vs. t' , xtitle='t(s)', ytitle='X(m) | V(m/s) | a(m/s²)', 
    xmax=20, xmin=0, ymax=5, ymin=-5, 
    foreground=color.black, background=color.white) # MEDIDAS EM FUNCAO DO TEMPO

#---------------------------------------------#
# CRIAR FUNCOES - INFORMACOES PARA A CURVA DO GRAFICO
#---------------------------------------------#
funcao_cinetica_x = gdots(gdisplay=grafico1,color=color.red) # energia cinetica
funcao_potencial_x = gdots(gdisplay=grafico1,color=color.green) # energia potencial
funcao_mecanica_x = gdots(gdisplay=grafico1,color=color.black) # energia mecanica

funcao_cinetica_t = gdots(gdisplay=grafico2,color=color.red) # energia cinetica
funcao_potencial_t = gdots(gdisplay=grafico2,color=color.green) # energia potencial
funcao_mecanica_t = gdots(gdisplay=grafico2,color=color.black) # energia mecanica

funcao_metros = gdots(gdisplay=grafico3, color=color.orange) # posicao em função do tempo
funcao_velocidade = gdots(gdisplay=grafico3, color=color.blue) # velocidade em função do
funcao_aceleracao = gdots(gdisplay=grafico3, color=color.black) # aceleracao em função do tempo

#---------------------------------------------#
# FIGURAS - ESTRUTURAS 3D
#---------------------------------------------#
bloco = box(pos=(0,0,0), size=(2,2,2), color=color.blue)
                    
piso = box(pos=(0,-1.25,0), size=(20,0.5,10), color=color.cyan)
                    
parede_esquerda = box(pos=(-9.75,2,0), size=(0.5,6,10), color=color.cyan)
                    
parede_direita = box(pos=(9.75,2,0), size=(0.5,6,10), color=color.cyan)
                    
mola_esquerda = helix(pos=(-9.75,0,0), axis=(9.75,0,0), radius=0.5,
    thickness=0.1, coils=10, color=color.orange)
                    
mola_direita = helix(pos=(9.75,0,0), axis=(-9.75,0,0), radius=0.5,
    thickness=0.1, coils=10, color=color.orange)

#---------------------------------------------#
# GRANDEZAS DO PROBLEMA
#---------------------------------------------#
# CASO GERAL: k1 (1° constante - mola 1) e k2 (2° constante - mola 2)

m = 10 # massa do bloco
k1 = 5 # 1° contante
k2 = 5 # 2° constante
x = 2 # distancia que a mola pode deformar
x0 = 0 # posicao inicial
v = 0 # volocidade
v0 = 0 # vecolidade inicial
t = 0 # tempo para usar nos graficos
dt = 0.009 # variacao do tempo (formulas)

caixa_texto = label(pos=(3,5,0), text='x = %1.1f' % x) # cria a distancia em forma de texto
caixa_texto2 = label(pos=(-3,5,0), text='t = %1.1f' % t) # cria o tempo em forma de texto

#---------------------------------------------#
# ANIMACAO - O QUE FAZ TUDO FUNCIONAR
#---------------------------------------------#
                    
while True:
    rate(100)

    t += dt
    a = -((k1+k2)/m)*bloco.pos.x
    v += v0 + a*dt
    x += x0 + v*dt

    caixa_texto.text='x = %1.2f' % x # mostra a distancia em forma de texto

    bloco.pos.x = x
    mola_esquerda.axis = bloco.pos - parede_esquerda.pos + (0,2,0)
    mola_direita.axis = bloco.pos - parede_direita.pos + (0,2,0)

    Ec = (m*v**2)/2
    Ep = ((k1 + k2)*x**2)/2
    E = Ec + Ep

    #---------------------------------------------#
    # EXECUTANDO AS FUNCOES
    #---------------------------------------------#
    if t <= 20:
        funcao_cinetica_x.plot(pos=(x,Ec)) # plotando (imagem) a energia cinetica em funcao de x
        funcao_potencial_x.plot(pos=(x,Ep)) # plotando (imagem) a energia potencial em funcao de x
        funcao_mecanica_x.plot(pos=(x,E)) # plotando (imagem) a energia meconica em funcao de x

        funcao_cinetica_t.plot(pos=(t,Ec)) # plotando (imagem) a energia cinetica em funcao de t
        funcao_potencial_t.plot(pos=(t,Ep)) # plotando (imagem) a energia potencial em funcao de t
        funcao_mecanica_t.plot(pos=(t,E)) # plotando (imagem) a energia meconica em funcao de t

        funcao_metros.plot(pos=(t,x)) # plotando (imagem) a distancia em funçao do tempo
        funcao_velocidade.plot(pos=(t,v)) # plotando (imagem) a distancia em funçao do tempo
        funcao_aceleracao.plot(pos=(t,a)) # plotando (imagem) a distancia em funçao do tempo

        caixa_texto2.text='t = %1.2f' % t # mostra o tempo em forma de texto
