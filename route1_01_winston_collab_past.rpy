
image winston_past_mansion_bar_table = "images/winston past/winston_past_mansion_bar_table.png"
image winston_past_mansion_bar_table_blurred = im.Blur("images/winston past/winston_past_mansion_bar_table.png", 1.5)

label winston_collab_past_start:

    pause 2.0

    $ renpy.music.set_volume(0.6, delay=0, channel='music')
    play music "music/myers lobby/lobby horror.ogg"

    pause 3.0

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/engineering room/winston_past_radio-1.ogg"

    radio2 "\"On July 20, {w=0.5}2081, {w=0.5}at approximately 23:00, {w=0.5}several minor explosions occurred near the G4 Central Prison area, {w=0.5}destroying part of the prison wall.\""

    $ rollback_ = True

    play sound "music/engineering room/winston_past_radio-2.ogg"

    radio2 "\"The whereabouts of Winston Loomis, {w=0.5}a former Myers researcher and the mastermind behind the G4 Cyborg Incident, {w=0.5}who was sentenced for life, {w=0.5}remain unknown.\""

    play sound "music/engineering room/winston_past_radio-3.ogg"

    radio2 "\"The possibility that he died in the explosion cannot be ruled out until the site is cleared.\""

    play sound "music/engineering room/winston_past_radio-4.ogg"

    radio2 "\"On July 21, {w=0.5}2081, {w=0.5}the police completed the clean-up of the explosion scene. {w=0.5}Bionic prosthetic fragments and explosives were found, {w=0.5}confirming that Winston had absconded.\""

    play sound "music/engineering room/winston_past_radio-5.ogg"

    radio2 "\"The fugitive is still at large, {w=0.5}and the police have yet to find any information leading to his arrest......\""

    stop music fadeout 2.0

    $ renpy.pause(0.15, hard='True')

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/tv turn off.ogg"

    scene black
    show proto_tv_turn_off

    $ renpy.pause(2.0, hard='True')
    pause 2.0

    $ renpy.music.set_volume(0.6, delay=0, channel='music')
    play music "music/bgm/bizets-habanera.ogg"

    pause 2.0

    scene lobby_bright
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
    show vic_angry_flip at vic_pos_2
    show vin_high_brow_satire at vin_pos_2
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    pause 2.0

    window show

    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/huh.ogg"

    show vic_suspicious_flip at vic_pos_2 with Dissolve(0.2)

    vic "\"My dear Vincent, {w=0.5}tell me. {w=0.5}This news doesn't happen to be connected to you in any way, {w=0.5}does it?\""

    window hide

    pause 1.0

    $ say_who = _("Vincent")

    window show

    vin "\"......\""

    show vin_rebellious at vin_pos_2
    hide vin_high_brow_satire
    with Dissolve(0.2)

    vin "\"......\""

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/vin_hmm.ogg"

    show vin_high_brow_satire at vin_pos_2
    hide vin_rebellious
    with Dissolve(0.2)

    vin "\"...I have no knowledge of this. {w=0.5}I've only just heard about the news as well.\""

    $ say_who = ""

    window hide

    hide vic_suspicious_flip with Dissolve(0.2)

    pause 1.0

    window show

    $ say_who = _("Victor")

    vic "\"......\""

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/hmm.ogg"

    show vic_suspicious_flip at vic_pos_2
    hide vic_angry_flip
    with Dissolve(0.2)

    vic "\"Oh? {w=0.5}Is that so?\""

    vic "\"Then would you mind explaining to me...\""

    show vic_suspicious_flip:
        linear 0.3 xpos 0.18

    show vin_high_brow_satire:
        linear 0.3 xpos 0.78

    $ renpy.pause(0.1, hard='True')

    show winston_normal
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/shake.ogg"

    show vic_mad_flip at vic_pos_3
    hide vic_suspicious_flip

    vic "{size=+8}\"How this man is right here in your mansion!?\"{/size}" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    show vin_rebellious behind winston_normal at vin_pos_3
    hide vin_high_brow_satire
    with Dissolve(0.2)

    $ say_who = _("Vincent")

    vin "\"......\""

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/Vincent.ogg"

    show vin_smile behind winston_normal at vin_pos_3
    hide vin_rebellious
    with Dissolve(0.2)

    vin "\"I just happened to run into Mr. Loomis on my way back.\""

    vin "\"What an amazing twist of fate. {w=0.5}Wouldn't you agree, {w=0.5}Mr. Loomis?\""

    window hide

    show vin_normal behind winston_normal at vin_pos_3
    hide vin_smile
    with Dissolve(0.2)

    pause 1.0

    $ say_who = ""

    window show

    win "\"......\""

    vic "\"......\""

    vin "\"......\""

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/winston/cough1.ogg"

    show winston_talk
    hide winston_normal
    with Dissolve(0.2)

    win "\"...*cough*.\""

    show vin_rebellious behind winston_talk at vin_pos_3
    hide vin_normal
    with Dissolve(0.2)

    vin "\"......\""

    jump winston_intro

