
image vin_bat_1_1_1 = "images/vin battle 1/vin_bat_1_1_1.png"
image vin_bat_1_1_2 = "images/vin battle 1/vin_bat_1_1_2.png"
image vin_bat_1_1:
    contains:
        "black"
    contains:
        "images/vin battle 1/vin_bat_1_1_2.png"
    contains:
        "images/vin battle 1/vin_bat_1_1_1.png"
image vin_bat_1_2_1 = "images/vin battle 1/vin_bat_1_2_1.png"
image vin_bat_1_2:
    contains:
        "images/vin battle 1/vin_bat_1_2_1.png"
    contains:
        ConditionSwitch("vin_bat_1_solve_plus == True", "images/vin battle 1/vin_bat_1_2_2.png", "vin_bat_1_solve_plus == False", "images/empty.png")
    contains:
        ConditionSwitch("vin_bat_1_solve_minus == True", "images/vin battle 1/vin_bat_1_2_3.png", "vin_bat_1_solve_minus == False", "images/empty.png")
image vin_bat_1_3_1 = "images/vin battle 1/vin_bat_1_3_1.png"
image vin_bat_1_3_2 = "images/vin battle 1/vin_bat_1_3_2.png"
image vin_bat_1_3_3 = "images/vin battle 1/vin_bat_1_3_3.png"
image vin_bat_1_3_4 = "images/vin battle 1/vin_bat_1_3_4.png"
image vin_bat_1_3:
    contains:
        "black"
    contains:
        "images/vin battle 1/vin_bat_1_3_2.png"
    contains:
        "vin_bat_1_tv_s"
    contains:
        "bad_tv_signal"
        zoom 0.5 xoffset 500 yoffset 110
    contains:
        "images/vin battle 1/vin_bat_1_3_3.png"
    contains:
        "images/vin battle 1/vin_bat_1_3_1.png"
image vin_bat_1_3_0:
    contains:
        "black"
    contains:
        "images/vin battle 1/vin_bat_1_3_2.png"
    contains:
        "images/vin battle 1/vin_bat_1_3_3.png"
    contains:
        "images/vin battle 1/vin_bat_1_3_1.png"
image vin_bat_1_3_fini:
    contains:
        "black"
    contains:
        "vin_bat_1_tv_s"
    contains:
        "bad_tv_signal"
        zoom 0.5 xoffset 500 yoffset 110
    contains:
        "images/vin battle 1/vin_bat_1_3_1.png"
    contains:
        "images/vin battle 1/vin_bat_1_3_4.png"
image room_1_banner = "images/vin battle 1/room_1_banner.png"
image vin_bat_1_tv_s:
    contains:
        "images/vin battle 1/vin_bat_1_tv_s_1.png"
    contains:
        "images/vin battle 1/vin_bat_1_tv_s_2.png"
    contains:
        "images/vin battle 1/vin_bat_1_tv_s_3.png"
    contains:
        "images/vin battle 1/vin_bat_1_tv_s_4.png"

label vincent_battle_01_start:

    scene black
    show vin_bat_1_1_1:
        zoom 4.5 xoffset -3480 yoffset -850
        ease 0.4 zoom 1.0 xoffset 0 yoffset 0
    $ renpy.pause(1.1, hard='True')

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/monster moan 2.ogg"

    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 2.0, dist=15))
    $ renpy.pause(3.2, hard='True')

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/motor.ogg"

    show vin_bat_1_1_2 behind vin_bat_1_1_1:
        yoffset -550
        ease 1.0 yoffset 0

    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15))
    $ renpy.pause(1.5, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound1')
    $ renpy.music.play("music/static.ogg", channel="sound1", loop = False)

    $ renpy.pause(1.0, hard='True')


    show vin_bat_1_1_1:
        zoom 1.0 xoffset 0 yoffset 0
    show vin_bat_1_1_2 behind vin_bat_1_1_1:
        yoffset 0

    window show

    radio "\"Vanora! {w=0.5}Vanora!\""

    v "!?"

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/shock2.ogg" fadeout 2.0

    v "\"Draco!? {w=0.5}Is that you?\"" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    show character_icon_box_1:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 800 ypos 50
        xpos 800 ypos 50
    show draco_icon_blood_serious:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 800 ypos 48
        xpos 800 ypos 48
    show character_icon_box_2:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 800 ypos 50
        xpos 800 ypos 50

    dra "\"Vanora, {w=0.5}Vincent is going berserk! {w=0.5}You need to get out of there now!\""

    v "\"What do I do!?\""

    show vin_bat_1_2_1 behind character_icon_box_1
    with Dissolve(0.5)


    show character_icon_box_1:
        xpos 800 ypos 50
    show character_icon_box_2:
        xpos 800 ypos 50
    show draco_icon_blood_close_eye_serious behind character_icon_box_2:
        xpos 800 ypos 48
    hide draco_icon_blood_serious
    with Dissolve(0.2)

    $ say_who = _("Draco")

    dra "\"You need to first restore power to this room by operating the two control panels connected to the breaker box.\""


    $ vin_bat_1_solve_cp = False

    show vin_bat_1_3_0 behind character_icon_box_1
    hide vin_bat_1_2_1
    with Dissolve(0.5)

    dra "\"This will reactivate the eight touch monitors on the wall.\""

    show draco_icon_blood_serious behind character_icon_box_2:
        xpos 800 ypos 48
    hide draco_icon_blood_close_eye_serious
    with Dissolve(0.2)

    dra "\"After that, {w=0.5}match all the corresponding symbols on the screens, {w=0.5}and the entrance to the next room will unlock.\""

    $ renpy.music.set_volume(0.2, delay=0, channel='background noise')
    $ renpy.music.play(["<silence 1.0>", "music/banging.ogg"], channel="background noise", fadeout = 6.0, fadein = 6.0, loop = True)

    show vin_bat_1_1 behind character_icon_box_1
    with Dissolve(0.5)

    dra "\"I have locked the door behind you, {w=0.5}but I can only hold him off for so long.\""

    show draco_icon_blood_close_eye_serious behind character_icon_box_2:
        xpos 800 ypos 48
    hide draco_icon_blood_serious
    with Dissolve(0.2)

    dra "\"Please hurry!\""

    $ say_who = ""

    window hide

    hide draco_icon_blood_close_eye_serious
    hide character_icon_box_1
    hide character_icon_box_2
    with Dissolve(0.5)

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()

    $ renpy.pause(0.1, hard='True')
    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/wrong.ogg"
    show room_1_banner with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')
    pause 2.0
    $ renpy.pause(0.1, hard='True')
    hide room_1_banner with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')

    jump vincent_battle_01_click_start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
