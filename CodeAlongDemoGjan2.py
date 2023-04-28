import pygame

"""
Step 1: Create a screen
"""
panel_size = 150
screen_width = 800
# increase our current screen height by the height of the panel
screen_height = (400 + panel_size)

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

# import the panel image
panel_image = pygame.image.load('assets/panel.png')

# show the panel on the screen
screen.blit(panel_image, (0, screen_height - panel_size))

"""
Step 4: Create a character
"""

# create our hero using a dictionary
hero = {
    "name": "Fighter",
    "max_hp": 200,
    "current_hp": 200,
    "attack_dmg": 20,
    "potions": 3,
    "alive": True
}

# import the hero image
knight_image = pygame.image.load('assets/Knight/Idle/0.png')

# show the image on the screen
screen.blit(knight_image, (0, 0))

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
