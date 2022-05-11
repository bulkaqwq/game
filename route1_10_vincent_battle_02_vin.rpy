
image vb2_1_blurred = im.Blur("images/vin battle 2/vin_bat_2_1_1.png", 4.0)

image vb2_giant_face_0 = "images/vin battle 2 vin/giant face/0.png"
image vb2_giant_face_1 = "images/vin battle 2 vin/giant face/1.png"
image vb2_giant_face_3 = "images/vin battle 2 vin/giant face/3.png"
image vb2_giant_face_4 = "images/vin battle 2 vin/giant face/4.png"

image vb2_vin_giant_face:
    contains:
        "images/vin battle 2 vin/giant face/4.png"
    contains:
        "vb2_vin_giant_face_eye"
    contains:
        "vb2_vin_giant_face_tear"

image vb2_vin_giant_face_tear:
    "images/vin battle 2 vin/giant face/vb2_tear_anim/1.png"
    0.15
    "images/vin battle 2 vin/giant face/vb2_tear_anim/2.png"
    0.15
    "images/vin battle 2 vin/giant face/vb2_tear_anim/3.png"
    0.15
    "images/vin battle 2 vin/giant face/vb2_tear_anim/4.png"
    0.15
    repeat

image vb1_vin_2_anim:
    "images/vin battle 2 vin/vin 2/1.png" with Dissolve(0.05)
    0.15
    "images/vin battle 2 vin/vin 2/2.png" with Dissolve(0.05)
    0.15
    "images/vin battle 2 vin/vin 2/3.png" with Dissolve(0.05)
    0.15
    "images/vin battle 2 vin/vin 2/4.png" with Dissolve(0.05)
    0.15
    "images/vin battle 2 vin/vin 2/5.png" with Dissolve(0.05)
    0.15
    "images/vin battle 2 vin/vin 2/4.png" with Dissolve(0.05)
    0.15
    "images/vin battle 2 vin/vin 2/3.png" with Dissolve(0.05)
    0.15
    "images/vin battle 2 vin/vin 2/2.png" with Dissolve(0.05)
    0.15
    repeat

image vb2_corridor:
    contains:
        "images/vin battle 2 vin/vb2 corridor/0.png"
    contains:
        "vb2_corridor_anim"

image vb2_corridor_anim:
    "images/vin battle 2 vin/vb2 corridor/1.png"
    0.1
    "images/vin battle 2 vin/vb2 corridor/2.png"
    0.1
    "images/vin battle 2 vin/vb2 corridor/3.png"
    0.1
    "images/vin battle 2 vin/vb2 corridor/4.png"
    0.1
    "images/vin battle 2 vin/vb2 corridor/5.png"
    0.1
    "images/vin battle 2 vin/vb2 corridor/6.png"
    0.1
    repeat

image vb2_vin_giant_face_eye_0:
    "images/vin battle 2 vin/giant face/2.png"
    block:
        alpha 0.8
        0.07
        alpha 1
        0.07
        repeat

image vb2_vin_giant_face_eye:
    "images/vin battle 2 vin/giant face/5.png"
    block:
        alpha 0.8
        0.07
        alpha 1
        0.07
        repeat

