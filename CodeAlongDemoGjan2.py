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

"""
Step 5: Make adjustments to our hero
"""
# make knight 3 times bigger
knight_model = pygame.transform.scale(
    knight_image, (knight_image.get_width() * 3, knight_image.get_height() * 3))

# show the image on the screen
screen.blit(knight_model, (50, 177))


"""
Step 6: Create the enemies
"""
bandit_1 = {
    "name": "Bandit 1",
    "max_hp": 150,
    "current_hp": 150,
    "attack_dmg": 50,
    "potions": 1,
    "alive": True,
}

bandit_2 = {
    "name": "Bandit 2",
    "max_hp": 150,
    "current_hp": 150,
    "attack_dmg": 50,
    "potions": 1,
    "alive": True
}

"""
Step 7: Make adjustments to bandit model and make it appear on screen
"""
# import the bandit image
bandit_image = pygame.image.load('assets/Bandit/Idle/0.png')
bandit_image = pygame.transform.scale(
    bandit_image, (bandit_image.get_width() * 3, bandit_image.get_height() * 3))

# make the bandit appear on screen
bandit_1["model"] = bandit_image
bandit_2["model"] = bandit_image

screen.blit(bandit_1["model"], (480, 197))
screen.blit(bandit_2["model"], (610, 197))

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
