import pygame
from main import transfer
from load import loadImage

WINDOW, WIDTH, HEIGHT, XOFFSET, YOFFSET, FONT, LETTER_BOX, lineSize, positions, WORDS = transfer()

TEXT_SIZE = lineSize * 2

def draw_letter_box(window, box, x_offset, y_offset):
    window.blit(box, (x_offset, y_offset))

def draw_white(window, sizeX, sizeY, posX, poxY, blank=loadImage("HangmanBlank.png")):
    blank = pygame.transform.scale(blank, (sizeX, sizeY))
    window.blit(blank, (posX, poxY))
    pygame.display.update()

def insertLetter(letter, text_size=25, widths=None, height=None, letterBox:bool=False, letterWidth=WIDTH, 
                 letterHeight=HEIGHT, boxOffsetX = XOFFSET, boxOffsetY=YOFFSET, window=WINDOW, font=FONT):
    global letter_Search
    letter_Search = letter
    text = pygame.font.SysFont(font, text_size * 2)
    text = text.render(letter.upper(), False, (0,0,0))
    half = text_size/2
    if letterBox: 
        centerX = (letterWidth - boxOffsetX)/2 - half
        centerY = (letterHeight - boxOffsetY)/2 - text_size
    else:
        centerX = (widths[1] + widths[0])/2  - half
        centerY = height - text_size * 2.5
    window.blit(text, (centerX, centerY))
    pygame.display.update()

def drawScreen(image, transparency):

    endingScreen = pygame.transform.scale(loadImage(image), (900, 500)) # size of window
    endingScreen.set_alpha(transparency)
    WINDOW.blit(endingScreen, (0,0))
    pygame.display.update()