label vin_bat_2_vin_start:

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    stop music fadeout 4.0

    $ renpy.pause(0.5, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/engineering room/door accept beep.ogg"

    show vin_bat_1_3_4
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(1.0, hard='True')

    scene black
    show vin_bat_2_1
    $ renpy.transition(Dissolve(0.2))
    $ renpy.pause(1.0, hard='True')

    $ renpy.music.set_volume(0.3, delay=0, channel='electricity')
    $ renpy.music.play(["<silence 1.0>", "music/electricity.ogg"], channel="electricity", loop=False)

    show black as black_2:
        alpha 0
        pause 1.0
        alpha 0.3
        pause 0.3
        alpha 0.15
        pause 0.2
        alpha 0.6
        pause 0.5
        alpha 0.3
        pause 0.5
        alpha 0.3
        pause 0.5
        alpha 0.5
        pause 0.1
        alpha 0.8
        pause 0.3
        alpha 0.0
        pause 0.05
        alpha 0.5
        pause 0.4
        alpha 0.3
        pause 0.3
        alpha 0.15
        pause 0.2
        alpha 0.7
        pause 0.6
        alpha 0.3
        pause 0.5
        alpha 0.7
        pause 0.05
        alpha 1

    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/banging.ogg"

    $ renpy.pause(3.0, hard='True')

    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/banging.ogg"

    $ renpy.music.stop(channel="electricity", fadeout = 3.0)

    $ renpy.pause(3.0, hard='True')

    show black as black_2:
        alpha 1
    show vin_bat_2_1_1 behind black_2:
    hide vin_bat_2_1

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/legal department/explosion 2.ogg" fadeout 3.0

    $ renpy.pause(0.5, hard=True)

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music ["music/ambience/mic horror ambience 4.ogg","<silence 1.0>"]

    $ renpy.pause(2.0, hard=True)

    show black as black_2:
        alpha 1
        pause 1.0
        alpha 0.8
        pause 0.3
        alpha 0.4
        pause 0.2
        alpha 0.5
        pause 0.3
        alpha 0.3
        pause 0.5
        alpha 0.7
        pause 0.05
        alpha 1
        pause 0.4
        alpha 0.6
        pause 0.5
        alpha 0.7
        pause 0.1
        repeat

    show vb1_vin_giant_face_0 behind black_2:
        yoffset -100 xoffset 1600
        linear 4.0 xoffset 0
    show vb1_vin_giant_face_eye behind black_2:
        yoffset -100 xoffset 1600
        linear 4.0 xoffset 0
    show vb1_vin_giant_face_tear behind black_2:
        yoffset -100 xoffset 1600
        linear 4.0 xoffset 0

    $ _rollback = True
    $ _skipping = True

    $ renpy.pause(5.0, hard=True)

    show textbox4:
        xanchor 0.5 yanchor 0.5 ypos 540 xpos 260 zoom 1.0 xzoom 1.05 yzoom 0.01 alpha 0
        linear 0.2 alpha 1.0 yzoom 1.0
    $ renpy.pause(0.1, hard=True)

    cyb_vin_vertical_1 "{cps=*0.5}\"The unbearable torture of my body being crushed...\"{/cps}"

    cyb_vin_vertical_1 "{cps=*0.5}\"The agonizing pain of my blood being drained...\"{/cps}"

    show textbox4:
        linear 0.3 alpha 0

    $ rollback_ = True

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/basement/zs_crack1.ogg"

    show black as black_3 behind textbox4:
        alpha 1
        0.5
        alpha 0

    hide black_2
    show black as black_2 behind textbox4:
        alpha 1
        pause 1.0
        alpha 0.8
        pause 0.3
        alpha 0.4
        pause 0.2
        alpha 0.5
        pause 0.3
        alpha 0.3
        pause 0.5
        alpha 0.7
        pause 0.05
        alpha 1
        pause 0.4
        alpha 0.6
        pause 0.5
        alpha 0.7
        pause 0.1
        repeat
    show vb2_giant_face_0 behind vb1_vin_giant_face_tear:
        yoffset -100 xoffset 0
    show vb2_vin_giant_face_eye_0 behind vb1_vin_giant_face_tear:
        yoffset -100 xoffset 0
    hide vb1_vin_giant_face_eye
    hide vb1_vin_giant_face_eye
    hide vb1_vin_giant_face_0

    $ renpy.pause(2.0, hard=True)

    show textbox4:
        xanchor 0.5 yanchor 0.5 ypos 140 xpos 1020 xzoom 1.1 yzoom 0.01 alpha 0
        linear 0.2 alpha 1.0 yzoom 1.0
    $ renpy.pause(0.1, hard=True)

    cyb_vin_vertical_2 "{cps=*0.5}\"I remember everything, {w=0.5}Vanora. {w=0.5}I remember it all.\"{/cps}"

    show textbox4:
        linear 0.3 alpha 0

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/basement/zs_crack1.ogg"

    show black as black_3 behind textbox4:
        alpha 1
        0.5
        alpha 0
    hide black_2
    show black as black_2 behind textbox4:
        alpha 1
        pause 1.0
        alpha 0.8
        pause 0.3
        alpha 0.4
        pause 0.2
        alpha 0.5
        pause 0.3
        alpha 0.3
        pause 0.5
        alpha 0.7
        pause 0.05
        alpha 1
        pause 0.4
        alpha 0.6
        pause 0.5
        alpha 0.7
        pause 0.1
        repeat
    show vb2_giant_face_1 behind vb2_vin_giant_face_eye_0:
        yoffset -100 xoffset 0
    hide vb2_giant_face_0

    $ renpy.pause(2.0, hard=True)

    show textbox4:
        xanchor 0.5 yanchor 0.5 ypos 540 xpos 260 zoom 1.0 xzoom 1.05 yzoom 0.01 alpha 0
        linear 0.2 alpha 1.0 yzoom 1.0
    $ renpy.pause(0.1, hard=True)

    cyb_vin_vertical_1 "{cps=*0.5}\"And I... {w=0.7}will never forgive the Myers Corporation.\"{/cps}"

    stop music fadeout 3.0

    show textbox4:
        linear 0.3 alpha 0

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/basement/zs_crack1.ogg"

    hide vb2_giant_face_1
    hide vb2_vin_giant_face_eye_0
    show vb2_giant_face_3 behind vb1_vin_giant_face_tear:
        yoffset -100 xoffset 0
    show vb2_vin_giant_face_eye_0 behind vb1_vin_giant_face_tear:
        yoffset -318 xoffset 0
    show vb1_vin_giant_face_tear:
        yoffset -318
    show black as black_3 behind textbox4:
        alpha 1
        0.5
        alpha 0
    hide black_2
    show black as black_2 behind textbox4:
        alpha 1
        pause 1.0
        alpha 0.8
        pause 0.3
        alpha 0.4
        pause 0.2
        alpha 0.5
        pause 0.3
        alpha 0.3
        pause 0.5
        alpha 0.7
        pause 0.05
        alpha 1
        pause 0.4
        alpha 0.6
        pause 0.5
        alpha 0.7
        pause 0.1
        repeat
    $ renpy.pause(1.0, hard=True)

    $ renpy.pause(2.0, hard=True)

    show textbox4:
        xanchor 0.5 yanchor 0.5 ypos 540 xpos 260 zoom 1.0 xzoom 1.05 yzoom 0.01 alpha 0
        linear 0.2 alpha 1.0 yzoom 1.0
    $ renpy.pause(0.1, hard=True)

    cyb_vin_vertical_1 "{cps=*0.5}\"{color=#f00}I will slaughter them all... {w=0.7}each and every one of them.{/color}\"{/cps}"

    show textbox4:
        linear 0.3 alpha 0
    $ renpy.pause(0.3, hard=True)

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)
    $ renpy.block_rollback()
    $ _rollback = False

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/monster moan 2.ogg"

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music "music/bgm/Boss Vincent bgm 3.ogg"

    hide black_2
    hide black_3
    hide textbox4
    show white_back:
        alpha 0
        linear 0.5 alpha 1
    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 2.0, dist=15))
    $ renpy.pause(1.5, hard='True')

    hide vb2_giant_face_3
    hide vb1_vin_giant_face_tear
    hide white_back
    hide vb2_vin_giant_face_eye_0
    show vb2_1_blurred:
        alpha 0
        parallel:
            pause 1.0
            linear 0.8 alpha 0 xalign 0.5 yalign 0 zoom 1.0
            linear 0.8 alpha 0.2 xalign 0.5 yalign 0 zoom 1.2
            linear 0.8 alpha 0 xalign 0.5 yalign 0 zoom 1.0
            repeat
    show game_over_static:
        alpha 0
        block:
            ease 3.0 alpha 0
            2.0
            ease 3.0 alpha 0.2
            2.0
            repeat
    show vb1_vin_2_anim behind white_back
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(2.0, hard=True)

    $ renpy.pause(0.1, hard='True')
    pause 0.2
    $ renpy.pause(0.1, hard='True')
    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/wrong.ogg"
    show question-2-small with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')
    pause 2.0
    $ renpy.pause(0.1, hard='True')
    hide question-2-small with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')

    $ _rollback = True
    $ _skipping = True

    show screen vin_battle_chance with Dissolve(0.2)

    window show

    cyb_vin "{cps=*0.5}\"As long as I'm still alive, {w=0.5}as long as I still have my last breath...\"{/cps}"

    $ rollback_ = True

    cyb_vin "{cps=*0.5}\"I will search every corner of the G4 district... {w=0.5}track down every remaining Myers scum...\"{/cps}"

    cyb_vin "{cps=*0.5}\"Tear off every inch of their skin... {w=0.5}and grind their bodies into a fine dust...\"{/cps}"

    cyb_vin "{cps=*0.5}\"Deceit, {w=0.5}betrayal... {w=0.5}Six long years of waiting... {w=0.5}I will have my revenge.\"{/cps}"

    cyb_vin "{cps=*0.5}\"Vanora, {w=0.5}are you prepared for your judgement?\"{/cps}"

    window hide

