
import pygame

################################################################################
################################################################################
class Monster(object):

  ##############################################################################
  def __init__(self):
    self.image = pygame.image.load("../Images/Monsters/1.png")
    self.imageSize = self.image.get_size()
    self.xPosition = 960 - self.imageSize[0]/2
    self.yPosition = 660

  ##############################################################################
  def draw(self, window):
    window.blit(self.image, (self.xPosition, self.yPosition))
