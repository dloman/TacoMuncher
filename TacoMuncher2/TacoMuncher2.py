#!/usr/bin/python

import pygame

gWindow = pygame.display.set_mode((1920,1080))

################################################################################
def updateScreen():
  gWindow.fill((0, 0, 0))
  pygame.display.flip()

################################################################################
################################################################################
if __name__ == "__main__":
  pygame.init()
  pygame.display.set_caption('Taco Muncher!')
  clock = pygame.time.Clock()
  while True:
    updateScreen()
    clock.tick(50)

