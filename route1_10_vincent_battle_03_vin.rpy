
image vb3_1_blurred = im.Blur("images/vin battle 3/vin_bat_3_1_1.png", 4.0)
image vin_bat_3_1_fini2 = "images/vin battle 3/vin_bat_3_1_fini2.png"

image vb3_vin_anim:
    contains:
        "images/vin battle 3 vin/1.png"
        3.0
        "images/vin battle 3 vin/3.png"
        0.05
        "images/vin battle 3 vin/1.png"
        2.0
        "images/vin battle 3 vin/3.png"
        0.05
        "images/vin battle 3 vin/1.png"
        0.3
        "images/vin battle 3 vin/3.png"
        0.06
        "images/vin battle 3 vin/2.png"
        0.05
        "images/vin battle 3 vin/3.png"
        0.05
        repeat
    contains:
        "vb3_vin_electric"
        3.0
        "images/empty.png"
        0.05
        "vb3_vin_electric"
        2.0
        "images/empty.png"
        0.05
        "vb3_vin_electric"
        0.3
        "images/empty.png"
        0.16
        repeat

image vb3_vin_electric:
    "images/vin battle 3 vin/4.png" with Dissolve(0.05)
    0.15
    "images/vin battle 3 vin/5.png" with Dissolve(0.05)
    0.15
    "images/vin battle 3 vin/6.png" with Dissolve(0.05)
    0.15
    "images/vin battle 3 vin/7.png" with Dissolve(0.05)
    0.15
    repeat

image vb3_vin_giant_face:
    contains:
        "images/vin battle 3 vin/giant face/0.png"
    contains:
        "vb3_vin_giant_face_tear"
    contains:
        "vb3_vin_giant_face_eye"

image vb3_vin_giant_face_tear:
    "images/vin battle 3 vin/giant face/1.png"
    0.15
    "images/vin battle 3 vin/giant face/2.png"
    0.15
    "images/vin battle 3 vin/giant face/3.png"
    0.15
    "images/vin battle 3 vin/giant face/4.png"
    0.15
    repeat

image vb3_vin_giant_face_eye:
    "images/vin battle 3 vin/giant face/5.png"
    block:
        alpha 0.8
        0.07
        alpha 1
        0.07
        repeat

label vin_bat_3_vin_start:

    stop music fadeout 5.0

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/engineering room/door accept beep.ogg"

    show vin_bat_1_3_4 with Dissolve(0.5)

    $ renpy.pause(1.5, hard='True')

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

    $ renpy.pause(2.5, hard=True)

    scene black
    show vin_bat_3_1_fini
    show vb3_1_blurred:
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
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(2.0, hard=True)

    $ renpy.music.set_volume(1.0, delay=0, channel='background noise')
    $ renpy.music.play("music/basement/zs_vent.ogg", channel="background noise", fadein=5.0, fadeout=5.0, loop = True)

    show vb3_vin_anim
    $ renpy.transition(Dissolve(3.0))
    $ renpy.pause(4.0, hard=True)

    pause 1.0

    window show

    cyb_vin "{cps=*0.5}\"Vanora...\"{/cps}"

    window hide

    pause 1.0

    window show

    v "\"*Sigh* {w=0.5}Vincent, {w=0.5}you really are quite persistent.\""

    $ rollback_ = True

    v "\"Take a look at yourself and what you've become.\""

    v "\"Are you really that obsessed with killing me?\""

    $ renpy.music.stop(channel="background noise", fadeout = 3.0)

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music ["<silence 1.5>", "music/bgm/The End.ogg"]
    queue music "music/bgm/The End.ogg"

    cyb_vin "{cps=*0.5}\"Vanora... {w=0.5}Is running away the only thing you can manage?\"{/cps}"

    v "\"Me? {w=0.5}Running away?\""

    v "\"Hmph. {w=0.5}Vincent, {w=0.5}why can't you see it?\""

    v "\"You're the one who has really been running away all this time.\""

    cyb_vin "{cps=*0.5}\"...What are you saying?\"{/cps}"

    window hide

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)
    $ renpy.block_rollback()
    $ _rollback = False

    $ renpy.pause(0.1, hard='True')
    pause 0.2
    $ renpy.pause(0.1, hard='True')
    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/wrong.ogg"
    show question-3-small with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')
    pause 2.0
    $ renpy.pause(0.1, hard='True')
    hide question-3-small with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')

    $ _rollback = True
    $ _skipping = True

    show screen vin_battle_chance with Dissolve(0.2)

    window show

    v "\"Ask yourself this, {w=0.5}Vincent. {w=0.5}Do you really think this is all Myers' fault?\""

    $ rollback_ = True

    v "\"You constantly tell yourself that Myers is the cause of all your misfortunes.\""

    v "\"But the truth is, {w=0.5}you just don't want to face a fact that is obvious to you:\""

    window hide

label vb3_vin_q3:

    $ _skipping = False
    $ rollback_ = False
    $ _rollback = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    show screen countdown(timer_range=10, timer_jump='vb3_vin_death')

    menu:
        "You can't change what has already happened.":

            jump vb3_vin_q3_1
        "You didn't matter to the Myers Corporation.":

            jump vb3_vin_q3_2
        "Your time to die is near.":

            jump vb3_vin_q3_3

