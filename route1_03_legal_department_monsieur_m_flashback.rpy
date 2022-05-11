
image legal_department_flashback_background = "images/Legal Department/legal department flashback background.png"
image legal_department_flashback_monsieur_m = "images/Legal Department/legal department flashback m.png"
image legal_department_flashback_monsieur_m_2 = "images/Legal Department/legal department flashback m 2.png"
image legal_department_flashback_monsieur_m_smile = "images/Legal Department/legal department flashback m smile.png"
image legal_department_flashback_lighting:
    "images/Legal Department/legal department flashback lighting.png"
    block:
        pause 2.5
        alpha 1.0
        linear 1.0 alpha 0.5
        pause 2.5
        alpha 1.0
        linear 1.0 alpha 0.5
        alpha 1.0
        linear 1.0 alpha 0.5
        repeat


image legal_department_elevator_1 = "images/Legal Department/legal department elevator 1.png"
image legal_department_elevator_2 = "images/Legal Department/legal department elevator 2.png"
image legal_department_elevator_door_1 = "images/Legal Department/legal department elevator door 1.png"
image legal_department_elevator_door_2 = "images/Legal Department/legal department elevator door 2.png"
image legal_department_elevator_signal = "images/Legal Department/legal department elevator signal.png"

label legal_department_monsieur_m_flashback_start:

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    $ renpy.pause(0.5, hard='True')
    pause 4.0

    window show
    noname_message "{color=#f00}Do you remember who you are?{/color}"
    window hide

    $ rollback_ = True

    nvl show Dissolve(0.2)

    $ legal_department_chanting_count = 0

    while legal_department_chanting_count != 2:
        nvl_text "{cps=*20}All Hail Myers All Hail Myers All Hail Myers All Hail Myers All Hail Myers All Hail Myers All Hail Myers{/cps}{nw}"
        nvl_text "{cps=*20}All Hail Myers All Hail Myers All Hail Myers All Hail Myers All Hail Myers All Hail Myers All Hail Myers{/cps}{nw}"
        nvl_text "{cps=*20}All Hail Myers All Hail Myers All Hail Myers All Hail Myers All Hail Myers All Hail Myers All Hail Myers{/cps}{nw}"
        nvl_text "{cps=*20}All Hail Myers All Hail Myers All Hail Myers All Hail Myers All Hail Myers All Hail Myers All Hail Myers{/cps}{nw}"
        nvl_text "{cps=*20}All Hail Myers All Hail Myers All Hail Myers All Hail Myers All Hail Myers All Hail Myers All Hail Myers{/cps}{nw}"

        nvl clear

        $ legal_department_chanting_count += 1

    nvl hide Dissolve(0.5)

    window show
    noname_message "{color=#f00}Do you still remember your purpose?{/color}"
    window hide
    nvl show Dissolve(0.2)

    $ legal_department_chanting_count = 0

    while legal_department_chanting_count != 2:
        nvl_text "{cps=*20}{color=#f00}All Hail Myers {/color}All Hail Myers All Hail Myers All Hail Myers All Hail Myers All Hail Myers All Hail Myers{/cps}{nw}"
        nvl_text "{cps=*20}All Hail Myers All Hail Myers All Hail Myers All Hail Myers All Hail Myers {color=#f00}All Hail Myers {/color}All Hail Myers{/cps}{nw}"
        nvl_text "{cps=*20}All Hail Myers All Hail Myers {color=#f00}All Hail Myers {/color}All Hail Myers All Hail Myers All Hail Myers All Hail Myers{/cps}{nw}"
        nvl_text "{cps=*20}All Hail Myers {color=#f00}All Hail Myers {/color}All Hail Myers All Hail Myers All Hail Myers All Hail Myers All Hail Myers{/cps}{nw}"
        nvl_text "{cps=*20}All Hail Myers All Hail Myers All Hail Myers All Hail Myers All Hail Myers {color=#f00}All Hail Myers{/color} All Hail Myers{/cps}{nw}"

        nvl clear

        $ legal_department_chanting_count += 1

    nvl clear
    nvl hide Dissolve(0.5)

    $ legal_department_chanting_count = 0

    window show
    noname_message "{color=#f00}We all miss you so much.{/color}"
    window hide

    nvl show Dissolve(0.2)

    while legal_department_chanting_count != 2:
        nvl_text "{cps=*20}{color=#f00}All Hail Myers All Hail Myers All Hail Myers All Hail Myers All Hail Myers All Hail Myers All Hail Myers{/color}{/cps}{nw}"
        nvl_text "{cps=*20}{color=#f00}All Hail Myers All Hail Myers All Hail Myers All Hail Myers All Hail Myers All Hail Myers All Hail Myers{/color}{/cps}{nw}"
        nvl_text "{cps=*20}{color=#f00}All Hail Myers All Hail Myers All Hail Myers All Hail Myers All Hail Myers All Hail Myers All Hail Myers{/color}{/cps}{nw}"
        nvl_text "{cps=*20}{color=#f00}All Hail Myers All Hail Myers All Hail Myers All Hail Myers All Hail Myers All Hail Myers All Hail Myers{/color}{/cps}{nw}"
        nvl_text "{cps=*20}{color=#f00}All Hail Myers All Hail Myers All Hail Myers All Hail Myers All Hail Myers All Hail Myers All Hail Myers{/color}{/cps}{nw}"

        nvl clear

        $ legal_department_chanting_count += 1

    nvl hide Dissolve(0.5)

    window show
    noname_message "{color=#f00}Hurry up and come back home.{/color}"
    window hide

    show legal_department_flashback_background behind game_over_static
    show legal_department_flashback_monsieur_m behind game_over_static:
        zoom 1.1 yoffset -20 xalign 0.5 yalign 0.5
    show legal_department_flashback_lighting behind game_over_static
    show game_over_static:
        ease 4.0 alpha 0.01
        block:
            pause 4.0
            ease 4.0 alpha 0.2
            pause 3.0
            ease 4.0 alpha 0.01

    $ renpy.pause(1.0, hard='True')

    pause 4.0

    window show

    $ say_who = "???"

    m "\"Oh, {w=0.5}hey! {w=0.5}Hello! {w=0.5}Welcome to Myers Corporation!\""

    m "\"How does it feel to be alive? {w=0.5}Pretty good, {w=0.5}huh?\""

    m "\"I know you're still a little confused right now, {w=0.5}but that's okay! {w=0.5}I assure you that you will soon get used to it.\""

    m "\"Oh? {w=0.5}You're asking what your mission is?\""

    show legal_department_flashback_monsieur_m_smile behind game_over_static:
        zoom 1.1 yoffset -7 xalign 0.5 yalign 0.5
    with Dissolve(0.2)

    m "\"My Dear, {w=0.5}patience, {w=0.5}we'll get to that.\""

    m "\"Where should I start?{w=0.5}...Oh!\""

    m "\"You know, {w=0.5}I have this old friend who's a little mad at me.\""

    m "\"A little mad that he wants to murder me and destory my company.\""

    m "\"So he has made a weapon. {w=0.5}A very deadly weapon.\""

    m "\"We don't know what that weapon is.\""

    m "\"But a little birdy told me it had something to do with other people's memories. {w=0.5}Ah! {w=0.5}Pretty frightening right?\""

    m "\"So, {w=0.5}here's what I need you to do-\""

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    $ renpy.sound.play("music/legal department/Ringing.ogg", loop=True)

    stop music fadeout 1.0

    $ renpy.pause(0.1, hard=True)

    hide legal_department_flashback_monsieur_m_smile
    show legal_department_flashback_monsieur_m behind game_over_static:
        zoom 1.1 yoffset -20 xalign 0.5 yalign 0.5
        yoffset 0
        ease 0.2 yoffset -20

    $ renpy.pause(1.0, hard=True)
    pause 2.0

    m "\"Oh, {w=0.5}my apologies! {w=0.5}I hope this is about my delivery!\""

    stop sound

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/engineering room/door accept beep.ogg"

    hide legal_department_flashback_monsieur_m
    show legal_department_flashback_monsieur_m_2 behind game_over_static:
        zoom 1.05 yoffset -20 xalign 0.5 yalign 0.5
        yoffset 0
        ease 0.2 yoffset -20

    m "\"Hello?\""

    m "\"Oh! {w=0.5}Already? {w=0.5}That's awesome!\""

    m "\"But unfortunately, {w=0.5}I'm not at home right now, {w=0.5}my friend.\""

    m "\"Yes, {w=0.5}just leave the package at the door. {w=0.5}Yes, {w=0.5}the entire uniform!\""

    m "\"Alright, {w=0.5}that's great! {w=0.5}Thank you so much!\""

    window hide

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/legal department/phone beep.ogg"

    pause 1.5

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music "music/ambience/horror ambience 2.ogg"

    hide legal_department_flashback_monsieur_m_2
    show legal_department_flashback_monsieur_m behind game_over_static:
        zoom 1.1 yoffset -20 xalign 0.5 yalign 0.5
        yoffset 0
        ease 0.2 yoffset -20

    m "\"Sorry about that. {w=0.5}Where was I again?\""

    show legal_department_flashback_monsieur_m_smile behind game_over_static:
        zoom 1.1 yoffset -7 xalign 0.5 yalign 0.5
    with Dissolve(0.2)

    m "\"That's right! {w=0.5}I need you to locate his weapon.\""

    m "\"And then destroy it.\""

    m "\"And while you're at it, {w=0.5}try to figure out what kind of experiments this guy is up to.\""

    m "\"And your code name, {w=0.5}will be...\""

    $ say_who = ""

    stop music fadeout 1.0

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/legal department/explosion 1.ogg"

    $ renpy.transition(PushMove(0.05, "pushup"))
    $ renpy.pause(0.05, hard=True)
    $ renpy.transition(PushMove(0.05, "pushup"))
    $ renpy.pause(0.05, hard=True)

    hide bad_tv_signal onlayer tvsignal
    scene legal_department
    $ renpy.transition(PushMove(0.05, "pushup"))
    $ renpy.pause(0.05, hard=True)
    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15))
    $ renpy.pause(1.0, hard=True)

    pause 2.0

    van "!?"

    van "A sudden, {w=0.5}tremendous shudder from the legal department snapped me back to reality."

    van "What just happened?"

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music "music/intense chase.ogg"

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
    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 1.5, dist=15))

    show legal_department at constant_shake:
        zoom 1.05 xoffset 50 yoffset -20 xalign 0.5 yalign 05
    show legal_department_blurred:
        alpha 0
        parallel:
            pause 1.0
            linear 0.8 alpha 0 xalign 0.5 yalign 0 zoom 1.0
            linear 0.8 alpha 0.3 xalign 0.5 yalign 0 zoom 1.2
            linear 0.8 alpha 0 xalign 0.5 yalign 0 zoom 1.0
            repeat
    show main_title_shadow

    $ renpy.pause(1.0, hard=True)

    window show

    van "!?"

    van "Suddenly, {w=0.5}a man flew through the wall connecting the laboratory to the legal department, {w=0.5}as if he was thrown by something with full force."

    van "He was slammed into the wall at the other end of the department, {w=0.5}and then fell to the floor."

    show black:
        zoom 1.2 xalign 0.5 yalign 0.5 alpha 0.8
    with Dissolve(0.2)

    van "Is that..."

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/shock2.ogg" fadeout 2.0
    van "\"Dra-{w=0.5}Draco!!!???\"" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    van "But because of the massive impact, {w=0.5}Draco had lost his consciousness."

    window hide

    hide black with Dissolve(0.5)

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/monster moan 2.ogg"
    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 2.5, dist=15))
    $ renpy.pause(2.5, hard=True)

    pause 1.0

    van "What followed was an inhuman roar from the lab. {w=0.5}I could hear the monster's approaching steps."

    show black:
        zoom 1.2 xalign 0.5 yalign 0.5 alpha 0.8
    with Dissolve(0.5)

    $ renpy.pause(0.1, hard=True)

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/shock2.ogg" fadeout 2.0
    van "\"Draco!! {w=0.5}Draco!!\"" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    dra "\"......\""

    van "I shook Draco violently, {w=0.5}but he didn't respond."

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/shock2.ogg" fadeout 2.0
    van "\"Draco, {w=0.5}wake up!!!\"" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    dra "\"......\""

    hide black with Dissolve(0.5)

    van "Damn it, {w=0.5}what should I do!?"

    van "!?"

    van "The basement! {w=0.5}Quick!"

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/run.ogg"

    scene black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(1.0, hard=True)

    van "I dashed to the elevator and punched the button."

    van "Hurry, {w=0.5}please be quick!!"

    show legal_department_elevator_2
    show legal_department_elevator_door_1
    show legal_department_elevator_door_2
    show legal_department_elevator_1
    show main_title_shadow
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(1.0, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/legal department/ElevatorOpening.ogg"

    show legal_department_elevator_signal
    $ renpy.transition(Dissolve(0.2))
    $ renpy.pause(0.2, hard='True')


    show legal_department_elevator_door_1:
        ease 1.5 xoffset -300
    show legal_department_elevator_door_2:
        ease 1.5 xoffset 300

    $ renpy.pause(1.5, hard='True')

    van "!"

    scene black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    van "I hurried and dragged Draco into the elevator, {w=0.5}then pressed the button to close the door."

    stop music fadeout 3.0

    jump legal_department_elevator_start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
