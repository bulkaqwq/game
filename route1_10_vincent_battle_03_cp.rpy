
image vb3_cp_zoom_base:
    contains:
        "images/vin battle 3/vb3_cp_zoom_0.png"
    contains:
        Text(_("{size=+30}{font=impact.ttf}ENTER{/font}{/size}"))
        xalign 0.5 ypos 625 yanchor 0.5
    contains:
        ConditionSwitch("vb3_cp_buttons[0] == 0", "images/vin battle 3/vb3_cp_zoom_1.png", "vb3_cp_buttons[0] == 1", "images/vin battle 3/vb3_cp_zoom_2.png")
        xpos 380 ypos 53
    contains:
        ConditionSwitch("vb3_cp_buttons[1] == 0", "images/vin battle 3/vb3_cp_zoom_1.png", "vb3_cp_buttons[1] == 1", "images/vin battle 3/vb3_cp_zoom_2.png")
        xpos 560 ypos 53
    contains:
        ConditionSwitch("vb3_cp_buttons[2] == 0", "images/vin battle 3/vb3_cp_zoom_1.png", "vb3_cp_buttons[2] == 1", "images/vin battle 3/vb3_cp_zoom_2.png")
        xpos 740 ypos 53
    contains:
        ConditionSwitch("vb3_cp_buttons[3] == 0", "images/vin battle 3/vb3_cp_zoom_1.png", "vb3_cp_buttons[3] == 1", "images/vin battle 3/vb3_cp_zoom_2.png")
        xpos 380 ypos 232
    contains:
        ConditionSwitch("vb3_cp_buttons[4] == 0", "images/vin battle 3/vb3_cp_zoom_1.png", "vb3_cp_buttons[4] == 1", "images/vin battle 3/vb3_cp_zoom_2.png")
        xpos 560 ypos 232
    contains:
        ConditionSwitch("vb3_cp_buttons[5] == 0", "images/vin battle 3/vb3_cp_zoom_1.png", "vb3_cp_buttons[5] == 1", "images/vin battle 3/vb3_cp_zoom_2.png")
        xpos 740 ypos 232
    contains:
        ConditionSwitch("vb3_cp_buttons[6] == 0", "images/vin battle 3/vb3_cp_zoom_1.png", "vb3_cp_buttons[6] == 1", "images/vin battle 3/vb3_cp_zoom_2.png")
        xpos 380 ypos 410
    contains:
        ConditionSwitch("vb3_cp_buttons[7] == 0", "images/vin battle 3/vb3_cp_zoom_1.png", "vb3_cp_buttons[7] == 1", "images/vin battle 3/vb3_cp_zoom_2.png")
        xpos 560 ypos 410
    contains:
        ConditionSwitch("vb3_cp_buttons[8] == 0", "images/vin battle 3/vb3_cp_zoom_1.png", "vb3_cp_buttons[8] == 1", "images/vin battle 3/vb3_cp_zoom_2.png")
        xpos 740 ypos 410

image vb3_cp_zoom_1 = "images/vin battle 3/vb3_cp_zoom_1.png"
image vb3_cp_zoom_2 = "images/vin battle 3/vb3_cp_zoom_2.png"

