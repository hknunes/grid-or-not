import pygame
from pygame.locals import *
from pygame.sprite import Sprite, RenderUpdates

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

numLinhas = 5   # A tabela tem 8 linhas
numColunas = 5  # A tabela tem 5 colunas
Tab = [[[74 * i, 74 * j] for j in range(numColunas)] for i in range(numLinhas)]

im0 = pygame.image.load('im0.gif')

# inicia a linha e coluna dum circulo que inicialmente está seleccionado
xSele = 0
ySele = 0

# inicia a linha e coluna do circulo onde está o cursor do rato
xPre = 0
yPre = 0

# existe um circulo seleccionado  
Selected = True

# Inicia Pygame
pygame.init()

# Define o ecrã
size = [370, 370]
screen = pygame.display.set_mode(size)

# escreve titulo da janela 
pygame.display.set_caption("Grid - 0.0")

#coordenadas do rato
pos = pygame.mouse.get_pos()

# Create a red player block
seta = pygame.draw.rect(screen, red, ((pos[0], pos[1]), (5, 5)))


#Para entrar em loop, até que a janela seja fechada.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():    # User did something
        if event.type == pygame.QUIT:   # If user clicked close
            done = True     # Flag that we are done so we exit this loop

    # Clear the screen
    screen.fill(black)
    #coordenadas do rato
    pos = pygame.mouse.get_pos()

    #posição do rato
    xR = pos[0]
    yR = pos[1]

    # Set the player object to the mouse location
    seta.x = pos[0]
    seta.y = pos[1]

    # --- Desenha grelha --- #
    for i in range(numLinhas):
        for j in range(numColunas):
            x = Tab[i][j][0]
            y = Tab[i][j][1]

            square = screen.blit(im0, (x,y))

            if xR > x and xR < x + 74 and yR > y and yR < y + 74:
                xPre = j
                yPre = i
                ##/-------------/##

    mousestat = pygame.mouse.get_pressed()  # teclas do rato
    # Selecciona o circulo onde o cursor está posicionado
    if mousestat[0]:
        xSele = xPre
        ySele = yPre

        ValX = Tab[ySele][xSele][0]
        ValY = Tab[ySele][xSele][1]


        # Caso esteja seleccionado um circulo, desenha quadrado
    # vermelho que o envolva          
    if Selected:
        ValX = Tab[ySele][xSele][0]
        ValY = Tab[ySele][xSele][1]

        pygame.draw.rect(screen, black, [ValX, ValY, 74, 74], 2)
        #squareR = pygame.draw.rect(screen, red, ((ValX+20,ValY+20),(60,60)))

    # Limit to 20 frames per second
    clock.tick(15)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.update()

pygame.quit()
