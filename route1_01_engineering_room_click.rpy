
init 2 python:

    iEngineeringRoomKey = Item("EngineeringRoomKey","images/Engineering Room 1/Engineering_room_key_object.png")
    iEngineeringRoomTape = Item("EngineeringRoomTape","images/Engineering Room 1/Engineering_room_tape_object.png")
    iEngineeringRoomKnife = Item("EngineeringRoomKnife","images/Engineering Room 1/Engineering_room_knife_object.png")

label route_1_engineering_room_click_start:

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False


    $ active_item = None

    $ inventory = []
    scene engineering_room_1


    $ engineering_room_investigate_vent = False
    $ engineering_room_investigate_gate = False
    $ engineering_room_investigate_arm_circle = False
    $ engineering_room_investigate_trophy = False
    $ engineering_room_investigate_broken_drawer = False
    $ engineering_room_has_key = False
    $ engineering_room_used_key = False
    $ engineering_room_used_tape = False
    $ engineering_room_used_knife = False
    $ engineering_room_investigate_puzzle = False
    $ engineering_room_click_puzzle_screen = False
    $ engineering_room_puzzle_solved = False
    $ engineering_room_visit_secret_lab = False


    $ engineering_room_4_image = "images/Engineering Room 1/Engineering_room_4.png"

    $ renpy.pause(0.5, hard='True')

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/UI Dark.ogg"

    noname "Objective: {w=0.5}Find Zalmona's item."

    window hide

    $ rollback_ = False
    $ renpy.block_rollback()
    $ _rollback = False

    show screen inventory_screen
    with Dissolve(0.2)

    call screen engineering_room_1_screen with Dissolve(0.1)

label engineering_room_1_to_2_switch:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/scan map.ogg"


    $ renpy.pause(0.01, hard='True')







    show engineering_room_1:
        linear 0.3 xoffset -1280
    show engineering_room_2:
        xoffset 1280
        linear 0.3 xoffset 0
    show zalmona_drop_shadow:
        xoffset 1530
        linear 0.3 xoffset 255
    show zalmona_normal:
        xoffset 1530
        linear 0.3 xoffset 255
    $ renpy.pause(0.3, hard='True')

    scene engineering_room_2
    show zalmona_drop_shadow at zal_pos_2
    show zalmona_normal at zal_pos_2



    call screen engineering_room_2_screen with Dissolve(0.1)

label engineering_room_2_to_1_switch:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/scan map.ogg"


    $ renpy.pause(0.01, hard='True')




    show engineering_room_2:
        linear 0.3 xoffset 1280
    show zalmona_drop_shadow:
        linear 0.3 xoffset 1280
    show zalmona_normal:
        linear 0.3 xoffset 1280
    show engineering_room_1:
        xoffset -1280
        linear 0.3 xoffset 0
    $ renpy.pause(0.3, hard='True')

    scene engineering_room_1



    call screen engineering_room_1_screen with Dissolve(0.1)

label engineering_room_2_to_3_switch:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/scan map.ogg"


    $ renpy.pause(0.01, hard='True')





    show engineering_room_2:
        linear 0.3 xoffset -1280
    show zalmona_drop_shadow:
        linear 0.3 xoffset -1280
    show zalmona_normal:
        linear 0.3 xoffset -1280
    show engineering_room_3:
        xoffset 1280
        linear 0.3 xoffset 0
    $ renpy.pause(0.3, hard='True')

    scene engineering_room_3



    call screen engineering_room_3_screen with Dissolve(0.1)

label engineering_room_3_to_2_switch:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/scan map.ogg"


    $ renpy.pause(0.01, hard='True')







    show engineering_room_3:
        linear 0.3 xoffset 1280
    show engineering_room_2:
        xoffset -1280
        linear 0.3 xoffset 0
    show zalmona_drop_shadow:
        xoffset -1030
        linear 0.3 xoffset 255
    show zalmona_normal:
        xoffset -1030
        linear 0.3 xoffset 255
    $ renpy.pause(0.3, hard='True')

    scene engineering_room_2
    show zalmona_drop_shadow at zal_pos_2
    show zalmona_normal at zal_pos_2



    call screen engineering_room_2_screen with Dissolve(0.1)

label engineering_room_3_to_4_switch:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/scan map.ogg"


    $ renpy.pause(0.01, hard='True')





    show engineering_room_3:
        xoffset 0
        linear 0.3 xoffset -1280
    show engineering_room_4:
        xoffset 1280
        linear 0.3 xoffset 0
    $ renpy.pause(0.3, hard='True')

    scene engineering_room_4



    call screen engineering_room_4_screen with Dissolve(0.1)

label engineering_room_4_to_1_switch:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/scan map.ogg"


    $ renpy.pause(0.01, hard='True')





    show engineering_room_1:
        xoffset 1280
        linear 0.3 xoffset 0
    show engineering_room_4:
        linear 0.3 xoffset -1280
    $ renpy.pause(0.3, hard='True')

    scene engineering_room_1



    call screen engineering_room_1_screen with Dissolve(0.1)

label engineering_room_4_to_3_switch:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/scan map.ogg"


    $ renpy.pause(0.01, hard='True')





    show engineering_room_4:
        linear 0.3 xoffset 1280
    show engineering_room_3:
        xoffset -1280
        linear 0.3 xoffset 0
    $ renpy.pause(0.3, hard='True')

    scene engineering_room_3



    call screen engineering_room_3_screen with Dissolve(0.1)

label engineering_room_1_to_4_switch:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/scan map.ogg"


    $ renpy.pause(0.01, hard='True')





    show engineering_room_1:
        linear 0.3 xoffset 1280
    show engineering_room_4:
        xoffset -1280
        linear 0.3 xoffset 0
    $ renpy.pause(0.3, hard='True')

    scene engineering_room_4



    call screen engineering_room_4_screen with Dissolve(0.1)

