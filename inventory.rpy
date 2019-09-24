screen items:
    fixed:
         xpos 400
         ypos 300
         textbutton "Add and Show" action Jump("compute")

label inventory:
     show screen items

     menu:
         "Return":
             hide screen items
             jump game_menu

label compute:

     hide screen items
     $ inv.append("fishing rod")
     $ inv.append("yoyo")
     $ inv.append("kurta eyes")
     python:
         showitems = True

         def display_items_overlay():
             if showitems:
                 inventory_show = "Inventory: "
                 for i in range(0, len(inv)):
                     item_name = inv[i].title()
                     if i > 0:
                         inventory_show += ", "
                     inventory_show += item_name
                 ui.frame()
                 ui.text(inventory_show)
         config.overlay_functions.append(display_items_overlay)

     "Inventory"
     $ showitems = False
     jump game_menu
