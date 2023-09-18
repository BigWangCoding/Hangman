import pygame
from load import loadImage

pygame.font.init()

LETTER_BOX = loadImage("Enter-letter-box.png")
HANG_MAN_IMAGE_6 = loadImage("Hangman6.png")
HANG_MAN_IMAGE_5 = loadImage("Hangman5.png")
HANG_MAN_IMAGE_4 = loadImage("Hangman4.png")
HANG_MAN_IMAGE_3 = loadImage("Hangman3.png")
HANG_MAN_IMAGE_2 = loadImage("Hangman2.png")
HANG_MAN_IMAGE_1 = loadImage("Hangman1.png")
HANG_MAN_IMAGE_0 = loadImage("Hangman0.png")

lives_to_image = {
    6: HANG_MAN_IMAGE_6,
    5: HANG_MAN_IMAGE_5,
    4: HANG_MAN_IMAGE_4,
    3: HANG_MAN_IMAGE_3,
    2: HANG_MAN_IMAGE_2,
    1: HANG_MAN_IMAGE_1,
    0: HANG_MAN_IMAGE_0,

}

WIDTH, HEIGHT = 900, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)
FPS = 60

SCALED_WIDTH, SCALED_HEIGHT = WIDTH * 0.35, HEIGHT * 0.6

LETTER_SIZE_WIDTH = 175
LETTER_SIZE_HEIGHT = 175


LETTER_BOX = pygame.transform.scale(LETTER_BOX, (LETTER_SIZE_WIDTH, LETTER_SIZE_HEIGHT))
LETTER_BOX_X_OFFSET, LETTER_BOX_Y_OFFSET = 10, 10

pygame.display.set_caption("Hangman")

def transformHangMan(HANG_MAN_IMAGE):
    return pygame.transform.scale(HANG_MAN_IMAGE, (SCALED_WIDTH, SCALED_HEIGHT))
    

SECRET_WORD = "Hello, my name is andy"
lenOfCharacters = len("".join([i for i in SECRET_WORD if i.isalpha()]))
WORDS = SECRET_WORD.split()

FONT = "Comic Sans MS"
TEXT_SIZE = 50

lives = 6

lineSize = 25

PositionsOfLetters = {}

def draw_letter_box():
    WINDOW.blit(LETTER_BOX, (LETTER_BOX_X_OFFSET, LETTER_BOX_Y_OFFSET))

def draw_window(HANG_MAN):
    WINDOW.fill(WHITE)
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
            PositionsOfLetters[(startPoint, endPoint)] = i.lower()
            pygame.draw.line(WINDOW, (0,0,0), startPoint, endPoint, 4)

        prevPositionX, newPositionX = newPositionX + 10, newPositionX + lineSize + 10
        prevLetter = i
        
    pygame.display.update()


letter_Search = None
def insertLetter(letter, text_size, widths=None, height=None, letterBox:bool=False):
    global letter_Search
    letter_Search = letter

    text = pygame.font.SysFont(FONT, text_size * 2)
    text = text.render(letter.upper(), False, (0,0,0))
    half = text_size/2
    if letterBox: 
        centerX = (LETTER_SIZE_WIDTH - LETTER_BOX_X_OFFSET)/2 - half
        centerY = (LETTER_SIZE_HEIGHT - LETTER_BOX_Y_OFFSET)/2 - TEXT_SIZE
    else:
        centerX = (widths[1] + widths[0])/2  - half
        centerY = height - text_size * 2.5
    WINDOW.blit(text, (centerX, centerY))
    pygame.display.update()

def searchPositions(letter_Search):
    global lives
    found = False
    for i in PositionsOfLetters:
        if PositionsOfLetters[i] == letter_Search:
            insertLetter(letter_Search, int(lineSize/2), (i[0][0], i[1][0]), i[0][1])
            found = True
    if not found:
        lives -= 1
        HANG_MAN = transformHangMan(lives_to_image[lives])
        WINDOW.blit(HANG_MAN, (100, 0))
        pygame.display.update()
        
        

entered_keys = set()
def main():
    clock = pygame.time.Clock()
    run = True
    HANG_MAN = transformHangMan(HANG_MAN_IMAGE_6)
    draw_window(HANG_MAN)

    while run and lives != 0:
        clock.tick(FPS)

        key = None
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key)
                if not key.isalpha():
                    key = None
                
                print(key)
        if key == "backspace":
            draw_letter_box()
            pygame.display.update()
        elif key == "return":
            searchPositions(letter_Search)
            draw_letter_box()
            pygame.display.update()
        elif key == "tab" or (not key) or (key in entered_keys):
            pass
        elif key:
            entered_keys.add(key)
            draw_letter_box()
            insertLetter(key, letterBox=True, text_size=TEXT_SIZE)
                
    pygame.quit()

# Running main function only if the current file name is called main
# cannot run main from another file
if __name__ == "__main__":
    main()
    print(entered_keys)
