import pygame
import time

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
grey = (127,127,127)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('SCAPE INSPER')

imag_sala1 = pygame.image.load('insper_test2.jpg')
imag2 = pygame.image.load('tijolo.jpeg')
imag3 = pygame.image.load('out.jpg')
imag4 = pygame.image.load('ipad.jpg')


clock = pygame.time.Clock()

Inventário = []
    

estado = 0
while estado >= 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            estado = -1
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (X,Y) = pygame.mouse.get_pos()
            print(X,Y)

            
            gameDisplay.fill(white)
            gameDisplay.blit(imag_sala1,(0,0))
            gameDisplay.blit(imag4,(516,424))
            
    

            if estado == 0:
                if 339 <= X <= 435 and 442<= Y <= 503:
                    estado = 1

            elif estado == 1:
                gameDisplay.fill(black)
                gameDisplay.blit(imag2,(400,300))
                gameDisplay.blit(imag3,(562,525))
                if 400 <= X <= 460 and 300 <= Y <= 438:
                    print(2)
                    if imag2 not in Inventário:
                        Inventário.append(imag2)
                        print(Inventário)
                elif 562 <= X <= 800 and 525 <= Y <= 600:
                    estado = 0
           
    clock.tick(10)
    pygame.display.update()






###########################################################################################

''''
class Inventário:
    
    def __init__(self,objeto):
        self.objeto = pygame.image.load(objeto)

    def adiciona_inventario(self,objeto):
        if e in Insper_toy:
            e["imagem"] = self.objeto
            
    def mostra_objeto(self):
        if self.objeto in inventário:
            print("
            '''''
        
        
        
        


































