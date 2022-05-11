


image myers_tunnel_3_spook_shadow:
    contains:
        "images/tunnel/myers_tunnel_3_sppook_shadow_1.png"
    contains:
        "images/tunnel/myers_tunnel_3_sppook_shadow_2.png"
        alpha 0.8
        pause 0.05
        alpha 1.0
        pause 0.05
        repeat

image myers_tunnel_light_fickering:
    contains:
        "images/transparent dark-small.png"
        alpha 0
        pause 1.0
        linear 2.0 alpha 0.55
        pause 0.2
        linear 1.0 alpha 0.3
        pause 1.0
        linear 0.5 alpha 0
        repeat

image myers_tunnel_1_flickering:
    contains:
        "images/tunnel/Myers_Tunnel_1.png"
    contains:
        "myers_tunnel_light_fickering"

image myers_tunnel_2_flickering:
    contains:
        "images/tunnel/Myers_Tunnel_2.png"
    contains:
        "myers_tunnel_light_fickering"

image myers_tunnel_3_flickering:
    contains:
        "images/tunnel/Myers_Tunnel_3.png"
    contains:
        "myers_tunnel_light_fickering"

image myers_tunnel_3_mascot_flickering:
    contains:
        "images/tunnel/Myers_Tunnel_3_mascot.png"
    contains:
        "myers_tunnel_light_fickering"

image myers_tunnel_3_shadow:
    "images/tunnel/myers_tunnel_3_shadow_1.png"
    pause 0.8
    "images/tunnel/myers_tunnel_3_shadow_2.png"
    pause 0.1
    "images/tunnel/myers_tunnel_3_shadow_3.png"
    pause 0.1
    "images/empty-screen-small.png"

image myers_tunnel_spook_1 = "images/tunnel/tunnel spook/tunnel_spook_1.png"
image myers_tunnel_spook_2 = "images/tunnel/tunnel spook/tunnel_spook_2.png"

image myers_tunnel_invitation_zoom = "images/tunnel/myers_tunnel_invitation_zoom.png"

screen myers_tunnel1:

    imagebutton:
        xpos 745
        ypos 380
        idle "images/tunnel/myers_tunnel_1_arrow_idle.png"
        hover "images/tunnel/myers_tunnel_1_arrow_selected.png"
        focus_mask "images/tunnel/myers_tunnel_1_arrow_selected.png"
        action Jump("myers_tunnel__2")

screen myers_tunnel2:

    imagebutton:
        xpos 657
        ypos 276
        idle "images/tunnel/myers_tunnel_2_blood_idle.png"
        hover "images/tunnel/myers_tunnel_2_blood_hover.png"
        focus_mask "images/tunnel/myers_tunnel_2_blood_hover.png"
        action Jump("myers_tunnel_2_investigate_blood")

    imagebutton:
        xpos 586
        ypos 450
        idle "images/tunnel/myers_tunnel_2_arrow_up_idle.png"
        hover "images/tunnel/myers_tunnel_2_arrow_up_selected.png"
        focus_mask "images/tunnel/myers_tunnel_2_arrow_up_idle.png"
        action Jump("myers_tunnel__3")

    imagebutton:
        xpos 560
        ypos 550
        idle "images/tunnel/myers_tunnel_2_arrow_down_idle.png"
        hover "images/tunnel/myers_tunnel_2_arrow_down_selected.png"
        focus_mask "images/tunnel/myers_tunnel_2_arrow_down_idle.png"
        action Jump("myers_tunnel__1")

