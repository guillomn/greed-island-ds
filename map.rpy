screen map:
    textbutton "Masadora" at truecenter action Jump("masadora")

    fixed:
        xpos 700
        ypos 200
        textbutton "Soufrabi" action Jump("soufrabi")

    fixed:
        xpos 200
        ypos 200
        textbutton "Shiso Tree" action Jump("shiso")

    fixed:
        xpos 700
        ypos 500
        textbutton "Aiai" action Jump("aiai")

label location:

    scene bg map
    show screen map
    menu:
        "Return":
            if last_location == "masadora":
                scene bg masadora
            elif last_location == "soufrabi":
                scene bg soufrabi
            elif last_location == "shiso":
                scene bg shiso
            elif last_location == "aiai":
                scene bg aiai
            elif last_location == "aiai_2":
                scene bg aiai 2

            hide screen map
            jump game_menu


label masadora:

    hide screen map
    $ last_location = "masadora"
    scene bg masadora
    menu:
        "Return":
            jump game_menu

label soufrabi:

    hide screen map
    $ last_location = "soufrabi"
    scene bg soufrabi
    menu:
        "Return":
            jump game_menu

label shiso:

    hide screen map
    $ last_location = "shiso"
    scene bg shiso
    menu:
        "Return":
            jump game_menu

label aiai:

    hide screen map
    $ last_location = "aiai"
    scene bg aiai
    menu:
        "Enter city":
            jump aiai_2
        "Return":
            jump game_menu

label aiai_2:

    $ last_location = "aiai_2"
    scene bg aiai 2
    menu:
        "Talk to Goreinu":
            jump goreinu
        "Go back":
            jump aiai
        "Return":
            jump game_menu

label antokiba:

label dorias:

label rubicuta:

label limeiro:

label badlands:

label banditville:

label bunzen:
