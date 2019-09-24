label bank:
    menu:
        "Add Money":
            jump add_money
        "Return":
            jump game_menu

label add_money:
    $ money += 100
    "You currently have [money] jenny."
    jump game_menu
