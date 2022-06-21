import pygame, sys
pygame.init()

#Definir colores
negro = (0,0,0)
blanco = (255, 255, 255)
verde = (0, 255, 0)
rojo = (255, 0, 0)
azul = (0, 0, 255)

#Tamaño
size = (800, 500)
#Crear ventana
screen = pygame.display.set_mode(size)
#Controlar FPS
clock = pygame.time.Clock()

#Coordenadas del cuadrado
cord_x = 100
cord_y = 100

#Velocidad a la que se movera el cuadrado
speed_x = 10
speed_y = 10

while True:
    #Identifica todos los eventos en la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Acabas de cerrar la ventana")
            sys.exit()
    #Logica
    if cord_x > 720 or cord_x < 0:
        speed_x*=-1
    if cord_y > 420 or cord_y < 0:
        speed_y*=-1

    cord_x+=speed_x
    cord_y+=speed_y

    #Poner color de fondo
    screen.fill(blanco)
    
    # Zona de dibujo
    pygame.draw.rect(screen, negro, (cord_x, cord_y, 80, 80))

    #Actualizar pantalla
    pygame.display.flip()
    clock.tick(60)
