
image vb3_cp2_zoom_base:
    contains:
        "images/vin battle 3/vb3_cp2_zoom.png"
    contains:
        Text(_("{size=+20}{font=impact.ttf}ENTER{/font}{/size}"))
        xalign 0.5 ypos 542 yanchor 0.5

image vb3_cp2_button = "images/Engineering Room 1/Engineering_room_3_puzzle_button_idle.png"

image vb3_cp2_icon_1 = "images/vin battle 3/vb3_cp2_icon_1.png"
image vb3_cp2_icon_2 = "images/vin battle 3/vb3_cp2_icon_2.png"
image vb3_cp2_icon_3 = "images/vin battle 3/vb3_cp2_icon_3.png"
image vb3_cp2_icon_4 = "images/vin battle 3/vb3_cp2_icon_4.png"
image vb3_cp2_icon_5 = "images/vin battle 3/vb3_cp2_icon_5.png"
image vb3_cp2_icon_6 = "images/vin battle 3/vb3_cp2_icon_6.png"
image vb3_cp2_icon_7 = "images/vin battle 3/vb3_cp2_icon_7.png"
image vb3_cp2_icon_8 = "images/vin battle 3/vb3_cp2_icon_8.png"

screen vb3_cp2_screen:

    if vb3_cp2_icons[0] == 1:
        add "vb3_cp2_icon_1" xpos 262 ypos 80
    elif vb3_cp2_icons[0] == 2:
        add "vb3_cp2_icon_2" xpos 262 ypos 80
    elif vb3_cp2_icons[0] == 3:
        add "vb3_cp2_icon_3" xpos 262 ypos 80
    elif vb3_cp2_icons[0] == 4:
        add "vb3_cp2_icon_4" xpos 262 ypos 80
    elif vb3_cp2_icons[0] == 5:
        add "vb3_cp2_icon_5" xpos 262 ypos 80
    elif vb3_cp2_icons[0] == 6:
        add "vb3_cp2_icon_6" xpos 262 ypos 80
    elif vb3_cp2_icons[0] == 7:
        add "vb3_cp2_icon_7" xpos 262 ypos 80
    elif vb3_cp2_icons[0] == 8:
        add "vb3_cp2_icon_8" xpos 262 ypos 80

    if vb3_cp2_icons[1] == 1:
        add "vb3_cp2_icon_1" xpos 570 ypos 80
    elif vb3_cp2_icons[1] == 2:
        add "vb3_cp2_icon_2" xpos 570 ypos 80
    elif vb3_cp2_icons[1] == 3:
        add "vb3_cp2_icon_3" xpos 570 ypos 80
    elif vb3_cp2_icons[1] == 4:
        add "vb3_cp2_icon_4" xpos 570 ypos 80
    elif vb3_cp2_icons[1] == 5:
        add "vb3_cp2_icon_5" xpos 570 ypos 80
    elif vb3_cp2_icons[1] == 6:
        add "vb3_cp2_icon_6" xpos 570 ypos 80
    elif vb3_cp2_icons[1] == 7:
        add "vb3_cp2_icon_7" xpos 570 ypos 80
    elif vb3_cp2_icons[1] == 8:
        add "vb3_cp2_icon_8" xpos 570 ypos 80

    if vb3_cp2_icons[2] == 1:
        add "vb3_cp2_icon_1" xpos 862 ypos 80
    elif vb3_cp2_icons[2] == 2:
        add "vb3_cp2_icon_2" xpos 862 ypos 80
    elif vb3_cp2_icons[2] == 3:
        add "vb3_cp2_icon_3" xpos 862 ypos 80
    elif vb3_cp2_icons[2] == 4:
        add "vb3_cp2_icon_4" xpos 862 ypos 80
    elif vb3_cp2_icons[2] == 5:
        add "vb3_cp2_icon_5" xpos 862 ypos 80
    elif vb3_cp2_icons[2] == 6:
        add "vb3_cp2_icon_6" xpos 862 ypos 80
    elif vb3_cp2_icons[2] == 7:
        add "vb3_cp2_icon_7" xpos 862 ypos 80
    elif vb3_cp2_icons[2] == 8:
        add "vb3_cp2_icon_8" xpos 862 ypos 80

    imagebutton:
        xpos 1030
        ypos 620
        idle "images/basement/basement_door_arrow_down_idle.png"
        hover "images/tunnel/myers_tunnel_door_arrow_down_hover.png"
        focus_mask "images/basement/basement_door_arrow_down_idle.png"
        action Jump("vb3_cp2_leave")

    imagebutton:
        xpos 295
        ypos 583
        idle "images/Engineering Room 1/Engineering_room_3_puzzle_button_idle.png"
        hover "images/Engineering Room 1/Engineering_room_3_puzzle_button_hover.png"
        focus_mask "images/Engineering Room 1/Engineering_room_3_puzzle_button_hover.png"
        action Call("vb3_cp2_manipulate", 0)

    imagebutton:
        xpos 600
        ypos 583
        idle "images/Engineering Room 1/Engineering_room_3_puzzle_button_idle.png"
        hover "images/Engineering Room 1/Engineering_room_3_puzzle_button_hover.png"
        focus_mask "images/Engineering Room 1/Engineering_room_3_puzzle_button_hover.png"
        action Call("vb3_cp2_manipulate", 1)

    imagebutton:
        xpos 900
        ypos 583
        idle "images/Engineering Room 1/Engineering_room_3_puzzle_button_idle.png"
        hover "images/Engineering Room 1/Engineering_room_3_puzzle_button_hover.png"
        focus_mask "images/Engineering Room 1/Engineering_room_3_puzzle_button_hover.png"
        action Call("vb3_cp2_manipulate", 2)

    imagebutton:
        xpos 200
        ypos 511
        idle "images/vin battle 3/vb3_cp2_enter_idle.png"
        hover "images/vin battle 3/vb3_cp2_enter_hover.png"
        action Jump("vb3_cp2_check")

