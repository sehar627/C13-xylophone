import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the display
width, height = 800, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Xylophone")

FPS = 20
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
INDIGO = (75, 0, 130)
VIOLET = (238, 130, 238)

# Define key dimensionskey_width = 100
key_height = 30
key_margin = 10


sound1=pygame.mixer.Sound("note1.mp3")
sound2=pygame.mixer.Sound("note2.mp3")
sound3=pygame.mixer.Sound("note3.mp3")
sound4=pygame.mixer.Sound("noteA.mp3")
sound5=pygame.mixer.Sound("noteB.mp3")
sound6=pygame.mixer.Sound("noteC.mp3")
sound7=pygame.mixer.Sound("noteD.mp3")
sound8=pygame.mixer.Sound("noteE.mp3")


# Define the small rectangle (player-controlled object)
small_rect_width = 40
small_rect_height = 30
small_rect_x = 600
small_rect_y = 300
small_rect_speed = 10

# Main game loop
running = True
while running:
    screen.fill("black")
    # Draw the xylophone keys directly using coordinates in pygame.draw.rect
    key1=pygame.draw.rect(screen, RED, (0, 100, 70, 250))
    key2=pygame.draw.rect(screen, ORANGE, (80, 100, 70, 220))
    key3=pygame.draw.rect(screen, YELLOW, (160,100,70,200))
    key4=pygame.draw.rect(screen, GREEN, (240,100,70,180))
    key5=pygame.draw.rect(screen, BLUE, (320,100,70,160))
    key6=pygame.draw.rect(screen, INDIGO, (400,100,70,140))
    key7=pygame.draw.rect(screen, VIOLET, (480,100,70,120))
    key8=pygame.draw.rect(screen, RED, (560,100,70,100))

    # Draw the small rectangle (player-controlled)
    small_rect=pygame.draw.rect(screen, WHITE, (small_rect_x, small_rect_y, 40, 40))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle movement of the small rectangle using arrow keys
    
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                 small_rect_x -= 20
            if event.key == pygame.K_RIGHT:
                 small_rect_x += 20
            if event.key == pygame.K_UP:
                 small_rect_y -= 20
            if event.key == pygame.K_DOWN:
                 small_rect_y += 20
          
    # Check for collisions with xylophone keys and play the sound
   
    if small_rect.colliderect(key1): 
           sound1.play()

    if small_rect.colliderect(key2):
           sound2.play()

    if small_rect.colliderect(key3):
           sound3.play()

    if small_rect.colliderect(key4):
           sound4.play()
    if small_rect.colliderect(key5):
           sound5.play()
    if small_rect.colliderect(key6):
           sound6.play()

    if small_rect.colliderect(key7):
           sound7.play()
    if small_rect.colliderect(key8):
           sound8.play()
           




    pygame.display.flip()
    clock.tick(FPS)

# Clean up
pygame.quit()
sys.exit()
