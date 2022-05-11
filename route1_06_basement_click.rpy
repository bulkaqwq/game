
image basement_1:
    contains:
        "basement_broken_elevator_2"
    contains:
        "legal_department_elevator_2"
        alpha 0
        pause 0.2
        alpha 0.3
        pause 1.0
        alpha 0.2
        pause 0.5
        alpha 0
        pause 0.1
        alpha 0.4
        pause 0.1
        alpha 0.3
        pause 0.1
        alpha 1.0
        alpha 0.1
        repeat
    contains:
        "basement_broken_elevator_1"

image basement_2 = "[basement_2_image]"
default basement_2_image = "basement_2_bookshelf"
image basement_2_2 = "images/basement/basement-2-2.png"
image basement_2_1 = "images/basement/basement-2-1.png"

image basement_3:
    contains:
        "black"
    contains:
        "images/basement/basement-3-2.png"
    contains:
        "images/basement/basement-3-1.png"

image basement_4:
    contains:
        "images/basement/basement-4-1.png"
    contains:
        ConditionSwitch("basement_4_layer_1 == True", "images/basement/basement-4-2.png", "basement_4_layer_1 == False", "images/empty.png")
    contains:

        ConditionSwitch("basement_4_layer_2 == True", "images/basement/basement-4-3.png", "basement_4_layer_2 == False", "images/empty.png")
    contains:
        ConditionSwitch("basement_4_layer_3 == True", "images/basement/basement-4-4.png", "basement_4_layer_3 == False", "images/empty.png")

image basement_4_1 = "images/basement/basement-4-1.png"
image basement_4_2:
    xalign 0.5 yalign 1.0
    contains:
        "images/basement/basement-4-2.png"
image basement_4_3:
    xalign 0.5 yalign 1.0
    contains:
        "images/basement/basement-4-3.png"

image basement_4_lev_zoom = "images/basement/basement-4-lev-zoom.png"
image basement_4_cup_zoom = "images/basement/basement-4-cup-zoom.png"
image basement_4_cup_zoom_blurred = im.Blur("images/basement/basement-4-cup-zoom.png", 1.5)
image basement_4_box_zoom_1 = "images/basement/basement-4-box-zoom-1.png"
image basement_4_box_zoom_2 = "images/basement/basement-4-box-zoom-2.png"
image basement_4_box_zoom_3 = "images/basement/basement-4-box-zoom-3.png"
image basement_4_box_zoom_4 = "images/basement/basement-4-box-zoom-4.png"
image basement_4_puzzle_zoom = "images/basement/basement-4-puzzle-zoom.png"
image basement_photo = "images/basement/basement-photo.png"

image basement_3_2 = "images/basement/basement-3-2.png"
image basement_3_1 = "images/basement/basement-3-1.png"

image basement_2_bookshelf:
    contains:
        "images/basement/basement-2-1.png"
    contains:
        "images/basement/basement-2-2.png"

image basement_2_computer_zoom:
    contains:
        "images/basement/basement-2-computer-zoom-1.png"
    contains:
        "images/basement/basement-2-computer-zoom-2.png"
        alpha 1.0
        0.6
        alpha 0.0
        0.6
        repeat


init 2 python:
    iBasementKnife = Item("BasementKnife","images/Engineering Room 1/Engineering_room_knife_object.png")
    iBasementKey = Item("BasementKey","images/Engineering Room 1/Engineering_room_key_object.png")

label route1_basement_click_start:

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False


    $ active_item = None
    $ inventory = []


    $ store.inventory.append(iBasementKnife)
    $ setattr(iBasementKnife, "selected", False)

    $ renpy.pause(0.5, hard='True')

    $ renpy.music.set_volume(0.8, delay=0, channel='UI Dark')
    $ renpy.music.play("music/UI Dark.ogg", channel="UI Dark", loop = False)

    noname "Objective: {w=0.5}Locate the secret chamber"

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music ("music/Tunnel/myersSewers.ogg")

    window hide

    $ rollback_ = False
    $ renpy.block_rollback()
    $ _rollback = False


    $ basement_investigate_elevator = False
    $ basement_see_basement_4 = False
    $ basement_see_myer_chan = False
    $ basement_4_layer_1 = False
    $ basement_4_layer_2 = False
    $ basement_4_layer_3 = False
    $ basement_cut_myer_chan = False
    $ basement_check_lev_poster = False
    $ basement_check_bookshelf = False
    $ basement_find_key = False
    $ basement_check_cup_zoom = False
    $ basement_see_flashback = False
    $ basement_4_check_puzzle = False
    $ basement_4_solve_puzzle = False
    $ basement_unlock_box = False

    show screen inventory_screen
    with Dissolve(0.2)

    call screen basement_room_1_screen with Dissolve(0.2)

screen basement_room_1_screen:


    imagebutton:
        xpos 30
        ypos 560
        idle "images/basement/left-pink-arrow.png"
        hover "images/myers-click/left-white-arrow-small-small.png"
        focus_mask "images/myers-click/left-black-arrow-small-small.png"
        action Jump("basement_room_1_to_4")

    imagebutton:
        xpos 1030
        ypos 560
        idle "images/basement/right-pink-arrow.png"
        hover "images/myers-click/right-white-arrow-small-small.png"
        focus_mask "images/myers-click/right-black-arrow-small-small.png"
        action Jump("basement_room_1_to_2")

    imagebutton:
        xpos 328
        ypos 12
        idle "images/basement/basement-1-elevator-idle.png"
        hover "images/basement/basement-1-elevator-hover.png"
        focus_mask "images/basement/basement-1-elevator-hover.png"
        action checkInteractionValid0("basement_room_1_screen", "basement_room_1_investigate_elevator")

    imagebutton:
        xpos 970
        ypos 246
        idle "images/basement/basement-1-elevator-button-idle.png"
        hover "images/basement/basement-1-elevator-button-hover.png"
        focus_mask "images/basement/basement-1-elevator-button-hover.png"
        action checkInteractionValid0("basement_room_1_screen", "basement_room_1_investigate_elevator_button")

screen basement_room_2_screen:


    imagebutton:
        xpos 30
        ypos 560
        idle "images/basement/left-pink-arrow.png"
        hover "images/myers-click/left-white-arrow-small-small.png"
        focus_mask "images/myers-click/left-black-arrow-small-small.png"
        action Jump("basement_room_2_to_1")

    imagebutton:
        xpos 1030
        ypos 560
        idle "images/basement/right-pink-arrow.png"
        hover "images/myers-click/right-white-arrow-small-small.png"
        focus_mask "images/myers-click/right-black-arrow-small-small.png"
        action Jump("basement_room_2_to_3")

    imagebutton:
        xpos 112
        ypos 189
        idle "images/basement/basement-2-computer-idle.png"
        hover "images/basement/basement-2-computer-hover.png"
        focus_mask "images/basement/basement-2-computer-hover.png"
        action checkInteractionValid0("basement_room_2_screen", "basement_room_2_investigate_computer")

    imagebutton:
        xpos 732
        ypos 53
        idle "images/basement/basement-2-bookshelf-idle.png"
        hover "images/basement/basement-2-bookshelf-hover.png"
        focus_mask "images/basement/basement-2-bookshelf-hover.png"
        action checkInteractionValid0("basement_room_2_screen", "basement_room_2_investigate_bookshelf")

screen basement_room_3_screen:



    imagebutton:
        xpos 30
        ypos 560
        idle "images/basement/left-pink-arrow.png"
        hover "images/myers-click/left-white-arrow-small-small.png"
        focus_mask "images/myers-click/left-black-arrow-small-small.png"
        action Jump("basement_room_3_to_2")

    imagebutton:
        xpos 1030
        ypos 560
        idle "images/basement/right-pink-arrow.png"
        hover "images/myers-click/right-white-arrow-small-small.png"
        focus_mask "images/myers-click/right-black-arrow-small-small.png"
        action Jump("basement_room_3_to_4")

    imagebutton:
        xpos 650
        ypos 320
        idle "images/myers-click/dialogue-idle-crop-small.png"
        hover "images/myers-click/dialogue-hover-crop-small.png"
        focus_mask "images/myers-click/dialogue-hover-crop-small.png"
        action Jump("basement_room_3_vincent_talk")

    imagebutton:
        xpos 230
        ypos 96
        idle "images/basement/basement-3-gate-idle.png"
        hover "images/basement/basement-3-gate-hover.png"
        focus_mask "images/basement/basement-3-gate-hover.png"
        action checkInteractionValid0("basement_room_3_screen", "basement_room_3_investigate_gate")

