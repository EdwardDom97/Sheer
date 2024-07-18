#Sheer

#had an odd idea, making a battle sim that's primarily text/button based with a build timer.
#after the build time is up there is an instant battle report if the player wins or loses.
#player will be able to pick a base type, summon a variety of ground troops that can gather, fight, 
#scout and do more as more features are developed. difficulty will determine the size and composition of the 
#opposing army. some inital buildings will be walls, melee troop outpost, base building, and more to come 

#Sheer by Tristan Dombroski 07/11/2024 10:53 PM EST.

#importing the libraries
import pygame
import sys
from pygame.locals import *


#initializes the game loop
pygame.init()

#color pallatte RBG values for editing.
#Naple Yellow (252, 240, 167)
#Desert Sand (254, 220, 172)
#Golden Wheat(228, 184, 129)
#Blue (0, 0, 255)




#screen variables
screen_width = 1600
screen_height = 900

#the display itself using the screen variables
screen = pygame.display.set_mode((screen_width, screen_height))

#The caption of the application itself
pygame.display.set_caption('Sheer Version 1.0  Tristan Dombroski') 

#The in-game font variable
game_font = pygame.font.SysFont(None, 54)  # Choose the font type and size

#displaying the title and version on the Main menu screen
menuintro = game_font.render("Sheer Version 1.0", True, (10, 10, 10))
menuintro_rect = menuintro.get_rect(midleft = (50, 125)) #this is not a button it's the 'background' to the text



#here I want to introduce some buttons for the main menu 
play_game_button = pygame.image.load('graphics/buttons/startbutton.png')
play_game_button_rect = play_game_button.get_rect(topleft = (75, 200))

exit_game_button = pygame.image.load('graphics/buttons/exitbutton.png')
exit_game_button_rect = exit_game_button.get_rect(topleft = (75, 275))



#these buttons displayed inside of the game loop
menu_button =  pygame.image.load('graphics/buttons/menubutton.png')
menu_button_rect = menu_button.get_rect(topleft = (450, 100))

start_match_button = pygame.image.load('graphics/buttons/startmatchbutton.png')
start_match_button_rect = start_match_button.get_rect(topleft = (700, 800))


#this text will be displayed in the game loop for the player to pick a base
select_base_text = game_font.render("Select your base:", True, (10, 10, 10))
select_base_text_rect = select_base_text.get_rect(midleft = (50, 225)) #


#the images below are going to be for the base selection via base icons, right now is just human and beast will be next
#selection images
human_base_icon = pygame.image.load('graphics/bases/HumanBase/humanbaseicon.png')
human_base_icon_rect = human_base_icon.get_rect(center = (175, 375))


#this text will be displayed in the game loop for the player to pick a difficulty
select_difficulty_text = game_font.render("Select your difficulty", True, (10, 10, 10))
select_difficulty_text_rect = select_difficulty_text.get_rect(midleft = (50, 525)) 

#these are the difficulty buttons 
easy_difficulty_button = pygame.image.load('graphics/buttons/easydifficultybutton.png')
easy_difficulty_button_rect = easy_difficulty_button.get_rect(center = (150, 625))





# IMPORTANT the following images are going to be used inside of the BATTLE Loop. This could be the most intensive part of the entire code structure so far.

#Human Base Background
battle_background_scene = pygame.image.load('graphics/bases/HumanBase/humanbasebackgroundgui.png')
battle_background_scene_rect = battle_background_scene.get_rect() #unused for now


# Hire Unit button
hire_units_button = pygame.image.load('graphics/buttons/hireunitsbutton.png')
hire_units_button_rect = hire_units_button.get_rect(topleft=(140, screen_height - 300))

# Build structures button
build_structures_button = pygame.image.load('graphics/buttons/buildstructuresbutton.png')
build_structures_button_rect = build_structures_button.get_rect(topleft=(450, screen_height - 300))


