
image vb1_click_minigame_bar_1:
    contains:
        "images/vin battle 1 vin/click_minigame_bar.png"
        subpixel True
    contains:
        "images/vin battle 1 vin/click_minigame_target.png"
        subpixel True
image vb1_click_minigame_line = "images/vin battle 1 vin/click_minigame_line.png"

screen vb1_clickmini_screen:

    add "images/vin battle 1 vin/click_minigame_line.png" xpos 1000 ypos vb1_clickmini_pos yanchor 0.5

    key "K_SPACE" action Jump("vb1_vin_click_mini_press")




screen vb1_clickmini_down:
    timer 0.0001 repeat True action [If(vb1_clickmini_pos <= 600, SetVariable("vb1_clickmini_pos", vb1_clickmini_pos + 10)),If(vb1_clickmini_pos >= 600, Hide("vb1_clickmini_down"), Show("vb1_clickmini_up"))]
screen vb1_clickmini_up:
    timer 0.0001 repeat True action [If(vb1_clickmini_pos >= 135, SetVariable("vb1_clickmini_pos", vb1_clickmini_pos - 10)),If(vb1_clickmini_pos <= 135, Hide("vb1_clickmini_up"), Show("vb1_clickmini_down"))]

label vb1_vin_click_mini_start:

    $ vb1_clickmini_pos = 135

    show vb1_vin_corridor:
        block:
            xpos 0

            linear 2 xpos -120
            linear 2 xpos 0
            repeat

    show vb1_click_minigame_bar_1:
        xpos 1000 ypos 100
    $ renpy.transition(Dissolve(0.3))
    $ renpy.pause(0.3, hard='True')

    show screen countdown(timer_range=10, timer_jump='vb1_vin_death')
    show screen vb1_clickmini_down

    call screen vb1_clickmini_screen
    $ renpy.transition(Dissolve(0.1))
    $ renpy.pause(0.1, hard='True')

label vb1_vin_click_mini_press:

    hide screen vb1_clickmini_down
    hide screen vb1_clickmini_up
    hide screen countdown

    if vb1_clickmini_pos > 280 and vb1_clickmini_pos < 441:
        $ renpy.music.set_volume(0.6, delay=0, channel='sound')
        play sound "music/weapon click.ogg"
    else:
        $ renpy.music.set_volume(0.7, delay=0, channel='sound')
        play sound "music/tech interface.ogg"

        hide screen vin_battle_chance
        $ vin_battle_chance_num -= 1

    show vb1_click_minigame_line:
        xpos 1000 ypos vb1_clickmini_pos yanchor 0.5

    $ renpy.pause(1.0, hard='True')

    hide vb1_click_minigame_bar_1
    hide vb1_click_minigame_line
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    if vb1_clickmini_pos > 280 and vb1_clickmini_pos < 441:

        jump vb1_clickmini_run
    else:


        $ renpy.music.set_volume(0.7, delay=0, channel='sound')
        play sound "music/stab.ogg"

        show blood-2:
            0.3
            alpha 1
            linear 0.3 alpha 0
        show red-bg:
            alpha 0
            linear 0.3 alpha 1
            linear 0.5 alpha 0
        $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 1.5, dist=15))

        $ renpy.pause(1.0, hard='True')

label vb1_clickmini_run:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/run.ogg"

    show vb1_vin_corridor:
        linear 1 xpos -11200 xzoom 4.0 alpha 0
    show vb1_vin_giant_face:
        linear 0.2 xoffset -1000

    $ renpy.pause(1.5, hard='True')

    if vin_battle_chance_num == 0:

        jump vb1_vin_death

    jump vincent_battle_02_start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
