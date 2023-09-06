import pygame
import time
from datetime import datetime
import sys

# Set up the display
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()

# Get the screen height
h = screen.get_height();

# Set up the font
font = pygame.font.Font('./dejavu-sans-mono.book.ttf', int(200*h/768))

# Set up the colors
black = (0, 0, 0)
white = (255, 255, 255)

# Run the clock display
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(black)

    # Get the current time
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    # Render the time
    text = font.render(current_time, True, white)
    text_rect = text.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
    screen.blit(text, text_rect)

    # Update the display
    pygame.display.update()
    clock.tick(1)
