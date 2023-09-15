import pygame
import os


# Setting up the screen size
WIDTH, HEIGHT = 900, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)
FPS = 60

pygame.display.set_caption("Hangman")


# RGB colors and have to update the display to actually change colors
def fill_window():
    WINDOW.fill(WHITE)
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
        fill_window()
         
    pygame.quit()



# Running main function only if the current file name is called main
# cannot run main from another file
if __name__ == "__main__":
    main()
