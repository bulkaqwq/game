
image vb2_locker_zoom_1 = "images/vin battle 2/vb2_locker_zoom_1.png"
image vb2_locker_zoom_2 = "images/vin battle 2/vb2_locker_zoom_2.png"
image vb2_ammo_zoom = "images/vin battle 2/vb2_ammo_zoom.png"
image vb2_bucket_zoom = "images/vin battle 2/vb2_bucket_zoom.png"
image vb2_uniform_zoom = "images/vin battle 2/vb2_uniform_zoom.png"
image vb2_tech_zoom = "images/vin battle 2/vb2_tech_zoom.png"
image vb2_plush_zoom = "images/vin battle 2/vb2_plush_zoom.png"
image vb2_flashlight_zoom = "images/vin battle 2/vb2_flashlight_zoom.png"
image vb2_cube_zoom = "images/vin battle 2/vb2_cube_zoom.png"

label vb2_locker_1:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show black as black_2:
        alpha 0.5
    show vb2_locker_zoom_1
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/basement/zs_locker.ogg")

    show vb2_locker_zoom_2
    show vb2_plush_zoom:
        xalign 0.5 yalign 0.5 zoom 0.01
        ease 0.5 zoom 1.0
    hide vb2_locker_zoom_1
    $ renpy.transition(Dissolve(0.2))
    $ renpy.pause(1.0, hard='True')

    pause 0.5

    v "A teddy bear."

    $ renpy.pause(0.1, hard='True')

    hide vb2_locker_zoom_2
    hide vb2_plush_zoom
    hide black_2
    with Dissolve(0.5)

    call screen vin_bat_2_4_screen

label vb2_locker_2:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show black as black_2:
        alpha 0.5
    show vb2_locker_zoom_1
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/basement/zs_locker.ogg")

    show vb2_locker_zoom_2
    show vb2_ammo_zoom:
        xalign 0.5 yalign 0.5 zoom 0.01
        ease 0.5 zoom 1.0
    hide vb2_locker_zoom_1
    $ renpy.transition(Dissolve(0.2))
    $ renpy.pause(1.0, hard='True')

    pause 0.5

    v "Some bullets."

    $ renpy.pause(0.1, hard='True')

    hide vb2_locker_zoom_2
    hide vb2_ammo_zoom
    hide black_2
    with Dissolve(0.5)

    call screen vin_bat_2_4_screen

label vb2_locker_3:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show black as black_2:
        alpha 0.5
    show vb2_locker_zoom_1
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/basement/zs_locker.ogg")

    show vb2_locker_zoom_2
    show vb2_tech_zoom:
        xalign 0.5 yalign 0.5 zoom 0.01
        ease 0.5 zoom 1.0
    hide vb2_locker_zoom_1
    $ renpy.transition(Dissolve(0.2))
    $ renpy.pause(1.0, hard='True')

    pause 0.5

    v "Some kind of high-tech wristband."

    $ renpy.pause(0.1, hard='True')

    hide vb2_locker_zoom_2
    hide vb2_tech_zoom
    hide black_2
    with Dissolve(0.5)

    call screen vin_bat_2_4_screen

label vb2_locker_4:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show black as black_2:
        alpha 0.5
    show vb2_locker_zoom_1
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/basement/zs_locker.ogg")

    show vb2_locker_zoom_2
    show vb2_flashlight_zoom:
        xalign 0.5 yalign 0.5 zoom 0.01
        ease 0.5 zoom 1.0
    if not vb2_meet_shadow_van:

        $ renpy.music.set_volume(1.0, delay=0, channel='sound1')
        $ renpy.music.play("music/basement/vita_female_giggle.ogg", channel="sound1", loop = False)

        show basement_shadow_vanora:
            xalign 0.52 yalign 0.5 zoom 1.0
            ease 0.5 zoom 4.0 xalign 0.52 alpha 0

        $ vb2_meet_shadow_van = True

    hide vb2_locker_zoom_1
    $ renpy.transition(Dissolve(0.2))
    $ renpy.pause(1.0, hard='True')

    pause 0.5

    v "A flashlight."

    $ renpy.pause(0.1, hard='True')

    hide vb2_locker_zoom_2
    hide vb2_flashlight_zoom
    hide black_2
    hide basement_shadow_vanora
    with Dissolve(0.5)

    call screen vin_bat_2_4_screen

label vb2_locker_5:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show black as black_2:
        alpha 0.5
    show vb2_locker_zoom_1
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/basement/zs_locker.ogg")

    show vb2_locker_zoom_2
    show vb2_uniform_zoom:
        xalign 0.5 yalign 0.5 zoom 0.01
        ease 0.5 zoom 1.0
    hide vb2_locker_zoom_1
    $ renpy.transition(Dissolve(0.2))
    $ renpy.pause(1.0, hard='True')

    pause 0.5

    v "A variety of professional uniforms."

    $ renpy.pause(0.1, hard='True')

    hide vb2_locker_zoom_2
    hide vb2_uniform_zoom
    hide black_2
    with Dissolve(0.5)

    call screen vin_bat_2_4_screen

label vb2_locker_6:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show black as black_2:
        alpha 0.5
    show vb2_locker_zoom_1
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/basement/zs_locker.ogg")

    show vb2_locker_zoom_2
    show vb2_cube_zoom:
        xalign 0.5 yalign 0.5 zoom 0.01
        ease 0.5 zoom 1.0
    hide vb2_locker_zoom_1
    $ renpy.transition(Dissolve(0.2))
    $ renpy.pause(1.0, hard='True')

    pause 0.5

    v "A Rubik's Cube that's been taken apart."

    $ renpy.pause(0.1, hard='True')

    hide vb2_locker_zoom_2
    hide vb2_cube_zoom
    hide black_2
    with Dissolve(0.5)

    call screen vin_bat_2_4_screen

label vb2_locker_7:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show black as black_2:
        alpha 0.5
    show vb2_locker_zoom_1
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/basement/zs_locker.ogg")

    show vb2_locker_zoom_2
    show vb2_bucket_zoom:
        xalign 0.5 yalign 0.5 zoom 0.01
        ease 0.5 zoom 1.0
    hide vb2_locker_zoom_1
    $ renpy.transition(Dissolve(0.2))
    $ renpy.pause(1.0, hard='True')

    pause 0.5

    v "A bucket for cleaning."

    $ renpy.pause(0.1, hard='True')

    hide vb2_locker_zoom_2
    hide vb2_bucket_zoom
    hide black_2
    with Dissolve(0.5)

    call screen vin_bat_2_4_screen
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
