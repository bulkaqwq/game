
image legal_department = "images/Legal Department/legal department.png"
image legal_department_blurred = im.Blur("images/Legal Department/legal department.png", 1.5)
image legal_department_vincent_table = "images/Legal Department/legal department vincent table.png"
image legal_department_letter = "images/Legal Department/legal department letter.png"
image legal_department_vincent_table_2 = "images/Legal Department/legal department vincent table 2.png"
image legal_department_glove = "images/Legal Department/legal department glove.png"
image legal_department_vincent_table_2_blurred = im.Blur("images/Legal Department/legal department vincent table 2.png", 1.5)
image legal_department_glove_blurred = im.Blur("images/Legal Department/legal department glove.png", 1.5)

screen legal_department_vincent_desk_screen:

    imagebutton:
        xpos 426
        ypos 205
        idle "images/Legal Department/legal department letter idle.png"
        hover "images/Legal Department/legal department letter hover.png"
        focus_mask "images/Legal Department/legal department letter hover.png"
        action Jump("legal_department_vincent_desk_investigate_letter")

    imagebutton:
        xpos 771
        ypos 170
        idle "images/Legal Department/legal department glove idle.png"
        hover "images/Legal Department/legal department glove hover.png"
        focus_mask "images/Legal Department/legal department glove hover.png"
        action Jump("legal_department_vincent_desk_investigate_glove")

