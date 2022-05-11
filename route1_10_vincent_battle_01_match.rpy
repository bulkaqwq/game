
image vin_bat_1_match_2 = "images/vin battle 1/vin_bat_1_match_2.png"
image vin_bat_1_match_1 = "images/vin battle 1/vin_bat_1_match_1.png"
image vin_bat_1_match_s_1 = "images/vin battle 1/vin_bat_1_match_s_1.png"
image vin_bat_1_match_s_2 = "images/vin battle 1/vin_bat_1_match_s_2.png"
image vin_bat_1_match_s_3 = "images/vin battle 1/vin_bat_1_match_s_3.png"
image vin_bat_1_match_s_4 = "images/vin battle 1/vin_bat_1_match_s_4.png"
image vin_bat_1_match_s_5 = "images/vin battle 1/vin_bat_1_match_s_5.png"
image vin_bat_1_match_s_6 = "images/vin battle 1/vin_bat_1_match_s_6.png"
image vin_bat_1_match_s_7 = "images/vin battle 1/vin_bat_1_match_s_7.png"
image vin_bat_1_match_s_8 = "images/vin battle 1/vin_bat_1_match_s_8.png"

screen vin_bat_1_match_screen_arrow:
    imagebutton:
        xpos 698
        ypos 615
        idle "images/basement/basement_door_arrow_down_idle.png"
        hover "images/tunnel/myers_tunnel_door_arrow_down_hover.png"
        focus_mask "images/basement/basement_door_arrow_down_idle.png"
        action Jump("vin_bat_1_match_leave")

screen vin_bat_1_match_screen:

    if not vin_bat_1_match_h[1]:
        imagebutton:
            xpos 135
            ypos 44
            idle "images/vin battle 1/vin_bat_1_match_1_idle.png"
            hover "images/vin battle 1/vin_bat_1_match_1_hover.png"
            focus_mask "images/vin battle 1/vin_bat_1_match_1_hover.png"
            action Jump("vin_bat_1_click_match_1")

    if not vin_bat_1_match_h[2]:
        imagebutton:
            xpos 455
            ypos 119
            idle "images/vin battle 1/vin_bat_1_match_2_idle.png"
            hover "images/vin battle 1/vin_bat_1_match_2_hover.png"
            focus_mask "images/vin battle 1/vin_bat_1_match_2_hover.png"
            action Jump("vin_bat_1_click_match_2")

    if not vin_bat_1_match_h[3]:
        imagebutton:
            xpos 702
            ypos 44
            idle "images/vin battle 1/vin_bat_1_match_3_idle.png"
            hover "images/vin battle 1/vin_bat_1_match_3_hover.png"
            focus_mask "images/vin battle 1/vin_bat_1_match_3_hover.png"
            action Jump("vin_bat_1_click_match_3")

    if not vin_bat_1_match_h[4]:
        imagebutton:
            xpos 942
            ypos 105
            idle "images/vin battle 1/vin_bat_1_match_4_idle.png"
            hover "images/vin battle 1/vin_bat_1_match_4_hover.png"
            focus_mask "images/vin battle 1/vin_bat_1_match_4_hover.png"
            action Jump("vin_bat_1_click_match_4")

    if not vin_bat_1_match_h[5]:
        imagebutton:
            xpos 97
            ypos 301
            idle "images/vin battle 1/vin_bat_1_match_5_idle.png"
            hover "images/vin battle 1/vin_bat_1_match_5_hover.png"
            focus_mask "images/vin battle 1/vin_bat_1_match_5_hover.png"
            action Jump("vin_bat_1_click_match_5")

    if not vin_bat_1_match_h[6]:
        imagebutton:
            xpos 396
            ypos 449
            idle "images/vin battle 1/vin_bat_1_match_6_idle.png"
            hover "images/vin battle 1/vin_bat_1_match_6_hover.png"
            focus_mask "images/vin battle 1/vin_bat_1_match_6_hover.png"
            action Jump("vin_bat_1_click_match_6")

    if not vin_bat_1_match_h[7]:
        imagebutton:
            xpos 697
            ypos 360
            idle "images/vin battle 1/vin_bat_1_match_7_idle.png"
            hover "images/vin battle 1/vin_bat_1_match_7_hover.png"
            focus_mask "images/vin battle 1/vin_bat_1_match_7_hover.png"
            action Jump("vin_bat_1_click_match_7")

    if not vin_bat_1_match_h[8]:
        imagebutton:
            xpos 1022
            ypos 337
            idle "images/vin battle 1/vin_bat_1_match_8_idle.png"
            hover "images/vin battle 1/vin_bat_1_match_8_hover.png"
            focus_mask "images/vin battle 1/vin_bat_1_match_8_hover.png"
            action Jump("vin_bat_1_click_match_8")

