import pygame
import os

def loadImage(name):
    return pygame.image.load(os.path.join("Assets", name))