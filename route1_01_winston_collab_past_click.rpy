image winston_past_poker_1 = "images/winston past/winston_past_poker_1.png"
image winston_past_poker_2 = "images/winston past/winston_past_poker_2.png"
image winston_past_poker_3 = "images/winston past/winston_past_poker_3.png"
image winston_past_poker_4 = "images/winston past/winston_past_poker_4.png"
image winston_past_pen_zoom = "images/winston past/winston_past_pen_zoom.png"

screen winston_collab_past_bar_click_screen:

    imagebutton:
        xpos 700
        ypos 324
        idle "images/winston past/winston_past_poker_idle.png"
        hover "images/winston past/winston_past_poker_hover.png"
        focus_mask "images/winston past/winston_past_poker_hover.png"
        action Jump("winston_collab_past_bar_investigate_poker")

    imagebutton:
        xpos 946
        ypos 195
        idle "images/winston past/winston_past_martini_idle.png"
        hover "images/winston past/winston_past_martini_hover.png"
        focus_mask "images/winston past/winston_past_martini_hover.png"
        action Jump("winston_collab_past_bar_investigate_martini")

    imagebutton:
        xpos 413
        ypos 23
        idle "images/winston past/winston_past_radio_idle.png"
        hover "images/winston past/winston_past_radio_hover.png"
        focus_mask "images/winston past/winston_past_radio_hover.png"
        action Jump("winston_collab_past_bar_investigate_radio")

    imagebutton:
        xpos 257
        ypos 322
        idle "images/winston past/winston_past_diary_idle.png"
        hover "images/winston past/winston_past_diary_hover.png"
        focus_mask "images/winston past/winston_past_diary_hover.png"
        action Jump("winston_collab_past_bar_investigate_diary")

    imagebutton:
        xpos 555
        ypos 349
        idle "images/winston past/winston_past_pen_idle.png"
        hover "images/winston past/winston_past_pen_hover.png"
        focus_mask "images/winston past/winston_past_pen_hover.png"
        action Jump("winston_collab_past_bar_investigate_pen")

screen winston_collab_past_bar_poker_screen:

    imagebutton:
        xpos 520
        ypos 610
        idle "images/john past/arrow_down_idle.png"
        hover "images/john past/arrow_down_hover.png"
        focus_mask "images/john past/arrow_down_idle.png"
        action Jump("winston_collab_past_bar_investigate_poker_end")


label winston_collab_past_bar_click_start:

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)


    $ winston_collab_past_bar_check_poker = False
    $ winston_collab_past_bar_check_diary = False
    $ winston_collab_past_bar_check_radio = False

    call screen winston_collab_past_bar_click_screen

