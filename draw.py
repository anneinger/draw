import pygame

pygame.init() # Initialize Pygame
screen = pygame.display.set_mode((640, 480)) # Create a window of 640x480 pixels
screen.fill((255, 255, 255)) # Fill the screen with white


# Draw the ground
pygame.draw.line(screen, (0, 0, 0), (0, 380), (700,380))

# Draw the bottom of the house
pygame.draw.line(screen, ("red"), (120, 375), (515, 375))

# Draw two walls
#wall 1
pygame.draw.line(screen, ("purple"), (120, 375), (120,150))

#wall 2
pygame.draw.line(screen, ("purple"), (515, 375), (515,150))

# Draw the roof
#bunden af taget
pygame.draw.line(screen, ("black"), (120, 150), (515, 150))

#Højre skrå væg
pygame.draw.line(screen, ("black"), (120, 150), (325,50))

#Venstre skrå væg
pygame.draw.line(screen, ("black"), (515, 150), (325,50))

#

# Make sure the window stays open until the user closes it
run_flag = True
while run_flag is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False
    pygame.display.flip() # Refresh the screen so drawing appears