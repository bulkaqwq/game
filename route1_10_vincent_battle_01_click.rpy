

screen vin_bat_1_1_screen:

    imagebutton:
        xpos 30
        ypos 560
        idle "images/basement/left-pink-arrow.png"
        hover "images/myers-click/left-white-arrow-small-small.png"
        focus_mask "images/myers-click/left-black-arrow-small-small.png"
        action Jump("vin_bat_1_1_to_3_switch")

    imagebutton:
        xpos 1030
        ypos 560
        idle "images/basement/right-pink-arrow.png"
        hover "images/myers-click/right-white-arrow-small-small.png"
        focus_mask "images/myers-click/right-black-arrow-small-small.png"
        action Jump("vin_bat_1_1_to_2_switch")

    imagebutton:
        xpos 441
        ypos 40
        idle "images/vin battle 1/vin_bat_1_speaker_idle.png"
        hover "images/vin battle 1/vin_bat_1_speaker_hover.png"
        focus_mask "images/vin battle 1/vin_bat_1_speaker_hover.png"
        action Jump("vin_bat_1_investigate_speaker")

    imagebutton:
        xpos 788
        ypos 97
        idle "images/vin battle 1/vin_bat_1_door_idle.png"
        hover "images/vin battle 1/vin_bat_1_door_hover.png"
        focus_mask "images/vin battle 1/vin_bat_1_door_hover.png"
        action Jump("vin_bat_1_investigate_back_door")

screen vin_bat_1_2_screen:

    imagebutton:
        xpos 30
        ypos 560
        idle "images/basement/left-pink-arrow.png"
        hover "images/myers-click/left-white-arrow-small-small.png"
        focus_mask "images/myers-click/left-black-arrow-small-small.png"
        action Jump("vin_bat_1_2_to_1_switch")

    imagebutton:
        xpos 1030
        ypos 560
        idle "images/basement/right-pink-arrow.png"
        hover "images/myers-click/right-white-arrow-small-small.png"
        focus_mask "images/myers-click/right-black-arrow-small-small.png"
        action Jump("vin_bat_1_2_to_3_switch")

    if not vin_bat_1_solve_plus:
        imagebutton:
            xpos 272
            ypos 144
            idle "images/vin battle 1/vin_bat_1_cp_idle.png"
            hover "images/vin battle 1/vin_bat_1_cp_hover.png"
            focus_mask "images/vin battle 1/vin_bat_1_cp_hover.png"
            action Jump("vin_bat_1_investigate_cp_plus")
    else:
        imagebutton:
            xpos 272
            ypos 144
            idle "images/vin battle 1/vin_bat_1_cp_idle.png"
            hover "images/vin battle 1/vin_bat_1_cp_hover.png"
            focus_mask "images/vin battle 1/vin_bat_1_cp_hover.png"
            action Jump("vin_bat_1_investigate_cp_solved")

    if not vin_bat_1_solve_minus:
        imagebutton:
            xpos 272
            ypos 295
            idle "images/vin battle 1/vin_bat_1_cp_idle.png"
            hover "images/vin battle 1/vin_bat_1_cp_hover.png"
            focus_mask "images/vin battle 1/vin_bat_1_cp_hover.png"
            action Jump("vin_bat_1_investigate_cp_minus")
    else:
        imagebutton:
            xpos 272
            ypos 295
            idle "images/vin battle 1/vin_bat_1_cp_idle.png"
            hover "images/vin battle 1/vin_bat_1_cp_hover.png"
            focus_mask "images/vin battle 1/vin_bat_1_cp_hover.png"
            action Jump("vin_bat_1_investigate_cp_solved")

