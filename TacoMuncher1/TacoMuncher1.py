#!/usr/bin/python

import pygame

gWindow = pygame.display.set_mode((1920,1080))

################################################################################
################################################################################
pygame.init()
pygame.display.set_caption('Taco Muncher!')
clock = pygame.time.Clock()
while True:
  gWindow.fill((0, 0, 0))
  pygame.display.flip()
  clock.tick(50)

