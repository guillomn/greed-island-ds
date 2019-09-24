#training

#training intro and menu
label training:

    "What do you want to train?"

    menu:
        "Strength":
            jump training_text_str
        "Dexterity":
            jump training_text_dex
        "Intelligence":
            jump training_text_int
        "Nen":
            jump training_text_nen

# strength training logic
label training_text_str:

    $ strength += 1

    if train_str_txt == 0:
        $ train_str_txt += 1
        "You pumped steel with your biceps, and they are now on fire!"
    elif train_str_txt == 1:
        $ train_str_txt += 1
        "Your abs feel as if they are going to explode!"
    elif train_str_txt == 2:
        $ train_str_txt = 0
        "All of that squatting payed off! You feel strong in the legs."

    "You gained 1 strength! You have now [strength] strength."
    jump game_menu

# dexterity training logic
label training_text_dex:

    $ dexterity += 1

    if train_dex_txt == 0:
        $ train_dex_txt += 1
        "You balanced on a rope for 5 hours."
    elif train_dex_txt == 1:
        $ train_dex_txt += 1
        "You walked 10 km handstanding."
    elif train_dex_txt == 2:
        $ train_dex_txt = 0
        "You slept the night while standing on one leg."

    "You gained 1 dexterity! You have now [dexterity] dexterity."
    jump game_menu

# intelligence training logic
label training_text_int:

    $ intelligence += 1

    if train_int_txt == 0:
        $ train_int_txt += 1
        "You read a book about insects, boosting your knowledge!"
    elif train_int_txt == 1:
        $ train_int_txt += 1
        "You meditated for 5 hours. You boosted your self-awareness and outside-the-box thinking."
    elif train_int_txt == 2:
        $ train_int_txt = 0
        "You ran multiple combat simulations in your head, and came up with new strategies!"

    "You gained 1 intelligence! You have now [intelligence] intelligence."
    jump game_menu

# nen training logic
label training_text_nen:

    $ nen += 1

    if train_nen_txt == 0:
        $ train_nen_txt += 1
        "You practiced your Ren endurance. You feel quite exhausted!"
    elif train_nen_txt == 1:
        $ train_nen_txt += 1
        "You practiced your hatsu to make it more natural and efficient."
    elif train_nen_txt == 2:
        $ train_nen_txt = 0
        "You practiced other nen categories to boost your overall know-how."

    "You gained 1 nen! You have now [nen] Nen."
    jump game_menu
