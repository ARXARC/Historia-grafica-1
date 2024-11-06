import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((1082, 980))
opt1 = pygame.image.load("1.png")
opt2 = pygame.image.load("2.png")
opt3 = pygame.image.load("3.png")
opt4 = pygame.image.load("4.png")
opt5 = pygame.image.load("5.png")
end1 = pygame.image.load("end1.png")
end2 = pygame.image.load("end2.png")
end3 = pygame.image.load("end3.png")
opcion1 = 0
opcion2 = 0
rst= 0
current_image = opt1 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                opcion1 += 1
                current_image = opt2  
            elif event.key == pygame.K_2:
                opcion2 += 2
                current_image = opt2  
            elif event.key == pygame.K_3:
                opcion1 += 1
                current_image = opt3
            elif event.key == pygame.K_4:
                opcion2 += 2
                current_image = opt3  
            elif event.key == pygame.K_5:
                opcion1 += 1
                current_image = opt4 
            elif event.key == pygame.K_6:
                opcion2 += 2
                current_image = opt4   
            elif event.key == pygame.K_7:
                opcion1 += 1
                current_image = opt5
            elif event.key == pygame.K_8:
                opcion2 += 2
                current_image = opt5 
                rst= opcion1+opcion2
                if rst <= 5:
                    current_image = end1 
                elif rst >= 6 and rst <= 9:
                    current_image = end2 
                elif rst >= 10:
                    current_image = end3
    screen.fill((0, 0, 0))
    screen.blit(current_image, (0, 0))  
    pygame.display.flip()