label winston_collab_past_bar_investigate_poker:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show winston_past_mansion_bar_table at Position(xpos = 0, ypos = 0)

    show winston_past_mansion_bar_table:
        ease 0.5 zoom 2.0 xoffset -300 yoffset 135

    pause 0.5

    show transparent dark-small:
        alpha 0.8
    with Dissolve(0.5)

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound ("music/winston past/RunningThumbThroughDeck.ogg")

    show winston_past_poker_1:
        xpos 160 ypos -400
        easein_bounce 0.5 xpos 160 ypos 100

    show winston_past_poker_2:
        xpos 400 ypos -400
        pause 0.1
        easein_bounce 0.5 xpos 400 ypos 100

    show winston_past_poker_3:
        xpos 640 ypos -400
        pause 0.2
        easein_bounce 0.5 xpos 640 ypos 100

    show winston_past_poker_4:
        xpos 880 ypos -400
        pause 0.3
        easein_bounce 0.5 xpos 880 ypos 100

    $ renpy.pause(0.5, hard='True')

    if not winston_collab_past_bar_check_poker:

        $ winston_collab_past_bar_check_poker = True

        $ _skipping = True
        $ renpy.block_rollback()
        $ _rollback = True

        show character_icon_box_1:
            xpos 1350 ypos 300
            easein_expo 1.0 xpos 800 ypos 300
        show vin_icon_satire:
            xpos 1350 ypos 298
            easein_expo 1.0 xpos 800 ypos 298
            xpos 800 ypos 298
        show character_icon_box_2:
            xpos 1350 ypos 300
            easein_expo 1.0 xpos 800 ypos 300

        window show

        vin "Poker cards."

        $ rollback_ = True

        vin "The poker cards from the G4 district are a bit different from the more prevalent version."

        vin "The more prevalent version originated from the G3 district, {w=0.5}with four suits: spades, hearts, clubs, and diamonds."

        vin "On the other hand, {w=0.5}the G4 version has a nature theme, {w=0.5}with the four suits replaced by {color=#f00}fire, trees, water droplets, and the moon{/color}."

        vin "There have been many theories as to why this is, {w=0.5}but there is still no definitive answer."

        hide vin_icon_satire
        show vin_icon_high_brow_satire behind character_icon_box_2:
            xpos 800 ypos 298

        vin "However, {w=0.5}this is quite ironic in my opinion,"

        vin "Because the culture and purpose of G4 has nothing to do with nature at all."

        hide vin_icon_high_brow_satire
        show vin_icon_satire behind character_icon_box_2:
            xpos 800 ypos 298

        vin "But more importantly-"

        vin "Why would Winston Loomis bring a deck of cards to Myers Corporation? {w=0.5}And specifically these four?"

        vin "Every employee should know that it is strictly forbidden to carry non-work-related items, {w=0.5}let alone playing cards."

        vin "What's even stranger is, {w=0.5}these four cards happen to contain all four suits, {w=0.5}and {color=#f00}the numbers just happen to be from A to 4{/color} as well."

        hide vin_icon_satire
        show vin_icon_high_brow_satire behind character_icon_box_2:
            xpos 800 ypos 298

        vin "Obviously, {w=0.5}this is some kind of hint that Winston was giving himself. {w=0.5}It is some kind of {color=#f00}code{/color}."

        window hide

        hide character_icon_box_1
        hide character_icon_box_2
        hide vin_icon_high_brow_satire
        $ renpy.transition(Dissolve(0.5))
        $ renpy.pause(0.5, hard='True')

        if renpy.is_skipping():
            $ renpy.choice_for_skipping()
        $ _skipping = False
        $ rollback_ = False
        $ _rollback = False
        $ renpy.music.stop(channel="beep", fadeout = 0.5)

    call screen winston_collab_past_bar_poker_screen

label winston_collab_past_bar_investigate_poker_end:

    hide winston_past_poker_1
    hide winston_past_poker_2
    hide winston_past_poker_3
    hide winston_past_poker_4
    hide transparent dark-small
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    show winston_past_mansion_bar_table:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    $ renpy.pause(0.5, hard='True')
    hide winston_past_mansion_bar_table
    scene winston_past_mansion_bar_table

    $ renpy.block_rollback()
    $ _rollback = False

    call screen winston_collab_past_bar_click_screen

label winston_collab_past_bar_investigate_martini:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show winston_past_mansion_bar_table at Position(xpos = 0, ypos = 0)

    show winston_past_mansion_bar_table:
        ease 0.5 zoom 2.0 xoffset -600 yoffset 400

    pause 0.5

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    show character_icon_box_1:
        xpos 1350 ypos 300
        easein_expo 1.0 xpos 800 ypos 300
    show vin_icon_normal:
        xpos 1350 ypos 298
        easein_expo 1.0 xpos 800 ypos 298
        xpos 800 ypos 298
    show character_icon_box_2:
        xpos 1350 ypos 300
        easein_expo 1.0 xpos 800 ypos 300

    window show

    vin "A specially mixed martini."

    $ rollback_ = True

    vin "It has become more than just a mere pleasure of taste for me."

    vin "It is now a necessity of life."

    window hide

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    hide character_icon_box_1
    hide vin_icon_normal
    hide character_icon_box_2
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    show winston_past_mansion_bar_table:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    $ renpy.pause(0.5, hard='True')
    hide winston_past_mansion_bar_table
    scene winston_past_mansion_bar_table

    $ renpy.block_rollback()
    $ _rollback = False

    call screen winston_collab_past_bar_click_screen

