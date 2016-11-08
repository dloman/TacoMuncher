
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
    if not self.isDead:
      newPosition = self.xPosition + distance
      if 0 < newPosition < 1920 - self.imageSize[0]:
        self.xPosition = newPosition

  ##############################################################################
  def moveY(self, distance):
    self.yPosition += distance
    if self.yPosition > 1080:
      self.isDead = True

  ##############################################################################
  def checkForCollision(self, xPosition, yPosition, size):
    xOverlap = \
      self.xPosition <= xPosition <= self.xPosition + self.imageSize[0] or \
      xPosition <= self.xPosition <= xPosition + size[0]

    yOverlap = \
      self.yPosition <= yPosition <= self.yPosition + self.imageSize[1] or \
      yPosition <= self.yPosition <= yPosition + size[1]

    return xOverlap and yOverlap

  ##############################################################################
  def kill(self, imageFilePath = None):
    if imageFilePath:
      self.image = pygame.image.load(imageFilePath)
    self.isDead = True
