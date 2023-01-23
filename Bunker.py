import pygame

class Bunker(pygame.sprite.Sprite):
  def __init__(self, x: int, y: int, groeße: int, farbe: tuple):
    super().__init__()
    self.image = pygame.Surface((groeße,groeße))
    self.image.fill(farbe)
    self.rect = self.image.get_rect()
    self.rect.center = (x,y)