import pygame

"""
Step 1: Create a screen
"""
screen_width = 800
screen_height = 400

# initialize/setup our game
pygame.init()

# Give our game
pygame.display.set_caption("RPG Hero Game")

# Show our screen
screen = pygame.display.set_mode((screen_width, screen_height))

"""
Step 2: Create a background in the game
"""

# import the background image
background_image = pygame.image.load('assets/background.png')

# now show the image on the screen
screen.blit(background_image, (0, 0))

"""
Step 3: Create Information Panel
"""

"""
Last Step: To keep the game running and keep it updating
"""
# To basically keep our game (screen) on display and not close after opening
keep_game_running = True
while keep_game_running:

    # whenever user presses a button or do something get all of those events/interactions
    for event in pygame.event.get():
        # if any of the user input/interaction is equal to quitting the game/screen make keep running False
        if event.type == pygame.QUIT:
            keep_game_running = False

    # keep updating the screen
    pygame.display.update()

# quit the game/screen
pygame.quit()
