# -*- coding: cp1252 -*-
# Para projectos de MDP 2011-12
# ISEL-PT

# 1. Cria uma tabela de 5x5 com círculos coloridos
# Permite seleccionar círculos usando o rato.
# 2. Determina colunas com pelo menos 3 elementos da mesma cor


# Importa dois módulos
# O módulo random é usado para escolher as cores para os círculos 
import pygame
import random

# Define as cores a usar
black = [0, 0, 0]
white = [255, 255, 255]
red = [105, 0, 0]

# Define característica da tabela
numLinhas = 5    # A tabela tem 5 linhas
numColunas = 5   # A tabela tem 5 colunas
ojectivo = 3  # Objectivo é fazer 3 elementos repetidos nas colunas

# A função que determina as colunas a alterar

def tensDeRemover(Tab, nlinhas, ncolunas, objectivo):
    """ tensDeRemover(list,int,int,int)->set, que para a tabela Tab,
        com n linhas e m colunas, tensDeRemover(Tab,n,m,k) devolve o conjunto
        DelColunas as colunas que tenhem pelo menos k objectos iguais"""
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


cor = []    # É desta lista que se escolhe as cores para os circulos
cor.append([0, 205, 0])
cor.append([205, 105, 0])
cor.append([50, 105, 50])
cor.append([50, 105, 205])

# inicia o motor de jogo
pygame.init()

# define o ecrã  
screen = pygame.display.set_mode([500, 500])

# escreve titulo da janela 
pygame.display.set_caption("Tabela - 2012/13")

# Cria a distribuição inicial das cores pelos círculos.
# Na matriz Tab cada posição (i,j) contem uma lista [x,y,cor] com as coordenadas
# do vértice superior esquerdo do quadrado que contem o círculo de cor indicada
Tab = []
for j in range(numColunas):
    linha = []
    for i in range(numLinhas):
        linha.append([100 * i, 100 * j, random.randrange(len(cor))])
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

    # Limpa frame
    screen.fill(black)

    # Função que determina linhas ou colunas a remover
    ColunasRem = tensDeRemover(Tab, numLinhas, numColunas, ojectivo)

    print("Colunas a alterar:", ColunasRem)

    #
    # Aqui deves remover as linhas e colunas e actualizar tabela de circulos
    #

    pos = pygame.mouse.get_pos()    #coordenadas do rato

    #posição do rato
    xR = pos[0]
    yR = pos[1]

    #Desenha estado actual do tabuleiro    
    for i in range(numLinhas):
        for j in range(numColunas):
            x = Tab[i][j][0]      # vértice sup. esquerdo x
            y = Tab[i][j][1]      # vértice sup. esquerdo y
            c = cor[Tab[i][j][2]]   # cor
            pygame.draw.circle(screen, c, [x + 50, y + 50], 45, 0)   # desenho as minhas peças
            # Determina linha e coluna da casa onde o cursor está posicionado
            if xR > x and xR < x + 100 and yR > y and yR < y + 100:
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