screen basement_room_4_screen:

    imagebutton:
        xpos 30
        ypos 560
        idle "images/basement/left-pink-arrow.png"
        hover "images/myers-click/left-white-arrow-small-small.png"
        focus_mask "images/myers-click/left-black-arrow-small-small.png"
        action [Hide("displayTextScreenGeneral"), Jump("basement_room_4_to_3")]

    imagebutton:
        xpos 1030
        ypos 560
        idle "images/basement/right-pink-arrow.png"
        hover "images/myers-click/right-white-arrow-small-small.png"
        focus_mask "images/myers-click/right-black-arrow-small-small.png"
        action [Hide("displayTextScreenGeneral"), Jump("basement_room_4_to_1")]

    if not basement_cut_myer_chan:
        imagebutton:
            xpos 255
            ypos 0
            idle "images/basement/basement-4-poster-idle.png"
            hover "images/basement/basement-4-poster-hover.png"
            focus_mask "images/basement/basement-4-poster-hover.png"
            action [Hide("displayTextScreenGeneral"), testItem_General0(iBasementKnife,"basement_cut_myer_chan", True, "basement_room_4_screen", "basement_room_4_cut_myer_chan", "basement_room_4_investigate_myer_chan")]
    else:
        imagebutton:
            xpos 255
            ypos 0
            idle "images/basement/basement-4-poster-idle.png"
            hover "images/basement/basement-4-poster-hover.png"
            focus_mask "images/basement/basement-4-poster-hover.png"
            action [Hide("displayTextScreenGeneral"), checkInteractionValid0("basement_room_4_screen", "basement_room_4_investigate_lev_poster")]

    imagebutton:
        xpos 539
        ypos 352
        idle "images/basement/basement-4-drawer-idle.png"
        hover "images/basement/basement-4-drawer-hover.png"
        focus_mask "images/basement/basement-4-drawer-hover.png"
        action [Hide("displayTextScreenGeneral"), checkInteractionValid0("basement_room_4_screen", "basement_room_4_investigate_drawer_1")]

    imagebutton:
        xpos 918
        ypos 352
        idle "images/basement/basement-4-drawer-idle.png"
        hover "images/basement/basement-4-drawer-hover.png"
        focus_mask "images/basement/basement-4-drawer-hover.png"
        action [Hide("displayTextScreenGeneral"), checkInteractionValid0("basement_room_4_screen", "basement_room_4_investigate_drawer_2")]

    imagebutton:
        xpos 539
        ypos 457
        idle "images/basement/basement-4-cupboard-idle.png"
        hover "images/basement/basement-4-cupboard-hover.png"
        focus_mask "images/basement/basement-4-cupboard-hover.png"
        action [Hide("displayTextScreenGeneral"), checkInteractionValid0("basement_room_4_screen", "basement_room_4_investigate_cupboard_1")]

    imagebutton:
        xpos 918
        ypos 457
        idle "images/basement/basement-4-cupboard-idle.png"
        hover "images/basement/basement-4-cupboard-hover.png"
        focus_mask "images/basement/basement-4-cupboard-hover.png"
        action [Hide("displayTextScreenGeneral"), checkInteractionValid0("basement_room_4_screen", "basement_room_4_investigate_cupboard_2")]

    imagebutton:
        xpos 1059
        ypos 51
        idle "images/basement/basement-4-air-vent-idle.png"
        hover "images/basement/basement-4-air-vent-hover.png"
        focus_mask "images/basement/basement-4-air-vent-hover.png"
        action [Hide("displayTextScreenGeneral"), checkInteractionValid0("basement_room_4_screen", "basement_room_4_investigate_air_vent")]

    if not basement_4_solve_puzzle:
        imagebutton:
            xpos 724
            ypos 352
            idle "images/basement/basement-4-code-idle.png"
            hover "images/basement/basement-4-code-hover.png"
            focus_mask "images/basement/basement-4-code-hover.png"
            action checkInteractionValid0("basement_room_4_screen", "basement_room_4_investigate_puzzle")
    else:
        imagebutton:
            xpos 724
            ypos 352
            idle "images/basement/basement-4-code-idle.png"
            hover "images/basement/basement-4-code-hover.png"
            focus_mask "images/basement/basement-4-code-hover.png"
            action NullAction()
            hovered Show("displayTextScreenGeneral", displayText = _(" I have solved the puzzle "), xalign_value=0.685, yalign_value=0.6)
            unhovered Hide("displayTextScreenGeneral")

    if not basement_4_solve_puzzle:
        imagebutton:
            xpos 744
            ypos 320
            idle "images/basement/basement-4-box-idle.png"
            hover "images/basement/basement-4-box-hover.png"
            focus_mask "images/basement/basement-4-box-hover.png"
            action checkInteractionValid0("basement_room_4_screen", "basement_room_4_investigate_box")
    elif not basement_unlock_box:
        imagebutton:
            xpos 747
            ypos 211
            idle "images/basement/basement-4-box-2-idle.png"
            hover "images/basement/basement-4-box-2-hover.png"
            focus_mask "images/basement/basement-4-box-2-hover.png"
            action [Hide("displayTextScreenGeneral"), testItem_General0(iBasementKey,"basement_unlock_box", True, "basement_room_4_screen", "basement_room_4_unlock_box", "basement_room_4_investigate_box_2")]
    else:
        imagebutton:
            xpos 747
            ypos 211
            idle "images/basement/basement-4-box-2-idle.png"
            hover "images/basement/basement-4-box-2-hover.png"
            focus_mask "images/basement/basement-4-box-2-hover.png"
            action [Hide("displayTextScreenGeneral"), checkInteractionValid0("basement_room_4_screen", "basement_room_4_investigate_box_3")]

    if basement_4_layer_2:
        imagebutton:
            xpos 330
            ypos 608
            idle "images/basement/basement-4-cup-idle.png"
            hover "images/basement/basement-4-cup-hover.png"
            focus_mask "images/basement/basement-4-cup-hover.png"
            action [Hide("displayTextScreenGeneral"), checkInteractionValid0("basement_room_4_screen", "basement_room_4_investigate_cup")]

screen basement_room_4_cup_screen:

    if not basement_see_flashback:
        imagebutton:
            xpos 300
            ypos 97
            idle "images/basement/basement-4-cup-zoom-idle.png"
            hover "images/basement/basement-4-cup-zoom-hover.png"
            focus_mask "images/basement/basement-4-cup-zoom-hover.png"
            action checkInteractionValid0("basement_room_4_cup_screen", "basement_room_4_investigate_cup_zoom")
    else:
        imagebutton:
            xpos 300
            ypos 97
            idle "images/basement/basement-4-cup-zoom-idle.png"
            hover "images/basement/basement-4-cup-zoom-hover.png"
            focus_mask "images/basement/basement-4-cup-zoom-hover.png"
            action checkInteractionValid0("basement_room_4_cup_screen", "basement_room_4_teleport")

    imagebutton:
        xpos 520
        ypos 610
        idle "images/basement/basement_door_arrow_down_idle.png"
        hover "images/tunnel/myers_tunnel_door_arrow_down_hover.png"
        focus_mask "images/basement/basement_door_arrow_down_idle.png"
        action Jump("basement_4_finish_investigate_cup")

screen basement_room_4_photo_screen:

    imagebutton:
        xpos 520
        ypos 610
        idle "images/basement/basement_door_arrow_down_idle.png"
        hover "images/tunnel/myers_tunnel_door_arrow_down_hover.png"
        focus_mask "images/basement/basement_door_arrow_down_idle.png"
        action Jump("basement_4_finish_investigate_photo")


label basement_room_1_to_2:

    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound ("music/Tunnel/FootSteps_EmployeePass.ogg")

    scene black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.pause(0.1, hard='True')
    pause 2.0
    $ renpy.pause(0.1, hard='True')

    stop sound fadeout 2.0

    scene basement_2
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    call screen basement_room_2_screen with Dissolve(0.2)

