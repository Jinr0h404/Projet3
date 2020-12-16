import pygame
import graphic.constant


class Game:
    """this class manages the displayof the game. It takes as attribute
    basic info like title and size of the game screen"""
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
        """method to display inventory on a text surface"""
        font = pygame.font.Font(None, 24)
        text = font.render(
            "   inventaire:      Ether :  {}\
            Tube :  {}        Aiguille :  {}".format(
                # int() permet de transformer mon booleen en en valeur 0 ou 1
                int(mac.item["ether"]),
                int(mac.item["tube"]),
                int(mac.item["aiguille"])
            ),
            1,
            (graphic.constant.white),
        )
        self.screen.blit(text, (0, 680))

    def item_pos(self, mac, item):
        """method to display or not the surfaces representing the object.
        Know if I should display an object by looking at the values of my
        key in the Macgyver object dictionary"""
        if mac.item["ether"] is False:
            self.screen.blit(
                graphic.constant.picture_ether, item["ether"])
        if mac.item["aiguille"] is False:
            self.screen.blit(
                graphic.constant.picture_aiguille, item["aiguille"])
        if mac.item["tube"] is False:
            self.screen.blit(
                graphic.constant.picture_tube, item["tube"])

    def graph_move(self, mac):
        """ method to interact with the user's keybord actions for move"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.play = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    mac.move_down()
                elif event.key == pygame.K_UP:
                    mac.move_up()
                elif event.key == pygame.K_RIGHT:
                    mac.move_right()
                elif event.key == pygame.K_LEFT:
                    mac.move_left()

    def run(self, logic, mac, bad, item):
        """main method of the graphic part. It displays the game by taking
        the various graphic and logical elements as parameter"""
        bad_state = True

        while self.play:
            self.screen.fill(
                graphic.constant.black
            )  # define background color for screen surface
            self.inventory(mac)
            for element in logic.list_wall:
                self.screen.blit(graphic.constant.picture_wall, element)
            for element in logic.list_floor:
                self.screen.blit(
                    graphic.constant.picture_floor, element
                )  # blit copy the surface picture on surface of screen_size
            for element in logic.list_start:
                self.screen.blit(graphic.constant.picture_floor, element)
            for element in logic.list_finish:
                self.screen.blit(graphic.constant.picture_floor, element)
                self.screen.blit(graphic.constant.picture_finish, element)
            self.graph_move(mac)

            if (mac.position[0] in bad.field_of_view) and mac.safe is True:
                bad_state = False
            if bad_state is False:
                for element in bad.position:
                    self.screen.blit(graphic.constant.picture_rip, element)
            else:
                for element in bad.position:
                    self.screen.blit(graphic.constant.picture_badguy, element)
            self.item_pos(mac, item)
            mac_lose = False
            if (mac.position[0] in bad.field_of_view) and mac.safe is False:
                for element in mac.position:
                    mac_lose = True
                    self.screen.blit(graphic.constant.picture_rip, element)
                    font_lose = pygame.font.Font(None, 36)
                    lose_surf = pygame.Surface((300, 200))
                    lose_surf_rect = lose_surf.get_rect()
                    lose_surf_rect.center = (337, 337)
                    lose_text_surface = font_lose.render(
                        "You lose !!!", 1, graphic.constant.white
                    )
                    lose_text_rect = lose_text_surface.get_rect()
                    lose_text_rect.center = (337, 337)
                    self.screen.blit(lose_surf, lose_surf_rect)
                    self.screen.blit(lose_text_surface, lose_text_rect)
                    pygame.display.flip()
                    while mac_lose:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
            else:
                for element in mac.position:
                    self.screen.blit(graphic.constant.picture_macgy, element)
                    if mac.free is True:
                        font_free = pygame.font.Font(None, 36)
                        free_surf = pygame.Surface((300, 200))
                        free_surf_rect = free_surf.get_rect()
                        free_surf_rect.center = (337, 337)
                        free_text_surface = font_free.render(
                            "You are free !!!", 1, graphic.constant.white
                        )
                        victory_text_rect = free_text_surface.get_rect()
                        victory_text_rect.center = (337, 337)
                        self.screen.blit(free_surf, free_surf_rect)
                        self.screen.blit(free_text_surface, victory_text_rect)
                        pygame.display.flip()
                        while mac.free:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()

            pygame.display.flip()  # tell to pygame display game surface
        pygame.quit()