label winston_collab_past_bar_investigate_radio:

    if not winston_collab_past_bar_check_radio:

        $ winston_collab_past_bar_check_radio = True

        $ renpy.music.set_volume(1.0, delay=0, channel='sound')
        play sound ("music/zoom.wav")

        show winston_past_mansion_bar_table at Position(xpos = 0, ypos = 0)

        show winston_past_mansion_bar_table:
            ease 0.5 zoom 2.0 xoffset 0 yoffset 700

        pause 0.5

        $ _skipping = True
        $ renpy.block_rollback()
        $ _rollback = True

        show character_icon_box_1:
            xpos 1350 ypos 300
            easein_expo 1.0 xpos 800 ypos 300
        show vin_icon_satire:
            xpos 1350 ypos 298
            easein_expo 1.0 xpos 800 ypos 298
            xpos 800 ypos 298
        show character_icon_box_2:
            xpos 1350 ypos 300
            easein_expo 1.0 xpos 800 ypos 300

        window show

        vin "The boombox Victor brought in. {w=0.5}I don't know what he was thinking."

        $ rollback_ = True

        vin "However, {w=0.5}the news of Winston's escape is now widespread throughout the G4 district."

        hide vin_icon_satire
        show vin_icon_high_brow_satire behind character_icon_box_2:
            xpos 800 ypos 298

        vin "This is not what I desired. {w=0.5}But unfortunately, {w=0.5}it is inevitable."

        stop music fadeout 5.0

        window hide

        hide character_icon_box_1
        hide vin_icon_high_brow_satire
        hide character_icon_box_2
        with Dissolve(0.5)

        show winston_past_mansion_bar_table:
            ease 0.5 zoom 1.0 xoffset 0 yoffset 0

        $ renpy.pause(0.5, hard='True')
        hide winston_past_mansion_bar_table
        scene winston_past_mansion_bar_table

        $ renpy.pause(1.0, hard='True')

        if renpy.is_skipping():
            $ renpy.choice_for_skipping()
        $ _skipping = False
        $ rollback_ = False
        $ renpy.music.stop(channel="beep", fadeout = 0.5)

        $ renpy.block_rollback()
        $ _rollback = False



        show winston_past_mansion_bar_table_blurred:
            ease 0.4 xoffset -10 yoffset -10 alpha 0.5

            ease 0.4 xoffset 10 yoffset -10 alpha 0.5

            ease 0.4 xoffset -10 yoffset 10 alpha 0.5

            ease 0.4 xoffset 10 yoffset 10 alpha 0.5

            ease 0.4 xoffset 0 yoffset 0 alpha 1.0

        $ renpy.pause(0.1, hard='True')

        $ renpy.music.set_volume(1.0, delay=0, channel='sound')
        play sound "music/heartbeat.ogg"

        show bedroom_headache
        $ renpy.transition(Dissolve(0.4))
        $ renpy.pause(0.4, hard='True')

        hide bedroom_headache
        $ renpy.transition(Dissolve(0.4))
        $ renpy.pause(0.4, hard='True')

        show bedroom_headache
        $ renpy.transition(Dissolve(0.4))
        $ renpy.pause(0.4, hard='True')

        hide bedroom_headache
        $ renpy.transition(Dissolve(0.4))
        $ renpy.pause(0.4, hard='True')

        $ renpy.pause(0.1, hard='True')

        scene black
        show white back
        $ renpy.transition(Dissolve(0.1))
        $ renpy.pause(0.1, hard='True')

        stop music

        $ renpy.music.set_volume(0.7, delay=0, channel='sound')
        play sound "music/teleport.ogg"

        $ renpy.music.set_volume(1.0, delay=0, channel='robot memory')
        $ renpy.music.play("music/magic teleport.ogg", channel="robot memory", loop=False)

        $ renpy.pause(1.0, hard='True')

        hide white back
        $ renpy.transition(Dissolve(1.0))
        $ renpy.pause(1.0, hard='True')

        jump winston_collab_past_end
    else:


        scene engineering_room_4
        show white back
        $ renpy.transition(Dissolve(0.1))
        $ renpy.pause(0.1, hard='True')

        stop music

        $ renpy.music.set_volume(0.7, delay=0, channel='sound')
        play sound "music/teleport.ogg"

        $ renpy.pause(0.3, hard='True')

        hide white back
        $ renpy.transition(Dissolve(1.0))
        $ renpy.pause(1.0, hard='True')

        $ renpy.music.set_volume(1.0, delay=0, channel='music')
        play music "music/bgm/lab investigation.ogg"

        show screen inventory_screen
        with Dissolve(0.2)

        call screen engineering_room_4_screen with Dissolve(0.2)

