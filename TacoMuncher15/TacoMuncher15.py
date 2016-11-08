#!/usr/bin/python

from GameObject import GameObject

import pygame
import random

################################################################################
################################################################################
class Game(object):

  ##############################################################################
  def __init__(self):
    self.monster = GameObject("../Images/Monsters/1.png", 960, 660)
    self.radishes = []
    self.window = pygame.display.set_mode((1920,1080))
    self.clock = pygame.time.Clock()
    self.isGameOver = False

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
    if self.isGameOver:
      self.drawGameOver()
    else:
      self.monster.draw(self.window)
      for radish in self.radishes:
        radish.draw(self.window)
    pygame.display.flip()

  ##############################################################################
  def drawGameOver(self):
    font = pygame.font.Font('freesansbold.ttf',200)
    surface = font.render('GAME OVER!', True, (255,0,0))
    rectangle = surface.get_rect()
    rectangle.midbottom = (960, 540)
    self.window.blit(surface, rectangle)

  ##############################################################################
  def update(self):
    self.randomRadishCreation()

    for event in pygame.event.get():
      self.eventHandler(event)

    self.keyboardHandler(pygame.key.get_pressed())

    self.gravity()

    self.checkForCollisions()

    self.removeDeadRadishs()

    self.drawScreen()
    self.clock.tick(50)

  ##############################################################################
  def checkForCollisions(self):
    for radish in self.radishes:
      if self.monster.checkForCollision(radish.xPosition, radish.yPosition, radish.imageSize):
        self.monster.kill("../Images/Monsters/Dead1.png")
        return

  ##############################################################################
  def gravity(self):
    for radish in self.radishes:
      radish.moveY(10)

  ##############################################################################
  def randomRadishCreation(self):
    if random.randint(0, 100) > 98:
      radishImageFileName = "../Images/Items/radish.png"

      xPosition = random.randint(0, 1857)

      newRadish = GameObject(radishImageFileName, xPosition, -10)

      self.radishes.append(newRadish)

  ##############################################################################
  def removeDeadRadishs(self):
    aliveRadishes = []
    for radish in self.radishes:
      if not radish.isDead:
        aliveRadishes.append(radish)
    self.radishes = aliveRadishes
    if self.monster.isDead:
      self.monster.moveY(5)
      if self.monster.yPosition > 1080:
        self.isGameOver = True

################################################################################
################################################################################
if __name__ == "__main__":
  pygame.init()
  pygame.display.set_caption('Taco Muncher!')
  Game = Game()
  while True:
    Game.update()

