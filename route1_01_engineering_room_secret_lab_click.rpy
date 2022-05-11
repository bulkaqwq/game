define engineering_room_secret_lab_monitor_num = [0, 0, 0]

screen engineering_room_secret_lab_click_screen:

    imagebutton:
        xpos 520
        ypos 620
        idle "images/john past/arrow_down_idle.png"
        hover "images/john past/arrow_down_hover.png"
        focus_mask "images/john past/arrow_down_idle.png"
        action [Hide("displayTextScreenGeneral"), Jump("engineering_room_secret_lab_leave_lab")]

    imagebutton:
        xpos 918
        ypos 258
        idle "images/Engineering Room Secret Lab/Engineering_room_secret_lab_monitor_idle.png"
        hover "images/Engineering Room Secret Lab/Engineering_room_secret_lab_monitor_hover.png"
        focus_mask "images/Engineering Room Secret Lab/Engineering_room_secret_lab_monitor_hover.png"
        if not engineering_room_secret_lab_drain_container_2:
            action checkInteractionValid("engineering_room_secret_lab_click_screen", "engineering_room_secret_lab_investigate_monitor")
        else:
            action NullAction()
            hovered Show("displayTextScreenGeneral", displayText = " I have drained the chamber ", xalign_value=0.985, yalign_value=0.6)
            unhovered Hide("displayTextScreenGeneral")

    imagebutton:
        xpos 132
        ypos 0
        idle "images/Engineering Room Secret Lab/Engineering_room_secret_lab_container_1_idle.png"
        hover "images/Engineering Room Secret Lab/Engineering_room_secret_lab_container_1_hover.png"
        focus_mask "images/Engineering Room Secret Lab/Engineering_room_secret_lab_container_1_hover.png"
        action [Hide("displayTextScreenGeneral"), checkInteractionValid("engineering_room_secret_lab_click_screen", "engineering_room_secret_lab_investigate_container_1")]

    imagebutton:
        xpos 394
        ypos 0
        idle "images/Engineering Room Secret Lab/Engineering_room_secret_lab_container_1_idle.png"
        hover "images/Engineering Room Secret Lab/Engineering_room_secret_lab_container_2_hover.png"
        focus_mask "images/Engineering Room Secret Lab/Engineering_room_secret_lab_container_2_hover.png"
        action [Hide("displayTextScreenGeneral"), checkInteractionValid("engineering_room_secret_lab_click_screen", "engineering_room_secret_lab_investigate_container_2")]

    imagebutton:
        xpos 657
        ypos 0
        idle "images/Engineering Room Secret Lab/Engineering_room_secret_lab_container_3_idle.png"
        hover "images/Engineering Room Secret Lab/Engineering_room_secret_lab_container_3_hover.png"
        focus_mask "images/Engineering Room Secret Lab/Engineering_room_secret_lab_container_3_hover.png"
        action [Hide("displayTextScreenGeneral"), checkInteractionValid("engineering_room_secret_lab_click_screen", "engineering_room_secret_lab_investigate_container_3")]

    imagebutton:
        xpos 937
        ypos 46
        idle "images/Engineering Room Secret Lab/Engineering_room_secret_lab_blackboard_idle.png"
        hover "images/Engineering Room Secret Lab/Engineering_room_secret_lab_blackboard_hover.png"
        focus_mask "images/Engineering Room Secret Lab/Engineering_room_secret_lab_blackboard_hover.png"
        action [Hide("displayTextScreenGeneral"), checkInteractionValid("engineering_room_secret_lab_click_screen", "engineering_room_secret_lab_investigate_blackboard")]