screen vin_bat_1_3_screen:

    imagebutton:
        xpos 30
        ypos 560
        idle "images/basement/left-pink-arrow.png"
        hover "images/myers-click/left-white-arrow-small-small.png"
        focus_mask "images/myers-click/left-black-arrow-small-small.png"
        action Jump("vin_bat_1_3_to_2_switch")

    imagebutton:
        xpos 1030
        ypos 560
        idle "images/basement/right-pink-arrow.png"
        hover "images/myers-click/right-white-arrow-small-small.png"
        focus_mask "images/myers-click/right-black-arrow-small-small.png"
        action Jump("vin_bat_1_3_to_1_switch")

    imagebutton:
        xpos 178
        ypos 97
        idle "images/vin battle 1/vin_bat_1_door_idle.png"
        hover "images/vin battle 1/vin_bat_1_door_hover.png"
        focus_mask "images/vin battle 1/vin_bat_1_door_hover.png"
        action Jump("vin_bat_1_investigate_front_door")

    imagebutton:
        xpos 506
        ypos 111
        idle "images/vin battle 1/vin_bat_1_match_idle.png"
        hover "images/vin battle 1/vin_bat_1_match_hover.png"
        focus_mask "images/vin battle 1/vin_bat_1_match_hover.png"
        action Jump("vin_bat_1_investigate_match")

label vincent_battle_01_click_start:

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.block_rollback()
    $ _rollback = False


    $ vin_bat_1_solve_plus = False
    $ vin_bat_1_solve_minus = False
    $ vin_bat_1_solve_cp = False
    $ vin_bat_1_plus_num = 4
    $ vin_bat_1_inv_match = False
    $ vin_bat_1_shadow_van = False

    call screen vin_bat_1_1_screen with Dissolve(0.2)

label vin_bat_1_1_to_2_switch:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/scan map.ogg"

    $ renpy.music.stop(channel="background noise", fadeout = 1.0)

    scene black
    show vin_bat_1_1:
        alpha 1
        linear 0.3 xoffset -1280 alpha 0
    show vin_bat_1_2:
        xoffset 1280 alpha 0
        linear 0.3 xoffset 0 alpha 1
    $ renpy.pause(0.3, hard='True')

    scene vin_bat_1_2

    call screen vin_bat_1_2_screen

label vin_bat_1_1_to_3_switch:

    if vin_bat_1_solve_cp and not vin_bat_1_shadow_van:

        $ renpy.music.stop(channel="background noise", fadeout = 1.0)

        $ renpy.music.set_volume(1.0, delay=0, channel='sound')
        play sound "music/basement/vita_female_giggle.ogg"

        $ vin_bat_1_shadow_van = True
        scene black
        show game_over_static:
            linear 0.05 xoffset -70 yoffset 70
            linear 0.05 xoffset 70 yoffset -70
            linear 0.05 xoffset 0 yoffset 70
            linear 0.05 xoffset -70 yoffset -70
            linear 0.05 xoffset 0 yoffset 0
            repeat
        show basement_shadow_vanora:
            zoom 2.0 xalign 0.55 alpha 0.8 yoffset -10
            block:
                linear 0.05 xoffset -70 yoffset 70
                linear 0.05 xoffset 70 yoffset -70
                linear 0.05 xoffset 0 yoffset 70
                linear 0.05 xoffset -70 yoffset -70
                linear 0.05 xoffset 0 yoffset 0
                repeat
        $ renpy.pause(0.3, hard='True')

        scene vin_bat_1_3
        hide game_over_static
        hide basement_shadow_vanora
        $ renpy.transition(wipeLeft)
        $ renpy.pause(0.5, hard='True')
    else:


        $ renpy.music.set_volume(1.0, delay=0, channel='sound')
        play sound "music/scan map.ogg"

        $ renpy.music.stop(channel="background noise", fadeout = 1.0)

        scene black
        show vin_bat_1_1:
            alpha 1
            linear 0.3 xoffset 1280 alpha 0
        if vin_bat_1_solve_cp:
            show vin_bat_1_3:
                xoffset -1280 alpha 0
                linear 0.3 xoffset 0 alpha 1
        else:
            show vin_bat_1_3_0:
                xoffset -1280 alpha 0
                linear 0.3 xoffset 0 alpha 1
        $ renpy.pause(0.3, hard='True')

    call screen vin_bat_1_3_screen

