
image vb2_cp_zoom:
    contains:
        "images/vin battle 2/vb2_cp_zoom.png"
    contains:
        ConditionSwitch("vb2_cp_num_code > 0", "images/vin battle 2/vb2_cp_rec.png", "vb2_cp_num_code <= 0", "images/empty.png")
        xpos 723 ypos 260
    contains:
        ConditionSwitch("vb2_cp_num_code > 1", "images/vin battle 2/vb2_cp_rec.png", "vb2_cp_num_code <= 1", "images/empty.png")
        xpos 810 ypos 260
    contains:
        ConditionSwitch("vb2_cp_num_code > 2", "images/vin battle 2/vb2_cp_rec.png", "vb2_cp_num_code <= 2", "images/empty.png")
        xpos 898 ypos 260
    contains:
        ConditionSwitch("vb2_cp_num_code > 3", "images/vin battle 2/vb2_cp_rec.png", "vb2_cp_num_code <= 3", "images/empty.png")
        xpos 986 ypos 260

screen vb2_cp_screen:

    imagebutton:
        xpos 520
        ypos 610
        idle "images/basement/basement_door_arrow_down_idle.png"
        hover "images/tunnel/myers_tunnel_door_arrow_down_hover.png"
        focus_mask "images/basement/basement_door_arrow_down_idle.png"
        action Jump("vb2_cp_leave")

    imagebutton:
        xpos 170
        ypos 81
        idle "images/vin battle 2/vb2_cp_button_idle.png"
        hover "images/vin battle 2/vb2_cp_button_hover.png"
        focus_mask "images/vin battle 2/vb2_cp_button_hover.png"
        action Call("vb2_cp_manipulate",1)

    imagebutton:
        xpos 330
        ypos 81
        idle "images/vin battle 2/vb2_cp_button_idle.png"
        hover "images/vin battle 2/vb2_cp_button_hover.png"
        focus_mask "images/vin battle 2/vb2_cp_button_hover.png"
        action Call("vb2_cp_manipulate",2)

    imagebutton:
        xpos 491
        ypos 81
        idle "images/vin battle 2/vb2_cp_button_idle.png"
        hover "images/vin battle 2/vb2_cp_button_hover.png"
        focus_mask "images/vin battle 2/vb2_cp_button_hover.png"
        action Call("vb2_cp_manipulate",3)

    imagebutton:
        xpos 170
        ypos 241
        idle "images/vin battle 2/vb2_cp_button_idle.png"
        hover "images/vin battle 2/vb2_cp_button_hover.png"
        focus_mask "images/vin battle 2/vb2_cp_button_hover.png"
        action Call("vb2_cp_manipulate",4)

    imagebutton:
        xpos 330
        ypos 241
        idle "images/vin battle 2/vb2_cp_button_idle.png"
        hover "images/vin battle 2/vb2_cp_button_hover.png"
        focus_mask "images/vin battle 2/vb2_cp_button_hover.png"
        action Call("vb2_cp_manipulate",5)

    imagebutton:
        xpos 491
        ypos 241
        idle "images/vin battle 2/vb2_cp_button_idle.png"
        hover "images/vin battle 2/vb2_cp_button_hover.png"
        focus_mask "images/vin battle 2/vb2_cp_button_hover.png"
        action Call("vb2_cp_manipulate",6)

    imagebutton:
        xpos 170
        ypos 400
        idle "images/vin battle 2/vb2_cp_button_idle.png"
        hover "images/vin battle 2/vb2_cp_button_hover.png"
        focus_mask "images/vin battle 2/vb2_cp_button_hover.png"
        action Jump("vb2_cp_delete_num")

    imagebutton:
        xpos 330
        ypos 400
        idle "images/vin battle 2/vb2_cp_button_idle.png"
        hover "images/vin battle 2/vb2_cp_button_hover.png"
        focus_mask "images/vin battle 2/vb2_cp_button_hover.png"
        action Call("vb2_cp_manipulate",7)

    imagebutton:
        xpos 491
        ypos 400
        idle "images/vin battle 2/vb2_cp_button_idle.png"
        hover "images/vin battle 2/vb2_cp_button_hover.png"
        focus_mask "images/vin battle 2/vb2_cp_button_hover.png"
        action Jump("vb2_cp_check_answer")

label vb2_cp_manipulate(vb2_cp_button):

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound ("music/passcode beep.ogg")

    if vb2_cp_num_code < 4:
        $ vb2_cp_cur_code.append(vb2_cp_button)
        $ vb2_cp_num_code = vb2_cp_num_code + 1

    $ renpy.pop_call()

    call screen vb2_cp_screen

label vb2_cp_delete_num:

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound ("music/passcode beep.ogg")

    if vb2_cp_num_code > 0:
        $ vb2_cp_num_code = vb2_cp_num_code - 1
        $ del vb2_cp_cur_code[-1]

    call screen vb2_cp_screen

label vb2_cp_check_answer:

    $ vb2_cp_correct_code = [7,2,4,5]

    python:

        if len(vb2_cp_cur_code) != 4:
            renpy.jump("vb2_cp_fail")

        for x in range(4):
            if vb2_cp_cur_code[x] != vb2_cp_correct_code[x]:
                renpy.jump("vb2_cp_fail")

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/weapon click.ogg"
    $ renpy.pause(1.0, hard='True')

    $ vb2_solve_cp = True

    show vin_bat_2_2 behind black

    show black:
        alpha 0.5
        linear 0.5 alpha 0

    show vb2_cp_zoom:
        yoffset 0
        ease 0.5 yoffset -3000
    $ renpy.pause(0.5, hard='True')

    hide black
    hide vb2_cp_zoom

    $ renpy.pause(0.5, hard='True')

    scene black
    show vin_bat_1_3_3
    show vin_bat_2_3_1
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(1.0, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/engineering room/door accept beep.ogg"

    show vin_bat_2_3_2
    $ renpy.transition(Dissolve(0.2))
    $ renpy.pause(1.2, hard='True')

    scene vin_bat_2_2
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard=True)

    call screen vin_bat_2_2_screen

label vb2_cp_fail:

    $ vb2_cp_cur_code.clear()
    $ vb2_cp_num_code = 0

    $ renpy.music.set_volume(0.7, delay=0, channel='sound')
    play sound "music/tech interface.ogg"
    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 0.5, dist=15))
    $ renpy.pause(0.5, hard='True')

    call screen vb2_cp_screen
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
