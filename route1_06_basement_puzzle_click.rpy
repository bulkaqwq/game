
image basement_4_puzzle_num = "images/basement/basement-4-puzzle-num.png"

screen basement_4_puzzle_screen:



    if basement_4_num_enter_passcode >= 1:
        add "images/basement/basement-4-puzzle-num.png" xpos 525 ypos 117
    if basement_4_num_enter_passcode >= 2:
        add "images/basement/basement-4-puzzle-num.png" xpos 582 ypos 117
    if basement_4_num_enter_passcode >= 3:
        add "images/basement/basement-4-puzzle-num.png" xpos 637 ypos 117
    if basement_4_num_enter_passcode >= 4:
        add "images/basement/basement-4-puzzle-num.png" xpos 692 ypos 117
    if basement_4_num_enter_passcode >= 5:
        add "images/basement/basement-4-puzzle-num.png" xpos 749 ypos 117
    if basement_4_num_enter_passcode >= 6:
        add "images/basement/basement-4-puzzle-num.png" xpos 805 ypos 117

    imagebutton:
        xpos 220
        ypos 211
        idle "images/basement/basement-4-puzzle-idle.png"
        hover "images/basement/basement-4-puzzle-hover.png"
        focus_mask "images/basement/basement-4-puzzle-hover.png"
        action Call("basement_4_puzzle_press_button", 1)

    imagebutton:
        xpos 461
        ypos 211
        idle "images/basement/basement-4-puzzle-idle.png"
        hover "images/basement/basement-4-puzzle-hover.png"
        focus_mask "images/basement/basement-4-puzzle-hover.png"
        action Call("basement_4_puzzle_press_button", 2)

    imagebutton:
        xpos 703
        ypos 211
        idle "images/basement/basement-4-puzzle-idle.png"
        hover "images/basement/basement-4-puzzle-hover.png"
        focus_mask "images/basement/basement-4-puzzle-hover.png"
        action Call("basement_4_puzzle_press_button", 3)

    imagebutton:
        xpos 944
        ypos 211
        idle "images/basement/basement-4-puzzle-idle.png"
        hover "images/basement/basement-4-puzzle-hover.png"
        focus_mask "images/basement/basement-4-puzzle-hover.png"
        action Call("basement_4_puzzle_press_button", 4)

    imagebutton:
        xpos 520
        ypos 610
        idle "images/basement/basement_door_arrow_down_idle.png"
        hover "images/tunnel/myers_tunnel_door_arrow_down_hover.png"
        focus_mask "images/basement/basement_door_arrow_down_idle.png"
        action Jump("basement_4_puzzle_leave")

label basement_4_puzzle_screen_start:

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False

    if not basement_4_check_puzzle:

        $ basement_4_check_puzzle = True

        $ renpy.pause(0.5, hard='True')

        $ renpy.music.set_volume(0.8, delay=0, channel='UI Dark')
        $ renpy.music.play("music/UI Dark.ogg", channel="UI Dark", loop = False)

        noname "Warning: {w=0.5}The device will unlock automatically after entering the correct answer."

        noname "If a wrong answer is entered, {w=0.5}the device will return to zero when it reaches six digits."

        $ _rollback = False
        $ rollback_ = False

    $ basement_4_entered_passcode = list("")

    $ basement_4_num_enter_passcode = 0

    call screen basement_4_puzzle_screen

label basement_4_puzzle_press_button(basement_4_puzzle_color):

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound ("music/passcode beep.ogg")

    $ basement_4_entered_passcode.append(basement_4_puzzle_color)
    $ basement_4_num_enter_passcode = basement_4_num_enter_passcode + 1

    if basement_4_num_enter_passcode > 5:

        if basement_4_entered_passcode != [4,1,3,3,2,1]:
            jump basement_4_puzzle_reset
        else:
            jump basement_4_solve_puzzle

    $ renpy.pop_call()

    call screen basement_4_puzzle_screen

label basement_4_puzzle_reset:

    show basement_4_puzzle_num:
        xpos 525 ypos 117
    show basement_4_puzzle_num as basement_4_puzzle_num_2:
        xpos 582 ypos 117
    show basement_4_puzzle_num as basement_4_puzzle_num_3:
        xpos 637 ypos 117
    show basement_4_puzzle_num as basement_4_puzzle_num_4:
        xpos 692 ypos 117
    show basement_4_puzzle_num as basement_4_puzzle_num_5:
        xpos 749 ypos 117
    show basement_4_puzzle_num as basement_4_puzzle_num_6:
        xpos 805 ypos 117

    $ renpy.pop_call()

    $ basement_4_num_enter_passcode = 0

    $ basement_4_entered_passcode = list("")

    $ renpy.music.set_volume(0.7, delay=0, channel='sound')
    play sound "music/tech interface.ogg"

    noname "Access denied."

    hide basement_4_puzzle_num
    hide basement_4_puzzle_num_2
    hide basement_4_puzzle_num_3
    hide basement_4_puzzle_num_4
    hide basement_4_puzzle_num_5
    hide basement_4_puzzle_num_6

    call screen basement_4_puzzle_screen

label basement_4_solve_puzzle:

    show basement_4_puzzle_num:
        xpos 525 ypos 117
    show basement_4_puzzle_num as basement_4_puzzle_num_2:
        xpos 582 ypos 117
    show basement_4_puzzle_num as basement_4_puzzle_num_3:
        xpos 637 ypos 117
    show basement_4_puzzle_num as basement_4_puzzle_num_4:
        xpos 692 ypos 117
    show basement_4_puzzle_num as basement_4_puzzle_num_5:
        xpos 749 ypos 117
    show basement_4_puzzle_num as basement_4_puzzle_num_6:
        xpos 805 ypos 117

    $ renpy.pop_call()

    $ basement_4_num_enter_passcode = 0

    $ basement_4_entered_passcode = list("")

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/weapon click.ogg"

    noname "Access granted."

    scene black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ basement_4_solve_puzzle = True
    $ basement_4_layer_3 = True

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound ["<silence 0.2>","music/motor.ogg"]

    show basement_4_box_zoom_2
    show basement_4_box_zoom_4:
        yoffset 419
        pause 0.3
        linear 0.8 yoffset 0
    show basement_4_box_zoom_3
    with Dissolve(0.3)
    with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    pause 1.0
    $ renpy.pause(0.1, hard='True')

    scene black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    scene basement_4
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    call screen basement_room_4_screen with Dissolve(0.2)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
