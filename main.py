import pygame
import os

pygame.font.init()

# Setting up the screen size
WIDTH, HEIGHT = 900, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)
FPS = 60

SCALED_WIDTH, SCALED_HEIGHT = WIDTH * 0.7, HEIGHT * 0.7

# Getting hangman image from assets folder
HANG_MAN_IMAGE = pygame.image.load(
    os.path.join("Assets", "Hangman.png"))
# Scale hang man image
HANG_MAN = pygame.transform.scale(HANG_MAN_IMAGE, (SCALED_WIDTH, SCALED_HEIGHT))
pygame.display.set_caption("Hangman")

SECRET_WORD = "How, are, you, doing"
WORDS = SECRET_WORD.split()

FONT = "Comic Sans MS"
TEXT_SIZE = 50
#DashPosition = set()
# RGB colors and have to update the display to actually change colors

size = SCALED_HEIGHT / len(SECRET_WORD) - 10
lineSize = size if size > 25 else 25
def draw_window():
    WINDOW.fill(WHITE)
    # Drawing hangman image into screen
    WINDOW.blit(HANG_MAN, (0, 0))

    
    
    prevPositionX, newPositionX = 500, 500 + lineSize

    positionY = 100
    curWord = 1
    for i in SECRET_WORD:
        
        if i == " ":
            word = WORDS[curWord]
            curWord += 1
            totalSpaceTaken = len(word) * lineSize + newPositionX
            
            
            if WIDTH - totalSpaceTaken < 0:
                positionY += 50
                prevPositionX, newPositionX = 500, 500 + lineSize
                continue
        elif i == ",":
            text = pygame.font.SysFont(FONT, TEXT_SIZE)
            text = text.render(",", False, (0,0,0))
            WINDOW.blit(text, (prevPositionX - 10, positionY - 50))
        else: 
            newLine = pygame.draw.line(WINDOW, (0,0,0), (prevPositionX, positionY), (newPositionX, positionY), 4)
            #DashPosition.add((prevPositionX, newPositionX, positionY))
        prevPositionX, newPositionX = newPositionX + 10, newPositionX + lineSize + 10
        
    pygame.display.update()

# The function main will be where we run the game
def main():
    clock = pygame.time.Clock()
    run = True
    # To run pygame, you must have to check if the user has quit the screen
    # pygame.QUIT tells us that the user has exited out of the window
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()
         
    pygame.quit()



# Running main function only if the current file name is called main
# cannot run main from another file
if __name__ == "__main__":
    main()
