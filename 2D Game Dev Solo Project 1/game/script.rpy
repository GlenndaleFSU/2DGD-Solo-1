# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



define d = Character("Daniel")
define t = Character("Tom")
define s = Character("Stelle")
define z = Character("Zack")


# The game starts here.

label start:

    # Place where the DM and the game take the name of your player.
    scene game table-adjusted
    with Dissolve(.5)
    
    "You arrive at the table, greet your DM and friend Tom, and wave to the others as you head over to your seat."

    d "{cps=25}Ok guys, I'm Daniel, and I'm gonna be your DM for the night. {p}Before we start, let's once again go over who we all are and what class we picked before we start."

    label namePlayer:
        $ name = renpy.input("What's your name?")
        $ name = name.strip() 
        define p = Character("[name]")

        p "{cps=25}Hi! I'm [name]. I went to session zero."
        t "{cps=25}Welcome back, buddy."
        s "{cps=25}Hey."
        z "{cps=25}Hello, {b} hello! {/b}"
        d "{cps=25}Alright [name], Which class were you playing again?"
        jump choice1
    
    # The DM asks you for your class.

    label choice1:
        menu:

            "Rouge":
                jump choice1_rouge

            "Paladin":
                jump choice1_pal

        label choice1_rouge:

            $ player_class = 1

            p "{cps=25}I went with Swashbuckler Rogue."
            d "{cps=25}You have picked the Rouge class. Nice choice!"

            jump choice1_done

        label choice1_pal:

            $ player_class = 2

            p "{cps=25}Wanted to try Paladin. Going with Devotion."
            d "{cps=25}You have picked the Paladin class. Nice choice!"

            jump choice1_done

    

    label choice1_done:

        # ... the game continues here.
        # These display lines of dialogue.

        t "{cps=25}I'm Tom, and I've chosen to try out a Mercy Monk."
        s "{cps=25}I'm Stelle, and I chose a Multiclass Pyro Sorcerer/Evocation Wizard."
        z "{cps=25}{b}Hello everbody!{/b} My name is Zack and I've chosen a Eloquence Bard/Rouge multiclass."
        d "{cps=25}That's everyone! {b}Sweet{/b}!"
        p "{cps=25}I'm finally ready to play!"
        t "{cps=25}Sweet! Let's get started."
        "Yeah! {space=20} Woo!"

        jump dungeon_begin

    label dungeon_begin:
        d "So, we begin our campaign in a carriage, treking through the woods. /nThe cart's wheels creak as they turn over the bumps."
        d "Soon, one of you begins to speak up."




    # This ends the game.

    return