screen engineering_room_secret_lab_monitor_zoom_srceen:

    text "{size=+130}{color=#1F9F2D}{font=impact.ttf}[engineering_room_secret_lab_monitor_num[0]]{/font}{/color}{/size}" xpos 513 ypos 158 xalign 0.5
    text "{size=+130}{color=#1F9F2D}{font=impact.ttf}[engineering_room_secret_lab_monitor_num[1]]{/font}{/color}{/size}" xpos 678 ypos 158 xalign 0.5
    text "{size=+130}{color=#1F9F2D}{font=impact.ttf}[engineering_room_secret_lab_monitor_num[2]]{/font}{/color}{/size}" xpos 843 ypos 158 xalign 0.5

    imagebutton:
        xpos 520
        ypos 620
        idle "images/john past/arrow_down_idle.png"
        hover "images/john past/arrow_down_hover.png"
        focus_mask "images/john past/arrow_down_idle.png"
        action Call("engineering_room_secret_lab_leave_monitor_screen")

    imagebutton:
        xpos 450
        ypos 170
        idle "images/Engineering Room Secret Lab/Engineering_room_secret_lab_monior_binary_idle.png"
        hover "images/Engineering Room Secret Lab/Engineering_room_secret_lab_monior_binary_hover.png"
        focus_mask "images/Engineering Room Secret Lab/Engineering_room_secret_lab_monior_binary_focusmask.png"
        action [Play("sound", "music/Tunnel/wheelMoveSFX.ogg"), Call("engineering_room_secret_lab_monitor_change_num", 0)]

    imagebutton:
        xpos 615
        ypos 170
        idle "images/Engineering Room Secret Lab/Engineering_room_secret_lab_monior_binary_idle.png"
        hover "images/Engineering Room Secret Lab/Engineering_room_secret_lab_monior_binary_hover.png"
        focus_mask "images/Engineering Room Secret Lab/Engineering_room_secret_lab_monior_binary_focusmask.png"
        action [Play("sound", "music/Tunnel/wheelMoveSFX.ogg"), Call("engineering_room_secret_lab_monitor_change_num", 1)]

    imagebutton:
        xpos 780
        ypos 170
        idle "images/Engineering Room Secret Lab/Engineering_room_secret_lab_monior_binary_idle.png"
        hover "images/Engineering Room Secret Lab/Engineering_room_secret_lab_monior_binary_hover.png"
        focus_mask "images/Engineering Room Secret Lab/Engineering_room_secret_lab_monior_binary_focusmask.png"
        action [Play("sound", "music/Tunnel/wheelMoveSFX.ogg"), Call("engineering_room_secret_lab_monitor_change_num", 2)]

    imagebutton:
        xpos 558
        ypos 360
        idle "images/Engineering Room Secret Lab/Engineering_room_secret_lab_enter_idle.png"
        hover "images/Engineering Room Secret Lab/Engineering_room_secret_lab_enter_hover.png"
        focus_mask "images/Engineering Room Secret Lab/Engineering_room_secret_lab_enter_idle.png"
        action Jump("engineering_room_secret_lab_check_code_correctness")

screen engineering_room_secret_lab_blackboard_srceen:

    imagebutton:
        xpos 520
        ypos 620
        idle "images/john past/arrow_down_idle.png"
        hover "images/john past/arrow_down_hover.png"
        focus_mask "images/john past/arrow_down_idle.png"
        action Jump("engineering_room_secret_lab_investigate_blackboard_end")

screen engineering_room_secret_lab_container_2_zoom_screen:

    imagebutton:
        xpos 1005
        ypos 650
        idle "images/john past/arrow_down_idle.png"
        hover "images/john past/arrow_down_hover.png"
        focus_mask "images/john past/arrow_down_idle.png"
        action Jump("engineering_room_secret_lab_container_2_leave")

    imagebutton:
        xpos 371
        ypos 50
        idle "images/Engineering Room Secret Lab/Engineering_room_secret_lab_container_2_zoom_idle.png"
        hover "images/Engineering Room Secret Lab/Engineering_room_secret_lab_container_2_zoom_hover.png"
        focus_mask "images/Engineering Room Secret Lab/Engineering_room_secret_lab_container_2_zoom_hover.png"
        action testItem_General(iEngineeringRoomKnife,"engineering_room_used_knife", True, "engineering_room_secret_lab_container_2_zoom_screen", "engineering_room_secret_lab_use_knife_cyborg_zoom_container_2", "engineering_room_secret_lab_investigate_cyborg_zoom_container_2")

label engineering_room_secret_lab_investigate_monitor:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    $ engineering_room_secret_lab_monitor_num = [0, 0, 0]

    show engineering_room_secret_lab at Position(xpos = 0, ypos = 0)

    show engineering_room_secret_lab:
        ease 0.5 zoom 2.0 xoffset -600 yoffset 300

    pause 0.5

    show black:
        alpha 0.5
    with Dissolve(0.5)

    show engineering_room_secret_lab_monitor_zoom

    call screen engineering_room_secret_lab_monitor_zoom_srceen