screen engineering_room_1_screen:

    imagebutton:
        xpos 980
        ypos 43
        idle "images/Engineering Room 1/Engineering_room_vent_idle.png"
        hover "images/Engineering Room 1/Engineering_room_vent_hover.png"
        focus_mask "images/Engineering Room 1/Engineering_room_vent_hover.png"
        action checkInteractionValid("engineering_room_1_screen", "engineering_room_1_investigate_vent")

    imagebutton:
        xpos 348
        ypos 0
        idle "images/Engineering Room 1/Engineering_room_1_gate_idle.png"
        hover "images/Engineering Room 1/Engineering_room_1_gate_hover.png"
        focus_mask "images/Engineering Room 1/Engineering_room_1_gate_hover.png"
        action checkInteractionValid("engineering_room_1_screen", "engineering_room_1_investigate_gate")

    imagebutton:
        xpos 786
        ypos 231
        idle "images/Engineering Room 1/Engineering_room_arm_3_idle.png"
        hover "images/Engineering Room 1/Engineering_room_arm_4_hover.png"
        focus_mask "images/Engineering Room 1/Engineering_room_arm_4_hover.png"
        action checkInteractionValid("engineering_room_1_screen", "engineering_room_1_investigate_arm_4")

    imagebutton:
        xpos 155
        ypos 231
        idle "images/Engineering Room 1/Engineering_room_arm_3_idle.png"
        hover "images/Engineering Room 1/Engineering_room_arm_3_hover.png"
        focus_mask "images/Engineering Room 1/Engineering_room_arm_3_hover.png"
        action checkInteractionValid("engineering_room_1_screen", "engineering_room_1_investigate_arm_3")

    imagebutton:
        xpos 0
        ypos 379
        idle "images/Engineering Room 1/Engineering_room_arm_1_idle.png"
        hover "images/Engineering Room 1/Engineering_room_arm_1_hover.png"
        focus_mask "images/Engineering Room 1/Engineering_room_arm_1_hover.png"
        action checkInteractionValid("engineering_room_1_screen", "engineering_room_1_investigate_arm_1")

    imagebutton:
        xpos 834
        ypos 379
        idle "images/Engineering Room 1/Engineering_room_arm_1_idle.png"
        hover "images/Engineering Room 1/Engineering_room_arm_2_hover.png"
        focus_mask "images/Engineering Room 1/Engineering_room_arm_2_hover.png"
        action checkInteractionValid("engineering_room_1_screen", "engineering_room_1_investigate_arm_2")

    imagebutton:
        xpos 30
        ypos 560
        idle "images/myers-click/left-black-arrow-small-small.png"
        hover "images/myers-click/left-white-arrow-small-small.png"
        focus_mask "images/myers-click/left-black-arrow-small-small.png"
        action Jump("engineering_room_1_to_4_switch")

    imagebutton:
        xpos 1030
        ypos 560
        idle "images/myers-click/right-black-arrow-small-small.png"
        hover "images/myers-click/right-white-arrow-small-small.png"
        focus_mask "images/myers-click/right-black-arrow-small-small.png"
        action Jump("engineering_room_1_to_2_switch")

screen engineering_room_2_screen:

    imagebutton:
        xpos 223
        ypos 64
        idle "images/Engineering room 1/Engineering_room_2_door_idle.png"
        hover "images/Engineering room 1/Engineering_room_2_door_hover.png"
        focus_mask "images/Engineering room 1/Engineering_room_2_door_hover.png"
        action [Hide("displayTextScreenGeneral"), checkInteractionValid("engineering_room_2_screen", "engineering_room_2_investigate_door")]

    imagebutton:
        xpos 550
        ypos 207
        idle "images/Engineering room 1/Engineering_room_2_key_scanner_idle.png"
        hover "images/Engineering room 1/Engineering_room_2_key_scanner_hover.png"
        focus_mask "images/Engineering room 1/Engineering_room_2_key_scanner_hover.png"
        action NullAction()
        hovered Show("displayTextScreenGeneral", displayText = _(" I need Zalmona's key card "), xalign_value=0.5, yalign_value=0.35)
        unhovered Hide("displayTextScreenGeneral")

    imagebutton:
        xpos 30
        ypos 560
        idle "images/myers-click/left-black-arrow-small-small.png"
        hover "images/myers-click/left-white-arrow-small-small.png"
        focus_mask "images/myers-click/left-black-arrow-small-small.png"
        action [Hide("displayTextScreenGeneral"), Jump("engineering_room_2_to_1_switch")]

    imagebutton:
        xpos 1030
        ypos 560
        idle "images/myers-click/right-black-arrow-small-small.png"
        hover "images/myers-click/right-white-arrow-small-small.png"
        focus_mask "images/myers-click/right-black-arrow-small-small.png"
        action [Hide("displayTextScreenGeneral"), Jump("engineering_room_2_to_3_switch")]

    imagebutton:
        xpos 645
        ypos 350
        idle "images/myers-click/dialogue-idle-crop-small.png"
        hover "images/myers-click/dialogue-hover-crop-small.png"
        focus_mask "images/myers-click/dialogue-hover-crop-small.png"
        action [Hide("displayTextScreenGeneral"), Jump("engineering_room_2_talk_zalmona")]

