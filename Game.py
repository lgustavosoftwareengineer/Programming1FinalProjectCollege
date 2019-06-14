import pygame
from random import randint
pygame.init()

largura = 800
altura = 600
comprimentos = (800,600)
tela = pygame.display.set_mode(comprimentos)
pygame.display.set_caption("car game")
relogio=pygame.time.Clock()

#imagens usadas
carro_imagem=pygame.image.load("car1.jpg")
fundo = pygame.image.load("download12.jpg")
faixa_amarela=pygame.image.load("yellow strip.jpg")
faixa=pygame.image.load("strip.jpg")
foto_obstaculo1 = pygame.image.load("car2.jpg")
foto_obstaculo2 = pygame.image.load("car4.jpg")

#musicas
music = pygame.mixer.music.load("tokyo_bits.ogg")
#car_moving=pygame.mixer.Sound("engine_start.wav")


carro_largura = 56
obstaculo_altura=125


#Cores
preto = (0,0,0)
amarelo = (234,226,72)
vermelho = (255,0,21)
cinza = (178, 171, 171)

#fonte
font = pygame.font.SysFont(None, 20)


    
    


def texto(msg, cor, larg, alt,):
    #A função render() poe o texto em uma superfície
    texto1 = font.render(msg, True, cor)
    #No pygame nao existe uma funçao para inserir diretamente
    # o texto na tela
    # por isso eu uso:
    tela.blit(texto1, [larg, alt])
    
    # A superficie onde eu irei blitar o texto é o fundo
    
def Fundo():
    tela.blit(fundo,(0,0))
    #tela.blit(fundo,(0,200))
    #tela.blit(fundo,(0,400))
    tela.blit(fundo, (700, 0))
    #tela.blit(fundo, (700,200))
    #tela.blit(fundo, (700,400))
    tela.blit(faixa_amarela, (largura / 2, 100))
    tela.blit(faixa_amarela, (largura/2,200))
    tela.blit(faixa_amarela, (largura/2,300))
    tela.blit(faixa_amarela, (largura / 2, 400))
    tela.blit(faixa_amarela, (largura / 2, 500))


#função que cria os obstaculos
def obstaculo(obs_x, obs_y, obs_pic):
    
    tela.blit(obs_pic, (obs_x, obs_y))


def carro(x,y):
    tela.blit(carro_imagem,(x,y))



def game():
    x=(largura*0.45)
    y=(altura*0.8)
    
    pos_x=0
    pos_y=0
    
    obs_x=largura/3
    obs_y=0
    obs_vel=5
    
    obs_x1=largura/3 + 130
    obs_y1=100
    obs_vel1=5.7

    sair = True
    menu = False
    bateu = False
    pygame.mixer.music.play(-1)
    while sair:
        while bateu:
            tela.fill(preto)
            texto("YOUR LOSEEEEE!!!", vermelho, largura/2, altura/2)
            texto("Press q to quit(ur sucker)", vermelho, largura/2, altura/1.8 )
            texto("Press c to continue(ur idiot)", vermelho, largura/2, altura/1.7)
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
        obstaculo(obs_x, obs_y, foto_obstaculo1)
        obstaculo(obs_x1, obs_y1, foto_obstaculo2)
        
        
        #se o carro bater na lateral o jogo dá endgame
        if x>680-carro_largura or x<110:
            bateu = True
        

        #fazer o obstaculo ficar em looping
        if obs_y> altura-obstaculo_altura:
            obs_y = 0
            obs_x = randint(140, 400)

        #fazer o obstaculo ficar em looping
        if obs_y1> altura-obstaculo_altura:
            obs_y1 = 0
            obs_x1 = randint(450, largura-150)  

          

        
    
        pygame.display.update()
        relogio.tick(60)

game()
pygame.quit()
