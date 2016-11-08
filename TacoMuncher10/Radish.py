
import pygame

################################################################################
################################################################################
class Radish(object):

  ##############################################################################
  def __init__(self):
    self.image = pygame.image.load("../Images/Items/radish.png")
    self.imageSize = self.image.get_size()
    self.xPosition = 960 - self.imageSize[0]/2
    self.yPosition = 10

  ##############################################################################
  def draw(self, window):
    window.blit(self.image, (self.xPosition, self.yPosition))

  ##############################################################################
  def moveX(self, distance):
    newPosition = self.xPosition + distance
    if 0 < newPosition < 1920 - self.imageSize[0]:
      self.xPosition = newPosition
