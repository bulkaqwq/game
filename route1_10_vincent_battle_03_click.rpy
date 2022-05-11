
screen vin_bat_3_1_screen:

    imagebutton:
        xpos 788
        ypos 97
        idle "images/vin battle 1/vin_bat_1_door_idle.png"
        hover "images/vin battle 1/vin_bat_1_door_hover.png"
        focus_mask "images/vin battle 1/vin_bat_1_door_hover.png"
        action Jump("vin_bat_3_investigate_back_door")

    imagebutton:
        xpos 150
        ypos 258
        idle "images/vin battle 3/vb3_desk_idle.png"
        hover "images/vin battle 3/vb3_desk_hover.png"
        focus_mask "images/vin battle 3/vb3_desk_hover.png"
        action Jump("vb3_investigate_desk")

    imagebutton:
        xpos 30
        ypos 560
        idle "images/basement/left-pink-arrow.png"
        hover "images/myers-click/left-white-arrow-small-small.png"
        focus_mask "images/myers-click/left-black-arrow-small-small.png"
        action Jump("vin_bat_3_1_to_3_switch")

    imagebutton:
        xpos 1030
        ypos 560
        idle "images/basement/right-pink-arrow.png"
        hover "images/myers-click/right-white-arrow-small-small.png"
        focus_mask "images/myers-click/right-black-arrow-small-small.png"
        action Jump("vin_bat_3_1_to_2_switch")

screen vin_bat_3_2_screen:

    imagebutton:
        xpos 30
        ypos 560
        idle "images/basement/left-pink-arrow.png"
        hover "images/myers-click/left-white-arrow-small-small.png"
        focus_mask "images/myers-click/left-black-arrow-small-small.png"
        action Jump("vin_bat_3_2_to_1_switch")

    imagebutton:
        xpos 1030
        ypos 560
        idle "images/basement/right-pink-arrow.png"
        hover "images/myers-click/right-white-arrow-small-small.png"
        focus_mask "images/myers-click/right-black-arrow-small-small.png"
        action Jump("vin_bat_3_2_to_3_switch")

    imagebutton:
        xpos 343
        ypos 310
        idle "images/vin battle 3/vb3_wb_idle.png"
        hover "images/vin battle 3/vb3_wb_hover.png"
        focus_mask "images/vin battle 3/vb3_wb_hover.png"
        action Jump("vb3_investigate_wb")

    imagebutton:
        xpos 395
        ypos 158
        idle "images/vin battle 3/vb3_cp_idle.png"
        hover "images/vin battle 3/vb3_cp_hover.png"
        focus_mask "images/vin battle 3/vb3_cp_hover.png"
        action Jump("vb3_investigate_cp")

screen vin_bat_3_3_screen:

    imagebutton:
        xpos 178
        ypos 97
        idle "images/vin battle 1/vin_bat_1_door_idle.png"
        hover "images/vin battle 1/vin_bat_1_door_hover.png"
        focus_mask "images/vin battle 1/vin_bat_1_door_hover.png"
        action Jump("vin_bat_3_investigate_front_door")

    imagebutton:
        xpos 608
        ypos 203
        idle "images/vin battle 3/vb3_cp2_idle.png"
        hover "images/vin battle 3/vb3_cp2_hover.png"
        focus_mask "images/vin battle 3/vb3_cp2_hover.png"
        action Jump("vb3_investigate_cp2")

    imagebutton:
        xpos 30
        ypos 560
        idle "images/basement/left-pink-arrow.png"
        hover "images/myers-click/left-white-arrow-small-small.png"
        focus_mask "images/myers-click/left-black-arrow-small-small.png"
        action Jump("vin_bat_3_3_to_2_switch")

    imagebutton:
        xpos 1030
        ypos 560
        idle "images/basement/right-pink-arrow.png"
        hover "images/myers-click/right-white-arrow-small-small.png"
        focus_mask "images/myers-click/right-black-arrow-small-small.png"
        action Jump("vin_bat_3_3_to_1_switch")

screen vb3_wb_zoom_screen:

    imagebutton:
        xpos 520
        ypos 610
        idle "images/basement/basement_door_arrow_down_idle.png"
        hover "images/tunnel/myers_tunnel_door_arrow_down_hover.png"
        focus_mask "images/basement/basement_door_arrow_down_idle.png"
        action Jump("vin_bat_3_wb_leave")

label vincent_battle_03_click_start:

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.block_rollback()
    $ _rollback = False


    $ vb3_solve_cp = False
    $ vb3_cp_buttons = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    $ vb3_cp2_icons = [1,1,1]

    call screen vin_bat_3_1_screen with Dissolve(0.2)

label vin_bat_3_1_to_3_switch:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/scan map.ogg"

    $ renpy.music.stop(channel="background noise", fadeout = 1.0)

    scene black
    show vin_bat_3_1:
        alpha 1
        linear 0.3 xoffset 1280 alpha 0
    show vin_bat_3_3:
        xoffset -1280 alpha 0
        linear 0.3 xoffset 0 alpha 1
    $ renpy.pause(0.3, hard='True')

    scene vin_bat_3_3

    call screen vin_bat_3_3_screen

label vin_bat_3_1_to_2_switch:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/scan map.ogg"

    $ renpy.music.stop(channel="background noise", fadeout = 1.0)

    scene black
    show vin_bat_3_1:
        alpha 1
        linear 0.3 xoffset -1280 alpha 0
    show vin_bat_3_2:
        xoffset 1280 alpha 0
        linear 0.3 xoffset 0 alpha 1
    $ renpy.pause(0.3, hard='True')

    scene vin_bat_3_2

    call screen vin_bat_3_2_screen

