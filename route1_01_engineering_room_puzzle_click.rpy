
image engineering_room_3_puzzle_base = "images/Engineering Room 1/Engineering_room_3_puzzle_base.png"
image engineering_room_3_puzzle_red = "images/Engineering Room 1/Engineering_room_3_puzzle_red.png"
image engineering_room_3_puzzle_blue = "images/Engineering Room 1/Engineering_room_3_puzzle_blue.png"
image engineering_room_3_puzzle_green = "images/Engineering Room 1/Engineering_room_3_puzzle_green.png"
image engineering_room_3_puzzle_yellow = "images/Engineering Room 1/Engineering_room_3_puzzle_yellow.png"
image engineering_room_3_puzzle_diamond = "images/Engineering Room 1/Engineering_room_3_diamond.png"
image engineering_room_3_puzzle_square = "images/Engineering Room 1/Engineering_room_3_square.png"
image engineering_room_3_puzzle_circle = "images/Engineering Room 1/Engineering_room_3_circle.png"
image engineering_room_3_puzzle_triangle = "images/Engineering Room 1/Engineering_room_3_triangle.png"

screen engineering_room_3_puzzle_screen:

    $ engineering_room_3_puzzle_xpos = 200
    for x in engineering_room_3_puzzle_color_button_list:
        if x == 1:
            add "engineering_room_3_puzzle_green" xpos engineering_room_3_puzzle_xpos ypos 150
        elif x == 2:
            add "engineering_room_3_puzzle_red" xpos engineering_room_3_puzzle_xpos ypos 150
        elif x == 3:
            add "engineering_room_3_puzzle_blue" xpos engineering_room_3_puzzle_xpos ypos 150
        elif x == 4:
            add "engineering_room_3_puzzle_yellow" xpos engineering_room_3_puzzle_xpos ypos 150
        $ engineering_room_3_puzzle_xpos = engineering_room_3_puzzle_xpos + 250

    $ engineering_room_3_puzzle_xpos = 200
    for x in engineering_room_3_puzzle_shape_button_list:
        if x == 1:
            add "engineering_room_3_puzzle_diamond" xpos engineering_room_3_puzzle_xpos ypos 150
        elif x == 2:
            add "engineering_room_3_puzzle_square" xpos engineering_room_3_puzzle_xpos ypos 150
        elif x == 3:
            add "engineering_room_3_puzzle_circle" xpos engineering_room_3_puzzle_xpos ypos 150
        elif x == 4:
            add "engineering_room_3_puzzle_triangle" xpos engineering_room_3_puzzle_xpos ypos 150
        $ engineering_room_3_puzzle_xpos = engineering_room_3_puzzle_xpos + 250

    imagebutton:
        xpos 520
        ypos 610
        idle "images/john past/arrow_down_idle.png"
        hover "images/john past/arrow_down_hover.png"
        focus_mask "images/john past/arrow_down_idle.png"
        action Jump("engineering_room_3_investigate_puzzle_end")


    imagebutton:
        xpos 254
        ypos 37
        idle "images/Engineering Room 1/Engineering_room_3_puzzle_button_idle.png"
        hover "images/Engineering Room 1/Engineering_room_3_puzzle_button_hover.png"
        focus_mask "images/Engineering Room 1/Engineering_room_3_puzzle_button_hover.png"
        action [Play("sound", "music/Tunnel/wheelMoveSFX.ogg"), Call("engineering_room_3_puzzle_change_color", 0)]


    imagebutton:
        xpos 254
        ypos 437
        idle "images/Engineering Room 1/Engineering_room_3_puzzle_button_2_idle.png"
        hover "images/Engineering Room 1/Engineering_room_3_puzzle_button_2_hover.png"
        focus_mask "images/Engineering Room 1/Engineering_room_3_puzzle_button_2_hover.png"
        action [Play("sound", "music/Tunnel/wheelMoveSFX.ogg"), Call("engineering_room_3_puzzle_change_shape", 0)]


    imagebutton:
        xpos 506
        ypos 37
        idle "images/Engineering Room 1/Engineering_room_3_puzzle_button_idle.png"
        hover "images/Engineering Room 1/Engineering_room_3_puzzle_button_hover.png"
        focus_mask "images/Engineering Room 1/Engineering_room_3_puzzle_button_hover.png"
        action [Play("sound", "music/Tunnel/wheelMoveSFX.ogg"), Call("engineering_room_3_puzzle_change_color", 1)]


    imagebutton:
        xpos 506
        ypos 437
        idle "images/Engineering Room 1/Engineering_room_3_puzzle_button_2_idle.png"
        hover "images/Engineering Room 1/Engineering_room_3_puzzle_button_2_hover.png"
        focus_mask "images/Engineering Room 1/Engineering_room_3_puzzle_button_2_hover.png"
        action [Play("sound", "music/Tunnel/wheelMoveSFX.ogg"), Call("engineering_room_3_puzzle_change_shape", 1)]


    imagebutton:
        xpos 757
        ypos 37
        idle "images/Engineering Room 1/Engineering_room_3_puzzle_button_idle.png"
        hover "images/Engineering Room 1/Engineering_room_3_puzzle_button_hover.png"
        focus_mask "images/Engineering Room 1/Engineering_room_3_puzzle_button_hover.png"
        action [Play("sound", "music/Tunnel/wheelMoveSFX.ogg"), Call("engineering_room_3_puzzle_change_color", 2)]


    imagebutton:
        xpos 757
        ypos 437
        idle "images/Engineering Room 1/Engineering_room_3_puzzle_button_2_idle.png"
        hover "images/Engineering Room 1/Engineering_room_3_puzzle_button_2_hover.png"
        focus_mask "images/Engineering Room 1/Engineering_room_3_puzzle_button_2_hover.png"
        action [Play("sound", "music/Tunnel/wheelMoveSFX.ogg"), Call("engineering_room_3_puzzle_change_shape", 2)]


    imagebutton:
        xpos 1009
        ypos 37
        idle "images/Engineering Room 1/Engineering_room_3_puzzle_button_idle.png"
        hover "images/Engineering Room 1/Engineering_room_3_puzzle_button_hover.png"
        focus_mask "images/Engineering Room 1/Engineering_room_3_puzzle_button_hover.png"
        action [Play("sound", "music/Tunnel/wheelMoveSFX.ogg"), Call("engineering_room_3_puzzle_change_color", 3)]


    imagebutton:
        xpos 1009
        ypos 437
        idle "images/Engineering Room 1/Engineering_room_3_puzzle_button_2_idle.png"
        hover "images/Engineering Room 1/Engineering_room_3_puzzle_button_2_hover.png"
        focus_mask "images/Engineering Room 1/Engineering_room_3_puzzle_button_2_hover.png"
        action [Play("sound", "music/Tunnel/wheelMoveSFX.ogg"), Call("engineering_room_3_puzzle_change_shape", 3)]

