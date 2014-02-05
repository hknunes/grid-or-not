# Projecto MDP 2012-2013
# 
# 1. Carrega imagem de fundo
# 2. Carrega imagem do jogador e define cor transparente
# 3. Carrega som ambiente longo mp3
# 4. Carrega som curto wav
# 5. O som ambiente toca até a janela ser fechada
 
# Importa módulo pygame
import pygame
 
# Define cor a assumir como transparente na imagem do jogador
white=[255,255,255]
 
# Inicia o motor de jogo
pygame.init()

# Inicia o mixer (Isto é importante!!!)
pygame.mixer.init()
# isto permite parametrizar o som de acordo com a sua placa

# Carrega música ambiente (só pode ter uma a tocar)
pygame.mixer.music.load("Kalimba.mp3") # música ambiente

# Toca música ambiente indefinidamente
pygame.mixer.music.play(-1) 
# o parâmetro desta função define o número de vezes que a música vai tocar
# sempre que o parâmetro é -1 a música toda indefinidamente
# (i.e. até fechar a janela).
# Nota: no final deve fazer pygame.mixer.music.stop() para fazer reset à sua 
# placa de som.
 
# Carrega um som curto:
click_sound = pygame.mixer.Sound("click.wav")

# Cria janela gráfica 564x500 - isto tem de vir antes de carregar as imagens
screen = pygame.display.set_mode([564,400])

# Carrega imagens.
fundo = pygame.image.load("cena21.jpg").convert()
jogador = pygame.image.load("fno.png").convert()

# Define Cor da imagem do jogador que se assume como transparente
# para poder ver fundo.
jogador.set_colorkey(white)

 
# Define o nome da janela
pygame.display.set_caption('MDP- Som ambiente mp3 e som curto wav')
   
# define relógio
clock = pygame.time.Clock()
 
done = False
 
while done==False:
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
 					# termina jogo
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_sound.play()
			# Sempre que um botão do rato é
								# usado faz som

       
    # copia imagem para o fundo
    screen.blit(fundo, [0,0])
 
    # Determina posição do cursor do rato
    [xRato, yRato] = pygame.mouse.get_pos()
     
    # Copia imagem do jogador para ecrã na posições do cursor
    screen.blit(jogador, [xRato,yRato])

    # Actualiza imagem do frame 
    pygame.display.flip()

    # Número de frames por segundo
    clock.tick(10)


pygame.mixer.music.stop() # Atenção: para parar a música ambiente

pygame.quit ()