screen engineering_room_3_screen:

    imagebutton:
        xpos 980
        ypos 43
        idle "images/Engineering Room 1/Engineering_room_vent_idle.png"
        hover "images/Engineering Room 1/Engineering_room_vent_hover.png"
        focus_mask "images/Engineering Room 1/Engineering_room_vent_hover.png"
        action [Hide("displayTextScreenGeneral"), checkInteractionValid("engineering_room_3_screen", "engineering_room_3_investigate_vent")]

    imagebutton:
        xpos 786
        ypos 231
        idle "images/Engineering Room 1/Engineering_room_arm_3_idle.png"
        hover "images/Engineering Room 1/Engineering_room_arm_4_hover.png"
        focus_mask "images/Engineering Room 1/Engineering_room_arm_4_hover.png"
        action [Hide("displayTextScreenGeneral"), checkInteractionValid("engineering_room_3_screen", "engineering_room_3_investigate_arm_4")]

    imagebutton:
        xpos 155
        ypos 231
        idle "images/Engineering Room 1/Engineering_room_arm_3_idle.png"
        hover "images/Engineering Room 1/Engineering_room_arm_3_hover.png"
        focus_mask "images/Engineering Room 1/Engineering_room_arm_3_hover.png"
        action [Hide("displayTextScreenGeneral"), checkInteractionValid("engineering_room_3_screen", "engineering_room_3_investigate_arm_3")]

    imagebutton:
        xpos 0
        ypos 379
        idle "images/Engineering Room 1/Engineering_room_arm_1_idle.png"
        hover "images/Engineering Room 1/Engineering_room_arm_1_hover.png"
        focus_mask "images/Engineering Room 1/Engineering_room_arm_1_hover.png"
        action [Hide("displayTextScreenGeneral"), checkInteractionValid("engineering_room_3_screen", "engineering_room_3_investigate_arm_with_key")]

    imagebutton:
        xpos 834
        ypos 379
        idle "images/Engineering Room 1/Engineering_room_arm_1_idle.png"
        hover "images/Engineering Room 1/Engineering_room_arm_2_hover.png"
        focus_mask "images/Engineering Room 1/Engineering_room_arm_2_hover.png"
        action [Hide("displayTextScreenGeneral"), checkInteractionValid("engineering_room_3_screen", "engineering_room_3_investigate_arm_2")]

    imagebutton:
        xpos 413
        ypos 78
        idle "images/Engineering Room 1/Engineering_room_3_puzzle_idle.png"
        hover "images/Engineering Room 1/Engineering_room_3_puzzle_hover.png"
        focus_mask "images/Engineering Room 1/Engineering_room_3_puzzle_hover.png"
        if not engineering_room_puzzle_solved:
            action checkInteractionValid("engineering_room_3_screen", "engineering_room_3_investigate_puzzle")
        else:
            action NullAction()
            hovered Show("displayTextScreenGeneral", displayText = _(" I have solved the puzzle "), xalign_value=0.5, yalign_value=0.35)
            unhovered Hide("displayTextScreenGeneral")

    imagebutton:
        xpos 30
        ypos 560
        idle "images/myers-click/left-black-arrow-small-small.png"
        hover "images/myers-click/left-white-arrow-small-small.png"
        focus_mask "images/myers-click/left-black-arrow-small-small.png"
        action [Hide("displayTextScreenGeneral"), Jump("engineering_room_3_to_2_switch")]

    imagebutton:
        xpos 1030
        ypos 560
        idle "images/myers-click/right-black-arrow-small-small.png"
        hover "images/myers-click/right-white-arrow-small-small.png"
        focus_mask "images/myers-click/right-black-arrow-small-small.png"
        action [Hide("displayTextScreenGeneral"), Jump("engineering_room_3_to_4_switch")]

screen engineering_room_4_screen:

    imagebutton:
        xpos 871
        ypos 64
        idle "images/Engineering Room 1/Engineering_room_4_door_idle.png"
        hover "images/Engineering Room 1/Engineering_room_4_door_hover.png"
        focus_mask "images/Engineering Room 1/Engineering_room_4_door_hover.png"
        if not engineering_room_puzzle_solved:
            action checkInteractionValid("engineering_room_4_screen", "engineering_room_4_investigate_door")
        else:
            action checkInteractionValid("engineering_room_4_screen", "engineering_room_secret_lab_start")

    imagebutton:
        xpos 207
        ypos 369
        idle "images/Engineering Room 1/Engineering_room_4_drawer_idle.png"
        hover "images/Engineering Room 1/Engineering_room_4_drawer_hover.png"
        focus_mask "images/Engineering Room 1/Engineering_room_4_drawer_hover.png"
        action testItem_General(iEngineeringRoomKey,"engineering_room_used_key", True, "engineering_room_4_screen", "engineering_room_4_unlock_drawer_1", "engineering_room_4_investigate_drawer_1")

    imagebutton:
        xpos 459
        ypos 369
        idle "images/Engineering Room 1/Engineering_room_4_drawer_idle.png"
        hover "images/Engineering Room 1/Engineering_room_4_drawer_hover.png"
        focus_mask "images/Engineering Room 1/Engineering_room_4_drawer_hover.png"
        action checkInteractionValid("engineering_room_4_screen", "engineering_room_4_investigate_drawer_2")

    imagebutton:
        xpos 459
        ypos 443
        idle "images/Engineering Room 1/Engineering_room_4_cupboard_idle.png"
        hover "images/Engineering Room 1/Engineering_room_4_cupboard_hover.png"
        focus_mask "images/Engineering Room 1/Engineering_room_4_cupboard_hover.png"
        action checkInteractionValid("engineering_room_4_screen", "engineering_room_4_investigate_cupboard_2")

    imagebutton:
        xpos 207
        ypos 443
        idle "images/Engineering Room 1/Engineering_room_4_cupboard_idle.png"
        hover "images/Engineering Room 1/Engineering_room_4_cupboard_hover.png"
        focus_mask "images/Engineering Room 1/Engineering_room_4_cupboard_hover.png"
        action checkInteractionValid("engineering_room_4_screen", "engineering_room_4_investigate_cupboard_1")

    imagebutton:
        xpos 283
        ypos 230
        idle "images/Engineering Room 1/Engineering_room_4_radio_idle.png"
        hover "images/Engineering Room 1/Engineering_room_4_radio_hover.png"
        focus_mask "images/Engineering Room 1/Engineering_room_4_radio_hover.png"
        action testItem_General(iEngineeringRoomTape,"engineering_room_used_tape", True, "engineering_room_4_screen", "engineering_room_4_radio_put_in_tape", "engineering_room_4_investigate_radio")

    imagebutton:
        xpos 498
        ypos 205
        idle "images/Engineering Room 1/Engineering_room_4_trophy_idle.png"
        hover "images/Engineering Room 1/Engineering_room_4_trophy_hover.png"
        focus_mask "images/Engineering Room 1/Engineering_room_4_trophy_hover.png"
        action checkInteractionValid("engineering_room_4_screen", "engineering_room_4_investigate_trophy")

    imagebutton:
        xpos 30
        ypos 560
        idle "images/myers-click/left-black-arrow-small-small.png"
        hover "images/myers-click/left-white-arrow-small-small.png"
        focus_mask "images/myers-click/left-black-arrow-small-small.png"
        action Jump("engineering_room_4_to_3_switch")

    imagebutton:
        xpos 1030
        ypos 560
        idle "images/myers-click/right-black-arrow-small-small.png"
        hover "images/myers-click/right-white-arrow-small-small.png"
        focus_mask "images/myers-click/right-black-arrow-small-small.png"
        action Jump("engineering_room_4_to_1_switch")