label basement_room_1_to_4:

    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound ("music/Tunnel/FootSteps_EmployeePass.ogg")

    scene black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.pause(0.1, hard='True')
    pause 2.0
    $ renpy.pause(0.1, hard='True')

    stop sound fadeout 2.0

    scene basement_4
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    if not basement_see_basement_4:
        $ basement_see_basement_4 = True
        jump basement_room_4_initial_convo

    call screen basement_room_4_screen with Dissolve(0.2)

label basement_room_2_to_1:

    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound ("music/Tunnel/FootSteps_EmployeePass.ogg")

    scene black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.pause(0.1, hard='True')
    pause 2.0
    $ renpy.pause(0.1, hard='True')

    stop sound fadeout 2.0

    scene basement_1
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    call screen basement_room_1_screen with Dissolve(0.2)

label basement_room_2_to_3:

    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound ("music/Tunnel/FootSteps_EmployeePass.ogg")

    scene black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.pause(0.1, hard='True')
    pause 2.0
    $ renpy.pause(0.1, hard='True')

    stop sound fadeout 2.0

    scene basement_3
    show vin_normal at vin_pos_2
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    call screen basement_room_3_screen with Dissolve(0.2)

label basement_room_3_to_2:

    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound ("music/Tunnel/FootSteps_EmployeePass.ogg")

    scene black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.pause(0.1, hard='True')
    pause 2.0
    $ renpy.pause(0.1, hard='True')

    stop sound fadeout 2.0

    scene basement_2
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    call screen basement_room_2_screen with Dissolve(0.2)

label basement_room_3_to_4:

    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound ("music/Tunnel/FootSteps_EmployeePass.ogg")

    scene black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.pause(0.1, hard='True')
    pause 2.0
    $ renpy.pause(0.1, hard='True')

    stop sound fadeout 2.0

    scene basement_4
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    if not basement_see_basement_4:
        $ basement_see_basement_4 = True
        jump basement_room_4_initial_convo

    call screen basement_room_4_screen with Dissolve(0.2)

label basement_room_4_to_3:

    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound ("music/Tunnel/FootSteps_EmployeePass.ogg")

    scene black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.pause(0.1, hard='True')
    pause 2.0
    $ renpy.pause(0.1, hard='True')

    stop sound fadeout 2.0

    scene basement_3
    show vin_normal at vin_pos_2
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    call screen basement_room_3_screen with Dissolve(0.2)

label basement_room_4_to_1:

    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound ("music/Tunnel/FootSteps_EmployeePass.ogg")

    scene black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.pause(0.1, hard='True')
    pause 2.0
    $ renpy.pause(0.1, hard='True')

    stop sound fadeout 2.0

    scene basement_1
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    call screen basement_room_1_screen with Dissolve(0.2)

label basement_room_1_investigate_elevator:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show basement_1 at Position(xpos = 0, ypos = 0)

    show basement_1:
        ease 0.5 zoom 1.5 xoffset 20 yoffset 250

    $ renpy.pause(0.5, hard='True')

    $ renpy.music.set_volume(0.3, delay=0, channel='electricity')
    $ renpy.music.play("music/electricity.ogg", channel="electricity", loop=False, fadein=3.0)

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    v "The elevator. {w=0.5}That's what I took to get to the basement."

    $ rollback_ = True

    v "Draco and I were pursued by some sort of monster on our way here."

    v "I had no clue what happened after the crash. {w=0.5}I don't know what happened to Draco either."

    if not basement_investigate_elevator:

        show character_icon_box_1:
            xpos 1350 ypos 50
            easein_expo 1.0 xpos 800 ypos 50
            xpos 800 ypos 50
        show vin_icon_smile:
            xpos 1350 ypos 50
            easein_expo 1.0 xpos 800 ypos 48
            xpos 800 ypos 48
        show character_icon_box_2:
            xpos 1350 ypos 50
            easein_expo 1.0 xpos 800 ypos 50
            xpos 800 ypos 50

        $ renpy.music.set_volume(0.4, delay=0, channel='sound')
        play sound "music/vin_hmm.ogg"

        vin "\"There's no need to worry about Draco, {w=0.5}Vanora.\""

        v "\"!?\""

        hide character_icon_box_1
        hide vin_icon_smile
        hide character_icon_box_2
        with Dissolve(0.5)

    show basement_1:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    $ renpy.pause(0.5, hard='True')

    if not basement_investigate_elevator:

        $ renpy.pause(0.5, hard='True')

        show vin_normal
        with Dissolve(0.5)

        $ renpy.pause(0.5, hard='True')

        window show

        v "\"You know where he is?\""

        show vin_smile
        hide vin_normal
        with Dissolve(0.2)

        vin "\"No. {w=0.5}But what I do know is, {w=0.5}he's not as vulnerable as you imagine him to be.\""

        hide vin_smile
        show vin_normal
        with Dissolve(0.2)

        show character_icon_box_1:
            xpos 200 ypos 250
        show van_icon_normal:
            xpos 200 ypos 248
        show character_icon_box_2:
            xpos 200 ypos 250
        with Dissolve(0.5)

        v "\"......\""

        window hide

        hide vin_normal
        hide character_icon_box_1
        hide van_icon_normal
        hide character_icon_box_2
        $ renpy.transition(Dissolve(0.5))
        $ renpy.pause(0.5, hard='True')

        $ basement_investigate_elevator = True

    $ renpy.music.stop(channel="electricity", fadeout = 2.0)

    $ renpy.block_rollback()
    $ _rollback = False
    $ rollback_ = False
    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False

    hide basement_1
    scene basement_1

    call screen basement_room_1_screen with Dissolve(0.2)

label basement_room_1_investigate_elevator_button:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show basement_1 at Position(xpos = 0, ypos = 0)

    show basement_1:
        ease 0.5 zoom 2.0 xoffset -640 yoffset 500

    pause 0.5

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/basement/zs_tap.ogg")

    pause 2.0

    v "The elevator button. {w=0.5}It's no longer working."

    show basement_1:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    $ renpy.pause(0.5, hard='True')

    call screen basement_room_1_screen with Dissolve(0.2)

label basement_room_2_investigate_bookshelf:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show basement_2 at Position(xpos = 0, ypos = 0)

    show basement_2:
        ease 0.5 zoom 1.5 xoffset -300 yoffset 300

    pause 0.5

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    v "A bookcase full of books."

    $ rollback_ = True

    if not basement_check_bookshelf:


        $ basement_check_bookshelf = True

        $ renpy.pause(0.5, hard='True')

        show character_icon_box_1:
            xpos 1350 ypos 50
            easein_expo 1.0 xpos 800 ypos 50
            xpos 800 ypos 50
        show vin_icon_smile:
            xpos 1350 ypos 50
            easein_expo 1.0 xpos 800 ypos 48
            xpos 800 ypos 48
        show character_icon_box_2:
            xpos 1350 ypos 50
            easein_expo 1.0 xpos 800 ypos 50
            xpos 800 ypos 50

        vin "\"Hmm? {w=0.5}How fascinating.\""

        hide character_icon_box_1
        hide vin_icon_smile
        hide character_icon_box_2
        with Dissolve(0.5)

        show basement_2:
            ease 0.5 zoom 1.0 xoffset 0 yoffset 0

        $ renpy.pause(0.5, hard='True')

        $ renpy.music.set_volume(0.1, delay=0, channel='sound')
        play sound "music/cloth.mp3" fadeout 2.0

        pause 1.0

        v "Vincent took a book off the bookcase and flipped through it."

        $ renpy.pause(0.5, hard='True')

        show character_icon_box_1:
            xpos 800 ypos 50
        show vin_icon_normal:
            xpos 800 ypos 48
        show character_icon_box_2:
            xpos 800 ypos 50
        with Dissolve(0.5)

        window show

        show vin_icon_smile behind character_icon_box_2:
            xpos 800 ypos 48
        hide vin_icon_normal
        with Dissolve(0.2)

        vin "\"Do you enjoy reading, {w=0.5}Vanora?\""

        show character_icon_box:
            xpos 200 ypos 250
        show van_icon_normal:
            xpos 200 ypos 248
        with Dissolve(0.5)

        v "\"...Not really.\""

        $ renpy.music.set_volume(0.4, delay=0, channel='sound')
        play sound "music/vin_hmm.ogg"

        hide vin_icon_smile
        show vin_icon_high_brow_talk behind character_icon_box_2:
            xpos 800 ypos 48
        with Dissolve(0.2)

        vin "\"Not really? {w=0.5}Is it because you can't understand them?\""

        window hide

        hide character_icon_box_1
        hide vin_icon_high_brow_talk
        hide character_icon_box_2
        hide van_icon_normal
        hide character_icon_box
        with Dissolve(0.5)

        $ renpy.music.set_volume(0.1, delay=0, channel='sound')
        play sound "music/cloth.mp3" fadeout 2.0

        $ renpy.pause(0.5, hard='True')

        v "Vincent mocked me as he put the book back on the shelf."

        $ say_who = _("Vincent")

        show vin_normal
        $ renpy.transition(Dissolve(0.5))
        $ renpy.pause(0.5, hard='True')

        window show

        show vin_high_single_brow_talk
        hide vin_normal
        with Dissolve(0.2)

        vin "\"But how strange it is, {w=0.5}don't you think?\""

        hide vin_high_single_brow_talk
        show vin_smile
        with Dissolve(0.2)

        vin "\"We're in the basement of the Myers Corporation, {w=0.5}yet the bookcase is filled with books on {color=#f00}history{/color} and {color=#f00}philosophy{/color}.\""

        hide vin_smile
        show vin_normal
        with Dissolve(0.2)

        v "\"!?\""

        show vin_close_eye
        hide vin_smile
        with Dissolve(0.2)

        vin "\"Of course, {w=0.5}I won't complain as those happen to be my favorite as well.\""

        window hide

        $ say_who = ""

        hide vin_close_eye with Dissolve(0.5)

        $ renpy.pause(0.1, hard='True')

        hide vin_normal
        $ renpy.transition(Dissolve(0.5))
        $ renpy.pause(0.5, hard='True')
    else:


        v "We're in the basement of the Myers Corporation, {w=0.5}yet the bookcase is mostly filled with books on {color=#f00}history{/color} and {color=#f00}philosophy{/color}."

        show basement_2:
            ease 0.5 zoom 1.0 xoffset 0 yoffset 0

        $ renpy.pause(0.5, hard='True')

    if basement_check_lev_poster and not basement_find_key:

        $ basement_find_key = True
        jump basement_room_2_find_key

    $ renpy.block_rollback()
    $ _rollback = False
    $ rollback_ = False
    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False

    hide basement_2
    scene basement_2

    call screen basement_room_2_screen with Dissolve(0.2)

