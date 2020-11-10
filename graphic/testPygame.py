import pygame

pygame.init()

ecran = pygame.display.set_mode((675, 675))
pygame.display.set_caption("Help MacGyver")
picture_menu = pygame.image.load("../data/projet_3.png").convert_alpha()
pygame.display.set_icon(picture_menu)


noir = (10, 10, 10)

picture_macgy = pygame.image.load("../data/MacGyver.png").convert_alpha() # cherche et tranforme l'image en surface puis la converti
picture_floor = pygame.image.load("../data/floor15.png").convert_alpha()
picture_wall = pygame.image.load("../data/wall15.png").convert_alpha()

rect_macgy = picture_macgy.get_rect()
rect_floor = picture_floor.get_rect()
rect_wall = picture_wall.get_rect()



list_wall = [(10, 10),(30, 30), (50,50), (90,90), (120,120), (150, 150)]

continuer = True

while continuer: 
    ecran.fill(noir) # definit une couleur de fond pour l'ecran
    for element in list_wall:
        ecran.blit(picture_floor, (element))
    ecran.blit(picture_floor, list_wall[2]) # blit copie l'image_surface en parametre sur la surface de l'ecran
    ecran.blit(picture_macgy, (0, 0, 20, 20)) # le tuple 0,0 donne la position de départ de l'image
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
    pygame.display.flip() # dit à pygame d'afficher la surface du jeu

pygame.quit()