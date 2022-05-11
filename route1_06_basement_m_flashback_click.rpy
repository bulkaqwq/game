
image basement_m_laptop_zoom = "images/basement m flashback/basement-m-laptop-zoom.png"
image basement_m_screen_saver = "images/basement m flashback/basement-m-screen-saver.png"
image basement_m_screen_saver_1 = "images/basement m flashback/basement-m-screen-saver-1.png"
image basement_m_screen_saver_2 = "images/basement m flashback/basement-m-screen-saver-2.png"
image basement_m_screen_saver_3 = "images/basement m flashback/basement-m-screen-saver-3.png"
image basement_m_screen_saver_4 = "images/basement m flashback/basement-m-screen-saver-4.png"
image basement_m_folder_hint_1 = "images/basement m flashback/basement-m-folder-hint-1.png"
image basement_m_folder_hint_2 = "images/basement m flashback/basement-m-folder-hint-2.png"

image basement_m_screen_saver_myer_chan:
    "basement_m_screen_saver"
    1.0
    "basement_m_screen_saver_1"
    1.7
    "basement_m_screen_saver_2"
    0.6
    "basement_m_screen_saver_3"
    0.8
    "basement_m_screen_saver_4"
    2.0
    repeat

screen basement_m_table_screen:

    imagebutton:
        xpos 440
        ypos 170
        idle "images/basement m flashback/basement-m-laptop-idle.png"
        hover "images/basement m flashback/basement-m-laptop-hover.png"
        focus_mask "images/basement m flashback/basement-m-laptop-hover.png"
        action Jump("basement_m_table_investigate_computer")

    imagebutton:
        xpos 0
        ypos 0
        idle "images/basement m flashback/basement-m-lamp-idle.png"
        hover "images/basement m flashback/basement-m-lamp-hover.png"
        focus_mask "images/basement m flashback/basement-m-lamp-hover.png"
        action Jump("basement_m_table_investigate_lamp")

    imagebutton:
        xpos 406
        ypos 462
        idle "images/basement m flashback/basement-m-folder-idle.png"
        hover "images/basement m flashback/basement-m-folder-hover.png"
        focus_mask "images/basement m flashback/basement-m-folder-hover.png"
        action Jump("basement_m_table_investigate_folder")

    if not basement_see_flashback:
        imagebutton:
            xpos 970
            ypos 273
            idle "images/basement m flashback/basement-m-mug-idle.png"
            hover "images/basement m flashback/basement-m-mug-hover.png"
            focus_mask "images/basement m flashback/basement-m-mug-hover.png"
            action Jump("basement_m_table_investigate_mug")
    else:
        imagebutton:
            xpos 970
            ypos 273
            idle "images/basement m flashback/basement-m-mug-idle.png"
            hover "images/basement m flashback/basement-m-mug-hover.png"
            focus_mask "images/basement m flashback/basement-m-mug-hover.png"
            action Jump("basement_m_table_teleport")

screen basement_m_table_puzzle_zoom:

    imagebutton:
        xpos 520
        ypos 610
        idle "images/basement/basement_door_arrow_down_idle.png"
        hover "images/tunnel/myers_tunnel_door_arrow_down_hover.png"
        focus_mask "images/basement/basement_door_arrow_down_idle.png"
        action Jump("basement_m_table_puzzle_zoom_leave")