label basement_room_2_find_key:

    show character_icon_box:
        xpos -370 ypos 250
        easein 0.8 xpos 200 ypos 250 subpixel True
        xpos 200 ypos 250
    show van_icon_close_eye:
        xpos -370 ypos 248
        easein 0.8 xpos 200 ypos 248 subpixel True
        xpos 200 ypos 248

    $ renpy.pause(0.5, hard='True')

    window show

    v "\"History and philosophy...\""

    v "\"Philosophy...\""


    show character_icon_box:
        xpos 200 ypos 250
    hide van_icon_close_eye
    show van_icon_normal:
        xpos 200 ypos 248

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/shock2.ogg" fadeout 2.0

    v "!?" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    hide van_icon_normal
    hide character_icon_box
    with Dissolve(0.5)

    v "\"Vincent, {w=0.5}you mentioned that 'Leviathan' is also the name of a philosophical work, {w=0.5}right?\""

    show character_icon_box_1:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 800 ypos 50
        xpos 800 ypos 50
    show vin_icon_smile:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 800 ypos 48
        xpos 800 ypos 48
    show character_icon_box_2:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 800 ypos 50
        xpos 800 ypos 50

    vin "\"That is correct.\""

    hide character_icon_box_1
    hide vin_icon_smile
    hide character_icon_box_2
    with Dissolve(0.5)
    v " I swept my eyes quickly over each of the books' titles."

    v "\"'Being and Nothingness', {w=0.5}'Republic', {w=0.5}'The Birth of Tragedy'...\""

    window hide

    pause 1.0

    v "\"...Here it is. {w=0.5}'Leviathan'.\""

    $ renpy.music.set_volume(0.1, delay=0, channel='sound')
    play sound "music/cloth.mp3" fadeout 2.0

    pause 1.0

    v "I took \"Leviathan\" off the bookcase and opened the book."

    v "As I had expected - {w=0.5}the inside of the book is actually completely hollow."

    v "Hidden inside is... {w=0.5}{color=#f00}a key{/color}."

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    $ renpy.pause(0.5, hard='True')

    $ renpy.music.set_volume(0.8, delay=0, channel='UI Dark')
    $ renpy.music.play("music/UI Dark.ogg", channel="UI Dark", loop = False)

    noname "Collected item: {w=0.5}A key"


    $ store.inventory.append(iBasementKey)
    $ store.active_item = None
    $ renpy.restart_interaction()

    $ setattr(iBasementKey, "selected", False)

    $ renpy.block_rollback()
    $ _rollback = False
    $ rollback_ = False
    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False

    call screen basement_room_2_screen with Dissolve(0.2)

label basement_room_2_investigate_computer:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show basement_2 at Position(xpos = 0, ypos = 0)

    show basement_2:
        ease 0.5 zoom 1.5 xoffset 300 yoffset 150

    pause 0.5

    if not basement_unlock_box:

        $ _skipping = True
        $ renpy.block_rollback()
        $ _rollback = True

        v "A computer."

        $ rollback_ = True

        $ renpy.music.set_volume(0.4, delay=0, channel='sound')
        play sound "music/John Past/discord.ogg"

        show basement_2_computer_zoom
        $ renpy.transition(Dissolve(1.0))
        $ renpy.pause(1.0, hard='True')

        pause 1.0

        window show

        v "Hm?"

        window hide

        $ renpy.pause(1.0, hard='True')

        show character_icon_box_1:
            xpos 800 ypos 50
        show vin_icon_normal:
            xpos 800 ypos 48
        show character_icon_box_2:
            xpos 800 ypos 50
        with Dissolve(0.5)

        window show

        show vin_icon_smile behind character_icon_box_2:
            xpos 800 ypos 48
        hide vin_icon_normal
        with Dissolve(0.2)

        vin "\"Looks like you need to follow the on-screen instructions to enter some form of password.\""

        window hide

        hide character_icon_box_1
        hide vin_icon_smile
        hide character_icon_box_2
        $ renpy.transition(Dissolve(1.0))
        $ renpy.pause(1.0, hard='True')

        pause 1.0

        v "I don't know what the password is yet. {w=0.5}I need to gather more clues."
    else:


        $ renpy.music.set_volume(0.4, delay=0, channel='sound')
        play sound "music/John Past/discord.ogg"

        show basement_2_computer_zoom
        $ renpy.transition(Dissolve(0.5))
        $ renpy.pause(0.5, hard='True')

        python:
            basement_enter_code = renpy.input(_("Enter password: "), length=12)
            basement_enter_code = basement_enter_code.strip()
            basement_enter_code = basement_enter_code.lower()

        if basement_enter_code != "ru37":

            $ renpy.music.set_volume(0.7, delay=0, channel='sound')
            play sound "music/tech interface.ogg"
            noname "Access denied."

            if basement_enter_code == "rmu3/2/2077" or basement_enter_code == "rmu 3/2/2077":

                show character_icon_box_1:
                    xpos 800 ypos 50
                show vin_icon_normal:
                    xpos 800 ypos 48
                show character_icon_box_2:
                    xpos 800 ypos 50
                with Dissolve(0.5)

                window show

                show vin_icon_smile behind character_icon_box_2:
                    xpos 800 ypos 48
                hide vin_icon_normal
                with Dissolve(0.2)

                vin "\"Hmm... {w=0.5}Perhaps all you need to enter are the missing characters?\""

                window hide

                hide vin_icon_smile
                hide character_icon_box_1
                hide character_icon_box_2
                $ renpy.transition(Dissolve(1.0))
        else:

            $ renpy.music.set_volume(0.6, delay=0, channel='sound')
            play sound "music/weapon click.ogg"
            noname "Access granted."

            jump basement_click_end

    hide basement_2_computer_zoom
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    show basement_2:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0
    $ renpy.pause(0.5, hard='True')

    $ renpy.block_rollback()
    $ _rollback = False
    $ rollback_ = False
    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False

    hide basement_2
    scene basement_2

    call screen basement_room_2_screen with Dissolve(0.2)

