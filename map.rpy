### Positions
### 0,-350      top left corner
### 1280,-350   top right corner
### 0,0         center left
### 0,350       bottom left corner
### 640,0       center

## Places
## Masadora, Soufrabi, Shiso Tree, Aiai, Limeiro, Antokiba, Dorias, Rubicuta, Badlands, Bandit Village


screen map:

    fixed:
        pos 1100,320
        textbutton "Return" action Jump("location_logic")

    fixed:
        pos 545,-125
        textbutton "Masadora" action Jump("masadora") style "map" text_style "map_button_text"

    fixed:
        pos 345,-140
        textbutton "Soufrabi" action Jump("soufrabi") style "map" text_style "map_button_text"

    fixed:
        pos 610,130
        textbutton "Shiso Tree" action Jump("shiso") style "map" text_style "map_button_text"

    fixed:
        pos 775,230
        textbutton "Aiai" action Jump("aiai") style "map" text_style "map_button_text"

    fixed:
        pos 750,-160
        textbutton "Limeiro" action Jump("limeiro") style "map" text_style "map_button_text"

    fixed:
        pos 620,105
        textbutton "Antokiba" action Jump("antokiba") style "map" text_style "map_button_text"

    fixed:
        pos 500,215
        textbutton "Dorias" action Jump("dorias") style "map" text_style "map_button_text"

    fixed:
        pos 475,135
        textbutton "Rubicuta" action Jump("rubicuta") style "map" text_style "map_button_text"

    fixed:
        pos 640,50
        textbutton "Badlands" action Jump("badlands") style "map" text_style "map_button_text"

    fixed:
        pos 450,85
        textbutton "Bandit Village" action Jump("bvillage") style "map" text_style "map_button_text"


label location:

    scene bg map
    call screen map

label location_logic:

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
            elif last_location == "limeiro":
                scene bg soufrabi
            elif last_location == "antokiba":
                scene bg soufrabi
            elif last_location == "dorias":
                scene bg soufrabi
            elif last_location == "rubicuta":
                scene bg soufrabi
            elif last_location == "badlands":
                scene bg soufrabi
            elif last_location == "bvillage":
                scene bg soufrabi

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

        hide screen map
        $ last_location = "antokiba"
        scene bg antokiba
        menu:
            "Return":
                jump game_menu

label dorias:

    hide screen map
    $ last_location = "dorias"
    scene bg dorias
    menu:
        "Return":
            jump game_menu

label rubicuta:

    hide screen map
    $ last_location = "rubicuta"
    scene bg soufrabi
    menu:
        "Return":
            jump game_menu

label limeiro:

    hide screen map
    $ last_location = "limeiro"
    scene bg limeiro
    menu:
        "Return":
            jump game_menu

label badlands:

    hide screen map
    $ last_location = "badlands"
    scene bg badlands
    menu:
        "Return":
            jump game_menu

label bvillage:

    hide screen map
    $ last_location = "bvillage"
    scene bg bvillage
    menu:
        "Return":
            jump game_menu
