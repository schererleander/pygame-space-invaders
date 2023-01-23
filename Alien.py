import pygame
import os

class Alien(pygame.sprite.Sprite):
  def __init__(self, bildDateipfad: str, position: tuple, wert: int):
    super().__init__()
    self.image = pygame.image.load(os.path.abspath(bildDateipfad))
    self.rect = self.image.get_rect()
    self.rect.center = position
    
    self.__wert = wert
    self.__geschwindigkeit = 1
  
  def getRect(self):
    return self.rect

  def getWert(self) -> int:
    return self.__wert
  
  def aendereRichtung(self):
    self.__geschwindigkeit *= -1

  def bewegen(self):
    self.rect.x += self.__geschwindigkeit
  
  def bewegeRunter(self, y):
    self.rect.y += y