label engineering_room_3_puzzle_screen_prep:

    if not engineering_room_click_puzzle_screen:

        if renpy.is_skipping():
            $ renpy.choice_for_skipping()

        $ renpy.pause(0.5, hard='True')

        $ renpy.music.set_volume(0.8, delay=0, channel='sound')
        play sound "music/UI Dark.ogg"

        noname "Warning: {w=0.5}The device will unlock automatically after entering the correct answer."

    $ _skipping = False
    $ rollback_ = False
    $ _rollback = False

    hide engineering_room_3_puzzle_color_1
    hide engineering_room_3_puzzle_color_2
    hide engineering_room_3_puzzle_red_2
    hide engineering_room_3_puzzle_color_3
    hide engineering_room_3_puzzle_color_4
    hide engineering_room_3_puzzle_shape_1
    hide engineering_room_3_puzzle_square_2
    hide engineering_room_3_puzzle_shape_2
    hide engineering_room_3_puzzle_shape_3
    hide engineering_room_3_puzzle_shape_4

    if not engineering_room_click_puzzle_screen:

        $ engineering_room_click_puzzle_screen = True

        $ engineering_room_3_puzzle_color_button_list = [1,2,3,4];
        $ engineering_room_3_puzzle_shape_button_list = [1,2,3,4];

        $ engineering_room_3_puzzle_color_correct_list = [1,3,4,2];
        $ engineering_room_3_puzzle_shape_correct_list = [4,2,1,3];

    call screen engineering_room_3_puzzle_screen with Dissolve(0.2)

