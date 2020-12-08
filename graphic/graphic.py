import pygame
import graphic.constant




class Game:
    def __init__(self):
        self.screen_size = (675, 705)
        self.title = graphic.constant.game_title
        self.picture_title = graphic.constant.picture_title
        pygame.init()
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption(self.title)
        picture_menu = pygame.image.load(self.picture_title).convert_alpha()
        pygame.display.set_icon(picture_menu)
        self.play = True
        self.end = False

    def inventory(self, mac):
        font = pygame.font.Font(None, 24)
        text = font.render(
            "   inventaire:      Ether :  {}      Tube :  {}      Aiguille :  {}".format(
                mac.item["ether"], mac.item["tube"], mac.item["aiguille"]
            ),
            1,
            (graphic.constant.white),
        )
        self.screen.blit(text, (0, 680))

    def item_pos(self, mac, item):
        if mac.item["ether"] == False:
            self.screen.blit(graphic.constant.picture_ether, item["ether"])
        if mac.item["aiguille"] == False:
            self.screen.blit(graphic.constant.picture_aiguille, item["aiguille"])
        if mac.item["tube"] == False:
            self.screen.blit(graphic.constant.picture_tube, item["tube"])

    def graph_move(self, mac):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    self.play = False
            if event.type == pygame.KEYDOWN:
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

#    def victory_display(self,mac):
#        if mac.free == True
#            for element in liste:
#                    self.screen.blit(graphic.constant.picture_floor, element)



    def run(self, logic, mac, bad, item):

        for key, value in mac.item.items():
            pass

        bad_state = True


        while self.play:
            self.screen.fill(
                graphic.constant.black
            )  # definit une couleur de fond pour l'screen_size
            self.inventory(mac)
            # screen_game_rect.fill(white)
            for element in logic.list_wall:
                self.screen.blit(graphic.constant.picture_wall, element)
            for element in logic.list_floor:
                self.screen.blit(
                    graphic.constant.picture_floor, element
                )  # blit copie l'image_surface en parametre sur la surface de l'screen_size
            for element in logic.list_start:
                self.screen.blit(graphic.constant.picture_floor, element)
            for element in logic.list_finish:
                self.screen.blit(graphic.constant.picture_floor, element)
                self.screen.blit(graphic.constant.picture_finish, element)
            self.graph_move(mac)

            if (mac.position[0] in bad.field_of_view) and mac.safe == True:
                bad_state = False
            if bad_state == False:
                for element in bad.position:
                    self.screen.blit(graphic.constant.picture_rip, element)
            else:
                for element in bad.position:
                    self.screen.blit(graphic.constant.picture_badguy, element)
            self.item_pos(mac, item)
            mac_lose = False
            if (mac.position[0] in bad.field_of_view) and mac.safe == False:
                for element in mac.position:
                    mac_lose = True
                    self.screen.blit(graphic.constant.picture_rip, element)
                    font_victory = pygame.font.Font(None, 36)
                    test = pygame.Surface((300,200))
                    testB = test.get_rect()
                    testB.center = (337,337)
                    vicory_text_surface = font_victory.render("You lose !!!", 1, graphic.constant.white)
                    victory_text_rect = vicory_text_surface.get_rect()
                    victory_text_rect.center = (337, 337)
                    self.screen.blit(test, testB)
                    self.screen.blit(vicory_text_surface, victory_text_rect)
                    pygame.display.flip()
                    while mac_lose:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
            else:
                for element in mac.position:
                    self.screen.blit(graphic.constant.picture_macgy, element)
                    if mac.free == True:
                        font_victory = pygame.font.Font(None, 36)
                        test = pygame.Surface((300,200))
                        testB = test.get_rect()
                        testB.center = (337,337)
                        vicory_text_surface = font_victory.render("You are free !!!", 1, graphic.constant.white)
                        victory_text_rect = vicory_text_surface.get_rect()
                        victory_text_rect.center = (337, 337)
                        self.screen.blit(test, testB)
                        self.screen.blit(vicory_text_surface, victory_text_rect)
                        pygame.display.flip()
                        while mac.free:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()


            pygame.display.flip()  # dit à pygame d'afficher la surface du jeu
        pygame.quit()
