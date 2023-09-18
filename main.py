import pygame
import os

pygame.font.init()

# Setting up the screen size
WIDTH, HEIGHT = 900, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)
FPS = 60

SCALED_WIDTH, SCALED_HEIGHT = WIDTH * 0.4, HEIGHT * 0.6

LETTER_SIZE_WIDTH = 175
LETTER_SIZE_HEIGHT = 175

LETTER_BOX = pygame.image.load(
    os.path.join("Assets", "Enter-letter-box.png"))
LETTER_BOX = pygame.transform.scale(LETTER_BOX, (LETTER_SIZE_WIDTH, LETTER_SIZE_HEIGHT))
LETTER_BOX_X_OFFSET, LETTER_BOX_Y_OFFSET = 10, 10
# Getting hangman image from assets folder
HANG_MAN_IMAGE = pygame.image.load(
    os.path.join("Assets", "Hangman.png"))
# Scale hang man image
HANG_MAN = pygame.transform.scale(HANG_MAN_IMAGE, (SCALED_WIDTH, SCALED_HEIGHT))
pygame.display.set_caption("Hangman")

SECRET_WORD = "Hello, my name is andy"
WORDS = SECRET_WORD.split()

FONT = "Comic Sans MS"
TEXT_SIZE = 50

# RGB colors and have to update the display to actually change colors


lineSize = 25

PositionsOfLetters = {}
def draw_letter_box():
    WINDOW.blit(LETTER_BOX, (LETTER_BOX_X_OFFSET, LETTER_BOX_Y_OFFSET))
def draw_window():
    WINDOW.fill(WHITE)
    # Drawing hangman image into screen
    draw_letter_box()
    WINDOW.blit(HANG_MAN, (100, 0))
    

    
    
    prevPositionX, newPositionX = 500, 500 + lineSize

    positionY = 100
    curWord = 1
    prevLetter = None
    for i in SECRET_WORD:
        
        if i == " ":
            word = WORDS[curWord]
            curWord += 1
            totalSpaceTaken = len(word) * lineSize + newPositionX
            
            
            if WIDTH - totalSpaceTaken < 50:
                positionY += 50
                prevPositionX, newPositionX = 500, 500 + lineSize
                prevLetter = i
            elif prevLetter == ",":
                pass    
            else:
                prevPositionX, newPositionX = newPositionX + 10, newPositionX + lineSize + 10
            prevLetter = i
            continue

            
        elif i == ",":
            text = pygame.font.SysFont(FONT, TEXT_SIZE)
            text = text.render(",", False, (0,0,0))
            WINDOW.blit(text, (prevPositionX - 10, positionY - 50))

        else: 
            startPoint = (prevPositionX, positionY)
            endPoint = (newPositionX, positionY)
            PositionsOfLetters[(startPoint, endPoint)] = i
            pygame.draw.line(WINDOW, (0,0,0), startPoint, endPoint, 4)

        prevPositionX, newPositionX = newPositionX + 10, newPositionX + lineSize + 10
        prevLetter = i
        
    pygame.display.update()
def insertLetter(letter):
    letter = letter.title()
    text = pygame.font.SysFont(FONT, TEXT_SIZE * 2)
    text = text.render(letter, False, (0,0,0))
    half = TEXT_SIZE/2
    centerX = (LETTER_SIZE_WIDTH - LETTER_BOX_X_OFFSET)/2 - half
    centerY = (LETTER_SIZE_HEIGHT - LETTER_BOX_Y_OFFSET)/2 - TEXT_SIZE

    

    WINDOW.blit(text, (centerX, centerY))
    pygame.display.update()
    

# The function main will be where we run the game
def main():
    clock = pygame.time.Clock()
    run = True
    draw_window()
    # To run pygame, you must have to check if the user has quit the screen
    # pygame.QUIT tells us that the user has exited out of the window
    while run:
        clock.tick(FPS)

        key = None
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key)
                if not key.isalpha():
                    key = None
                
        

        if key:
            draw_letter_box()
            insertLetter(key)
                
    pygame.quit()

# Running main function only if the current file name is called main
# cannot run main from another file
if __name__ == "__main__":
    main()
