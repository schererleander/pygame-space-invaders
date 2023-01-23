import pygame
from Steuerung import Steuerung

pygame.init() 

dieSteuerung = Steuerung()
dieSteuerung.loop()

pygame.quit()