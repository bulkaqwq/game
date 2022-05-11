image vb1_3_blurred = im.Blur("images/vin battle 1/vin_bat_1_1_1.png", 4.0)
image vb1_vin_0_idle = "images/vin battle 1 vin/vin 0/1.png"
image vb1_vin_0_anim1:
    "images/vin battle 1 vin/vin 0/1.png"
    1.0
    "images/vin battle 1 vin/vin 0/2.png"
    0.01
    "images/vin battle 1 vin/vin 0/1.png"
    2.0
    "images/vin battle 1 vin/vin 0/2.png"
    0.01
    "images/vin battle 1 vin/vin 0/1.png"
    0.02
    "images/vin battle 1 vin/vin 0/2.png"
    0.01
    repeat
image vb1_vin_0_anim2:
    "images/vin battle 1 vin/vin 0/1.png"
    0.8
    "images/vin battle 1 vin/vin 0/2.png"
    0.01
    "images/vin battle 1 vin/vin 0/1.png"
    1.0
    "images/vin battle 1 vin/vin 0/2.png"
    0.01
    "images/vin battle 1 vin/vin 0/1.png"
    0.02
    "images/vin battle 1 vin/vin 0/2.png"
    0.01
    "images/vin battle 1 vin/vin 0/1.png"
    0.1
    "images/vin battle 1 vin/vin 0/2.png"
    0.01
    "images/vin battle 1 vin/vin 0/1.png"
    0.1
    "images/vin battle 1 vin/vin 0/2.png"
    0.01
    repeat
image vb1_vin_1_idle = "images/vin battle 1 vin/vin 1/0.png"
image vb1_vin_1_anim:
    "images/vin battle 1 vin/vin 1/4.png" with Dissolve(0.05)
    0.15
    "images/vin battle 1 vin/vin 1/5.png" with Dissolve(0.05)
    0.15
    "images/vin battle 1 vin/vin 1/4.png" with Dissolve(0.05)
    0.15
    "images/vin battle 1 vin/vin 1/3.png" with Dissolve(0.05)
    0.15
    "images/vin battle 1 vin/vin 1/2.png" with Dissolve(0.05)
    0.15
    "images/vin battle 1 vin/vin 1/1.png" with Dissolve(0.05)
    0.15
    "images/vin battle 1 vin/vin 1/2.png" with Dissolve(0.05)
    0.15
    "images/vin battle 1 vin/vin 1/3.png" with Dissolve(0.05)
    0.15
    repeat


image vb1_vin_giant_face:
    contains:
        "images/vin battle 1 vin/giant face/0.png"
    contains:
        "vb1_vin_giant_face_tear"
    contains:
        "vb1_vin_giant_face_eye"

image vb1_vin_giant_face_tear:
    "images/vin battle 1 vin/giant face/vb1_tear_anim/1.png"
    0.15
    "images/vin battle 1 vin/giant face/vb1_tear_anim/2.png"
    0.15
    "images/vin battle 1 vin/giant face/vb1_tear_anim/3.png"
    0.15
    "images/vin battle 1 vin/giant face/vb1_tear_anim/4.png"
    0.15
    repeat

image vb1_vin_giant_face_eye:
    "images/vin battle 1 vin/giant face/1.png"
    block:
        alpha 0.8
        0.07
        alpha 1
        0.07
        repeat

image vb1_vin_giant_face_0 = "images/vin battle 1 vin/giant face/0.png"

image vb1_vin_corridor = "images/vin battle 1 vin/vb1_vin_corridor.png"

screen vin_battle_chance:

    text _("{font=VHS.ttf}{color=#ffffff}CHANCES:[vin_battle_chance_num]{/color}{/font}") xpos 0.985 ypos 0.02 xanchor 1.0 outlines [(2, "#000000", 0, 0,)]

