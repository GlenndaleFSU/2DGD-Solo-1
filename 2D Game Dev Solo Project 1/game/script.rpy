# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



define d = Character("Daniel")
define t = Character("Tom")
define s = Character("Stelle")
define z = Character("Zack")
define e = Character("Everyone")

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
    show dm_neutral:
        xalign 0.5
        yalign 0.2

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

            $ player_class = True
             
            p "{cps=25}I went with Swashbuckler Rogue."
            d "{cps=25}You have picked the Rouge class. Nice choice!"

            jump choice1_done

        label choice1_pal:

            $ player_class = False
             
            p "{cps=25}Wanted to try Paladin. Going with Devotion."
            d "{cps=25}You have picked the Paladin class. Nice choice!"

            jump choice1_done

    

    label choice1_done:

        # ... the game continues here.
        # These display lines of dialogue.

        t "{cps=25}I'm Tom, and I've chosen to try out a Mercy Monk."
        show tom_neutral:
            xalign 0.25
            yalign 0.6

        s "{cps=25}I'm Stelle, and I chose a Multiclass Pyro Sorcerer/Evocation Wizard."
        show stelle_neutral:
            xalign 0.75
            yalign 0.3
        z "{cps=25}{b}Hello everbody!{/b} My name is Zack and I've chosen a Eloquence Bard/Rouge multiclass."
        show zack_neutral:
            xalign 0.75
            yalign 0.6
        d "{cps=25}That's everyone! {b}Sweet{/b}!"
        p "{cps=25}I'm finally ready to play!"
        t "{cps=25}Sweet! Let's get started."
        e "Yeah! {space=20} Woo!"

        jump dungeon_begin

    label dungeon_begin:

        # This is the first third.

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
        show zack_neutral:
            xalign 0.75
            yalign 0.6
        hide zack_neutral
        z "Ah, I do believe it is time to introduce myself."
        show zack_singing:
            xalign 0.75
            yalign 0.6
        play music "lute_sound.mp3" fadeout 1
        "Music provided by f-r-a-g-i-l-e on Freesound."
        hide zack_singing
        show zack_neutral:
            xalign 0.75
            yalign 0.6
        z "{b}Why hello there lovelies!{/b} I am Harry Havartia, a dashing rouge and world-class performer!"

        jump choice2

        label choice2:
            p "{i}Okay, how am I going to introduce myself..."

            if player_class:
                menu:
                    "I'mma go for a casual vibe.":
                        p "{i}Yeah, this should fit the character.{/i}"
                        jump choice2_casual
                    "How about a more cocky approach.":
                        p "{i}Yeah, this should fit the character.{/i}"
                        jump choice2_cocky

                label choice2_casual:
                    p "Hey. I'm Gillien. I can steal pretty well."
                    e "Sup.     Hey.    Welcome!"
                    jump dungeon

                label choice2_cocky:
                    p "The name's Gillien Hundbrand. Best pirate in all the seas, and the lands."
                    e "Yo~!     Hey.    Heh..."
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
                    
                    p "Hello everyone. My name is Gillien Hundbrand. A travelling Paladin of the Threefold God."
                    e "Hello!      Hey.    Wassup?"
                    
                    jump dungeon


                label choice2_bold:
                    p "Oho! I am Gillien Hundbrand, and I will be your shield!"
                    e "Alright!     Yeah!     Woo!"
                    jump dungeon

    label dungeon:

        # This is the second third.

        d "With that, everyone has introduced themselves. \nAnother NPC goes in to read out their mission."
        d "*So here's your mission for today. \nThere is an artifact animating a golem within the nearby dungeon.*"
        d "*It's causing the nearby monsters to evacuate into town. \nYour mission is to go in and destroy it.*"
        d "With your briefing finished, you all pack your equipment and begin to enter the dungeon."
        d "*Good luck.*"
        
        "This session went the way a lot of one-shot dungeons oft went. From wild rolls and poor luck..." 
        d "The dungeon springs a trap! Make a dex save! DC 12"
        hide tom_neutral
        show tom_happy:
            xalign 0.25
            yalign 0.6
        t "Sweet! I got a 15"
        s "23"
        show zack_screaming:
            xalign 0.75
            yalign 0.6
        z "23!!! *dice rolls* Damn. Nat 1."
        hide tom_happy
        show tom_neutral:
            xalign 0.25
            yalign 0.6
        e "Ooooooooooough."
        if player_class:
            p "HaHAAAA! A 19!"
            hide dm_neutral
            show dm_happy:
                xalign 0.5
                yalign 0.2
            d "Nice roll, new guy!"
            hide dm_happy
        else:
            p "My AC is 20."
            show dm_happy:
                xalign 0.5
                yalign 0.2
            d "Wow."
            hide dm_happy
        show dm_neutral:
            xalign 0.5
            yalign 0.2
        d "Harry takes a hit from the arrow trap, and now has poison."
        hide dm_neutral
        show dm_devious:
            xalign 0.5
            yalign 0.2
        d "Harry takes...54 piercing!"
        z "Ahh! I am struck! The cobran arrows have taken my--"
        if player_class:
            p "The chest I found had antitoxins."
        else:
            p "I cast Lesser Restoration."
        show zack_neutral:
            xalign 0.75
            yalign 0.6
        z "Thank you my friend."
        
        "...To failed negotiations and running from traps."
        hide dm_devious

        show dm_neutral:
            xalign 0.5
            yalign 0.2
        d "You see a suspicious old merchant sitting on the floor with a mat in front of him, containing unique treasures and items."
        d "One is a medallion with a sun and moon in front, the next, a bracelet containing a pearl pulsating in a rainbow, and a set of--"
        hide stelle_neutral
        show stelle_happy:
            xalign 0.75
            yalign 0.3
        s "I'm gonna burn him and take his stuff."
        t "Now, now, Zaraana allow me to talk this one out."
        z "Then I shall persuade him!"
        d "Roll persuasion."
        z "*dice rolling*...Does a 10 pass?"
        d "No. You begin to speak your arguement, but the argument is shaky and the old man ignores him."
        t "Let's try something else."

        if player_class:
            t "I'll distract him, you steal the items."
            p "Got it."
            d "[name], roll sleight of hand, Tom, roll Charisma. DC 15"
            p "Well now. A 13."
            t "Yeah, I got a 12."
            d "So you try and speak to him and it seems like he's paying attention,\nbut he looks over and notices the theiving attempt."
            d "You thieves! Get back here!\nGillien manages to barely snag one thing before you all book it to the next room."
        else:
            t "How's about we just try to persuade him for a discount."
            p "Yeah."
            d "[name], Tom, roll Persuasion. The average of your rolls will be measured against DC 14."
            p "Got an 8."
            hide tom_neutral
            show tom_angry:
                xalign 0.25
                yalign 0.6
            t "Damn, a 1."
            d "You both try and fail miserably, to the point where the old man starts to get offended, and destroys all but one of the items."
            d "The old man then vanishes."
            hide tom_angry
        
        show tom_neutral:
            xalign 0.25
            yalign 0.6
        d "You appear in the next room. The room seems mundane enough."
        z "Let us rest a while."
        s "What's the new item?"
        t "Let's take a look."
        d "Roll insight."
        hide stelle_neutral
        show stelle_surprised:
            xalign 0.75
            yalign 0.3
        s "*Bad luck roll* Damn, a Nat 1."
        d "Now, as a consequence of failing, I'm gonna need everyone to make a dex save."
        e "Does a 5 pass?"
        hide dm_neutral
        show dm_devious:
            xalign 0.5
            yalign 0.2
        d "*wicked grin* No! the item lights up, and the floor begins to drop beneath you!"
        hide zack_neutral
        show zack_screaming:
            xalign 0.75
            yalign 0.6
        s "Uh oh."
        t "Crap!"
        p "AAAAAAAAHHH!!!"
        z "WAAAAHHHH!!"
        hide zack_screaming
        hide stelle_surprised

        "Before long, the final hours approached, and the climactic battle was in its peak."
        show zack_neutral:
            xalign 0.75
            yalign 0.6
        show stelle_neutral:
            xalign 0.75
            yalign 0.3
        d "The archfiend is about to charge up its special attack.\nAll creatures in front of it, make a dex save."
        t "Got a dirty 20!"
        p "Got a Nat 20!"
        d "Okay, you guys manage to jump out of the way, and Gillien notices an exposed weakspot.\nIt is now your turn, and you have advantage on your next rolls."
        if player_class:
            p "So I'm gonna slash from my Vicious Rapier from stealth, with sneak attack, and with Master Duelist."
            d "Roll stealth, then your attack."
            p "*luckiest roll #1* Holy crap! I got a Nat 20 on both!"
            show tom_happy:
                xalign 0.25
                yalign 0.6
            show stelle_surprised:
                xalign 0.75
                yalign 0.3
            show zack_screaming:
                xalign 0.75
                yalign 0.6
            show dm_happy:
                xalign 0.5
                yalign 0.2
            e "OOOHH SHIT!"
            d "YO! Stealth passes, roll for crit!"
            p "I got two 8's! That makes 24 Piercing!"
            d "Wow!"
            p "Then my second attack will be to fire my special bullets at it, adding my two inspiration die to the attack."
            d "Okay, so it's probably gonna die to this hit, un less you get really unluck--"
            p "*luckiest roll #2* Another Nat 20!"
            e "WHAT!!!!"
            p "Can I still add my inspiration die?"
            s "Dude, you don't need it but sure! I wanna see where this goes."
            p "*luckiest roll #3* Got a 12!"
            t "YEEAAHHH!!"
            s "Jesus Christ!"
            z "Well damn!"
            d "Okay, new house rule. If you ever get a series of rolls that impossible, that's an instant kill."
            d "Okay, how do you wanna go about this?"
            p "Okay, so I start off by running through the side of the walls, and then throw dust at the monster's eyes so it's blinded,\nthen in that split second, I perform a series of slashes to the weakpoint,\nand then stop at the fron of the weakpoint, and then shoot it."
            d "Okay, the monster is, so thoroughly dead that I don't think it's even recognizable, cut into several pieces, the backwall covered in blood."
            jump dungeon_end
        else:
            p "Okay, so first, I'm gonna use my shield to hit it into the wall. Then, I'm gonna do a jumping slash with my Holy Avenger Longsword, using 4th level Divine Smite and Blinding Smite, and my 2 inspiration die."
            d "Okay, is the shield your first attack, or do you have shield master?"
            p "The first."
            d "Roll for attack, then roll a D6 if it hits and add your strength mod."
            p "*luckiest roll #1* Nat 20."
            show tom_happy:
                xalign 0.25
                yalign 0.6
            show stelle_happy:
                xalign 0.75
                yalign 0.3
            show zack_screaming:
                xalign 0.75
                yalign 0.6
            show dm_happy:
                xalign 0.5
                yalign 0.2
            t "Okay, buddy!"
            s "And so it begins..."
            z "This is gonna be good!"
            p "Got a 6 for damage."
            d "Okay, so you knock it so hard, that it collides with the portal opening jewel, destroying it, and knocking it prone. Do your thing..."
            p "*luckiest roll #2* I got a Nat 20 AND max roll on my inspiration die!"
            t "Yoyoyoyoyoyoyo! Dude!"
            show stelle_surprised:
                xalign 0.75
                yalign 0.3
            s "I'm sorry, what?"
            z "Holy crap!"
            d "Okay, roll your crit damage, but I think any hit at this rate will kill it."
            p "Okay, so...*luckiest roll #3* That's 20 slashing, and with the extra damage from the holy avenger and the smites, 100 Radiant!"
            e "FCJUHBVIVGKUTTRWHAT!     WHAT THE ACTUAL FUCK!   OH MY GOD!"
            d "Okay, so the ceiling of the dungeon opens up, and a literal portal to Mount Celestia's peak starts engulfing Gillien in an obscene amount of light, describe the rest."
            p "As the light pours in, it concentrates on my sword, turning it into a white blade with a rainbow corona that lights the room.\nThen, he rushes towards the enemy, slashing him into the protal along with himself,\nthen stabs him back down."
            d "Okay, this absolutely obliterates the demon. Like, straight up disintegration. The entire room is permanently glowing as the portal closes above you, and the entire dungeon vanished."
            jump dungeon_end
    
    label dungeon_end:

        # This is the end.
        hide game table-adjusted
        hide stelle_surprised
        hide tom_happy
        hide zack_screaming
        hide dm_happy
        "And so the end woud finally come..."

        d "The room is all cleared, you make your way back to the NPC's who give you a shit ton of money. You did it guys! Oneshot's over!"
        t "That was amazing!"
        s "Props to [name] over here for having the best luck!"
        p "I don't expect that to happen again, but that was fun!"
        z "You should join our next session!"
        p "Thanks guys, I really needed this after the stress of the last few months."
        d "I know, right!"
        s "Yeah, my last project was rough."
        z "I haven't gotten a good night's sleep since winter break!"
        t "It seems like all of us have had it rough lately.\Don't fret, we can still contact one another."
        t "So...[name], about that offer from Zack, do you wanna come to our session?"
        p "Y'know, I think I will. When's the date?"

        "As [name] walked back to his dorm, he realized that he had a good opportunity on his hands. Yes, his life will be much better now."





        
        
            


        



        



            

        



        


    # This ends the game.

    return
