image myers_lobby_blurred = im.Blur("images/Myers Lobby/myers lobby.png", 4.0)
image myers_lobby = "images/Myers Lobby/myers lobby.png"
image myers_lobby_side_gate = "images/Myers Lobby/myers lobby side gate.png"

image myers_lobby_with_draco_glitch_1 = "images/Myers Lobby/myers lobby with draco glitch 1.jpg"
image myers_lobby_with_draco_glitch_2 = "images/Myers Lobby/myers lobby with draco glitch 2.jpg"

image myers_lobby_draco_glitch:

    "images/Myers Lobby/glitches/glitch 1.png"
    pause 1.0
    "images/Myers Lobby/glitches/glitch 3.png"
    pause 1.0
    "images/Myers Lobby/glitches/glitch 4.png"
    pause 1.0
    "images/Myers Lobby/glitches/glitch 2.png"
    pause 1.0
    repeat

label myers_lobby_start:

    $ renpy.free_memory()

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = True

    $ renpy.pause(3.0, hard=True)

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/myers lobby/draco footstep.ogg"

    $ renpy.pause(5.0, hard='True')

    $ renpy.pause(4.0, hard=True)

    stop sound fadeout 1.0

    anon "\"Lady [name!t]?\""

    $ renpy.pause(2.0, hard=True)

    van "\"......\""

    $ renpy.pause(2.0, hard=True)

    anon "\"Lady [name!t]? {w=0.5}With all due respect, {w=0.5}napping here is not the most sensible choice.\""

    $ renpy.pause(1.0, hard='True')

    scene myers_lobby
    show myers_lobby_blurred
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

    show draco_fisheye_2 onlayer front:
        xalign 0.5 yalign 0.5 alpha 0
    show draco_fisheye_blurred onlayer front:
        xalign 0.5 yalign 0.5
    $ renpy.transition(Dissolve(3.0))
    $ renpy.pause(3.0, hard='True')

    pause 2.0

    van "\"......?\""

    van "\"What... {w=0.5}what happened?\""

    pause 1.0
    $ renpy.pause(0.1, hard='True')

    hide draco_fisheye_blurred onlayer front
    hide myers_lobby_blurred
    show draco_fisheye_2 onlayer front:
        xalign 0.5 yalign 0.5 alpha 1
    $ renpy.transition(Dissolve(3.0))
    $ renpy.pause(3.0, hard='True')

    pause 1.0

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/draco/huh huh.mp3"

    show draco_fisheye onlayer front:
        xalign 0.5 yalign 0.5 alpha 1
    hide draco_fisheye_2 onlayer front
    $ renpy.transition(Dissolve(0.2))
    $ renpy.pause(0.2, hard='True')

    anon "\"Good evening, {w=0.5}my dear [name!t].\""

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/shock2.ogg" fadeout 2.0

    van "!?" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    hide draco_fisheye onlayer front
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    $ renpy.music.set_volume(0.8, delay=0, channel='music')
    play music "music/myers lobby/deeranic.ogg"

    pause 2.0
    $ renpy.pause(0.1, hard='True')

    show draco_drop_shadow at dra_pos_1
    show draco_normal at dra_pos_1
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    pause 1.0

    show draco_talk at dra_pos_1
    with Dissolve(0.2)

    window show

    anon "\"It is {color=#f00}an incredible chance of fate {/color}for us to meet each other in such a desolate place, {w=0.5}don't you think?\""

    hide draco_talk with Dissolve(0.2)

    van "What appeared in front of me was a dark-haired young man who was dressed formally and elegantly."

    van "He looked {color=#f00}very similar to Vincent {/color}in appearance, {w=0.5}but much younger."

    van "\"...Would you mind telling me who you are?\""

    $ say_who = "???"

    anon "\"......\""

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/draco/hmm.mp3"

    show draco_close_eye_talk at dra_pos_1
    hide draco_normal
    with Dissolve(0.2)

    anon "\"It seems inevitable, {w=0.5}doesn't it?\""

    hide draco_close_eye_talk
    show draco_normal at dra_pos_1
    show draco_talk at dra_pos_1
    with Dissolve(0.2)

    anon "\"Only in youth does coincidence seem the same as fate.{w=0.5} Later, {w=0.5}we know that the real course of our lives is decided within us.\""

    hide draco_talk with Dissolve(0.2)

    $ say_who = ""

    van "\"......\""

    van "(You don't look so old yourself...)"

    show draco_talk at dra_pos_1 with Dissolve(0.2)

    anon "\"I am {color=#f00}Mr. Edgeworth's butler{/color}. {w=0.5}You can call me {color=#f00}Draco{/color}.\""

    hide draco_talk with Dissolve(0.2)

    jump draco_intro