label legal_department_start:

    $ renpy.free_memory()

    $ _skipping = True
    $ renpy.block_rollback()
    if renpy.is_skipping():
        $ renpy.choice_for_skipping()

    $ renpy.pause(1.0, hard="True")
    pause 1.0

    $ renpy.music.set_volume(0.2, delay=0, channel='music')
    play music "music/chapter2-haunting.ogg"

    pause 4.0

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/myers lobby/draco footstep.ogg"

    pause 3.0

    $ renpy.pause(3.0, hard="True")

    stop sound fadeout 1.0

    $ _rollback = True

    scene legal_department
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')
    show dust:
        alpha 0
        block:
            ease 5.0 alpha 0.5
            ease 5.0 alpha 1.0
            ease 5.0 alpha 0.5
            ease 5.0 alpha 0
            pause 5.0
            repeat

    pause 4.0
    $ renpy.pause(0.1, hard="True")

    window show

    van "......"

    van "Here we are. {w=0.5}The Legal Department."

    van "It's hard to believe that Vincent used to work here."

    van "!?"

    $ say_who = name

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show legal_department:
        ease 0.5 zoom 1.5 yoffset 300

    $ renpy.pause(0.5, hard='True')

    van "Wait a second. {w=0.5}In the distance, {w=0.5}is that...{w=0.5} an elevator?"

    van "Zalmona had told me,"

    van "The only way to get back to the Myers lobby now is to take the elevator to the basement, {w=0.5}and then return there from the other side."

    van "So it seems that this is what she was talking about."

    van "However..."

    show legal_department:
        ease 0.5 zoom 1.0 yoffset 0

    van "I've come a long way, {w=0.5}shouldn't I investigate this place first?"

    van "......"

    van "But..."

    van "What's the point."

    scene black with Dissolve(0.5)

    van "......"

    van "I have now long lost the confidence I had when I was confronting Draco in the Myers lobby."

    van "I'm not sure if I want to know the truth anymore."

    $ say_who = ""

    scene lobby_bright
    show vic-smoke-low-talk-small at vic_pos
    show lobby_vic_smoke_animation:
        xoffset 70 alpha 0
        block:
            ease 5.0 xoffset 70 alpha 0
            pause 5.0
            ease 5.0 xoffset 70 alpha 0.5
            pause 5.0
            repeat
    show memory_frame:
        linear 1.0 alpha 0.3
        linear 1.0 alpha 1
        repeat
    $ renpy.transition(Fade(.2, 0, 0.25, color="#fff"))
    $ renpy.pause(0.5, hard='True')

    vic "\"You have to realize, {w=0.5}losing your memories could also be a blessing.\""

    vic "\"Countless people are imprisoned by their own memories; {w=0.5}they try their best to let go, {w=0.5}yet cling to them at the same time.\""

    vic "\"But you, {w=0.5}on the other hand, {w=0.5}are given a second chance.\""

    $ say_who = _("Victor")
    show vic-smoke-talk-small behind memory_frame at vic_pos with Dissolve(0.2)

    vic "\"Isn't that wonderful? {w=0.5}I'll be honest, {w=0.5}even I am getting a bit jealous.\""

    $ say_who = ""

    scene lobby_bright
    show vin-arm-talk-small at vin_pos_2
    show vic-normal-small-flip at vic_pos_2
    show memory_frame:
        linear 1.0 alpha 0.3
        linear 1.0 alpha 1
        repeat
    $ renpy.transition(Fade(.2, 0, 0.25, color="#fff"))
    $ renpy.pause(0.5, hard='True')

    vin "\"How did you end up here? {w=0.5}[name!t], {w=0.5}I regret to inform you that I don't know either.\""

    vin "\"The truth is, {w=0.5}my butler was the one who heard peculiar knocking sounds on the door last night.\""

    vin "\"When he went to open it, {w=0.5}he saw you face down on the stairs. {w=0.5}Unconscious.\""

    scene myers_lobby
    show draco_close_eye_talk at dra_pos_1
    show memory_frame:
        linear 1.0 alpha 0.3
        linear 1.0 alpha 1
        repeat
    $ renpy.transition(Fade(.2, 0, 0.25, color="#fff"))
    $ renpy.pause(0.5, hard='True')

    $ say_who = _("Draco")

    dra "\"Your seemingly commendable courage is nothing more than ignorance wrapped up in a pretty package.\""

    hide draco_close_eye_talk
    show draco_normal behind memory_frame at dra_pos_1
    show draco_talk behind memory_frame at dra_pos_1
    with Dissolve(0.2)

    dra "\"You have absolutely no clue what you are about to face.\""

    dra "\"Do you really believe that you can face up to all the dangers that are coming your way?\""

    dra "\"Do you really believe that you can accept the truth that will be revealed?\""

    $ say_who = ""

    scene black
    $ renpy.transition(Fade(.2, 0, 0.25, color="#fff"))
    $ renpy.pause(0.5, hard='True')

    van "......"

    van "Vincent, {w=0.5}Victor, {w=0.5}and Draco..."

    van "How many lies are there all around me?"

    van "...Why is it like that?"

    van "Why is everyone lying to me?"

    van "Ever since I woke up in the mansion, {w=0.5}I have been deceived again and again."

    van "Why, {w=0.5}why are all of you lying to me?"

    window hide

    stop music fadeout 3.0

    scene legal_department
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    pause 2.0

    van "......"

    pause 2.0

    van "What am I doing. {w=0.5}I don't have time to think about that right now."

    van "Since I am already here, {w=0.5}I might as well take a little look around first."

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/myers lobby/draco footstep.ogg"

    scene black with Dissolve(0.5)

    $ renpy.pause(3.0, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/PageFlipshort.ogg"

    pause 2.0

    van "I started to briefly read through some of the documents I've found."

    pause 2.0

    van "......"

    van "Uh...{w=0.5}These documents from the Legal Department..."

    van "I really don't understand them at all..."

    pause 2.0

    $ renpy.pause(0.1, hard='True')

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/shock2.ogg" fadeout 2.0

    window show

    $ renpy.pause(0.1, hard='True')

    van "!?" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    van "Hold on a second. {w=0.5}The nameplate on this table..."

    van "\"Vincent Edgeworth, {w=0.5}Chief Legal Officer.\""

    van "So, {w=0.5}then, {w=0.5}this used to be -"

    scene legal_department_vincent_table with Dissolve(0.5)

    van "{color=#f00}Vincent's office table!?{/color}"

    van "On the table was a note and a glove."

    van "The note looked brand new, {w=0.5}and therefore seemed out of place compared to the rest of the files here."

    van "Someone could have just recently left it here."

    van "Was Zalmona the one who put it here?"

    window hide

    $ renpy.music.set_volume(0.1, delay=0, channel='sound')
    play sound "music/cloth.mp3" fadeout 2.0

    show legal_department_letter onlayer inyourface:
        xalign 0.5 yalign 0.5
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    pause 1.0

    van "I picked up the note from the desk."

    $ renpy.music.set_volume(0.5, delay=0, channel='music')
    play music "music/ambience/horror ambience 1.ogg" fadein 3.0

    show black onlayer inyourface:
        zoom 2.0 alpha 0.5 xalign 0.5 yalign 0.5
    nvl show Dissolve(0.5)

    diary "\"Dear my lovely [name!t],\""

    diary "\"How are you doing?\""

    diary "\"Ha-ha. {w=0.5}I'm just joking. {w=0.5}Of course I know you're not doing well. {w=0.5}Because you've lost all your memories.\""

    diary "\"So, {w=0.5}do you want to get all your memories back?\""

    diary "\"I know you do.\""

    diary "\"In that case, {w=0.5}I have left you a small gift.\""

    nvl clear

    diary "\"I'm sure it will help a lot in getting back what you want.\""

    diary "\"- an old friend who wishes to remain anonymous\""

    nvl clear

    hide black onlayer inyourface
    nvl hide Dissolve(1.0)

    $ renpy.pause(1.0, hard='True')

    hide legal_department_letter onlayer inyourface
    with Dissolve(1.0)

    van "A gift for me?"

    van "It must be referring to the glove next to it."

    pause 2.0

    van "......"

    van "For some reason, {w=0.5}I was blasted with a wave of anxiety."

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    $ renpy.pause(0.5, hard='True')

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/UI Dark.ogg"

    noname "Objective: {w=0.5}Put on the glove."

    $ rollback_ = False
    $ renpy.block_rollback()
    $ _rollback = False

    call screen legal_department_vincent_desk_screen

label legal_department_vincent_desk_investigate_letter:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/selectsounds.ogg"

    van "A note with a message written on it. {w=0.5}Looks like it was just left recently."

    show legal_department_letter onlayer inyourface:
        xalign 0.5 yalign 0.5
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    show black onlayer inyourface:
        zoom 2.0 alpha 0.5 xalign 0.5 yalign 0.5
    nvl show Dissolve(0.5)

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    diary "\"Dear my lovely [name!t],\""

    $ rollback_ = True

    diary "\"How are you doing?\""

    diary "\"Ha-ha. {w=0.5}I'm just joking. {w=0.5}Of course I know you're not doing well. {w=0.5}Because you've lost all your memories.\""

    diary "\"So, {w=0.5}do you want to get all your memories back?\""

    diary "\"I know you do.\""

    diary "\"In that case, {w=0.5}I have left you a small gift.\""

    nvl clear

    diary "\"I'm sure it will help a lot in getting back what you want.\""

    diary "\"- an old friend who wishes to remain anonymous\""

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)
    $ renpy.block_rollback()
    $ _rollback = False

    nvl clear

    hide black onlayer inyourface
    nvl hide Dissolve(1.0)

    hide legal_department_letter onlayer inyourface
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    call screen legal_department_vincent_desk_screen

