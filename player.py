import pygame as pg
from settings import Settings # (*) doesn't work for some reason 
import math

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = Settings.player_pos
        self.angle = Settings.player_angle
        self.shot = False
        self.health = Settings.player_max_health
        self.rel = 0
        self.health_recovery_delay = 700
        self.time_prev = pg.time.get_ticks()
        # Diagonal movement correction
        self.diag_move_corr = 1 / math.sqrt(2)

    def recover_health(self):
        if self.check_health_recovery_delay() and self.health < Settings.player_max_health:
            self.health += 1

    def check_health_recovery_delay(self):
        time_now = pg.time.get_ticks()
        if time_now - self.time_prev > self.health_recovery_delay:
            self.time_prev = time_now
            return True

    def check_game_over(self):
        if self.health < 1:
            self.game.object_renderer.game_over()
            pg.display.flip()
            pg.time.delay(2000)
            self.game.new_game()

    def get_damage(self, damage):
        self.health -= damage
        self.game.object_renderer.player_damage()
        self.game.sound.player_pain.play()
        self.check_game_over()

    def single_fire_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and not self.shot and not self.game.weapon.reloading:
                self.game.sound.shotgun.play()
                self.shot = True
                self.game.weapon.reloading = True

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = Settings.player_speed * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()
        num_key_pressed = -1
        if keys[pg.K_w]:
            num_key_pressed += 1
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            num_key_pressed += 1
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            num_key_pressed += 1
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            num_key_pressed += 1
            dx += -speed_sin
            dy += speed_cos

        # Diag move correction
        if num_key_pressed:
            dx *= self.diag_move_corr
            dy *= self.diag_move_corr

        self.check_wall_collision(dx, dy)

        # Camera movement with arrow keys
        if keys[pg.K_LEFT]:
            self.angle -= Settings.player_rot_speed * self.game.delta_time
        if keys[pg.K_RIGHT]:
            self.angle += Settings.player_rot_speed * self.game.delta_time
        self.angle %= math.tau

    def check_wall(self, x, y):
        map_value = self.game.map.world_map.get((x, y), None)
        return map_value is None or map_value in self.game.map.non_colliding_tiles
    
    def check_wall_collision(self, dx, dy):
        scale = Settings.player_size_scale / self.game.delta_time
        if self.check_wall(int(self.x + dx * scale), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * scale)):
            self.y += dy

    def draw(self):
        #pg.draw.line(self.game.screen, "yellow", (self.x * 100, self.y * 100),
        #             (self.x * 100 + Settings.width * math.cos(self.angle), 
        #             self.y * 100 + Settings.width * math.sin(self.angle)), 2)
        pg.draw.circle(self.game.screen, "green", (self.x * 100, self.y * 100), 15)

    def mouse_control(self):
        mx, my = pg.mouse.get_pos()
        if mx < Settings.mouse_border_left or mx > Settings.mouse_border_right:
            pg.mouse.set_pos([Settings.half_width, Settings.half_height])
        self.rel = pg.mouse.get_rel()[0]
        self.rel = max(-Settings.mouse_max_rel, min(Settings.mouse_max_rel, self.rel))
        self.angle += self.rel * Settings.mouse_sensitivity * self.game.delta_time

    def update(self):
        self.movement()
        self.mouse_control()
        self.recover_health()

    @property
    def pos(self):
        return self.x, self.y
    
    @property
    def map_pos(self):
        return int(self.x), int(self.y)