import pygame
from pygame.locals import *
from pygame.sprite import Sprite, RenderUpdates
import random

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

numLinhas = 5   # A tabela tem 5 linhas
numColunas = 5  # A tabela tem 5 colunas
objectivo = 3   # Objectivo do jogo

def tensDeRemover(Tab, nlinhas, ncolunas, objectivo):

    RemoveColuna = set()

    for i in range(nlinhas):
        for j in range(ncolunas):
            cont = 1
            k = i + 1
            while k < nlinhas and Tab[k][j][2] == Tab[i][j][2]:
                cont += 1
                k += 1
            k = i - 1
            while k >= 0 and Tab[k][j][2] == Tab[i][j][2]:
                cont += 1
                k -= 1
            if cont >= objectivo:
                RemoveColuna.add(j)
    return RemoveColuna

cor = [pygame.image.load("im0.gif"), pygame.image.load("im1.gif"), pygame.image.load("im2.gif"),
       pygame.image.load("im3.gif")]    # É desta lista que se escolhe as cores para os circulos

# # Tab = [[[74 * i, 74 * j] for j in range(numColunas)] for i in range(numLinhas)]

# incia motor de jogo
pygame.init()

# define ecra
screen = pygame.display.set_mode([500,500])

# escrever titulo da janela
pygame.display.set_caption("Grid or Not")

Tab=[]
for j in range(numColunas):
    linha = []
    for i in range(numLinhas):
        linha.append([74*i, 74*j, random.randrange(len(cor))])
    Tab.append(linha)

# inicia a linha e coluna do circulo onde está o cursor do rato
xPre = 0
yPre = 0

# Inicia Loop do jogo
done = False

clock = pygame.time.Clock()

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Limpa ecra
    screen.fill(black)

    # Função que determina linhas ou colunas a remover
    ColunasRem = tensDeRemover(Tab, numLinhas, numColunas, objectivo)

    print("Colunas a alterar:", ColunasRem)

    #
    # Aqui deves remover as linhas e colunas e actualizar tabela de circulos
    #

    pos = pygame.mouse.get_pos()    # coordenadas do rato

    # posiçao do rato
    xR = pos[0]
    yR = pos[1]

    # Desenha o estado actual do tabuleiro
    for i in range(numLinhas):
        for j in range(numColunas):
            x = Tab[i][j][0]      # vértice sup. esquerdo x
            y = Tab[i][j][1]      # vértice sup. esquerdo y
            c = cor[Tab[i][j][2]]   # cor
            screen.blit(c, (x, y))   # desenho as minhas peças
            # Determina linha e coluna da casa onde o cursor está posicionado
            if xR > x and xR < x + 74 and yR > y and yR < y + 74:
                xPre = j
                yPre = i

    mousestat = pygame.mouse.get_pressed()  # teclas do rato

    # Caso seja seleccionado um circulo, desenha quadrado
    # vermelho que o envolva e troca a sua cor
    if mousestat[0]:
        ValX = Tab[yPre][xPre][0]   # Coordenada x
        ValY = Tab[yPre][xPre][1]   # Coordenada y
        Ncor = Tab[yPre][xPre][2] + 1   # Roda a cor do disco
        if Ncor > len(cor) - 1:
            Ncor = 0
        Tab[yPre][xPre][2] = Ncor     # Altera cor
        pygame.draw.rect(screen, red, [ValX, ValY, 100, 100], 4)

    pygame.display.flip()
    clock.tick(10)

pygame.quit()