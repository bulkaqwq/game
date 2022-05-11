
image vin_bat_2_1_1 = "images/vin battle 2/vin_bat_2_1_1.png"
image vin_bat_2_1:
    contains:
        "black"
    contains:
        "images/vin battle 1/vin_bat_1_1_2.png"
    contains:
        "images/vin battle 2/vin_bat_2_1_1.png"
image vin_bat_2_2_1 = "images/vin battle 2/vin_bat_2_2_1.png"
image vin_bat_2_2:
    contains:
        "images/vin battle 2/vin_bat_2_2_1.png"
    contains:
        ConditionSwitch("vb2_solve_cp == True", "images/vin battle 2/vin_bat_2_2_2.png", "vb2_solve_cp == False", "images/empty.png")
image vin_bat_2_4_1 = "images/vin battle 2/vin_bat_2_4_1.png"
image vin_bat_2_4:
    contains:
        "images/vin battle 2/vin_bat_2_4_1.png"
image vin_bat_2_3_1 = "images/vin battle 2/vin_bat_2_3_1.png"
image vin_bat_2_3_2 = "images/vin battle 2/vin_bat_2_3_2.png"
image vin_bat_2_3:
    contains:
        "black"
    contains:
        "images/vin battle 1/vin_bat_1_3_3.png"
    contains:
        "images/vin battle 2/vin_bat_2_3_1.png"
    contains:
        ConditionSwitch("vb2_solve_cp == True", "images/vin battle 2/vin_bat_2_3_2.png", "vb2_solve_cp == False", "images/empty.png")
image vin_bat_2_3_fini:
    contains:
        "black"
    contains:
        "images/vin battle 2/vin_bat_2_3_1.png"
    contains:
        "images/vin battle 2/vin_bat_2_3_2.png"
    contains:
        "images/vin battle 1/vin_bat_1_3_4.png"
image room_2_banner = "images/vin battle 2/room_2_banner.png"

label vincent_battle_02_start:

    hide screen vin_battle_chance
    hide memory_frame
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(1.0, hard='True')

    $ renpy.free_memory()

    scene black
    show vin_bat_2_1_1:
        zoom 4.5 xoffset -3480 yoffset -850
        ease 0.4 zoom 1.0 xoffset 0 yoffset 0
    $ renpy.pause(1.1, hard='True')

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/monster moan 2.ogg"

    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 2.0, dist=15))
    $ renpy.pause(3.2, hard='True')

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/motor.ogg"

    show vin_bat_1_1_2 behind vin_bat_2_1_1:
        yoffset -550
        ease 1.0 yoffset 0

    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15))
    $ renpy.pause(1.5, hard='True')

    pause 1.0

    $ renpy.music.set_volume(0.2, delay=0, channel='background noise')
    $ renpy.music.play(["<silence 1.0>", "music/banging.ogg"], channel="background noise", fadeout = 6.0, fadein = 6.0, loop = True)

    $ renpy.pause(0.01, hard='True')
    show character_icon_box:
        xpos 130 ypos 250
    show van_icon_angry:
        xpos 130 ypos 248
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ _rollback = True
    $ _skipping = True

    window show

    v "I'm not safe here, {w=0.5}but this door should be enough to hold Vincent off for a while."

    $ rollback_ = True

    v "I need to solve the puzzles here and get out of this room as soon as possible."

    window hide

    hide character_icon_box
    hide van_icon_angry
    with Dissolve(0.5)

    $ vb2_solve_cp = False
    if renpy.is_skipping():
        $ renpy.choice_for_skipping()

    $ renpy.pause(0.5, hard=True)

    $ renpy.music.play("music/UI Dark.ogg", channel="sfx1", synchro_start=True)
    show vin_bat_2_2_1
    $ renpy.transition(Fade(.2, 0, 0.2, color="#fff"))
    $ renpy.pause(0.5, hard=True)

    $ renpy.music.play("music/UI Dark.ogg", channel="sfx2", synchro_start=True)
    show vin_bat_2_3
    hide vin_bat_2_2_1
    $ renpy.transition(Fade(.2, 0, 0.2, color="#fff"))
    $ renpy.pause(0.5, hard=True)

    $ renpy.music.play("music/UI Dark.ogg", channel="sfx3_new", synchro_start=True)
    show vin_bat_2_4_1
    hide vin_bat_2_3
    $ renpy.transition(Fade(.2, 0, 0.2, color="#fff"))
    $ renpy.pause(0.5, hard=True)

    $ renpy.music.play("music/UI Dark.ogg", channel="sfx1", synchro_start=True)
    show vin_bat_2_1_1
    hide vin_bat_2_4_1
    $ renpy.transition(Fade(.2, 0, 0.2, color="#fff"))
    $ renpy.pause(1.0, hard=True)

    $ renpy.pause(0.1, hard='True')
    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/wrong.ogg"
    show room_2_banner with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')
    pause 2.0
    $ renpy.pause(0.1, hard='True')
    hide room_2_banner with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')

    jump vincent_battle_02_click_start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