# Human Unit Window
human_unit_window = pygame.image.load('graphics/bases/HumanBase/humanunitwindow.png')
human_unit_window_rect = human_unit_window.get_rect(center = (screen_width // 2, screen_height // 2))
display_human_unit_window = False

# Human Units
# Human Farmer costs 5 gold and 5 food, produces 1 gold and 2 food per minute. Adds one to unit count
human_farmer = pygame.image.load('graphics/bases/HumanBase/units/unitfarmer.png')
human_farmer_rect = human_farmer.get_rect(center=(screen_width // 2 , screen_height // 2 - 100))


# Human Lumberjack costs 5 gold, 5 food, and 5 wood, produces 1 gold and 2 wood per minute. Adds one to unit count
human_lumberjack = pygame.image.load('graphics/bases/HumanBase/units/unitlumberjack.png')
human_lumberjack_rect = human_lumberjack.get_rect(center=(screen_width // 2, screen_height // 2))

# Human Warrior costs 10 gold, 5 food and 5 wood, adds + 2 to damage and defense. Adds two to unit count
human_warrior = pygame.image.load('graphics/bases/HumanBase/units/unitwarrior.png')
human_warrior_rect = human_warrior.get_rect(center=(screen_width // 2 , screen_height // 2 + 100))





# Clock setup to regulate frames and keep track of building/summoning
clock = pygame.time.Clock()


#declaring the start up to be set in the MainMenu state. 
game_state = "MainMenu"
game_running = True






#states used in the program
MENU = 'MainMenu'
GAME = 'GAME'
BATTLE = "Battle"

#base variables (this is a test chunk)
HUMANS = "Humans"
BEASTS = "Beasts"

#game state variables
base_selected = 'None'
difficulty_selected = 'None'


# Battle timer variable (8 minutes in milliseconds)
battle_time = 8 * 60 * 1000  # 8 minutes in milliseconds
battle_start_time = None


#main/first game loop
while game_running:

    #time
    current_time = pygame.time.get_ticks()


    # Event handling
    mx, my = pygame.mouse.get_pos()

    click = False



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            click = True


        if event.type == MOUSEBUTTONDOWN and event.button == 3:
            click = False
            display_human_unit_window = False
            

    



    #main menu code block start

    if game_state == "MainMenu":

        #resets the game selection variables
        base_selected = 'None'
        difficulty_selected = 'None'

        
        #play game button logic
        if play_game_button_rect.collidepoint((mx, my)):  
            if click:
                game_state = "GAME"


        #exit game logic
        if exit_game_button_rect.collidepoint((mx, my)):  
            if click:
                pygame.quit()
                sys.exit()




    #main game loop
    if game_state == "GAME":


        #variables to be used in the Game state to set up for the Battle state
        
      


        if menu_button_rect.collidepoint((mx, my)):  
            if click:
                game_state = "MainMenu"


        if human_base_icon_rect.collidepoint((mx, my)) and click:
            base_selected = "Humans"
        

        if easy_difficulty_button_rect.collidepoint((mx, my)) and click:
            difficulty_selected = "Easy"
        

        if start_match_button_rect.collidepoint((mx, my)):  
            if click:
                if base_selected != 'None' and difficulty_selected != 'None':
                    game_state = "BATTLE"
                    battle_start_time = pygame.time.get_ticks()  # Set the battle start time when the battle begins







    if game_state == "BATTLE":

        if menu_button_rect.collidepoint((mx, my)):  
            if click:
                game_state = "MainMenu"


        if hire_units_button_rect.collidepoint((mx, my)):
            if click:
                display_human_unit_window = True

                

            
            
            


         # Calculate remaining battle time
        
        # Calculate remaining battle time
        elapsed_time = pygame.time.get_ticks() - battle_start_time
        remaining_time = max(battle_time - elapsed_time, 0)
        minutes = remaining_time // (60 * 1000)
        seconds = (remaining_time // 1000) % 60
        timer_text = f"{minutes:02}:{seconds:02}"
        timer_surface = game_font.render(timer_text, True, (10, 10, 10))
        timer_rect = timer_surface.get_rect(center=(screen_width // 2, 50))

            





    #END OF LOGIC LOOPS
    #Splitting the states into two separate catagories, Logic above and Rendering below because I cannot figure out how to keep the base_selected rectangle to remain true after click
    #START OF RENDERING LOOPS






    if game_state == "MainMenu":


        screen.fill((228, 184, 129)) #Golden Wheat color
        screen.blit(menuintro, menuintro_rect) #displays the title and version
        
        # Main menu screen buttons
        #play game
        screen.blit(play_game_button, play_game_button_rect)

        #exit game
        screen.blit(exit_game_button, exit_game_button_rect)


    

        pass










    elif game_state == "GAME":


        
        screen.fill((228, 184, 129)) #Golden Wheat color
        screen.blit(menuintro, menuintro_rect) #displays the title and version

        #allows the player to return to the main menu at any time
        screen.blit(menu_button, menu_button_rect)

        

        #prompts the player to pick a base
        screen.blit(select_base_text, select_base_text_rect)

        #displays the human base
        screen.blit(human_base_icon, human_base_icon_rect)




        #prompts the player to pick a difficulty
        screen.blit(select_difficulty_text, select_difficulty_text_rect)

        #easy difficulty button 
        screen.blit(easy_difficulty_button, easy_difficulty_button_rect)
        

        #start match button
        screen.blit(start_match_button, start_match_button_rect)



        #rendering logic?
        if base_selected == "Humans":
            pygame.draw.rect(screen, (255,0,0), human_base_icon_rect, 2)
        
        if difficulty_selected == "Easy":
            pygame.draw.rect(screen, (255,0,0), easy_difficulty_button_rect, 2)


        pass




    elif game_state == "BATTLE":

        #gives the player ample starting resources
        if difficulty_selected == "Easy":
            player_coins = 100
            player_wood = 100
            player_food = 100



         # Resource text and display

        #player_coins_text = f"Coins: {player_coins}"  I would use this one instead of the below if my humanbasebackgroundgui didn't have the words painted onto the .png itself will fix later

        #displays the players coins on the screen
        player_coins_text = f"{player_coins}"
        player_coins_display = game_font.render(player_coins_text, True, (10, 10, 10))
        player_coins_display_rect = player_coins_display.get_rect(topleft=(325, screen_height - 100))


        player_wood_text = f"{player_wood}"
        player_wood_display = game_font.render(player_wood_text, True, (10, 10, 10))
        player_wood_display_rect = player_wood_display.get_rect(topleft=(700, screen_height - 100))

        player_food_text = f"{player_food}"
        player_food_display = game_font.render(player_food_text, True, (10, 10, 10))
        player_food_display_rect = player_food_display.get_rect(topleft=(1200, screen_height - 100))






        screen.fill((228, 184, 129)) #Golden Wheat color

        screen.blit(battle_background_scene, (0, 0))

        screen.blit(menuintro, menuintro_rect) #displays the title and version

        #allows the player to return to the main menu at any time
        screen.blit(menu_button, menu_button_rect)

        # Render resources
        screen.blit(player_coins_display, player_coins_display_rect)
        screen.blit(player_wood_display, player_wood_display_rect)
        screen.blit(player_food_display, player_food_display_rect)

        #renders the hire unit and build structure buttons

        screen.blit(hire_units_button,hire_units_button_rect)
        screen.blit(build_structures_button, build_structures_button_rect)


        #displays a red border around the hire units button while the mouse is over it
        if hire_units_button_rect.collidepoint((mx, my)):
            pygame.draw.rect(screen, (255,0,0), hire_units_button_rect, 2)

        #displays a red border around the build structures button while the mouse is over it
        if build_structures_button_rect.collidepoint((mx, my)):
            pygame.draw.rect(screen, (255,0,0), build_structures_button_rect, 2)


        #toggles the human unit window when the "Hire Units" button is hovered over and clicked.
        if display_human_unit_window:
            screen.blit(human_unit_window, human_unit_window_rect)

            # Blit the human units
            screen.blit(human_farmer, human_farmer_rect)
            screen.blit(human_lumberjack, human_lumberjack_rect)
            screen.blit(human_warrior, human_warrior_rect)






        # Render the timer
        screen.blit(timer_surface, timer_rect)
        pass







    #final rendering of the screen and updating the clock/frames per second   
    pygame.display.update()
    clock.tick(60)