label vin_bat_1_2_to_1_switch:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/scan map.ogg"

    $ renpy.music.set_volume(0.2, delay=0, channel='background noise')
    $ renpy.music.play(["music/banging.ogg","<silence 1.0>"], channel="background noise", fadeout = 6.0, fadein = 6.0, loop = True)

    scene black
    show vin_bat_1_2:
        alpha 1
        linear 0.3 xoffset 1280 alpha 0
    show vin_bat_1_1:
        xoffset -1280 alpha 0
        linear 0.3 xoffset 0 alpha 1
    $ renpy.pause(0.3, hard='True')

    scene vin_bat_1_1

    call screen vin_bat_1_1_screen

label vin_bat_1_2_to_3_switch:

    if vin_bat_1_solve_cp and not vin_bat_1_shadow_van:

        $ renpy.music.set_volume(1.0, delay=0, channel='sound')
        play sound "music/basement/vita_female_giggle.ogg"

        $ vin_bat_1_shadow_van = True
        scene black
        show game_over_static:
            linear 0.05 xoffset -70 yoffset 70
            linear 0.05 xoffset 70 yoffset -70
            linear 0.05 xoffset 0 yoffset 70
            linear 0.05 xoffset -70 yoffset -70
            linear 0.05 xoffset 0 yoffset 0
            repeat
        show basement_shadow_vanora:
            zoom 2.0 xalign 0.55 alpha 0.8 yoffset -10
            block:
                linear 0.05 xoffset -70 yoffset 70
                linear 0.05 xoffset 70 yoffset -70
                linear 0.05 xoffset 0 yoffset 70
                linear 0.05 xoffset -70 yoffset -70
                linear 0.05 xoffset 0 yoffset 0
                repeat
        $ renpy.pause(0.3, hard='True')

        scene vin_bat_1_3
        hide game_over_static
        hide basement_shadow_vanora
        $ renpy.transition(wipeLeft)
        $ renpy.pause(0.5, hard='True')
    else:


        $ renpy.music.set_volume(1.0, delay=0, channel='sound')
        play sound "music/scan map.ogg"

        scene black
        show vin_bat_1_2:
            alpha 1
            linear 0.3 xoffset -1280 alpha 0

        if vin_bat_1_solve_cp:
            show vin_bat_1_3:
                xoffset 1280 alpha 0
                linear 0.3 xoffset 0 alpha 1
        else:
            show vin_bat_1_3_0:
                xoffset 1280 alpha 0
                linear 0.3 xoffset 0 alpha 1
        $ renpy.pause(0.3, hard='True')

    call screen vin_bat_1_3_screen

label vin_bat_1_3_to_2_switch:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/scan map.ogg"

    scene black
    if vin_bat_1_solve_cp:
        show vin_bat_1_3:
            alpha 1
            linear 0.3 xoffset 1280 alpha 0
    else:
        show vin_bat_1_3_0:
            alpha 1
            linear 0.3 xoffset 1280 alpha 0
    show vin_bat_1_2:
        xoffset -1280 alpha 0
        linear 0.3 xoffset 0 alpha 1
    $ renpy.pause(0.3, hard='True')

    scene vin_bat_1_2

    call screen vin_bat_1_2_screen

label vin_bat_1_3_to_1_switch:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/scan map.ogg"

    $ renpy.music.set_volume(0.2, delay=0, channel='background noise')
    $ renpy.music.play(["music/banging.ogg","<silence 1.0>"], channel="background noise", fadeout = 6.0, fadein = 6.0, loop = True)

    scene black

    if vin_bat_1_solve_cp:
        show vin_bat_1_3:
            alpha 1
            linear 0.3 xoffset -1280 alpha 0
    else:
        show vin_bat_1_3_0:
            alpha 1
            linear 0.3 xoffset -1280 alpha 0
    show vin_bat_1_1:
        xoffset 1280 alpha 0
        linear 0.3 xoffset 0 alpha 1
    $ renpy.pause(0.3, hard='True')

    scene vin_bat_1_1

    call screen vin_bat_1_1_screen

