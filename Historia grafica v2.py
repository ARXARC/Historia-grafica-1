import pygame, sys
pygame.init()
screen = pygame.display.set_mode((1082, 980))
opcion= 0
current_image = pygame.image.load("1.png")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                opcion += 1
                current_image = pygame.image.load("2.png") 
            elif event.key == pygame.K_2:
                opcion += 2
                current_image = pygame.image.load("2.png") 
            elif event.key == pygame.K_3:
                opcion += 1
                current_image = pygame.image.load("3.png")
            elif event.key == pygame.K_4:
                opcion += 2
                current_image = pygame.image.load("3.png")
            elif event.key == pygame.K_5:
                opcion += 1
                current_image = pygame.image.load("4.png")
            elif event.key == pygame.K_6:
                opcion += 2
                current_image = pygame.image.load("4.png")  
            elif event.key == pygame.K_7:
                opcion += 1
                current_image = pygame.image.load("5.png")
            elif event.key == pygame.K_8:
                opcion += 2
                if opcion <= 5:
                    current_image = pygame.image.load("end1.png")
                elif opcion >= 6 and opcion <= 9:
                    current_image = pygame.image.load("end2.png")
                elif opcion >= 10:
                    current_image = pygame.image.load("end3.png")
    screen.fill((0, 0, 0))
    screen.blit(current_image, (0, 0))  
    pygame.display.flip()
