# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



define d = Character("Daniel", kind=nvl)
define t = Character("Tom", kind=nvl)
define s = Character("Stelle", kind=nvl)
define z = Character("Zack", kind=nvl)
define e = Character("Everyone", kind=nvl)

# The game starts here.

label start:
    # Introduction
    "You are a new college student getting by in college. {p}Your grades are decent, your attendance is perfect, and you've made a few friends."
    "But college life is starting to grate on you, what with the sleepless nights, and declining mental health."
    "Noticing that your health is starting to decline, \nyour friend Tom offers to invite you to a Tabletop RPG group that's beginning a new oneshot for President's Day break."
    "Feeling desperate for someting to break up the monotony, \nyou accept, going to their session zero to learn about the plot for the next semester, and drafting up a character sheet."
    "Finished, you head over to see what it's about."

    # Place where the DM and the game take the name of your player.
    scene game table-adjusted
    with Dissolve(.5)
    
    "You arrive at the table, greet your DM and friend Tom, and wave over to your seat."

    d "{cps=25}Ok guys, I'm Daniel, and I'm gonna be your DM for the night. {p}Before we start, let's once again go over who we all are and what class we picked before we start."

    label namePlayer:
        $ name = renpy.input("What's your name?")
        $ name = name.strip() 
        define p = Character("[name]", kind=nvl)

        p "{cps=25}Hi! I'm [name]. I went to session zero."
        t "{cps=25}Welcome back, buddy."
        s "{cps=25}Hey."
        z "{cps=25}Hello, {b} hello! {/b}"
        d "{cps=25}Alright [name], Which class were you playing again?"

        nvl clear
        jump choice1
    
    # The DM asks you for your class.

    label choice1:
        menu:

            "Rouge":
                jump choice1_rouge

            "Paladin":
                jump choice1_pal

        label choice1_rouge:

            $ player_class = True
            nvl show dissolve 
            p "{cps=25}I went with Swashbuckler Rogue."
            d "{cps=25}You have picked the Rouge class. Nice choice!"

            jump choice1_done

        label choice1_pal:

            $ player_class = False
            nvl show dissolve 
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
        e "Yeah! {space=20} Woo!"
        nvl clear

        jump dungeon_begin

    label dungeon_begin:
        nvl show dissolve 
        d "You all begin outside this dungeon, a newly formed adventuring party of strangers, \nhired by the local baron to uncover the dark sounds coming from this very cave."
        d "As you all step out of the cart and set up camp, \nyou all light a campfire and take a seat. Introduce yourselves."

        "Your friend to the left raises his hand."
        d "The first person steps up and removes the mask they're wearing. \nThey reveal themselves to be a young Aaracokra monk with a dark color."
        t "Good day to you all. My name is Voran Minh. I come from lands to the east of here, and I practice the Merciful Way."
        e "Hello.   Ho There!   Hi."

        "The person far away from you raises their hand."
        d "Suddenly, from another part of the campfire coughs, and stands up. \nThey remove their hood and reveal a crimson-colored tiefling, covered in scars and burns."
        s "The name's Zaraana. I study evocation wizardry and I'm born from a fire demon."
        e "Good day!    Hello there.    Hey."

        "The person to the right of you raises his hand, and begins air-strumming a little tune that he hums."

        z "Ah, I do believe it is time to introduce myself."
        play music "lute_sound.mp3" fadeout 1
        "Music provided by f-r-a-g-i-l-e on Freesound."
        z "{b}Why hello there lovelies!{/b} I am Harry Havartia, a dashing rouge and world-class performer!"

        jump choice2

        label choice2:
            p "{i}Okay, how am I going to introduce myself..."
            nvl hide dissolve 

            if player_class:
                menu:
                    "I'mma go for a casual vibe.":
                        p "{i}Yeah, this should fit the character.{/i}"
                        jump choice2_casual
                    "How about a more cocky approach.":
                        p "{i}Yeah, this should fit the character.{/i}"
                        jump choice2_cocky

                label choice2_casual:
                    nvl show dissolve 
                    p "Hey. I'm Gillien. I can steal pretty well."
                    e "Sup.     Hey.    Welcome!"
                    nvl hide dissolve
                    jump dungeon

                label choice2_cocky:
                    nvl show dissolve 
                    p "The name's Gillien Hundbrand. Best pirate in all the seas, and the lands."
                    e "Yo~!     Hey.    Heh..."
                    nvl hide dissolve
                    jump dungeon
                    

            else:
                menu:
                    "How about a more calm demeanor?":
                        p "{i}Yeah, this should fit the character.{/i}"
                        jump choice2_calm
                    "He sounds more like the bold type.":
                        p "{i}Yeah, this should fit the character.{/i}"
                        jump choice2_bold

                label choice2_calm:
                    nvl show dissolve 
                    p "Hello everyone. My name is Gillien Hundbrand. A travelling Paladin of the Threefold God."
                    e "Hello!      Hey.    Wassup?"
                    nvl hide dissolve
                    jump dungeon


                label choice2_bold:
                    nvl show dissolve 
                    p "Oho! I am Gillien Hundbrand, and I will be your shield!"
                    e "Alright!     Yeah!     Woo!"
                    nvl hide dissolve
                    jump dungeon

    label dungeon:
        d "With that, everyone has introduced themselves. \nAnother NPC goes in to read out their mission."
        d "*So here's your mission for today. \nThere is an artifact animating a golem within the nearby dungeon.*"
        d "*It's causing the nearby monsters to evacuate into town. \nYour mission is to go in and destroy it.*"
        d "With your briefing finished, you all pack your equipment and begin to enter the dungeon."
        d "*Good luck.*"
        
        "This session went the way a lot of one-shot dungeons oft went." 
        d "The dungeon springs a trap! Make a dex save! DC 12"
        z "Sweet! I got a 15"
        s "23"
        t "23!!! *dice rolls* Damn. Nat 1."
        e "Ooooooooooough."
        if player_class:
            p "HaHAAAA! A 19!"
            d "Nice roll, new guy!"
        else:
            p "My AC is 20."
            d "Wow."
        d "Voran takes a hit from the arrow trap, and now has poison."
        d "Voran takes...54"
        t "Ahh! I am struck! The cobran arrows have taken my--"
        if player_class:
            p "The chest I found had antitoxins."
        else:
            p "I cast Lesser Restoration."
        t "Thank you my friend."
        



        



            

        



        


    # This ends the game.

    return
