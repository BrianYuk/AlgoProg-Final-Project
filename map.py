import pygame as pg

_ = False # The empty space in the map
mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 3, 3, 3, 3, _, _, _, 2, 2, 2, _, _, 1],
    [1, _, _, _, _, _, 4, _, _, _, _, _, 2, _, _, 1],
    [1, _, _, _, _, _, 4, _, _, _, _, _, 2, _, _, 1],
    [1, _, _, 3, 3, 3, 3, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, 4, _, _, _, 4, _, _, _, _, _, _, 1],
    [1, 1, 1, 3, 1, 3, 1, 1, 1, 3, _, _, 3, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 3, _, _, 3, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 3, _, _, 3, 1, 9, 1],
    [1, 1, 3, 1, 1, 1, 1, 1, 1, 3, _, _, 3, 1, 1, 1],
    [1, 4, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 2, _, _, _, _, _, 3, 4, _, 4, 3, _, 1],
    [1, _, _, 5, _, _, _, _, _, _, 3, _, 3, _, _, 1],
    [1, _, _, 2, _, _, _, _, _, _, _, _, _, _, _, 1],
    [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, 4, _, _, _, _, _, _, 4, _, _, 4, _, _, _, 1],
    [1, 1, 3, 3, _, _, 3, 3, 1, 3, 3, 1, 3, 1, 1, 1],
    [1, 6, 1, 3, _, _, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 3, 3, 4, _, _, 4, 3, 3, 3, 3, 3, 3, 3, 3, 1],
    [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3],
    [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3],
    [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3],
    [3, _, _, 5, _, _, 4, 4, _, _, 4, 4, _, _, _, 3],
    [3, _, _, 5, _, _, 4, 4, _, _, 4, 4, _, _, _, 3],
    [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3],
    [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3],
    [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3],
    [3, 3, 3, 3, 3, 4, 4, _, _, 4, 4, 3, 10, 3, 3, 3],
    [1, 3, 3, 3, 3, 3, 4, _, _, 4, 17, _, _, _, 16, 1],
    [1, 3, 3, 3, 3, 3, 4, _, _, 4, 11, _, _, _, 7, 1],
    [1, 3, 3, 3, 3, 3, 4, _, _, 4, 9, _, _, _, 8, 1],
    [1, 3, 3, 3, 3, 3, 4, _, _, 4, 13, _, _, _, 12, 1],
    [1, 3, 3, 3, 3, 4, 4, _, _, 4, 4, 6, 15, 14, 3, 1],
    [1, 7, 3, 4, 4, _, _, _, _, _, _, 4, 4, 3, 3, 1],
    [1, 4, 4, _, _, _, _, _, _, _, _, _, _, 4, 4, 1],
    [4, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 4],
    [4, _, _, _, 3, _, _, _, _, _, _, 4, _, _, _, 4],
    [4, _, _, 4, _, _, _, _, _, _, _, _, _, _, _, 4],
    [5, _, _, _, _, _, _, 4, 3, _, _, _, _, _, _, 5],
    [5, _, _, _, _, _, _, 2, 4, _, _, _, _, _, _, 5],
    [4, _, _, _, _, _, _, _, _, _, _, _, 3, _, _, 4],
    [4, _, _, _, 3, _, _, _, _, _, _, 4, _, _, _, 4],
    [4, _, _, _, _, _, _, _, _, _, 3, _, _, _, _, 4],
    [1, 4, 4, _, _, _, _, _, _, _, _, _, _, 4, 4, 1],
    [1, 3, 3, 4, 4, _, _, _, _, _, _, 4, 4, 3, 3, 1],
    [1, 3, 3, 3, 3, 4, 4, _, _, 4, 4, 3, 3, 3, 3, 1],
    [1, 3, 3, 3, 3, 3, 4, 5, 5, 4, 3, 3, 3, 3, 3, 1],
]

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.non_colliding_tiles = {10}  #To set value for 10 as a non-colliding object for "easter egg" room
        self.rows = len(self.mini_map)
        self.cols = len(self.mini_map[0])
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    def draw(self):
        for pos, value in self.world_map.items():
            color = "darkgray" if value not in self.non_colliding_tiles else "lightgray" # No collision for "_" and "10"
            pg.draw.rect(self.game.screen, color, (pos[0] * 100, pos[1] * 100, 100, 100), 2)