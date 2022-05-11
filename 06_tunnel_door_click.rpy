


image myers_tunnel_john_robot:

    "images/tunnel/john_robot_animation/john_robot_1.png"
    pause 0.03
    "images/tunnel/john_robot_animation/john_robot_2.png"
    pause 0.03
    "images/tunnel/john_robot_animation/john_robot_3.png"
    pause 0.03
    "images/tunnel/john_robot_animation/john_robot_4.png"
    pause 0.03
    "images/tunnel/john_robot_animation/john_robot_5.png"
    pause 0.03
    "images/tunnel/john_robot_animation/john_robot_4.png"
    pause 0.03
    "images/tunnel/john_robot_animation/john_robot_3.png"
    pause 0.03
    "images/tunnel/john_robot_animation/john_robot_2.png"
    pause 0.03
    repeat

screen myers_tunnel_passcode_door:

    add "images/tunnel/myers_tunnel_passcode_block.png" xpos 300 ypos 200
    add "images/tunnel/myers_tunnel_passcode_block.png" xpos 470 ypos 200
    add "images/tunnel/myers_tunnel_passcode_block.png" xpos 640 ypos 200
    add "images/tunnel/myers_tunnel_passcode_block.png" xpos 810 ypos 200

    text "{size=+200}{color=#000}{font=impact.ttf}[myers_tunnel_door_code_1]{/font}{/color}{/size}" xpos 373 ypos 170 xalign 0.5
    text "{size=+200}{color=#000}{font=impact.ttf}[myers_tunnel_door_code_2]{/font}{/color}{/size}" xpos 543 ypos 170 xalign 0.5
    text "{size=+200}{color=#000}{font=impact.ttf}[myers_tunnel_door_code_3]{/font}{/color}{/size}" xpos 713 ypos 170 xalign 0.5
    text "{size=+200}{color=#000}{font=impact.ttf}[myers_tunnel_door_code_4]{/font}{/color}{/size}" xpos 883 ypos 170 xalign 0.5

    imagebutton:
        xpos 520
        ypos 610
        idle "images/tunnel/myers_tunnel_door_arrow_down_idle.png"
        hover "images/tunnel/myers_tunnel_door_arrow_down_hover.png"
        focus_mask "images/tunnel/myers_tunnel_door_arrow_down_hover.png"
        action Jump("myers_tunnel_passcode_door_leave")

    imagebutton:
        xpos 320
        ypos 110
        idle "images/tunnel/myers_tunnel_door_arrow_up_idle.png"
        hover "images/tunnel/myers_tunnel_door_arrow_up_hover.png"
        focus_mask "images/tunnel/myers_tunnel_door_arrow_up_idle.png"
        action [Play("sound", "music/Tunnel/wheelMoveSFX.ogg"), If(myers_tunnel_door_code_1 < 9, true=SetVariable("myers_tunnel_door_code_1", myers_tunnel_door_code_1 + 1), false=SetVariable("myers_tunnel_door_code_1", 0)), Jump("myers_tunnel_passcode_correct")]

    imagebutton:
        xpos 320
        ypos 450
        idle "images/tunnel/myers_tunnel_door_code_arrow_down_idle.png"
        hover "images/tunnel/myers_tunnel_door_code_arrow_down_hover.png"
        focus_mask "images/tunnel/myers_tunnel_door_code_arrow_down_hover.png"
        action [Play("sound", "music/Tunnel/wheelMoveSFX.ogg"), If(myers_tunnel_door_code_1 > 0, true=SetVariable("myers_tunnel_door_code_1", myers_tunnel_door_code_1 - 1), false=SetVariable("myers_tunnel_door_code_1", 9)), Jump("myers_tunnel_passcode_correct")]

    imagebutton:
        xpos 489
        ypos 110
        idle "images/tunnel/myers_tunnel_door_arrow_up_idle.png"
        hover "images/tunnel/myers_tunnel_door_arrow_up_hover.png"
        focus_mask "images/tunnel/myers_tunnel_door_arrow_up_idle.png"
        action [Play("sound", "music/Tunnel/wheelMoveSFX.ogg"), If(myers_tunnel_door_code_2 < 9, true=SetVariable("myers_tunnel_door_code_2", myers_tunnel_door_code_2 + 1), false=SetVariable("myers_tunnel_door_code_2", 0)), Jump("myers_tunnel_passcode_correct")]

    imagebutton:
        xpos 489
        ypos 450
        idle "images/tunnel/myers_tunnel_door_code_arrow_down_idle.png"
        hover "images/tunnel/myers_tunnel_door_code_arrow_down_hover.png"
        focus_mask "images/tunnel/myers_tunnel_door_code_arrow_down_hover.png"
        action [Play("sound", "music/Tunnel/wheelMoveSFX.ogg"), If(myers_tunnel_door_code_2 > 0, true=SetVariable("myers_tunnel_door_code_2", myers_tunnel_door_code_2 - 1), false=SetVariable("myers_tunnel_door_code_2", 9)), Jump("myers_tunnel_passcode_correct")]

    imagebutton:
        xpos 659
        ypos 110
        idle "images/tunnel/myers_tunnel_door_arrow_up_idle.png"
        hover "images/tunnel/myers_tunnel_door_arrow_up_hover.png"
        focus_mask "images/tunnel/myers_tunnel_door_arrow_up_idle.png"
        action [Play("sound", "music/Tunnel/wheelMoveSFX.ogg"), If(myers_tunnel_door_code_3 < 9, true=SetVariable("myers_tunnel_door_code_3", myers_tunnel_door_code_3 + 1), false=SetVariable("myers_tunnel_door_code_3", 0)), Jump("myers_tunnel_passcode_correct")]

    imagebutton:
        xpos 659
        ypos 450
        idle "images/tunnel/myers_tunnel_door_code_arrow_down_idle.png"
        hover "images/tunnel/myers_tunnel_door_code_arrow_down_hover.png"
        focus_mask "images/tunnel/myers_tunnel_door_code_arrow_down_hover.png"
        action [Play("sound", "music/Tunnel/wheelMoveSFX.ogg"), If(myers_tunnel_door_code_3 > 0, true=SetVariable("myers_tunnel_door_code_3", myers_tunnel_door_code_3 - 1), false=SetVariable("myers_tunnel_door_code_3", 9)), Jump("myers_tunnel_passcode_correct")]

    imagebutton:
        xpos 830
        ypos 110
        idle "images/tunnel/myers_tunnel_door_arrow_up_idle.png"
        hover "images/tunnel/myers_tunnel_door_arrow_up_hover.png"
        focus_mask "images/tunnel/myers_tunnel_door_arrow_up_idle.png"
        action [Play("sound", "music/Tunnel/wheelMoveSFX.ogg"), If(myers_tunnel_door_code_4 < 9, true=SetVariable("myers_tunnel_door_code_4", myers_tunnel_door_code_4 + 1), false=SetVariable("myers_tunnel_door_code_4", 0)), Jump("myers_tunnel_passcode_correct")]

    imagebutton:
        xpos 830
        ypos 450
        idle "images/tunnel/myers_tunnel_door_code_arrow_down_idle.png"
        hover "images/tunnel/myers_tunnel_door_code_arrow_down_hover.png"
        focus_mask "images/tunnel/myers_tunnel_door_code_arrow_down_hover.png"
        action [Play("sound", "music/Tunnel/wheelMoveSFX.ogg"), If(myers_tunnel_door_code_4 > 0, true=SetVariable("myers_tunnel_door_code_4", myers_tunnel_door_code_4 - 1), false=SetVariable("myers_tunnel_door_code_4", 9)), Jump("myers_tunnel_passcode_correct")]