label vb3_vin_q3_2:

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

    v "\"You never mattered to the Myers Corporation, {w=0.5}Vincent. {w=0.5}You were always just a pawn to them.\""

    $ rollback_ = True

    v "\"You felt stupid, {w=0.5}because it was your lifelong dream to be hired by them.\""

    cyb_vin "{cps=*0.5}\"Hahaha, {w=0.5}don't you think I already know that, {w=0.5}Vanora?\"{/cps}"

    cyb_vin "{cps=*0.5}\"But none of this matters anymore... {w=0.5}because Myers will soon get what they deserve!\"{/cps}"

    window hide

    jump vb3_vin_fail

label vb3_vin_q3_3:

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

    v "\"You're scared, {w=0.5}Vincent. {w=0.5}You know your own life is at stake.\""

    $ rollback_ = True

    v "\"Despite the futility of what you're doing, {w=0.5}your revenge gives you a false sense of hope.\""

    cyb_vin "{cps=*0.5}\"Ha, {w=0.5}haha...\"{/cps}"

    cyb_vin "{cps=*0.5}\"Vanora, {w=0.5}why can't you understand?\"{/cps}"

    cyb_vin "{cps=*0.5}\"Do you really think I, {w=0.5}Vincent Edgeworth, {w=0.5}am that afraid of death?\"{/cps}"

    window hide

label vb3_vin_fail:

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
        jump vb3_vin_death

    jump vb3_vin_q3

label vb3_vin_death:

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
    show vb3_vin_giant_face:
        yoffset 1000 xalign 0.6
        ease 0.1 yoffset -300 zoom 1.2 xalign 0.5
    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=30))
    $ renpy.pause(1.0, hard=True)

    hide vincent_basement_bg
    show black-bg
    hide vb3_vin_giant_face
    $ renpy.transition(Dissolve(0.4))
    $ renpy.pause(1.0, hard='True')

    jump death