label winston_collab_past_bar_investigate_diary:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show winston_past_mansion_bar_table at Position(xpos = 0, ypos = 0)

    show winston_past_mansion_bar_table:
        ease 0.5 zoom 2.0 xoffset 500 yoffset 130

    pause 0.5

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    show character_icon_box_1:
        xpos 1350 ypos 300
        easein_expo 1.0 xpos 800 ypos 300
    show vin_icon_high_brow_satire:
        xpos 1350 ypos 298
        easein_expo 1.0 xpos 800 ypos 298
        xpos 800 ypos 298
    show character_icon_box_2:
        xpos 1350 ypos 300
        easein_expo 1.0 xpos 800 ypos 300

    window show

    stop music fadeout 3.0

    vin "A leather notebook. {w=0.5}The cover is engraved with a {color=#f00}triangle{/color}."

    $ rollback_ = True

    if not winston_collab_past_bar_check_diary:

        vin "Every page of the notebook is filled with details of each day's experiments in neat handwriting."

        hide vin_icon_high_brow_satire
        show vin_icon_satire behind character_icon_box_2:
            xpos 800 ypos 298

        vin "There is no doubt that this was Winston's {color=#f00}research journal{/color}."

    window hide

    hide vin_icon_satire
    hide character_icon_box_1
    hide vin_icon_high_brow_satire
    hide vin_icon_high_brow_satire
    hide character_icon_box_2
    with Dissolve(0.5)

    $ rollback_ = True

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music ("music/TenseMusic.ogg")

    nvl show Dissolve(0.5)

    diary "February 15, {w=0.5}2080, {w=0.5}Sunny"

    diary "{color=#f00}Subject No. 5{/color} exhibited very severe rejection, {w=0.5}accompanied by significant mental decline."

    diary "The subject exhibited multiple symptoms of discomfort, {w=0.5}including convulsions, {w=0.5}screaming, {w=0.5}and banging on the containment unit."

    diary "{color=#f00}Subjects No. 1{/color} and {color=#f00}No. 3{/color} are currently stable, {w=0.5}and have not exhibited any signs of rejection."

    nvl clear

    diary "April 10, {w=0.5}2080,{w=0.5} Sunny"

    diary "Subject No. 5's mental condition deteriorated further, {w=0.5}and a portion of the epidermis on the torso showed signs of decay."

    diary "The subject made several attempts to destroy the containment unit, {w=0.5}and still showed no signs of improvement after food intake."

    diary "Subjects No. 1 and No. 3 are currently in a stable condition, {w=0.5}with no rejection observed at this time."

    nvl clear

    diary "July 1, {w=0.5}2080, {w=0.5}Cloudy"

    diary "Subject No. 5's physical condition has deteriorated to the point where only thirty percent of the body's surface still has skin."

    diary "If this subject continues to fail to demonstrate successful mechanization, {w=0.5}we will remove its {color=#f00}memory core{/color}."

    diary "Subject No. 3 is otherwise in good condition, {w=0.5}but with an abnormal refusal to take food today."

    diary "Subject No. 1 is currently in a stable condition, {w=0.5}with no rejection observed at this time."

    nvl clear

    diary "December 20, {w=0.5}2080,{w=0.5} Rainy"

    diary "Subject No. 5's memory core has been successfully dismantled, {w=0.5}and the subject is temporarily sealed in its containment unit."

    diary "We will dismember it at a later date and dispose of its body parts in the wastewater pool outside the G4 district."

    diary "Subjects No. 1 and No. 3 are currently in stable condition and no rejection is observed."

    nvl clear

    diary "January 12, {w=0.5}2081,{w=0.5} Sunny"

    diary "Today, {w=0.5}subject No. 1 suddenly became unstable and violent, {w=0.5}and attempted to attack several researchers."

    diary "The subject stabilized after the removal of the memory core and is now temporarily sealed in its containment unit."

    diary "Subject No. 3 remains stable at this time, {w=0.5}but has yet to show any evidence of successful psychic linking."

    nvl clear

    stop music fadeout 4.0

    nvl hide Dissolve(0.5)

    $ renpy.pause(1.0, hard='True')

    if not winston_collab_past_bar_check_diary:

        $ winston_collab_past_bar_check_diary = True

        show character_icon_box_1:
            xpos 1350 ypos 300
            easein_expo 1.0 xpos 800 ypos 300
        show vin_icon_dark:
            xpos 1350 ypos 298
            easein_expo 1.0 xpos 800 ypos 298
            xpos 800 ypos 298
        show character_icon_box_2:
            xpos 1350 ypos 300
            easein_expo 1.0 xpos 800 ypos 300

        window show

        vin "......"

        window hide

        pause 1.0

        hide vin_icon_dark
        show vin_icon_dark_smile behind character_icon_box_2:
            xpos 800 ypos 298
        with Dissolve(0.2)

        pause 1.0

        window show

        vin "Memory core is it? {w=0.5}Huh."

        window hide

        hide vin_icon_satire
        hide character_icon_box_1
        hide vin_icon_dark_smile
        hide character_icon_box_2
        with Dissolve(0.5)

    show winston_past_mansion_bar_table:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    $ renpy.pause(0.5, hard='True')
    hide winston_past_mansion_bar_table
    scene winston_past_mansion_bar_table

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    $ renpy.block_rollback()
    $ _rollback = False

    $ renpy.music.set_volume(0.5, delay=0, channel='music')
    play music ("music/bgm/jazz-lounge.ogg")

    call screen winston_collab_past_bar_click_screen