label engineering_room_1_investigate_vent:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show engineering_room_1 at Position(xpos = 0, ypos = 0)

    show engineering_room_1:
        ease 0.5 zoom 3.0 xoffset -1000 yoffset 1350

    pause 0.5

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    van "Ventilation duct opening. {w=0.5}Nothing special about it."

    if not engineering_room_investigate_vent:

        $ engineering_room_investigate_vent = True

        $ rollback_ = True

        show character_icon_box:
            xpos -350 ypos 50
            easein_expo 1.0 xpos 170 ypos 50
            xpos 170 ypos 50
        show zalmona_icon_happy:
            xpos -350 ypos 50
            easein_expo 1.0 xpos 170 ypos 48
            xpos 170 ypos 48

        zal "\"Maybe we can get out of here by crawling out through this opening.\""

        van "\"......I don't think we’ll fit through.\""


        show character_icon_box:
            xpos 170 ypos 50
        show zalmona_icon_normal:
            xpos 170 ypos 48
        hide zalmona_icon_happy

        zal "\"You mean you won't fit through? {w=0.5}Or me?\""

        van "\"......I don't think either of us will fit through.\""

        show zalmona_icon_surprised:
            xpos 170 ypos 48
        hide zalmona_icon_normal

        zal "\"Huh!? {w=0.5}For real?\""

        van "......"

        hide zalmona_icon_surprised
        hide character_icon_box
        $ renpy.transition(Dissolve(0.3))
        $ renpy.pause(0.5, hard='True')

    show engineering_room_1:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    $ renpy.pause(0.5, hard='True')
    hide engineering_room_1
    scene engineering_room_1

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ renpy.block_rollback()
    $ _rollback = False
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    call screen engineering_room_1_screen with Dissolve(0.1)

label engineering_room_1_investigate_gate:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show engineering_room_1 at Position(xpos = 0, ypos = 0)

    show engineering_room_1:
        ease 0.5 zoom 1.5 xoffset 0 yoffset 350

    pause 0.5

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    van "The gate that connects Myers lobby and the lab. {w=0.5}I came in here from the other side."

    $ rollback_ = True

    van "I can't hear anything from the other side. {w=0.5}I don't know what has happened to Draco."

    if not engineering_room_investigate_gate:

        van "\"Zalmona, {w=0.5}is there really no way to reopen the gate from here?\""

    show engineering_room_1:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    $ renpy.pause(0.5, hard='True')
    hide engineering_room_1
    scene engineering_room_1

    if not engineering_room_investigate_gate:

        $ engineering_room_investigate_gate = True

        show zalmona_drop_shadow
        show zalmona_angry
        $ renpy.transition(Dissolve(0.5))
        $ renpy.pause(0.5, hard='True')

        window show

        $ say_who = _("Zalmona")

        zal "\"Huh? {w=0.5}Why don't you find it for me then?\""

        hide zalmona_angry
        show zalmona_surprised
        with Dissolve(0.2)

        zal "\"As far as I know, {w=0.5}only the front desk can control the gates on either side of the lobby.\""

        zal "\"It's a feature of the Myers security system.\""

        $ say_who = ""

        van "\"......With all due respect, {w=0.5}the security system doesn't make much sense to me.\""

        hide zalmona_surprised
        show zalmona_normal
        with Dissolve(0.2)

        zal "\"I know right? {w=0.5}I have no clue what they were thinking either.\""

        zal "\"Right now the only possible way for us to get out of here,\""

        zal "\"Is to reach the other side of Myers by taking the elevator from the basement, {w=0.5}and then go back to the lobby from there.\""

        van "\"I see...\""

        van "Then it seems that my assumptions were not wrong."

        window hide

        hide zalmona_drop_shadow
        hide zalmona_normal
        $ renpy.transition(Dissolve(0.5))
        $ renpy.pause(0.5, hard='True')

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    $ renpy.block_rollback()
    $ _rollback = False

    call screen engineering_room_1_screen with Dissolve(0.1)

label engineering_room_1_investigate_arm_1:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show engineering_room_1 at Position(xpos = 0, ypos = 0)

    show engineering_room_1:
        ease 0.5 zoom 1.5 xoffset 300 yoffset 0

    jump engineering_room_1_investigate_arm_end

label engineering_room_1_investigate_arm_2:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show engineering_room_1 at Position(xpos = 0, ypos = 0)

    show engineering_room_1:
        ease 0.5 zoom 1.5 xoffset -300 yoffset 0

    jump engineering_room_1_investigate_arm_end

label engineering_room_1_investigate_arm_3:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show engineering_room_1 at Position(xpos = 0, ypos = 0)

    show engineering_room_1:
        ease 0.5 zoom 1.5 xoffset 300 yoffset 200

    jump engineering_room_1_investigate_arm_end

label engineering_room_1_investigate_arm_end:

    $ renpy.pause(0.5, hard='True')

    van "A robotic arm. {w=0.5}Nothing special about it."

    show engineering_room_1:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    $ renpy.pause(0.5, hard='True')

    hide engineering_room_1
    scene engineering_room_1

    call screen engineering_room_1_screen with Dissolve(0.1)

label engineering_room_1_investigate_arm_4:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show engineering_room_1 at Position(xpos = 0, ypos = 0)

    show engineering_room_1:
        ease 0.5 zoom 1.5 xoffset -300 yoffset 200

    pause 0.5

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    if not engineering_room_investigate_arm_circle:

        $ engineering_room_investigate_arm_circle = True

        van "A robotic arm."

        $ rollback_ = True

        show character_icon_box:
            xpos -350 ypos 50
            easein_expo 1.0 xpos 130 ypos 50
        show zalmona_icon_normal:
            xpos -350 ypos 50
            easein_expo 1.0 xpos 130 ypos 48

        zal "\"Hey, {w=0.5}did you notice?\""

        van "\"Huh?\""

        zal "\"Something is different about this robotic arm.\""

        zal "\"Come take a look.\""

        show engineering_room_1_arm_4_zoom behind character_icon_box
        $ renpy.transition(Dissolve(0.5))
        $ renpy.pause(0.5, hard='True')

        zal "\"You see this? {w=0.5}This one has an extra {color=#f00}circle {/color}engraved on it.\""

        van "\"Hmm... {w=0.5}You're right.\""

        van "But that's just a small detail. {w=0.5}Does it really mean anything?"
    else:


        show engineering_room_1_arm_4_zoom
        $ renpy.transition(Dissolve(0.5))
        $ renpy.pause(0.5, hard='True')

        van "A robotic arm. {w=0.5}It has a {color=#f00}circle{/color} engraved on it."

    hide character_icon_box
    hide zalmona_icon_normal
    hide engineering_room_1_arm_4_zoom
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    show engineering_room_1:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    $ renpy.pause(0.5, hard='True')

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)
    $ renpy.block_rollback()
    $ _rollback = False

    hide engineering_room_1
    scene engineering_room_1

    call screen engineering_room_1_screen with Dissolve(0.1)