screen myers_tunnel3:

    imagebutton:
        xpos 430
        ypos 435
        idle "images/tunnel/myers_tunnel_3_arrow_up_idle.png"
        hover "images/tunnel/myers_tunnel_3_arrow_up_selected.png"
        focus_mask "images/tunnel/myers_tunnel_3_arrow_up_selected.png"
        action Jump("myers_tunnel__4")

    imagebutton:
        xpos 455
        ypos 550
        idle "images/tunnel/myers_tunnel_3_arrow_down_idle.png"
        hover "images/tunnel/myers_tunnel_3_arrow_down_selected.png"
        focus_mask "images/tunnel/myers_tunnel_3_arrow_down_selected.png"
        action Jump("myers_tunnel__2")

    imagebutton:
        xpos 578
        ypos 398
        idle "images/tunnel/myers_tunnel_3_blood_idle.png"
        hover "images/tunnel/myers_tunnel_3_blood_hover.png"
        focus_mask "images/tunnel/myers_tunnel_3_blood_hover.png"
        action Jump("myers_tunnel_3_investigate_blood")

    imagebutton:
        xpos 855
        ypos 69
        idle "images/tunnel/myers_tunnel_3_invitation_idle.png"
        hover "images/tunnel/myers_tunnel_3_invitation_hover.png"
        focus_mask "images/tunnel/myers_tunnel_3_invitation_hover.png"
        action Jump("myers_tunnel_3_investigate_invitation")

    if myers_tunnel_drop_mascot:
        imagebutton:
            xpos 144
            ypos 475
            idle "images/tunnel/myers_tunnel_3_mascot_idle.png"
            hover "images/tunnel/myers_tunnel_3_mascot_hover.png"
            focus_mask "images/tunnel/myers_tunnel_3_mascot_hover.png"
            action Jump("myers_tunnel_3_investigate_mascot")

screen myers_tunnel4:

    imagebutton:
        xpos 580
        ypos 600
        idle "images/tunnel/myers_tunnel_4_arrow_idle.png"
        hover "images/tunnel/myers_tunnel_4_arrow_hover.png"
        focus_mask "images/tunnel/myers_tunnel_4_arrow_idle.png"
        action Jump("myers_tunnel__3")

    imagebutton:
        xpos 507
        ypos 80
        idle "images/tunnel/myers_tunnel_4_door_idle.png"
        hover "images/tunnel/myers_tunnel_4_door_hover.png"
        focus_mask "images/tunnel/myers_tunnel_4_door_hover.png"
        action Jump("myers_tunnel_4_investigate_door")

    imagebutton:
        xpos 220
        ypos 320
        idle "images/tunnel/myers_tunnel_4_blood_idle.png"
        hover "images/tunnel/myers_tunnel_4_blood_hover.png"
        focus_mask "images/tunnel/myers_tunnel_4_blood_hover.png"
        action Jump("myers_tunnel_4_investigate_blood")

screen myers_tunnel_mascot_screen:

    if not myers_tunnel_travel_john_past:
        imagebutton:
            xpos 0
            ypos 0
            idle "images/empty-screen-small.png"
            hover "images/tunnel/Myers_Tunnel_mascot_hover.png"
            focus_mask "images/tunnel/Myers_Tunnel_mascot_hover.png"
            action Jump("myers_tunnel_mascot_close_up_investigate")
    else:
        imagebutton:
            xpos 0
            ypos 0
            idle "images/empty-screen-small.png"
            hover "images/tunnel/Myers_Tunnel_mascot_hover.png"
            focus_mask "images/tunnel/Myers_Tunnel_mascot_hover.png"
            action Jump("myers_tunnel_mascot_teleport")

    imagebutton:
        xpos 580
        ypos 600
        idle "images/tunnel/myers_tunnel_4_arrow_idle.png"
        hover "images/tunnel/myers_tunnel_4_arrow_hover.png"
        focus_mask "images/tunnel/myers_tunnel_4_arrow_idle.png"
        action Jump("myers_tunnel_3_finish_investigate_mascot")

label myers_tunnel__1:

    scene black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound ("music/Tunnel/FootSteps_EmployeePass.ogg")

    $ renpy.pause(0.1, hard='True')

    pause 1.5

    $ renpy.pause(2.5, hard='True')

    stop sound fadeout 2.0

    scene myers_tunnel_1_flickering
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    call screen myers_tunnel1 with Dissolve(0.1)