label vin_bat_1_vin_start:

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    stop music fadeout 4.0

    $ renpy.pause(0.5, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/engineering room/door accept beep.ogg"

    show vin_bat_1_3_4 with Dissolve(0.5)

    $ renpy.pause(0.5, hard='True')

    show character_icon_box_1:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 800 ypos 50
        xpos 800 ypos 50
    show draco_icon_blood_serious:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 800 ypos 48
        xpos 800 ypos 48
    show character_icon_box_2:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 800 ypos 50
        xpos 800 ypos 50
    with Dissolve(0.5)

    window show

    dra "\"Good work, {w=0.5}Vanora! {w=0.5}Now all there's left to do...\""

    window hide

    $ renpy.pause(0.01, hard=True)

    scene black
    show vin_bat_1_1_2
    show vin_bat_1_1_1
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard=True)

    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/banging.ogg"

    $ renpy.pause(3.0, hard='True')

    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/banging.ogg"

    $ renpy.pause(3.0, hard='True')

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/legal department/explosion 2.ogg" fadeout 3.0

    $ renpy.pause(0.1, hard=True)

    show white back:
        zoom 1.25 xalign 0.5 yalign 0.5
        alpha 1.0
        ease 0.2 alpha 0.4
        alpha 1.0
        ease 0.2 alpha 0.4
        alpha 1.0
        ease 0.2 alpha 0.4
        ease 0.5 alpha 0

    show lobby_dust:
        pause 1.0
        ease 0.5 alpha 0
    hide vin_bat_1_1_2
    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 1.5, dist=15))

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music "music/ambience/mic horror ambience 3.ogg"

    $ renpy.pause(3.0, hard='True')

    show vb1_3_blurred:
        alpha 0
        parallel:
            pause 1.0
            linear 0.8 alpha 0 xalign 0.5 yalign 0 zoom 1.0
            linear 0.8 alpha 0.2 xalign 0.5 yalign 0 zoom 1.2
            linear 0.8 alpha 0 xalign 0.5 yalign 0 zoom 1.0
            repeat

    show vb1_vin_0_idle
    $ renpy.transition(Dissolve(3.0))
    $ renpy.pause(4.0, hard=True)

    pause 1.0

    hide white back

    window show

    vin "{cps=*0.5}\"Vanora...\"{/cps}"

    $ rollback_ = True

    vin "{cps=*0.5}\"Did you really think that...{w=1.0} you could get away?\"{/cps}"

    show vb1_vin_0_anim1
    hide vb1_vin_0_idle

    vin "{cps=*0.5}\"Ha...{w=1.0} Haha...\"{/cps}"

    vin "{cps=*0.5}\"Hahahaha...\"{/cps}"

    show vb1_vin_0_anim2
    hide vb1_vin_0_anim1

    vin "{cps=*0.5}\"Hahahahaha...\"{/cps}"

    window hide

    $ renpy.pause(0.5, hard='True')

    show vb1_vin_0_anim2:
        xalign 0.5
        linear 0.5 zoom 1.2 yoffset 120
        pause 1.0
        linear 0.5 zoom 1.4 yoffset 240
        pause 1.0
        linear 0.5 zoom 1.6 yoffset 360

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/squish.ogg"
    $ renpy.pause(1.5, hard='True')
    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/squish.ogg"
    $ renpy.pause(1.5, hard='True')
    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/squish.ogg"
    $ renpy.pause(1.5, hard='True')

    stop music fadeout 3.0

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/monster moan 2.ogg"

    show white_back:
        alpha 0
        linear 0.5 alpha 1
    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 2.0, dist=15))

    $ renpy.pause(1.5, hard='True')
    hide vb1_vin_0_anim2
    show game_over_static behind white_back:
        alpha 0.2
    show vb1_vin_1_idle behind white_back:
        zoom 1.6 yoffset -70 xalign 0.5
    $ renpy.pause(0.01, hard='True')
    hide white_back
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard=True)

    pause 2.0

    window show

    cyb_vin "{cps=*0.5}\"Judgment Day for the Myers Corporation...{w=1.0} has fallen upon us.\"{/cps}"

    window hide

    $ vin_battle_chance_num = 2

    show screen vin_battle_chance
    with Dissolve(0.2)

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music "music/bgm/Boss Vincent bgm 2.ogg"

    show game_over_static:
        ease 3.0 alpha 0
        2.0
        ease 3.0 alpha 0.2
        2.0
        repeat

    show vb1_vin_1_anim:
        zoom 1.6 yoffset -70 xalign 0.5
        ease 1.0 zoom 1.0 xoffset 0 yoffset 0
    hide vb1_vin_1_idle
    $ renpy.pause(0.5, hard='True')

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ renpy.block_rollback()

    $ renpy.pause(0.1, hard='True')
    pause 2.0
    $ renpy.pause(0.1, hard='True')
    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/wrong.ogg"
    show live-die-small with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')
    pause 2.0
    $ renpy.pause(0.1, hard='True')
    hide live-die-small with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/email sent.ogg"

    show transparent dark-small
    show myers_lobby_draco_battle_explanation_1:
        yoffset 100
        linear 0.5 yoffset 50
    show myers_lobby_draco_battle_explanation_2:
        yoffset -100
        linear 0.5 yoffset -50
    show myers_lobby_draco_battle_explanation_wheel:
        parallel:
            rotate 0
            linear 8.0 rotate 360
            repeat
        parallel:
            xpos -425 ypos 0
    show myers_lobby_draco_battle_explanation_wheel_2:
        parallel:
            rotate 0
            linear 8.0 rotate -360
            repeat
        parallel:
            xpos 975 ypos 0
    with Dissolve(0.5)

    $ rollback = True

    noname_warning_3 "(Warning: {w=0.5}From here on, {w=0.5}you will need to answer a series of questions, {w=0.5}play mini games, {w=0.5}and solve puzzles to escape from Vincent.)"

    $ rollback_ = True

    noname_warning_3 "(You will only be able to make {color=#f00}two{/color} mistakes.)"

    noname_warning_3 "(Making more than two mistakes or exceeding the time limit will immediately lead to {color=#f00}death{/color}.)"

    noname_warning_3 "(Saving would be a great idea now.)"

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)
    $ renpy.block_rollback()
    $ _rollback = False

    hide transparent dark-small
    hide myers_lobby_draco_battle_explanation_1
    hide myers_lobby_draco_battle_explanation_2
    show myers_lobby_draco_battle_explanation_1:
        yoffset 50
        linear 0.5 yoffset 100 alpha 0
    show myers_lobby_draco_battle_explanation_2:
        yoffset -50
        linear 0.5 yoffset -100 alpha 0
    hide myers_lobby_draco_battle_explanation_wheel
    hide myers_lobby_draco_battle_explanation_wheel_2
    with Dissolve(0.5)
    hide myers_lobby_draco_battle_explanation_1
    hide myers_lobby_draco_battle_explanation_2

    $ renpy.pause(0.1, hard='True')
    pause 0.2
    $ renpy.pause(0.1, hard='True')
    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/wrong.ogg"
    show question-1-small with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')
    pause 2.0
    $ renpy.pause(0.1, hard='True')
    hide question-1-small with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')

    $ _rollback = True
    $ _skipping = True

    window show

    cyb_vin "{cps=*0.5}\"Vanora...{w=0.5} Here you are, {w=0.5}standing face to face with me at this moment...\"{/cps}"

    $ rollback_ = True

    cyb_vin "{cps=*0.5}\"Do you think...{w=0.5} it is fate for us to be here? {w=0.5}Do you believe in fate?\"{/cps}"

    window hide