label engineering_room_2_talk_zalmona:

    $ renpy.block_rollback()

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/selectsounds.ogg"

    $ _rollback = True
    $ _skipping = True

    zal "\"The truth is, {w=0.5}I've lost a round, {w=0.5}spherical object.\""

    $ rollback_ = True

    zal "\"If you can help me find it, {w=0.5}I'll give you the key card to the Legal Department.\""

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ _rollback = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    call screen engineering_room_2_screen with Dissolve(0.1)

label engineering_room_2_investigate_door:

    hide zalmona_drop_shadow
    hide zalmona_normal

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show engineering_room_2 at Position(xpos = 0, ypos = 0)

    show engineering_room_2:
        ease 0.5 zoom 2.0 xoffset 600 yoffset 600

    pause 0.5

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    van "The door to the Legal Department."

    $ rollback_ = True

    van "I need to find Zalmona's item first."

    show engineering_room_2:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    $ renpy.pause(0.5, hard='True')

    hide engineering_room_2
    scene engineering_room_2
    show zalmona_drop_shadow at zal_pos_2
    show zalmona_normal at zal_pos_2

    $ renpy.block_rollback()
    $ _rollback = False
    $ rollback_ = False
    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    call screen engineering_room_2_screen with Dissolve(0.1)



label engineering_room_3_investigate_puzzle:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show engineering_room_3 at Position(xpos = 0, ypos = 0)

    show engineering_room_3:
        ease 0.5 zoom 2.9 xoffset 0 yoffset 1250

    pause 0.5

    show transparent dark-small:
        alpha 0.7
    show engineering_room_3_puzzle_base as engineering_room_3_puzzle_base_1:
        xpos 200 ypos 150
    show engineering_room_3_puzzle_green as engineering_room_3_puzzle_color_1:
        xpos 200 ypos 150
    show engineering_room_3_puzzle_diamond as engineering_room_3_puzzle_shape_1:
        xpos 200 ypos 150
    show engineering_room_3_puzzle_base as engineering_room_3_puzzle_base_2:
        xpos 450 ypos 150
    show engineering_room_3_puzzle_red as engineering_room_3_puzzle_color_2:
        xpos 450 ypos 150
    show engineering_room_3_puzzle_square as engineering_room_3_puzzle_shape_2:
        xpos 450 ypos 150
    show engineering_room_3_puzzle_base as engineering_room_3_puzzle_base_3:
        xpos 700 ypos 150
    show engineering_room_3_puzzle_blue as engineering_room_3_puzzle_color_3:
        xpos 700 ypos 150
    show engineering_room_3_puzzle_circle as engineering_room_3_puzzle_shape_3:
        xpos 700 ypos 150
    show engineering_room_3_puzzle_base as engineering_room_3_puzzle_base_4:
        xpos 950 ypos 150
    show engineering_room_3_puzzle_yellow as engineering_room_3_puzzle_color_4:
        xpos 950 ypos 150
    show engineering_room_3_puzzle_triangle as engineering_room_3_puzzle_shape_4:
        xpos 950 ypos 150
    $ renpy.transition(Dissolve(0.5))

    if not engineering_room_investigate_puzzle:

        $ engineering_room_investigate_puzzle = True

        $ renpy.pause(1.0, hard='True')

        $ _skipping = True
        $ renpy.block_rollback()
        $ _rollback = True

        show character_icon_box:
            xpos 1350 ypos 300
            easein_expo 1.0 xpos 800 ypos 300
            xpos 800 ypos 300
        show zalmona_icon_normal:
            xpos 1350 ypos 298
            easein_expo 1.0 xpos 800 ypos 298
            xpos 800 ypos 298

        zal "\"Contemporary art really is getting more and more pretentious.\""

        $ rollback_ = True

        zal "\"Detective,{w=0.5} what do you think these four art piece mean?\""

        van "\"...I think it's some kind of device.\""

        show zalmona_icon_surprised:
            xpos 800 ypos 298
        hide zalmona_icon_normal

        zal "\"Some kind of device?\""

        van "\"Look here, {w=0.5}there are two buttons under each piece.\""

        show zalmona_icon_normal:
            xpos 800 ypos 298
        hide zalmona_icon_surprised

        zal "\"Oh? {w=0.5}Let me try pressing one of them.\""

        $ renpy.music.set_volume(1.0, delay=0, channel='sound')
        play sound "music/Tunnel/wheelMoveSFX.ogg" fadeout 1.0

        show engineering_room_3_puzzle_red as engineering_room_3_puzzle_red_2 behind engineering_room_3_puzzle_shape_1:
            xpos 200 ypos 150
        hide engineering_room_3_puzzle_color_1
        with Dissolve(0.5)

        show zalmona_icon_surprised:
            xpos 800 ypos 298
        hide zalmona_icon_normal

        van "!?"

        van "\"The color of the art... {w=0.5}has changed.\""

        zal "\"Then what about pressing the other one?\""

        $ renpy.music.set_volume(1.0, delay=0, channel='sound')
        play sound "music/Tunnel/wheelMoveSFX.ogg" fadeout 1.0

        show engineering_room_3_puzzle_square as engineering_room_3_puzzle_square_2:
            xpos 200 ypos 150
        hide engineering_room_3_puzzle_shape_1
        with Dissolve(0.5)

        van "\"The shape changed this time.\""

        show zalmona_icon_normal:
            xpos 800 ypos 298
        hide zalmona_icon_surprised

        zal "\"I understand now. {w=0.5}I think we're supposed to {color=#f00}match each shape with a corresponding color{/color}.\""

        zal "\"It's not that difficult. {w=0.5}We just need to try all the combinations, {w=0.5}and we should be able to find the right answer.\""

        van "\"No. {w=0.5}It's not as simple as that.\""

        show zalmona_icon_surprised:
            xpos 800 ypos 298
        hide zalmona_icon_normal

        zal "\"Eh?\""

        van "\"We can change the shape of each art, {w=0.5}but we can also change their colors.\""

        van "\"What it means is that not only do we need to match each shape with the color that corresponds to it,\""

        van "\"We also need to find {color=#f00}a specific order{/color} of the art piece, {w=0.5}perhaps by colors.\""

        show zalmona_icon_normal:
            xpos 800 ypos 298
        hide zalmona_icon_surprised

        zal "\"Indeed. {w=0.5}If that's the case, {w=0.5}there will be a lot more possible answers.\""

        van "\"Correct. {w=0.5}It will be very impractical to just try each of them one by one.\""

        if engineering_room_used_tape:

            hide zalmona_icon_normal
            hide character_icon_box

            hide engineering_room_3_puzzle_red_2
            hide engineering_room_3_puzzle_square_2
            show engineering_room_3_puzzle_green as engineering_room_3_puzzle_color_1:
                xpos 200 ypos 150
            show engineering_room_3_puzzle_diamond as engineering_room_3_puzzle_shape_1:
                xpos 200 ypos 150
            with Dissolve(0.5)

            jump engineering_room_3_puzzle_screen_prep
    else:


        if not engineering_room_used_tape:

            $ renpy.pause(1.0, hard='True')

            $ _skipping = True
            $ renpy.block_rollback()
            $ _rollback = True

            van "\"A device.\""

            $ rollback_ = True

            van "\"Not only do I need to match each shape to its corresponding color, {w=0.5}I also need to find a specific order.\""

            van "\"I don't know what the answer to the puzzle is yet. {w=0.5}It would be very impractical to just guess.\""

        if engineering_room_used_tape:

            $ renpy.pause(0.5, hard='True')

            jump engineering_room_3_puzzle_screen_prep