screen vb3_cp_screen:

    imagebutton:
        xpos 970
        ypos 620
        idle "images/basement/basement_door_arrow_down_idle.png"
        hover "images/tunnel/myers_tunnel_door_arrow_down_hover.png"
        focus_mask "images/basement/basement_door_arrow_down_idle.png"
        action Jump("vb3_cp_leave")

    imagebutton:
        xpos 380
        ypos 590
        idle "images/vin battle 3/vb3_cp_enter_idle.png"
        hover "images/vin battle 3/vb3_cp_enter_hover.png"
        focus_mask "images/vin battle 3/vb3_cp_enter_hover.png"
        action Jump("vb3_cp_check")

    imagebutton:
        xpos 380
        ypos 53
        idle "images/vin battle 3/vb3_cp_button_idle.png"
        hover "images/vin battle 3/vb3_cp_button_hover.png"
        focus_mask "images/vin battle 3/vb3_cp_button_hover.png"
        action Call("vb3_cp_manipulate", 0)

    imagebutton:
        xpos 560
        ypos 53
        idle "images/vin battle 3/vb3_cp_button_idle.png"
        hover "images/vin battle 3/vb3_cp_button_hover.png"
        focus_mask "images/vin battle 3/vb3_cp_button_hover.png"
        action Call("vb3_cp_manipulate", 1)

    imagebutton:
        xpos 740
        ypos 53
        idle "images/vin battle 3/vb3_cp_button_idle.png"
        hover "images/vin battle 3/vb3_cp_button_hover.png"
        focus_mask "images/vin battle 3/vb3_cp_button_hover.png"
        action Call("vb3_cp_manipulate", 2)

    imagebutton:
        xpos 380
        ypos 232
        idle "images/vin battle 3/vb3_cp_button_idle.png"
        hover "images/vin battle 3/vb3_cp_button_hover.png"
        focus_mask "images/vin battle 3/vb3_cp_button_hover.png"
        action Call("vb3_cp_manipulate", 3)

    imagebutton:
        xpos 560
        ypos 232
        idle "images/vin battle 3/vb3_cp_button_idle.png"
        hover "images/vin battle 3/vb3_cp_button_hover.png"
        focus_mask "images/vin battle 3/vb3_cp_button_hover.png"
        action Call("vb3_cp_manipulate", 4)

    imagebutton:
        xpos 740
        ypos 232
        idle "images/vin battle 3/vb3_cp_button_idle.png"
        hover "images/vin battle 3/vb3_cp_button_hover.png"
        focus_mask "images/vin battle 3/vb3_cp_button_hover.png"
        action Call("vb3_cp_manipulate", 5)

    imagebutton:
        xpos 380
        ypos 410
        idle "images/vin battle 3/vb3_cp_button_idle.png"
        hover "images/vin battle 3/vb3_cp_button_hover.png"
        focus_mask "images/vin battle 3/vb3_cp_button_hover.png"
        action Call("vb3_cp_manipulate", 6)

    imagebutton:
        xpos 560
        ypos 410
        idle "images/vin battle 3/vb3_cp_button_idle.png"
        hover "images/vin battle 3/vb3_cp_button_hover.png"
        focus_mask "images/vin battle 3/vb3_cp_button_hover.png"
        action Call("vb3_cp_manipulate", 7)

    imagebutton:
        xpos 740
        ypos 410
        idle "images/vin battle 3/vb3_cp_button_idle.png"
        hover "images/vin battle 3/vb3_cp_button_hover.png"
        focus_mask "images/vin battle 3/vb3_cp_button_hover.png"
        action Call("vb3_cp_manipulate", 8)

label vb3_cp_start:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show black:
        alpha 0
        linear 0.5 alpha 0.5

    show vb3_cp_zoom_base:
        yoffset 3000
        ease 0.5 yoffset 0

    $ renpy.pause(0.5, hard='True')

    call screen vb3_cp_screen

label vb3_cp_leave:

    show black:
        alpha 0.5
        linear 0.5 alpha 0

    show vb3_cp_zoom_base:
        yoffset 0
        ease 0.5 yoffset -3000
    $ renpy.pause(0.5, hard='True')

    hide black
    hide vb3_cp_zoom_base

    call screen vin_bat_3_2_screen

label vb3_cp_manipulate(vb3_cp_button):

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound ("music/passcode beep.ogg")

    if vb3_cp_buttons[vb3_cp_button] == 0:
        $ vb3_cp_buttons[vb3_cp_button] = 1
    else:
        $ vb3_cp_buttons[vb3_cp_button] = 0

    hide vb3_cp_zoom_base
    show vb3_cp_zoom_base

    $ renpy.pop_call()

    call screen vb3_cp_screen

label vb3_cp_check:

    $ vb3_cp_ans = [0, 4, 5, 6, 7]

    python:


        vb3_cp_sum = 0
        for x in range(len(vb3_cp_buttons)):
            vb3_cp_sum = vb3_cp_sum + vb3_cp_buttons[x]
        if vb3_cp_sum != 5:
            renpy.music.set_volume(0.7, delay=0, channel='sound')
            renpy.music.play("music/tech interface.ogg", channel="sound", loop = False)
            vb3_cp_buttons = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            renpy.hide("vb3_cp_zoom_base")
            renpy.show("vb3_cp_zoom_base")
            renpy.call_screen("vb3_cp_screen")

        for x in range(5):
            if vb3_cp_buttons[vb3_cp_ans[x]] != 1:
                renpy.music.set_volume(0.7, delay=0, channel='sound')
                renpy.music.play("music/tech interface.ogg", channel="sound", loop = False)
                vb3_cp_buttons = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                renpy.hide("vb3_cp_zoom_base")
                renpy.show("vb3_cp_zoom_base")
                renpy.call_screen("vb3_cp_screen")

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/weapon click.ogg"
    $ renpy.pause(1.0, hard='True')

    $ vb3_solve_cp = True

    show black:
        alpha 0.5
        linear 0.5 alpha 0

    show vb3_cp_zoom_base:
        yoffset 0
        ease 0.5 yoffset -3000
    $ renpy.pause(0.5, hard='True')

    hide black
    hide vb3_cp_zoom_base

    $ renpy.pause(0.5, hard='True')

    scene black
    show vin_bat_1_3_3
    show vin_bat_3_3_1
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(1.0, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/engineering room/door accept beep.ogg"

    show vin_bat_3_3_2
    $ renpy.transition(Dissolve(0.2))
    $ renpy.pause(1.2, hard='True')

    scene vin_bat_3_2
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard=True)

    call screen vin_bat_3_2_screen
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
