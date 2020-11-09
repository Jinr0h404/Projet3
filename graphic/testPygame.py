import pygame

pygame.init()

ecran = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Help MacGyver")
picture_menu = pygame.image.load("../data/projet_3.png").convert()
pygame.display.set_icon(picture_menu)


picture_macgy = pygame.image.load("../data/MacGyver.png").convert()
picture_floor = pygame.image.load("../data/floor15.png").convert()
picture_wall = pygame.image.load("../data/wall15.png").convert()

list_wall = [(10, 10),(30, 30), (50,50)]

continuer = True

while continuer:
    ecran.blit(picture_floor, list_wall[2])
    ecran.blit(picture_macgy, (0, 0)) # le tuple 0,0 donne la position de départ de l'image
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            continuer = False
    pygame.display.flip()

pygame.quit()