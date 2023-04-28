import pygame

"""
Step 1: Create a screen
"""
panel_size = 150
screen_width = 800
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

# make the panel show on the screen
screen.blit(panel_image, (0, screen_height - panel_size))


"""
Step 4: Create a Character
"""

# create a dictionary (because it can have different data types) for our character
hero = {
    "name": "Fighter",  # name of the character
    "max_hp": 250,  # max health of the character
    # current health of the character that gets decreased as it goes into battle
    "current_hp": 250,
    "attack_dmg": 30,  # the attack our character can do
    "potions": 3,  # healing ability our character has
    "alive": True  # whether or not game is over
}

"""
Step 5: Show the character on the screen
"""
# import the image of the hero
hero_image = pygame.image.load('assets/Knight/Idle/0.png')

"""
Step 6: Make the character bigger and put it in correct position
"""
# used pygame.transform to scale up (make bigger) the image of character
# then save the image in the "model" property of hero
hero["model"] = pygame.transform.scale(
    hero_image, (hero_image.get_width() * 3, hero_image.get_height() * 3))

# show the character on the screen
screen.blit(hero["model"], (70, 177))

"""
Step 7: Create the enemy characters
"""
bandit_1 = {
    "name": "Bandit 1",  # name of the character
    "max_hp": 150,  # max health of the character
    # current health of the character that gets decreased as it goes into battle
    "current_hp": 150,
    "attack_dmg": 15,  # the attack our character can do
    "potions": 1,  # healing ability our character has
    "alive": True  # whether or not game is over
}

bandit_2 = {
    "name": "Bandit 2",  # name of the character
    "max_hp": 150,  # max health of the character
    # current health of the character that gets decreased as it goes into battle
    "current_hp": 150,
    "attack_dmg": 15,  # the attack our character can do
    "potions": 1,  # healing ability our character has
    "alive": True  # whether or not game is over
}


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
