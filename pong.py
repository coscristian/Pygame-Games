import pygame
pygame.init()

#Colores
negro = (0, 0, 0)
blanco = (255, 255, 255)
ancho_pantalla = 800
alto_pantalla = 600
tamanio_pantalla = (ancho_pantalla, alto_pantalla)
ancho_jugador = 15
altura_jugador = 90

pantalla = pygame.display.set_mode(tamanio_pantalla)
clock = pygame.time.Clock()

#Coordenadas y velocidad del jugador 1
jugador1_x_coord = 50
jugador1_y_cord = 300 - 45
jugador1_y_velocidad = 0

#Coordenadas y velocidad jugador 2
jugador2_x_coord = 750 - ancho_jugador
jugador2_y_cord = 300 - 45
jugador2_y_velocidad = 0

#Coordenadas de la pelota
pelota_x = 400
pelota_y = 300
pelota_veloc_x = 3
pelota_veloc_y = 3

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                jugador1_y_velocidad = -5
            if event.key == pygame.K_s:
                jugador1_y_velocidad = 5
            if event.key == pygame.K_UP:
                jugador2_y_velocidad = -5
            if event.key == pygame.K_DOWN:
                jugador2_y_velocidad = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                jugador1_y_velocidad = 0
            if event.key == pygame.K_s:
                jugador1_y_velocidad = 0
            if event.key == pygame.K_UP:
                jugador2_y_velocidad = 0
            if event.key == pygame.K_DOWN:
                jugador2_y_velocidad = 0
    #Logica del juego
    #Modificando la posicion de jugadores
    jugador1_y_cord += jugador1_y_velocidad
    jugador2_y_cord += jugador2_y_velocidad
    #Limite superior
    if jugador1_y_cord < -altura_jugador:  
        jugador1_y_cord = alto_pantalla 
    if jugador2_y_cord < -altura_jugador:
        jugador2_y_cord = alto_pantalla 
    #Limite inferior
    if jugador1_y_cord > alto_pantalla:
        jugador1_y_cord = -altura_jugador
    if jugador2_y_cord > alto_pantalla:
        jugador2_y_cord = -altura_jugador
    #Movimiento pelota
    #Limites verticales pelota
    if pelota_y > 595 or pelota_y < 10:
        pelota_veloc_y *= -1
    #Limites horizontales pelota
    if pelota_x > 800 or pelota_x < 0:
        pelota_x = ancho_pantalla // 2
        pelota_y = alto_pantalla // 2
        pelota_veloc_x *=-1
        pelota_veloc_y *=-1
    #Modificando la posicion de la pelota (Movimiento)
    pelota_x += pelota_veloc_x
    pelota_y += pelota_veloc_y
    #Color de fondo
    pantalla.fill(negro)
    #Zona de dibujo
    jugador1 = pygame.draw.rect(pantalla, blanco, (jugador1_x_coord, jugador1_y_cord, ancho_jugador, altura_jugador))
    jugador2 = pygame.draw.rect(pantalla, blanco, (jugador2_x_coord, jugador2_y_cord, ancho_jugador, altura_jugador))
    pelota = pygame.draw.circle(pantalla, blanco, (pelota_x, pelota_y), 5)
    #Colisiones
    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
        pelota_veloc_x *= -1
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
