#Librerias
import pygame
import numpy as np
import time

#Iniciar la libreria pygame.
pygame.init()

#Ancho y alto de la pantalla. 
width, height = 1000, 1000
#Creacion de la pantalla.
screen = pygame.display.set_mode((height, width))

#Color de fondo = casi negro, casi oscuro. 
bg = 25, 25, 25
#Pintando el fondo con el color elegido.
screen.fill(bg)

#Cantidad de celdas en eje X, Y
nxC, nyC = 50, 50

#Ancho y alto de celdas dado por la division entre ancho y alto de la pantalla 
dimCW = width / nxC
#y el nro de celdas que tenemos.
dimCH = height / nyC

#Estado de las celdas. Vivas = 1; Muertas = 0
gameState = np.zeros((nxC, nyC))

##Automata palo.
#gameState[5, 3] = 1
#gameState[5, 4] = 1
#gameState[5, 5] = 1

#Automata movil
gameState[21, 21] = 1
gameState[22, 22] = 1
gameState[23, 23] = 1
gameState[21, 23] = 1
gameState[20, 23] = 1

#Bucle de ejecucion
while True:

    newGameState = np.copy(gameState)

    screen.fill(bg)
    time.sleep(0.1)

    # Bucle para recorrer cada una de las celdas generadas
    for y in range(0, nxC):
        for x in range(0, nyC):

        
            #Calculamos el numero de vecinos cercanos
            n_neigh = gameState[(x+1) % nxC, (x-1) % nyC] + \
                      gameState[(x) % nxC, (y-1) % nyC] + \
                      gameState[(x+1) % nxC, (y-1) % nyC] + \
                      gameState[(x-1) % nxC, (y) % nyC] + \
                      gameState[(x+1) % nxC, (y) % nyC] + \
                      gameState[(x-1) % nxC, (y+1) % nyC] + \
                      gameState[(x) % nxC, (y+1) % nyC] + \
                      gameState[(x+1) % nxC, (y+1) % nyC] 
                      
            #Rule #1: Una celula muerta con exactamente 3 vecinas vivas, "revive".
            if gameState[x, y] == 0 and n_neigh == 3:
                newGameState[x, y] = 1

            #Rule #2: Una celula viva con menos de 2 o mas de 3 vecinas vivas, "muere"
            elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                newGameState[x, y] = 0

            #Creamos el poligono de cada celda a dibujar
            poly = [((x)   * dimCW, y * dimCH),
                    ((x+1) * dimCW, y * dimCH),
                    ((x+1) * dimCW, (y+1) * dimCH),
                    ((x)   * dimCW, (y+1) * dimCH)]

            #Dibujamos las celdas para cada par de ejes x e y
            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0)

    #Actualizamos el estado del juego. 
    gameState = np.copy(newGameState)

    pygame.display.flip()
