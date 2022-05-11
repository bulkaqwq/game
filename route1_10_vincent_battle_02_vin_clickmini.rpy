
image vb2_click_minigame_bar_2:
    contains:
        "images/vin battle 1 vin/click_minigame_bar.png"
        subpixel True
    contains:
        "images/vin battle 2 vin/click_minigame_target.png"
        subpixel True

screen vb2_clickmini_screen:

    add "images/vin battle 1 vin/click_minigame_line.png" xpos 1000 ypos vb2_clickmini_pos yanchor 0.5

    key "K_SPACE" action Jump("vb2_vin_click_mini_press")




screen vb2_clickmini_down:
    timer 0.0001 repeat True action [If(vb2_clickmini_pos <= 600, SetVariable("vb2_clickmini_pos", vb2_clickmini_pos + 10)),If(vb2_clickmini_pos >= 600, Hide("vb2_clickmini_down"), Show("vb2_clickmini_up"))]
screen vb2_clickmini_up:
    timer 0.0001 repeat True action [If(vb2_clickmini_pos >= 135, SetVariable("vb2_clickmini_pos", vb2_clickmini_pos - 10)),If(vb2_clickmini_pos <= 135, Hide("vb2_clickmini_up"), Show("vb2_clickmini_down"))]

label vb2_vin_click_mini_start:

    $ vb2_clickmini_pos = 135

    show vb2_click_minigame_bar_2:
        xpos 1000 ypos 100
    $ renpy.transition(Dissolve(0.3))
    $ renpy.pause(0.3, hard='True')

    show screen countdown_(timer_range=10, timer_jump='vb2_vin_death', timer_yalign=0.05)
    show screen vb2_clickmini_down

    call screen vb2_clickmini_screen
    $ renpy.transition(Dissolve(0.1))
    $ renpy.pause(0.1, hard='True')

label vb2_vin_click_mini_press:

    hide screen vb2_clickmini_down
    hide screen vb2_clickmini_up
    hide screen countdown_

    if (vb2_clickmini_pos > 235 and vb2_clickmini_pos < 307) or (vb2_clickmini_pos > 435 and vb2_clickmini_pos < 505):

        $ renpy.music.set_volume(0.6, delay=0, channel='sound')
        play sound "music/weapon click.ogg"
    else:


        $ renpy.music.set_volume(0.7, delay=0, channel='sound')
        play sound "music/tech interface.ogg"

        hide screen vin_battle_chance
        $ vin_battle_chance_num -= 1

    show vb1_click_minigame_line:
        xpos 1000 ypos vb2_clickmini_pos yanchor 0.5


    $ renpy.pause(1.0, hard='True')

    hide vb2_click_minigame_bar_2
    hide vb1_click_minigame_line
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    if (vb2_clickmini_pos > 235 and vb2_clickmini_pos < 307) or (vb2_clickmini_pos > 435 and vb2_clickmini_pos < 505):

        jump vb2_clickmini_run
    else:


        $ renpy.music.set_volume(0.7, delay=0, channel='sound')
        play sound "music/stab.ogg"

        show blood-2:
            alpha 1
            0.3
            linear 0.3 alpha 0
        show red-bg:
            alpha 0
            linear 0.3 alpha 1
            linear 0.5 alpha 0
        $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 1.5, dist=15))
        $ renpy.pause(1.0, hard='True')

label vb2_clickmini_run:

    $ renpy.music.stop(channel="background noise", fadeout = 3.0)

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/run.ogg"

    show vb2_vin_giant_face:
        ease 0.5 zoom 5.0 alpha 0 yoffset -2000
    show vb2_corridor:
        ease 1.0 zoom 5.0 alpha 0 xoffset -3900 yoffset -1800

    $ renpy.pause(3.0, hard='True')

    if vin_battle_chance_num == 0:

        jump vb2_vin_death

    jump vincent_battle_03_start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