label myers_tunnel_passcode_door_leave:

    hide transparent dark-small with Dissolve(0.2)

    show myers_tunnel_4:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    $ renpy.pause(0.5, hard='True')

    call screen myers_tunnel4 with Dissolve(0.2)

label myers_tunnel_passcode_correct:

    if myers_tunnel_door_code_1 == 0 and myers_tunnel_door_code_2 == 4 and myers_tunnel_door_code_3 == 3 and myers_tunnel_door_code_4 == 0:

        $ renpy.music.set_volume(0.6, delay=0, channel='sound')
        play sound "music/weapon click.ogg"

        noname "Access granted."

        hide transparent dark-small with Dissolve(0.5)

        show myers_tunnel_4:
            ease 0.5 zoom 1 xoffset 0 yoffset 0

        $ renpy.pause(0.5, hard='True')

        scene black

        show myers_tunnel_4_door_hollow
        show myers_tunnel_4_hollow

        $ renpy.pause(1.0, hard='True')

        $ renpy.music.set_volume(1.0, delay=0, channel='sound')
        play sound "music/Tunnel/GarageDoorSFX.ogg"

        show myers_tunnel_4_door_hollow:
            zoom 1 xoffset 0 yoffset 0
            ease 2.0 xoffset 0 yoffset -500
        $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 2.0, dist=15))
        $ renpy.pause(2.0, hard='True')

        stop sound fadeout 3.0
        stop music fadeout 5.0

        $ renpy.pause(3.0, hard='True')

        $ _skipping = True
        $ renpy.block_rollback()
        $ _rollback = True

        van "It worked."

        if renpy.is_skipping():
            $ renpy.choice_for_skipping()
        $ _skipping = False
        $ rollback_ = False
        $ renpy.music.stop(channel="beep", fadeout = 0.5)

        $ renpy.music.set_volume(0.4, delay=0, channel='sound')
        play sound ("music/Tunnel/horror-triller-whistle.ogg")

        $ renpy.pause(3.0, hard='True')
        stop sound fadeout 1.0
        $ renpy.pause(3.0, hard='True')

        $ renpy.music.set_volume(0.7, delay=0, channel='sound')
        play sound "music/first robot growl.ogg" fadeout 1.0

        show myers_tunnel_john_robot:
            zoom 0.45 xalign 0.5 yoffset 50
            linear 0.3 zoom 8.0 xalign 0.5 yoffset -1500

        show myers_tunnel_4_hollow:
            linear 0.05 xoffset -10 yoffset 10
            linear 0.05 xoffset 10 yoffset -10
            linear 0.05 xoffset 0 yoffset 10
            linear 0.05 xoffset -10 yoffset -10
            linear 0.05 xoffset 0 yoffset 0
            repeat

        $ renpy.pause(0.35, hard='True')

        scene black

        $ renpy.pause(1.0, hard='True')
        pause 3.0

        jump john_past_end
    else:

        call screen myers_tunnel_passcode_door
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
