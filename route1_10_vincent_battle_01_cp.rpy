
image vin_bat_1_tv_dis_1 = "images/vin battle 1/vin_bat_1_tv_dis_1.png"
image vin_bat_1_tv_dis_2 = "images/vin battle 1/vin_bat_1_tv_dis_2.png"
image vin_bat_1_tv_dis_3 = "images/vin battle 1/vin_bat_1_tv_dis_3.png"


image vin_bat_1_tv_s_1 = "images/vin battle 1/vin_bat_1_tv_s_1.png"
image vin_bat_1_tv_s_2 = "images/vin battle 1/vin_bat_1_tv_s_2.png"
image vin_bat_1_tv_s_3 = "images/vin battle 1/vin_bat_1_tv_s_3.png"

image vin_bat_1_cp_zoom_plus:
    contains:
        "images/vin battle 1/vin_bat_1_cp_1.png"
    contains:
        "images/vin battle 1/vin_bat_1_cp_2.png"
    contains:
        Text("{size=+90}{color=#1F9F2D}{font=VHS.ttf}57{/font}{/color}{/size}")
        xpos 760 ypos 80 xanchor 0.5
    contains:
        Text("{size=+90}{color=#1F9F2D}{font=VHS.ttf}[vin_bat_1_plus_display]{/font}{/color}{/size}")
        xpos 495 ypos 80 xanchor 0.5
    contains:
        Text("{size=+90}{color=#000000}{font=VHS.ttf}7{/font}{/color}{/size}")
        xpos 556 ypos 405 xanchor 0.5
    contains:
        Text("{size=+90}{color=#000000}{font=VHS.ttf}9{/font}{/color}{/size}")
        xpos 698 ypos 405 xanchor 0.5
    contains:
        Text("{size=+90}{color=#000000}{font=VHS.ttf}1{/font}{/color}{/size}")
        xpos 556 ypos 265 xanchor 0.5
    contains:
        Text("{size=+90}{color=#000000}{font=VHS.ttf}5{/font}{/color}{/size}")
        xpos 698 ypos 265 xanchor 0.5
    contains:
        ConditionSwitch("vin_bat_1_plus_click > 0", "images/vin battle 1/vin_bat_1_cp_light_1.png", "vin_bat_1_plus_click <= 0", "images/empty.png")
    contains:
        ConditionSwitch("vin_bat_1_plus_click > 1", "images/vin battle 1/vin_bat_1_cp_light_2.png", "vin_bat_1_plus_click <= 1", "images/empty.png")
    contains:
        ConditionSwitch("vin_bat_1_plus_click > 2", "images/vin battle 1/vin_bat_1_cp_light_3.png", "vin_bat_1_plus_click <= 2", "images/empty.png")
    contains:
        ConditionSwitch("vin_bat_1_plus_click > 3", "images/vin battle 1/vin_bat_1_cp_light_4.png", "vin_bat_1_plus_click <= 3", "images/empty.png")
    contains:
        ConditionSwitch("vin_bat_1_plus_click > 4", "images/vin battle 1/vin_bat_1_cp_light_5.png", "vin_bat_1_plus_click <= 4", "images/empty.png")
    contains:
        ConditionSwitch("vin_bat_1_plus_click > 5", "images/vin battle 1/vin_bat_1_cp_light_6.png", "vin_bat_1_plus_click <= 5", "images/empty.png")
    contains:
        ConditionSwitch("vin_bat_1_plus_click > 6", "images/vin battle 1/vin_bat_1_cp_light_7.png", "vin_bat_1_plus_click <= 6", "images/empty.png")
    contains:
        ConditionSwitch("vin_bat_1_plus_click > 7", "images/vin battle 1/vin_bat_1_cp_light_8.png", "vin_bat_1_plus_click <= 7", "images/empty.png")
    contains:
        ConditionSwitch("vin_bat_1_plus_click > 8", "images/vin battle 1/vin_bat_1_cp_light_9.png", "vin_bat_1_plus_click <= 8", "images/empty.png")

