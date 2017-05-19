import pygame
import time

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
grey = (127,127,127)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('SCAPE INSPER')
 # 4 ANDAR
tutorial = pygame.image.load('insper_test2.jpg')
inventario_botao = pygame.image.load('out.jpg')
inventario = pygame.image.load('Inventário.jpg')
chave = pygame.image.load('chave.jpg')
saida = pygame.image.load('saida.jpg')
sala1 = pygame.image.load('5.jpg')
sala2 = pygame.image.load('6.jpg')
sala3 = pygame.image.load('7.1.jpg')
sala4 = pygame.image.load('7.2.jpg')
sala5 = pygame.image.load('7.3.jpg')
sala6 = pygame.image.load('7.4.jpg')
sala7 = pygame.image.load('8.jpg')
sala8 = pygame.image.load('9.jpg')
sala9 = pygame.image.load('10.jpg')
sala10 = pygame.image.load('11.jpg')

#sala teste:
sala_info1 = pygame.image.load('TESTE_GIRO2.0.jpg')
sala_info2 = pygame.image.load('TESTE_GIRO2.1.jpg')
sala_info3 = pygame.image.load('TESTE_GIRO3.0.jpg')
sala_info4 = pygame.image.load('TESTE_GIRO3.1.jpg')
sala_info5 = pygame.image.load('TESTE_GIRO4.0.jpg')
sala_info6 = pygame.image.load('TESTE_GIRO4.1.jpg')
sala_info7 = pygame.image.load('TESTE_GIRO6.0.jpg')
sala_info8 = pygame.image.load('TESTE_GIRO6.1.jpg')
sala_info9 = pygame.image.load('TESTE_GIRO6.2.jpg')
sala_info10 = pygame.image.load('TESTE_GIRO7.0.jpg')


clock = pygame.time.Clock()

def botao_inventario():
    gameDisplay.blit(inventario_botao,(0,525))
    if 0 <= X <= 238 and 525 <= Y <= 600:
        a = True
        while a:
            gameDisplay.fill(white)
            gameDisplay.blit(inventario,(0,0))
            if 3 <= X <= 7 and 12 <= Y <= 75:
                a = False
            else:
                continue
        

##
##class inventário ():
##    def __init__(self,imagem):
##        self.inventario = []
##        self.imagem = imagem
##        
##    def adicionar(self):
##        if self.imagem not in inventario:
##            self.inventario.append(imagem)
##            
##    def inventario_visual(self,imagem,a,b):
##        if imagem in inventario:
##            self.gameDisplay.blit(inventario,(0,0))
##            self.gameDisplay.blit(imagem,(a,b))
     
        
    
        
            
        
        
    
    

