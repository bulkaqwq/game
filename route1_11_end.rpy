
image vb3_corridor = "images/vin battle 3 vin/vb3_corridor.png"
image vb3_corridor_blood = "images/vin battle 3 vin/vb3_corridor_blood.png"

label route1_end:

    $ renpy.pause(2.0, hard=True)

    stop sound fadeout 3.0

    scene vb3_corridor
    show dust:
        alpha 0
        pause 5.0
        block:
            ease 5.0 alpha 0.5
            ease 5.0 alpha 1.0
            ease 5.0 alpha 0.5
            ease 5.0 alpha 0
            pause 5.0
            repeat
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(1.0, hard='True')

    v "As expected, {w=0.5}I met that man again outside the room."

    show draco_blood_shocked with Dissolve(1.0)

    pause 1.0

    $ say_who = _("Draco")

    window show

    dra "\"Va - {w=0.5}Vanora!\""

    hide draco_blood_shocked
    show draco_blood_upset
    with Dissolve(0.2)

    dra "\"I'm so glad you're okay.\""

    hide draco_blood_upset
    show draco_blood_serious
    with Dissolve(0.2)

    dra "\"How is Vin... {w=0.5}my master doing?\""

    window hide

    $ say_who = ""

    show draco_blood_serious:
        linear 0.5 xpos 0.73

    $ renpy.pause(1.0, hard='True')

    show vanora_normal at van_pos_1
    with Dissolve(1.0)

    pause 0.5

    window show

    v "\"......\""

    show van_close_eye at van_pos_1
    hide vanora_normal
    with Dissolve(0.2)

    v "\"He's dead.\""

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/shock2.ogg" fadeout 2.0

    hide draco_blood_serious
    show draco_blood_disbelief at dra_pos_2
    with Dissolve(0.2)

    dra "\"Wh - {w=0.5}what!? {w=0.5}How!?\"" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    v "Draco couldn't believe what he was hearing. {w=0.5}His whole body began to tremble."

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound ("music/vanora/Vanora hmm.ogg")

    hide van_close_eye
    show vanora_normal at van_pos_1
    with Dissolve(0.2)

    v "\"...I killed him.\" {w=0.5}I nonchalantly added."

    window hide

    pause 1.0

    window show

    dra "\"Va... {w=0.5}Vanora...\""

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/shake.ogg"

    show draco_blood_mad at dra_pos_2
    hide draco_blood_disbelief

    dra "\"...But why? {w=0.5}Why did you do that!?\"" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    show van_close_eye at van_pos_1
    hide vanora_normal
    with Dissolve(0.5)

    v "\"What's the matter?\""

    v "\"Was Vincent that important to you?\""

    v "My voice was toneless as I questioned him."

    show draco_blood_sad2 at dra_pos_2
    hide draco_blood_mad
    with Dissolve(0.2)

    $ say_who = _("Draco")

    dra "\"Do you even need to ask that? {w=0.5}He's my master, {w=0.5}no, {w=0.5}more importantly,\""

    hide draco_blood_sad2
    show draco_blood_mad at dra_pos_2
    with Dissolve(0.2)

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/shake.ogg"

    dra "\"He's my brother!!!\"" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    $ say_who = ""

    hide van_close_eye
    show vanora_normal at van_pos_1
    with Dissolve(0.5)

    stop music fadeout 3.0

    v "\"......\""

    window hide

    pause 2.0

    $ renpy.pause(0.01, hard=True)
    scene black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard=True)

    $ renpy.music.set_volume(0.8, delay=0, channel='music')
    play music ["<silence 1.0>", "music/bgm/ankari-sad.ogg"]
    queue music "music/bgm/ankari-sad.ogg"

    pause 2.0

    v "After a few seconds of silence, {w=0.5}I walked over to Draco."

    show dorm_mono_1_lighting:
        linear 0.01 alpha 0.9
        linear 0.01 alpha 1
        repeat
    show firefly_particles
    with Dissolve(1.0)

    $ renpy.music.set_volume(0.1, delay=0, channel='sound')
    play sound "music/cloth.mp3" fadeout 2.0

    pause 3.0

    show character_icon_box_1:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 800 ypos 50
        xpos 800 ypos 50
    show draco_icon_blood_blush:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 800 ypos 48
        xpos 800 ypos 48
    show character_icon_box_2:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 800 ypos 50
        xpos 800 ypos 50

    dra "\"Va, {w=0.5}Vanora! {w=0.5}What are you...?\""

    hide character_icon_box_1
    hide draco_icon_blood_blush
    hide character_icon_box_2
    with Dissolve(0.5)

    pause 0.5

    v "I leaned on Draco, {w=0.5}wrapped my arms around his waist, {w=0.5}and hugged him tightly."

    v "I buried my head in his chest."

    pause 0.5

    show character_icon_box:
        xpos 130 ypos 250
    show van_icon_sad_close:
        xpos 130 ypos 248
    with Dissolve(0.5)

    $ say_who = _("Vanora")

    window show

    v "\"I'm sorry, {w=0.5}Draco. {w=0.5}I had no choice. {w=0.5}I didn't want to kill him either.\""

    hide van_icon_sad_close
    show van_icon_sad:
        xpos 130 ypos 248
    with Dissolve(0.2)

    v "\"But I know you will forgive me, {w=0.5}right?\""

    v " I eagerly looked up at Draco."

    hide van_icon_sad
    show van_icon_sad_close:
        xpos 130 ypos 248
    with Dissolve(0.2)

    v "\"Because to you, {w=0.5}I'm more important than Vincent, {w=0.5}isn't that right?\""

    hide character_icon_box
    hide van_icon_sad_close
    show character_icon_box_1:
        xpos 800 ypos 50
    show draco_icon_blood_upset:
        xpos 800 ypos 48
    show character_icon_box_2:
        xpos 800 ypos 50
    with Dissolve(0.5)

    $ say_who = ""

    dra "\"But, {w=0.5}but...\""

    window hide

    hide character_icon_box_1
    hide draco_icon_blood_upset
    hide character_icon_box_2
    with Dissolve(0.3)

    pause 1.0

    v "I raised my left hand and gently touched Draco's cheek with the tips of my fingers. {w=0.5}I could feel his face heating up."

    pause 1.0

    show character_icon_box:
        xpos 130 ypos 250
    show van_icon_sad:
        xpos 130 ypos 248
    with Dissolve(0.5)

    $ say_who = _("Vanora")

    window show

    v "\"Draco... {w=0.5}Let it just be you and me, {w=0.5}just the two of us. {w=0.5}We don't need Vincent.\""

    hide van_icon_sad
    show van_icon_sad_close:
        xpos 130 ypos 248
    with Dissolve(0.2)

    v "\"Let us both escape from here... {w=0.5}and live together forever.\""

    hide character_icon_box
    hide van_icon_sad_close
    show character_icon_box_1:
        xpos 800 ypos 50
    show draco_icon_blood_sad:
        xpos 800 ypos 48
    show character_icon_box_2:
        xpos 800 ypos 50
    with Dissolve(0.5)

    $ say_who = ""

    dra "\"Va, {w=0.5}Vanora...\""

    window hide

    hide character_icon_box_1
    hide draco_icon_blood_sad
    hide character_icon_box_2
    with Dissolve(0.3)

    pause 1.0

    v "After a moment of hesitation, {w=0.5}Draco slowly raised his arms and wrapped them around me."

    stop music fadeout 3.0

    $ renpy.pause(1.0, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/jumpscare/jumpscare 1.ogg"

    show dorm_mono_1_lighting:
        linear 0.3 alpha 0
    show firefly_particles:
        linear 0.3 alpha 0
    show blood-2:
        alpha 1
        0.3
        linear 0.3 alpha 0
    show red-bg:
        alpha 0
        linear 0.3 alpha 1
        linear 0.5 alpha 0
    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 1.5, dist=15))
    $ renpy.pause(2.0, hard='True')

    show character_icon_box_1:
        xpos 800 ypos 50
    show draco_icon_blood_stabbed:
        xpos 800 ypos 48
    show character_icon_box_2:
        xpos 800 ypos 50
    with Dissolve(0.2)

    hide dorm_mono_1_lighting
    hide firefly_particles

    dra "{size=+8}\"Ah, {w=0.5}ahhhhhhhhhhhhhhhh!!!\"{/size}"

    hide character_icon_box_1
    hide draco_icon_blood_stabbed
    hide character_icon_box_2
    with Dissolve(0.2)

    pause 0.5

    v "I took out the scalpel I had been hiding in my pocket and thrusted it deep into Draco's chest."

    v "Again, {w=0.5}and again. {w=0.5}And again."

    pause 0.5

    show character_icon_box:
        xpos 130 ypos 250
    show van_icon_blood_normal:
        xpos 130 ypos 248
    with Dissolve(0.5)

    v "\"Found it.\""

    hide character_icon_box
    hide van_icon_blood_normal
    with Dissolve(0.2)

    $ renpy.music.set_volume(0.7, delay=0, channel='sound')
    play sound "music/engineering room/flesh 2.ogg"

    pause 2.0

    show engineering_room_secret_lab_device with Dissolve(1.0)

    v "From Draco's shredded chest, {w=0.5}I pulled out a round, {w=0.5}spherical device."

    scene black
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(2.0, hard='True')

    scene vb3_corridor_blood
    show dust:
        alpha 0
        pause 5.0
        block:
            ease 5.0 alpha 0.5
            ease 5.0 alpha 1.0
            ease 5.0 alpha 0.5
            ease 5.0 alpha 0
            pause 5.0
            repeat
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(2.0, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music "music/what happened.ogg"

    pause 3.0

    show character_icon_box:
        xpos 130 ypos 250
    show van_icon_blood_normal:
        xpos 130 ypos 248
    with Dissolve(0.5)

    $ say_who = _("Vanora")

    window show

    v "\"Unbelievable.\""

    v "\"So Vincent's so-called {color=#f00}'secret weapon'{/color} is a cyborg made from {color=#f00}his own genes{/color} and {color=#f00}young Victor's memories{/color}.\""

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound ("music/vanora/Vanora hmm.ogg")

    hide van_icon_blood_normal
    show van_icon_blood_close:
        xpos 130 ypos 248
    with Dissolve(0.5)

    v "\"Honestly, {w=0.5}now that I think about it, {w=0.5}you and Victor are indeed alike.\""

    v "\"Whenever you become too obsessed with someone, {w=0.5}you lose all your rationality.\""

    hide van_icon_blood_close
    show van_icon_blood_normal:
        xpos 130 ypos 248
    with Dissolve(0.5)

    v "\"Forgive me, {w=0.5}Draco. {w=0.5}I do appreciate all the help you've provided.\""

    v "\"However, {w=0.5}{color=#f00}my mission{/color} - {w=0.5}is to {color=#f00}destroy you{/color}.\""

    window hide

    $ say_who = ""

    hide character_icon_box
    hide van_icon_blood_normal
    with Dissolve(0.5)

    pause 0.5

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/basement/zs_drop.ogg"
    with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    v "I tossed Draco's memory core aside and began to slowly approach him with my scalpel."

    hide dust
    show firefly_particles
    with Dissolve(0.5)

    pause 0.5

    show character_icon_box_1:
        xpos 800 ypos 50
    show draco_icon_blood_dying:
        xpos 800 ypos 48
    show character_icon_box_2:
        xpos 800 ypos 50
    with Dissolve(0.5)

    dra "\"I deserve this...\""

    hide character_icon_box_1
    hide draco_icon_blood_dying
    hide character_icon_box_2
    show character_icon_box:
        xpos 130 ypos 250
    show van_icon_blood_normal:
        xpos 130 ypos 248
    with Dissolve(0.5)

    v "\"...Hmm?\""

    hide character_icon_box
    hide van_icon_blood_normal
    show character_icon_box_1:
        xpos 800 ypos 50
    show draco_icon_blood_dying:
        xpos 800 ypos 48
    show character_icon_box_2:
        xpos 800 ypos 50
    with Dissolve(0.5)

    dra "\"This is all my fault...\""

    dra "\"I'm sorry, {w=0.5}Vanora...\""

    dra "{color=#f00}\"I'm sorry I couldn't save you...\"{/color}"

    hide character_icon_box_1
    hide draco_icon_blood_dying
    hide character_icon_box_2
    show character_icon_box:
        xpos 130 ypos 250
    show van_icon_blood_normal:
        xpos 130 ypos 248
    with Dissolve(0.5)

    $ say_who = _("Vanora")

    window show

    v "\"......\""

    hide van_icon_blood_normal
    show van_icon_blood_close:
        xpos 130 ypos 248
    with Dissolve(0.2)

    v "\"Goodbye, {w=0.5}Draco.\""

    window hide

    $ say_who = ""

    hide van_icon_blood_close
    hide character_icon_box
    with Dissolve(0.5)

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
    $ renpy.pause(3.0, hard='True')

    scene black
    $ renpy.transition(Dissolve(1.5))
    $ renpy.pause(2.0, hard=True)

    v "After that, {w=0.5}I took the elevator from the other end of the basement back to the lobby of the Myers Corporation alone."

    scene myers_1
    $ renpy.transition(Dissolve(1.5))
    $ renpy.pause(2.0, hard=True)

    v "When I walked out of the Myers Corporation, {w=0.5}I realized it was already the next morning."

    show myers_anon
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    v "A man in blue greeted me at the gate as if he had been expecting me."

    pause 0.5

    window show

    m "\"Oh, {w=0.5}Inspector! {w=0.5}It's been a while. {w=0.5}Welcome back to the Underground Myers Corporation!\""

    window hide

    pause 0.5

    scene black
    $ renpy.transition(Dissolve(1.5))
    $ renpy.pause(2.5, hard=True)

    window show

    m "\"Hmm? {w=0.5}What is it, {w=0.5}Inspector?\""

    m "\"What's upsetting you? {w=0.5}What are all these tears about?\""

    window hide

    stop music fadeout 5.0

    $ end_credit_mode == 1

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)
    $ renpy.block_rollback()
    $ _rollback = False

    jump end_credit
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