label vb1_vin_q1:

    $ _skipping = False
    $ rollback_ = False
    $ _rollback = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    show screen countdown(timer_range=10, timer_jump='vb1_vin_death')

    menu:
        "There's nothing you can change.":

            jump vb1_vin_q1_1
        "It doesn't need to stay this way.":

            jump vb1_vin_q1_2
        "Your fate and actions are intertwined.":

            jump vb1_vin_q1_3

label vb1_vin_q1_1:

    $ vin_battle_chance_num -= 1

    if vin_battle_chance_num == 0:
        hide screen vin_battle_chance

    $ renpy.block_rollback()

    hide screen countdown

    $ renpy.block_rollback()

    $ renpy.pause(0.1, hard='True')
    pause 0.2
    $ renpy.pause(0.1, hard='True')
    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/wrong.ogg"
    show wrong-small with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')
    pause 2.0
    $ renpy.pause(0.1, hard='True')
    hide wrong-small with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')

    $ _rollback = True
    $ _skipping = True

    window show

    v "\"Endless suffering after another, {w=0.5}and bloodshed that could never possibly be forgotten... {w=0.5}Vincent, {w=0.5}I know what you have endured in the past.\""

    $ rollback_ = True

    v "\"But trust me, {w=0.5}I know it's not your fault. {w=0.5}There was nothing you could do.\""

    cyb_vin "{cps=*0.5}\"Ha, {w=0.5}haha... {w=0.5}You're right...\"{/cps}"

    cyb_vin "{cps=*0.5}\"It's not my fault... {w=0.5}{color=#f00}It's Myers'{/color}.\"{/cps}"

    cyb_vin "{cps=*0.5}\"And your unchangeable fate... {w=0.5}is to perish here!\"{/cps}"

    window hide

    jump vb1_vin_fail