label engineering_room_secret_lab_monitor_change_num(current_num):

    if engineering_room_secret_lab_monitor_num[current_num] == 0:
        $ engineering_room_secret_lab_monitor_num[current_num] = 1
    else:
        $ engineering_room_secret_lab_monitor_num[current_num] = 0

    $ renpy.pop_call()

    call screen engineering_room_secret_lab_monitor_zoom_srceen

label engineering_room_secret_lab_leave_monitor_screen:

    $ renpy.pop_call()
    $ engineering_room_secret_lab_monitor_num = [0, 0, 0]

    hide screen engineering_room_secret_lab_monitor_zoom_srceen
    hide engineering_room_secret_lab_monitor_zoom
    hide black with Dissolve(0.5)

    show engineering_room_secret_lab:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    $ renpy.pause(0.5, hard='True')

    hide engineering_room_secret_lab
    scene engineering_room_secret_lab

    call screen engineering_room_secret_lab_click_screen with Dissolve(0.2)

label engineering_room_secret_lab_investigate_container_1:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show engineering_room_secret_lab at Position(xpos = 0, ypos = 0)

    show engineering_room_secret_lab:
        ease 0.5 zoom 2.0 xoffset 600 yoffset 600

    pause 0.5

    van "A glass chamber. {w=0.5}There's nothing in it."

    show engineering_room_secret_lab:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    $ renpy.pause(0.5, hard='True')

    hide engineering_room_secret_lab
    scene engineering_room_secret_lab

    call screen engineering_room_secret_lab_click_screen with Dissolve(0.2)

label engineering_room_secret_lab_investigate_container_3:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show engineering_room_secret_lab at Position(xpos = 0, ypos = 0)

    show engineering_room_secret_lab:
        ease 0.5 zoom 2.0 xoffset -400 yoffset 600

    pause 0.5

    show engineering_room_secret_lab_zoom_cyborg_1 with Dissolve(0.5)

    van "A cyborg. {w=0.5}Thank goodness it's dead."

    hide engineering_room_secret_lab_zoom_cyborg_1 with Dissolve(0.5)

    show engineering_room_secret_lab:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    $ renpy.pause(0.5, hard='True')

    hide engineering_room_secret_lab
    scene engineering_room_secret_lab

    call screen engineering_room_secret_lab_click_screen with Dissolve(0.2)

label engineering_room_secret_lab_investigate_blackboard:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show engineering_room_secret_lab at Position(xpos = 0, ypos = 0)

    show engineering_room_secret_lab:
        ease 0.5 zoom 2.0 xoffset -600 yoffset 700

    pause 0.5

    show engineering_room_secret_lab_blackboard with Dissolve(0.5)

    if not engineering_room_secret_lab_investigate_blackboard_bool:

        $ engineering_room_secret_lab_investigate_blackboard_bool = True

        $ _skipping = True
        $ renpy.block_rollback()
        $ _rollback = True

        van "A blackboard. {w=0.5}There is a lot of diagrams and text marked on it."

        $ rollback_ = True

        zal "\"Detective, {w=0.5}you see this string of numbers in the upper right corner?\""

        van "\"1 = 001, {w=0.5}2 = 010, {w=0.5}7 = 111...\""

        van "\"Is this... {w=0.5}decimal to binary conversion?\""

        zal "\"Correct. {w=0.5}The binary numeral system is widely used in computing technology to represent numbers with just two symbols, {w=0.5}0 and 1.\""

        zal "\"For example, {w=0.5}in binary 110 means 0 + 1*2 + 1*2*2, {w=0.5}which is 6 in decimal.\""

        zal "\"And 111 means 1 + 1*2 + 1*2*2, {w=0.5}which is 7 in decimal.\""

        van "\"I see. {w=0.5}In other words, {w=0.5}we need to find the corresponding experimental subject number in binary.\""

        if renpy.is_skipping():
            $ renpy.choice_for_skipping()
        $ _skipping = False
        $ rollback_ = False
        $ renpy.music.stop(channel="beep", fadeout = 0.5)

        $ renpy.block_rollback()
        $ _rollback = False

    call screen engineering_room_secret_lab_blackboard_srceen

label engineering_room_secret_lab_investigate_blackboard_end:

    hide engineering_room_secret_lab_blackboard with Dissolve(0.5)

    show engineering_room_secret_lab:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    $ renpy.pause(0.5, hard='True')

    hide engineering_room_secret_lab
    scene engineering_room_secret_lab

    call screen engineering_room_secret_lab_click_screen with Dissolve(0.2)