label draco_intro_end:


    van "\"Vincent's butler? {w=0.5}So you're the one who saved me?\""

    van "\"You were also the one I saw earlier in the passageway, {w=0.5}weren't you?\""

    van "\"What are you doing in Myers?\""

    show draco_talk at dra_pos_1 with Dissolve(0.2)

    dra "\"It does not matter. {w=0.5}What matters is what you're looking for, {w=0.5}isn't it?\""

    hide draco_talk with Dissolve(0.2)

    van "\"What I am looking for?\""

    show draco_talk at dra_pos_1 with Dissolve(0.2)

    dra "\"The truth. {w=0.5}You're searching for the truth.\""

    dra "\"Mr. Edgeworth's past, {w=0.5}Mr. Blake's incident, {w=0.5}and the secret of Myers...\""

    $ say_who = _("Draco")

    dra "\"You are curious about all of this.\""

    show draco_close_eye_talk at dra_pos_1
    hide draco_talk
    hide draco_normal
    with Dissolve(0.2)

    dra "\"But Lady [name!t], {w=0.5}have you ever heard of such a phrase?\""

    show draco_talk at dra_pos_1 with Dissolve(0.2)
    hide draco_close_eye_talk

    dra "{color=#f00}\"Curiosity about bad things is a cursable disease that arises from impure thoughts.\"{/color}"

    hide draco_talk
    show draco_normal at dra_pos_1
    with Dissolve(0.2)

    $ say_who = ""

    van "\"......\""

    van "\"...Draco, {w=0.5}what exactly do you know?\""

    show draco_close_eye_talk at dra_pos_1
    hide draco_normal
    with Dissolve(0.2)

    $ say_who = _("Draco")

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/draco/huh huh.mp3"

    dra "\"I'm just a butler with little knowledge. {w=0.5}I don't know much about the past of Myers Corporation.\""

    hide draco_close_eye_talk
    show draco_talk at dra_pos_1
    with Dissolve(0.2)

    dra "\"The truth is, {w=0.5}I just can't bear to see such a lovely lady perish in this abandoned facility.\""

    show draco_close_eye_talk at dra_pos_1
    hide draco_normal
    hide draco_talk
    with Dissolve(0.2)

    dra "\"Of course, {w=0.5}I have my own reason to be here. {w=0.5}But at the same time, {w=0.5}I want to stop your impulsiveness.\""

    hide draco_close_eye_talk
    show draco_talk at dra_pos_1
    with Dissolve(0.2)

    dra "\"It is best you go back the way you came, {w=0.5}Lady [name!t].\""

    dra "{color=#f00}\"You don't belong here. {w=0.5}And you don't deserve to be here.\"{/color}"

    stop music fadeout 10.0

    window hide

    hide draco_talk
    show draco_normal at dra_pos_1
    with Dissolve(0.2)

    $ say_who = ""

    pause 1.5

    window show

    van "\"......\""

    van "\"Thank you for your kindness, {w=0.5}Draco.\""

    van "\"But I've made my decision about it.\""

    van "\"You're right. {w=0.5}I'm indeed curious about Myers Corporation.\""

    van "\"But what I care more about is finding my lost self.\""

    van "\"My name, {w=0.5}my home, {w=0.5}my family...\""

    van "\"I want to get it all back.\""

    van "\"I don't know why you're here, {w=0.5}but I hope you can find what you're looking for as well.\""

    van "\"Now if you would excuse me.\""

    window hide

    $ renpy.pause(1.0, hard='True')

    $ say_who = _("Draco")

    window show

    dra "\"......\""

    $ renpy.music.set_volume(0.4, delay=0, channel='music')
    play music "music/myers lobby/were-loosing-time.ogg" fadein 3.0

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/draco/huhhhh.mp3"

    hide draco_normal
    show draco_close_eye_talk at dra_pos_1
    with Dissolve(0.2)

    dra "\"How stupid.\""

    van "\"......?\""

    hide draco_close_eye_talk
    show draco_normal at dra_pos_1
    show draco_talk at dra_pos_1
    with Dissolve(0.2)

    dra "\"Anyone who studies the history of human catastrophes can be sure that ignorance is the main source of human adversities.\""

    hide draco_normal
    hide draco_talk
    show draco_close_eye_talk at dra_pos_1
    with Dissolve(0.2)

    dra "\"Your seemingly commendable courage is nothing more than ignorance wrapped up in a pretty package.\""

    hide draco_close_eye_talk
    show draco_normal at dra_pos_1
    show draco_talk at dra_pos_1
    with Dissolve(0.2)

    dra "\"You have absolutely no clue what you are about to face.\""

    dra "\"Do you really believe that you can face up to all the dangers that are coming your way?\""

    dra "\"Do you really believe that you can accept the truth that will be revealed?\""

    hide draco_normal
    hide draco_talk
    show draco_dark_smile at dra_pos_1
    with Dissolve(0.2)

    dra "\"Are your memories... {w=0.5}{color=#f00}really more precious than your life{/color}?\""

    show draco_close_eye_talk at dra_pos_1
    hide draco_dark_smile
    with Dissolve(0.2)

    dra "\"Please forgive me for my bluntness, {w=0.5}Lady [name!t]. {w=0.5}But you will soon be embraced by death even before the truth befalls.\""

    window hide

    $ say_who = ""

    hide draco_close_eye_talk
    show draco_normal at dra_pos_1
    with Dissolve(0.5)

    $ renpy.pause(1.0, hard='True')

    stop music fadeout 6.0

    window show

    van "\"......\""

    van "\"Maybe Victor was right.\""

    van "\"Losing my memories could be a second chance.\""

    van "\"What was I like before? {w=0.5}Who knows.\""

    $ say_who = name

    van "\"Maybe the loss of memory was intentional on my part. {w=0.5}Maybe everything right now is what I longed for.\""

    hide draco_normal
    show draco_surprised at dra_pos_1
    with Dissolve(0.2)

    van "\"But I'm sorry, {w=0.5}Draco. {w=0.5}I don't care much about that.\""

    van "\"The old me can make her own decisions, {w=0.5}but the new me, {w=0.5}and only the new me, {w=0.5}makes all the decisions now.\""

    van "\"And what I do know is... {w=0.5}I don't feel complete without my memories right now.\""

    van "\"I will not give up until I find out the truth.\""

    $ say_who = ""

    window hide

    $ renpy.pause(1.0, hard='True')

    pause 1.0

    window show

    dra "\"......\""

    $ say_who = _("Draco")

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/draco/huh huh.mp3"

    show draco_close_eye_talk at dra_pos_1 with Dissolve(0.2)
    hide draco_surprised

    $ renpy.music.set_volume(0.6, delay=0, channel='music')
    play music "music/myers lobby/epic-action-fight-scene-music.ogg"

    dra "\"Lady [name!t], {w=0.5}you are so determined. {w=0.5}It seems that there's nothing I can do about it.\""

    hide draco_close_eye_talk
    show draco_talk at dra_pos_1
    with Dissolve(0.2)

    dra "\"If that's the case, {w=0.5}why don't we play a little game?\""

    hide draco_talk
    show draco_normal at dra_pos_1
    with Dissolve(0.2)

    $ say_who = ""

    van "\"A game?\""

    $ say_who = _("Draco")

    show draco_talk at dra_pos_1 with Dissolve(0.2)

    dra "\"You came to Myers to investigate its past, {w=0.5}and your connection with it, {w=0.5}didn't you?\""

    dra "\"Then show me what you have learned.\""

    show draco_close_eye_talk at dra_pos_1
    hide draco_talk
    hide draco_normal
    with Dissolve(0.2)

    dra "\"If you can answer my questions correctly, {w=0.5}then I will allow you to continue your investigation here.\""

    dra "\"However...\""

    dra "\"If you fail...\""

    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/computer glitch.ogg"

    show bad_tv_signal onlayer tvsignal:
        alpha 1.0

    $ renpy.pause(0.1, hard=True)

    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.05, hard=True)
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.05, hard=True)
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.05, hard=True)
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.05, hard=True)
    show myers_lobby_with_draco_glitch_1
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.05, hard=True)
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.05, hard=True)
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.05, hard=True)
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.05, hard=True)
    show myers_lobby_with_draco_glitch_2
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.05, hard=True)
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.05, hard=True)
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.05, hard=True)
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.05, hard=True)

    hide draco_close_eye_talk
    hide myers_lobby_with_draco_glitch_1
    hide myers_lobby_with_draco_glitch_2
    hide bedroom_dust

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/kevin.ogg"

    show transparent dark-small:
        alpha 0.3

    show draco_fisheye_3 onlayer front:
        xalign 0.5 yalign 0.5

    show bad_tv_signal onlayer tvsignal:
        alpha 0.6

    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.1, hard=True)

    show myers_lobby_draco_glitch

    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15))
    $ renpy.pause(1.0, hard=True)

    cyb_dra "{color=#f00}\"Then I will end your life here with my own hands.\"{/color}"

    jump myers_lobby_draco_battle_start




