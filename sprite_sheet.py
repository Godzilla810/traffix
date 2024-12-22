import pygame

class SpriteSheet:
    def extract_images(sprite_sheet, frames_num):
        """分割精靈表，提取所有幀"""
        frames = []
        frame_width = sprite_sheet.get_width() // frames_num
        frame_height = sprite_sheet.get_height()
        for i in range(frames_num):
            frame = sprite_sheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
            frames.append(frame)
        return frames
