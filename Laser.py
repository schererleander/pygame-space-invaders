import pygame

class Laser(pygame.sprite.Sprite):
  def __init__(self, position: tuple, geschwindigkeit: str):
    super().__init__()
    self.image = pygame.Surface((3,10))
    self.image.fill((255,255,255)) # Farbe
    self.rect = self.image.get_rect()
    self.rect.center = position
    
    self.__geschwindigkeit = geschwindigkeit

  def getRect(self):
    return self.rect

  def bewegen(self):
    self.rect.y += self.__geschwindigkeit