label vb1_vin_q1_2:

    $ vin_battle_chance_num -= 1

    if vin_battle_chance_num == 0:
        hide screen vin_battle_chance

    $ renpy.block_rollback()

    hide screen countdown

    $ renpy.block_rollback()

    $ renpy.pause(0.1, hard='True')
    pause 0.2
    $ renpy.pause(0.1, hard='True')
    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/wrong.ogg"
    show wrong-small with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')
    pause 2.0
    $ renpy.pause(0.1, hard='True')
    hide wrong-small with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')

    $ _rollback = True
    $ _skipping = True

    window show

    v "\"There is no such thing as fate! {w=0.5}Everything we are facing now is the result of our free will.\""

    $ rollback_ = True

    v "\"It was my own choice to come to the Myers Corporation!\""

    v "\"And it was also my own choice to search for my vanished past!\""

    cyb_vin "{cps=*0.5}\"Ha, {w=0.5}haha...\"{/cps}"

    cyb_vin "{cps=*0.5}\"Then killing you here...{w=0.5} will be my choice!\"{/cps}"

    window hide

label vb1_vin_fail:

    $ renpy.music.set_volume(0.7, delay=0, channel='sound')
    play sound "music/stab.ogg"

    show blood-2:
        alpha 1
        0.3
        linear 0.3 alpha 0
    show red-bg:
        alpha 0
        linear 0.3 alpha 1
        linear 0.5 alpha 0
    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 1.5, dist=15))

    $ renpy.pause(1.0, hard='True')

    v "\"Umph, {w=0.5}agh!\""

    if vin_battle_chance_num == 0:
        jump vb1_vin_death

    jump vb1_vin_q1

label vb1_vin_q1_3:

    $ renpy.block_rollback()

    hide screen countdown

    $ renpy.pause(0.1, hard='True')
    pause 0.2
    $ renpy.pause(0.1, hard='True')
    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/correct.ogg"
    show correct-small with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')
    pause 2.0
    $ renpy.pause(0.1, hard='True')
    hide correct-small with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')

    $ _rollback = True
    $ _skipping = True

    window show

    v "\"Nothing in this world is purely a coincidence or the outcome of what we do.\""

    $ rollback_ = True

    v "\"This moment as I stand here confronting you... {w=0.5}is a result of our intertwining fates and actions.\""

    v "\"Vincent, {w=0.5}I saw your past.\""

    v "\"I know you spent all your youth chasing your dream. {w=0.5}Getting into the Myers Corporation was your dream come true.\""

    v "\"It was not fate that got you into the Myers Corporation. {w=0.5}It was because you worked hard for it.\""

    v "\"However, {w=0.5}there are also things that you just can't change.\""

    show character_icon_box:
        xpos 130 ypos 250
    show van_icon_mischief:
        xpos 130 ypos 248
    with Dissolve(0.3)

    v "\"After all, {w=0.5}{color=#f00}it was your fate to become an outcast and be forced to leave the Myers Corporation because you didn't belong there{/color}.\""

    window hide

    hide character_icon_box
    hide van_icon_mischief
    with Dissolve(0.3)

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/shock2.ogg" fadeout 2.0

    show white_back:
        alpha 0
        linear 0.2 alpha 0.3
        linear 0.2 alpha 0
        linear 0.1 alpha 0.1
        linear 0.1 alpha 0
        linear 0.1 alpha 0.1
        linear 0.3 alpha 0

    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15))
    $ renpy.pause(2.5, hard='True')

    $ renpy.music.set_volume(0.6, delay=0, channel='sound1')
    $ renpy.music.play("music/monster moan 2.ogg", channel="sound1", loop = False)

    cyb_vin "{cps=*0.5}\"How, {w=0.5}how did you...!?\"{/cps}"

    pause 1.0

    v "A look of shock appeared on Vincent's face, {w=0.5}but then it changed to one of excruciating pain."

    v "I ran to the exit of the room."

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)
    $ renpy.block_rollback()
    $ _rollback = False

    $ renpy.pause(0.5, hard='True')

