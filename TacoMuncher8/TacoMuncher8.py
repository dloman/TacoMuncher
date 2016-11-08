#!/usr/bin/python

import pygame
import Monster

################################################################################
################################################################################
class Game(object):

  ##############################################################################
  def __init__(self):
    self.monster = Monster.Monster()
    self.window = pygame.display.set_mode((1920,1080))
    self.clock = pygame.time.Clock()

  ##############################################################################
  def clearScreen(self):
    self.window.fill((0,0,0))

  ##############################################################################
  def eventHandler(self, event):
    if (event.type == pygame.QUIT):
      pygame.quit()
      exit()

  ##############################################################################
  def keyboardHandler(self, keys):
    if keys[pygame.K_LEFT]:
      self.monster.moveX(-10)
    if keys[pygame.K_RIGHT]:
      self.monster.moveX(10)

  ##############################################################################
  def drawScreen(self):
    self.clearScreen()
    self.monster.draw(self.window)
    pygame.display.flip()

  ##############################################################################
  def update(self):

    for event in pygame.event.get():
      self.eventHandler(event)

    self.keyboardHandler(pygame.key.get_pressed())

    self.drawScreen()
    self.clock.tick(50)

################################################################################
################################################################################
if __name__ == "__main__":
  pygame.init()
  pygame.display.set_caption('Taco Muncher!')
  Game = Game()
  while True:
    Game.update()

