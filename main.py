import pygame
import draw
from load import loadImage
from random import randint
import json
pygame.font.init()

LETTER_BOX = loadImage("Enter-letter-box.png")
HANG_MAN_IMAGE_6 = loadImage("Hangman6.png")
HANG_MAN_IMAGE_5 = loadImage("Hangman5.png")
HANG_MAN_IMAGE_4 = loadImage("Hangman4.png")
HANG_MAN_IMAGE_3 = loadImage("Hangman3.png")
HANG_MAN_IMAGE_2 = loadImage("Hangman2.png")
HANG_MAN_IMAGE_1 = loadImage("Hangman1.png")
HANG_MAN_IMAGE_0 = loadImage("Hangman0.png")

BLANK = loadImage("HangmanBlank.png")

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
SURFACE = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

WHITE = (255, 255, 255)
FPS = 60

SCALED_WIDTH, SCALED_HEIGHT = WIDTH * 0.35, HEIGHT * 0.6

LETTER_SIZE_WIDTH = 175
LETTER_SIZE_HEIGHT = 175

lineSize = 25

LETTER_BOX = pygame.transform.scale(LETTER_BOX, (LETTER_SIZE_WIDTH, LETTER_SIZE_HEIGHT))
LETTER_BOX_X_OFFSET, LETTER_BOX_Y_OFFSET = 10, 10

pygame.display.set_caption("Hangman")


    

SECRET_WORD = "Hello, my name is andy"
# lenOfCharacters = len("".join([i for i in SECRET_WORD if i.isalpha()]))
WORDS = SECRET_WORD.split()

FONT = "Comic Sans MS"
TEXT_SIZE = lineSize * 2
lenOfWord = len([i for i in SECRET_WORD if i.isalpha()])

lives = 6

PositionsOfLetters = {}

def transformHangMan(HANG_MAN_IMAGE):
    return pygame.transform.scale(HANG_MAN_IMAGE, (SCALED_WIDTH, SCALED_HEIGHT))

def transfer():
    return WINDOW, LETTER_SIZE_WIDTH, LETTER_SIZE_HEIGHT, LETTER_BOX_X_OFFSET, LETTER_BOX_Y_OFFSET, FONT, LETTER_BOX, lineSize, PositionsOfLetters, WORDS

SPECIAL_CHARACTERS = [",", ".", "!", "?", ";", "'", '"', "*", "(", ")", ":", "/"]

def draw_window(HANG_MAN, word):
    WINDOW.fill(WHITE)
    draw.draw_letter_box(WINDOW, LETTER_BOX, LETTER_BOX_X_OFFSET, LETTER_BOX_Y_OFFSET)
    WINDOW.blit(HANG_MAN, (100, 0))
    
    prevPositionX, newPositionX = 500, 500 + lineSize

    positionY = 100
    curWord = 1
    prevLetter = None
    for i in word:
        
        if i == " ":
            word = WORDS[curWord]
            curWord += 1
            totalSpaceTaken = len(word) * lineSize + newPositionX
            
            
            if WIDTH - totalSpaceTaken < 100:
                positionY += 50
                prevPositionX, newPositionX = 500, 500 + lineSize
                prevLetter = i
            elif prevLetter == ",":
                pass    
            else:
                prevPositionX, newPositionX = newPositionX + 10, newPositionX + lineSize + 10
            prevLetter = i
            continue

            
        elif i in SPECIAL_CHARACTERS:

            text = pygame.font.SysFont(FONT, TEXT_SIZE)
            text = text.render(i, False, (0,0,0))


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

def searchPositions(letter):
    if not letter:
        return
    global lives, letter_Search, lenOfWord
    found = False
    for i in PositionsOfLetters:
        if PositionsOfLetters[i].lower() == letter:
            letter_Search = letter
            lenOfWord -= 1
            draw.insertLetter(letter, int(lineSize/2), (i[0][0], i[1][0]), i[0][1])
            found = True
    if not found and letter.isalpha():
        print(letter)
        draw.draw_white(WINDOW, SCALED_WIDTH, SCALED_HEIGHT, 100 , 0)
        lives -= 1
        
        HANG_MAN = transformHangMan(lives_to_image[lives])
        WINDOW.blit(HANG_MAN, (100, 0))
        
        draw.insertLetter(letter, letterBox=True, text_size=TEXT_SIZE)
    pygame.display.update()
        
