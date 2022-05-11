

image john_past_desktop = "images/john past/john past desktop.png"
image john_past_desktop_blurred = im.Blur("images/john past/john past desktop.png", 3.0)
image john_past_vic_office_1 = "images/john past/vic office 1.png"

label john_past_start:

    pause 2.0

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music ["music/ambience/mic horror ambience 4.ogg","<silence 1.0>"] fadein 5.0

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    $ renpy.pause(1.0, hard='True')
    pause 2.0

    anon "Myers Corporation."

    $ rollback_ = True

    anon "That's the goal of everyone at G4."

    anon "A place to make dreams come true and parents proud."

    anon "At least... {w=0.5}that's what I thought."

    anon "I will never forget the day I came to Myers."

    anon "My excitement and exhilaration, {w=0.5}inevitably, {w=0.5}mixed up with nervousness."

    anon "Because to me, {w=0.5}it was the reward for my years of dedication and hard work."

    anon "I think... {w=0.5}every single elite in Myers can relate to that."

    anon "But who would have thought that behind this company that so many G4 residents longed for, {w=0.5}there was only filth, {w=0.5}sin, {w=0.5}and blood that would never dry up."

    anon "Who am I?"

    anon "I'm no longer human."

    anon "At this time, {w=0.5}I can't even remember my own name."

    anon "Every day now, {w=0.5}I can only wander aimlessly around Myers."

    anon "What am I struggling to find?"

    anon "......"

    anon "I don't know."

    anon "I don't know."

    anon "{cps=*2}I don't know I don't know I don't know I don't know I don't know I don't know I don't know I don't know I don't know I don't know{/cps}"

    stop music fadeout 5.0

    anon "......"

    anon "I only wish..."

    anon "Someone could put me out of my misery."

    pause 4.0
    $ renpy.pause(0.1, hard='True')

    scene john_past_desktop
    show john_past_desktop_blurred
    $ renpy.transition(Dissolve(2.0))
    $ renpy.pause(3.0, hard='True')

    $ renpy.music.set_volume(0.5, delay=0, channel='background noise')
    $ renpy.music.play("music/John Past/office background.ogg", channel="background noise", loop=True)

    pause 1.0

    van "What... {w=0.5}what is this?"

    van "Where have I... {w=0.5}arrived at???"

    hide john_past_desktop_blurred
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    pause 2.0

    john "Phew..."

    john "Okay, {w=0.5}John, {w=0.5}calm down..."

    john "It's just a job."

    john "I just need to smile and politely introduce myself to everyone."

    john "Ok, {w=0.5}ok..."

    john "Three, {w=0.5}two, {w=0.5}one -"

    $ renpy.music.set_volume(0.4, delay=0, channel='sound')
    play sound ("music/John Past/punch-face-hard.ogg")

    john "\"Nice to meet you! {w=0.5}My name is John!\"" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    john "Umm..."

    john "Wouldn't this seem a bit too emotional?"

    john " Start over, {w=0.5}start over..."

    john "Three, {w=0.5}two, {w=0.5}one -"

    $ renpy.music.set_volume(0.4, delay=0, channel='sound')
    play sound ("music/John Past/punch-face-hard.ogg")

    john "\"Nice to meet...\"" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/hmm.ogg"

    anon "\"Oh! {w=0.5}Are you John, {w=0.5}the new guy?\""

    john "!?"

    $ renpy.music.set_volume(0.5, delay=0, channel='music')
    play music ("music/bgm/jazz-lounge.ogg")

    scene john_past_vic_office_1:
        xoffset 0 yoffset -83
    $ renpy.transition(Dissolve(0.8))
    $ renpy.pause(1.6, hard='True')

    scene john_past_vic_office_1:
        xoffset 0 yoffset -83
        ease 1.0 xoffset 0 yoffset 0
        xoffset 0 yoffset 0
    $ renpy.pause(0.5, hard='True')

    show vic_normal at vic_pos
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    show bedroom_dust:
        alpha 0
        pause 5.0
        block:
            ease 5.0 alpha 0.5
            ease 5.0 alpha 1.0
            ease 5.0 alpha 0.5
            ease 5.0 alpha 0
            pause 5.0
            repeat

    pause 1.0

    show vic_talk at vic_pos
    with Dissolve(0.2)

    window show

    vic "\"Welcome to Myers! {w=0.5}In case you don't know, {w=0.5}I'm the {color=#f00}Chief Investment Officer{/color}, {w=0.5}Victor Blake.\""

    hide vic_talk with Dissolve(0.2)

    john "\"Ah, {w=0.5}nice to meet you, {w=0.5}Mr. Blake!\""

    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/hehe.ogg"

    show vic_happy_eye at vic_pos
    with Dissolve(0.2)

    $ say_who = _("Victor")

    vic "\"Ha ha, {w=0.5}no need to be so formal. {w=0.5}Just call me Victor.\""

    show vic_talk at vic_pos
    hide vic_happy_eye
    with Dissolve(0.2)

    vic "\"Looks like you've done all the paperwork to get started? {w=0.5}Otherwise you wouldn't even know where your desk is.\""

    hide vic_talk with Dissolve(0.2)

    $ say_who = ""

    john "\"Yes! {w=0.5}I've done it all.\""

    show vic_talk at vic_pos
    with Dissolve(0.2)

    vic "\"Very good. {w=0.5}Have you finished the online courses for the G4 district as well?\""

    hide vic_talk with Dissolve(0.2)

    john "\"Uh...{w=0.5}online courses?\""

    show vic_high_right_brow at vic_pos
    with Dissolve(0.2)

    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/huh.ogg"

    vic "\"Hum? {w=0.5}Could it be that this is your first job?\""

    hide vic_high_right_brow with Dissolve(0.2)

    john "\"Ye-{w=0.5}yes...\""

    john "\"Actually, {w=0.5}I have just graduated from college.\""

    show vic_happy_eye at vic_pos
    with Dissolve(0.2)

    $ say_who = _("Victor")

    vic "\"Oh! {w=0.5}Is that so?\""

    vic "\"Your parents must be very proud of you being able to work in Myers right out of college.\""

    show vic_talk at vic_pos
    hide vic_happy_eye
    with Dissolve(0.2)

    vic "\"But even so, {w=0.5}you have to complete the G4 online course. {w=0.5}It is mandatory for every employee on the job.\""

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/hmm.ogg"

    show vic_low_brow_talk at vic_pos
    with Dissolve(0.2)

    vic "\"Don't worry. {w=0.5}It's just trying to teach you etiquette and how to behave properly.\""

    vic "\"You know...\""

    vic "\"Don't get physical with your co-workers and things like that.\""

    hide vic_low_brow_talk with Dissolve(0.2)

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/cough.ogg" fadeout 2.0

    vic "\"Shh... {w=0.5}Let me tell you, {w=0.5}I've never really paid attention to their lectures either.\""

    $ say_who = ""

    show vic_unhappy at vic_pos
    with Dissolve(0.2)
    hide vic_low_brow_talk
    hide vic_talk
    hide vic_normal

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/vin_hmm.ogg"
    anon "\"Oh, {w=0.5}really? {w=0.5}That's not good to hear, {w=0.5}Director Blake.\""

    window hide

    hide vic_unhappy
    show vic_unhappy_flip
    $ renpy.transition(Dissolve(0.3))
    $ renpy.pause(0.5, hard='True')

    show vic_unhappy_flip:
        linear 0.4 xpos 0.25
    $ renpy.pause(0.1, hard='True')

    show vin_angry at vin_pos_2
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    window show

    vin "\"In fact, {w=0.5}I believe you are the one who needs these courses the most in the company, {w=0.5}Mr. Director.\""

    vin "\"Need I remind you of your great feat last night when you vomited all over the floor in the lavatory of my residence?\""

    vin "\"I must say your \"etiquette\" and \"behavior\" are quite impressive, {w=0.5}Mr. Blake.\""


    show vic_unhappy_flip at vic_pos_2
    show vic_talk_flip at vic_pos_2
    with Dissolve(0.2)

    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/huh.ogg"

    vic "\"Oh, {w=0.5}my dear Vincent! {w=0.5}What brings you to the Investment Department?\""

    show vic_normal_flip at vic_pos_2
    show vin_satire at vin_pos_2
    with Dissolve(0.2)
    hide vic_talk_flip
    hide vic_unhappy_flip

    vin "\"I just happened to be passing by. {w=0.5}It seems that Mr. Myers wants to discuss some important matters with me.\""

    show vin_high_brow_satire at vin_pos_2
    hide vin_satire
    hide vin_angry
    with Dissolve(0.2)

    vin "\"So, {w=0.5}who is this?\""

    show vic_talk_flip at vic_pos_2
    with Dissolve(0.2)

    vic "\"Myers' newest employee, {w=0.5}John. {w=0.5}As of today, {w=0.5}John is a member of the Investment Department.\""

    hide vic_talk_flip with Dissolve(0.2)

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/John Past/male gasp.ogg"

    john "\"He-{w=0.5}hello!\"" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    window hide

    show vin_normal at vin_pos_2
    with Dissolve(0.2)
    hide vin_high_brow_satire
    hide vin_angry
    hide vin_satire
    $ renpy.pause(0.1, hard='True')
    pause 0.3

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/Vincent.ogg"

    show vin_smile at vin_pos_2
    $ renpy.transition(Dissolve(0.2))
    $ renpy.pause(0.2, hard=True)

    window show

    vin "\"John is it? {w=0.5}Nice to meet you. {w=0.5}I am Vincent Edgeworth.\""

    show vin_high_single_brow_talk at vin_pos_2
    show vic_low_brow_flip at vic_pos_2
    hide vin_smile
    hide vin_normal
    with Dissolve(0.2)

    vin "\"You have my sympathies for being assigned to this man's department.\""

    vin "\"If he ever treats you badly, {w=0.5}you are welcome to transfer to the {color=#f00}Legal Department{/color} anytime.\""

    vin "\"We are located on the other side of the company.\""

    hide vin_high_single_brow_talk
    hide vin_smile
    show vin_normal at vin_pos_2
    with Dissolve(0.2)

    john "\"Err...{w=0.5}Ok, {w=0.5}understood...\""

    hide vic_low_brow_flip
    show vic_talk_flip at vic_pos_2
    with Dissolve(0.2)

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/hmm.ogg"

    vic "\"Oh, {w=0.5}congratulations on your success in helping Myers out, {w=0.5}Vincent.\""

    hide vic_talk_flip
    with Dissolve(0.2)

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/vin_hmm.ogg"

    show vin_satire at vin_pos_2
    with Dissolve(0.2)

    vin "\"...Victor. {w=0.5}That was already {color=#f00}two months ago{/color}.\""

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/shock2.ogg" fadeout 2.0

    john "!?" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    john "\"So you're the {color=#f00}famous lawyer who defended Myers{/color} in the G4 Cyborg Incident?\""

    john "\"I heard your performance in the courtroom was incredible!\""

    hide vin_satire
    show vin_smile at vin_pos_2
    with Dissolve(0.2)

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/Vincent.ogg"

    vin "\"I'm very flattered, {w=0.5}John. {w=0.5}It was indeed me who defended Myers, {w=0.5}but I wouldn't consider myself famous.\""

    hide vin_smile
    with Dissolve(0.2)

    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/hehe.ogg"

    show vic_talk_flip at vic_pos_2
    with Dissolve(0.2)

    vic "\"Vincent has had his hands full with this for a while. {w=0.5}Good thing he can finally relax now.\""

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/vin_hmm.ogg"

    hide vic_talk_flip
    show vin_satire at vin_pos_2
    with Dissolve(0.2)

    $ say_who = _("Vincent")

    vin "\"Aren't you saying that too soon, {w=0.5}Victor?\""

    hide vin_satire with Dissolve(0.2)

    vin "\"Anyways, {w=0.5}I must get going. {w=0.5}I can't keep Mr. Myers waiting.\""

    show vin_smile at vin_pos_2
    with Dissolve(0.2)

    vin "\"It was my pleasure to meet you, {w=0.5}John. {w=0.5}Welcome to Myers.\""

    hide vin_smile
    $ renpy.transition(Dissolve(0.2))
    $ renpy.pause(0.3, hard=True)

    $ say_who = ""

    window hide

    hide vin_normal
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')
    pause 0.5

    show vic_normal_flip:
        linear 0.4 xpos 0.55
    $ renpy.pause(0.5, hard=True)

    show vic_normal at vic_pos
    hide vic_normal_flip
    $ renpy.transition(Dissolve(0.3))
    $ renpy.pause(0.6, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/hmm.ogg"

    show vic_low_brow_talk at vic_pos
    $ renpy.transition(Dissolve(0.2))
    $ renpy.pause(0.2, hard='True')

    window show

    stop music fadeout 5.0

    vic "\"You are lucky to meet Vincent on your first day. {w=0.5}Even I don't see him very often at work.\""

    vic "\"That guy's attitude towards others has improved a lot since college, {w=0.5}but he hasn't changed a bit towards me.\""

    show vic_low_brow at vic_pos
    with Dissolve(0.2)

    john "\"Since college? {w=0.5}Were you and Mr. Edgeworth college classmates?\""

    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/hehe.ogg"

    show vic_talk at vic_pos
    with Dissolve(0.2)
    hide vic_low_brow_talk
    hide vic_low_brow

    vic "\"Ha ha, {w=0.5}not only that. {w=0.5}We were also {color=#f00}roommates{/color}.\""

    hide vic_talk with Dissolve(0.2)

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/shock2.ogg" fadeout 2.0

    john "\"Eh!? \"" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    show vic_low_brow_talk at vic_pos
    with Dissolve(0.2)

    $ say_who = _("Victor")

    vic "\"Although he seems very gentle now, {w=0.5}he was quite aloof to everyone back then.\""

    vic "\"His pretty face may have won the hearts of many girls, {w=0.5}but his cold and arrogant attitude did offend many classmates as well.\""

    show vic_talk at vic_pos
    with Dissolve(0.2)
    hide vic_low_brow_talk

    vic "\"However, {w=0.5}what does remain unchanged is his perseverance and determination.\""

    vic "\"When Vincent was in college, {w=0.5}he had only one goal, {w=0.5}and that was to get his dream job at Myers.\""

    show vic_low_brow_talk at vic_pos
    with Dissolve(0.2)
    hide vic_talk

    vic "\"Then, {w=0.5}he was just as busy as he is now, {w=0.5}always working late into the night to achieve his goals.\""

    show vic_talk at vic_pos
    with Dissolve(0.2)
    hide vic_low_brow_talk

    vic "\"But as you can see, {w=0.5}hard work does pay off - {w=0.5}he is now the {color=#f00}Chief Legal Officer{/color} at Myers.\""

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/hmm.ogg"

    show vic_low_brow_talk at vic_pos
    with Dissolve(0.2)
    hide vic_talk

    pause 0.3

    vic "\"All right, {w=0.5}John. {w=0.5}I think it is time to give you some personal space to finish those tedious courses.\""

    show vic_talk at vic_pos
    with Dissolve(0.2)
    hide vic_low_brow_talk

    vic "\"If you have any questions about the company, {w=0.5}please come by my desk.\""

    vic "\"I hope you enjoy your time in Myers! {w=0.5}I'll see you later.\""

    $ say_who = ""

    window hide

    $ renpy.pause(0.1, hard='True')

    hide vic_talk
    $ renpy.transition(Dissolve(0.2))
    $ renpy.pause(0.2, hard='True')
    hide vic_normal
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    show john_past_vic_office_1:
        ease 1.0 xoffset 0 yoffset -83

    $ renpy.pause(1.0, hard='True')

    window show

    john "Mr. Blake feels like a very easy going boss."

    john "But... {w=0.5}what's his mechanical prosthesis all about? {w=0.5}What has he been through?"

    john "And Mr. Edgeworth too; {w=0.5}what Mr. Blake said made me want to know more about him as well."

    john "......{w=0.5}Anyways, {w=0.5}this is not the time to think about that."

    window hide

    scene john_past_desktop
    $ renpy.transition(Dissolve(2.0))
    $ renpy.pause(2.0, hard='True')

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False

    $ renpy.pause(1.0, hard='True')

    john "Speaking of which, {w=0.5}I haven't even checked out my desk."

    john "It's time to see what's around here."

    $ renpy.music.set_volume(0.5, delay=0, channel='music')
    play music ("music/bgm/jazz-lounge.ogg")

    $ rollback_ = False
    $ renpy.block_rollback()
    $ _rollback = False


    $ john_past_calendar_page = 2
    $ john_past_check_calendar = False
    $ john_past_check_mascot = False

    call screen john_past_tabletop

label john_past_end:

    $ renpy.pause(0.1, hard='True')

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    scene john_past_desktop

    $ renpy.transition(Dissolve(3.0))
    $ renpy.pause(3.0, hard='True')

    $ renpy.music.set_volume(0.3, delay=0, channel='sound')
    play sound ("music/John Past/gossip-whispers.ogg")

    e1 "\"Hey,{w=0.5} did you see Victor's face today?\""

    $ rollback_ = True

    e2 "\"I did.{w=0.5} It was... {w=0.5}really scary.\""

    e2 "\"What happened? {w=0.5}Why is he being so strange today?\""

    e1 "\"Don't you know? {w=0.5}Vincent was in a very serious {color=#f00}car accident{/color} last night on his way to the party. {w=0.5}He is still in critical condition.\""

    e2 "\"Huh!?\""

    stop sound fadeout 4.0

    john "(!?)"

    john "(Mr. Edgeworth?)"

    anon "{color=#f00}\"Oh! {w=0.5}John, {w=0.5}is it?\"{/color}"

    scene john_past_vic_office_1

    show myers_anon
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    pause 1.0

    anon "{color=#f00}\"Hello, {w=0.5}hello! {w=0.5}Please excuse my surprise visit. {w=0.5}I just want to come by and say hi.\"{/color}"

    anon "{color=#f00}\"Are you free after work today? {w=0.5}Would you mind coming to the basement with me for a short conversation?\"{/color}"

    john "\"Err...{w=0.5} and you are?\""

    anon "{color=#f00}\"Oh! {w=0.5}This old brain of mine! {w=0.5}How could I forget to introduce myself?\"{/color}"

    anon "{color=#f00}\"Nice to meet you, {w=0.5}my friend.\"{/color}"

    anon "{color=#f00}\"You can call me... {w=0.5}{size=+8}Monsieur M{/size}.\"{/color}"

    window hide

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/demo end impact.ogg")
    scene black

    $ renpy.pause(1.0, hard='True')
    pause 3.0

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/UI Dark.ogg"

    window show

    noname "Investigation completed. {w=0.5}Successfully entered the Myers lobby."

    window hide

    jump myers_lobby_start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