label vb3_vin_q3_1:

    $ renpy.block_rollback()

    hide screen countdown
    hide screen vin_battle_chance
    with Dissolve(0.2)

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

    v "\"Face it, {w=0.5}Vincent. {w=0.5}You're just using your revenge to distract yourself from something you can't accept.\""

    $ rollback_ = True

    v "\"Because in your heart you don't want to admit that what happened in the past can no longer be changed.\""

    v "\"Perjury, {w=0.5}bribery... {w=0.5}You committed countless crimes as a lawyer, {w=0.5}but you did not do those because you wanted to.\""

    v "\"Yes, {w=0.5}Myers Corporation was the dream company you worked so hard to get into, {w=0.5}of course you would do anything for them.\""

    v "\"That's what you tell yourself, {w=0.5}isn't it?\""

    v "\"But the truth is, {w=0.5}you just wanted to fit in. {w=0.5}You just wanted to be accepted by Myers.\""

    v "\"Ever since your childhood, {w=0.5}you've always been a kid who was excluded by others.\""

    v "\"Despite that, {w=0.5}you never tried to hide who you really were, {w=0.5}until you entered the Myers Corporation.\""

    v "\"You started to put on a fake smile, {w=0.5}you started to imitate others, {w=0.5}just because you wanted to be accepted by them.\""

    v "\"But just when you thought everything was going so smoothly, {w=0.5}all of 'that' happened.\""

    v "\"Only then did you realize how foolish you had been.\""

    v "\"You want to go back in time. {w=0.5}You want to go back to RMU and start over again.\""

    window hide

    $ renpy.music.set_volume(0.1, delay=0, channel='sound')
    play sound "music/cloth.mp3" fadeout 2.0

    pause 1.0

    v "I pulled the picture of Vincent and Victor together at university out of my pocket."

    pause 0.5

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/monster moan 2.ogg"

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

    cyb_vin "{cps=*0.5}\"That...{w=0.5}That is...\"{/cps}"

    pause 1.0

    v "Vincent stretched out his non-existent right hand to reach for the picture."

    pause 1.0

    window show

    v "\"It's only when you're with Victor that you take your mask off and show who you really are.\""

    v "\"You always seem so impatient with him, {w=0.5}but that's the real you.\""

    v "\"Everything was ordinary then, {w=0.5}but it was the happiest time of your life. {w=0.5}You miss that time.\""

    v "\"But sadly, {w=0.5}Vincent -\""

    window hide

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/basement/zs_tear.ogg"

    pause 1.0

    v "I tore the photo into pieces."

    show character_icon_box:
        xpos 130 ypos 250
    show van_icon_mischief:
        xpos 130 ypos 248
    with Dissolve(0.3)

    v "{color=#f00}\"You can never go back in time. {w=0.5}You can't change what has already happened.\"{/color}"

    hide character_icon_box
    hide van_icon_mischief
    with Dissolve(0.3)

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/monster moan 2.ogg"

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

    cyb_vin "{size=+8}{cps=*0.5}\"No, {w=0.5}no!!!!!!!!\"{/cps}{/size}"

    stop sound
    $ renpy.pause(0.1, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/legal department/explosion 1.ogg" fadeout 3.0

    stop music fadeout 5.0

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
    show vb3_vin_anim:
        xanchor 0.5 yanchor 0.75 alpha 1
        linear 0.3 rotate 45 ypos 1.4 xpos 0.5 alpha 0
    hide vb3_1_blurred
    hide game_over_static
    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 1.5, dist=15))
    $ renpy.pause(2.5, hard=True)

    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()

    $ renpy.pause(0.1, hard='True')
    pause 0.2
    $ renpy.pause(0.1, hard='True')
    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/safe.ogg"
    show safe-banner onlayer ab_parallax with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')
    pause 2.0
    $ renpy.pause(0.1, hard='True')
    hide safe-banner onlayer ab_parallax with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')

    $ _rollback = True
    $ _skipping = True

    pause 2.0

    v "Vincent wanted to charge at me, {w=0.5}but as he tried to do so, {w=0.5}his crumbling body made him collapse to the ground."

    pause 1.5

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ["<silence 1.0>", "music/myers lobby/draco footstep.ogg"]

    $ renpy.pause(0.01, hard=True)
    scene black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard=True)

    pause 3.0
    $ renpy.pause(2.0, hard=True)

    stop sound fadeout 2.0

    v "\"Well, {w=0.5}Vincent -\""

    pause 0.5

    v "I walked up to Vincent, {w=0.5}who was lying on the ground and unable to move."

    $ renpy.pause(0.5, hard=True)

    show character_icon_box:
        xpos 130 ypos 250
    show van_icon_close_eye:
        xpos 130 ypos 248
    $ renpy.transition(Dissolve(0.3))
    $ renpy.pause(0.3, hard=True)

    v "\"Since your wish is simply unattainable,\""

    v "\"Could you do me a favor then?\""

    hide character_icon_box
    hide van_icon_close_eye
    with Dissolve(0.3)

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/basement/zs_kick.ogg"

    show blood-2:
        alpha 1
        0.3
        linear 0.3 alpha 0
    show red-bg:
        alpha 0
        linear 0.3 alpha 1
        linear 0.5 alpha 0
    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 1.5, dist=15))

    pause 3.0

    v "I lifted my right foot and stomped it into Vincent's face."

    pause 0.5

    show character_icon_box:
        xpos 130 ypos 250
    show van_icon_close_eye:
        xpos 130 ypos 248
    with Dissolve(0.3)

    v "\"Please give up your futile efforts and disappear from this world.\""

    hide character_icon_box
    hide van_icon_close_eye
    with Dissolve(0.3)

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/basement/zs_kick.ogg"

    show blood-2:
        alpha 1
        0.3
        linear 0.3 alpha 0
    show red-bg:
        alpha 0
        linear 0.3 alpha 1
        linear 0.5 alpha 0
    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 1.5, dist=15))

    pause 3.0

    v "I lifted my blood-stained foot, {w=0.5}and stomped his face again."

    pause 0.5

    show character_icon_box:
        xpos 130 ypos 250
    show van_icon_close_eye:
        xpos 130 ypos 248
    with Dissolve(0.3)

    v "\"You've already caused so much trouble for the Myers Corporation. {w=0.5}If you could do us this one small favor, {w=0.5}we'd greatly appreciate it.\""

    hide character_icon_box
    hide van_icon_close_eye
    with Dissolve(0.3)

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/basement/zs_kick.ogg"

    show blood-2:
        alpha 1
        0.3
        linear 0.3 alpha 0
    show red-bg:
        alpha 0
        linear 0.3 alpha 1
        linear 0.5 alpha 0
    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 1.5, dist=15))

    pause 3.0

    v "Again, {w=0.5}and again. {w=0.5}And again."

    v "I felt the same emotions welling up inside me as when I sliced open the cyborg's chest."

    v "It felt... {w=0.5}{color=#f00}exhilarating{/color}."

    pause 0.5

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music "music/ambience/mic horror ambience 3.ogg"

    $ renpy.pause(0.01, hard=True)
    scene vin_bat_3_1_fini2
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard=True)

    pause 0.5

    v "Before I realized it, {w=0.5}the part above Vincent's neck was completely flattened."

    v "\"...Finally.\""

    v "\"Now all there's left to do is to finish my mission.\""

    scene vin_bat_3_3_fini
    show basement_shadow_vanora:
        xoffset 200 alpha 1
        2.0
        linear 1.0 alpha 0
    show game_over_static:
        alpha 0.3
        2.0
        linear 1.0 alpha 0
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(3.5, hard=True)

    v "I started to walk towards the exit."

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/myers lobby/draco footstep.ogg"

    show black behind vin_bat_3_3_fini
    show vin_bat_3_3_fini:
        alpha 1
        ease 0.6 zoom 4.5 xoffset 1500 yoffset 1850 alpha 0

    $ renpy.pause(2.0, hard=True)

    jump route1_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