label engineering_room_secret_lab_investigate_container_2:

    if not engineering_room_secret_lab_drain_container_2:

        $ renpy.music.set_volume(1.0, delay=0, channel='sound')
        play sound ("music/zoom.wav")

        show engineering_room_secret_lab at Position(xpos = 0, ypos = 0)

        show engineering_room_secret_lab:
            ease 0.5 zoom 2.0 xoffset 300 yoffset 600

        pause 0.5

        $ _skipping = True
        $ renpy.block_rollback()
        $ _rollback = True

        van "A glass chamber. {w=0.5}In it stands a cyborg that looks just like a human being."

        $ rollback_ = True

        van "This gives me the creeps."

        show engineering_room_secret_lab:
            ease 0.5 zoom 1.0 xoffset 0 yoffset 0

        $ renpy.pause(0.5, hard='True')

        if renpy.is_skipping():
            $ renpy.choice_for_skipping()
        $ _skipping = False
        $ rollback_ = False
        $ renpy.music.stop(channel="beep", fadeout = 0.5)

        $ renpy.block_rollback()
        $ _rollback = False

        hide engineering_room_secret_lab
        scene engineering_room_secret_lab

        call screen engineering_room_secret_lab_click_screen with Dissolve(0.2)
    else:


        if not engineering_room_secret_lab_investigate_container_2:

            stop music fadeout 3.0

            hide screen inventory_screen with Dissolve(0.2)

            scene black
            $ renpy.transition(Dissolve(0.5))
            $ renpy.pause(0.5, hard='True')

            scene engineering_room_secret_lab_container_2_zoom
            $ renpy.transition(Dissolve(1.0))
            $ renpy.pause(1.0, hard='True')

            $ _skipping = True
            $ renpy.block_rollback()
            $ _rollback = True

            pause 2.0

            $ renpy.pause(0.1, hard='True')

            show character_icon_box:
                xpos 1350 ypos 300
                easein_expo 1.0 xpos 800 ypos 300
                xpos 800 ypos 300
            show zalmona_icon_panic:
                xpos 1350 ypos 298
                easein_expo 1.0 xpos 800 ypos 298
                xpos 800 ypos 298

            zal "\"......\""

            $ rollback_ = True

            hide character_icon_box
            hide zalmona_icon_panic
            $ renpy.transition(Dissolve(1.0))
            $ renpy.pause(1.0, hard='True')

            pause 2.0

            van "The already stifling atmosphere intensified as we caught the first glimpse of what was inside the glass chamber."

            van "Zalmona was horrified at first, {w=0.5}but her expression quickly changed to worry."

            van "But it was if we had mutually agreed not to say anything to each other beforehand, {w=0.5}we just stood in silence."

            van "I could sense Zalmona staring straight at me."

            van "But at that moment, {w=0.5}I was completely focused on the cyborg in front of me."

            van "\"Let's do this then.\""

            zal "\"...O-{w=0.5}Okay.\""

            $ renpy.music.set_volume(0.6, delay=0, channel='music')
            play music "music/myers lobby/lobby horror.ogg"

            if renpy.is_skipping():
                $ renpy.choice_for_skipping()
            $ _skipping = False
            $ rollback_ = False
            $ renpy.music.stop(channel="beep", fadeout = 0.5)
            $ renpy.block_rollback()
            $ _rollback = False

            $ engineering_room_secret_lab_investigate_container_2 = True

            show screen inventory_screen with Dissolve(0.2)

            call screen engineering_room_secret_lab_container_2_zoom_screen
        else:




            scene black
            $ renpy.transition(Dissolve(0.5))
            $ renpy.pause(0.5, hard='True')

            $ renpy.pause(0.5, hard='True')

            scene engineering_room_secret_lab_container_2_zoom
            $ renpy.transition(Dissolve(1.0))
            $ renpy.pause(1.0, hard='True')

            call screen engineering_room_secret_lab_container_2_zoom_screen


label engineering_room_secret_lab_container_2_leave:

    scene black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.pause(0.5, hard='True')

    scene engineering_room_secret_lab
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    call screen engineering_room_secret_lab_click_screen with Dissolve(0.2)


