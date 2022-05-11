
image basement_m:
    contains:
        "images/basement m flashback/basement m.png"

image basement_m_desk = "[basement_m_desk_image]"
image basement_m_desk_blurred_1 = im.Blur("images/basement m flashback/basement m desk 1.png", 1.5)
image basement_m_desk_blurred_2 = im.Blur("images/basement m flashback/basement m desk 2.png", 1.5)

image basement_m_steam:
    "images/basement m flashback/basement m steam/basement m steam 1.png"
    0.2
    "images/basement m flashback/basement m steam/basement m steam 2.png"
    0.2
    "images/basement m flashback/basement m steam/basement m steam 3.png"
    0.2
    "images/basement m flashback/basement m steam/basement m steam 4.png"
    0.2
    "images/basement m flashback/basement m steam/basement m steam 5.png"
    0.2
    "images/basement m flashback/basement m steam/basement m steam 6.png"
    0.2
    "images/basement m flashback/basement m steam/basement m steam 7.png"
    0.2
    "images/basement m flashback/basement m steam/basement m steam 8.png"
    0.2
    repeat

label basement_m_past_start:

    pause 3.0

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music ("music/TenseMusic.ogg") fadein 6.0

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    pause 1.0

    window show

    m "\"Here you are, {w=0.5}Inspector.\""

    $ rollback_ = True

    m "\"You know, {w=0.5}something's been bothering me for a while.\""

    v "\"What is it, {w=0.5}Monsieur M?\""

    window hide

    show basement_m:
        yoffset -1300
        linear 10 yoffset 0

    $ renpy.pause(10.0, hard='True')


    show basement_m:
        yoffset 0

    show demo_end_myers_lamp
    show basement_m_steam:
        block:
            ease 5.0 alpha 0
            pause 5.0
            ease 5.0 alpha 0.8
            pause 5.0
            repeat

    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(1.0, hard='True')

    window show

    m "\"Inspector, {w=0.5}if somebody could get a crystal-clear view of anyone's memory,\""

    m "\"Like seeing how a seemingly strong person had actually hidden in a corner and cried out in pain,\""

    m "\"Or the deceit and arguments behind what appears to be a beautiful love story,\""

    m "\"Or someone's painful childhood memories that have been repressed in the depths of their mind.\""

    m "\"What kind of power do you think this person would have in this world?\""

    window hide

    pause 1.0

    window show

    v "\"...They would be like an all-knowing, {w=0.5}all-powerful God.\""

    v "\"They would see all those things that no one wants to reveal and discover the truth that everyone is trying to hide.\""

    m "\"Yes. {w=0.5}There is no doubt that they could rule the entire world.\""

    m "\"And my goal... {w=0.5}is to be that person.\""

    v "\"!?\""

    v "\"Are you saying...\""

    m "\"Yes, {w=0.5}that's right. {w=0.5}Our researchers are getting closer and closer to reaching success.\""

    m "\"Soon, {w=0.5}I will become an omniscient god. {w=0.5}I will be able to see everyone's past, {w=0.5}and spy deep into their hearts.\""

    m "\"But strangely enough,\""

    m "\"Ever since this time last year, {w=0.5}important research documents and samples belonging to our organization have been disappearing one by one.\""

    m "\"What's even stranger is, {w=0.5}they all happen to be related to the research of this power.\""

    v "\"You mean, {w=0.5}they were stolen? {w=0.5}Someone is trying to steal our organization's research?\""

    m "\"It's indisputable that this thief is a member of our organization.\""

    v "\"!?\""

    v "\"There's a traitor who wants to acquire this power for themselves?\""

    m "\"......\""

    window hide

    pause 1.0

    window show

    m "\"Well Inspector, {w=0.5}have you noticed any suspicious members within the organization?\""

    v "\"......\""

    v "\"Sorry, {w=0.5}I haven't been paying much attention.\""

    m "\"...That's too bad.\""

    window hide

    pause 1.0

    window show

    m "\"You know, {w=0.5}Inspector. {w=0.5}There's something I've always admired about you.\""

    m "\"Whether you're telling the truth or not, {w=0.5}you are always able to keep that innocent look on your face.\""

    v "\"Monsieur M, {w=0.5}I would never lie to you.\""

    v "\"You are like a father to me.\""

    m "\"Oh, {w=0.5}am I?\""

    v "\"But surely, {w=0.5}such high-level research material is not something that just anyone can comprehend, {w=0.5}wouldn't you agree?\""

    v "\"If the thief was able to pinpoint exactly those documents and samples related to this memory-reading power, {w=0.5}I think he must be one of your researchers.\""

    m "\"......\""

    window hide

    $ renpy.pause(1.0, hard=True)

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    $ renpy.sound.play("music/legal department/Ringing.ogg", loop=True)

    stop music fadeout 1.0
    $ renpy.pause(0.1, hard=True)
    pause 2.0

    m "\"My apologies. {w=0.5}Please allow me to pick up the phone.\""

    show black as black_2
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(1.0, hard='True')

    stop sound fadeout 0.5

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/engineering room/door accept beep.ogg"

    pause 0.5

    m "\"Hello? {w=0.5}Monsieur M speaking.\""

    pause 1.0

    m "\"......\""

    pause 1.0

    m "\"Is that so? {w=0.5}I see. {w=0.5}Well done.\""

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/legal department/phone beep.ogg"

    pause 1.5

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music ("music/TenseMusic.ogg") fadein 3.0

    hide black_2
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    pause 2.0

    window show

    m "\"Inspector, {w=0.5}looks like I need to take my leave now.\""

    m "\"Keep being a good girl, {w=0.5}alright? {w=0.5}Don't touch anything on my desk.\""

    m "\"Perhaps there's a big secret hidden in this pink envelope... {w=0.5}Well, {w=0.5}who knows?\""

    v "\"......\""

    window hide

    stop music fadeout 4.0

    pause 2.0

    m "\"And by the way, {w=0.5}you were right.\""

    m "\"The thief was indeed one of our researchers.\""

    v "!?"

    m "\"I'll see you later.\""

    scene black
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(2.0, hard='True')

    $ basement_m_desk_image = "images/basement m flashback/basement m desk 1.png"

    pause 1.0

    scene basement_m_desk
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(2.0, hard='True')

    show character_icon_box:
        xpos 200 ypos 250
    show van_icon_close_eye:
        xpos 200 ypos 248
    with Dissolve(0.5)

    window show

    v "Monsieur M has left."


    show character_icon_box:
        xpos 200 ypos 250

    hide van_icon_close_eye
    show van_icon_normal:
        xpos 200 ypos 248

    v "From what I've heard, {w=0.5}ever since Monsieur M received a threatening video, {w=0.5}he became more and more paranoid."

    hide van_icon_normal
    show van_icon_close_eye:
        xpos 200 ypos 248

    v "Well, {w=0.5}to be honest, {w=0.5}I actually have no clue what he was like before that either."

    window hide

    hide van_icon_close_eye
    show van_icon_normal:
        xpos 200 ypos 248
    with Dissolve(0.5)

    pause 0.5

    $ say_who = _("Vanora")

    window show

    v "Tomorrow, {w=0.5}I will visit Vincent Edgeworth's mansion and investigate him using my cover as a detective."

    v "But my real objective is to uncover his secret weapon and destroy it."

    hide van_icon_normal
    show van_icon_close_eye:
        xpos 200 ypos 248
    with Dissolve(0.2)

    v "......"

    window hide

    $ say_who = ""

    $ renpy.music.set_volume(0.8, delay=0, channel='music')
    play music ["<silence 1.0>","music/creepy.wav"]

    pause 1.0

    show black
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    m "\"You know, {w=0.5}Inspector. {w=0.5}There's something I've always admired about you.\""

    m "\"Whether you're telling the truth or not, {w=0.5}you are always able to keep that innocent look on your face.\""

    hide black
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    pause 1.0

    $ say_who = _("Vanora")

    window show

    v "However, {w=0.5}I keep thinking about what Monsieur M had said today."

    hide van_icon_close_eye
    show van_icon_normal:
        xpos 200 ypos 248

    v "At first, {w=0.5}it seemed that he suspected me of being the thief,"

    v "But we actually both knew that this was impossible."

    hide van_icon_normal
    show van_icon_close_eye:
        xpos 200 ypos 248
    with Dissolve(0.2)

    v "The reason is simple: {w=0.5}I wasn't even part of this organization a year ago. {w=0.5}There is no way I could have stolen those things."

    window hide

    $ say_who = ""

    show black
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')


    hide van_icon_normal
    show van_icon_close_eye behind black:
        xpos 200 ypos 248

    m "\"And by the way, {w=0.5}you were right.\""

    m "\"The thief was indeed one of our researchers.\""

    hide black
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    pause 1.0

    $ say_who = _("Vanora")

    window show

    v "Just before Monsieur M left, {w=0.5}he received a phone call."

    v "The person on the other end of the phone may have just told him the true identity of the thief."

    v "But judging from Monsieur M's reaction, {w=0.5}everything seemed to be as he expected."

    hide van_icon_close_eye
    show van_icon_normal:
        xpos 200 ypos 248
    with Dissolve(0.2)

    v "Therefore, {w=0.5}it is way more likely that Monsieur M knew who the thief was long before our conversation."

    v "In that case, {w=0.5}why would Monsieur M invite me here to have such a seemingly meaningless conversation?"

    v "And it just happened to be the night before I was to go on a mission?"

    window hide

    $ say_who = ""

    stop music fadeout 3.0

    show black
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')


    hide van_icon_normal
    show van_icon_close_eye behind black:
        xpos 200 ypos 248

    m "\"Keep being a good girl, {w=0.5}alright? {w=0.5}Don't touch anything on my desk.\""

    m "\"Perhaps there's a big secret hidden in this pink envelope... {w=0.5}Well, {w=0.5}who knows?\""

    hide black
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    pause 1.0

    window show

    v "Don't touch anything on the desk..."

    hide van_icon_close_eye
    show van_icon_normal:
        xpos 200 ypos 248

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/shock2.ogg" fadeout 2.0

    v "......!" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    window hide

    hide van_icon_normal
    hide character_icon_box
    with Dissolve(0.5)

    v "Monsieur M, {w=0.5}I wish you had been more straightforward with your invitation."

    pause 1.0

    window show

    v "Monsieur M has never left me alone in his office before. {w=0.5}Nor has he ever specifically said such things."

    v "It is now obvious to me that he in fact meant quite the opposite - {w=0.5}{color=#f00}He actually wanted me to look at what was on the desk{/color}."

    v "Time to investigate the clues here."

    window hide

    $ renpy.music.set_volume(0.7, delay=0, channel='music')
    play music ("music/bgm/M office bgm.ogg")


    $ basement_m_lamp_on = False
    $ basement_m_investigate_folder = False
    $ basement_m_check_folder_dark = False
    $ basement_m_check_folder_light = False
    $ basement_m_folder_realization = False
    $ basement_m_check_laptop = False


    $ basement_m_photo_1_off = False
    $ basement_m_photo_2_off = False
    $ basement_m_photo_3_off = False

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    $ renpy.block_rollback()
    $ _rollback = False

    call screen basement_m_table_screen
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