image vin_bat_1_cp_zoom_minus:
    contains:
        "images/vin battle 1/vin_bat_1_cp_1.png"
    contains:
        Text("{size=+90}{color=#1F9F2D}{font=VHS.ttf}05{/font}{/color}{/size}")
        xpos 760 ypos 80 xanchor 0.5
    contains:
        Text("{size=+90}{color=#1F9F2D}{font=VHS.ttf}[vin_bat_1_minus_display]{/font}{/color}{/size}")
        xpos 495 ypos 80 xanchor 0.5
    contains:
        Text("{size=+90}{color=#000000}{font=VHS.ttf}8{/font}{/color}{/size}")
        xpos 556 ypos 405 xanchor 0.5
    contains:
        Text("{size=+90}{color=#000000}{font=VHS.ttf}9{/font}{/color}{/size}")
        xpos 698 ypos 405 xanchor 0.5
    contains:
        Text("{size=+90}{color=#000000}{font=VHS.ttf}2{/font}{/color}{/size}")
        xpos 556 ypos 265 xanchor 0.5
    contains:
        Text("{size=+90}{color=#000000}{font=VHS.ttf}3{/font}{/color}{/size}")
        xpos 698 ypos 265 xanchor 0.5
    contains:
        ConditionSwitch("vin_bat_1_minus_click > 0", "images/vin battle 1/vin_bat_1_cp_light_1.png", "vin_bat_1_minus_click <= 0", "images/empty.png")
    contains:
        ConditionSwitch("vin_bat_1_minus_click > 1", "images/vin battle 1/vin_bat_1_cp_light_2.png", "vin_bat_1_minus_click <= 1", "images/empty.png")
    contains:
        ConditionSwitch("vin_bat_1_minus_click > 2", "images/vin battle 1/vin_bat_1_cp_light_3.png", "vin_bat_1_minus_click <= 2", "images/empty.png")
    contains:
        ConditionSwitch("vin_bat_1_minus_click > 3", "images/vin battle 1/vin_bat_1_cp_light_4.png", "vin_bat_1_minus_click <= 3", "images/empty.png")
    contains:
        ConditionSwitch("vin_bat_1_minus_click > 4", "images/vin battle 1/vin_bat_1_cp_light_5.png", "vin_bat_1_minus_click <= 4", "images/empty.png")
    contains:
        ConditionSwitch("vin_bat_1_minus_click > 5", "images/vin battle 1/vin_bat_1_cp_light_6.png", "vin_bat_1_minus_click <= 5", "images/empty.png")
    contains:
        ConditionSwitch("vin_bat_1_minus_click > 6", "images/vin battle 1/vin_bat_1_cp_light_7.png", "vin_bat_1_minus_click <= 6", "images/empty.png")
    contains:
        ConditionSwitch("vin_bat_1_minus_click > 7", "images/vin battle 1/vin_bat_1_cp_light_8.png", "vin_bat_1_minus_click <= 7", "images/empty.png")
    contains:
        ConditionSwitch("vin_bat_1_minus_click > 8", "images/vin battle 1/vin_bat_1_cp_light_9.png", "vin_bat_1_minus_click <= 8", "images/empty.png")