label basement_room_3_vincent_talk:

    $ renpy.block_rollback()

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/selectsounds.ogg"

    $ _rollback = True
    $ _skipping = True

    show vin_smile at vin_pos_2

    vin "\"Since all Madam wants to know is the truth, {w=0.5}why don't we explore the room that is filled with truth together?\""

    $ rollback_ = True

    vin "\"The one and only secret chamber of the G4 Cyborg Incident is hidden somewhere in this room.\""

    vin "\"Why not use your power to solve the mystery here?\""

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ _rollback = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    hide vin_smile

    call screen basement_room_3_screen with Dissolve(0.2)

label basement_room_3_investigate_gate:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    scene black
    show basement_3_2
    show basement_3_1

    show basement_3_2:
        ease 0.5 zoom 1.5 xoffset 300 yoffset 250
    show basement_3_1:
        ease 0.5 zoom 1.5 xoffset 300 yoffset 250

    $ renpy.pause(0.6, hard='True')

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/motor.ogg"

    show basement_3_2:
        ease 1.0 yoffset -550

    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15))
    $ renpy.pause(1.0, hard='True')

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    $ renpy.pause(0.5, hard='True')

    show character_icon_box_1:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 800 ypos 50
        xpos 800 ypos 50
    show vin_icon_normal:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 800 ypos 48
        xpos 800 ypos 48
    show character_icon_box_2:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 800 ypos 50
        xpos 800 ypos 50

    $ renpy.pause(1.0, hard='True')

    window show


    show character_icon_box_1:
        xpos 800 ypos 50
    show character_icon_box_2:
        xpos 800 ypos 50
    hide vin_icon_normal
    show vin_icon_smile behind character_icon_box_2:
        xpos 800 ypos 48
    with Dissolve(0.2)

    vin "\"Well well, {w=0.5}having cold feet, {w=0.5}aren't we?\""

    $ rollback_ = True

    vin "\"Didn't you want to know the truth, {w=0.5}Vanora? {w=0.5}Why are you in such a hurry to leave?\""

    window hide

    show basement_3_2:
        ease 0.5 zoom 1.0 xoffset 0
    show basement_3_1:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    $ renpy.pause(0.1, hard='True')

    hide character_icon_box_1
    hide vin_icon_smile
    hide character_icon_box_2
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    show vin_close_eye at vin_pos_2
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ say_who = _("Vincent")

    window show

    vin "\"Of course, {w=0.5}if you have simply changed your mind, {w=0.5}I won't force you to stay either.\""

    show vin_smile at vin_pos_2
    hide vin_close_eye
    with Dissolve(0.2)

    vin "\"In the end, {w=0.5}your past memories have nothing to do with me, {w=0.5}wouldn't you agree?\""

    hide vin_smile
    show vin_normal at vin_pos_2
    show character_icon_box:
        xpos 200 ypos 250
    show van_icon_normal:
        xpos 200 ypos 248
    with Dissolve(0.5)

    $ say_who = ""

    v "\"......\""

    hide character_icon_box
    hide van_icon_normal
    with Dissolve(0.2)

    window hide

    $ renpy.pause(0.5, hard='True')

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/motor.ogg"

    show basement_3_2:
        ease 1.0 zoom 1.0 xoffset 0 yoffset 0

    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15))
    $ renpy.pause(1.0, hard='True')

    v "I can't leave yet. {w=0.5}I need to find the secret chamber."

    $ renpy.block_rollback()
    $ _rollback = False
    $ rollback_ = False
    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False

    scene basement_3
    show vin_normal at vin_pos_2

    call screen basement_room_3_screen with Dissolve(0.2)

label basement_room_4_initial_convo:

    $ renpy.pause(1.0, hard='True')

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    show character_icon_box:
        xpos 200 ypos 250
    show van_icon_normal:
        xpos 200 ypos 248
    with Dissolve(0.5)

    window show

    v "!?"

    v "\"What the hell happened here?\""

    $ say_who = _("Vincent")

    show character_icon_box_1:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 800 ypos 50
        xpos 800 ypos 50
    show vin_icon_normal:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 800 ypos 48
        xpos 800 ypos 48
    show character_icon_box_2:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 800 ypos 50
        xpos 800 ypos 50

    window show

    vin "\"Hmm... {w=0.5}Interesting.\""

    show character_icon_box_1:
        xpos 800 ypos 50
    show character_icon_box_2:
        xpos 800 ypos 50
    show vin_icon_smile behind character_icon_box_2:
        xpos 800 ypos 48
    hide vin_icon_normal
    with Dissolve(0.2)

    vin "\"The blood spatters on the walls are fresh. {w=0.5}It looks like a fight just happened here before we arrived.\""

    show van_icon_close_eye:
        xpos 200 ypos 248
    show vin_icon_normal behind character_icon_box_2:
        xpos 800 ypos 48
    hide vin_icon_smile
    hide van_icon_normal
    with Dissolve(0.2)

    $ say_who = ""

    v "\"Then this must be a fight between Draco... {w=0.5}and that monster.\""

    window hide

    $ renpy.pause(0.1, hard='True')

    hide van_icon_close_eye
    hide vin_icon_normal
    hide character_icon_box_1
    hide character_icon_box_2
    hide character_icon_box
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.block_rollback()
    $ _rollback = False
    $ rollback_ = False
    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False

    call screen basement_room_4_screen with Dissolve(0.2)

label basement_room_4_investigate_myer_chan:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show basement_4 at Position(xpos = 0, ypos = 0)

    show basement_4:
        ease 0.5 zoom 1.6 xoffset 300 yoffset 400

    $ renpy.pause(0.5, hard='True')

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    v "A poster of Myer-chan."

    $ rollback_ = True

    v "The poster was firmly fixed to the wall with some kind of {color=#f00}white glue{/color} around it."

    v "I picked at it with my finger, {w=0.5}but I couldn't get it off."

    if not basement_see_myer_chan:

        pause 1.0

        show character_icon_box_1:
            xpos 1350 ypos 50
            easein_expo 1.0 xpos 800 ypos 50
            xpos 800 ypos 50
        show vin_icon_high_brow_satire:
            xpos 1350 ypos 50
            easein_expo 1.0 xpos 800 ypos 48
            xpos 800 ypos 48
        show character_icon_box_2:
            xpos 1350 ypos 50
            easein_expo 1.0 xpos 800 ypos 50
            xpos 800 ypos 50

        window show

        vin "\"Vanora, {w=0.5}may I ask what your thoughts on the design of Myer-chan are?\""

        window hide

        hide character_icon_box_1
        hide vin_icon_high_brow_satire
        hide character_icon_box_2
        with Dissolve(0.5)

    show basement_4:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    $ renpy.pause(0.5, hard='True')

    if not basement_see_myer_chan:

        $ basement_see_myer_chan = True

        show vin_high_brow_satire at vin_pos_2
        $ renpy.transition(Dissolve(0.5))
        $ renpy.pause(0.5, hard='True')

        show character_icon_box:
            xpos 200 ypos 250
        show van_icon_normal:
            xpos 200 ypos 248
        with Dissolve(0.5)

        $ say_who = _("Vanora")

        window show

        v "\"...The intent of mascots is generally to serve as a bridge between the brand and the user, {w=0.5}reflecting the companies' spirit and strengths.\""


        hide van_icon_normal
        show character_icon_box:
            xpos 200 ypos 250
        show van_icon_close_eye:
            xpos 200 ypos 248

        v "\"Myer-chan's look as a mechanical prosthesis may be a bit too straightforward for many people.\""

        v "\"But I don't think there's any harm in a unique and comical design like this.\""

        show van_icon_normal:
            xpos 200 ypos 248
        hide van_icon_close_eye

        v "\"If you place Myer-chan next to other corporate mascots,\""

        v "\"It would stand out simply by making people go 'Huh? {w=0.5}What's this supposed to be?', {w=0.5}which is also an advantage in some sense.\""

        show vin_close_eye at vin_pos_2
        hide vin_high_brow_satire
        with Dissolve(0.2)

        vin "\"...In other words, {w=0.5}you believe Myer-chan has an advantage as a mascot simply because its design is too peculiar, {w=0.5}not because it's truly a qualified design?\""

        hide van_icon_normal
        show van_icon_close_eye:
            xpos 200 ypos 248
        with Dissolve(0.2)

        v "\"If you have to put it that way, {w=0.5}then yes.\""

        show van_icon_normal:
            xpos 200 ypos 248
        hide van_icon_close_eye
        hide vin_close_eye
        show vin_normal at vin_pos_2
        with Dissolve(0.2)

        v "\"What about you? {w=0.5}As a former lawyer at Myers Corporation, {w=0.5}what's your opinion on its design?\""

        $ renpy.music.set_volume(0.4, delay=0, channel='sound')
        play sound "music/vin_hmm.ogg"

        hide vin_normal
        show vin_thoughtful at vin_pos_2
        with Dissolve(0.2)

        vin "\"I thought it looked so hideous that I gave mine to Victor.\""

        show van_icon_speechless:
            xpos 200 ypos 248
        hide van_icon_normal
        with Dissolve(0.2)

        v "\"...I guess I can't really blame you for that.\""

        window hide

        $ say_who = ""

        hide van_icon_speechless
        hide character_icon_box
        hide vin_thoughtful
        $ renpy.transition(Dissolve(0.5))
        $ renpy.pause(0.5, hard='True')

    $ renpy.block_rollback()
    $ _rollback = False
    $ rollback_ = False
    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False

    hide basement_4
    scene basement_4

    call screen basement_room_4_screen with Dissolve(0.2)

