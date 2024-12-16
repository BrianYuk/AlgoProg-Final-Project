import pygame as pg
from settings import Settings

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
        self.sky_image = self.get_texture("resources/textures/sky.png", (Settings.width, Settings.half_height))
        self.sky_offset = 0
        self.blood_screen = self.get_texture("resources/textures/blood_screen.png", Settings.res)
        self.digit_size = 90
        self.digit_images = [self.get_texture(f"resources/textures/digits/{i}.png", [self.digit_size] * 2) 
                             for i in range(11)]
        self.digits = dict(zip(map(str, range(11)), self.digit_images))
        self.game_over_image = self.get_texture("resources/textures/game_over.png", Settings.res)
        self.win_image = self.get_texture("resources/textures/win.png", Settings.res)

    def draw(self):
        self.draw_background()
        self.render_game_objects()
        self.draw_player_health()

    def win(self):
        self.screen.blit(self.win_image, (0, 0))

    def game_over(self):
        self.screen.blit(self.game_over_image, (0, 0))

    def draw_player_health(self):
        health = str(self.game.player.health)
        for i, char in enumerate(health):
            self.screen.blit(self.digits[char], (i * self.digit_size, 0))
        self.screen.blit(self.digits["10"], ((i + 1) * self.digit_size, 0))

    def player_damage(self):
        self.screen.blit(self.blood_screen, (0, 0))

    def draw_background(self):
        self.sky_offset = (self.sky_offset + 4.5 * self.game.player.rel) % Settings.width
        self.screen.blit(self.sky_image, (-self.sky_offset, 0))
        self.screen.blit(self.sky_image, (-self.sky_offset + Settings.width, 0))
        # Floor
        pg.draw.rect(self.screen, Settings.floor_color, (0, Settings.half_height, Settings.width, Settings.height))

    def render_game_objects(self):
        list_objects = sorted(self.game.raycasting.objects_to_render, key=lambda t: t[0], reverse=True)
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    @staticmethod
    def get_texture(path, res=(Settings.texture_size, Settings.texture_size)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)
    
    def load_wall_textures(self):
        return {
            1: self.get_texture("resources/textures/1.png"), 
            2: self.get_texture("resources/textures/2.png"), 
            3: self.get_texture("resources/textures/3.png"), 
            4: self.get_texture("resources/textures/4.png"), 
            5: self.get_texture("resources/textures/5.png"), 
            6: self.get_texture("resources/textures/6.jpg"), 
            7: self.get_texture("resources/textures/7.jpg"), 
            8: self.get_texture("resources/textures/8.jpg"), 
            9: self.get_texture("resources/textures/9.jpg"),
            10: self.get_texture("resources/textures/10.png"),
            11: self.get_texture("resources/textures/11.jpg"),
            12: self.get_texture("resources/textures/12.jpg"),
            13: self.get_texture("resources/textures/13.jpg"),
            14: self.get_texture("resources/textures/14.jpg"),
            15: self.get_texture("resources/textures/15.jpg"),
            16: self.get_texture("resources/textures/16.jpg"),
            17: self.get_texture("resources/textures/17.jpg")
        }