screen vin_bat_1_cp_plus_screen:

    imagebutton:
        xpos 520
        ypos 610
        idle "images/basement/basement_door_arrow_down_idle.png"
        hover "images/tunnel/myers_tunnel_door_arrow_down_hover.png"
        focus_mask "images/basement/basement_door_arrow_down_idle.png"
        action Jump("vin_bat_1_cp_plus_leave")

    imagebutton:
        xpos 489
        ypos 257
        idle "images/vin battle 1/vin_bat_1_cp_button_idle.png"
        hover "images/vin battle 1/vin_bat_1_cp_button_hover.png"
        focus_mask "images/vin battle 1/vin_bat_1_cp_button_hover.png"
        action Call("vin_bat_1_cp_plus_manipulation", vin_bat_1_plus_num, 1)

    imagebutton:
        xpos 632
        ypos 257
        idle "images/vin battle 1/vin_bat_1_cp_button_idle.png"
        hover "images/vin battle 1/vin_bat_1_cp_button_hover.png"
        focus_mask "images/vin battle 1/vin_bat_1_cp_button_hover.png"
        action Call("vin_bat_1_cp_plus_manipulation", vin_bat_1_plus_num, 5)

    imagebutton:
        xpos 489
        ypos 397
        idle "images/vin battle 1/vin_bat_1_cp_button_idle.png"
        hover "images/vin battle 1/vin_bat_1_cp_button_hover.png"
        focus_mask "images/vin battle 1/vin_bat_1_cp_button_hover.png"
        action Call("vin_bat_1_cp_plus_manipulation", vin_bat_1_plus_num, 7)

    imagebutton:
        xpos 632
        ypos 397
        idle "images/vin battle 1/vin_bat_1_cp_button_idle.png"
        hover "images/vin battle 1/vin_bat_1_cp_button_hover.png"
        focus_mask "images/vin battle 1/vin_bat_1_cp_button_hover.png"
        action Call("vin_bat_1_cp_plus_manipulation", vin_bat_1_plus_num, 9)


screen vin_bat_1_cp_minus_screen:

    imagebutton:
        xpos 520
        ypos 610
        idle "images/basement/basement_door_arrow_down_idle.png"
        hover "images/tunnel/myers_tunnel_door_arrow_down_hover.png"
        focus_mask "images/basement/basement_door_arrow_down_idle.png"
        action Jump("vin_bat_1_cp_minus_leave")

    imagebutton:
        xpos 489
        ypos 257
        idle "images/vin battle 1/vin_bat_1_cp_button_idle.png"
        hover "images/vin battle 1/vin_bat_1_cp_button_hover.png"
        focus_mask "images/vin battle 1/vin_bat_1_cp_button_hover.png"
        action Call("vin_bat_1_cp_minus_manipulation", vin_bat_1_minus_num, 2)

    imagebutton:
        xpos 632
        ypos 257
        idle "images/vin battle 1/vin_bat_1_cp_button_idle.png"
        hover "images/vin battle 1/vin_bat_1_cp_button_hover.png"
        focus_mask "images/vin battle 1/vin_bat_1_cp_button_hover.png"
        action Call("vin_bat_1_cp_minus_manipulation", vin_bat_1_minus_num, 3)

    imagebutton:
        xpos 489
        ypos 397
        idle "images/vin battle 1/vin_bat_1_cp_button_idle.png"
        hover "images/vin battle 1/vin_bat_1_cp_button_hover.png"
        focus_mask "images/vin battle 1/vin_bat_1_cp_button_hover.png"
        action Call("vin_bat_1_cp_minus_manipulation", vin_bat_1_minus_num, 8)

    imagebutton:
        xpos 632
        ypos 397
        idle "images/vin battle 1/vin_bat_1_cp_button_idle.png"
        hover "images/vin battle 1/vin_bat_1_cp_button_hover.png"
        focus_mask "images/vin battle 1/vin_bat_1_cp_button_hover.png"
        action Call("vin_bat_1_cp_minus_manipulation", vin_bat_1_minus_num, 9)