label basement_room_4_cut_myer_chan:


    $ store.inventory.append(iBasementKnife)
    $ setattr(iBasementKnife, "selected", False)

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/selectsounds.ogg"

    show basement_4 at Position(xpos = 0, ypos = 0):
        alpha 1 xoffset 0 yoffset 0
    show basement_4_2 at Position(xpos = 0, ypos = 0):
        alpha 0 xoffset 0 yoffset 0

    show basement_4:
        ease 0.5 zoom 1.6 xoffset 300 yoffset 400
    show basement_4_2:
        ease 0.5 zoom 1.6 xoffset 300 yoffset 400

    pause 0.5

    v "I took out my scalpel and cut off a portion of the solidified glue along the edge of the poster, {w=0.5}then tore the entire thing off."

    $ rollback_ = True

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/basement/zs_tear_paper.ogg")

    show basement_4_2:
        ease 0.5 alpha 1.0

    $ renpy.pause(1.5, hard='True')

    show character_icon_box:
        xpos 200 ypos 250
    show van_icon_normal:
        xpos 200 ypos 248
    with Dissolve(0.3)

    v "!?"

    v "\"There's another poster hidden underneath Myers-chan's poster.\""

    show character_icon_box_1:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 800 ypos 50
        xpos 800 ypos 50
    show vin_icon_high_brow_satire:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 800 ypos 48
        xpos 800 ypos 48
    show character_icon_box_2:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 800 ypos 50
        xpos 800 ypos 50

    vin "\"And the seemingly lovely, {w=0.5}innocent Vanora has a secret hidden scalpel. {w=0.5}This world sure is full of surprises.\""

    hide character_icon_box_1
    hide vin_icon_high_brow_satire
    hide character_icon_box_2
    hide character_icon_box
    hide van_icon_normal
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    show basement_4:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0
    show basement_4_2:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0
    $ renpy.pause(0.5, hard='True')

    $ renpy.block_rollback()
    $ _rollback = False
    $ rollback_ = False
    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False

    $ basement_4_layer_1 = True
    scene basement_4

    call screen basement_room_4_screen with Dissolve(0.2)

label basement_room_4_investigate_lev_poster:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show basement_4 at Position(xpos = 0, ypos = 0)

    show basement_4:
        ease 0.5 zoom 1.6 xoffset 300 yoffset 400

    pause 0.5

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    v "There is another poster hidden beneath Myers-chan's poster."

    $ rollback_ = True

    if not basement_check_lev_poster:

        stop music fadeout 3.0

        show character_icon_box_1:
            subpixel True
            xpos 1350 ypos 50
            easein_expo 1.0 xpos 800 ypos 50
            xpos 800 ypos 50
        show vin_icon_smile:
            subpixel True
            xpos 1350 ypos 50
            easein_expo 1.0 xpos 800 ypos 48
            xpos 800 ypos 48
        show character_icon_box_2:
            subpixel True
            xpos 1350 ypos 50
            easein_expo 1.0 xpos 800 ypos 50
            xpos 800 ypos 50

        vin "\"Vanora, {w=0.5}do you know the name of this work?\""

        show character_icon_box:
            xpos -370 ypos 250
            easein_circ 1.0 xpos 200 ypos 250
            xpos 200 ypos 250
        show van_icon_normal:
            xpos -370 ypos 248
            easein_circ 1.0 xpos 200 ypos 248
            xpos 200 ypos 248

        v "\"...No, {w=0.5}I don't.\""

        $ renpy.music.set_volume(1.0, delay=0, channel='music')
        play music ("music/TenseMusic.ogg") fadein 6.0

        hide character_icon_box_1
        hide character_icon_box_2
        hide vin_icon_smile
        hide character_icon_box
        hide van_icon_normal
        with Dissolve(0.5)

        show basement_4:
            ease 0.5 zoom 1.0 xoffset 0 yoffset 0
        $ renpy.pause(0.5, hard='True')

        show vin_normal at vin_pos_2
        $ renpy.transition(Dissolve(0.5))
        $ renpy.pause(0.5, hard='True')

        show vin_smile at vin_pos_2
        with Dissolve(0.2)

        $ say_who = _("Vincent")

        window show

        vin "\"{color=#f00}'The Destruction of Leviathan'{/color}.\""

        window hide

        show black:
            alpha 0.8
        with Dissolve(0.5)
        show basement_4_lev_zoom

        window show

        vin "\"It is written in the Book of Isaiah that when God comes to Earth on Judgment Day, {w=0.5}he will punish Leviathan and slay him.\""

        vin "\"'The Destruction of Leviathan' depicts this scene. {w=0.5}Leviathan is the great sea serpent.\""

        show vin_close_eye behind black at vin_pos_2
        with Dissolve(0.2)

        vin "\"In the upper right corner of the original work, {w=0.5}God can be seen in the sky handling a sword with a fierce look.\""

        vin "\"But in this poster, {w=0.5}that part has been cut off. {w=0.5}We can only vaguely see his lower limbs.\""

        v "\"So whoever put the poster up here simply wanted Leviathan to be the center of attention.\""

        hide vin_close_eye with Dissolve(0.2)

        vin "\"In the Book of Job, {w=0.5}Leviathan is portrayed as a vicious creature that is so fierce that anyone who witnesses him will be terrified and overwhelmed.\""

        vin "\"He has teeth so terrible and a mouth so strong that nobody can open with force.\""

        vin "\"His eyes are depicted as the great light of the morning and his heart as an unbreakable block of stone.\""

        show vin_close_eye behind black at vin_pos_2
        with Dissolve(0.2)

        vin "\"It is worth mentioning that {color=#f00}'Leviathan' is also the name of a well-known work of political philosophy{/color}.\""

        window hide

        $ say_who = ""

        hide black
        hide basement_4_lev_zoom
        hide vin_close_eye
        hide vin_smile
        $ renpy.transition(Dissolve(0.5))
        $ renpy.pause(1.0, hard='True')

        show character_icon_box:
            xpos 200 ypos 250
        show van_icon_normal:
            xpos 200 ypos 248
        with Dissolve(0.5)

        window show

        v "!?"

        v "\"Did you just say that 'Leviathan' is also the name of a philosophical work?\""

        show vin_smile at vin_pos_2
        with Dissolve(0.2)

        stop music fadeout 3.0

        vin "\"Yes. {w=0.5}In the book, {w=0.5}Leviathan is a symbol of power, {w=0.5}and a metaphor for the author's ideal commonwealth and perfect government.\""

        window hide

        hide vin_smile
        with Dissolve(0.2)

        $ renpy.music.set_volume(1.0, delay=0, channel='music')
        play music ("music/Tunnel/myersSewers.ogg")

        hide vin_normal
        hide character_icon_box
        hide van_icon_normal
        $ renpy.transition(Dissolve(0.5))
        $ renpy.pause(0.5, hard='True')


        $ basement_check_lev_poster = True
    else:


        show black:
            alpha 0.8
        with Dissolve(0.5)
        show basement_4_lev_zoom

        v "Vincent told me that the name of the sea serpent is Leviathan. {w=0.5}It is also the name of a philosophical work."

        hide black
        hide basement_4_lev_zoom
        with Dissolve(0.5)

        show basement_4:
            ease 0.5 zoom 1.0 xoffset 0 yoffset 0
        $ renpy.pause(0.5, hard='True')

    $ renpy.block_rollback()
    $ _rollback = False
    $ rollback_ = False
    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False

    hide basement_4
    scene basement_4

    call screen basement_room_4_screen with Dissolve(0.2)

