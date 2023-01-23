import pygame
from Szenen import *

class Steuerung():
  def __init__(self):
    self.__szene = Menue()
    self.__szenenIndex = 0
    self.__verlasseSpiel = False
    self.__spielerListe = []
    self.__loop()

  def __sotiereSpielerListe(self):
    self.__spielerListe.sort(key=lambda spieler: spieler[1], reverse=True)

  def __addSpieler(self, spielerName: str, spielerScore: int):
    gibtSpieler = False
    for spieler in range(len(self.__spielerListe)):
      if self.__spielerListe[spieler][0] == spielerName:
        gibtSpieler = True
        self.__spielerListe[spieler][1] = spielerScore
    if not gibtSpieler:
      self.__spielerListe.append((spielerName, spielerScore))

  def __verlasseSpiel(self):
    self.__verlasseSpiel = True

  def __wechselSzene(self):
    self.__szenenIndex += 1
    if self.__szenenIndex > 3:
      self.__szenenIndex = 0
    match(self.__szenenIndex):
      case 0:
        self.__szene = Menue()
      case 1:
        self.__szene = Game()
      case 2:
        score = self.__szene.getScore()
        self.__szene = Benennung(score)
      case 3:
        score = self.__szene.getScore()
        name = self.__szene.getName()
        self.__addSpieler(name, score)
        self.__sotiereSpielerListe()
        self.__szene = Score(self.__spielerListe)


  def __loop(self):  
    while not self.__szene == None and not self.__verlasseSpiel:
      events = []
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.__verlasseSpiel = True
        if event.type == pygame.KEYDOWN:
          events.append(event)
          self.__szene.beiEingabe(events)

      self.__szene.beiUpdate()

      self.__szene.beiZeichne()

      if self.__szene.getWechselSzene():
        self.__wechselSzene()