label win_intro_end:

    hide winston_talk
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    show vic_mad_flip:
        linear 0.3 xpos 0.25

    show vin_rebellious:
        linear 0.3 xpos 0.73

    pause 1.0

    window show

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/hmm.ogg"

    vic "\"Oh? {w=0.5}Quite the twist of fate indeed.\""

    vic "\"My dear Vincent Edgeworth, {w=0.5}don't you know that Winston should be rotting in prison right now?\""

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/vin_hmm.ogg"

    show vin_annoyed_and_embarassed at vin_pos_2
    hide vin_rebellious
    with Dissolve(0.2)

    vin "\"What can I say? {w=0.5}Sometimes I don't pay much attention to such miniscule details.\""

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/shake.ogg"


    show vic_mad_flip at vic_pos_2
    show vic_mad_2_flip at vic_pos_2

    $ say_who = _("Victor")

    vic "\"Not paying much attention!?\"" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    vic "\"You can't be serious! {w=0.5}Have you forgotten that you were the one who put Winston in prison!?\""

    hide vic_mad_2_flip
    show vin_thoughtful at vin_pos_2
    with Dissolve(0.2)

    $ say_who = ""

    vic "\"...Vincent, {w=0.5}look me in the eyes.\""

    vic "\"You might have always been good at lying to other people.\""

    vic "\"But we both know very well that you could never do it in front of me.\""

    vic "\"You've always been like that. {w=0.5}And this is no exception.\""

    window hide

    pause 1.0

    window show

    $ say_who = _("Vincent")

    vin "\"......\""

    hide vin_thoughtful
    with Dissolve(0.2)

    $ say_who = ""

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/vin_hmm.ogg"

    vin "\"I have no idea what you're talking about. {w=0.5}I've been looking you in the eyes this whole time.\""

    show vic_angry_flip at vic_pos_2
    with Dissolve(0.2)

    vic "\"...No you haven't.\""

    show vin_annoyed_and_embarassed_2 at vin_pos_2
    with Dissolve(0.2)

    vin "\"I have.\""

    hide vic_angry_flip
    with Dissolve(0.2)

    vic "\"You haven't.\""

    show vin_angry at vin_pos_2
    with Dissolve(0.2)

    vin "\"I have.\""

    vic "\"......\""

    vin "\"......\""

    vic "\"......\""

    stop music fadeout 6.0

    vin "\"......\""

    vic "\"......\""

    vin "\"......\""

    window hide

    pause 2.0

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/hmm.ogg"

    show vic_hopeless_flip at vic_pos_2
    hide vic_mad_flip
    with Dissolve(0.2)

    pause 0.5

    window show

    $ say_who = _("Victor")

    vic "\"*sigh* {w=0.5}You know, {w=0.5}my friend.\""

    vic "\"I would always support you no matter what choice you make.\""

    show vin_slight_embarassed at vin_pos_2
    hide vin_annoyed_and_embarassed
    hide vin_annoyed_and_embarassed_2
    with Dissolve(0.2)

    vic "\"And I always have, {w=0.5}ever since we met each other in college.\""

    show vic_angry_flip at vic_pos_2
    hide vic_hopeless_flip
    with Dissolve(0.2)

    vic "\"But all of this, {w=0.5}it's just pure madness.\""

    show vic_angry_close_eye_flip at vic_pos_2
    hide vic_angry_flip
    with Dissolve(0.2)

    vic "\"I understand. {w=0.5}What Myers did to you is absolutely unforgivable.\""

    show vic_angry_flip at vic_pos_2
    hide vic_angry_close_eye_flip
    with Dissolve(0.2)

    vic "\"But do you realize that there's also no turning back to the path you're going?\""

    vic "\"The moment you choose revenge, {w=0.5}you are no longer different from your enemies.\""

    show vic_angry_close_eye_flip at vic_pos_2
    hide vic_angry_flip
    with Dissolve(0.2)

    vic "\"Vincent Edgeworth. {w=0.5}It is already a miracle that you survived from that disaster.\""

    show vic_angry_flip at vic_pos_2
    hide vic_angry_close_eye_flip
    with Dissolve(0.2)

    vic "\"You could still achieve so much in your future. {w=0.5}Do you really want to be at war with Myers forever?\""

    vic "\"Do you really think you can take on the entire Myers Corporation on your own?\""

    $ say_who = ""

    vic "\"Don't be ridiculous. {w=0.5}You are just sacrificing your life for nothing.\""

    window hide

    pause 2.0
    $ renpy.pause(0.1, hard='True')

    show vin_dark at vin_pos_2
    hide vin_slight_embarassed
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    pause 1.0

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music "music/bgm/ankari-sad.ogg"

    $ renpy.pause(3.0, hard='True')
    pause 2.0

    window show

    vin "\"......\""

    vin "\"...Then join me, {w=0.5}Victor.\""

    show vic_suspicious_flip at vic_pos_2
    hide vic_angry_flip
    with Dissolve(0.2)

    vic "\"What?\""

    show vin_thoughtful at vin_pos_2
    hide vin_dark
    with Dissolve(0.2)

    vin "\"Then join me. {w=0.5}I need you.\""

    show vic_surprised_flip at vic_pos_2
    hide vic_suspicious_flip
    with Dissolve(0.2)

    vic "\"......\""

    $ say_who = _("Vincent")

    vin "\"I may look like an idiot who's in over his head to you.{w=0.5} But I just no longer wish to be pushed around.\""

    vin "\"Do you really think Myers is going to let me go after all of that?\""

    vin "\"If I choose to do nothing now, {w=0.5}I will definitely be dead sooner or later.\""

    vin "\"But if I succeed in mastering this technology, {w=0.5}I can become the one in charge. {w=0.5}I can become better than Myers.\""

    show vin_satire at vin_pos_2
    hide vin_thoughtful
    with Dissolve(0.2)

    vin "\"You are right, {w=0.5}Victor. {w=0.5}I can't do that on my own.\""

    vin "\"I need the mind of Winston Loomis. {w=0.5}But beyond that, {w=0.5}{color=#f00}I need another man{/color}.\""

    $ say_who = ""

    vin "\"Someone I know I can trust, {w=0.5}someone I know I can entrust my life to.\""

    window hide

    pause 2.0

    window show

    $ say_who = _("Victor")

    vic "\"......\""

    show vic_hopeless_flip at vic_pos_2
    hide vic_surprised_flip
    with Dissolve(0.2)

    vic "\"Vincent, {w=0.5}have you gone mad? {w=0.5}Don't you realize who I am?\""

    $ say_who = ""

    vic "\"Do you understand how dangerous a decision like this is?\""

    show vin_thoughtful at vin_pos_2
    hide vin_satire
    with Dissolve(0.2)

    $ say_who = _("Vincent")

    vin "\"I believe the world is in equilibrium. {w=0.5}A dynamic equilibrium.\""

    vin "\"And eventually, {w=0.5}you will realize that good and evil are but two changing rhythms.\""

    show vin_melancholy at vin_pos_2
    hide vin_thoughtful
    with Dissolve(0.2)

    $ say_who = ""

    vin "\"I trust you, {w=0.5}Victor. {w=0.5}And I'm sure we can find the equilibrium that's just right.\""

    vic "\"......\""

    window hide

    pause 3.0

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/hmm.ogg"

    show vic_low_brow_talk_flip at vic_pos_2
    hide vic_hopeless_flip
    with Dissolve(0.5)

    window show

    $ say_who = _("Victor")

    vic "\"*sigh* {w=0.5}That's right. {w=0.5}How could I forget?\""

    vic "\"{color=#f00}Vincent Edgeworth never regrets his choice.{/color}\""

    vic "\"But it's been a long time since I've seen you like that.\""

    show vic_accepting_flip at vic_pos_2
    hide vic_low_brow_talk_flip
    with Dissolve(0.5)

    vic "\"It's going to be an incredibly long and difficult path. {w=0.5}But this time, {w=0.5}Vincent Edgeworth, {w=0.5}I'm willing to walk alongside you.\""

    $ say_who = ""

    show vin_slight_embarassed at vin_pos_2
    hide vin_melancholy
    show vic_low_brow_flip at vic_pos_2
    hide vic_accepting_flip
    with Dissolve(0.2)

    vin "\"......\""

    vin "\"...Thank you, {w=0.5}Victor.\""

    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/huh.ogg"

    show vic_talk_flip at vic_pos_2
    hide vic_low_brow_flip
    with Dissolve(0.2)

    vic "\"What did you say? {w=0.5}I couldn't hear you.\""

    show vin_annoyed_and_embarassed at vin_pos_2
    hide vin_slight_embarassed
    show vic_normal_flip at vic_pos_2
    hide vic_talk_flip
    with Dissolve(0.2)

    vin "\"...I said- {w=0.5}Thank you.\""

    stop music fadeout 4.0

    hide vic_normal_flip
    hide vin_annoyed_and_embarassed
    hide vin_angry

    show vic_surprised_flip at vic_pos_2
    show vin_surprised at vin_pos_2
    with Dissolve(0.2)

    $ renpy.pause(0.1, hard='True')

    show vic_surprised_flip:
        linear 0.3 xpos 0.18

    show vin_surprised:
        linear 0.3 xpos 0.78

    $ renpy.pause(0.1, hard='True')

    show winston_normal
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ say_who = _("Winston")

    win "\"......\""

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/winston/cough1.ogg"

    show winston_talk
    hide winston_normal
    with Dissolve(0.2)

    win "\"...*cough*\""

    vin "\"......\""

    vic "\"......\""

    win "\"......\""

    $ say_who = ""

    $ renpy.music.set_volume(0.8, delay=0, channel='music')
    play music "music/jazz.ogg"

    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/hehe.ogg"

    show vic_talk_flip behind winston_normal at vic_pos_3
    hide vic_surprised_flip
    show winston_normal
    hide winston_talk
    with Dissolve(0.2)

    vic "\"Oh look, {w=0.5}we almost forgot. {w=0.5}Mr. Loomis's been here the whole time.\""

    vic "\"Looks like he's heard everything we've been saying.\""

    vic "\"Speaking of which- {w=0.5}what are you planning to do with this fellow?\""

    show vin_annoyed_and_embarassed behind winston_normal at vin_pos_3
    hide vin_surprised
    show vic_normal_flip behind winston_normal at vic_pos_3
    hide vic_talk_flip
    with Dissolve(0.2)

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/vin_hmm.ogg"

    vin "\"Perhaps we can throw him back in prison.\""

    show vic_talk_flip behind winston_normal at vic_pos_3
    hide vic_normal_flip
    with Dissolve(0.2)

    vic "\"Oh ho ho. {w=0.5}What's the matter, {w=0.5}my dear Vincent?\""

    vic "\"What's that embarrassed look on your face?\""

    show vic_normal_flip behind winston_normal at vic_pos_3
    hide vic_talk_flip
    show vin_angry behind winston_normal at vin_pos_3
    hide vin_annoyed_and_embarassed
    with Dissolve(0.2)

    vin "\"Victor, {w=0.5}that's enough.\""

    show vic_talk_flip behind winston_normal at vic_pos_3
    hide vic_normal_flip
    with Dissolve(0.2)

    vic "\"By the way, {w=0.5}I actually got a surprise for you.\""

    $ renpy.music.set_volume(0.1, delay=0, channel='sound')
    play sound "music/cloth.mp3" fadeout 2.0

    show transparent dark-small:
        alpha 1.0
    with Dissolve(0.5)

    pause 0.5

    show character_icon_box_1:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 700 ypos 50
        xpos 700 ypos 50
    show vin_icon_high_brow_satire:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 700 ypos 48
        xpos 700 ypos 48
    show character_icon_box_2:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 700 ypos 50
        xpos 700 ypos 50

    vin "\"And these are...?\""


    show character_icon_box_1:
        xpos 700 ypos 50
    show vin_icon_high_brow_satire:
        xpos 700 ypos 48
    show character_icon_box_2:
        xpos 700 ypos 50

    show character_icon_box_1 as second_character_icon_box_1:
        xpos -300 ypos 250
        easein_expo 1.0 xpos 200 ypos 250
        xpos 200 ypos 250
    show vic_icon_talk_flip:
        xpos -300 ypos 248
        easein_expo 1.0 xpos 200 ypos 248
        xpos 200 ypos 248
    show character_icon_box_2 as second_character_icon_box_2:
        xpos -300 ypos 250
        easein_expo 1.0 xpos 200 ypos 250
        xpos 200 ypos 250

    vic "\"Some items I brought back from Winston's lab.\""


    show character_icon_box_1 as second_character_icon_box_1:
        xpos 200 ypos 250
    show vic_icon_talk_flip:
        xpos 200 ypos 248
    show character_icon_box_2 as second_character_icon_box_2:
        xpos 200 ypos 250

    vic "\"I secretly broke open one of the drawers there when no one was around.\""

    hide vic_icon_talk_flip
    show vic_icon_normal_flip behind second_character_icon_box_2:
        xpos 200 ypos 248
    show vin_icon_surprised behind character_icon_box_2:
        xpos 700 ypos 48
    hide vin_icon_high_brow_satire
    with Dissolve(0.2)

    vin "\"In other words, {w=0.5}you've known this whole time that Winston's escape from prison was my work?\""

    show vic_icon_talk_flip behind second_character_icon_box_2:
        xpos 200 ypos 248
    hide vic_icon_normal_flip

    $ say_who = _("Victor")

    vic "\"Well, {w=0.5}you could say so.\""

    hide vin_icon_surprised
    show vin_icon_high_brow_satire behind character_icon_box_2:
        xpos 700 ypos 48
    with Dissolve(0.2)

    vic "\"Edgeworth, {w=0.5}why don't you take a moment and look through these?\""

    vic "\"And as for Mr. Loomis, {w=0.5}just leave him to me for the moment.\""

    $ say_who = ""

    stop music fadeout 3.0

    vin "\"......\""

    window hide

    scene black
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    pause 3.0

    $ renpy.music.set_volume(0.5, delay=0, channel='music')
    play music ("music/bgm/jazz-lounge.ogg")

    pause 4.0

    scene winston_past_mansion_bar_table
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    pause 2.0

    show character_icon_box_1:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 800 ypos 50
        xpos 800 ypos 50
    show vin_icon_high_brow_satire:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 800 ypos 48
        xpos 800 ypos 48
    show character_icon_box_2:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 800 ypos 50
        xpos 800 ypos 50

    pause 1.0

    window show

    vin "...Victor Blake."


    show character_icon_box_1:
        xpos 800 ypos 50
    show vin_icon_high_brow_satire:
        xpos 800 ypos 48
    show character_icon_box_2:
        xpos 800 ypos 50

    vin "He intimidates me sometimes."

    vin "He could read my mind without any difficulty, {w=0.5}and could even go as far as to anticipate my every move."

    show vin_icon_satire behind character_icon_box_2:
        xpos 800 ypos 48
    hide vin_icon_high_brow_satire

    vin "He never needed Myers' mechanical prosthesis to be a superhuman. {w=0.5}He already is one."

    vin "Sometimes I can't help but wonder:"

    vin "If I hadn't become friends with him back in college,"

    vin "If I never had him next to me when I needed him,"

    vin "How different would things be now? {w=0.5}Where would I possibly be at this moment?"

    show vin_icon_thoughtful behind character_icon_box_2:
        xpos 800 ypos 48
    hide vin_icon_satire

    vin "......"

    vin "I'd rather not think about it."

    window hide

    show vin_icon_satire behind character_icon_box_2:
        xpos 800 ypos 48
    hide vin_icon_thoughtful
    with Dissolve(0.5)

    pause 1.5

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.pause(0.5, hard='True')

    vin "Time is running out. {w=0.5}I need to carefully examine all the items Victor has brought back."

    hide vin_icon_satire
    hide character_icon_box_1
    hide character_icon_box_2
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.block_rollback()
    $ _rollback = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    jump winston_collab_past_bar_click_start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
