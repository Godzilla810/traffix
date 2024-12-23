import pygame
from setting import *

class SpriteSheet:
    def extract_images(sprite_sheet, images_num):
        """分割精靈表，提取所有幀"""
        images = []
        image_width = sprite_sheet.get_width() // images_num
        image_height = sprite_sheet.get_height()
        for i in range(images_num):
            image = sprite_sheet.subsurface(pygame.Rect(i * image_width, 0, image_width, image_height))
            image = pygame.transform.scale(image, (GRID_SIZE * image_width / image_height, GRID_SIZE))
            images.append(image)
        return images
