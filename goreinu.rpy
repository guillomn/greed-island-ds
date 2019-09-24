###### Goreinu Conversation Choices ######

#conversation choices
label goreinu:

    ##scene bg shiso
    show goreinu shy

    if goreinu_love >= 10 and goreinu_ask_out == True:
        jump goreinu_ask
    else:
        menu:
            "Talk to Goreinu":
                jump goreinu_talk_logic
            "Do you like me?":
                jump goreinu_level
            "Back off":
                jump expression last_location
            "Back to Game menu":
                jump game_menu


#talk prompted by goreinu when enough love level
#goreinu_ask_out must be set to "True" in one of the "talk" conversations to activate this conversation
#also goreinu_ask_out must be set to "False" so he doesn't loop on asking out
label goreinu_ask:

    $ goreinu_ask_out = False
    g "H-h-hi.."
    g "Might you have s-some time?"
    show goreinu shy2
    g "I-I mean, I totally understand if you don't!"
    menu:
        "Yeah, of course I do!":
            $ goreinu_love += 5
            jump positive
        "Nah, sorry.":
            $ goreinu_love -= 5
            jump negative

#logic to change between conversations
#must add +1 to goreinu_talk in each label for this to work
label goreinu_talk_logic:

    if goreinu_talk <= 0:
        jump goreinu_talk_1
    elif goreinu_talk == 1:
        jump goreinu_talk_2
    else:
        jump goreinu_talk_end

#conversations
label goreinu_talk_1:

    show goreinu shy
    p "What do you want to do after you've completed the game?"
    g "If I get the reward prize Mr. Battera is rewarding, first thing I'm going to do is to get myself a nice mansion."
    g "I've wanted a place I can call home for a while, and after spending all this time here in this game I want to spoil myself a little."
    g "After that, I don't know. Maybe I'll find myself some work through the association."
    $ goreinu_talk += 1
    $ goreinu_love += 5
    jump goreinu

label goreinu_talk_2:

    show goreinu shy
    p "What do you think of Greed Island then?"
    g "It's quite the game. Whoever made it must be extremely good with Nen. There are so many variations of it in use here."
    g "And the potency of the cards is quite something. They must have some pretty strong vows and restrictions going on here to achieve that level of fidelity."
    g "Also whoever made the game must be some kind of sadist. The requirements to beat the game are quite difficult to achieve, and then if there are multiple people trying to beat the game, it's bound to cause some sort of fighting and killing between players."
    g "Although I think that can be attributed to the players themselves being killers."
    $ goreinu_talk += 1
    $ goreinu_love += 5
    $ goreinu_ask_out = True
    $ intelligence += 5
    "Your intelligence increased by 5!"
    jump goreinu

label goreinu_talk_end:

    show goreinu shy
    g "Sorry, I got things to do"
    jump goreinu

#check level
label goreinu_level:

    if goreinu_love < 0:
        show goreinu shy2
        g "I hate you. You asshole."
    elif goreinu_love <= 5:
        show goreinu shy
        g "You're allright, I guess."
    elif goreinu_love >= 10:
        show goreinu shy3
        g "Ofcourse I do, you idiot."

    g "Level is [goreinu_love]"
    jump goreinu

###### Positive choice ######
label positive:

    show goreinu shy
    g "It's just that I've b-been enjoying these past moments we've had togheter, I think it'd be a shame if we ended things here.."
    jump goreinu

label negative:

###### Negative choice ######
    show goreinu shy3
    g "Ah.. s-sorry to bother you then.."
    jump goreinu
