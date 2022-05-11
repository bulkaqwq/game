
image vb2_match_zoom_1 = "images/vin battle 2/vb2_match_zoom_1.png"
image vb2_match_zoom_2 = "images/vin battle 2/vb2_match_zoom_2.png"
image vb2_match_zoom_3 = "images/vin battle 2/vb2_match_zoom_3.png"
image vb2_match_zoom_4 = "images/vin battle 2/vb2_match_zoom_4.png"

image vb2_match_button_1 = "images/vin battle 2/vb2_match_button_1.png"
image vb2_match_button_2 = "images/vin battle 2/vb2_match_button_2.png"

screen vb2_match_screen:

    imagebutton:
        xpos 520
        ypos 610
        idle "images/basement/basement_door_arrow_down_idle.png"
        hover "images/tunnel/myers_tunnel_door_arrow_down_hover.png"
        focus_mask "images/basement/basement_door_arrow_down_idle.png"
        action Jump("vb2_match_leave")

    imagebutton:
        xpos 285
        ypos 300
        idle "images/vin battle 2/vb2_match_button_idle.png"
        hover "images/vin battle 2/vb2_match_button_hover.png"
        focus_mask "images/vin battle 2/vb2_match_button_hover.png"
        action Call("vb2_match_manipulate", 0)

    imagebutton:
        xpos 485
        ypos 300
        idle "images/vin battle 2/vb2_match_button_idle.png"
        hover "images/vin battle 2/vb2_match_button_hover.png"
        focus_mask "images/vin battle 2/vb2_match_button_hover.png"
        action Call("vb2_match_manipulate", 1)

    imagebutton:
        xpos 685
        ypos 300
        idle "images/vin battle 2/vb2_match_button_idle.png"
        hover "images/vin battle 2/vb2_match_button_hover.png"
        focus_mask "images/vin battle 2/vb2_match_button_hover.png"
        action Call("vb2_match_manipulate", 2)

    imagebutton:
        xpos 885
        ypos 300
        idle "images/vin battle 2/vb2_match_button_idle.png"
        hover "images/vin battle 2/vb2_match_button_hover.png"
        focus_mask "images/vin battle 2/vb2_match_button_hover.png"
        action Call("vb2_match_manipulate", 3)

label vb2_match_start:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")


    $ vb2_match_pos = -700

    $ vb2_match_b_state = [True, True, True, True]

    show vb2_match_zoom_3
    show vb2_match_zoom_2:
        xoffset -1000
        ease 1.0 xoffset vb2_match_pos
    show vb2_match_zoom_1
    show vb2_match_zoom_4
    show vb2_match_button_1 as vb2_match_b_1:
        xpos 285 ypos 300
    show vb2_match_button_1 as vb2_match_b_2:
        xpos 485 ypos 300
    show vb2_match_button_1 as vb2_match_b_3:
        xpos 685 ypos 300
    show vb2_match_button_1 as vb2_match_b_4:
        xpos 885 ypos 300
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    call screen vb2_match_screen

label vb2_match_manipulate(vb2_manipulate_num):

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/Tunnel/wheelMoveSFX.ogg"

    if vb2_manipulate_num == 0:

        if vb2_match_b_state[0]:
            show vb2_match_button_2 as vb2_match_b_1:
                xpos 285 ypos 300
            $ vb2_match_b_state[0] = False
            $ vb2_match_pos = vb2_match_pos + 200
        else:
            show vb2_match_button_1 as vb2_match_b_1:
                xpos 285 ypos 300
            $ vb2_match_b_state[0] = True
            $ vb2_match_pos = vb2_match_pos - 200

    elif vb2_manipulate_num == 1:

        if vb2_match_b_state[1]:
            show vb2_match_button_2 as vb2_match_b_2:
                xpos 485 ypos 300
            $ vb2_match_b_state[1] = False
            $ vb2_match_pos = vb2_match_pos - 100
        else:
            show vb2_match_button_1 as vb2_match_b_2:
                xpos 485 ypos 300
            $ vb2_match_b_state[1] = True
            $ vb2_match_pos = vb2_match_pos + 100

    elif vb2_manipulate_num == 2:

        if vb2_match_b_state[2]:
            show vb2_match_button_2 as vb2_match_b_3:
                xpos 685 ypos 300
            $ vb2_match_b_state[2] = False
            $ vb2_match_pos = vb2_match_pos + 300
        else:
            show vb2_match_button_1 as vb2_match_b_3:
                xpos 685 ypos 300
            $ vb2_match_b_state[2] = True
            $ vb2_match_pos = vb2_match_pos - 300

    elif vb2_manipulate_num == 3:

        if vb2_match_b_state[3]:
            show vb2_match_button_2 as vb2_match_b_4:
                xpos 885 ypos 300
            $ vb2_match_b_state[3] = False
            $ vb2_match_pos = vb2_match_pos - 165
        else:
            show vb2_match_button_1 as vb2_match_b_4:
                xpos 885 ypos 300
            $ vb2_match_b_state[3] = True
            $ vb2_match_pos = vb2_match_pos + 165

    show vb2_match_zoom_2:
        ease 1.0 xoffset vb2_match_pos

    if vb2_match_pos == -365:

        $ renpy.music.set_volume(0.6, delay=0, channel='sound')
        play sound "music/weapon click.ogg"

        $ renpy.pause(1.5, hard='True')

        hide vb2_match_zoom_3
        hide vb2_match_zoom_2
        hide vb2_match_zoom_1
        hide vb2_match_zoom_4
        hide vb2_match_b_1
        hide vb2_match_b_2
        hide vb2_match_b_3
        hide vb2_match_b_4
        $ renpy.transition(Dissolve(0.5))
        $ renpy.pause(0.5, hard='True')

        $ renpy.pop_call()

        jump vin_bat_2_vin_start

    $ renpy.pop_call()

    call screen vb2_match_screen

label vb2_match_leave:

    hide vb2_match_zoom_3
    hide vb2_match_zoom_2
    hide vb2_match_zoom_1
    hide vb2_match_zoom_4
    hide vb2_match_b_1
    hide vb2_match_b_2
    hide vb2_match_b_3
    hide vb2_match_b_4
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    call screen vin_bat_2_3_screen
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
