
import pygame

################################################################################
################################################################################
class GameObject(object):

  ##############################################################################
  def __init__(self, imageFilePath, xStart, yStart):
    self.image = pygame.image.load(imageFilePath)
    self.imageSize = self.image.get_size()
    self.xPosition = xStart - self.imageSize[0]/2
    self.yPosition = yStart
    self.isDead = False

  ##############################################################################
  def draw(self, window):
    window.blit(self.image, (self.xPosition, self.yPosition))

  ##############################################################################
  def moveX(self, distance):
    newPosition = self.xPosition + distance
    if 0 < newPosition < 1920 - self.imageSize[0]:
      self.xPosition = newPosition

  ##############################################################################
  def moveY(self, distance):
    self.yPosition += distance
    if self.yPosition > 1080:
      self.isDead = True

