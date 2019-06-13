import pygame
import random
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
carro_largura = 56


#Cores
preto = (0,0,0)
amarelo = (234,226,72)
vermelho = (255,0,21)
cinza = (178, 171, 171)

#fonte
font = pygame.font.SysFont(None, 20)

def obstaculo():
    foto_obstaculo = pygame.image.load("car2.jpg")
    #if obs==0:
     #   foto_obsta=pygame.image.load("car2.jpg")
    #elif obs==1:
     #   foto_obsta=pygame.image.load("car4.jpg")
    #elif obs==2:
        #foto_obsta=pygame.image.load("car5.jpg")
    #elif obs==3:
        #foto_obsta=pygame.image.load("car6.jpg")
    #elif obs==4:
     #   foto_obsta=pygame.image.load("car7.jpg")


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




def carro(x,y):
    tela.blit(carro_imagem,(x,y))



def game():
    x=(largura*0.45)
    y=(altura*0.8)
    pos_x=0
    pos_y=0
    vel_obstaculo = 9
    obs=0
    obs_startx=random.randrange(200,largura-200)   
    obs_starty=-750
    obs_largura=56
    obs_altura=125

    sair = True
    menu = False
    bateu = False
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
                if event.key == pygame.K_RIGHT:
                    pos_x=5
            
            if event.type == pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    pos_x=0
        

        
        x+=pos_x

        tela.fill(cinza)
        Fundo()
        carro(x,y)
        if x>680-carro_largura or x<110:
            bateu = True

        pygame.display.update()
        relogio.tick(60)

game()
pygame.quit()