import pygame
from setting import *

class Animation(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet, images_num, animation_delay):
        self.animation = SpriteSheet.extract_images(sprite_sheet, images_num)
        self.frame = 0
        self.animation_time = 0
        self.animation_delay = animation_delay
        self.image : pygame.Surface = self.animation[0]

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.animation_time > self.animation_delay:
            self.frame += 1
            self.animation_time = now
            self.image = self.animation[self.frame % len(self.animation)]

class SpriteSheet:
    def extract_images(sprite_sheet : pygame.Surface, images_num : int) -> list[pygame.Surface]:
        images = []
        image_width = sprite_sheet.get_width() // images_num
        image_height = sprite_sheet.get_height()
        for i in range(images_num):
            image = sprite_sheet.subsurface(pygame.Rect(i * image_width, 0, image_width, image_height))
            image = pygame.transform.scale(image, (GRID_SIZE * image_width / image_height, GRID_SIZE))
            images.append(image)
        return images
