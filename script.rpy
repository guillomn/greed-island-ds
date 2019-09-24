# Goreinu VN

# Declare characters used by this game. The color argument colorizes the
# name of the character.


image black = "#000" #Black Background
image white = "#ffffff" #White Background

define g = Character("Goreinu")
define p = Character("Player")

init python:

    #relationship level
    goreinu_love = 0
    #used to trigger character asking out
    goreinu_ask_out = False
    #used to switch between talks
    goreinu_talk = 0

    #stores last location name
    last_location = ""

    #money
    money = 0

    #stats
    strength = 0
    intelligence = 0
    dexterity = 0
    nen = 0

    #training text logic
    train_str_txt = 0
    train_dex_txt = 0
    train_int_txt = 0
    train_nen_txt = 0

    #inventory items+quantity
    inv = []
    inv_quantity = []
    #loop index
    i = 0
    #final inv list
    #individual names in the array
    item_name = ""
    items = ""

###### The game starts here ######

label start:

    scene black
    $ last_location = "game menu"

menu game_menu:

    "See stats":
        jump stats
    "Map":
        jump location
    "Show Inventory":
        jump inventory
    "Training":
        jump training
    "Bank":
        jump bank
    "Exit Greed Island":
        jump badend

###### Endings ######
label badend:

    ".:. Bad Ending."
    jump gameover

label goodend:

    ".:. Good Ending."
    jump gameover

###### This ends the game ######
label gameover:

    return