label legal_department_vincent_desk_investigate_glove:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/selectsounds.ogg"

    window show

    van "Should I put on the glove?"

    window hide

    menu:
        "Yes":
            $ renpy.pause(1.0, hard='True')
            $ renpy.music.set_volume(0.1, delay=0, channel='sound')
            play sound "music/cloth.mp3" fadeout 2.0

            $ renpy.block_rollback()
            $ _rollback = True
            $ _skipping = True

            jump legal_department_monsieur_m_flashback
        "No":

            call screen legal_department_vincent_desk_screen

label legal_department_monsieur_m_flashback:

    stop music fadeout 1.0

    scene legal_department_vincent_table_2
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    $ renpy.pause(1.0, hard='True')

    show legal_department_glove onlayer inyourface:
        xalign 0.5 yalign 0.5
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    van "The glove...{w=0.5}fits my hand perfectly."

    $ rollback_ = True

    show legal_department_vincent_table_2_blurred:
        ease 0.4 xoffset -10 yoffset -10 alpha 0.5

        ease 0.4 xoffset 10 yoffset -10 alpha 0.5

        ease 0.4 xoffset -10 yoffset 10 alpha 0.5

        ease 0.4 xoffset 10 yoffset 10 alpha 0.5

        ease 0.4 xoffset 0 yoffset 0 alpha 1.0

    $ renpy.pause(0.1, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/heartbeat.ogg"

    show legal_department_glove_blurred onlayer inyourface:
        xalign 0.5 yalign 0.5

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

    hide legal_department_vincent_table_2_blurred
    hide legal_department_glove_blurred onlayer inyourface
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    van "!?"

    hide legal_department_glove onlayer inyourface
    scene black
    show game_over_static
    show bad_tv_signal onlayer tvsignal:
        linear 1.0 alpha 1.0
        linear 1.0 alpha 0.2
        repeat
    show white back
    $ renpy.transition(Dissolve(0.1))
    $ renpy.pause(0.1, hard='True')

    stop music

    $ renpy.music.set_volume(0.7, delay=0, channel='sound')
    play sound "music/teleport.ogg"

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music "music/ambience/horror ambience 2.ogg"

    $ renpy.pause(0.5, hard='True')

    hide white back
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    jump legal_department_monsieur_m_flashback_start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
