import os
import pygame
from setting import *

class Animation(pygame.sprite.Sprite):
    def __init__(self, path, animation_delay, images_num = None):
        # sprite_sheet
        if path.endswith('.png') or path.endswith('.jpg'):
            self.animation = Tool.extract_images_from_sprite_sheet(path, images_num)
        # folder
        else:
            self.animation = Tool.extract_images_from_folder(path)
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

class Tool():
    def extract_images_from_sprite_sheet(sprite_sheet_path : str, images_num : int) -> list[pygame.Surface]:
        images = []
        sprite_sheet = pygame.image.load(sprite_sheet_path).convert_alpha()
        image_width = sprite_sheet.get_width() // images_num
        image_height = sprite_sheet.get_height()
        for i in range(images_num):
            image = sprite_sheet.subsurface(pygame.Rect(i * image_width, 0, image_width, image_height))
            image = pygame.transform.scale(image, (GEM_SIZE * image_width / image_height, GEM_SIZE))
            images.append(image)
        return images
    
    def extract_images_from_folder(forder_path : str) -> list[pygame.Surface]:
        images = []
        for file in os.listdir(forder_path):
            image = pygame.image.load(f"{forder_path}/{file}")
            image = pygame.transform.scale(image, (GEM_SIZE, GEM_SIZE))
            images.append(image)
        return images
