from doompy.sprite_object import AnimatedSprite
from doompy.settings import config

from collections import deque
import pygame as pg


class Weapon(AnimatedSprite):
    def __init__(
        self,
        game,
        path=config.resource_root.joinpath("sprites/weapon/shotgun/0.png"),
        scale=0.4,
        animation_time=90,
        sound_path=config.resource_root.joinpath("sound/shotgun.wav"),
        damage=100,
    ):
        super().__init__(game=game, path=path, scale=scale, animation_time=animation_time)

        self.shoot_sound = pg.mixer.Sound(sound_path)
        self.shoot_sound.set_volume(config.VOLUME)

        self.images = deque(
            [
                pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
                for img in self.images
            ]
        )
        self.weapon_pos = (
            config.HALF_WIDTH - self.images[0].get_width() // 2,
            config.HEIGHT - self.images[0].get_height(),
        )
        self.reloading = False
        self.num_images = len(self.images)
        self.frame_counter = 0
        self.damage = damage
        self.shot = False

    def single_shot(self):
        self.shot = True
        self.reloading = True

    def continous_shot(self):
        raise NotImplementedError
    
    def animate_shot(self):
        if self.reloading:
            self.shot = False
            if self.animation_trigger:
                self.shoot_sound.play()
                self.images.rotate(-1)
                self.image = self.images[0]
                self.frame_counter += 1
                if self.frame_counter == self.num_images:
                    self.reloading = False
                    self.shot = False
                    self.frame_counter = 0

    def draw(self):
        self.game.screen.blit(self.images[0], self.weapon_pos)

    def update(self):
        self.check_animation_time()
        self.animate_shot()


class Shotgun(Weapon):
    def __init__(self, game, scale=0.4):
        path = config.resource_root.joinpath("sprites/weapon/shotgun/0.png")
        animation_time = 90
        sound_path = config.resource_root.joinpath("sound/shotgun.wav")
        damage = 50
        super().__init__(
            game=game, path=path, scale=scale, animation_time=animation_time, sound_path=sound_path, damage=damage
        )


class Pistol(Weapon):
    def __init__(self, game, scale=0.4):
        path=config.resource_root.joinpath("sprites/weapon/shotgun/0.png")
        animation_time = 30
        sound_path = config.resource_root.joinpath("sound/shotgun.wav")
        damage = 20
        super().__init__(
            game=game, path=path, scale=scale, animation_time=animation_time, sound_path=sound_path, damage=damage
        )


class FooGun(Weapon):
    def __init__(self, game, scale=0.4):
        path=config.resource_root.joinpath("sprites/weapon/foo/0.png")
        animation_time = 30
        sound_path = config.resource_root.joinpath("sound/shotgun.wav")
        damage = 40
        super().__init__(
            game=game, path=path, scale=scale, animation_time=animation_time, sound_path=sound_path, damage=damage
        )





class MachineGun(Weapon):
    def __init__(
        self,
        game,
        path=config.resource_root.joinpath("sprites/weapon/shotgun/0.png"),
        scale=0.4,
        animation_time=10,
        sound_path=config.resource_root.joinpath("sound/shotgun.wav"),
        damage=20,
    ):
        super().__init__(game, path, scale, animation_time, sound_path, damage)
