import pygame
from random import randint
pygame.init()


#medidas usadas
largura = 300
altura = 600
comprimentos = (300,600)

#criando tela
tela = pygame.display.set_mode(comprimentos)

#legenda
pygame.display.set_caption("car game")

#fps
relogio=pygame.time.Clock()

#imagens usadas
carro_imagem=pygame.image.load("car7.jpg")
fundo = pygame.image.load("download12.jpg")
faixa_amarela=pygame.image.load("yellow strip.jpg")
#faixa=pygame.image.load("strip.jpg")

#carro azul
foto_obstaculo1 = pygame.image.load("car2.jpg")

#carro roxo
foto_obstaculo2 = pygame.image.load("car4.jpg")

#foto menu
roda_menu = pygame.image.load("burning_wheel.png")

#musicas
#music = pygame.mixer.music.load("tokyo_bits.ogg")
music = pygame.mixer.music.load("top_gear_music.ogg")
#car_moving=pygame.mixer.Sound("engine_start.wav")


#variáveis usadas para limitar a movimentação
carro_largura = 56
obstaculo_altura=125


#Cores
preto = (0,0,0)
amarelo = (234,226,72)
vermelho = (255,0,21)
cinza = (118, 123, 132)
branco = (255,255,255)

#fonte
font = pygame.font.SysFont(None, 20)
font_upper = pygame.font.SysFont(None, 50)

#função usada para criar texto
def texto(msg, cor, larg, alt,fonte):
    #A função render() poe o texto em uma superfície
    texto1 = fonte.render(msg, True, cor)
    #No pygame nao existe uma funçao para inserir diretamente
    # o texto na tela
    # por isso eu uso:
    tela.blit(texto1, [larg, alt])
    # A superficie onde eu irei blitar o texto é o fundo
    
#função usada para por os objetos do fundo na tela
def Fundo():
    tela.blit(fundo,(-50,0))
    #tela.blit(fundo,(0,200))
    #tela.blit(fundo,(0,400))
    tela.blit(fundo, (350, 0))
    #tela.blit(fundo, (700,200))
    #tela.blit(fundo, (700,400))
    


#função que cria os obstaculos
def obstaculo(obs_x, obs_y, obs_pic):
   
   tela.blit(obs_pic, (obs_x, obs_y))

#variavel acrescimo de posiçao y

_y_ = 0

mudar = 0

#objetos que vão se mover
def objetos_fundo(obs_faixa_x, obs_faixa_y):
    global _y_
    global mudar
    for step in range(0, 3*65+1, 65):
        tela.blit(faixa_amarela, (obs_faixa_x, obs_faixa_y+ step + _y_))
        mudar = obs_faixa_y+ step + _y_
        _y_ += 2

#função que cria o carro
def carro(x,y):
    tela.blit(carro_imagem,(x,y))


#função que roda o jogo
def game():
    
    #variáveis posição do carro
    x=(largura*0.45)
    y=(altura*0.8)
    
    #variaveis movimentação, carro
    pos_x=0
    pos_y=0
    
    #variaveis de movimentação, obstáculo0
    obs_x=largura/3
    obs_y=0
    obs_vel=5
    
    #variaveis de movimentação, obstáculo1
    obs_x1=largura/3 + 130
    obs_y1=100
    obs_vel1=5.7

    #variaveis da movimentação, 
    obs_faixa_x = largura/2
    #modulos de mudanças de tela
    sair = True
    menu = True
    bateu = False

    #música de fundo
    pygame.mixer.music.play(-1)
    
    while menu:
        tela.fill(branco)
        tela.blit(roda_menu, (largura/5, altura/5))
        
        texto("PRESS SPACE TO PLAY", vermelho, largura/7, altura/4,font)
        texto("PRESS Q TO QUIT", vermelho, largura/7, altura/3, font)
        pygame.display.update()
        for event in pygame.event.get():
                
            if event.type ==  pygame.QUIT:
                menu = False
                sair = False
                bateu = False
                        
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menu = False
                if event.key == pygame.K_q:
                    menu = False
                    sair = False
                    bateu = False

    if menu == False:                    
        while sair:
            while bateu:
                tela.fill(preto)
                texto("YOUR LOSEEEEE!!!", vermelho, largura/7, altura/5, font)
                texto("Press q to quit(ur sucker)", vermelho, largura/7, altura/3.9, font )
                texto("Press c to continue(ur idiot)", vermelho, largura/7, altura/3, font)
                pygame.display.update()
                for event in pygame.event.get():
                
                    if event.type ==  pygame.QUIT:
                        sair = False
                        bateu = False
                
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            sair = False
                            bateu = False
                        if event.key == pygame.K_c:
                            game()
            for event in pygame.event.get():
                
                if event.type ==  pygame.QUIT:
                    sair = False
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sair = False
                        
                    if event.key == pygame.K_LEFT:
                        pos_x=-5
                        pos_y=0
                        #car_moving.play()
                    if event.key == pygame.K_RIGHT:
                        pos_x=5
                        pos_y=0
                        #car_moving.play()
                if event.type == pygame.KEYUP:
                    if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                        pos_x=0
                        pos_y=0
            

            #gera o movimento dos obstaculos
            obs_y+=obs_vel
            obs_y1+=obs_vel1
            
            #gera a variaçao do movimento do carro
            x+=pos_x
            y+=pos_y
            
            tela.fill(cinza)
            #chama o background
            Fundo()
            
            #cria o carro
            carro(x,y)
            
            #cria os obstaculos
            
            '''azul'''
            obstaculo(obs_x, obs_y, foto_obstaculo1)
            
            '''roxo'''
            obstaculo(obs_x1, obs_y1, foto_obstaculo2)
            
            objetos_fundo(largura/2, 0)
            
            
            #se o carro bater na lateral o jogo dá endgame
            if x>380-carro_largura or x<50:
                bateu = True
            

            #fazer o obstaculo ficar em looping
            if obs_y> altura-obstaculo_altura:
                obs_y = -10
                obs_x = randint(50, 96)
                #print(obs_x)
                #obstaculo(obs_x1, obs_y1, foto_obstaculo2)
                #pygame.display.update()

            #fazer o obstaculo ficar em looping
            if obs_y1> altura-obstaculo_altura:
                obs_y1 = -10
                obs_x1 = randint(190, 244) 
                print(obs_x1)
                #obstaculo(obs_x1, obs_y1, foto_obstaculo1)
                #pygame.display.update()
            global mudar
            #print(mudar)
            global _y_
            if (mudar >= 800):
                _y_ = 0
                

            
            #usada para atualizar a tela
            pygame.display.update()
            #definir o fps
            relogio.tick(60)

game()
pygame.quit()
