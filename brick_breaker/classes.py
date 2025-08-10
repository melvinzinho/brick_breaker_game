import pygame


class Brick:
    def __init__(self, x, y):
        self.pos = [x, y]
        self.active = True

        self.image = pygame.image.load(
            "brick_breaker/assets/full_metal_brick.png"
        ).convert_alpha()
        self.scale = pygame.transform.scale_by(self.image, 2)
        self.mask = pygame.mask.from_surface(self.scale)
