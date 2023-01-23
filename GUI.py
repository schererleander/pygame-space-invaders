import pygame
import os

class GUI():
  def __init__(self, screen):
    self.__screen = screen

  def zeichneText(self, text: str, groeße: int, x: int, y: int, farbe: tuple):
    font = pygame.font.Font(os.path.abspath('assets/8bit.ttf'), groeße)
    text = font.render(text, True, farbe)
    self.__screen.blit(text, (x-text.get_width()/2, y-text.get_height()/2))

  def zeichneRoundedButton(self, text: str, groeße: int, x: int, y: int, weite: int, hoehe: int, radius: int, farbeButton: tuple, farbeText: tuple):

    pygame.draw.aaline(self.__screen,farbeButton,(x-weite/2,y-hoehe/2+radius),(x-weite/2,y+hoehe/2-radius)) #left line
    pygame.draw.aaline(self.__screen,farbeButton,(x+weite/2,y-hoehe/2+radius),(x+weite/2,y+hoehe/2-radius)) #right line
    pygame.draw.aaline(self.__screen,farbeButton,(x-weite/2+radius,y-hoehe/2),(x+weite/2-radius,y-hoehe/2)) #top line
    pygame.draw.aaline(self.__screen,farbeButton,(x-weite/2+radius,y+hoehe/2),(x+weite/2-radius,y+hoehe/2)) #bottom line

    pygame.draw.circle(self.__screen,farbeButton,(x-weite/2+radius,y-hoehe/2+radius),radius, 0) #topleft circle
    pygame.draw.circle(self.__screen,farbeButton,(x+weite/2-radius,y-hoehe/2+radius),radius, 0) #topright circle
    pygame.draw.circle(self.__screen,farbeButton,(x-weite/2+radius,y+hoehe/2-radius),radius, 0) #bottomleft circle
    pygame.draw.circle(self.__screen,farbeButton,(x+weite/2-radius,y+hoehe/2-radius),radius, 0) #bottomright circle

    pygame.draw.rect(self.__screen, farbeButton, pygame.Rect(x-weite/2+radius,y-hoehe/2,weite-radius*2,hoehe)) #middle rect
    pygame.draw.rect(self.__screen, farbeButton, pygame.Rect(x-weite/2,y-hoehe/2+radius,radius,hoehe-radius*2)) #left rect
    pygame.draw.rect(self.__screen, farbeButton, pygame.Rect(x+weite/2-radius,y-hoehe/2+radius,radius,hoehe-radius*2)) #right rect

    font = pygame.font.Font(os.path.abspath('assets/8bit.ttf'), groeße)
    text = font.render(text, True, farbeText)
    self.__screen.blit(text, (x-text.get_width()/2, y-text.get_height()/2))
    