label vb1_vin_q1_fini:

    hide screen vin_battle_chance with Dissolve(0.2)

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/scan map.ogg"

    $ renpy.pause(0.01, hard='True')
    scene black
    show vin_bat_1_3_fini:
        1.0

        ease 0.4 zoom 4.5 xoffset -850 yoffset -750
    $ renpy.transition(room_pushright)
    $ renpy.pause(1.0, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/run.ogg"

    show black as black_2:
        alpha 0
        pause 0.2
        ease 0.2 alpha 1
    $ renpy.pause(2.5, hard='True')

    $ renpy.free_memory()

    cyb_vin "{cps=*0.5}\"Vanora!!!!!!!!\"{/cps}"

    show vb1_vin_corridor:
        xpos -1800
        ease 0.7 xpos 0
    $ renpy.transition(Dissolve(0.3))
    $ renpy.pause(0.6, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound1')
    $ renpy.music.play(["<silence 0.5>", "music/jumpscare/jumpscare 1.ogg"], channel="sound1", loop = False)

    show vb1_vin_1_idle:
        alpha 0
        0.5
        zoom 1.0 xoffset -1300 yoffset 100 alpha 1
        ease 0.3 zoom 2.4 xoffset -1000 yoffset -30 alpha 0
    show vb1_vin_giant_face:
        alpha 0
        0.5
        zoom 0.7 xoffset -1300 yoffset -160 alpha 0
        ease 0.3 zoom 1.0 xoffset -200 yoffset -100 alpha 1
    show memory_frame:
        alpha 0
        0.5
        block:
            alpha 0
            0.08
            alpha 0.3
            0.08
            repeat
    $ renpy.pause(0.5, hard='True')
    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 0.8, dist=70))
    $ renpy.pause(1.0, hard='True')

    show screen vin_battle_chance with Dissolve(0.2)

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/email sent.ogg"

    show transparent dark-small
    show myers_lobby_draco_battle_explanation_1:
        yoffset 100
        linear 0.5 yoffset 50
    show myers_lobby_draco_battle_explanation_2:
        yoffset -100
        linear 0.5 yoffset -50
    show myers_lobby_draco_battle_explanation_wheel:
        parallel:
            rotate 0
            linear 8.0 rotate 360
            repeat
        parallel:
            xpos -425 ypos 0
    show myers_lobby_draco_battle_explanation_wheel_2:
        parallel:
            rotate 0
            linear 8.0 rotate -360
            repeat
        parallel:
            xpos 975 ypos 0
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    noname_warning_3 "(Tap the {color=#f00}spacebar{/color} and hit the {color=#f00}red target{/color} to escape Vincent!)"

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)
    $ renpy.block_rollback()
    $ _rollback = False

    hide transparent dark-small
    hide myers_lobby_draco_battle_explanation_1
    hide myers_lobby_draco_battle_explanation_2
    show myers_lobby_draco_battle_explanation_1:
        yoffset 50
        linear 0.5 yoffset 100 alpha 0
    show myers_lobby_draco_battle_explanation_2:
        yoffset -50
        linear 0.5 yoffset -100 alpha 0
    hide myers_lobby_draco_battle_explanation_wheel
    hide myers_lobby_draco_battle_explanation_wheel_2
    with Dissolve(0.5)
    hide myers_lobby_draco_battle_explanation_1
    hide myers_lobby_draco_battle_explanation_2

    jump vb1_vin_click_mini_start

label vb1_vin_death:

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)
    $ rollback_ = False
    $ _rollback = False

    stop music fadeout 4.0

    hide screen vin_battle_chance
    scene grey-bg
    show black-bg
    $ renpy.transition(Dissolve(0.2))
    $ renpy.pause(8.0, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound1')
    $ renpy.music.play("music/vin jump.ogg", channel="sound1", loop = False)
    show vincent_basement_bg:
        alpha 0
        linear 0.2 alpha 0.5
        linear 0.05 xoffset -70 yoffset 70
        linear 0.05 xoffset 70 yoffset -70
        linear 0.05 xoffset 0 yoffset 70
        linear 0.05 xoffset -70 yoffset -70
        linear 0.05 xoffset 0 yoffset 0
        linear 0.05 xoffset -70 yoffset 70
        linear 0.05 xoffset 70 yoffset -70
        linear 0.05 xoffset 0 yoffset 70
        linear 0.05 xoffset -70 yoffset -70
        linear 0.05 xoffset 0 yoffset 0
    show vb1_vin_giant_face:
        yoffset 1000 xalign 0.5
        ease 0.1 yoffset -380 zoom 1.5 xalign 0.5
    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=30))
    $ renpy.pause(1.0, hard=True)

    hide vincent_basement_bg
    show black-bg
    hide vb1_vin_giant_face
    $ renpy.transition(Dissolve(0.4))
    $ renpy.pause(1.0, hard='True')

    jump death
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
