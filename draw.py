import pygame
from main import transfer
from load import loadImage

def draw_letter_box(window, box, x_offset, y_offset):
    window.blit(box, (x_offset, y_offset))

def draw_white(window, sizeX, sizeY, posX, poxY, blank=loadImage("HangmanBlank.png")):
    blank = pygame.transform.scale(blank, (sizeX, sizeY))
    window.blit(blank, (posX, poxY))
    pygame.display.update()