label basement_room_4_investigate_drawer_1:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show basement_4 at Position(xpos = 0, ypos = 0)

    show basement_4:
        ease 0.5 zoom 1.6 xoffset 75 yoffset 75

    jump basement_room_4_investigate_drawer_end

label basement_room_4_investigate_drawer_2:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show basement_4 at Position(xpos = 0, ypos = 0)

    show basement_4:
        ease 0.5 zoom 1.6 xoffset -380 yoffset 75

    jump basement_room_4_investigate_drawer_end

label basement_room_4_investigate_drawer_end:

    $ renpy.pause(0.5, hard='True')

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    v "A drawer."

    $ rollback_ = True

    $ renpy.music.set_volume(0.7, delay=0, channel='sound')
    play sound ("music/drawer.ogg")

    $ renpy.pause(1.0, hard='True')

    v "I slide-opened it and took a look."

    v "Inside were just some discarded papers."

    show basement_4:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0
    $ renpy.pause(0.5, hard='True')

    $ renpy.block_rollback()
    $ _rollback = False
    $ rollback_ = False
    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False

    hide basement_4
    scene basement_4

    call screen basement_room_4_screen with Dissolve(0.2)

label basement_room_4_investigate_cupboard_1:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show basement_4 at Position(xpos = 0, ypos = 0)

    show basement_4:
        ease 0.5 zoom 1.6 xoffset 75 yoffset 20

    if basement_4_layer_2:
        jump basement_room_4_investigate_cupboard_end
    else:
        jump basement_room_4_break_cup

label basement_room_4_investigate_cupboard_2:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show basement_4 at Position(xpos = 0, ypos = 0)

    show basement_4:
        ease 0.5 zoom 1.6 xoffset -380 yoffset 20

    jump basement_room_4_investigate_cupboard_end

label basement_room_4_investigate_cupboard_end:

    $ renpy.pause(0.5, hard='True')

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    v "A cupboard under a drawer."

    $ rollback_ = True

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/engineering room/Cupboard_open.ogg")

    pause 1.0

    v "I opened it and took a look."

    v "There was nothing in it."

    show basement_4:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    $ renpy.pause(0.5, hard='True')

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    $ renpy.block_rollback()
    $ _rollback = False

    hide basement_4
    scene basement_4

    call screen basement_room_4_screen with Dissolve(0.2)

label basement_room_4_break_cup:

    pause 0.5

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    v "A cupboard under a drawer."

    $ rollback_ = True

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/engineering room/Cupboard_open.ogg")

    $ renpy.pause(1.0, hard='True')

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound ("music/Tunnel/glass break.ogg")

    with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    v "!?"

    pause 1.0

    v "A white mug fell out and shattered on the floor."

    stop music fadeout 3.0

    show basement_4:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    $ renpy.pause(0.5, hard='True')

    show basement_4_3
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(1.0, hard='True')

    show character_icon_box_1:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 800 ypos 50
        xpos 800 ypos 50
    show vin_icon_dark:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 800 ypos 48
        xpos 800 ypos 48
    show character_icon_box_2:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 800 ypos 50
        xpos 800 ypos 50

    vin "\"......\""

    hide character_icon_box_1
    hide vin_icon_dark
    hide character_icon_box_2
    with Dissolve(0.5)

    v "For some reason, {w=0.5}Vincent's face turned sullen."

    $ renpy.pause(0.5, hard='True')

    show character_icon_box:
        xpos 200 ypos 250
    show van_icon_normal:
        xpos 200 ypos 248
    with Dissolve(0.5)

    v "\"Are you mad at me for breaking the mug, {w=0.5}Vincent?\""

    show vin_dark at vin_pos_2
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(1.0, hard='True')

    vin "\"...No. {w=0.5}Why would I be mad about...\""

    hide vin_dark
    hide character_icon_box
    hide van_icon_normal
    with Dissolve(0.2)

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/dorm/zs_collapse.ogg" fadeout 1.0

    with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    pause 0.5

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/shock2.ogg" fadeout 2.0

    v "!?" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    v "Vincent suddenly lost his balance. {w=0.5}Without the support of the wall, {w=0.5}he might have already fallen to the floor."

    v "\"Vincent!? {w=0.5}Are you okay?\""

    vin "\"No, {w=0.5}don't come any closer.\""

    v "Vincent held out one of his hands, {w=0.5}telling me not to come closer."

    show vin_dark at vin_pos_2
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    vin "\"I'm fine. {w=0.5}I don't need you to worry about me.\""

    v "Leaning against the cupboard by the wall, {w=0.5}he regained his footing."

    vin "\"...Let's continue our investigation.\""

    show character_icon_box:
        xpos 200 ypos 250
    show van_icon_normal:
        xpos 200 ypos 248
    with Dissolve(0.5)

    v "\"......\""

    hide character_icon_box
    hide van_icon_normal
    hide vin_dark
    with Dissolve(0.5)

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music ("music/Tunnel/myersSewers.ogg")


    $ basement_4_layer_2 = True

    scene basement_4

    $ renpy.block_rollback()
    $ _rollback = False
    $ rollback_ = False
    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False

    call screen basement_room_4_screen with Dissolve(0.2)

label basement_room_4_investigate_cup:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show basement_4 at Position(xpos = 0, ypos = 0)

    show basement_4:
        ease 0.5 zoom 3.0 xoffset 500 yoffset 20

    pause 0.5

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    $ renpy.pause(0.1, hard='True')

    show basement_4_cup_zoom
    show black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    hide black
    with Dissolve(0.5)

    if not basement_check_cup_zoom:

        $ basement_check_cup_zoom = True

        v "A shattered mug."

        $ rollback_ = True

        v "The moment I opened the cupboard, {w=0.5}a white mug fell out and shattered on the floor."

        v "Why would someone leave a mug full of fluid in such a place?"

    $ renpy.block_rollback()
    $ _rollback = False
    $ rollback_ = False
    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False

    call screen basement_room_4_cup_screen

label basement_room_4_investigate_cup_zoom:

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/selectsounds.ogg"

    window show

    v "Investigate the mug?"

    window hide

    menu:
        "Yes":
            $ _skipping = True
            $ renpy.block_rollback()
            $ _rollback = True

            hide screen inventory_screen
            with Dissolve(0.2)

            $ renpy.pause(1.0, hard='True')

            show character_icon_box_1:
                xpos 1350 ypos 50
                easein_expo 1.0 xpos 800 ypos 50
                xpos 800 ypos 50
            show vin_icon_smile:
                xpos 1350 ypos 50
                easein_expo 1.0 xpos 800 ypos 48
                xpos 800 ypos 48
            show character_icon_box_2:
                xpos 1350 ypos 50
                easein_expo 1.0 xpos 800 ypos 50
                xpos 800 ypos 50

            vin "\"Be careful, {w=0.5}Vanora. {w=0.5}Don't hurt yourself.\""

            $ rollback_ = True

            hide character_icon_box_1
            hide vin_icon_smile
            hide character_icon_box_2
            with Dissolve(0.5)

            $ renpy.music.set_volume(0.1, delay=0, channel='sound')
            play sound "music/cloth.mp3" fadeout 2.0

            pause 1.0

            v "I squatted down and carefully touched one of the shards with the tip of my finger."

            $ renpy.pause(0.5, hard='True')



            show basement_4_cup_zoom_blurred:
                ease 0.4 xoffset -10 yoffset -10 alpha 0.5
                ease 0.4 xoffset 10 yoffset -10 alpha 0.5
                ease 0.4 xoffset -10 yoffset 10 alpha 0.5
                ease 0.4 xoffset 10 yoffset 10 alpha 0.5
                ease 0.4 xoffset 0 yoffset 0 alpha 1.0

            $ renpy.pause(0.1, hard='True')

            $ renpy.music.set_volume(1.0, delay=0, channel='sound')
            play sound "music/heartbeat.ogg"

            show bedroom_headache
            $ renpy.transition(Dissolve(0.4))
            $ renpy.pause(0.4, hard='True')

            hide bedroom_headache
            $ renpy.transition(Dissolve(0.4))
            $ renpy.pause(0.4, hard='True')

            show bedroom_headache
            $ renpy.transition(Dissolve(0.4))
            $ renpy.pause(0.4, hard='True')

            hide bedroom_headache
            $ renpy.transition(Dissolve(0.4))
            $ renpy.pause(0.4, hard='True')

            $ renpy.pause(0.1, hard='True')

            hide basement_4_cup_zoom_blurred
            $ renpy.transition(Dissolve(1.0))
            $ renpy.pause(1.0, hard='True')

            pause 1.0

            v "......?"

            if renpy.is_skipping():
                $ renpy.choice_for_skipping()
            $ _skipping = False
            $ rollback_ = False
            $ renpy.music.stop(channel="beep", fadeout = 0.5)
            $ renpy.block_rollback()
            $ _rollback = False

            scene black
            show white back
            $ renpy.transition(Dissolve(0.1))
            $ renpy.pause(0.1, hard='True')

            stop music

            $ renpy.music.set_volume(0.7, delay=0, channel='sound')
            play sound "music/teleport.ogg"

            $ renpy.pause(1.0, hard='True')

            hide white back
            $ renpy.transition(Dissolve(1.0))
            $ renpy.pause(1.0, hard='True')

            jump basement_m_past_start
        "No":

            call screen basement_room_4_cup_screen