label myers_tunnel__2:

    scene black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound ("music/Tunnel/FootSteps_EmployeePass.ogg")

    $ renpy.pause(0.1, hard='True')

    if not myers_tunnel_see_blood:
        $ renpy.pause(1.5, hard='True')
    else:
        pause 1.5

    $ renpy.pause(2.5, hard='True')

    stop sound fadeout 2.0

    scene myers_tunnel_2_flickering
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    if not myers_tunnel_see_blood:

        $ renpy.pause(0.5, hard='True')

        pause 0.5

        $ myers_tunnel_see_blood = True

        $ renpy.music.set_volume(1.0, delay=0, channel='sound')
        play sound ("music/zoom.wav")

        show myers_tunnel_2_flickering at Position(xpos = 0, ypos = 0)

        show myers_tunnel_2_flickering:
            ease 0.5 zoom 2.5 xoffset -300 yoffset 450

        $ renpy.pause(0.5, hard='True')

        $ _skipping = True
        $ renpy.block_rollback()
        $ _rollback = True

        pause 1.0

        van "!?"

        $ rollback_ = True

        van "A puddle of blood."

        van "To be honest, {w=0.5}this is not what I wanted to see. {w=0.5}But I'm starting to get used to it."

        pause 1.0

        van "......"

        van "From the shape of the blood spatter, {w=0.5}it looks like a body has been dragged deeper into the tunnel after someone was killed."

        $ renpy.music.set_volume(0.1, delay=0, channel='sound')
        play sound "music/cloth.mp3" fadeout 2.0

        pause 1.5

        van "I squatted down and carefully dipped my fingertips into it."

        pause 1.0

        van "......"

        van "No hallucinations, {w=0.5}nothing happened this time."

        van "But......"

        pause 1.0

        van "I rubbed my fingertips with my thumb."

        $ renpy.music.set_volume(1.0, delay=0, channel='sound')
        play sound "music/vic horror.ogg"

        pause 1.5

        van "This puddle of blood... {w=0.5}{color=#f00}it's not completely dried up{/color}."

        van "......"

        van "In other words, {w=0.5}I may not be the only uninvited guest here."

        van "I need to be careful."

        show myers_tunnel_2_flickering:
            ease 0.5 zoom 1 xoffset 0 yoffset 0
        $ renpy.pause(0.5, hard='True')

        if renpy.is_skipping():
            $ renpy.choice_for_skipping()
        $ _skipping = False
        $ rollback_ = False
        $ renpy.music.stop(channel="beep", fadeout = 0.5)

        hide myers_tunnel_2_flickering
        scene myers_tunnel_2_flickering

        $ renpy.block_rollback()
        $ _rollback = False

    call screen myers_tunnel2 with Dissolve(0.1)

label myers_tunnel__3:

    scene black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound ("music/Tunnel/FootSteps_EmployeePass.ogg")

    $ renpy.pause(0.1, hard='True')

    if not myers_tunnel_see_shadow:

        $ renpy.pause(1.5, hard='True')
    else:
        pause 1.5

    $ renpy.pause(2.5, hard='True')

    stop sound fadeout 2.0

    if not myers_tunnel_drop_mascot:
        if not myers_tunnel_see_shadow:

            $ myers_tunnel_see_shadow = True

            scene myers_tunnel_3_flickering
            show myers_tunnel_3_shadow
            show myers_tunnel_3_spook_shadow
            $ renpy.transition(Dissolve(0.5))
            $ renpy.pause(0.5, hard='True')

            $ renpy.music.set_volume(1.0, delay=0, channel='sound')
            play sound ["<silence 0.3>", "music/Tunnel/ohSoScared.ogg"]

            $ renpy.pause(2.0, hard='True')

            hide myers_tunnel_3_spook_shadow
            $ renpy.transition(Dissolve(1.0))
            $ renpy.pause(1.0, hard='True')

            $ _skipping = True
            $ renpy.block_rollback()
            $ _rollback = True

            van "!?"

            $ rollback_ = False

            van "Who was that?"

            if renpy.is_skipping():
                $ renpy.choice_for_skipping()
            $ _skipping = False
            $ rollback_ = False
            $ renpy.music.stop(channel="beep", fadeout = 0.5)
        else:


            scene myers_tunnel_3_flickering
            $ renpy.transition(Dissolve(0.5))
            $ renpy.pause(0.5, hard='True')
    else:

        scene myers_tunnel_3_mascot_flickering
        $ renpy.transition(Dissolve(0.5))
        $ renpy.pause(0.5, hard='True')

        if not myers_tunnel_see_mascot_shock:

            $ myers_tunnel_see_mascot_shock = True

            $ renpy.music.set_volume(1.0, delay=0, channel='sound')
            play sound "music/Tunnel/ZoomInSFX.ogg"

            $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15))
            $ renpy.pause(1.0, hard='True')

    call screen myers_tunnel3 with Dissolve(0.1)