label vb3_cp2_start:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show black:
        alpha 0.6
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    show vb3_cp2_zoom_base
    call screen vb3_cp2_screen with Dissolve(0.2)

label vb3_cp2_leave:

    hide vb3_cp2_b1
    hide vb3_cp2_b2
    hide vb3_cp2_b3
    hide vb3_cp2_zoom_base
    $ renpy.pause(0.01, hard='True')

    hide black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    call screen vin_bat_3_3_screen

label vb3_cp2_manipulate(vb3_cp2_num):

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound ("music/passcode beep.ogg")

    if vb3_cp2_icons[vb3_cp2_num] < 8:
        $ vb3_cp2_icons[vb3_cp2_num] += 1
    else:
        $ vb3_cp2_icons[vb3_cp2_num] = 1
    $ renpy.pop_call()

    call screen vb3_cp2_screen

label vb3_cp2_check:

    $ vb3_cp2_ans = [5, 7, 2]

    python:
        for x in range(3):
            if vb3_cp2_icons[x] != vb3_cp2_ans[x]:
                renpy.music.set_volume(0.7, delay=0, channel='sound')
                renpy.music.play("music/tech interface.ogg", channel="sound", loop = False)
                renpy.call_screen("vb3_cp2_screen")

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/weapon click.ogg"

    show vb3_cp2_button as vb3_cp2_b1:
        xpos 295 ypos 583
    show vb3_cp2_button as vb3_cp2_b2:
        xpos 600 ypos 583
    show vb3_cp2_button as vb3_cp2_b3:
        xpos 900 ypos 583

    show vb3_cp2_icon_5:
        xpos 262 ypos 80
    show vb3_cp2_icon_7:
        xpos 570 ypos 80
    show vb3_cp2_icon_2:
        xpos 862 ypos 80

    $ renpy.pause(1.0, hard='True')

    hide vb3_cp2_b1
    hide vb3_cp2_b2
    hide vb3_cp2_b3
    hide vb3_cp2_zoom_base
    hide vb3_cp2_icon_5
    hide vb3_cp2_icon_7
    hide vb3_cp2_icon_2
    hide black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(1.0, hard='True')

    jump vin_bat_3_vin_start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
