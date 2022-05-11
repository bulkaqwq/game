
image graduation_bar = "images/graduation/graduation_bar.png"
image graduation_tie = "images/graduation/graduation_tie.png"

image chamber_core_members = "images/chamber/chamber-core-members.png"
image chamber_m = "images/chamber/chamber-m.png"
image chamber_cyborg_hand = "images/chamber/chamber-cyborg-hand.png"

label graduation_start:

    $ renpy.free_memory()
    if renpy.is_skipping():
        $ renpy.choice_for_skipping()

    $ _skipping = True

    $ _rollback = True

    $ renpy.pause(2.0, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music ("music/ambience/crowd.ogg") fadein 3.0 fadeout 3.0

    pause 4.0

    window show

    anon "\"Vincent Edgeworth, {w=0.5}is it? {w=0.5}Here's your package. {w=0.5}Have a nice day!\""

    vin "\"Thank you very much.\""

    window hide

    stop music fadeout 3.0

    $ renpy.pause(3.0, hard='True')

    scene dorm1
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

    pause 1.0

    show college_vin_sad
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/dorm/knock door.ogg" fadeout 2.0

    pause 2.0

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/open door.ogg" fadeout 1.0

    show college_vin_sad:
        linear 0.5 xpos 0.73

    $ renpy.pause(1.0, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music ["<silence 1.0>", "music/bgm/dorm.ogg"]
    queue music "music/bgm/dorm.ogg"

    $ renpy.pause(1.0, hard='True')

    show college_vic_normal_flip at vic_pos_2
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.5, hard='True')

    show college_victor_talk_2_flip at vic_pos_2
    hide college_vic_normal_flip
    with Dissolve(0.2)

    window show

    vic "\"Oh, {w=0.5}hey, {w=0.5}Vincent! {w=0.5}There you are. {w=0.5}I was wondering why I hadn't seen you in the library.\""

    show college_victor_low_brow_flip at vic_pos_2
    hide college_victor_talk_2_flip
    with Dissolve(0.2)

    vin "\"......\""

    show college_victor_surprised_flip at vic_pos_2
    hide college_victor_low_brow_flip
    with Dissolve(0.2)

    $ say_who = _("Victor")

    vic "\"...What's wrong, {w=0.5}Vincent? {w=0.5}You look a little down.\""

    show college_victor_talk_2_flip at vic_pos_2
    hide college_victor_surprised_flip
    with Dissolve(0.2)

    vic "\"Let me guess... {w=0.5}Did that international kid from G2 piss you off again?\""

    hide college_victor_talk_2_flip
    show college_victor_low_brow_flip at vic_pos_2
    show college_vin_think at vin_pos_2
    hide college_vin_sad
    with Dissolve(0.2)

    $ say_who = ""

    vin "\"...No.\""

    show college_victor_surprised_flip at vic_pos_2
    hide college_victor_low_brow_flip
    with Dissolve(0.2)

    vic "\"Then what's the matter? {w=0.5}Did something happen?\""

    show college_vin_unpleased2 at vin_pos_2
    hide college_vin_think
    with Dissolve(0.2)

    vin "\"I was hired by the Myers Corporation. {w=0.5}I received my job offer letter from them today.\""

    show college_victor_happy_flip at vic_pos_2
    hide college_victor_surprised_flip
    with Dissolve(0.2)

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/shake.ogg"

    vic "\"Oh, {w=0.5}what did you just say!?\"" with Shake((0.5, 1.0, 0.5, 1.0), 3.0, dist=15)

    vic "\"That's wonderful news, {w=0.5}Vincent! {w=0.5}Congratulations, {w=0.5}we should celebrate!\""

    show college_vin_sad at vin_pos_2
    hide college_vin_unpleased2
    with Dissolve(0.2)

    vin "\"...Uh-huh.\""

    hide college_victor_happy_flip
    show college_victor_surprised_flip at vic_pos_2
    with Dissolve(0.2)

    $ say_who = _("Victor")

    vic "\"......\""

    show college_victor_sad_flip at vic_pos_2
    hide college_victor_happy_flip
    with Dissolve(0.2)

    vic "\"Vincent, {w=0.5}hasn't it been your lifelong dream to work for the Myers Corporation? {w=0.5}Why are you looking so glum?\""

    show college_vin_awk at vin_pos_2
    hide college_vin_sad
    with Dissolve(0.2)

    $ say_who = "Vincent"

    vin "\"Yes, {w=0.5}it is indeed my dream to work at the Myers Corporation. {w=0.5}It's just... {w=0.5}It also means that everything at RMU is about to end.\""

    show college_vin_sad at vin_pos_2
    hide college_vin_awk
    show college_victor_surprised_flip at vic_pos_2
    hide college_victor_sad_flip
    with Dissolve(0.2)

    vin "\"I never thought I would feel such deep sorrow about leaving here. {w=0.5}My four years here have just flown by.\""

    $ say_who = ""

    window hide

    pause 1.0

    window show
    vic "\"......\""
    window hide
    pause 1.0
    window show

    show college_victor_talk_2_flip at vic_pos_2
    hide college_victor_surprised_flip
    with Dissolve(0.2)

    vic "\"Yeah.{w=0.5} It's all coming to an end, {w=0.5}isn't it?\""

    vic "\"I still vividly remember the first day we met. {w=0.5}I can't believe that was four years ago.\""

    show college_victor_low_brow_flip at vic_pos_2
    hide college_victor_talk_2_flip
    with Dissolve(0.2)

    vin "\"......\""

    show college_victor_sad_flip at vic_pos_2
    hide college_victor_low_brow_flip
    with Dissolve(0.2)

    $ say_who = _("Victor")

    vic "\"......\""

    show college_victor_talk_2_flip at vic_pos_2
    hide college_victor_sad_flip
    with Dissolve(0.2)

    vic "\"Speaking of which, {w=0.5}the class will be having a graduation party tonight. {w=0.5}Would you like to come with me, {w=0.5}Vincent?\""

    show college_vin_mad_3 at vin_pos_2
    hide college_vin_sad
    show college_victor_low_brow_flip at vic_pos_2
    hide college_victor_talk_2_flip
    with Dissolve(0.2)

    $ say_who = ""

    vin "\"Not interested.\""

    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/hehe.ogg"

    show college_victor_happy_flip at vic_pos_2
    hide college_victor_low_brow_flip
    with Dissolve(0.2)

    $ say_who = _("Victor")

    vic "\"...Haha. {w=0.5}I'm not surprised at all.\""

    show college_victor_talk_flip at vic_pos_2
    hide college_victor_happy_flip
    with Dissolve(0.2)

    vic "\"You know, {w=0.5}Vincent, {w=0.5}they are all your friends. {w=0.5}There's nothing wrong with seeing them one last time, {w=0.5}wouldn't you agree?\""

    show college_vin_mad at vin_pos_2
    hide college_vin_mad_3
    show college_vic_normal_flip at vic_pos_2
    hide college_victor_talk_flip
    with Dissolve(0.2)

    $ say_who = ""

    vin "\"They are not my friends.\""

    show college_victor_talk_2_flip at vic_pos_2
    hide college_vic_normal_flip
    with Dissolve(0.2)

    vic "\"Maybe you don't feel that way, {w=0.5}but they do. {w=0.5}They see you as their friend.\""

    hide college_victor_talk_2_flip
    show college_victor_low_brow_flip at vic_pos_2
    hide college_vin_mad
    show college_vin_mad_2 at vin_pos_2
    with Dissolve(0.2)

    vin "\"I don't want to be friends with them. {w=0.5}Just having you is enough.\""

    show college_victor_shy_flip at vic_pos_2
    hide college_victor_low_brow_flip
    with Dissolve(0.2)

    vic "\"......\""

    vin "\"......\""

    show college_victor_happy_2_flip at vic_pos_2
    hide college_victor_shy_flip
    with Dissolve(0.2)

    vic "\"......\""

    show college_vin_shy at vin_pos_2
    hide college_vin_mad_2
    with Dissolve(0.2)

    vin "\"......\""

    show college_victor_talk_flip at vic_pos_2
    hide college_victor_happy_2_flip
    with Dissolve(0.2)

    $ say_who = _("Victor")

    vic "\"Then how about just the two of us?\""

    show college_vin_normal at vin_pos_2
    hide college_vin_shy
    with Dissolve(0.2)

    vic "\"Just you and me. {w=0.5}There will be nobody else.\""

    show college_victor_talk_2_flip at vic_pos_2
    hide college_victor_talk_flip
    with Dissolve(0.2)

    vic "\"You're almost out of university, {w=0.5}yet you've never had a drink, {w=0.5}have you?\""

    hide college_victor_talk_2_flip
    show college_victor_talk_flip at vic_pos_2
    with Dissolve(0.2)

    vic "\"My favorite bar is in downtown G4. {w=0.5}Let me take you there, {w=0.5}like a date, {w=0.5}what do you think?\""

    show college_vin_unpleased2 at vin_pos_2
    hide college_vin_normal
    hide college_victor_talk_flip
    show college_vic_normal_flip at vic_pos_2
    with Dissolve(0.2)

    $ say_who = ""

    vin "\"...When?\""

    show college_victor_happy_flip at vic_pos_2
    hide college_vic_normal_flip
    with Dissolve(0.2)

    vic "\"How about 5 o'clock tonight? {w=0.5}I'll drive us there. {w=0.5}Of course, {w=0.5}that also means I won't be able to drink tonight.\""

    hide college_victor_happy_flip
    show college_vic_normal_flip at vic_pos_2
    hide college_vin_unpleased2
    show college_vin_mad at vin_pos_2
    with Dissolve(0.2)

    vin "\"...It's a deal then.\""

    window hide

    pause 1.0

    hide college_vin_mad
    hide college_vic_normal_flip
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    pause 1.0

    show dorm2 behind dust
    $ renpy.transition(Dissolve(3.0))
    $ renpy.pause(3.5, hard='True')

    pause 1.0

    show college_vic_normal_flip at vic_pos_2
    show college_vin_normal at vin_pos_2
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    pause 1.0

    show college_victor_talk_flip at vic_pos_2
    hide college_vic_normal_flip
    with Dissolve(0.2)

    $ say_who = _("Victor")

    window show

    vic "\"Are you ready, {w=0.5}Vincent?\""

    show college_victor_surprised_flip at vic_pos_2
    hide college_victor_talk_flip
    with Dissolve(0.2)

    vic "\"Huh? {w=0.5}Wait a second. {w=0.5}Did you use hair gel on your head?\""

    show college_vin_shy at vin_pos_2
    hide college_vin_normal
    with Dissolve(0.2)

    vin "\"What? {w=0.5}No...\""

    show college_victor_talk_flip at vic_pos_2
    hide college_victor_surprised_flip
    with Dissolve(0.2)

    vic "\"Not only that, {w=0.5}but you've also changed into a new suit!\""

    show college_victor_happy_flip at vic_pos_2
    hide college_victor_talk_flip
    with Dissolve(0.2)

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/shake.ogg"

    vic "\"Pfft hahahaha! {w=0.5}Did you really think this was a date, {w=0.5}Vincent?\"" with Shake((0.5, 1.0, 0.5, 1.0), 3.0, dist=15)

    show college_vin_mad_3 at vin_pos_2
    hide college_vin_shy
    with Dissolve(0.2)

    vin "\"You have some nerve to say that. {w=0.5}Do you really think I can't smell the cologne you're wearing?\""

    show college_victor_talk_2_flip at vic_pos_2
    hide college_victor_happy_flip
    with Dissolve(0.2)

    vic "\"Ha, {w=0.5}haha... {w=0.5}Okay, {w=0.5}you got me there.\""

    hide college_victor_talk_2_flip
    show college_victor_talk_flip at vic_pos_2
    hide college_vin_mad_3
    show college_vin_normal at vin_pos_2
    with Dissolve(0.2)

    vic "\"Anyway, {w=0.5}shall we get going then?\""

    window hide

    $ say_who = ""

    hide college_victor_talk_flip
    show college_vic_normal_flip at vic_pos_2
    with Dissolve(0.2)

    pause 1.0

    stop music fadeout 6.0

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/open door.ogg" fadeout 1.0

    $ renpy.pause(1.0, hard='True')

    scene black
    $ renpy.transition(Dissolve(2.0))
    $ renpy.pause(2.0, hard='True')

    pause 5.0

    $ renpy.music.set_volume(0.5, delay=0, channel='music')
    play music ("music/bgm/jazz-lounge.ogg")

    pause 2.0

    window show

    vin "\"'Did you know? {w=0.5}An estimated 50-80%% of life on Earth is located under the surface of the oceans.'\""

    vin "\"'The oceans contain 99%% of the living space on the planet. {w=0.5}And humans have only explored less than 10%% of that space.'\""

    window hide

    pause 1.0

    scene graduation_bar
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
    show character_icon_box_1:
        xpos 750 ypos 50
    show college_vin_icon_drunk_1:
        xpos 750 ypos 48
    show character_icon_box_2:
        xpos 750 ypos 50
    with Dissolve(1.0)

    window show

    $ say_who = _("Vincent")

    vin "\"'Not only that, {w=0.5}but the oceans account for 96%% of all the water on the surface of the Earth. {w=0.5}And the remainder? {w=0.5}It's all fresh water in the form of rivers, {w=0.5}lakes and ice.'\""

    vin "\"'At the same time, {w=0.5}the ocean absorbs about 25%% of the CO2 emitted into the atmosphere from human activities each year.'\""

    vin "\"'This greatly reduces the impact of greenhouse gas on the climate.'\""

    hide college_vin_icon_drunk_1
    show college_vin_icon_drunk_2 behind character_icon_box_2:
        xpos 750 ypos 48
    with Dissolve(0.2)

    vin "\"'The ocean sure is incredible and full of wonder. {w=0.5}Wouldn't you say so, {w=0.5}Vincent?'\""

    $ say_who = ""

    show character_icon_box_1 as second_character_icon_box_1:
        xpos 200 ypos 250
    show college_vic_icon_happy_flip:
        xpos 200 ypos 248
    show character_icon_box_2 as second_character_icon_box_2:
        xpos 200 ypos 250
    with Dissolve(0.5)

    $ say_who = _("Victor")

    vic "\"Hahaha. {w=0.5}Oh my god, {w=0.5}you sound just like him!\""

    show college_vic_icon_talk_flip behind second_character_icon_box_2:
        xpos 200 ypos 248
    hide college_vic_icon_happy_flip
    show college_vin_icon_drunk_3 behind character_icon_box_2:
        xpos 750 ypos 48
    hide college_vin_icon_drunk_2
    with Dissolve(0.2)

    vic "\"I heard that that guy is getting a PhD after he graduates. {w=0.5}After that, {w=0.5}he's going back to G2 to take over his father's company.\""

    show college_vic_icon_normal_flip behind second_character_icon_box_2:
        xpos 200 ypos 248
    hide college_vic_icon_talk_flip
    show college_vin_icon_drunk_1 behind character_icon_box_2:
        xpos 750 ypos 48
    hide college_vin_icon_drunk_3
    with Dissolve(0.2)

    $ say_who = ""

    vin "\"Oh, {w=0.5}really? {w=0.5}I have absolutely zero interest in knowing his future career plans. {w=0.5}Bartender, {w=0.5}please make me another Martini.\""

    show college_vic_icon_happy_flip behind second_character_icon_box_2:
        xpos 200 ypos 248
    hide college_vic_icon_normal_flip
    show college_vin_icon_drunk_3 behind character_icon_box_2:
        xpos 750 ypos 48
    hide college_vin_icon_drunk_1
    with Dissolve(0.2)



    vic "\"See? {w=0.5}I knew you would enjoy Martinis.\""

    show college_vic_icon_normal_flip behind second_character_icon_box_2:
        xpos 200 ypos 248
    hide college_vic_icon_happy_flip
    show college_vin_icon_drunk_2 behind character_icon_box_2:
        xpos 750 ypos 48
    hide college_vin_icon_drunk_3
    with Dissolve(0.2)

    vin "\"Then what about you, {w=0.5}Victor? {w=0.5}What are your plans after graduation?\""

    show college_vic_icon_close_eye_talk_flip behind second_character_icon_box_2:
        xpos 200 ypos 248
    hide college_vic_icon_normal_flip
    show college_vin_icon_drunk_3 behind character_icon_box_2:
        xpos 750 ypos 48
    hide college_vin_icon_drunk_2
    with Dissolve(0.2)

    vic "\"Like you, {w=0.5}I've been hired by a company. {w=0.5}I will be working at their Investment Department.\""

    show college_vic_icon_normal_flip behind second_character_icon_box_2:
        xpos 200 ypos 248
    hide college_vic_icon_close_eye_talk_flip
    show college_vin_icon_drunk_4 behind character_icon_box_2:
        xpos 750 ypos 48
    hide college_vin_icon_drunk_3
    with Dissolve(0.2)

    vin "\"That's wonderful news to hear, {w=0.5}Victor. {w=0.5}I'm happy for you.\""

    show college_vic_icon_talk_2_flip behind second_character_icon_box_2:
        xpos 200 ypos 248
    hide college_vic_icon_normal_flip
    show college_vin_icon_drunk_5 behind character_icon_box_2:
        xpos 750 ypos 48
    hide college_vin_icon_drunk_4
    with Dissolve(0.2)

    vic "\"Really? {w=0.5}You don't look so happy to me.\""

    show college_vic_icon_low_brow_flip behind second_character_icon_box_2:
        xpos 200 ypos 248
    hide college_vic_icon_talk_2_flip
    show college_vin_icon_drunk_4 behind character_icon_box_2:
        xpos 750 ypos 48
    hide college_vin_icon_drunk_5
    with Dissolve(0.2)

    vin "\"No, {w=0.5}no. {w=0.5}Believe me, {w=0.5}I really am. {w=0.5}It's just that I was thinking...\""

    stop music fadeout 5.0

    vin "\"These may be the final days we get to sit side by side like this.\""

    window hide

    show college_vic_icon_sad_flip behind second_character_icon_box_2:
        xpos 200 ypos 248
    hide college_vic_icon_low_brow_flip
    with Dissolve(0.5)

    pause 1.0

    show college_vin_icon_drunk_5 behind character_icon_box_2:
        xpos 750 ypos 48
    hide college_vin_icon_drunk_4
    with Dissolve(0.5)

    pause 1.0

    window show

    vic "\"......\""

    window hide

    hide college_vin_icon_drunk_5
    hide college_vic_icon_sad_flip
    hide second_character_icon_box_1
    hide second_character_icon_box_2
    hide character_icon_box_1
    hide character_icon_box_2
    with Dissolve(1.0)

    pause 1.0

    show college_victor_sad_flip at vic_pos_2
    show college_vin_sad at vin_pos_2
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    pause 1.0

    hide college_victor_sad_flip
    show college_victor_talk_2_flip at vic_pos_2
    with Dissolve(0.5)

    window show

    vic "\"Guess you're getting too attached to me, {w=0.5}huh? {w=0.5}Does going into the Myers Corporation alone make you nervous?\""

    show college_vin_awk at vin_pos_2
    hide college_vin_sad
    hide college_victor_talk_2_flip
    show college_victor_low_brow_flip at vic_pos_2
    with Dissolve(0.2)

    vin "\"...Sometimes it really feels like you're reading my mind.\""

    hide college_victor_low_brow_flip
    show college_victor_close_eye_3_flip at vic_pos_2
    with Dissolve(0.2)

    vic "\"......\""

    window hide

    $ renpy.music.set_volume(0.7, delay=0, channel='music')
    play music "music/bgm/lonely night.ogg"

    $ renpy.music.set_volume(0.1, delay=0, channel='sound')
    play sound "music/cloth.mp3" fadeout 2.0

    $ renpy.pause(1.0, hard=True)

    show college_vin_awk:
        xpos 0.73 alpha 1
        linear 0.3 xpos 0.78 alpha 1
    show college_victor_close_eye_3_flip:
        xpos 0.25 alpha 1
        linear 0.3 xpos 0.18 alpha 1

    $ renpy.pause(0.3, hard=True)

    show transparent dark-small behind college_vin_awk:
        alpha 0.8
    show graduation_tie
    with Dissolve(0.5)

    pause 0.5

    show college_vin_surprised at vin_pos_3
    hide college_vin_awk
    with Dissolve(0.2)

    window show

    vin "\"Huh? {w=0.5}What's this?\""

    $ say_who = _("Victor")

    show college_victor_talk_2_flip at vic_pos_3
    hide college_victor_close_eye_3_flip
    with Dissolve(0.2)

    vic "\"A graduation present from me.\""

    vic "\"Since you're going to be working at the Myers Corporation, {w=0.5}I thought you would maybe consider changing your outfit?\""

    show college_victor_happy_flip at vic_pos_3
    hide college_victor_talk_2_flip
    with Dissolve(0.2)

    vic "\"A black tie gives a more professional feel, {w=0.5}don't you think?\""

    show college_vin_happy at vin_pos_3
    hide college_vin_surprised
    with Dissolve(0.2)

    $ say_who = ""

    vin "\"...Thank you, {w=0.5}Victor. {w=0.5}I will treasure it.\""

    window hide

    hide transparent dark-small
    hide graduation_tie
    with Dissolve(0.5)

    show college_vin_happy:
        linear 0.3 xpos 0.73 alpha 1
    show college_victor_happy_flip:
        linear 0.3 xpos 0.25 alpha 1
    $ renpy.pause(0.3, hard=True)

    show college_victor_close_eye_3_flip at vic_pos_2
    hide college_victor_happy_flip
    with Dissolve(0.5)

    pause 0.5

    show college_victor_talk_2_flip at vic_pos_2
    hide college_victor_close_eye_3_flip
    with Dissolve(0.5)

    window show

    vic "\"Listen, {w=0.5}my friend. {w=0.5}What I'm going to say next... {w=0.5}may sound a little cheesy, {w=0.5}but these are all words that come from the bottom of my heart.\""

    vic "\"Do you remember the day we first met each other? {w=0.5}In our dorm?\""

    show college_victor_low_brow_flip at vic_pos_2
    hide college_victor_talk_2_flip
    show college_vin_close_eye at vin_pos_2
    hide college_vin_happy
    with Dissolve(0.2)

    vin "\"...How could I ever forget?\""

    show college_vin_normal at vin_pos_2
    hide college_vin_close_eye
    show college_victor_close_eye_talk_2_flip at vic_pos_2
    hide college_victor_low_brow_flip
    with Dissolve(0.2)

    $ say_who = _("Victor")

    vic "\"To tell the truth, {w=0.5}I never thought we would become best friends when I met you that day.\""

    vic "\"I know, {w=0.5}I did say to you that I was sure we would become great friends.\""

    hide college_victor_close_eye_talk_2_flip
    show college_victor_talk_2_flip at vic_pos_2
    with Dissolve(0.2)

    vic "\"However, {w=0.5}I didn't really mean it at that time.\""

    show college_victor_close_eye_talk_2_flip at vic_pos_2
    hide college_victor_low_brow_flip
    with Dissolve(0.2)

    vic "\"But you've changed me so much in the last four years. {w=0.5}Perhaps you don't even realize it yourself.\""

    show college_vin_surprised at vin_pos_2
    hide college_vin_normal
    hide college_victor_close_eye_talk_2_flip
    show college_victor_talk_2_flip at vic_pos_2
    with Dissolve(0.2)

    vic "\"Every second I'm with you, {w=0.5}I feel like my life is full of meaning. {w=0.5}You've helped me regain my purpose.\""

    vic "\"I want to be an outstanding person like you, {w=0.5}Vincent. {w=0.5}But more importantly...\""

    show college_victor_close_eye_talk_2_flip at vic_pos_2
    hide college_victor_talk_2_flip
    with Dissolve(0.2)

    vic "\"I want to stay with you, {w=0.5}and keep being there for you.\""

    hide college_victor_close_eye_talk_2_flip
    show college_victor_talk_2_flip at vic_pos_2
    with Dissolve(0.2)

    vic "\"I'm sure that you'll achieve so many great things when you enter the Myers Corporation,\""

    show college_victor_happy_flip at vic_pos_2
    hide college_victor_talk_2_flip
    with Dissolve(0.2)

    vic "\"Because I know you, {w=0.5}and I know that there's nothing Vincent Edgeworth can't possibly do.\""

    show college_victor_close_eye_talk_2_flip at vic_pos_2
    hide college_victor_happy_flip
    with Dissolve(0.2)

    vic "\"But I also can't deny that your journey at the Myers Corporation won't always be smooth.\""

    vic "\"You're going to face all kinds of challenges and inevitably setbacks, {w=0.5}some big, {w=0.5}some small.\""

    hide college_victor_close_eye_talk_2_flip
    show college_victor_talk_2_flip at vic_pos_2
    with Dissolve(0.2)

    vic "\"But I want you to know that,\""

    vic "\"Whenever you feel overwhelmed and need a hand, {w=0.5}whenever you need someone to reflect on the ups and downs of life with,\""

    window hide

    $ renpy.music.set_volume(0.1, delay=0, channel='sound')
    play sound "music/cloth.mp3" fadeout 2.0

    hide college_victor_talk_2_flip
    hide college_vin_surprised
    with Dissolve(0.5)

    show transparent dark-small:
        alpha 0.8
    with Dissolve(1.0)

    show character_icon_box_1 as second_character_icon_box_1:
        xpos 200 ypos 250
    show college_vic_icon_happy_flip:
        xpos 200 ypos 248
    show character_icon_box_2 as second_character_icon_box_2:
        xpos 200 ypos 250
    with Dissolve(0.5)

    window show

    vic "\"You'll have a dear friend... {w=0.5}{color=#f00}always waiting for you at the Investment Department at the Myers Corporation.{/color}\""

    pause 0.2

    show character_icon_box_1:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 800 ypos 50
        xpos 800 ypos 50
    show college_vin_icon_surprised:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 800 ypos 48
        xpos 800 ypos 48
    show character_icon_box_2:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 800 ypos 50
        xpos 800 ypos 50

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/shock2.ogg" fadeout 2.0

    vin "\"...Could, {w=0.5}could this be!?\"" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    hide college_vic_icon_happy_flip
    show college_vic_icon_talk_2_flip:
        xpos 200 ypos 248
    with Dissolve(0.2)

    vic "\"My job offer letter from the Myers Corporation.\""

    hide college_vic_icon_talk_2_flip
    show college_vic_icon_talk_flip:
        xpos 200 ypos 248
    with Dissolve(0.2)

    vic "\"I'm sorry, {w=0.5}Vincent Edgeworth. {w=0.5}I'm afraid you're not getting rid of me yet.\""

    window hide

    $ say_who = ""

    scene black with Dissolve(1.0)

    pause 3.0

    window show

    vic "\"...Vin - {w=0.5}Vincent!?\""

    vic "\"Are you crying!?\""

    window hide

    pause 2.0

    window show

    vin "Nothing is predestined in life."

    vin "I've always believed that ever since I was a child."

    vin "A person's destiny can be changed by no one but themselves."

    vin "But at that moment, {w=0.5}I finally realized: {w=0.5}I was wrong. {w=0.5}So terribly wrong."

    vin "The day we met at RMU,"

    vin "The moment he entered my life,"

    vin "Everything was destined to change."

    vin "Coming to RMU was my fate. {w=0.5}Meeting him was my fate. {w=0.5}Getting to know him was my fate."

    window hide

    pause 1.0

    window show

    vic "\"I just remembered that there is a pet store near the bar. {w=0.5}Want to go see some kittens?\""

    window hide

    pause 2.0

    stop music fadeout 5.0

    vin "But just as one person is enough to transform your life,"

    vin "A corporation full of sin is also enough to take everything away from you."

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music "music/ambience/mic horror ambience 3.ogg"

    pause 4.0

    $ renpy.free_memory()

    window show

    anon "{color=#f00}\"Vincent, {w=0.5}the company is in big trouble.\"{/color}"

    anon "{color=#f00}\"You have to make them believe that it's all his fault, {w=0.5}or this might be over for us.\"{/color}"

    window hide

    pause 4.0

    window show

    vin "My name is Vincent Edgeworth. {w=0.5}I am a former attorney at the Myers Corporation."

    vin "To many people, {w=0.5}an attorney stands for law and justice, {w=0.5}yet my life is filled with nothing but sin."

    vin "I do whatever it takes to achieve my aims. {w=0.5}Forged evidence, {w=0.5}bribery, {w=0.5}everything."

    vin "Sounds selfish, {w=0.5}doesn't it?"

    vin "But it was all for the best of my company. {w=0.5}My one and only dream company."

    vin "I've never lost a single case I've taken on. {w=0.5}Even this one."

    window hide

    pause 1.0

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ["music/car crash.ogg"]

    show red-bg
    $ renpy.transition(Dissolve(0.3))
    $ renpy.pause(0.3, hard='True')

    hide red-bg
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.pause(1.5, hard='True')

    vin "Yet the company paid me back by trying to kill me in a car accident."

    pause 2.0

    show red-bg
    $ renpy.transition(Dissolve(0.3))
    $ renpy.pause(0.3, hard='True')

    hide red-bg
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.pause(1.0, hard='True')

    window show

    vin "\"Uhhh...{w=0.5} Ahhhh...\""

    window hide

    pause 1.0

    vin "Pain. {w=0.5}Every single bone in my body was crushed."

    vin "Crimson blood filled my vision."

    vin "But somehow, {w=0.5}I survived."

    vin "The next thing I remember, {w=0.5}I was laying on a piece of cold metal. {w=0.5}My body couldn't move, {w=0.5}but I could faintly hear voices around me."

    pause 2.0

    window show

    anon "{color=#f00}\"Remove the organs. {w=0.5}Begin implanting the endoskeleton.\"{/color}"

    window hide

    pause 0.5

    $ renpy.music.set_volume(0.7, delay=0, channel='sound')
    play sound "music/basement/zs_saw.ogg" fadeout 1.0

    show red-bg
    $ renpy.transition(Dissolve(0.3))
    $ renpy.pause(0.3, hard='True')

    hide red-bg
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.pause(1.0, hard='True')

    window show

    vin "\"Ahhh...{w=0.5} Uhhhh...\""

    window hide

    pause 2.0

    vin "I wanted to struggle, {w=0.5}I wanted to scream. {w=0.5}But all I could do was watch it happen."

    scene basement_chamber
    show memory_frame:
        linear 1.0 alpha 0.3
        linear 1.0 alpha 1
        repeat
    with Dissolve(1.0)

    pause 1.0

    vin "After hours of operation, {w=0.5}I was placed inside the secret chamber."

    show chamber_core_members behind memory_frame:
        alpha 0
        linear 1.0 alpha 1

    vin "Countless tubes penetrated my torso. {w=0.5}Standing in front of me were the core members of the Myers Corporation."

    vin "No, {w=0.5}there was another figure. {w=0.5}A figure that seemed so familiar, {w=0.5}but at the same time different."

    show chamber_m behind memory_frame
    with Dissolve(1.0)

    pause 1.0

    window show

    vin "\"Mr. My - {w=0.5}Myers?\""

    m "\"Feed him.\""

    window hide

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/basement/zs_drop.ogg"
    with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    pause 1.0

    vin "A piece of raw meat was thrown in front of me. {w=0.5}Human flesh."

    show red-bg
    $ renpy.transition(Dissolve(0.3))
    $ renpy.pause(0.3, hard='True')

    hide red-bg
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    vin "I felt disgusted. {w=0.5}But I couldn't help but engulf it."

    m "\"Leave him in the chamber and observe his behavior.\""

    anon "\"Yes, {w=0.5}Monsieur M.\""

    hide chamber_m with Dissolve(1.0)

    vin "\"Wait, {w=0.5}don't go...\""

    show chamber_m with Dissolve(1.0)

    vin "\"Tell me... {w=0.5}Why? {w=0.5}Why are you doing this?\""

    vin "\"I did everything you asked... {w=0.5}I devoted everything I had to this company...\""

    pause 0.5

    m "\"......\""

    m "\"I know, {w=0.5}Vincent. {w=0.5}I know.\""

    m "\"I've seen all your efforts.\""

    m "\"And that's why I know, {w=0.5}you would be willing to take this little pain for the company too, {w=0.5}wouldn't you?\""

    hide chamber_m with Dissolve(1.0)

    vin "\"No...{w=0.5} No...\""

    m "\"Goodbye, {w=0.5}Vincent Edgeworth. {w=0.5}I hope you survive.\""

    vin "\"No...{w=0.5} No!!!!!!!!\""

    scene black with Dissolve(1.0)

    pause 1.0

    window show

    vin "I don't remember how long I was kept there."

    vin "Every day, {w=0.5}every second in the chamber felt so long."

    vin "Revolting chunks of flesh, {w=0.5}torn skin, {w=0.5}and the unbearable pain..."

    vin "I felt that living was worse than death. {w=0.5}I just wanted everything to be over."

    window hide

    pause 1.0

    stop music fadeout 5.0

    scene basement_chamber
    show memory_frame:
        linear 1.0 alpha 0.3
        linear 1.0 alpha 1
        repeat
    with Dissolve(1.0)

    pause 1.0

    window show

    vin "\"......\""

    window hide

    pause 0.5

    $ renpy.music.set_volume(0.1, delay=0, channel='sound')
    play sound "music/cloth.mp3" fadeout 2.0

    show chamber_cyborg_hand
    with Dissolve(1.0)

    pause 2.0

    window show

    vin "My black tie. {w=0.5}It had long been stained crimson with blood."

    vin "\"Victor... {w=0.5}I wonder how that guy is doing now.\""

    vin "\"What would he think if he sees the monster I've become?\""

    vin "\"......\""

    window hide

    $ renpy.music.set_volume(0.8, delay=0, channel='music')
    play music ["<silence 2.0>", "music/bgm/hl_song3.ogg"] fadeout 6.0

    pause 1.0

    scene black with Dissolve(1.0)

    vin "\"Is this all part of my fate?\""

    vin "\"To join the Myers Corporation alongside him, {w=0.5}but then never be able to see him again.\""

    vin "\"I'm the naive one after all.\""

    vin "\"This entire time, {w=0.5}I was just another one of Myers' pawns. {w=0.5}I was never truly accepted by them.\""

    pause 0.5

    scene lobby_bright
    show vic_low_brow_talk at vic_pos
    show memory_frame:
        linear 1.0 alpha 0.3
        linear 1.0 alpha 1
        repeat
    $ renpy.transition(Fade(.2, 0, 0.25, color="#fff"))
    $ renpy.pause(0.5, hard='True')

    window show

    $ say_who = _("Victor")

    vic "\"Huh? {w=0.5}You're asking me if a person's fate could possibly be changed?\""

    show vic_talk behind memory_frame at vic_pos
    hide vic_low_brow_talk
    with Dissolve(0.2)

    vic "\"If I have to be honest, {w=0.5}I can't give you an exact answer either.\""

    show vic_accepting behind memory_frame at vic_pos
    hide vic_talk
    with Dissolve(0.2)

    vic "\"But what I do know is, {w=0.5}if that man is Vincent Edgeworth, {w=0.5}then he will never let anyone dictate his destiny.\""

    window hide

    $ say_who = ""

    scene basement_chamber
    show chamber_cyborg_hand
    show memory_frame:
        linear 1.0 alpha 0.3
        linear 1.0 alpha 1
        repeat
    $ renpy.transition(Fade(.2, 0, 0.25, color="#fff"))
    $ renpy.pause(0.5, hard='True')

    pause 1.0

    vin "\"...No. {w=0.5}Destiny or not, {w=0.5}this isn't the ending I wanted.\""

    vin "\"They can crush every bone in my body and slice off every inch of my skin,\""

    vin "\"But I, {w=0.5}Vincent Edgeworth, {w=0.5}cannot accept spending the rest of my life here in this rotting, {w=0.5}reeking chamber.\""

    vin "\"I have so much more to achieve, {w=0.5}and I have so many things that I want to see again.\""

    vin "\"Even if I am no longer human, {w=0.5}even if it's no longer possible for me to return to a normal life,\""

    vin "\"As long as I have one last gasp... {w=0.5}I will claw my way back through hell.\""

    stop music fadeout 7.0

    scene black with Dissolve(1.0)

    pause 1.0

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/monster moan 2.ogg"

    $ renpy.pause(3.0, hard=True)

    vin "\"No... {w=0.5}That's not enough.\""

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/basement/zs_break_bone.ogg"

    show blood-2:
        alpha 1
        0.3
        linear 0.3 alpha 0
        1.0
        alpha 1
        0.3
        linear 0.3 alpha 0
        1.5
        alpha 1
        0.3
        linear 0.3 alpha 0
        1.3
        alpha 1
        0.3
        linear 0.3 alpha 0
    show red-bg:
        alpha 0
        linear 0.3 alpha 1
        linear 0.5 alpha 0
        0.8
        linear 0.3 alpha 1
        linear 0.5 alpha 0
        1.3
        linear 0.3 alpha 1
        linear 0.5 alpha 0
        1.0
        linear 0.3 alpha 1
        linear 0.5 alpha 0

    vin "\"I will make every core member get what they deserve...\""

    vin "\"I will let them know what it feels like to have their bodies torn apart...\""

    vin "{color=#f00}\"I will make Myers Corporation... {w=0.5}pay a painful price.\"{/color}"

    scene black
    show white back
    $ renpy.transition(Dissolve(0.1))
    $ renpy.pause(0.1, hard='True')

    stop music

    $ renpy.music.set_volume(0.7, delay=0, channel='sound')
    play sound "music/teleport.ogg"

    $ renpy.music.set_volume(1.0, delay=0, channel='robot memory')
    $ renpy.music.play("music/magic teleport.ogg", channel="robot memory", loop=False)

    $ renpy.pause(0.3, hard='True')

    hide white back
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    jump vincent_battle_start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