label engineering_room_secret_lab_check_code_correctness:

    $ engineering_room_secret_lab_code_sum = engineering_room_secret_lab_monitor_num[0] * 4 + engineering_room_secret_lab_monitor_num[1] * 2 + engineering_room_secret_lab_monitor_num[2]



    if engineering_room_secret_lab_code_sum != 3:

        $ renpy.music.set_volume(0.7, delay=0, channel='sound')
        play sound "music/tech interface.ogg"

        show engineering_room_secret_lab_monitor_error

        if engineering_room_secret_lab_code_sum == 1:

            noname "System error. {w=0.5}The containment unit for subject No. 1 has been damaged."

        elif engineering_room_secret_lab_code_sum == 5:

            noname "System error. {w=0.5}The containment unit for subject No. 5 is empty."
        else:


            noname "System error. {w=0.5}Invalid subject number."

        hide engineering_room_secret_lab_monitor_error
    else:


        $ renpy.music.set_volume(0.6, delay=0, channel='sound')
        play sound "music/weapon click.ogg"

        show engineering_room_secret_lab_monitor_approved

        noname "Command received. {w=0.5}Draining the containment unit for subject No. 3."

        hide engineering_room_secret_lab_monitor_approved
        hide screen engineering_room_secret_lab_monitor_zoom_srceen
        hide engineering_room_secret_lab_monitor_zoom
        hide black with Dissolve(0.5)

        show engineering_room_secret_lab:
            ease 0.5 zoom 1.0 xoffset 0 yoffset 0

        $ renpy.pause(0.5, hard='True')

        hide engineering_room_secret_lab
        scene engineering_room_secret_lab

        $ renpy.pause(0.5, hard='True')

        scene black
        $ renpy.transition(Dissolve(0.5))
        $ renpy.pause(0.5, hard='True')

        $ renpy.music.set_volume(1.0, delay=0, channel='sound')
        play sound "music/engineering room/water splash.ogg"

        $ engineering_room_secret_lab_drain_container_2 = True

        $ renpy.pause(2.0, hard='True')

        scene engineering_room_secret_lab
        $ renpy.transition(Dissolve(1.0))
        $ renpy.pause(1.0, hard='True')

        call screen engineering_room_secret_lab_click_screen with Dissolve(0.2)

    call screen engineering_room_secret_lab_monitor_zoom_srceen

label engineering_room_secret_lab_leave_lab:

    stop music fadeout 1.0

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/engineering room/Cupboard_open.ogg")

    scene black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.pause(0.5, hard='True')

    scene engineering_room_4
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music ["<silence 1.0>", "music/bgm/lab investigation.ogg"] fadein 3.0
    queue music "music/bgm/lab investigation.ogg"

    call screen engineering_room_4_screen with Dissolve(0.2)

label engineering_room_secret_lab_investigate_cyborg_zoom_container_2:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/selectsounds.ogg"

    van "\"......\""

    call screen engineering_room_secret_lab_container_2_zoom_screen

label engineering_room_secret_lab_use_knife_cyborg_zoom_container_2:

    stop music fadeout 3.0

    hide screen inventory_screen with Dissolve(0.5)

    scene black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    pause 1.0

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    van "I took the scalpel that Zalmona handed to me, {w=0.5}and started making deep cuts into the cyborg's body."

    $ rollback_ = True

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/squish.ogg"

    pause 1.0

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/squish.ogg"

    pause 1.0

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/squish.ogg"

    van "Again, {w=0.5}and again. {w=0.5}And again."

    van "I felt emotions that I had never felt before welling up inside me."

    van "But all Zalmona did was just stare. {w=0.5}She didn't utter a word."

    van "Before I realized it, {w=0.5}the cyborg's chest was shredded to pieces."

    van "And revealed beneath her skin... {w=0.5}was a peculiar {color=#f00}spherical device{/color}."

    van "I grabbed the sphere with my bare hand, {w=0.5}and pulled it out."

    $ renpy.music.set_volume(0.7, delay=0, channel='sound')
    play sound "music/engineering room/flesh 2.ogg"

    pause 2.0

    stop sound fadeout 1.0

    show engineering_room_secret_lab_device with Dissolve(1.0)

    pause 1.0

    van "\"This is what you wanted, {w=0.5}right?\""

    van "\"This cyborg's memory core?\""

    zal "\"......\""

    zal "\"...Yes.\""

    hide engineering_room_secret_lab_device with Dissolve(1.0)

    pause 1.0

    van "I handed it to Zalmona with my blood-soaked hand."

    pause 2.0

    zal "\"......\""

    zal "\"Let's get the hell out of here. {w=0.5}I can't stand it in here anymore.\""

    jump engineering_room_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
