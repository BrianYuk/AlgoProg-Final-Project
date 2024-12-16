import pygame as pg

class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = "resources/sound/"

        # Load sounds
        self.shotgun = pg.mixer.Sound(self.path + "shotgun.wav")
        self.npc_pain = pg.mixer.Sound(self.path + "npc_pain.wav")
        self.npc_death = pg.mixer.Sound(self.path + "npc_death.wav")
        self.npc_shot = pg.mixer.Sound(self.path + "npc_attack.wav")
        self.npc_shot.set_volume(0.2)
        self.player_pain = pg.mixer.Sound(self.path + "player_pain.wav")
        self.theme = pg.mixer.Sound(self.path + "troll_music.mp3")
        pg.mixer.music.set_volume(0.3)

    # Load music
    def load_music(self, game, volume=0.3):
        music_path = self.path + game
        try:
            pg.mixer.music.load(music_path)
            pg.mixer.music.set_volume(volume)
            print(f"Loaded music: {music_path}")
        except pg.error as e:
            print(f"Failed to load music: {music_path}\n{e}")