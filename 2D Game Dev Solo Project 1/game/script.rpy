# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



define d = Character("DM")
define t = Character("Tom")
define s = Character("Stelle")
define z = Character("Zack")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene game table

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    name = renpy.input("What's you're name?")
    define p = Character("[name]")

    d "Alright [name], Which class do you want to play?"
    jump choice1
    
    label choice1
        menu:

        "Rouge":
            jump choice1_rouge

        "Paladin"
            jump choice1_pal

    label choice1_rouge:

        $ menu_flag = True

        d "You have picked the rouge class."

        jump choice1_done

    label choice1_pal:

        $ menu_flag = False

        d "You have picked the paladin class."

        jump choice1_done

    

    label choice1_done:

        # ... the game continues here.
        # These display lines of dialogue.

        p "I've started a new game, made the sheet and we should be good."

        p "I'm finally ready to play!"

        t "Sweet! Let's get started."




    # This ends the game.

    return