entered_keys = set()

transparency = 10
def drawButton(text):
    global button, widthOfButton, heightOfButton, surf, centerX
    widthOfButton = 300
    heightOfButton = 100
    
    xCorner = (WIDTH/2) - (widthOfButton/2)
    yCorner = (HEIGHT/2) - (heightOfButton/2)


    font = pygame.font.SysFont(FONT, 50, bold=True)
    surf = font.render(text, True, (255,255,255))

    surf = pygame.transform.scale(surf, (widthOfButton-10, heightOfButton-10))
    
    button = pygame.Rect(xCorner, yCorner, widthOfButton, heightOfButton)

    centerX = (widthOfButton/2 - surf.get_width()/2)

    
    pygame.display.update()

def main():
    global transparency
    clock = pygame.time.Clock()
    run = True
    
    HANG_MAN = transformHangMan(HANG_MAN_IMAGE_6)
    draw_window(HANG_MAN, SECRET_WORD)
    
    while run:
        
        global letter_Search
        clock.tick(FPS)
    
        key = None
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            elif event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key)
                if not key.isalpha():
                    key = None
            elif ((not lives) or (not lenOfWord)) and event.type == pygame.MOUSEBUTTONDOWN:
                if button.collidepoint(event.pos):
                    restart()

               
        if (not lives) or (not lenOfWord):
            
            winLose = True if lives else False
            if winLose:
                draw.drawScreen("YouWon.png", transparency)
                drawButton("Continue!")
            else:
                draw.drawScreen("YouLost.png", transparency)
                drawButton("Try Again!")
            
            a, b = pygame.mouse.get_pos()

            if button.x <= a <= button.x + widthOfButton and button.y <= b <= button.x + heightOfButton:
                pygame.draw.rect(WINDOW, (100, 100, 100), button)
            else:
                pygame.draw.rect(WINDOW, (0, 0, 0), button)
            WINDOW.blit(surf, (button.x + centerX, button.y + heightOfButton/8))
            

            
        elif key == "backspace":
            letter_Search = None
            draw.draw_letter_box(WINDOW, LETTER_BOX, LETTER_BOX_X_OFFSET, LETTER_BOX_Y_OFFSET)
            pygame.display.update()
        elif key == "return":
            if letter_Search not in ["return", "backspace", "tab"] and (letter_Search not in entered_keys):
                entered_keys.add(letter_Search)
                searchPositions(letter_Search)
                draw.draw_letter_box(WINDOW, LETTER_BOX, LETTER_BOX_X_OFFSET, LETTER_BOX_Y_OFFSET)
            

            pygame.display.update()
        elif key == "tab" or (not key) or (key in entered_keys):
            pass

        elif key:

            draw.draw_letter_box(WINDOW, LETTER_BOX, LETTER_BOX_X_OFFSET, LETTER_BOX_Y_OFFSET)
            letter_Search = key
            draw.insertLetter(key, letterBox=True, text_size=TEXT_SIZE)
            
    pygame.quit()
def get_word():
    with open("database.json", "r") as database:
        data = json.load(database)
        indexNumber = randint(0, len(data) - 1)

        word = data[str(indexNumber)]
    return word
        


def restart():
    global WINDOW, lives, PositionsOfLetters, WORDS, entered_keys, lenOfWord, SECRET_WORD

    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
        
    SECRET_WORD = get_word()
    lenOfWord = len([i for i in SECRET_WORD if i.isalpha()])
    HANG_MAN = transformHangMan(HANG_MAN_IMAGE_6)
    lives = 6
    WORDS = SECRET_WORD.split()
    entered_keys = set()

    PositionsOfLetters = {}
    draw_window(HANG_MAN, SECRET_WORD)


# Running main function only if the current file name is called main
# cannot run main from another file
if __name__ == "__main__":
    main()
