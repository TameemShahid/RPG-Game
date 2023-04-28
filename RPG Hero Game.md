# RPG Hero Game

## Step 1: Create a screen

1. Screen is just a rectangle, and since screen is a rectangle it needs to have some:
   1. Width
   2. Height
   3. Create a variables for screen width and height

````python
screen_width = 800
screen_height = 400
````

2. Give our screen (our soon to be game) a title 

```python
pygame.display.set_caption("RPG Hero")
```

3. Make the screen appear

```python
pygame.display.set_mode((screen_width, screen_height))
```

## Step 2: Create a background

1. Import background image.

   ```python
   background_image = pygame.image.load('assets/background.png').convert_alpha()
   ```

2. Place the background image on the empty screen we have

   ```python
   screen.blit(background_image, (0, 0))
   ```

## Step 3: Create a Panel to show health and other options

1. Modify the lines where we created the variables for screen height and screen width to the make size for panel as well.

   ```python
   panel_size = 150
   screen_width = 800
   screen_height = (400 + panel_size)
   ```

   We created another variable for the panel size and then added the panel size to our previous screen size

2. Import the panel image and save it in a variable

   ````python
   panel_image = pygame.image.load('assets/panel.png').convert_alpha()
   ````

3. Place the image on our screen

   ```python
   screen.blit(panel_image, (0, screen_height - panel_size))
   ```

## Step 4: Create a Hero Character

Before jumping ahead and just starting coding away, take a second and think what do we need. What does characters usually have in games. Take an example of Pokémon in a battle:

* Pokémon has a name.
* Pokémon has some position on the screen, meaning it has *x & y* co-ordinates.
* Pokémon has some health.
* Pokémon has some attack through which it does damage to enemy.
* Pokémon can use potions to heal.
* Lastly the state of the Pokémon whether it is alive or not 

1. Create a dictionary for our hero

   ```python
   hero = {
       "name": "Fighter",
       "max_hp": 300,
       "current_hp": 300,
       "attack_dmg": 10,
       "potions": 3,
       "alive": True
   }
   ```

2. Import the model of the hero

   ```python
   hero_image = pygame.image.load('assets/0.png')
   ```

3. Show the hero on the screen

   ```python
   screen.blit(hero_image, (0, 0))
   ```

## Step 5: Make Adjustments to Hero

1. Make model bigger.

   ```python
   hero_model = pygame.transform.scale(hero_image, (hero_image.get_width() * 3, hero_image.get_height() * 3))
   ```

2. Make the hero appear on the screen

   ```python
   screen.blit(hero_model, (50, 177))
   ```

## Step 6: Create the Enemies

1. Create the enemies using dictionary object

   ```python
   bandit_1 = {
       "name": "Bandit 1",
       "max_hp": 150,
       "current_hp": 150,
       "attack_dmg": 50,
       "potions": 1,
       "alive": True
   }
   
   bandit_2 = {
       "name": "Bandit 2",
       "max_hp": 150,
       "current_hp": 150,
       "attack_dmg": 50,
       "potions": 1,
       "alive": True
   }
   ```

## Step 7: Make adjustments to Characters

1. Import bandit images

   ```python
   bandit_image = pygame.image.load('assets/Bandit/Idle/0.png')
   ```

2. Make bandits bigger

   ```python
   bandit_1["model"] = pygame.transform.scale(
       bandit_image, (bandit_image.get_width() * 3, bandit_image.get_height() * 3))
   
   bandit_2["model"] = pygame.transform.scale(
       bandit_image, (bandit_image.get_width() * 3, bandit_image.get_height() * 3))
   ```

3. Make the bandits appear on the screen

   ```python
   screen.blit(bandit_1["model"], (480, 197))
   screen.blit(bandit_2["model"], (610, 197))
   ```

   