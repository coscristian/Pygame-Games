import pygame, sys, random
pygame.init()

#Colores
blanco = (255, 255, 255)
rojo = (255, 0, 0)
negro = (0, 0, 0)

#Crear pantalla
size = (800, 500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

#Quitar visibilidad del mouse
pygame.mouse.set_visible(0)

#Coordeanas cuadrado
coord_cuad_x = 10
coord_cuad_y = 10

#Velocidad
velocidad_x = 0
velocidad_y = 0

#Matriz para coordenadas
matriz_coord = []

for i in range(60):
    x = random.randint(0, 800)
    y = random.randint(0, 500)
    matriz_coord.append([x,y])
while True:
    #Obtener eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #Eventos de teclado
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                velocidad_x = -3
            if event.key == pygame.K_RIGHT:
                velocidad_x = 3
            if event.key == pygame.K_DOWN:
                velocidad_y = 3
            if event.key == pygame.K_UP:
                velocidad_y = -3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                velocidad_x = 0
            if event.key == pygame.K_RIGHT:
                velocidad_x = 0
            if event.key == pygame.K_DOWN:
                velocidad_y = 0
            if event.key == pygame.K_UP:
                velocidad_y = 0
        
    #Movimiento de las coordenadas del cuadrado
    coord_cuad_x += velocidad_x
    coord_cuad_y += velocidad_y

    #Pintar la ventana
    screen.fill(negro)
    #Circulos en la pantalla 
    for coord in matriz_coord:
        x = coord[0]
        y = coord[1]
        pygame.draw.circle(screen, blanco, (x, y), 2)
        #Aumenta la posicion en y
        coord[1]+=1
        if coord[1] > 500:
            coord[1] = 0

    #Obtener posicion del mouse
    #mouse_pos = pygame.mouse.get_pos()
    #pos_x, pos_y = mouse_pos
    #DIbujar cuadrado
    pygame.draw.rect(screen, rojo, (coord_cuad_x, coord_cuad_y, 30, 30))    
    pygame.display.flip()
    clock.tick(60)