label vin_bat_1_match_start:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    scene black
    show vin_bat_1_match_1
    show bad_tv_signal
    show vin_bat_1_match_2
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')


    $ vin_bat_1_match_cur_act = 0
    $ vin_bat_1_match = [False, False, False, False, False, False, False, False, False]
    $ vin_bat_1_match_h = [False, False, False, False, False, False, False, False, False]
    $ vin_bat_1_match_num = 0

    show screen vin_bat_1_match_screen_arrow

    call screen vin_bat_1_match_screen

label vin_bat_1_match_leave:

    hide screen vin_bat_1_match_screen_arrow

    hide vin_bat_1_match_1
    hide bad_tv_signal
    hide vin_bat_1_match_2
    hide vin_bat_1_match_s_1
    hide vin_bat_1_match_s_2
    hide vin_bat_1_match_s_3
    hide vin_bat_1_match_s_4
    hide vin_bat_1_match_s_5
    hide vin_bat_1_match_s_6
    hide vin_bat_1_match_s_7
    hide vin_bat_1_match_s_8
    show vin_bat_1_3
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    call screen vin_bat_1_3_screen with Dissolve(0.2)

label vin_bat_1_click_match_1:

    $ vin_bat_1_match_h[1] = True

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/misc_menu.wav"

    if vin_bat_1_match_cur_act == 0:
        $ vin_bat_1_match_cur_act = 1

    show vin_bat_1_match_s_1 behind bad_tv_signal
    with Dissolve(0.1)

    if vin_bat_1_match_cur_act != 1:
        if vin_bat_1_match_cur_act != 7:
            $ vin_bat_1_match_cur_act = 0
            jump vin_bat_1_click_match_incorrect
        else:
            $ vin_bat_1_match[1] = True
            $ vin_bat_1_match[7] = True
            $ vin_bat_1_match_cur_act = 0
            $ vin_bat_1_match_num += 2
            jump vin_bat_1_click_match_correct

    call screen vin_bat_1_match_screen

label vin_bat_1_click_match_2:

    $ vin_bat_1_match_h[2] = True

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/misc_menu.wav"

    if vin_bat_1_match_cur_act == 0:
        $ vin_bat_1_match_cur_act = 2

    show vin_bat_1_match_s_2 behind bad_tv_signal
    with Dissolve(0.1)

    if vin_bat_1_match_cur_act != 2:
        if vin_bat_1_match_cur_act != 4:
            $ vin_bat_1_match_cur_act = 0
            jump vin_bat_1_click_match_incorrect
        else:
            $ vin_bat_1_match[2] = True
            $ vin_bat_1_match[4] = True
            $ vin_bat_1_match_cur_act = 0
            $ vin_bat_1_match_num += 2
            jump vin_bat_1_click_match_correct

    call screen vin_bat_1_match_screen

label vin_bat_1_click_match_3:

    $ vin_bat_1_match_h[3] = True

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/misc_menu.wav"

    if vin_bat_1_match_cur_act == 0:
        $ vin_bat_1_match_cur_act = 3

    show vin_bat_1_match_s_3 behind bad_tv_signal
    with Dissolve(0.1)

    if vin_bat_1_match_cur_act != 3:
        if vin_bat_1_match_cur_act != 6:
            $ vin_bat_1_match_cur_act = 0
            jump vin_bat_1_click_match_incorrect
        else:
            $ vin_bat_1_match[3] = True
            $ vin_bat_1_match[6] = True
            $ vin_bat_1_match_cur_act = 0
            $ vin_bat_1_match_num += 2
            jump vin_bat_1_click_match_correct

    call screen vin_bat_1_match_screen

label vin_bat_1_click_match_4:

    $ vin_bat_1_match_h[4] = True

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/misc_menu.wav"

    if vin_bat_1_match_cur_act == 0:
        $ vin_bat_1_match_cur_act = 4

    show vin_bat_1_match_s_4 behind bad_tv_signal
    with Dissolve(0.1)

    if vin_bat_1_match_cur_act != 4:
        if vin_bat_1_match_cur_act != 2:
            $ vin_bat_1_match_cur_act = 0
            jump vin_bat_1_click_match_incorrect
        else:
            $ vin_bat_1_match[4] = True
            $ vin_bat_1_match[2] = True
            $ vin_bat_1_match_cur_act = 0
            $ vin_bat_1_match_num += 2
            jump vin_bat_1_click_match_correct

    call screen vin_bat_1_match_screen

label vin_bat_1_click_match_5:

    $ vin_bat_1_match_h[5] = True

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/misc_menu.wav"

    if vin_bat_1_match_cur_act == 0:
        $ vin_bat_1_match_cur_act = 5

    show vin_bat_1_match_s_5 behind bad_tv_signal
    with Dissolve(0.1)

    if vin_bat_1_match_cur_act != 5:
        if vin_bat_1_match_cur_act != 8:
            $ vin_bat_1_match_cur_act = 0
            jump vin_bat_1_click_match_incorrect
        else:
            $ vin_bat_1_match[5] = True
            $ vin_bat_1_match[8] = True
            $ vin_bat_1_match_cur_act = 0
            $ vin_bat_1_match_num += 2
            jump vin_bat_1_click_match_correct

    call screen vin_bat_1_match_screen

