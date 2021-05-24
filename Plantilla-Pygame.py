import pygame

pygame.init() #Inicializar Pygame
screen = pygame.display.set_mode((600, 800)) #Definir la ventana (x,y)
clock = pygame.time.Clock() #Definir clock interno

#Variables
FPS = 30 #Frames Por Segundo
running = 1 

while running == 1: #Bucle de Juego
    #Imprimir en pantalla
    screen.fill((255,255,255)) #Lenar la pantalla con un color

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0

    clock.tick(FPS) #Actualizar actos en funcion de los FPS
    pygame.display.update() #Actualizar Pantalla

pygame.quit()
quit()