label vin_bat_1_cp_plus_manipulation(vin_bat_1_cp_current_num, vin_bat_1_cp_add_num):

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound ("music/passcode beep.ogg")

    python:
        vin_bat_1_plus_num = vin_bat_1_cp_current_num + vin_bat_1_cp_add_num
        vin_bat_1_plus_display = str(vin_bat_1_plus_num).zfill(2)
        vin_bat_1_plus_click += 1
        renpy.pop_call()

    hide vin_bat_1_cp_zoom_plus
    show vin_bat_1_cp_zoom_plus

    if vin_bat_1_plus_click == 9:
        $ renpy.pause(0.2, hard='True')

        if vin_bat_1_plus_num != 57:
            $ renpy.music.set_volume(0.7, delay=0, channel='sound')
            play sound "music/tech interface.ogg"
            $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 0.5, dist=15))
            $ renpy.pause(0.5, hard='True')
            $ vin_bat_1_plus_num = 4
            $ vin_bat_1_plus_display = str(vin_bat_1_plus_num).zfill(2)
            $ vin_bat_1_plus_click = 0


            hide vin_bat_1_cp_zoom_plus
            show vin_bat_1_cp_zoom_plus
        else:

            $ renpy.music.set_volume(0.6, delay=0, channel='sound')
            play sound "music/weapon click.ogg"
            $ renpy.pause(1.0, hard='True')
            $ vin_bat_1_solve_plus = True

            show black:
                alpha 0.6
                linear 0.5 alpha 0

            show vin_bat_1_cp_zoom_plus:
                yoffset 0
                ease 0.5 yoffset -3000
            $ renpy.pause(0.5, hard='True')

            hide black
            hide vin_bat_1_cp_zoom_plus

            hide vin_bat_1_2
            show vin_bat_1_2

            if not (vin_bat_1_solve_plus and vin_bat_1_solve_minus):

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

                dra "\"Excellent job, {w=0.5}Vanora! {w=0.5}Just one more to go!\""

                hide character_icon_box_1
                hide draco_icon_blood_serious
                hide character_icon_box_2
                with Dissolve(0.3)
            else:


                jump vin_bat_1_cp_finished

            call screen vin_bat_1_2_screen with Dissolve(0.2)

    call screen vin_bat_1_cp_plus_screen

label vin_bat_1_cp_minus_manipulation(vin_bat_1_cp_current_num, vin_bat_1_cp_minus_num):

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound ("music/passcode beep.ogg")

    python:
        vin_bat_1_minus_num = vin_bat_1_cp_current_num - vin_bat_1_cp_minus_num
        vin_bat_1_minus_display = str(vin_bat_1_minus_num).zfill(2)
        vin_bat_1_minus_click += 1
        renpy.pop_call()

    hide vin_bat_1_cp_zoom_minus
    show vin_bat_1_cp_zoom_minus

    if vin_bat_1_minus_click == 9:
        $ renpy.pause(0.2, hard='True')

        if vin_bat_1_minus_num != 5:
            $ renpy.music.set_volume(0.7, delay=0, channel='sound')
            play sound "music/tech interface.ogg"
            $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 0.5, dist=15))
            $ renpy.pause(0.5, hard='True')
            $ vin_bat_1_minus_num = 79
            $ vin_bat_1_minus_display = str(vin_bat_1_minus_num).zfill(2)
            $ vin_bat_1_minus_click = 0


            hide vin_bat_1_cp_zoom_minus
            show vin_bat_1_cp_zoom_minus
        else:

            $ renpy.music.set_volume(0.6, delay=0, channel='sound')
            play sound "music/weapon click.ogg"
            $ renpy.pause(1.0, hard='True')
            $ vin_bat_1_solve_minus = True

            show black:
                alpha 0.4
                linear 0.5 alpha 0

            show vin_bat_1_cp_zoom_minus:
                yoffset 0
                ease 0.5 yoffset -3000
            $ renpy.pause(0.5, hard='True')

            hide black
            hide vin_bat_1_cp_zoom_minus

            hide vin_bat_1_2
            show vin_bat_1_2

            if not (vin_bat_1_solve_plus and vin_bat_1_solve_minus):

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

                dra "\"Excellent job, {w=0.5}Vanora! {w=0.5}Just one more to go!\""

                hide character_icon_box_1
                hide draco_icon_blood_serious
                hide character_icon_box_2
                with Dissolve(0.3)
            else:


                jump vin_bat_1_cp_finished

            call screen vin_bat_1_2_screen with Dissolve(0.2)

    call screen vin_bat_1_cp_minus_screen