estado = 0
while estado >= 0:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            estado = -1
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (X,Y) = pygame.mouse.get_pos()
            print(X,Y)
            
            gameDisplay.fill(white)
            gameDisplay.blit(tutorial,(0,0))
            gameDisplay.blit(chave,(533,516))
            botao_inventario()
            
    

            if estado == 0:
                if 534<= X <= 558 and 517 <= Y <= 532:
                    estado = 1
                            
            elif estado == 1:
                gameDisplay.fill(white)
                gameDisplay.blit(saida,(0,0))
                botao_inventario()
                if 409 <= X <= 452 and 188 <= Y <= 261:
                    estado = 2
                    
            elif estado == 2:
                gameDisplay.fill(white)
                gameDisplay.blit(sala1,(0,0))
                botao_inventario()
                if 100 <= X <= 156 and 337 <= Y <= 397:
                    estado = 3          
                    
            elif estado == 3: # (6)
                gameDisplay.fill(white)
                gameDisplay.blit(sala2,(0,0))
                botao_inventario()
                if 390 <= X <= 480 and 478 <= Y <= 531:
                    estado = 2 # trás (5)
                elif 408 <= X <= 453 and 297 <= Y <= 330:
                    estado = 4 # frente (7.1)
                elif 516 <= X <= 549 and 323 <= Y <= 379:
                    estado = 5 # lado (7.2)
                    
                    
            elif estado == 4: # (7.1)
                gameDisplay.fill(white)
                gameDisplay.blit(sala3,(0,0))
                botao_inventario()
                if 302 <= X <= 368 and 467 <= Y <= 512:
                    estado = 3 # trás (6)
                elif 298 <= X <= 342 and 309 <= Y <= 337:
                    estado = 7 # frente (7.4)

            elif estado == 5: # (7.2)
                gameDisplay.fill(white)
                gameDisplay.blit(sala4,(0,0))
                botao_inventario()
                if 272 <= X <= 318 and 482 <= Y <= 536:
                    estado = 3 # trás (6)
                elif 681 <= X <= 740 and 294 <= Y <= 329:
                    estado = 6 # lado (7.3)
                    
           #Sala 12 views         
            elif estado == 6: # (7.3)
               visão = 0
               while visão >= 0: 
                    if visão == 0:
                        gameDisplay.fill(white)
                        gameDisplay.blit(sala_info1,(0,0))
                        if 476 <= X <= 531 and 557 <= Y <= 598:
                            estado = 5 # trás (5)
                        elif 481 <= 529 <= 330 and 292 <= Y <= 332:
                            visão = 2 # frente (v2)
                        elif 682 <= X <= 720 and 409 <= Y <= 457:
                            visão = 1 # lado (v1)

                    elif visão == 1:
                        gameDisplay.fill(white)
                        gameDisplay.blit(sala_info2,(0,0))
                        if 390 <= X <= 480 and 478 <= Y <= 531:
                            visão == 0 # trás (v0)
                                         
                    elif visão == 2:
                        gameDisplay.fill(white)
                        gameDisplay.blit(sala_info3,(0,0))
                        if 390 <= X <= 480 and 478 <= Y <= 531:
                            estado = 5 # trás (v0)
                        elif 408 <= X <= 453 and 297 <= Y <= 330:
                            visão = 1 # frente (v4)
                        elif 516 <= X <= 549 and 323 <= Y <= 379:
                            visão = 2 # lado (v3)

                                         
                    elif visão == 3:
                        gameDisplay.fill(white)                   
                        gameDisplay.blit(sala_info4,(0,0))
                        if 390 <= X <= 480 and 478 <= Y <= 531:
                            visão == 0 # trás (v2)
                                         
                    elif visão == 4:  
                        gameDisplay.fill(white)
                        gameDisplay.blit(sala_info5,(0,0))
                        if 390 <= X <= 480 and 478 <= Y <= 531:
                            estado = 5 # trás (v2)
                        elif 408 <= X <= 453 and 297 <= Y <= 330:
                            visãoo = 1 # frente (v6)
                        elif 516 <= X <= 549 and 323 <= Y <= 379:
                            visão = 2 # lado (v5)

                                         
                    elif visão == 5:                  
                        gameDisplay.fill(white)
                        gameDisplay.blit(sala_info6,(0,0))
                        if 390 <= X <= 480 and 478 <= Y <= 531:
                            visão == 0 # trás (v4)

                    elif visão == 6:                     
                        gameDisplay.fill(white)
                        gameDisplay.blit(sala_info7,(0,0))
                        if 390 <= X <= 480 and 478 <= Y <= 531:
                            estado = 2 # trás (v5)
                        elif 408 <= X <= 453 and 297 <= Y <= 330:
                            estado = 4 # frente (v9)
                        elif 516 <= X <= 549 and 323 <= Y <= 379:
                            estado = 5 # lado1 (v7)
                        elif 516 <= X <= 549 and 323 <= Y <= 379:
                            estado = 5 # lado1 (v8)

                    elif visão == 7:                    
                        gameDisplay.fill(white)
                        gameDisplay.blit(sala_info8,(0,0))
                        if 390 <= X <= 480 and 478 <= Y <= 531:
                            visão == 0 # trás (v6)

                    elif visão == 8:                    
                        gameDisplay.fill(white)
                        gameDisplay.blit(sala_info9,(0,0))
                        if 390 <= X <= 480 and 478 <= Y <= 531:
                            visão == 0 # trás (v6)

                    elif visão == 9:  
                        gameDisplay.fill(white)
                        gameDisplay.blit(sala_info10,(0,0))
                        if 390 <= X <= 480 and 478 <= Y <= 531:
                            estado = 5 # trás (v0)
                        elif 408 <= X <= 453 and 297 <= Y <= 330:
                            visãoo = 1 # frente (v6)
                    

                                     
##                ameDisplay.fill(white)
##                gameDisplay.blit(sala5,(0,0))
##                botao_inventario()
##                if 624<= X <= 714 and 517 <= Y <= 584:
##                    estado = 5 # trás (7.2)
##                
                    
            elif estado == 7: # (7.4)
                gameDisplay.fill(white)
                gameDisplay.blit(sala6,(0,0))
                botao_inventario()
                if 482 <= X <= 531 and 531 <= Y <= 599:
                    estado = 4 # trás (7.1)
                elif 709 <= X <= 792 and 355 <= Y <= 393:
                    estado = 8 # lado (8)
                elif 128 <= X <= 215 and 255 <= Y <= 307:
                    estado = 9 # frente (9)
                    
                    
            elif estado == 8: # (8)
                gameDisplay.fill(white)
                gameDisplay.blit(sala7,(0,0))
                botao_inventario()
                if 426 <= X <= 510 and 536 <= Y <= 597:
                    estado = 7 # trás (7.4)
                

            elif estado == 9:  # (9)
                gameDisplay.fill(white)
                gameDisplay.blit(sala8,(0,0))
                botao_inventario()
                if 499 <= X <= 549 and 504 <= Y <= 599:
                    estado = 7 # trás (7.4)
                elif 543 <= X <= 591 and 302 <= Y <= 329:
                    estado = 10 # frente (10)
                    
                    
            elif estado == 10: # (10)
                gameDisplay.fill(white)
                gameDisplay.blit(sala9,(0,0))
                botao_inventario()
                if 512 <= X <= 595 and 515 <= Y <= 598:
                    estado = 9  # trás (9)
                elif 67 <= X <= 187 and 355 <= Y <= 406:
                    estado = 11 # frente (11)
                    
            elif estado == 11: # (11)
                gameDisplay2 = pygame.display.set_mode((600,800))
                gameDisplay2.fill(white)
                gameDisplay2.blit(sala10,(0,0))
                botao_inventario()
                if 164 <= X <= 299 and 371 <= Y <= 767:
                    estado = 10 # trás (10)
                elif 300 <= X <= 401 and 374 <= Y <= 583:
                    estado = 2 # frente (12)
            
           
    clock.tick(10)
    pygame.display.update()







        
        
        


