label basement_m_table_investigate_computer:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show basement_m_desk at Position(xpos = 0, ypos = 0)

    show basement_m_desk:
        ease 0.5 zoom 2.0 xoffset -50 yoffset 450

    $ renpy.pause(0.5, hard='True')

    if not basement_m_check_laptop:

        $ basement_m_check_laptop = True

        show black

        show basement_m_screen_saver_myer_chan:
            zoom 0.35 xpos 100 ypos 50 alpha 1
            linear 1.0 xpos 300 ypos 330
            linear 1.7 xpos 800 ypos 50
            linear 0.6 xpos 1000 ypos 150
            linear 0.8 xpos 800 ypos 330
            linear 2.0 xpos 100 ypos 50
            repeat

        show bad_tv_signal onlayer ab_parallax:
            xalign 0.5 zoom 0.8
        show basement_m_laptop_zoom onlayer ab_parallax

        if basement_m_lamp_on:
            show basement_m_laptop_light onlayer ab_parallax

        $ renpy.transition(Dissolve(0.5))
        $ renpy.pause(1.0, hard='True')

        $ _skipping = True
        $ renpy.block_rollback()
        $ _rollback = True

        pause 2.0



        v "Monsieur M's laptop."

        $ rollback_ = True

        stop music fadeout 3.0

        $ renpy.pause(3.0, hard='True')

        $ renpy.music.set_volume(0.4, delay=0, channel='sound')
        play sound "music/John Past/discord.ogg"

        hide basement_m_screen_saver_myer_chan
        show basement_m_laptop_bg
        show monsieur_m_photo_1:
            xpos 940 ypos 88 xanchor 1.0
        show monsieur_m_photo_2:
            xpos 230 ypos 78
        show monsieur_m_photo_3:
            xpos 1020 ypos 78 xanchor 1.0

        $ renpy.pause(1.0, hard='True')

        v "!?"

        pause 1.0

        v "I feel like I'm not really supposed to see those photos..."

        hide monsieur_m_photo_1
        hide monsieur_m_photo_2
        hide monsieur_m_photo_3
    else:


        stop music fadeout 3.0

        scene black

        show basement_m_laptop_bg

        if not basement_m_photo_1_off:
            show monsieur_m_photo_1:
                xpos 940 ypos 88 xanchor 1.0

        if not basement_m_photo_2_off:
            show monsieur_m_photo_2:
                xpos 230 ypos 78

        if not basement_m_photo_3_off:
            show monsieur_m_photo_3:
                xpos 1020 ypos 78 xanchor 1.0

        show bad_tv_signal onlayer ab_parallax:
            xalign 0.5 zoom 0.8
        show basement_m_laptop_zoom onlayer ab_parallax

        if basement_m_lamp_on:
            show basement_m_laptop_light onlayer ab_parallax

        $ renpy.transition(Dissolve(0.5))
        $ renpy.pause(0.5, hard='True')

    $ renpy.block_rollback()
    $ _rollback = False
    $ rollback_ = False
    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False

    show screen basement_m_laptop_zoom_leave

    call screen basement_m_laptop_zoom

label basement_m_table_investigate_lamp:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show basement_m_desk at Position(xpos = 0, ypos = 0)

    show basement_m_desk:
        ease 0.5 zoom 2.0 xoffset 550 yoffset 720

    pause 0.5

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    v "The desk lamp on Monsieur M's desk."

    $ rollback_ = True

    if not basement_m_lamp_on:

        v "Should I turn it on?"

        menu:
            "Yes":

                show basement_m_desk:
                    ease 0.5 zoom 1.0 xoffset 0 yoffset 0

                $ renpy.pause(0.5, hard='True')

                $ renpy.block_rollback()
                $ _rollback = False

                if renpy.is_skipping():
                    $ renpy.choice_for_skipping()
                $ _skipping = False
                $ rollback_ = False
                $ renpy.music.stop(channel="beep", fadeout = 0.5)

                $ renpy.pause(0.2, hard='True')

                show black
                $ renpy.transition(Dissolve(1.0))
                $ renpy.pause(1.5, hard='True')

                $ basement_m_desk_image = "images/basement m flashback/basement m desk 2.png"

                hide black
                $ renpy.transition(Dissolve(1.0))
                $ renpy.pause(1.0, hard='True')

                $ basement_m_lamp_on = True

                call screen basement_m_table_screen
            "No":

                jump basement_m_do_nothing
    else:


        v "Should I turn it off?"

        menu:
            "Yes":
                show basement_m_desk:
                    ease 0.5 zoom 1.0 xoffset 0 yoffset 0

                $ renpy.pause(0.5, hard='True')

                if renpy.is_skipping():
                    $ renpy.choice_for_skipping()
                $ _skipping = False
                $ rollback_ = False
                $ renpy.music.stop(channel="beep", fadeout = 0.5)

                $ renpy.block_rollback()
                $ _rollback = False

                show black
                $ renpy.transition(Dissolve(1.0))
                $ renpy.pause(1.5, hard='True')

                $ basement_m_desk_image = "images/basement m flashback/basement m desk 1.png"

                hide black
                $ renpy.transition(Dissolve(1.0))
                $ renpy.pause(1.0, hard='True')

                $ basement_m_lamp_on = False

                call screen basement_m_table_screen
            "No":

                jump basement_m_do_nothing

