import pygame
import os


# Setting up the screen size
WIDTH, HEIGHT = 900, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)
FPS = 60

SCALED_WIDTH, SCALED_HEIGHT = WIDTH * 0.8, HEIGHT * 0.8

# Getting hangman image from assets folder
HANG_MAN_IMAGE = pygame.image.load(
    os.path.join("Assets", "Hangman.png"))
# Scale hang man image
HANG_MAN = pygame.transform.scale(HANG_MAN_IMAGE, (SCALED_WIDTH, SCALED_HEIGHT))
pygame.display.set_caption("Hangman")

CENTER_WIDTH = WIDTH/2
CENTER_IMAGE = CENTER_WIDTH - SCALED_WIDTH/2

# RGB colors and have to update the display to actually change colors
def draw_window():
    WINDOW.fill(WHITE)
    # Drawing hangman image into screen
    WINDOW.blit(HANG_MAN, (CENTER_IMAGE, 0))
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