label basement_4_finish_investigate_cup:

    hide basement_4_cup_zoom
    show black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')


    show basement_4 behind black:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0
    show black:
        linear 0.5 alpha 0

    $ renpy.pause(0.5, hard='True')

    hide black

    scene basement_4

    $ renpy.block_rollback()
    $ _rollback = False
    $ rollback_ = False
    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False

    call screen basement_room_4_screen with Dissolve(0.2)

label basement_room_4_teleport:

    stop music fadeout 1.0

    hide screen inventory_screen
    scene basement_m_desk
    show white back
    $ renpy.transition(Dissolve(0.1))
    $ renpy.pause(0.1, hard='True')

    stop music

    $ renpy.music.set_volume(0.7, delay=0, channel='sound')
    play sound "music/teleport.ogg"

    $ renpy.pause(0.3, hard='True')

    hide white back
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    $ renpy.music.set_volume(0.7, delay=0, channel='music')
    play music ("music/bgm/M office bgm.ogg")

    call screen basement_m_table_screen

label basement_room_4_investigate_air_vent:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show basement_4 at Position(xpos = 0, ypos = 0)

    show basement_4:
        ease 0.5 zoom 2.0 xoffset -640 yoffset 700

    pause 0.5

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    v "Ventilation duct opening. {w=0.5}Nothing special about it."

    show basement_4:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    $ renpy.pause(0.5, hard='True')

    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)
    $ renpy.block_rollback()
    $ _rollback = False
    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False

    hide basement_4
    scene basement_4

    call screen basement_room_4_screen with Dissolve(0.2)

label basement_room_4_investigate_box:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show basement_4 at Position(xpos = 0, ypos = 0)

    show basement_4:
        ease 0.5 zoom 2.0 xoffset -320 yoffset 450

    pause 0.5

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    $ renpy.pause(0.1, hard='True')

    show basement_4_box_zoom_1
    show black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.pause(0.1, hard='True')

    hide black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    v "Huh? {w=0.5}What is this?"

    $ rollback_ = True

    v "There seems to be some kind of pink box embedded in the surface of the table."

    hide basement_4_box_zoom_1
    show black
    with Dissolve(0.5)

    show black:
        linear 0.5 alpha 0

    show basement_4:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0
    $ renpy.pause(0.5, hard='True')

    hide black

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    $ renpy.block_rollback()
    $ _rollback = False

    hide basement_4
    scene basement_4

    call screen basement_room_4_screen with Dissolve(0.2)

label basement_room_4_investigate_puzzle:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show basement_4 at Position(xpos = 0, ypos = 0)

    show basement_4:
        ease 0.5 zoom 2.0 xoffset -320 yoffset 350

    $ renpy.pause(0.5, hard='True')

    show black:
        alpha 0.8
    with Dissolve(0.5)

    show basement_4_puzzle_zoom:
        ypos -40

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    if not basement_see_flashback:

        pause 1.0

        v "Some kind of keypad. {w=0.5}The buttons have been switched from their usual numbers to colors."

        $ rollback_ = True

        v "I don't know what to enter yet. {w=0.5}I need to gather more clues."
    else:


        jump basement_4_puzzle_screen_start

label basement_4_puzzle_leave:

    $ basement_4_num_enter_passcode = 0

    $ basement_4_entered_passcode = list("")

    hide basement_4_puzzle_zoom
    hide black
    with Dissolve(0.5)

    show basement_4:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    $ renpy.pause(0.5, hard='True')

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    $ renpy.block_rollback()
    $ _rollback = False

    hide basement_4
    scene basement_4

    call screen basement_room_4_screen with Dissolve(0.2)

label basement_room_4_investigate_box_2:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show basement_4 at Position(xpos = 0, ypos = 0)

    show basement_4:
        ease 0.5 zoom 2.0 xoffset -320 yoffset 450

    pause 0.5

    $ renpy.pause(0.1, hard='True')

    show basement_4_box_zoom_2
    show basement_4_box_zoom_4
    show basement_4_box_zoom_3
    show black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.pause(0.1, hard='True')

    hide black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    v "A mysterious box. {w=0.5}There is a keyhole in it."

    hide basement_4_box_zoom_2
    hide basement_4_box_zoom_4
    hide basement_4_box_zoom_3
    show black
    with Dissolve(0.5)

    show black:
        linear 0.5 alpha 0

    show basement_4:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    $ renpy.pause(0.5, hard='True')

    hide black

    call screen basement_room_4_screen with Dissolve(0.2)

label basement_room_4_unlock_box:

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/weapon click.ogg"

    show basement_4 at Position(xpos = 0, ypos = 0)

    show basement_4:
        ease 0.5 zoom 2.0 xoffset -320 yoffset 450

    pause 0.5

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    v "The box is unlocked."

    $ rollback_ = True

    show transparent dark-small:
        alpha 0.6
    with Dissolve(0.5)

    pause 0.5

    v "What I find inside is..."

    show basement_photo
    with Dissolve(0.5)

    pause 1.0

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/shock2.ogg" fadeout 2.0

    v "!?" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    v "Is, {w=0.5}is this!?"

    show character_icon_box_1:
        xpos 870 ypos 50
    show vin_icon_slight_embarassed:
        xpos 870 ypos 48
    show character_icon_box_2:
        xpos 870 ypos 50
    with Dissolve(0.5)

    vin "\"Gucci, {w=0.5}Penelope, {w=0.5}and Boss. {w=0.5}Those are the names of my three cats.\""

    v "\"Victor's eyes and arms... {w=0.5}Isn't this a picture of you guys at university?\""

    vin "\"......\""

    hide character_icon_box_1
    hide vin_icon_slight_embarassed
    hide character_icon_box_2
    with Dissolve(0.5)

    pause 1.0

    v "Vincent didn't answer. {w=0.5}He looked away to the other side of the room."

    show basement_photo:
        ease 0.3 zoom 0.8 yoffset -130

    $ renpy.pause(0.5, hard='True')

    $ renpy.block_rollback()
    $ _rollback = False
    $ rollback_ = False
    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False

    call screen basement_room_4_photo_screen

label basement_4_finish_investigate_photo:

    hide basement_photo
    hide transparent dark-small
    with Dissolve(0.5)

    show basement_4:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    $ renpy.pause(0.5, hard='True')

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    $ renpy.block_rollback()
    $ _rollback = False

    call screen basement_room_4_screen with Dissolve(0.2)

label basement_room_4_investigate_box_3:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show basement_4 at Position(xpos = 0, ypos = 0)

    show basement_4:
        ease 0.5 zoom 2.0 xoffset -320 yoffset 450

    pause 0.5

    show transparent dark-small:
        alpha 0.6
    with Dissolve(0.5)

    show basement_photo:
        zoom 0.8 xoffset 125 yoffset 10

    call screen basement_room_4_photo_screen
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
