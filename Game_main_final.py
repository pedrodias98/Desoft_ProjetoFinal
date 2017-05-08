import pygame
import time

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('SCAPE INSPER')

imag = pygame.image.load('armario.png')
imag2 = pygame.image.load('tijolo.jpeg')

clock = pygame.time.Clock()

Inventário = []
    

estado = 0
while estado >= 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            estado = -1
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (X,Y) = pygame.mouse.get_pos()
            
    gameDisplay.fill(white)

    if estado == 0:
        gameDisplay.blit(imag,(400,300))
        if 434 < X < 452 and 347 < Y < 354:
            tela = 1

    elif estado == 1
        gameDisplay.blit(imag2,(400,300))        
        if 400< X < 460 and 300 < Y < 438:
            print(2)
            if imag2 not in Inventário:
                Inventário.append(imag2)
                print(Inventário)
        elif 200 < X < 300 and 300 < Y < 400:
            estado = 0
           
    clock.tick(10)
    pygame.display.update()