label myers_tunnel__4:

    scene black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound ("music/Tunnel/FootSteps_EmployeePass.ogg")

    $ renpy.pause(0.1, hard='True')

    if not myers_tunnel_drop_mascot:

        $ renpy.pause(3.0, hard='True')
        show myers_tunnel_spook_1
        $ renpy.pause(0.1, hard='True')
        show myers_tunnel_spook_2
        $ renpy.pause(0.1, hard='True')
        hide myers_tunnel_spook_1
        hide myers_tunnel_spook_2
        $ renpy.pause(1.0, hard='True')
    else:
        pause 1.5
        $ renpy.pause(2.5, hard='True')

    stop sound fadeout 2.0

    scene myers_tunnel_4
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    if not myers_tunnel_drop_mascot:

        $ myers_tunnel_drop_mascot = True

        $ _skipping = True
        $ renpy.block_rollback()
        $ _rollback = True

        pause 2.5

        van "!?"

        $ rollback_ = True

        $ renpy.music.set_volume(1.0, delay=0, channel='sound')
        play sound ("music/zoom.wav")

        show myers_tunnel_4 at Position(xpos = 0, ypos = 0)

        show myers_tunnel_4:
            ease 0.5 zoom 1.5 xoffset 0 yoffset 250

        $ renpy.pause(0.5, hard='True')

        pause 1.0

        van "This should be the end of the employee passageway."

        van "To be honest, {w=0.5}it is not as long as I thought it would be."

        show myers_tunnel_4:
            ease 0.5 zoom 1 xoffset 0 yoffset 0

        pause 1.0

        van "But before that..."

        hide myers_tunnel_4
        scene myers_tunnel_4

        pause 0.5

        van "I looked around and took a deep breath."

        pause 1.0

        stop music fadeout 5.0

        $ renpy.pause(0.1, hard="True")

        $ renpy.music.set_volume(0.6, delay=0, channel='sound')
        play sound "music/shake.ogg"

        van "\"Anybody here???\"{w=0.5} I called out into the passage." with Shake((0.5, 1.0, 0.5, 1.0), 3.0, dist=15)

        $ renpy.pause(0.5, hard=True)

        $ renpy.music.set_volume(0.6, delay=0, channel='sound')
        play sound "music/Tunnel/creepy-bouncing-whooshes.ogg"

        $ renpy.pause(3.0, hard=True)

        van "!?"

        stop sound fadeout 4.0

        $ renpy.pause(3.0, hard=True)

        van "......Oh."

        van "For a moment,{w=0.5} I thought I heard a low,{w=0.5} vague reply."

        van "But it was just a distorted echo of my own voice."

        van "......{w=0.5}Strangely enough, {w=0.5}the figure I had just seen is now inexplicably gone."

        van "And there is an even trickier problem at hand -"

        van "If I want to access the lobby, {w=0.5}I'll need to enter a four-digit code."

        van "Well... {w=0.5}In this case..."

        van "I started thinking."

        $ renpy.music.set_volume(0.6, delay=0, channel='music')
        play music "music/myers lobby/lobby horror.ogg"

        pause 1.0

        $ renpy.pause(0.1, hard="True")

        show transparent dark-small:
            alpha 0.3
            pause 0.3
            alpha 0.15
            pause 0.2
            alpha 1.0
            pause 0.05
            alpha 0.3
            pause 0.5
            alpha 0.7
            pause 0.01
            alpha 0.1
            pause 0.01
            alpha 3.0
            pause 0.05
            alpha 0.05
            pause 0.05
            alpha 1.0
            pause 0.05
            alpha 0.0
            pause 0.05
            alpha 0.5
            pause 0.35
            alpha 0.1
            pause 0.05
            alpha 0.2
            pause 1.0
            repeat

        $ renpy.music.set_volume(0.3, delay=0, channel='electricity')
        $ renpy.music.play("music/electricity.ogg", channel="electricity", loop=False)

        pause 2.0
        $ renpy.pause(1.5, hard='True')

        $ renpy.music.set_volume(0.6, delay=0, channel='sound')
        play sound ("music/Tunnel/glass break.ogg")

        with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

        $ renpy.music.stop(channel="electricity", fadeout = 1.0)
        hide transparent dark-small with Dissolve(1.0)

        stop music fadeout 3.0

        $ renpy.pause(2.0, hard='True')

        van "!?"

        van "Just then, {w=0.5}a screeching noise coming from behind me interrupted my thoughts."

        van "What was that noise?"

        stop music

        $ renpy.music.set_volume(1.0, delay=0, channel='music')
        play music ("music/Tunnel/myersSewers.ogg")

        if renpy.is_skipping():
            $ renpy.choice_for_skipping()
        $ _skipping = False
        $ rollback_ = False
        $ renpy.music.stop(channel="beep", fadeout = 0.5)
        $ renpy.block_rollback()
        $ _rollback = False

    call screen myers_tunnel4 with Dissolve(0.1)