label winston_collab_past_bar_investigate_pen:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show winston_past_mansion_bar_table at Position(xpos = 0, ypos = 0)

    show winston_past_mansion_bar_table:
        ease 0.5 zoom 2.0 xoffset 100 yoffset 130

    pause 0.5

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    show character_icon_box_1:
        xpos 1350 ypos 300
        easein_expo 1.0 xpos 800 ypos 300
    show vin_icon_satire:
        xpos 1350 ypos 298
        easein_expo 1.0 xpos 800 ypos 298
        xpos 800 ypos 298
    show character_icon_box_2:
        xpos 1350 ypos 300
        easein_expo 1.0 xpos 800 ypos 300

    window show

    $ say_who = _("Vincent")

    vin "A fountain pen."

    $ rollback_ = True

    show winston_past_pen_zoom
    with Dissolve(0.5)

    hide vin_icon_satire
    show vin_icon_high_brow_satire behind character_icon_box_2:
        xpos 800 ypos 298

    vin "The whole surface of the barrel is smooth, {w=0.5}but only one side has a {color=#f00}square{/color} engraved on it, {w=0.5}which seems quite out of place."

    window hide

    $ say_who = ""

    hide character_icon_box_1
    hide vin_icon_satire
    hide character_icon_box_2
    hide vin_icon_high_brow_satire
    hide winston_past_pen_zoom
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    show winston_past_mansion_bar_table:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0
    $ renpy.pause(0.5, hard='True')

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    hide winston_past_mansion_bar_table
    scene winston_past_mansion_bar_table

    $ renpy.block_rollback()
    $ _rollback = False

    call screen winston_collab_past_bar_click_screen
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