label engineering_room_3_puzzle_change_color(engineering_room_3_puzzle_art_number):

    python:
        if engineering_room_3_puzzle_color_button_list[engineering_room_3_puzzle_art_number] != 4:
            engineering_room_3_puzzle_color_button_list[engineering_room_3_puzzle_art_number] += 1;
        else:
            engineering_room_3_puzzle_color_button_list[engineering_room_3_puzzle_art_number] = 1;

    jump engineering_room_3_puzzle_change_puzzle

    call screen engineering_room_3_puzzle_screen

label engineering_room_3_puzzle_change_shape(engineering_room_3_puzzle_art_number):

    python:
        if engineering_room_3_puzzle_shape_button_list[engineering_room_3_puzzle_art_number] != 4:
            engineering_room_3_puzzle_shape_button_list[engineering_room_3_puzzle_art_number] += 1;
        else:
            engineering_room_3_puzzle_shape_button_list[engineering_room_3_puzzle_art_number] = 1;

    jump engineering_room_3_puzzle_change_puzzle

    call screen engineering_room_3_puzzle_screen

label engineering_room_3_puzzle_change_puzzle:

    python:
        for x in range(4):
            if engineering_room_3_puzzle_color_button_list[x] != engineering_room_3_puzzle_color_correct_list[x]:
                renpy.pop_call()
                renpy.call_screen("engineering_room_3_puzzle_screen")
            if engineering_room_3_puzzle_shape_button_list[x] != engineering_room_3_puzzle_shape_correct_list[x]:
                renpy.pop_call()
                renpy.call_screen("engineering_room_3_puzzle_screen")

    $ engineering_room_puzzle_solved = True
    $ engineering_room_4_image = "images/Engineering Room 1/Engineering_room_4_unlocked.png"

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    show engineering_room_3_puzzle_green as engineering_room_3_puzzle_color_1:
        xpos 200 ypos 150
    show engineering_room_3_puzzle_triangle as engineering_room_3_puzzle_shape_1:
        xpos 200 ypos 150
    show engineering_room_3_puzzle_blue as engineering_room_3_puzzle_color_2:
        xpos 450 ypos 150
    show engineering_room_3_puzzle_square as engineering_room_3_puzzle_shape_2:
        xpos 450 ypos 150
    show engineering_room_3_puzzle_yellow as engineering_room_3_puzzle_color_3:
        xpos 700 ypos 150
    show engineering_room_3_puzzle_diamond as engineering_room_3_puzzle_shape_3:
        xpos 700 ypos 150
    show engineering_room_3_puzzle_red as engineering_room_3_puzzle_color_4:
        xpos 950 ypos 150
    show engineering_room_3_puzzle_circle as engineering_room_3_puzzle_shape_4:
        xpos 950 ypos 150

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/weapon click.ogg"

    pause 1.0

    van "It worked."

    $ rollback_ = True

    show character_icon_box:
        xpos 1350 ypos 300
        easein_expo 1.0 xpos 800 ypos 300
        xpos 800 ypos 300
    show zalmona_icon_surprised:
        xpos 1350 ypos 298
        easein_expo 1.0 xpos 800 ypos 298
        xpos 800 ypos 298

    zal "\"I can't believe it! {w=0.5}You're incredible!\""

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    $ renpy.pop_call()

    jump engineering_room_3_investigate_puzzle_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