label engineering_room_3_investigate_puzzle_end:

    hide transparent dark-small
    hide engineering_room_3_puzzle_base_1
    hide engineering_room_3_puzzle_base_2
    hide engineering_room_3_puzzle_base_3
    hide engineering_room_3_puzzle_base_4
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
    hide zalmona_icon_normal
    hide zalmona_icon_surprised
    hide character_icon_box
    with Dissolve(0.5)

    show engineering_room_3:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    $ renpy.pause(0.5, hard='True')

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    $ renpy.block_rollback()
    $ _rollback = False

    hide engineering_room_3
    scene engineering_room_3

    call screen engineering_room_3_screen with Dissolve(0.1)

label engineering_room_3_investigate_vent:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show engineering_room_3 at Position(xpos = 0, ypos = 0)

    show engineering_room_3:
        ease 0.5 zoom 3.0 xoffset -1000 yoffset 1350

    pause 0.5

    van "Ventilation duct opening. {w=0.5}Nothing special about it."

    show engineering_room_3:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    $ renpy.pause(0.5, hard='True')
    hide engineering_room_3
    scene engineering_room_3

    call screen engineering_room_3_screen with Dissolve(0.1)

label engineering_room_3_investigate_arm_2:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show engineering_room_3 at Position(xpos = 0, ypos = 0)

    show engineering_room_3:
        ease 0.5 zoom 1.5 xoffset -300 yoffset 0

    jump engineering_room_3_investigate_arm_end

label engineering_room_3_investigate_arm_3:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show engineering_room_3 at Position(xpos = 0, ypos = 0)

    show engineering_room_3:
        ease 0.5 zoom 1.5 xoffset 300 yoffset 200

    jump engineering_room_3_investigate_arm_end

label engineering_room_3_investigate_arm_4:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show engineering_room_3 at Position(xpos = 0, ypos = 0)

    show engineering_room_3:
        ease 0.5 zoom 1.5 xoffset -300 yoffset 200

    jump engineering_room_3_investigate_arm_end

label engineering_room_3_investigate_arm_end:

    $ renpy.pause(0.5, hard='True')

    van "A robotic arm. {w=0.5}Nothing special about it."

    show engineering_room_3:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    $ renpy.pause(0.5, hard='True')

    hide engineering_room_3
    scene engineering_room_3

    call screen engineering_room_3_screen with Dissolve(0.1)

label engineering_room_3_investigate_arm_with_key:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show engineering_room_3 at Position(xpos = 0, ypos = 0)

    show engineering_room_3:
        ease 0.5 zoom 1.5 xoffset 300 yoffset 0

    pause 0.5

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    if not engineering_room_has_key:

        $ engineering_room_has_key = True

        van "A robotic arm."

        $ rollback_ = True

        show engineering_room_3_arm_zoom_key
        $ renpy.transition(Dissolve(0.5))
        $ renpy.pause(0.5, hard='True')

        van "Hm? {w=0.5}Is that..."

        show character_icon_box:
            xpos -350 ypos 50
            easein_expo 0.5 xpos 130 ypos 50
        show zalmona_icon_surprised:
            xpos -350 ypos 50
            easein_expo 0.5 xpos 130 ypos 48

        zal "\"A key! {w=0.5}It's holding a key!\""

        hide zalmona_icon_surprised
        hide character_icon_box
        show engineering_room_3_arm_zoom_no_key
        hide engineering_room_3_arm_zoom_key
        $ renpy.transition(Dissolve(0.5))
        $ renpy.pause(0.5, hard='True')

        if renpy.is_skipping():
            $ renpy.choice_for_skipping()
        $ _skipping = False
        $ renpy.music.stop(channel="beep", fadeout = 0.5)

        $ renpy.pause(0.5, hard='True')

        $ renpy.music.set_volume(0.8, delay=0, channel='sound')
        play sound "music/UI Dark.ogg"

        noname "Collected item: {w=0.5}A key"


        $ store.inventory.append(iEngineeringRoomKey)
        $ store.active_item = None
        $ renpy.restart_interaction()

        $ setattr(iEngineeringRoomKey, "selected", False)

        hide engineering_room_3_arm_zoom_no_key
        $ renpy.transition(Dissolve(0.5))
        $ renpy.pause(0.5, hard='True')
    else:


        van "A robotic arm. {w=0.5}Nothing special about it."

    show engineering_room_3:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    $ renpy.pause(0.5, hard='True')

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)
    $ renpy.block_rollback()
    $ _rollback = False

    hide engineering_room_3
    scene engineering_room_3

    call screen engineering_room_3_screen with Dissolve(0.1)