label myers_tunnel_2_investigate_blood:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show myers_tunnel_2_flickering at Position(xpos = 0, ypos = 0)

    show myers_tunnel_2_flickering:
        ease 0.5 zoom 2.5 xoffset -300 yoffset 450

    $ renpy.pause(0.5, hard='True')

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    van "A puddle of blood."

    $ rollback_ = True

    van "It looks like a body was dragged deeper into the tunnel after someone was killed."

    van "The bloodstain is fresh and not completely dried up."

    van "That means that someone has just been here."

    van "...Or maybe a cyborg."

    show myers_tunnel_2_flickering:
        ease 0.5 zoom 1 xoffset 0 yoffset 0
    $ renpy.pause(0.5, hard='True')

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    hide myers_tunnel_2_flickering
    scene myers_tunnel_2_flickering

    $ renpy.block_rollback()
    $ _rollback = False

    call screen myers_tunnel2 with Dissolve(0.1)

label myers_tunnel_3_investigate_blood:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    if not myers_tunnel_drop_mascot:

        show myers_tunnel_3_flickering at Position(xpos = 0, ypos = 0)

        show myers_tunnel_3_flickering:
            ease 0.5 zoom 2.5 xoffset -300 yoffset 150
    else:


        show myers_tunnel_3_mascot_flickering at Position(xpos = 0, ypos = 0)

        show myers_tunnel_3_mascot_flickering:
            ease 0.5 zoom 2.5 xoffset -300 yoffset 150

    $ renpy.pause(0.5, hard='True')
    pause 0.5

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    van "The blood trail ends here."

    $ rollback_ = True

    van "But strangely enough, {w=0.5}there is no corpse to be seen anywhere."

    if not myers_tunnel_drop_mascot:

        show myers_tunnel_3_flickering:
            ease 0.5 zoom 1 xoffset 0 yoffset 0

        $ renpy.pause(0.5, hard='True')

        if renpy.is_skipping():
            $ renpy.choice_for_skipping()
        $ _skipping = False
        $ rollback_ = False
        $ renpy.music.stop(channel="beep", fadeout = 0.5)

        hide myers_tunnel_3_flickering
        scene myers_tunnel_3_flickering
    else:


        show myers_tunnel_3_mascot_flickering:
            ease 0.5 zoom 1 xoffset 0 yoffset 0

        $ renpy.pause(0.5, hard='True')

        if renpy.is_skipping():
            $ renpy.choice_for_skipping()
        $ _skipping = False
        $ rollback_ = False
        $ renpy.music.stop(channel="beep", fadeout = 0.5)

        hide myers_tunnel_3_mascot_flickering
        scene myers_tunnel_3_mascot_flickering

    $ renpy.block_rollback()
    $ _rollback = False

    call screen myers_tunnel3 with Dissolve(0.1)

