import pygame
import logic.logic
import graphic.constant



#class Screen:
#    def __init__(self):
#        self.screen_size = (675, 705)
#        self.title = "Help MacGyver"
#        self.picture_title = "data/projet_3.png"

#    def set_screen(self):
#        screen_display = pygame.display.set_mode(self.screen_size)
#        title_display = pygame.display.set_caption(self.title)
#        picture_menu = pygame.image.load(self.picture_title).convert_alpha()
#        display_picture_menu = pygame.display.set_icon(picture_menu)

class Game:
    def __init__(self):
        self.screen_size = (675, 705)
        self.title = "Help MacGyver"
        self.picture_title = "data/projet_3.png"
        pygame.init()
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption(self.title)
        picture_menu = pygame.image.load(self.picture_title).convert_alpha()
        pygame.display.set_icon(picture_menu)

    def run(self, logic, mac, bad, item): #screen):

        for key, value in mac.item.items():
            pass


        continuer = True
        bad_state = True

        while continuer: 
            self.screen.fill(graphic.constant.black) # definit une couleur de fond pour l'screen_size

            #affichage inventaire#
            font = pygame.font.Font(None, 24)
            text = font.render("inventaire:  Ether: {}   Tube: {}   Aiguille: {}".format(mac.item['ether'], mac.item['tube'],mac.item['aiguille']), 1, (graphic.constant.white))

            #screen_game_rect.fill(white)
            for element in logic.list_wall:
                self.screen.blit(graphic.constant.picture_wall, element)
            for element in logic.list_floor:
                self.screen.blit(graphic.constant.picture_floor, element) # blit copie l'image_surface en parametre sur la surface de l'screen_size
            for element in logic.list_start:
                self.screen.blit(graphic.constant.picture_floor, element)
            for element in logic.list_finish:
                self.screen.blit(graphic.constant.picture_floor, element)
                self.screen.blit(graphic.constant.picture_finish, element)
            
            if mac.position == bad.position and mac.safe == True:
                bad_state = False
            #if (mac.move_down() == bad.position or mac.move_up() == bad.position or mac.move_right() == bad.position or mac.move_left() == bad.position) and mac.safe == True:
                #bad_state = False
            if bad_state == False:
                for element in bad.position:
                    self.screen.blit(graphic.constant.picture_rip, element)
            else:
                for element in bad.position:
                    self.screen.blit(graphic.constant.picture_badguy, element)
            if mac.item['ether'] == False:
                self.screen.blit(graphic.constant.picture_ether, item["ether"])
            if mac.item['aiguille'] == False:
                self.screen.blit(graphic.constant.picture_aiguille, item["aiguille"])
            if mac.item['tube'] == False:
                self.screen.blit(graphic.constant.picture_tube, item["tube"])
            self.screen.blit(text, (0,680))
            for element in mac.position:
                self.screen.blit(graphic.constant.picture_macgy, element)
            #screen_size.blit(screen_game_rect, screen_game)
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


    