label engineering_room_4_investigate_door:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show engineering_room_4 at Position(xpos = 0, ypos = 0)

    show engineering_room_4:
        ease 0.5 zoom 1.5 xoffset -300 yoffset 270

    pause 0.5

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/engineering room/locked.ogg")

    pause 1.0

    van "I tried the door handle."

    $ rollback_ = True

    van "The door itself doesn't seem to be locked, {w=0.5}but because of the fixture on top, {w=0.5}I couldn't open it."

    show engineering_room_4:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    $ renpy.pause(0.5, hard='True')

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    $ renpy.block_rollback()
    $ _rollback = False

    hide engineering_room_4
    scene engineering_room_4

    call screen engineering_room_4_screen with Dissolve(0.1)

label engineering_room_4_investigate_trophy:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show engineering_room_4 at Position(xpos = 0, ypos = 0)

    show engineering_room_4:
        ease 0.5 zoom 2.0 xoffset 100 yoffset 500

    pause 0.5

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    van "A trophy."

    $ rollback_ = True

    van "The trophy has a {color=#f00}diamond shape{/color} engraved on it, {w=0.5}but there isn't any text."

    show engineering_room_4:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    $ renpy.pause(0.5, hard='True')

    if not engineering_room_investigate_trophy:

        $ engineering_room_investigate_trophy = True

        show zalmona_drop_shadow at zal_pos_2
        show zalmona_normal at zal_pos_2
        $ renpy.transition(Dissolve(0.5))
        $ renpy.pause(0.5, hard='True')

        window show

        zal "\"Detective, {w=0.5}who do you think this trophy is for?\""

        van "\"I'm not sure. {w=0.5}Maybe it's for employee of the month?\""

        hide zalmona_normal
        show zalmona_happy at zal_pos_2
        with Dissolve(0.2)

        zal "\"Employee of the month?\""

        zal "\"Perhaps the winner gets a free ticket to the basement. {w=0.5}Hahahaha.\""

        van "\"......\""

        window hide

        hide zalmona_happy
        hide zalmona_drop_shadow
        $ renpy.transition(Dissolve(0.5))
        $ renpy.pause(0.5, hard='True')

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    $ renpy.block_rollback()
    $ _rollback = False

    hide engineering_room_4
    scene engineering_room_4

    call screen engineering_room_4_screen with Dissolve(0.1)

label engineering_room_4_investigate_cupboard_1:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show engineering_room_4 at Position(xpos = 0, ypos = 0)

    show engineering_room_4:
        ease 0.5 zoom 2.0 xoffset 600 yoffset 100

    jump engineering_room_4_investigate_cupboard_end

label engineering_room_4_investigate_cupboard_2:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show engineering_room_4 at Position(xpos = 0, ypos = 0)

    show engineering_room_4:
        ease 0.5 zoom 2.0 xoffset 100 yoffset 100

    jump engineering_room_4_investigate_cupboard_end

label engineering_room_4_investigate_cupboard_end:

    pause 0.5

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    van "A cupboard under a drawer."

    $ rollback_ = True

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/engineering room/Cupboard_open.ogg")

    pause 1.0

    van "I opened it and took a look."

    van "There was nothing in it."

    show engineering_room_4:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    $ renpy.pause(0.5, hard='True')

    hide engineering_room_4
    scene engineering_room_4

    $ renpy.block_rollback()
    $ _rollback = False
    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    call screen engineering_room_4_screen with Dissolve(0.1)

label engineering_room_4_investigate_drawer_2:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show engineering_room_4 at Position(xpos = 0, ypos = 0)

    show engineering_room_4:
        ease 0.5 zoom 2.0 xoffset 100 yoffset 300

    pause 0.5

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    van "A drawer."

    $ rollback_ = True

    $ renpy.music.set_volume(0.7, delay=0, channel='sound')
    play sound ("music/drawer.ogg")

    pause 1.0

    van "I slide-opened it and took a look."

    van "There was nothing in it."

    if not engineering_room_investigate_broken_drawer:

        $ engineering_room_investigate_broken_drawer = True

        show character_icon_box:
            xpos 1350 ypos 50
            easein_expo 1.0 xpos 830 ypos 50
            xpos 830 ypos 50
        show zalmona_icon_normal:
            xpos 1350 ypos 50
            easein_expo 1.0 xpos 830 ypos 48
            xpos 830 ypos 48

        zal "\"That's disappointing. {w=0.5}It had a lock on it, {w=0.5}so I thought there would certainly be goodies inside.\""

        van "\"You're not exactly wrong.\""

        zal "\"Huh? {w=0.5}What do you mean?\""

        van "\"Look here, {w=0.5}the lock on this drawer has been pried open.\""


        show character_icon_box:
            xpos 830 ypos 50
        hide zalmona_icon_normal
        show zalmona_icon_surprised:
            xpos 830 ypos 48

        zal "\"!? {w=0.5}You're right.\""

        hide zalmona_icon_surprised
        show zalmona_icon_normal:
            xpos 830 ypos 48

        zal "\"Then it looks like someone has looted this place.\""

        zal "\"Whoever broke the lock must have taken the good stuff inside.\""

        van "\"Right.\""

        hide zalmona_icon_normal
        hide character_icon_box
        $ renpy.transition(Dissolve(0.5))
        $ renpy.pause(0.5, hard='True')
    else:


        van "The drawer looks like it had been pried open. {w=0.5}Someone may have taken the things in it."

    show engineering_room_4:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    $ renpy.pause(0.5, hard='True')
    hide engineering_room_4
    show engineering_room_4

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)
    $ renpy.block_rollback()
    $ _rollback = False

    call screen engineering_room_4_screen with Dissolve(0.1)

label engineering_room_4_investigate_drawer_1:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show engineering_room_4 at Position(xpos = 0, ypos = 0)

    show engineering_room_4:
        ease 0.5 zoom 2.0 xoffset 600 yoffset 300

    pause 0.5

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    van "A drawer."

    $ rollback_ = True

    if not engineering_room_used_key:

        $ renpy.music.set_volume(1.0, delay=0, channel='sound')
        play sound ("music/engineering room/locked.ogg")

        pause 1.0

        van "It's locked."
    else:


        $ renpy.music.set_volume(0.7, delay=0, channel='sound')
        play sound ("music/drawer.ogg")

        pause 1.0

        van "I slide-opened it and took a look."

        van "There was nothing in it."

    show engineering_room_4:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    $ renpy.pause(0.5, hard='True')

    hide engineering_room_4
    scene engineering_room_4

    $ renpy.block_rollback()
    $ _rollback = False
    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    call screen engineering_room_4_screen with Dissolve(0.1)

