#stats

#displays stats with a return button
screen stats():
    frame:
        xalign 0.5 ypos 50
        vbox:
            text "Strength [strength]"
            text "Dexterity [dexterity]"
            text "Intelligence [intelligence]"
            text "Nen [nen]"
            textbutton "Return":
                action Return(True)

#calls the stats screen
label stats:
        call screen stats
        with dissolve
        hide screen stats
        jump game_menu