label vin_bat_1_cp_finished:

    $ renpy.music.set_volume(0.8, delay=0, channel='vhs')
    $ renpy.music.play("music/insert vhs.ogg", channel="vhs", loop=False)

    $ renpy.pause(1.0, hard='True')

    scene black
    show vin_bat_1_3_2
    show vin_bat_1_3_3
    show vin_bat_1_3_1
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    show white back behind vin_bat_1_3_3:
        alpha 0.7 xoffset 500
    show game_over_static behind vin_bat_1_3_3:
        alpha 0.5 zoom 0.5 xoffset 500 yoffset 120
    show bad_tv_signal behind vin_bat_1_3_3:
        zoom 0.5 xoffset 500 yoffset 110
    $ renpy.transition(Dissolve(0.2))
    $ renpy.pause(1.0, hard='True')

    $ renpy.music.set_volume(0.7, delay=0, channel='background noise')
    $ renpy.music.play("music/basement/zs_loud_glitch.ogg", channel="background noise", loop=False)

    show vin_bat_1_tv_dis_1 as vin_bat_1_tv_dis_1_2 behind bad_tv_signal:
        alpha 0.5
        linear 0.1 yoffset -20
        linear 0.1 yoffset 20
        repeat
    show vin_bat_1_tv_dis_1 behind bad_tv_signal:
        alpha 0.5
        linear 0.1 yoffset 20
        linear 0.1 yoffset -20
        repeat
    $ renpy.transition(Dissolve(0.2))
    $ renpy.pause(1.0, hard='True')

    show vin_bat_1_tv_dis_3 as vin_bat_1_tv_dis_2_3 behind bad_tv_signal:
        alpha 0.5
        linear 0.1 yoffset -20
        linear 0.1 yoffset 20
        repeat
    show vin_bat_1_tv_dis_3 behind bad_tv_signal:
        alpha 0.5
        linear 0.1 yoffset 20
        linear 0.1 yoffset -20
        repeat
    hide vin_bat_1_tv_dis_1_2
    hide vin_bat_1_tv_dis_1
    $ renpy.transition(Dissolve(0.2))
    $ renpy.pause(1.0, hard='True')

    show vin_bat_1_tv_dis_2 as vin_bat_1_tv_dis_2_2 behind bad_tv_signal:
        alpha 0.5
        linear 0.1 yoffset -20
        linear 0.1 yoffset 20
        repeat
    show vin_bat_1_tv_dis_2 behind bad_tv_signal:
        alpha 0.5
        linear 0.1 yoffset 20
        linear 0.1 yoffset -20
        repeat
    hide vin_bat_1_tv_dis_3_2
    hide vin_bat_1_tv_dis_3
    $ renpy.transition(Dissolve(0.2))
    $ renpy.pause(1.0, hard='True')

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    $ renpy.music.play("music/KILLSWITCH.ogg", channel="sound", loop=False)

    show vin_bat_1_tv_s_2 behind bad_tv_signal
    $ renpy.transition(Dissolve(0.2))
    $ renpy.pause(0.4, hard='True')

    $ renpy.music.set_volume(0.8, delay=0, channel='sfx1')
    $ renpy.music.play("music/KILLSWITCH.ogg", channel="sfx1", loop=False)

    show vin_bat_1_tv_s_1 behind bad_tv_signal
    $ renpy.transition(Dissolve(0.2))
    $ renpy.pause(0.4, hard='True')

    $ renpy.music.set_volume(0.8, delay=0, channel='sfx2')
    $ renpy.music.play("music/KILLSWITCH.ogg", channel="sfx2", loop=False)

    show vin_bat_1_tv_s_4 behind bad_tv_signal
    $ renpy.transition(Dissolve(0.2))
    $ renpy.pause(0.4, hard='True')

    $ renpy.music.set_volume(0.8, delay=0, channel='sfx3_new')
    $ renpy.music.play("music/KILLSWITCH.ogg", channel="sfx3_new", loop=False)

    show vin_bat_1_tv_s_3 behind bad_tv_signal
    $ renpy.transition(Dissolve(0.2))
    $ renpy.pause(0.4, hard='True')

    $ vin_bat_1_solve_cp = True

    pause 1.0

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

    dra "\"Perfect! {w=0.5}Now all you have to do is match all the corresponding symbols on the screen!\""

    hide character_icon_box_1
    hide draco_icon_blood_serious
    hide character_icon_box_2
    with Dissolve(0.3)

    scene vin_bat_1_2
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    call screen vin_bat_1_2_screen with Dissolve(0.2)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