label vb2_vin_q2:

    $ _skipping = False
    $ rollback_ = False
    $ _rollback = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    show screen countdown(timer_range=10, timer_jump='vb2_vin_death')

    menu:
        "You are no different from Myers.":

            jump vb2_vin_q2_1
        "You will still be a monster.":

            jump vb2_vin_q2_2
        "Your plan will not succeed.":

            jump vb2_vin_q2_3

label vb2_vin_q2_1:

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

    v "\"How is what you did for your revenge any different than what Myers would do for their goals?\""

    $ rollback_ = True

    v "\"Murder, {w=0.5}bribery, {w=0.5}human experimentation...\""

    v "\"You're not as noble as you think, {w=0.5}you're just like any other despicable criminal!\""

    cyb_vin "{cps=*0.5}\"Ha, {w=0.5}haha... {w=0.5}Vanora, {w=0.5}do you really think I don't realize that? {w=0.5}Do you think I care about that?\"{/cps}"

    cyb_vin "{cps=*0.5}\"Nothing will stop my revenge... {w=0.5}just like how nothing will let you escape.\"{/cps}"

    window hide

    jump vb2_vin_fail

label vb2_vin_q2_3:

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

    v "\"Wake up, {w=0.5}Vincent!{w=0.5} Don't let your imagination run wild!\""

    $ rollback_ = True

    v "\"Do you really think you can defeat the Myers Corporation? {w=0.5}You know nothing of their power.\""

    v "\"You're lucky to have even survived this long.\""

    v "\"If you continue to push yourself to the very edge of life and death, {w=0.5}it will eventually come back to bite you.\""

    v "\"Give it up! {w=0.5}You won't succeed.\""

    cyb_vin "{cps=*0.5}\"Ha, {w=0.5}haha... {w=0.5}Vanora, {w=0.5}do you really think I still care about my own life after coming this far?\"{/cps}"

    cyb_vin "{cps=*0.5}\"No matter what happens... {w=0.5}I will not abandon my revenge. {w=0.5}I will destroy Myers completely!\"{/cps}"

    window hide