label myers_lobby_draco_battle_end:

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

    hide screen myers_lobby_draco_battle_chance
    hide bad_tv_signal onlayer tvsignal
    hide myers_lobby_draco_glitch
    hide draco_fisheye_4 onlayer front
    hide draco_fisheye_3 onlayer front
    hide transparent dark-small
    $ renpy.transition(Dissolve(1.0))

    stop music fadeout 6.0

    $ renpy.pause(3.0, hard='True')

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

    show draco_drop_shadow at dra_pos_1
    show draco_normal at dra_pos_1
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    pause 1.0

    show draco_talk at dra_pos_1
    with Dissolve(0.2)

    window show

    dra "\"Well done, {w=0.5}Lady [name!t]. {w=0.5}You did not disappoint me.\""

    hide draco_talk with Dissolve(0.2)

    van "\"Draco, {w=0.5}I've answered all your questions. {w=0.5}It's time to live up to promise and let me go.\""

    show draco_close_eye_talk at dra_pos_1
    hide draco_talk
    hide draco_normal
    with Dissolve(0.2)

    dra "\"As you wish. {w=0.5}In fact, {w=0.5}I had no intention of hurting you to begin with.\""

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/shake.ogg"

    $ say_who = name

    van "\"......\"" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    show draco_normal at dra_pos_1
    hide draco_close_eye_talk
    with Dissolve(0.2)

    $ say_who = ""

    van "\"What about your threat of \"ending your life here with my own hands\"?\""

    show draco_close_eye_talk at dra_pos_1
    hide draco_normal
    with Dissolve(0.2)

    dra "\"I just thought it would make the game more interesting that way. {w=0.5}That's all.\""

    van "\"......\""

    van "(These guys are each weirder than the next...)"

    show draco_normal at dra_pos_1
    hide draco_close_eye_talk
    with Dissolve(0.2)

    $ renpy.music.set_volume(0.4, delay=0, channel='music')
    play music ["<silence 1.0>", "music/myers lobby/were-loosing-time.ogg"] fadein 3.0

    van "\"But Mr. Butler, {w=0.5}I do have some questions for you as well.\""

    van "\"I'm just a butler with little knowledge. {w=0.5}I don't know much about the past of Myers Corporation.\""

    van "\"If I remember correctly, {w=0.5}you said that, {w=0.5}didn't you?\""

    show draco_talk at dra_pos_1
    with Dissolve(0.2)

    dra "\"Indeed I did. {w=0.5}Are there any problems?\""

    hide draco_talk with Dissolve(0.2)

    van "\"You have proved that this is a big lie.\""

    van "\"What are you hiding? {w=0.5}And why on earth are you here?\""

    van "\"I'm not letting you step out of here until I get an answer.\""

    window hide

    pause 1.5

    window show

    $ say_who = _("Draco")

    dra "\"......\""

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/draco/hmm.mp3"

    show draco_close_eye_talk at dra_pos_1
    hide draco_normal
    with Dissolve(0.2)

    dra "\"*sigh* {w=0.5}You just can't win with this lady.\""

    dra "\"But it won't hurt to tell you.\""

    dra "\"The truth is - \""

    dra "\"Mr. Edgeworth had a lot of hassles with the Myers Corporation.\""

    $ say_who = ""

    van "\"Hassles?\""

    van "\"Do you mean...\""

    van "\"{color=#f00}The car accident{/color}?\""

    show draco_normal at dra_pos_1
    hide draco_close_eye_talk
    show draco_talk at dra_pos_1
    with Dissolve(0.2)

    dra "\"Lady [name!t], {w=0.5}you are very clever. {w=0.5}I think you've already guessed.\""

    dra "\"The car accident was not actually an accident; {w=0.5}it was carefully planned by Myers Corporation.\""

    van "\"......\""

    show black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    hide draco_talk with Dissolve(0.2)

    van "That explains Vincent's gloomy face when he heard about the G4 Cyborg Incident."

    van "It also sounds completely in line with Myers' style."

    van "But..."

    van "{color=#f00}Why did Myers try to kill Vincent?{/color}"

    hide black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    van "\"I don't understand. {w=0.5}What did Vincent do?\""

    van "\"Didn't he get Myers Corporation off the hook for the G4 Cyborg Incident?\""

    show draco_talk at dra_pos_1
    with Dissolve(0.2)

    $ say_who = _("Draco")

    dra "\"The reason is simple.\""

    dra "\"Because he knew the truth about the G4 Cyborg Incident.\""

    show draco_close_eye_talk at dra_pos_1
    hide draco_normal
    hide draco_talk
    with Dissolve(0.2)

    dra "\"Although Mr. Edgeworth was a lawyer at Myers Corporation, \""

    dra "\"To the core members, {w=0.5}he was just a pawn and another outsider.\""

    dra "\"When the pawns have outlived their usefulness, {w=0.5}they are discarded.\""

    dra "\"And the fastest and most effective way to deal with unnecessary outsiders who know something they shouldn't,\""

    dra "\"is also to make them disappear from the world.\""

    dra "\"Therefore, {w=0.5}the company took the opportunity of holding a party to kill my master with a premeditated car accident.\""

    show draco_normal at dra_pos_1
    show draco_talk at dra_pos_1
    hide draco_close_eye_talk
    with Dissolve(0.2)

    dra "\"However, {w=0.5}they never expected that Mr. Edgeworth would survive.\""

    dra "\"Although the company failed in their plan, {w=0.5}they did not stop there.\""

    dra "\"Since then, {w=0.5}Mr. Edgeworth has received constant threats and harassment from Myers Corporation.\""

    hide draco_talk with Dissolve(0.2)

    $ say_who = ""

    van "\"Harassment? {w=0.5}Even after the bankruptcy?\""

    $ say_who = _("Draco")

    show draco_close_eye_talk at dra_pos_1
    hide draco_normal
    with Dissolve(0.2)

    dra "\"Yes.\""

    show draco_normal at dra_pos_1
    show draco_talk at dra_pos_1
    hide draco_close_eye_talk
    with Dissolve(0.2)

    dra "\"There are signs that Myers Corporation has become a secret underground organization after the G4 Cyborg Incident.\""

    dra "\"But to me that doesn't make much difference.\""

    dra "\"The old Myers Corporation was just a terrorist organization hiding under the banner of scientific research.\""

    hide draco_talk with Dissolve(0.2)

    $ say_who = ""

    van "\"So what you're saying is, {w=0.5}those still using the abandoned site of Myers Corporation is...\""

    van "\"Myers itself? \""

    show draco_close_eye_talk at dra_pos_1
    hide draco_normal
    with Dissolve(0.2)

    dra "\"That is why I am here. {w=0.5}It is the answer I'm searching for.\""

    $ say_who = name

    van "\"...Wait a minute.\""

    show draco_normal at dra_pos_1
    hide draco_close_eye_talk
    with Dissolve(0.2)

    van "\"If Vincent's car accident was the work of Myers, {w=0.5}how do you explain the death of all the core members?\""

    show draco_talk at dra_pos_1
    with Dissolve(0.2)

    $ say_who = ""

    dra "\"Someone else must have been responsible for that. {w=0.5}But I don't know who.\""

    hide draco_talk at dra_pos_1
    with Dissolve(0.2)

    van "......"

    show black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    van "So basically, {w=0.5}after Myers attempted to murder Vincent, {w=0.5}there was a {color=#f00}different perpetrator {/color}who assassinated all the core members of Myers Corporation?"

    hide black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    stop music fadeout 3.0

    van "\"So... {w=0.5}one last question.\""

    van "\"Do you know how I am involved...\""

    van "\"With all of this?\""

    show draco_dark at dra_pos_1
    hide draco_normal
    with Dissolve(0.2)

    dra "\"......\""

    van "At that moment, {w=0.5}Draco's smile disappeared."

    dra "\"...Sorry, {w=0.5}[name!t]. {w=0.5}I don't know.\""

    van "For some reason, {w=0.5}his tone is much heavier than before."

    van "And the sudden drop of formality also left me lost for words."

    show draco_low_brow_talk at dra_pos_1
    with Dissolve(0.2)

    dra "\"That's what you're here for, {w=0.5}isn't it?\""

    dra "\"I'm sure you'll find the answer.\""

    show draco_low_brow at dra_pos_1
    hide draco_low_brow_talk
    with Dissolve(0.2)

    van "Draco regained his smile, {w=0.5}as if he suddenly became aware that he was being out of character."

    van "But this time, {w=0.5}the smile was... {w=0.5}a bit different."

    van "It reminded me of {color=#f00}someone else{/color}."

    window hide

    pause 1.0

    window show

    van "\"I need your help, {w=0.5}Draco.\""

    van "\"If the two of us work together to investigate, {w=0.5}we will soon find out the truth.\""

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/draco/huh huh.mp3"

    show draco_normal at dra_pos_1
    show draco_talk at dra_pos_1
    hide draco_low_brow
    hide draco_dark
    with Dissolve(0.2)

    $ say_who = _("Draco")

    dra "\"Partner with me? {w=0.5}I'm really flattered.\""

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music ["music/ambience/mic horror ambience 4.ogg","<silence 1.0>"] fadein 5.0

    dra "\"So listen up, {w=0.5}Lady [name!t].\""

    dra "\"What I'm going to tell you next is very important for our investigation.\""

    dra "\"Starting from the lobby, {w=0.5}Myers Corporation is divided into two sections, {w=0.5}left and right.\""

    dra "\"Each section contains different departments and rooms. {w=0.5}On the left is Mr. Blake's Investment Department.\""

    dra "\"And Mr. Edgeworth's Legal Department is on the right side of Myers Corporation.\""

    show draco_close_eye_talk at dra_pos_1
    hide draco_normal
    hide draco_talk
    with Dissolve(0.2)

    dra "\"As to where you want to start, {w=0.5}it is entirely up to you.\""

    show draco_normal at dra_pos_1
    show draco_talk at dra_pos_1
    hide draco_close_eye_talk
    with Dissolve(0.2)

    dra "\"No matter which route you choose, {w=0.5}they will eventually lead to the basement - \""

    dra "\"In other words... {w=0.5}{color=#f00}where the secret chamber of G4 Cyborg Incident is located.{/color}"

    hide draco_talk with Dissolve(0.2)

    $ say_who = ""

    van "\"That is to say, {w=0.5}if I want to know about Victor's past, {w=0.5}I should choose to go left.\""

    van "\"But if I'm more curious about Vincent, {w=0.5} I should choose to go right.\""

    show draco_talk at dra_pos_1
    with Dissolve(0.2)

    dra "\"That's an interesting explanation. {w=0.5}You're not wrong saying that.\""

    dra "\"So - \""

    dra "\"Lady [name!t], {w=0.5}have you made up your mind?\""

    hide draco_talk with Dissolve(0.2)

    van "\"......\""

    stop music fadeout 5.0

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/UI Dark.ogg"

    noname "Warning: {w=0.5}Starting from the Myers lobby, {w=0.5}the game will have two different branches."

    noname "Depending on the route [name!t] chosen, {w=0.5}the game will unfold differently."

    noname "In order to keep the plot smooth, {w=0.5}branch 2 (left) will be unlocked after branch 1 (right) is finished."

    noname "(Alpha 1.0.0: {w=0.5}Game updated to Chapter 4)"

    window hide

    pause 1.0

    van "Which route should I choose?"

    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    menu:
        "Branch 1 - Right":

            window show

            show draco_talk at dra_pos_1
            with Dissolve(0.2)

            dra "\"Right is it? {w=0.5}Looks like you're more interested in Mr. Edgeworth.\""

            hide draco_talk with Dissolve(0.2)

            van "\"From the information we've gathered so far, {w=0.5}Vincent seems to be more closely involved in the G4 Cyborg Incident.\""

            van "\"I believe investigating the Legal Department will give us the answers we want.\""

            show draco_talk at dra_pos_1
            with Dissolve(0.2)

            dra "\"I see. {w=0.5}I'll have to agree.\""

            hide draco_talk with Dissolve(0.2)

            window hide

        "Branch 2 - Left" if route_2_available:


            $ route_2_available = False

    $ renpy.music.set_volume(0.8, delay=0, channel='background noise')
    $ renpy.music.play("music/myers lobby/radio tune.ogg", channel="background noise", loop=True)

    $ renpy.music.set_volume(0.6, delay=0, channel='music')
    play music "music/myers lobby/lobby horror.ogg"

    hide draco_normal
    show draco_surprised at dra_pos_1
    with Dissolve(0.2)

    show transparent dark-small:

        alpha 0.3
        pause 0.3
        alpha 0.15
        pause 0.2
        alpha 0.6
        pause 0.05
        alpha 0.3
        pause 0.5
        alpha 0.45
        pause 0.01
        alpha 0.1
        pause 0.01
        alpha 0.1
        pause 0.05
        alpha 0.05
        pause 0.05
        alpha 0.2
        pause 0.05
        alpha 0.0
        pause 0.05
        alpha 0.5
        pause 0.35
        alpha 0.1
        pause 0.05
        alpha 0.2
        pause 1.0
        repeat

    $ renpy.pause(1.0, hard='True')

    pause 1.0

    $ renpy.pause(0.1, hard='True')

    hide draco_surprised
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard=True)

    $ renpy.pause(2.0, hard=True)

    van "!?"

    van "Just as Draco and I reached an agreement, {w=0.5}the intercom in the Myers lobby went off without warning."

    stop sound fadeout 4.0
    $ renpy.music.stop(channel="background noise", fadeout = 4.0)

    $ renpy.pause(6.0, hard=True)

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/myers lobby/myers lobby radio/welcome to myers.ogg"

    radio "\"Wel{size=+8}come{/size} to{size=-8} the{/size} My{size=+10}ers{/size} Cor{size=-8}por{/size}a{size=+8}tion{/size}-\""

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/myers lobby/myers lobby radio/as the number 1.ogg"

    radio "\"{size=+10}As {/size}{size=+8}as {/size}as {size=-8}the {/size}#1 trusted {size=-8}sour{/size}ce {size=+10}for {/size}mechan{size=+8}ical {/size}prosthetics,\""

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/myers lobby/myers lobby radio/define global standards.ogg"

    radio "\"We {size=+10}define {/size}global {size=+8}stan{/size}dards {size=-8}{w=0.5}and {/size}create a first {size=-8}first {/size}first {size=+10}class {/size}corporate image.\""

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/myers lobby/myers lobby radio/design create enhance.ogg"

    radio "\"Design, {size=-8}create, {/size}{size=+10}enhance{/size}. {w=0.5}Myers Corporation.\""

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/myers lobby/myers lobby radio/please enjoy your tour.ogg"

    radio "\"Please {size=+10}enjoy {/size}yo{size=-10}ur {/size}visit, {w=0.5}and have a {size=+10}wonderful {/size}wonderful {size=+5}wonderful {/size}wonderful {size=-8}wonderful {/size}wonderful {size=+10}painful {/size}day!\""

    $ renpy.pause(2.0, hard=True)

    hide transparent dark-small with Dissolve(0.5)
    stop music fadeout 1.0
    $ renpy.pause(0.1, hard=True)
    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/myers lobby/huge monster steps.ogg"

    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 0.6, dist=15))
    $ renpy.pause(0.7, hard=True)

    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 0.6, dist=15))
    $ renpy.pause(0.8, hard=True)

    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 0.6, dist=15))
    $ renpy.pause(0.7, hard=True)

    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 0.6, dist=15))
    $ renpy.pause(0.9, hard=True)

    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 0.6, dist=15))
    $ renpy.pause(0.7, hard=True)

    $ renpy.pause(1.0, hard=True)

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/monster moan 2.ogg"

    pause 4.0

    van "!?"

    van "From the far end of the employee passage in the distance - {w=0.5}{color=#f00}comes a heartrending howl.{/color}"

    $ renpy.music.set_volume(0.8, delay=0, channel='music')
    play music "music/myers lobby/hordes of horror.ogg"

    show myers_lobby_blurred:
        alpha 0
        parallel:
            pause 1.0
            linear 0.8 alpha 0 xalign 0.5 yalign 0 zoom 1.0
            linear 0.8 alpha 0.3 xalign 0.5 yalign 0 zoom 1.2
            linear 0.8 alpha 0 xalign 0.5 yalign 0 zoom 1.0
            repeat

    show main_title_shadow

    pause 1.0
    $ renpy.pause(0.5, hard=True)

    pause 1.0

    show character_icon_box_1:
        xpos 1350 ypos 50
        easein_expo 0.5 xpos 700 ypos 50
    show draco_icon_serious:
        xpos 1350 ypos 50
        easein_expo 0.5 xpos 700 ypos 48
    show character_icon_box_2:
        xpos 1350 ypos 50
        easein_expo 0.5 xpos 700 ypos 50

    dra "\"Impossible. {w=0.5}What have they done to him!?\""


    show character_icon_box_1:
        xpos 700 ypos 50
    show draco_icon_serious:
        xpos 700 ypos 48
    show character_icon_box_2:
        xpos 700 ypos 50

    van "Draco's face suddenly became very serious."

    van "\"They? {w=0.5}To him?\""

    van "\"Draco, {w=0.5}what is going on?\""

    show draco_icon_close_eye_serious behind character_icon_box_2:
        xpos 700 ypos 48
    hide draco_icon_serious

    dra "\"There's no time to explain. {w=0.5}[name!t], {w=0.5}go now!\""

    hide character_icon_box_1
    hide draco_icon_close_eye_serious
    hide character_icon_box_2
    with Dissolve(0.2)

    pause 0.5

    van "\"Wait a minute - {w=0.5}Draco!\""

    $ renpy.pause(0.1, hard=True)

    window hide

    $ renpy.music.set_volume(0.4, delay=0, channel='sound')
    play sound ("music/John Past/punch-face-hard.ogg")

    with Shake((0.5, 1.0, 0.5, 1.0), 0.6, dist=15)

    van "Before I could finish, {w=0.5}Draco pushed me to the right room of the lobby, {w=0.5}and then punched a button on the front desk."

    pause 0.5

    $ renpy.pause(0.1, hard=True)

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/shock2.ogg" fadeout 2.0

    van "\"Draco!\"" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    $ renpy.pause(0.5, hard=True)

    show draco_serious behind main_title_shadow at dra_pos_1
    with Dissolve(0.5)

    window show

    $ say_who = _("Draco")

    dra "\"[name!t], {w=0.5}don't you want to know the truth? {w=0.5}Don't you want to know who you are?\""

    show draco_close_eye_serious at dra_pos_1
    hide draco_serious
    with Dissolve(0.2)

    dra "\"Then go. {w=0.5}If your life ends here and now, {w=0.5}all your efforts will be in vain.\""

    $ say_who = ""

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/shock2.ogg" fadeout 2.0

    van "\"But what about you!?\"" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    window hide

    stop music fadeout 4.0
    hide main_title_shadow
    hide myers_lobby_blurred
    with Dissolve(2.0)

    $ renpy.pause(3.0, hard=True)

    stop music

    $ renpy.music.set_volume(0.8, delay=0, channel='music')
    play music "music/myers lobby/trials errors.ogg"

    window show

    $ renpy.pause(0.1, hard=True)

    show draco_low_brow_talk at dra_pos_1
    hide draco_close_eye_serious
    $ renpy.transition(Dissolve(0.2))
    $ renpy.pause(0.2, hard=True)

    dra "\"I'm just a butler. {w=0.5}Please don't worry about me.\""

    dra "\"I'll try my best to hold him back.\""

    van "\"Bu - {w=0.5}but,\""

    show draco_close_eye_talk at dra_pos_1
    hide draco_low_brow_talk
    with Dissolve(0.2)

    $ say_who = _("Draco")

    dra "\"[name!t], {w=0.5}like you, {w=0.5} I am a person without a past.\""

    dra "\"It wasn't that long ago that my life could only be described as empty,{w=0.5} monotonous, {w=0.5}and boring.\""

    show draco_talk at dra_pos_1
    hide draco_close_eye_talk
    with Dissolve(0.2)

    dra "\"But the arrival of this one person changed everything around me.\""

    dra "\"She helped me break free from the blank world, {w=0.5}and made me realize that nothing is more important than the present.\""

    dra "\"She is very important to me. {w=0.5}I can't lose her a second time.\""

    show draco_normal at dra_pos_1
    hide draco_talk
    with Dissolve(0.2)

    $ say_who = ""

    pause 0.5

    van "\"......\""

    van "\"Draco...\""

    van "\"Do we... {w=0.5}know each other?\""

    show draco_close_eye at dra_pos_1
    hide draco_normal
    with Dissolve(0.2)

    van "In response to my question, {w=0.5}Draco smiled."

    show draco_talk at dra_pos_1
    hide draco_close_eye
    with Dissolve(0.2)

    dra "\"My name is {color=#f00}Draco Edgeworth{/color}. {w=0.5}It is my pleasure to meet you, {w=0.5}Lady [name!t].\""

    window hide

    $ renpy.pause(0.5, hard=True)

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/myers lobby/EndingDoorSFX.ogg"

    $ renpy.pause(0.1, hard=True)

    show transparent dark-small:
        alpha 0
        pause 1.5
        linear 1.5 alpha 1.0

    show myers_lobby_side_gate:
        yoffset -1000
        pause 2.0
        ease 0.8 yoffset -100
        ease 0.3 yoffset -137






    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 4.0, dist=15))
    $ renpy.pause(4.0, hard=True)

    stop sound fadeout 2.0

    $ renpy.pause(1.5, hard=True)

    van "!?"

    stop sound

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/shock2.ogg" fadeout 2.0

    van "\"Draco!! {w=0.5}Draco!!!\"" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    $ renpy.pause(1.0, hard=True)

    stop music fadeout 8.0

    scene black
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    $ renpy.pause(2.0, hard=True)

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False

    window show

    van "But only silence... {w=0.5}answers my cries."

    window hide

    $ renpy.pause(4.0, hard=True)

    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)
    $ renpy.block_rollback()
    $ _rollback = False

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/UI Dark.ogg"

    window show

    noname "Chapter Two: {w=0.5}The End"

    window hide

    jump route1_start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