label vin_bat_1_investigate_speaker:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/selectsounds.ogg"

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    show character_icon_box_1:
        xpos 200 ypos 250
    show draco_icon_blood_serious:
        xpos 200 ypos 250
    show character_icon_box_2:
        xpos 200 ypos 250
    with Dissolve(0.5)

    window show

    dra "\"Vanora, {w=0.5}you need to first restore power to this room by operating the two control panels connected to the breaker box.\""

    $ rollback_ = True

    dra "\"This will reactivate the eight touch monitors on the wall.\""

    dra "\"After that, {w=0.5}match all the corresponding symbols on the screens, {w=0.5}and the entrance to the next room will unlock.\""

    dra "\"Please hurry!\""

    window hide

    hide character_icon_box_1
    hide draco_icon_blood_serious
    hide character_icon_box_2
    with Dissolve(0.5)

    $ renpy.block_rollback()
    $ _rollback = False
    $ rollback_ = False
    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False

    call screen vin_bat_1_1_screen

label vin_bat_1_investigate_back_door:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/selectsounds.ogg"

    v "I have no reason to go back there. {w=0.5}It would be suicidal."

    call screen vin_bat_1_1_screen

label vin_bat_1_investigate_cp_plus:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show black:
        alpha 0
        linear 0.5 alpha 0.4

    if not vin_bat_1_solve_plus:

        $ vin_bat_1_plus_num = 4
        $ vin_bat_1_plus_display = str(vin_bat_1_plus_num).zfill(2)
        $ vin_bat_1_plus_click = 0

    show vin_bat_1_cp_zoom_plus:
        yoffset 3000
        ease 0.5 yoffset 0
    $ renpy.pause(0.5, hard='True')

    call screen vin_bat_1_cp_plus_screen

label vin_bat_1_cp_plus_leave:

    show black:
        alpha 0.4
        linear 0.5 alpha 0

    show vin_bat_1_cp_zoom_plus:
        yoffset 0
        ease 0.5 yoffset -3000
    $ renpy.pause(0.5, hard='True')

    hide black
    hide vin_bat_1_cp_zoom_plus


    $ vin_bat_1_plus_num = 4
    $ vin_bat_1_plus_display = str(vin_bat_1_plus_num).zfill(2)
    $ vin_bat_1_plus_click = 0

    call screen vin_bat_1_2_screen

label vin_bat_1_investigate_cp_minus:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show black:
        alpha 0
        linear 0.5 alpha 0.4

    if not vin_bat_1_solve_minus:

        $ vin_bat_1_minus_num = 79
        $ vin_bat_1_minus_display = str(vin_bat_1_minus_num).zfill(2)
        $ vin_bat_1_minus_click = 0

    show vin_bat_1_cp_zoom_minus:
        yoffset 3000
        ease 0.5 yoffset 0
    $ renpy.pause(0.5, hard='True')

    call screen vin_bat_1_cp_minus_screen

label vin_bat_1_cp_minus_leave:

    show black:
        alpha 0.4
        linear 0.5 alpha 0

    show vin_bat_1_cp_zoom_minus:
        yoffset 0
        ease 0.5 yoffset -3000
    $ renpy.pause(0.5, hard='True')

    hide black
    hide vin_bat_1_cp_zoom_minus


    $ vin_bat_1_minus_num = 79
    $ vin_bat_1_minus_display = str(vin_bat_1_minus_num).zfill(2)
    $ vin_bat_1_minus_click = 0

    call screen vin_bat_1_2_screen

label vin_bat_1_investigate_front_door:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/selectsounds.ogg"

    if not (vin_bat_1_solve_plus and vin_bat_1_solve_minus):
        v "Room exit. {w=0.5}I need to first restore power to this room."
    else:
        v "Room exit. {w=0.5}I need to match all the corresponding symbols on the screens."

    call screen vin_bat_1_3_screen

label vin_bat_1_investigate_cp_solved:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/selectsounds.ogg"

    v "I have already finished operating this control panel."

    call screen vin_bat_1_2_screen

label vin_bat_1_investigate_match:

    if not vin_bat_1_solve_cp:

        $ renpy.music.set_volume(1.0, delay=0, channel='sound')
        play sound "music/selectsounds.ogg"

        v "I need to first restore power to this room."

        call screen vin_bat_1_3_screen
    else:


        jump vin_bat_1_match_start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
