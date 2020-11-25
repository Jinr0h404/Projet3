import pygame
import logic.logic

############
#CONSTANTES#
############

black = (10, 10, 10)




class Screen:
    def __init__(self):
        self.screen_size = (675, 675)
        self.title = "Help MacGyver"
        self.picture_title = "data/projet_3.png"

    def set_screen(self):
        screen_size = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption(self.title)
        picture_menu = pygame.image.load(self.picture_title).convert_alpha()
        pygame.display.set_icon(self.picture_title)

class Game:
    def __init__(self):
        pass

    def run(self, logic, mac, bad, item, screen):
        pygame.init()

        

        screen_size = pygame.display.set_mode(screen.screen_size)
        pygame.display.set_caption(screen.title)
        picture_menu = pygame.image.load(screen.picture_title).convert_alpha()
        pygame.display.set_icon(picture_menu)


        picture_macgy = pygame.image.load("data/MacGyver.png").convert_alpha() # cherche et tranforme l'image en surface puis la converti
        picture_badguy = pygame.image.load("data/gardien.png").convert_alpha()
        picture_floor = pygame.image.load("data/floor15.png").convert_alpha()
        picture_wall = pygame.image.load("data/wall15.png").convert_alpha()
        picture_finish = pygame.image.load("data/stair45.png").convert_alpha()
        picture_tube = pygame.image.load("data/tube45.png").convert_alpha()
        picture_aiguille = pygame.image.load("data/aiguille45.png").convert_alpha()
        picture_ether = pygame.image.load("data/ether45.png").convert_alpha()

        continuer = True

        while continuer: 
            screen_size.fill(black) # definit une couleur de fond pour l'screen_size
            for element in logic.list_wall:
                screen_size.blit(picture_wall, element)
            for element in logic.list_floor:
                screen_size.blit(picture_floor, element) # blit copie l'image_surface en parametre sur la surface de l'screen_size
            for element in logic.list_start:
                screen_size.blit(picture_floor, element)
            for element in logic.list_finish:
                screen_size.blit(picture_floor, element)
                screen_size.blit(picture_finish, element)
            for element in bad.position:
                screen_size.blit(picture_badguy, element)
            screen_size.blit(picture_ether, item["ether"])
            screen_size.blit(picture_aiguille, item["aiguille"])
            screen_size.blit(picture_tube, item["tube"])
            for element in mac.position:
                screen_size.blit(picture_macgy, element)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    continuer = False
                if event.type  == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        for element in mac.position:
                            mac.move_down()     
                    elif event.key == pygame.K_UP:
                        for element in mac.position:
                            mac.move_up()
                    elif event.key == pygame.K_RIGHT:
                        for element in mac.position:
                            mac.move_right()
                    elif event.key == pygame.K_LEFT:
                        for element in mac.position:
                            mac.move_left()

            pygame.display.flip() # dit à pygame d'afficher la surface du jeu
        pygame.quit()


    