label vin_bat_1_click_match_6:

    $ vin_bat_1_match_h[6] = True

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/misc_menu.wav"

    if vin_bat_1_match_cur_act == 0:
        $ vin_bat_1_match_cur_act = 6

    show vin_bat_1_match_s_6 behind bad_tv_signal
    with Dissolve(0.1)

    if vin_bat_1_match_cur_act != 6:
        if vin_bat_1_match_cur_act != 3:
            $ vin_bat_1_match_cur_act = 0
            jump vin_bat_1_click_match_incorrect
        else:
            $ vin_bat_1_match[6] = True
            $ vin_bat_1_match[3] = True
            $ vin_bat_1_match_cur_act = 0
            $ vin_bat_1_match_num += 2
            jump vin_bat_1_click_match_correct

    call screen vin_bat_1_match_screen

label vin_bat_1_click_match_7:

    $ vin_bat_1_match_h[7] = True

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/misc_menu.wav"

    if vin_bat_1_match_cur_act == 0:
        $ vin_bat_1_match_cur_act = 7

    show vin_bat_1_match_s_7 behind bad_tv_signal
    with Dissolve(0.1)

    if vin_bat_1_match_cur_act != 7:
        if vin_bat_1_match_cur_act != 1:
            $ vin_bat_1_match_cur_act = 0
            jump vin_bat_1_click_match_incorrect
        else:
            $ vin_bat_1_match[7] = True
            $ vin_bat_1_match[1] = True
            $ vin_bat_1_match_cur_act = 0
            $ vin_bat_1_match_num += 2
            jump vin_bat_1_click_match_correct

    call screen vin_bat_1_match_screen

label vin_bat_1_click_match_8:

    $ vin_bat_1_match_h[8] = True

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/misc_menu.wav"

    if vin_bat_1_match_cur_act == 0:
        $ vin_bat_1_match_cur_act = 8

    show vin_bat_1_match_s_8 behind bad_tv_signal
    with Dissolve(0.1)

    if vin_bat_1_match_cur_act != 8:
        if vin_bat_1_match_cur_act != 5:
            $ vin_bat_1_match_cur_act = 0
            jump vin_bat_1_click_match_incorrect
        else:
            $ vin_bat_1_match[8] = True
            $ vin_bat_1_match[5] = True
            $ vin_bat_1_match_cur_act = 0
            $ vin_bat_1_match_num += 2
            jump vin_bat_1_click_match_correct

    call screen vin_bat_1_match_screen

label vin_bat_1_click_match_incorrect:

    $ renpy.music.set_volume(0.7, delay=0, channel='sound1')
    $ renpy.music.play("music/tech interface.ogg", channel="sound1", loop=False)

    $ renpy.pause(0.5, hard='True')

    if not vin_bat_1_match[1]:
        $ vin_bat_1_match_h[1] = False
        hide vin_bat_1_match_s_1
    if not vin_bat_1_match[2]:
        $ vin_bat_1_match_h[2] = False
        hide vin_bat_1_match_s_2
    if not vin_bat_1_match[3]:
        $ vin_bat_1_match_h[3] = False
        hide vin_bat_1_match_s_3
    if not vin_bat_1_match[4]:
        $ vin_bat_1_match_h[4] = False
        hide vin_bat_1_match_s_4
    if not vin_bat_1_match[5]:
        $ vin_bat_1_match_h[5] = False
        hide vin_bat_1_match_s_5
    if not vin_bat_1_match[6]:
        $ vin_bat_1_match_h[6] = False
        hide vin_bat_1_match_s_6
    if not vin_bat_1_match[7]:
        $ vin_bat_1_match_h[7] = False
        hide vin_bat_1_match_s_7
    if not vin_bat_1_match[8]:
        $ vin_bat_1_match_h[8] = False
        hide vin_bat_1_match_s_8
    with Dissolve(0.1)
    call screen vin_bat_1_match_screen

label vin_bat_1_click_match_correct:

    if vin_bat_1_match_num == 8:
        hide screen vin_bat_1_match_screen_arrow

    $ renpy.music.set_volume(1.0, delay=0, channel='sound1')
    $ renpy.music.play("music/email sent.ogg", channel="sound1", loop=False)

    $ renpy.pause(0.5, hard='True')

    if vin_bat_1_match_num == 8:

        hide vin_bat_1_match_1
        hide bad_tv_signal
        hide vin_bat_1_match_2
        hide vin_bat_1_match_s_1
        hide vin_bat_1_match_s_2
        hide vin_bat_1_match_s_3
        hide vin_bat_1_match_s_4
        hide vin_bat_1_match_s_5
        hide vin_bat_1_match_s_6
        hide vin_bat_1_match_s_7
        hide vin_bat_1_match_s_8
        show vin_bat_1_3
        $ renpy.transition(Dissolve(1.0))
        $ renpy.pause(1.0, hard='True')

        jump vin_bat_1_vin_start

    call screen vin_bat_1_match_screen
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
