image vin_bat_start_bg = "images/vin battle start/vin-bat-start-bg.png"
image vin_bat_start_drop_shadow = "images/vin battle start/vin-bat-start-drop-shadow.png"
image vin_bat_start_vin_1 = "images/vin battle start/vin-bat-start-vin-1.png"
image vin_bat_start_vin_2 = "images/vin battle start/vin-bat-start-vin-2.png"
image vin_bat_start_smile_1 = "images/vin battle start/vin-bat-start-smile-animation/vin-bat-start-smile-1.png"

image vin_bat_start_smile_animation:
    "images/vin battle start/vin-bat-start-smile-animation/vin-bat-start-smile-1.png"
    pause 0.1
    "images/vin battle start/vin-bat-start-smile-animation/vin-bat-start-smile-2.png"
    pause 0.1
    "images/vin battle start/vin-bat-start-smile-animation/vin-bat-start-smile-3.png"
    pause 0.1
    "images/vin battle start/vin-bat-start-smile-animation/vin-bat-start-smile-4.png"
    pause 0.1
    "images/vin battle start/vin-bat-start-smile-animation/vin-bat-start-smile-5.png"
    pause 0.1
    "images/vin battle start/vin-bat-start-smile-animation/vin-bat-start-smile-6.png"
    pause 0.1
    "images/vin battle start/vin-bat-start-smile-animation/vin-bat-start-smile-7.png"
    pause 0.1

image vin_bat_start_bg_animation:
    "images/vin battle start/vin-bat-start-bg-animation/vin-bat-start-bg1.jpg" with Dissolve(0.5)
    0.5
    "images/vin battle start/vin-bat-start-bg-animation/vin-bat-start-bg2.jpg" with Dissolve(0.5)
    0.5
    "images/vin battle start/vin-bat-start-bg-animation/vin-bat-start-bg3.jpg" with Dissolve(0.5)
    0.5
    "images/vin battle start/vin-bat-start-bg-animation/vin-bat-start-bg4.jpg" with Dissolve(0.5)
    0.5
    repeat

label vincent_battle_start:

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()

    pause 2.0

    scene basement_chamber
    show chamber_vincent_tie2
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    pause 2.0

    window show

    vin "\"......\""

    window hide

    pause 2.0

    window show

    vin "\"You saw... {w=0.5}all of that?\""

    window hide

    pause 1.0

    show character_icon_box:
        xpos 130 ypos 250
    show van_icon_angry:
        xpos 130 ypos 248
    with Dissolve(0.5)

    window show

    v "\"...It was you. {w=0.5}You were the one who murdered all the core members.\""

    v "\"What exactly... {w=0.5}are you?\""

    window hide

    scene vin_bat_start_bg
    show vin_bat_start_bg_animation
    show vin_bat_start_drop_shadow:
        ease 0.05 alpha 0.9
        ease 0.05 alpha 1.0
        repeat
    show vin_bat_start_vin_1:
    show vin_bat_start_smile_1
    with Dissolve(1.0)

    pause 1.0

    vin "\"Me? {w=0.5}What am I?\""

    vin "\"Can't you tell?\""

    show vin_bat_start_drop_shadow:
        parallel:
            ease 1.5 zoom 1.05 xoffset -30 yoffset -35
        parallel:
            ease 0.05 alpha 0.9
            ease 0.05 alpha 1.0
            repeat
    show vin_bat_start_vin_1:
        ease 1.5 zoom 1.05 xoffset -30 yoffset -35
        alpha 0
    show vin_bat_start_vin_2:
        parallel:
            alpha 0
            linear 0.5 alpha 1
        parallel:
            ease 1.5 zoom 1.05 xoffset -30 yoffset -35
    hide vin_bat_start_smile_1
    show vin_bat_start_smile_animation:
        ease 1.5 zoom 1.05 xoffset -30 yoffset -35
    show memory_frame:
        alpha 0
        block:
            ease 0.05 alpha 0.2
            ease 0.05 alpha 0.1
            repeat

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/monster moan 2.ogg"

    $ renpy.pause(0.2, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music "music/bgm/Boss Vincent bgm.ogg"

    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 2.0, dist=15))

    $ renpy.pause(2.5, hard='True')

    vin "\"I'm a product of the Myers Corporation, {w=0.5}just like you.\""

    vin "\"Take a good look, {w=0.5}this is how Myers Corporation treats a lawyer who has done everything he could for them.\""

    vin "\"I know Myers isn't gone yet.\""

    vin "\"But soon, {w=0.5}I will clean them all up.\""

    v "!?"

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/run.ogg"

    scene black with Dissolve(0.5)

    $ renpy.free_memory()

    v "I let go of Vincent's tie and ran out of the chamber at lightning speed."

    scene basement_4
    show basement_shadow_vanora:
        xoffset -100
    show game_over_static:
        alpha 0.3
    with Dissolve(0.5)

    pause 0.5

    v "Outside the chamber, {w=0.5}I once again saw that mysterious figure."

    v "She was standing next to the box, {w=0.5}seemingly hinting at something to me."

    hide basement_shadow_vanora
    hide game_over_static
    with Dissolve(0.5)

    v " I took the photo out from the box and placed it in my pocket, {w=0.5}then quickly ran to the next room."

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/scan map.ogg"

    scene black
    show basement_3_2
    show basement_3_1
    $ renpy.transition(room_pushright)
    $ renpy.pause(0.4, hard='True')

    $ renpy.pause(0.6, hard='True')

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/motor.ogg"

    show basement_3_2:
        ease 1.0 yoffset -550

    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15))
    $ renpy.pause(1.5, hard='True')

    hide basement_3_2
    show basement_3_1:
        ease 0.4 zoom 4.5 xoffset 1250 yoffset 1850
    show black as black_2:
        alpha 0
        pause 0.2
        ease 0.2 alpha 1
    $ renpy.pause(0.5, hard='True')

    jump vincent_battle_01_start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
