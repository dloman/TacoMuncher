#!/usr/bin/python

import pygame

gWindow = pygame.display.set_mode((1920,1080))

################################################################################
def updateScreen():
  gWindow.fill((0, 0, 0))
  pygame.display.flip()

################################################################################
def eventHandler(event):
  if (event.type == pygame.QUIT):
    pygame.quit()
    exit()

################################################################################
def keyboardHandler(keys):
  if keys[pygame.K_LEFT]:
    print "Left!"
  if keys[pygame.K_RIGHT]:
    print "Right!"

################################################################################
################################################################################
if __name__ == "__main__":
  pygame.init()
  pygame.display.set_caption('Taco Muncher!')
  clock = pygame.time.Clock()
  while True:
    for Event in pygame.event.get():
      eventHandler(Event)
    keyboardHandler(pygame.key.get_pressed())
    updateScreen()
    clock.tick(50)
