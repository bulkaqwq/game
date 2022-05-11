
image basement_m_laptop_light = "images/basement m flashback/basement-m-laptop-light.png"
image basement_m_laptop_bg = "images/basement m flashback/monsieur m laptop bg.png"


image monsieur_m_photo_1 = "images/basement m flashback/monsieur m photo 1.png"
image monsieur_m_photo_2 = "images/basement m flashback/monsieur m photo 2.png"
image monsieur_m_photo_3 = "images/basement m flashback/monsieur m photo 3.png"

screen basement_m_laptop_zoom:

    layer "tvsignal"

    if (not basement_m_photo_1_off) and basement_m_photo_2_off and basement_m_photo_3_off:
        imagebutton:
            xpos 940 ypos 88 xanchor 1.0
            idle "images/basement m flashback/monsieur m photo 1.png"
            hover "images/basement m flashback/monsieur m photo 1 hover.png"
            focus "images/basement m flashback/monsieur m photo 1.png"
            action Jump("basement_m_laptop_close_photo_1")

    else:
        if not basement_m_photo_1_off:
            imagebutton:
                xpos 940 ypos 88 xanchor 1.0
                idle "images/basement m flashback/monsieur m photo 1.png"
                hover "images/basement m flashback/monsieur m photo 1.png"
                focus "images/basement m flashback/monsieur m photo 1.png"
                action NullAction()

    if not basement_m_photo_2_off:
        imagebutton:
            xpos 230
            ypos 78
            idle "images/basement m flashback/monsieur m photo 2.png"
            hover "images/basement m flashback/monsieur m photo 2 hover.png"
            focus "images/basement m flashback/monsieur m photo 2.png"
            action Jump("basement_m_laptop_close_photo_2")

    if not basement_m_photo_3_off:
        imagebutton:
            xpos 1020
            ypos 78
            xanchor 1.0
            idle "images/basement m flashback/monsieur m photo 3.png"
            hover "images/basement m flashback/monsieur m photo 3 hover.png"
            focus "images/basement m flashback/monsieur m photo 3.png"
            action Jump("basement_m_laptop_close_photo_3")

screen basement_m_laptop_zoom_leave:

    layer "ab_parallax"

    imagebutton:
        xpos 520
        ypos 610
        idle "images/basement/basement_door_arrow_down_idle.png"
        hover "images/tunnel/myers_tunnel_door_arrow_down_hover.png"
        focus_mask "images/basement/basement_door_arrow_down_idle.png"
        action Jump("basement_m_table_laptop_zoom_leave")

label basement_m_laptop_close_photo_1:

    hide screen basement_m_laptop_zoom_leave

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/misc_menu.wav"

    show monsieur_m_photo_1:
        xpos 940 ypos 88 xanchor 1.0
        linear 0.5 zoom 0.001

    $ basement_m_photo_1_off = True

    $ renpy.pause(0.5, hard='True')

    if basement_m_investigate_folder:

        v "Hmm... {w=0.5}Looks like this picture is related to that piece of paper in the envelope."
    else:


        v "Hmm? {w=0.5}This picture looks like a clue of some sort."

    hide monsieur_m_photo_1
    hide monsieur_m_photo_2
    hide monsieur_m_photo_3

    show screen basement_m_laptop_zoom_leave

    call screen basement_m_laptop_zoom

label basement_m_laptop_close_photo_2:

    hide screen basement_m_laptop_zoom_leave

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/misc_menu.wav"

    if not basement_m_photo_3_off:

        show monsieur_m_photo_1:
            xpos 940 ypos 88 xanchor 1.0
        show monsieur_m_photo_2:
            xpos 230 ypos 78
            linear 0.5 zoom 0.001
        show monsieur_m_photo_3:
            xpos 1020 ypos 78
            xanchor 1.0
    else:


        show monsieur_m_photo_1:
            xpos 940 ypos 88 xanchor 1.0
        show monsieur_m_photo_2:
            xpos 230 ypos 78
            linear 0.5 zoom 0.001

    $ basement_m_photo_2_off = True

    $ renpy.pause(0.5, hard='True')

    hide monsieur_m_photo_1
    hide monsieur_m_photo_2
    hide monsieur_m_photo_3

    show screen basement_m_laptop_zoom_leave

    call screen basement_m_laptop_zoom

label basement_m_laptop_close_photo_3:

    hide screen basement_m_laptop_zoom_leave

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/misc_menu.wav"

    if not basement_m_photo_2_off:

        show monsieur_m_photo_1:
            xpos 940 ypos 88 xanchor 1.0
        show monsieur_m_photo_2:
            xpos 230 ypos 78
        show monsieur_m_photo_3:
            xpos 1020 ypos 78
            xanchor 1.0
            linear 0.5 zoom 0.001
    else:


        show monsieur_m_photo_1:
            xpos 940 ypos 88 xanchor 1.0
        show monsieur_m_photo_3:
            xpos 1020 ypos 78 xanchor 1.0
            linear 0.5 zoom 0.001

    $ basement_m_photo_3_off = True

    $ renpy.pause(0.5, hard='True')

    hide monsieur_m_photo_1
    hide monsieur_m_photo_2
    hide monsieur_m_photo_3

    show screen basement_m_laptop_zoom_leave

    call screen basement_m_laptop_zoom

label basement_m_table_laptop_zoom_leave:

    hide screen basement_m_laptop_zoom_leave

    if not basement_m_photo_1_off:
        show monsieur_m_photo_1:
            xpos 940 ypos 88 xanchor 1.0

    if not basement_m_photo_2_off:
        show monsieur_m_photo_2:
            xpos 230 ypos 78

    if not basement_m_photo_3_off:
        show monsieur_m_photo_3:
            xpos 1020 ypos 78 xanchor 1.0

    $ renpy.pause(0.1, hard='True')

    scene black
    hide bad_tv_signal onlayer ab_parallax
    hide basement_m_laptop_zoom onlayer ab_parallax
    hide basement_m_laptop_light onlayer ab_parallax
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(1.0, hard='True')

    $ renpy.music.set_volume(0.7, delay=0, channel='music')
    play music ("music/bgm/M office bgm.ogg")

    scene basement_m_desk
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    call screen basement_m_table_screen
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
