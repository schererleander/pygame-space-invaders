import pygame
import os

class Extra(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()
    self.image = pygame.image.load(os.path.abspath('assets/img/extra.png'))
    self.rect = self.image.get_rect()
    self.rect.center = (x,y)

    self.__geschwindigkeit = 2
  
  def bewegen(self):
    self.rect.x = self.rect.x + self.__geschwindigkeit
  
  def einschraenken(self, screenLaenge):
    if self.rect.left >= screenLaenge:
      self.kill()