label myers_tunnel_3_investigate_invitation:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    if not myers_tunnel_drop_mascot:

        show myers_tunnel_3_flickering at Position(xpos = 0, ypos = 0)

        show myers_tunnel_3_flickering:
            ease 0.5 zoom 2.5 xoffset -700 yoffset 1050
    else:


        show myers_tunnel_3_mascot_flickering at Position(xpos = 0, ypos = 0)

        show myers_tunnel_3_mascot_flickering:
            ease 0.5 zoom 2.5 xoffset -700 yoffset 1050

    $ renpy.pause(0.5, hard='True')

    show transparent dark-small:
        alpha 0.5
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')
    show myers_tunnel_invitation_zoom onlayer inyourface

    pause 1.0

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    $ renpy.pause(0.1, hard='True')

    van "Is this...{w=0.5} an invitation?"

    $ rollback_ = True

    van "The bottom half of the invitation has been burned, {w=0.5}so I can't see what came after."

    van "But on the invitation, {w=0.5}someone has written a small paragraph with a pen that looks like it has been added afterwards."

    pause 1.0

    noname "\"Do you like parties?\""

    noname "\"Enjoying good food and drink,{w=0.5} strengthening relationships... {w=0.5}the fact that there is a party proves that it is a day to be celebrated.\""

    noname "\"But unfortunately, {w=0.5}happiness and disaster are not absolute.\""

    noname "\"They are interdependent and can be transformed into each other.\""

    noname "\"In what looks like a charming backyard,{w=0.5} hidden beneath the lawn,{w=0.5} can be ugly, {w=0.5}wriggling insects.\""

    noname "\"And what may seem like a good time to you,{w=0.5} may be a shadow that lingers for the rest of his life.\""

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    hide myers_tunnel_invitation_zoom onlayer inyourface
    hide transparent dark-small

    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    if not myers_tunnel_drop_mascot:

        show myers_tunnel_3_flickering:
            ease 0.5 zoom 1 xoffset 0 yoffset 0

        $ renpy.pause(0.5, hard='True')

        hide myers_tunnel_3_flickering

        scene myers_tunnel_3_flickering
    else:


        show myers_tunnel_3_mascot_flickering:
            ease 0.5 zoom 1 xoffset 0 yoffset 0

        $ renpy.pause(0.5, hard='True')

        hide myers_tunnel_3_mascot_flickering

        scene myers_tunnel_3_mascot_flickering

    $ renpy.block_rollback()
    $ _rollback = False

    call screen myers_tunnel3 with Dissolve(0.1)

label myers_tunnel_4_investigate_blood:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show myers_tunnel_4 at Position(xpos = 0, ypos = 0)

    show myers_tunnel_4:
        ease 0.5 zoom 2.5 xoffset 700 yoffset 300

    $ renpy.pause(0.5, hard='True')
    pause 0.5

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    van "\"The day the nightmare began.\""

    show myers_tunnel_4:
        ease 0.5 zoom 1 xoffset 0 yoffset 0
    $ renpy.pause(0.5, hard='True')

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    hide myers_tunnel_4
    scene myers_tunnel_4

    $ renpy.block_rollback()
    $ _rollback = False

    call screen myers_tunnel4 with Dissolve(0.1)