label engineering_room_4_unlock_drawer_1:

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/weapon click.ogg"

    show engineering_room_4 at Position(xpos = 0, ypos = 0)

    show engineering_room_4:
        ease 0.5 zoom 2.0 xoffset 600 yoffset 300

    pause 0.5

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    van "I unlocked the drawer."

    $ renpy.music.set_volume(0.7, delay=0, channel='sound')
    play sound ("music/drawer.ogg")

    show transparent dark-small:
        alpha 0.6
    with Dissolve(0.5)

    pause 0.5

    van "What I find inside is..."

    show engineering_room_knife onlayer inyourface
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    van "A scalpel."

    hide engineering_room_knife onlayer inyourface
    show engineering_room_tape onlayer inyourface
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    van "And a cassette tape."

    hide engineering_room_tape onlayer inyourface
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    show character_icon_box:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 830 ypos 50
    show zalmona_icon_normal:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 830 ypos 48

    zal "\"A cassette tape in a locked drawer?\""

    zal "\"Detective, {w=0.5}you know what this means, {w=0.5}right?\""

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    hide character_icon_box
    hide zalmona_icon_normal
    hide transparent dark-small
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/UI Dark.ogg"

    noname "Collected items: {w=0.5}Scalpel, {w=0.5}Cassette Tape"


    $ store.inventory.append(iEngineeringRoomTape)
    $ store.inventory.append(iEngineeringRoomKnife)
    $ store.active_item = None
    $ renpy.restart_interaction()

    $ setattr(iEngineeringRoomTape, "selected", False)
    $ setattr(iEngineeringRoomKnife, "selected", False)

    show engineering_room_4:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    $ renpy.pause(0.5, hard='True')

    $ renpy.block_rollback()
    $ _rollback = False

    call screen engineering_room_4_screen with Dissolve(0.1)

label engineering_room_4_investigate_radio:

    if not engineering_room_used_tape:

        $ renpy.music.set_volume(1.0, delay=0, channel='sound')
        play sound ("music/zoom.wav")

        show engineering_room_4 at Position(xpos = 0, ypos = 0)

        show engineering_room_4:
            ease 0.5 zoom 2.0 xoffset 500 yoffset 450

        pause 0.5

        $ _skipping = True
        $ renpy.block_rollback()
        $ _rollback = True

        van "A boombox."

        $ rollback_ = True

        van "I don't really feel like listening to the radio right now."

        show engineering_room_4:
            ease 0.5 zoom 1.0 xoffset 0 yoffset 0

        $ renpy.pause(0.5, hard='True')
        hide engineering_room_4
        scene engineering_room_4

        $ renpy.block_rollback()
        $ _rollback = False
        if renpy.is_skipping():
            $ renpy.choice_for_skipping()
        $ _skipping = False
        $ rollback_ = False
        $ renpy.music.stop(channel="beep", fadeout = 0.5)

        call screen engineering_room_4_screen with Dissolve(0.1)
    else:


        hide screen inventory_screen
        scene winston_past_mansion_bar_table
        show white back
        $ renpy.transition(Dissolve(0.1))
        $ renpy.pause(0.1, hard='True')

        stop music fadeout 1.0

        $ renpy.music.set_volume(0.7, delay=0, channel='sound')
        play sound "music/teleport.ogg"

        $ renpy.pause(0.3, hard='True')

        hide white back
        $ renpy.transition(Dissolve(1.0))
        $ renpy.pause(1.0, hard='True')

        $ renpy.music.set_volume(0.5, delay=0, channel='music')
        play music ("music/bgm/jazz-lounge.ogg")

        call screen winston_collab_past_bar_click_screen

label engineering_room_4_radio_put_in_tape:

    hide screen inventory_screen
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    stop music fadeout 6.0

    $ renpy.music.set_volume(0.8, delay=0, channel='vhs')
    $ renpy.music.play("music/vhs tape.ogg", channel="vhs", loop=False)
    $ renpy.music.queue("music/vhs tape 2.ogg", channel='vhs', loop=True)

    van "I loaded the tape into the boombox, {w=0.5}and proceeded to press the play button."

    $ rollback_ = True

    pause 2.0

    van "Sporadically, {w=0.5}sounds started to come out from it one by one."

    pause 1.0

    radio2 "\"......\""

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/myers lobby/myers lobby radio/design create enhance.ogg"

    radio2 "\"On {size=+8}Ju{/size}ly {size=+2}20{/size}......{w=0.5}at {size=+4}approxim{/size}ately 23:00......{w=0.5}minor {size=+5}explosions{/size}......{w=0.5}Prison {size=-6}area{/size}......\""

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/myers lobby/myers lobby radio/welcome to myers.ogg"

    radio2 "\"The {size=-3}whereabouts{/size}......{w=0.5}Myers {size=+8}researcher{/size}......{w=0.5}sentenced to {size=+3}life{/size}......{w=0.5}remain unknown.\""

    van "The voice coming out was very faint and indistinct. {w=0.5}I could only make out a few vague words."

    show zalmona_drop_shadow at zal_pos_2
    show zalmona_angry at zal_pos_2
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.music.set_volume(0.3, delay=0, channel='sound')
    play sound "music/zalmona/Zalmona-huh_.ogg"

    zal "\"What the hell is wrong with this boombox!? {w=0.5}I can't understand shit!\""

    zal "\"Here- {w=0.5}I'll fix it!\""

    hide zalmona_drop_shadow
    hide zalmona_angry
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/banging.ogg"

    with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    pause 1.0

    van "With that, {w=0.5}Zalmona started banging on the boombox."

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/shake.ogg"

    van "\"Zalmona, {w=0.5}wait!\"" with Shake((0.5, 1.0, 0.5, 1.0), 3.0, dist=15)

    van "I tried to protect the boombox with my arms."

    $ renpy.music.stop(channel="vhs", fadeout = 3.0)



    show engineering_room_4_blurred:
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

    hide myers_tunnel_mascot_closeup_blurred
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    pause 1.0

    van "!?"

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

    jump winston_collab_past_start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
