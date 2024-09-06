import pygame

pygame.init() # Initialize Pygame
screen = pygame.display.set_mode((640, 480)) # Create a window of 640x480 pixels
screen.fill((255, 255, 255)) # Fill the screen with white


# Draw the ground
pygame.draw.line(screen, (0, 0, 0), (0, 380), (700,380))

# Draw the house
pygame.draw.rect(screen, ("red"), ((120, 180), (200, 200)))

# Draw the roof
pygame.draw.polygon(screen, ("black"), ((120, 180), (220, 80), (320, 179)))

#draw a sun
pygame.draw.circle(screen, ("yellow"), (500,100), 40)
                    

# Make sure the window stays open until the user closes it
run_flag = True
while run_flag is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False
    pygame.display.flip() # Refresh the screen so drawing appears