label basement_m_do_nothing:

    show basement_m_desk:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    $ renpy.pause(0.5, hard='True')

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    $ renpy.block_rollback()
    $ _rollback = False

    call screen basement_m_table_screen with Dissolve(0.2)

label basement_m_table_investigate_folder:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show basement_m_desk at Position(xpos = 0, ypos = 0)

    show basement_m_desk:
        ease 0.5 zoom 2.0 xoffset -50 yoffset 50

    pause 0.5

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    if not basement_m_investigate_folder:

        v "The pink envelope on the desk."

        $ rollback_ = True

        $ renpy.music.set_volume(1.0, delay=0, channel='sound')
        play sound "music/PageFlipshort.ogg"

    show black:
        alpha 0.8
    with Dissolve(0.5)

    if basement_m_lamp_on:
        show basement_m_folder_hint_1
        $ basement_m_check_folder_light = True
    else:
        show basement_m_folder_hint_2
        $ basement_m_check_folder_dark = True

    if not basement_m_folder_realization:
        if basement_m_check_folder_dark and basement_m_check_folder_light:

            pause 0.5

            v "!?"

            $ rollback_ = True

            v "The colors have changed."

            v "So that's it. {w=0.5}The colors only show up when I turn on the lamp."

            $ basement_m_folder_realization = True

    if not basement_m_investigate_folder:

        pause 0.5

        $ basement_m_investigate_folder = True

        v "Inside was a piece of paper printed with strange rectangles."

        if basement_m_photo_1_off:

            v "It seems to be related to the picture on Monsieur M's laptop somehow."

    $ renpy.block_rollback()
    $ _rollback = False
    $ rollback_ = False
    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False

    call screen basement_m_table_puzzle_zoom

label basement_m_table_puzzle_zoom_leave:

    hide black
    hide basement_m_folder_hint_1
    hide basement_m_folder_hint_2
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    jump basement_m_do_nothing

label basement_m_table_investigate_mug:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show basement_m_desk at Position(xpos = 0, ypos = 0)

    show basement_m_desk:
        ease 0.5 zoom 2.0 xoffset -600 yoffset 350

    pause 0.5

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    v "Monsieur M's mug."

    $ rollback_ = True

    v "At first glance it looked like it was coffee, {w=0.5}but as you got closer it smelled like hot chocolate."

    stop music fadeout 3.0

    show basement_m_desk:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    $ renpy.pause(0.5, hard='True')

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    $ renpy.block_rollback()
    $ _rollback = False

    if not basement_m_lamp_on:

        show basement_m_desk_blurred_1:
            ease 0.4 xoffset -10 yoffset -10 alpha 0.5
            ease 0.4 xoffset 10 yoffset -10 alpha 0.5
            ease 0.4 xoffset -10 yoffset 10 alpha 0.5
            ease 0.4 xoffset 10 yoffset 10 alpha 0.5
            ease 0.4 xoffset 0 yoffset 0 alpha 1.0
    else:


        show basement_m_desk_blurred_2:
            ease 0.4 xoffset -10 yoffset -10 alpha 0.5
            ease 0.4 xoffset 10 yoffset -10 alpha 0.5
            ease 0.4 xoffset -10 yoffset 10 alpha 0.5
            ease 0.4 xoffset 10 yoffset 10 alpha 0.5
            ease 0.4 xoffset 0 yoffset 0 alpha 1.0

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

    hide basement_m_desk_blurred_1
    hide basement_m_desk_blurred_2
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    pause 1.0

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

    $ renpy.music.set_volume(1.0, delay=0, channel='robot memory')
    $ renpy.music.play("music/magic teleport.ogg", channel="robot memory", loop=False)

    $ renpy.pause(1.0, hard='True')

    hide white back
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    jump basement_m_past_to_present

label basement_m_table_teleport:

    stop music fadeout 1.0

    scene basement_4_cup_zoom
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

    show screen inventory_screen
    with Dissolve(0.2)

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music ("music/Tunnel/myersSewers.ogg")

    call screen basement_room_4_cup_screen
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
