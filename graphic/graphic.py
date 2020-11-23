import pygame
import logic.logic


class Screen:
    def __init__(self):
        self.screen_size = (675, 675)
        self.title = "Help MacGyver"
        self.picture_title = "data/projet_3.png"

    def set_screen(self):
        screen_size = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption(self.title)
        picture_menu = pygame.image.load(self.picture_tile).convert_alpha()
        pygame.display.set_icon(self.picture_title)

def playgame(start_pos, finish_pos, wall_pos, floor_pos, mac_pos, bad_guy_pos, aiguille_pos, ether_pos, tube_pos):
    pygame.init()

    ecran = pygame.display.set_mode((675, 675))
    pygame.display.set_caption("Help MacGyver")
    picture_menu = pygame.image.load("data/projet_3.png").convert_alpha()
    pygame.display.set_icon(picture_menu)


    noir = (10, 10, 10)

    picture_macgy = pygame.image.load("data/MacGyver.png").convert_alpha() # cherche et tranforme l'image en surface puis la converti
    picture_badguy = pygame.image.load("data/gardien.png").convert_alpha()
    picture_floor = pygame.image.load("data/floor15.png").convert_alpha()
    picture_wall = pygame.image.load("data/wall15.png").convert_alpha()
    picture_finish = pygame.image.load("data/stair45.png").convert_alpha()
    picture_tube = pygame.image.load("data/tube45.png").convert_alpha()
    picture_aiguille = pygame.image.load("data/aiguille45.png").convert_alpha()
    picture_ether = pygame.image.load("data/ether45.png").convert_alpha()

    rect_macgy = picture_macgy.get_rect()
    rect_floor = picture_floor.get_rect()
    rect_wall = picture_wall.get_rect()


    continuer = True

    while continuer: 
        ecran.fill(noir) # definit une couleur de fond pour l'ecran
        for element in wall_pos:
            ecran.blit(picture_wall, element)
        for element in floor_pos:
            ecran.blit(picture_floor, element) # blit copie l'image_surface en parametre sur la surface de l'ecran
        for element in start_pos:
            ecran.blit(picture_floor, element)
        for element in finish_pos:
            ecran.blit(picture_floor, element)
            ecran.blit(picture_finish, element)
        for element in bad_guy_pos:
            ecran.blit(picture_badguy, element)
        ecran.blit(picture_ether, ether_pos)
        #ecran.blit(picture_ether, item_pos[0])
        ecran.blit(picture_aiguille, aiguille_pos)
        #ecran.blit(picture_aiguille, item_pos[1])
        ecran.blit(picture_tube, tube_pos)
        #ecran.blit(picture_tube, item_pos[2])
        #ecran.blit(picture_macgy, (0, 0)) # le tuple 0,0 donne la position de départ de l'image
        for element in mac_pos:
            ecran.blit(picture_macgy, element)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False
            if event.type  == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    for element in mac_pos:
                        mac_pos.move_down()
                        pass
                elif event.key == pygame.K_UP:
                    pass
        pygame.display.flip() # dit à pygame d'afficher la surface du jeu

    pygame.quit()