label vb2_vin_fail:

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
        jump vb2_vin_death

    jump vb2_vin_q2

label vb2_vin_q2_2:

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

    v "\"Oh? {w=0.5}Murdering the entire Myers Corporation you say?\""

    $ rollback_ = True

    v "\"To be honest, {w=0.5}I don't really care. {w=0.5}Even if that's your plan, {w=0.5}I'm not going out of my way to stop you.\""

    v "\"But Vincent, {w=0.5}you need to realize, {w=0.5}there is one thing that you cannot change -\""

    v "{color=#f00}\"Whether the Myers Corporation exists or not, {w=0.5}you are and will always be a monster rejected by society with no future.\"{/color}"

    v "\"Oh, {w=0.5}I know what you're thinking.\""

    v "\"'No, {w=0.5}I still have Victor. {w=0.5}I am not alone.'\""

    v "\"But Vincent, {w=0.5}Victor is not like you. {w=0.5}He's just a human.\""

    show character_icon_box:
        xpos 130 ypos 250
    show van_icon_mischief:
        xpos 130 ypos 248
    with Dissolve(0.3)

    v "\"Sooner or later, {w=0.5}you'll lose him. {w=0.5}And then you will have nothing left in this world.\""

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

    cyb_vin "{cps=*0.5}\"What, {w=0.5}what did you say!?\"{/cps}"

    pause 1.0

    v "Vincent's expression was filled with even more sorrow. {w=0.5}A steady stream of blood flowed from his eye socket."

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)
    $ renpy.block_rollback()
    $ _rollback = False

    $ renpy.pause(0.5, hard='True')