label myers_tunnel_3_investigate_mascot:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show myers_tunnel_3_mascot_flickering at Position(xpos = 0, ypos = 0)

    show myers_tunnel_3_mascot_flickering:
        ease 0.5 zoom 2.5 xoffset 800 yoffset 150

    $ renpy.pause(0.5, hard='True')

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    scene myers_tunnel_mascot_closeup
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    if not myers_tunnel_see_mascot:

        $ myers_tunnel_see_mascot = True

        pause 1.0

        van "Is this... {w=0.5}some kind of toy?"

        $ rollback_ = True

        van "I don't quite understand, {w=0.5}but it looks like an arm... {w=0.5}with arms."

        van "But more importantly, {w=0.5}I'm pretty sure this thing wasn't here before."

        van "That strange noise from earlier could have been the sound of it falling."

        van "Who is following me here? {w=0.5}And what do they want?"

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)
    $ renpy.block_rollback()
    $ _rollback = False

    call screen myers_tunnel_mascot_screen

label myers_tunnel_3_finish_investigate_mascot:

    scene myers_tunnel_3_mascot_flickering
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    call screen myers_tunnel3 with Dissolve(0.1)

label myers_tunnel_mascot_close_up_investigate:

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/selectsounds.ogg"

    window show

    van "Investigate the toy?"

    window hide

    menu:
        "Yes":
            $ _skipping = True
            $ renpy.block_rollback()
            $ _rollback = True

            $ renpy.pause(0.5, hard='True')

            van "A blood-stained... {w=0.5}arm with arms."

            $ rollback_ = True

            van "It looks like some sort of toy."

            van "The blood on the toy is not completely dried, {w=0.5}which makes me wonder if it is from the same person as the blood on the floor."

            van "Maybe I should pick it up and take a closer look."



            show myers_tunnel_mascot_closeup_blurred:
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

            van "......?"

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

            jump john_past_start
        "No":


            call screen myers_tunnel_mascot_screen

label myers_tunnel_4_investigate_door:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show myers_tunnel_4 at Position(xpos = 0, ypos = 0)

    show myers_tunnel_4:
        ease 0.5 zoom 1.5 xoffset 0 yoffset 250

    $ renpy.pause(0.5, hard='True')

    if not myers_tunnel_travel_john_past:

        $ _skipping = True
        $ renpy.block_rollback()
        $ _rollback = True

        van "A coded door. {w=0.5}I need to enter a four-digit code."

        $ rollback_ = True

        van "I don't know what the code is yet. {w=0.5}Using brute force would just be a waste of time."

        show myers_tunnel_4:
            ease 0.5 zoom 1.0 xoffset 0 yoffset 0
        $ renpy.pause(0.5, hard='True')

        if renpy.is_skipping():
            $ renpy.choice_for_skipping()
        $ _skipping = False
        $ rollback_ = False
        $ renpy.music.stop(channel="beep", fadeout = 0.5)

        hide myers_tunnel_4
        scene myers_tunnel_4

        call screen myers_tunnel4 with Dissolve(0.1)
    else:


        if not myers_tunnel_check_door:
            $ myers_tunnel_check_door = True

            $ renpy.music.set_volume(0.8, delay=0, channel='sound')
            play sound "music/UI Dark.ogg"

            noname "Warning: {w=0.5}The door will unlock automatically after entering the correct answer."

        show transparent dark-small:
            alpha 0.5
        with Dissolve(0.2)

        call screen myers_tunnel_passcode_door

label myers_tunnel_mascot_teleport:

    scene john_past_desktop
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

    $ renpy.music.set_volume(0.5, delay=0, channel='music')
    play music ("music/bgm/jazz-lounge.ogg")

    $ renpy.music.set_volume(0.5, delay=0, channel='background noise')
    $ renpy.music.play("music/John Past/office background.ogg", channel="background noise", loop=True)

    call screen john_past_tabletop
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