label vin_bat_3_2_to_1_switch:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/scan map.ogg"

    $ renpy.music.set_volume(0.2, delay=0, channel='background noise')
    $ renpy.music.play(["music/banging.ogg","<silence 1.0>"], channel="background noise", fadeout = 6.0, fadein = 6.0, loop = True)

    scene black
    show vin_bat_3_2:
        alpha 1
        linear 0.3 xoffset 1280 alpha 0
    show vin_bat_3_1:
        xoffset -1280 alpha 0
        linear 0.3 xoffset 0 alpha 1
    $ renpy.pause(0.3, hard='True')

    scene vin_bat_3_1

    call screen vin_bat_3_1_screen

label vin_bat_3_3_to_1_switch:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/scan map.ogg"

    $ renpy.music.set_volume(0.2, delay=0, channel='background noise')
    $ renpy.music.play(["music/banging.ogg","<silence 1.0>"], channel="background noise", fadeout = 6.0, fadein = 6.0, loop = True)

    scene black
    show vin_bat_3_3:
        alpha 1
        linear 0.3 xoffset -1280 alpha 0
    show vin_bat_3_1:
        xoffset 1280 alpha 0
        linear 0.3 xoffset 0 alpha 1
    $ renpy.pause(0.3, hard='True')

    scene vin_bat_3_1

    call screen vin_bat_3_1_screen

label vin_bat_3_3_to_2_switch:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/scan map.ogg"

    scene black
    show vin_bat_3_3:
        alpha 1
        linear 0.3 xoffset 1280 alpha 0
    show vin_bat_3_2:
        xoffset -1280 alpha 0
        linear 0.3 xoffset 0 alpha 1
    $ renpy.pause(0.3, hard='True')

    scene vin_bat_3_2

    call screen vin_bat_3_2_screen

label vin_bat_3_2_to_3_switch:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/scan map.ogg"

    scene black
    show vin_bat_3_2:
        alpha 1
        linear 0.3 xoffset -1280 alpha 0
    show vin_bat_3_3:
        xoffset 1280 alpha 0
        linear 0.3 xoffset 0 alpha 1
    $ renpy.pause(0.3, hard='True')

    scene vin_bat_3_3

    call screen vin_bat_3_3_screen

label vin_bat_3_investigate_back_door:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/selectsounds.ogg"

    v "I have no reason to go back there. {w=0.5}It would be suicidal."

    call screen vin_bat_3_1_screen

label vb3_investigate_desk:

    $ renpy.music.stop(channel="background noise", fadeout = 1.0)

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    nvl show Dissolve(0.5)

    $ _rollback = True
    $ _skipping = True

    diary "July 23, {w=0.5}2081, {w=0.5}Sunny"

    $ rollback_ = True

    diary "I never thought that Victor would actually agree to my request. "

    diary "Although he's always the first person to help me with my troubles no matter what I've asked of him,"

    diary "My request this time is just unprecedented -"

    diary "In order to accomplish it,{w=0.5} Victor will have to make a huge sacrifice."

    diary "I must admit that I feel very guilty and simultaneously worried,"

    nvl clear

    diary "because I'm not sure how seriously this will affect him."

    diary "But I have no choice, {w=0.5}Victor is the only person I can trust. {w=0.5}{color=#f00}This role has to be filled by no one but him.{/color}"

    nvl clear

    diary "May 7, {w=0.5}2084, {w=0.5}Rain"

    diary "The carrier has been cultured in the containment unit and the memories have been successfully implanted into the memory core."

    diary "Victor did have one request: {w=0.5}{color=#f00}he wanted all memories to take place before \"that thing\" happened.{/color}"

    diary "Although the carrier won't actually remember those, {w=0.5}I could understand why Victor would want that. {w=0.5}I complied."

    nvl clear

    diary "May 15, {w=0.5}2084, {w=0.5}Cloudy"

    diary "No, {w=0.5}this isn't even possible."

    diary "Everything was going so well, {w=0.5}but... {w=0.5}{color=#f00}his eyes.{/color}"

    diary "I couldn't believe it. {w=0.5}They looked {color=#f00}exactly the same{/color}!"

    nvl clear

    nvl hide Dissolve(0.5)

    v "Unlike the text before, {w=0.5}the last line of the diary looks like it was hastily written with a trembling hand."

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)
    $ renpy.block_rollback()
    $ _rollback = False

    $ renpy.music.set_volume(0.2, delay=0, channel='background noise')
    $ renpy.music.play(["music/banging.ogg","<silence 1.0>"], channel="background noise", fadeout = 6.0, fadein = 6.0, loop = True)

    call screen vin_bat_3_1_screen

label vb3_investigate_wb:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show black:
        alpha 0
        linear 0.5 alpha 0.4

    show vb3_whiteboard_zoom:
        alpha 0
        linear 0.5 alpha 1.0
    $ renpy.pause(0.5, hard='True')

    call screen vb3_wb_zoom_screen

label vin_bat_3_wb_leave:

    hide black
    hide vb3_whiteboard_zoom
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    call screen vin_bat_3_2_screen

label vin_bat_3_investigate_front_door:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/selectsounds.ogg"

    v "Room exit. {w=0.5}I need to first restore power to this room."

    call screen vin_bat_3_3_screen

label vb3_investigate_cp:

    if not vb3_solve_cp:

        jump vb3_cp_start

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/selectsounds.ogg"

    v "I have already finished operating this control panel."

    call screen vin_bat_3_2_screen

label vb3_investigate_cp2:

    if not vb3_solve_cp:

        $ renpy.music.set_volume(1.0, delay=0, channel='sound')
        play sound "music/selectsounds.ogg"

        v "I need to first restore power to this room."

        call screen vin_bat_3_3_screen
    else:


        jump vb3_cp2_start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