label vb2_vin_q2_fini:

    hide screen vin_battle_chance with Dissolve(0.2)

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/scan map.ogg"

    $ renpy.pause(0.01, hard='True')
    scene black
    show vin_bat_2_3_fini:
        1.0
        ease 0.4 zoom 4.5 xoffset -850 yoffset -750
    $ renpy.transition(room_pushright)
    $ renpy.pause(1.0, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/run.ogg"

    $ renpy.free_memory()

    $ renpy.music.set_volume(1.0, delay=0, channel='background noise')
    $ renpy.music.play("music/basement/zs_vent.ogg", channel="background noise", fadein=5.0, fadeout=5.0, loop = True)

    show black as black_2:
        alpha 0
        pause 0.2
        ease 0.2 alpha 1
    $ renpy.pause(2.5, hard='True')

    show vb2_corridor:
        parallel:
            xoffset 0
            ease 1.0 xoffset -400
        parallel:
            ease 1.0 yoffset -200
            block:
                ease 1.0 yoffset -50
                ease 1.0 yoffset -100
                repeat
    show memory_frame:
        alpha 0
        0.5
        block:
            alpha 0.1
            0.08
            alpha 0.3
            0.08
            repeat

    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(2.0, hard=True)

    $ renpy.music.set_volume(1.0, delay=0, channel='sound1')
    $ renpy.music.play("music/jumpscare/jumpscare 1.ogg", channel="sound1", loop = False)

    show vb2_vin_giant_face behind memory_frame:
        xoffset 100 yoffset -600 xalign 0.5
        ease 0.1 xoffset 0 yoffset -100 zoom 1.0 xalign 0.5
        block:
            ease 1.0 yoffset -80
            ease 1.0 yoffset -120
            repeat
    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 0.8, dist=70))
    $ renpy.pause(1.0, hard='True')

    show screen vin_battle_chance with Dissolve(0.2)

    jump vb2_vin_click_mini_start

label vb2_vin_death:

    $ renpy.music.stop(channel="background noise", fadeout = 5.0)

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

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
    show vb2_vin_giant_face:
        xoffset 600 yoffset -600 xalign 0.5
        ease 0.1 xoffset 300 yoffset -405 zoom 1.5 xalign 0.5
    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=30))
    $ renpy.pause(1.0, hard=True)

    hide vincent_basement_bg
    show black-bg
    hide vb2_vin_giant_face
    $ renpy.transition(Dissolve(0.4))
    $ renpy.pause(1.0, hard='True')

    jump death
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
