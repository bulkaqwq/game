

image engineering_room_1 = "images/Engineering Room 1/Engineering_room_1.png"
image engineering_room_2 = "images/Engineering Room 1/Engineering_room_2.png"
image engineering_room_3 = "images/Engineering Room 1/Engineering_room_3.png"

default engineering_room_4_image = "images/Engineering Room 1/Engineering_room_4.png"
image engineering_room_4 = "[engineering_room_4_image]"
image engineering_room_4_blurred = im.Blur("images/Engineering Room 1/Engineering_room_4.png", 1.5)

image engineering_room_keycard_zoom = "images/Engineering Room 1/Engineering_room_keycard_zoom.png"
image engineering_room_1_arm_4_zoom = "images/Engineering Room 1/Engineering_room_1_arm_4_zoom.png"
image engineering_room_3_arm_zoom_key = "images/Engineering Room 1/Engineering_room_3_arm_zoom_key.png"
image engineering_room_3_arm_zoom_no_key = "images/Engineering Room 1/Engineering_room_3_arm_zoom_no_key.png"
image engineering_room_tape = "images/Engineering Room 1/Engineering_room_tape.png"
image engineering_room_knife = "images/Engineering Room 1/Engineering_room_knife.png"


image engineering_room_vincent_parallax_background = "images/Vincent Parallax/vincent parallax background.png"
image engineering_room_vincent_parallax_vincent = "images/Vincent Parallax/vincent parallax vincent.png"
image engineering_room_vincent_parallax_circles = "images/Vincent Parallax/vincent parallax circles.png"
image engineering_room_vincent_parallax_particles = "images/Vincent Parallax/vincent parallax particles.png"

label route1_start:

    $ renpy.free_memory()

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = True
    $ _rollback = True

    $ renpy.pause(4.0, hard='True')
    pause 2.0
    $ renpy.pause(0.1, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music "music/bedroom suspense.ogg" fadein 3.0

    pause 6.0

    $ renpy.pause(0.1, hard='True')

    window show

    van "Draco Edgeworth."

    $ rollback_ = True

    van "From the first moment I saw him, {w=0.5}I thought he somehow looked very similar to Vincent."

    van "But I had no idea that Vincent and him were really related by blood."

    van "Are they brothers?"

    van "But..."

    van "What kind of person would make his own brother a butler?"

    window hide

    pause 1.0

    $ renpy.pause(0.1, hard='True')

    show memory_frame:
        alpha 0.8
        pause 0.001
        alpha 1
        pause 0.001
        repeat

    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    pause 0.5

    $ renpy.pause(0.1, hard='True')

    show draco_white_shadow behind memory_frame:
        alpha 0.8
        pause 0.001
        alpha 0.75
        pause 0.001
        repeat

    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    window show

    dra "\"[name!t], {w=0.5}like you, {w=0.5}I am a person without a past.\""

    dra "\"It wasn't that long ago that my life could only be described as empty,{w=0.5} monotonous, {w=0.5}and boring.\""

    dra "\"But the arrival of this one person changed everything around me.\""

    dra "\"She helped me break free from the blank world, {w=0.5}and made me realize that nothing is more important than the present.\""

    dra "\"She is very important to me. {w=0.5}I can't lose her a second time.\""

    window hide

    pause 0.5
    $ renpy.pause(0.1, hard='True')

    hide draco_white_shadow
    hide memory_frame
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    pause 2.0
    $ renpy.pause(0.1, hard='True')

    window show

    van "Draco..."

    van "What exactly did all of that... {w=0.5}mean?"

    van "......"

    window hide

    stop music fadeout 7.0

    pause 5.0
    $ renpy.pause(0.1, hard='True')

    show myers_lobby_side_gate:
        yoffset -137
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    pause 2.0

    $ renpy.pause(0.1, hard='True')

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/shock2.ogg" fadeout 2.0

    van "\"Draco!!!{w=0.5} Draco!!!\"" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/banging.ogg"

    with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    pause 1.5

    van "I banged on the gate again and again, {w=0.5}but there was no response."

    pause 1.0

    van "\"Damn it... {w=0.5}This can't be it! {w=0.5}There has to be a way!\""

    van "I groped along the nearby walls but didn't find any switch to reopen the gate."

    pause 1.0

    van "\"......\""

    van "\"Draco...\""

    van "I felt disheartened at how powerless I was, {w=0.5}how he was right there yet I couldn't help him."

    pause 0.5

    $ renpy.pause(0.1, hard='True')

    $ renpy.music.set_volume(0.3, delay=0, channel='sound')
    play sound "music/mad vincent.ogg" fadeout 1.0

    anon "{size=+8}\"What the hell??? {w=0.5}Why's the gate locked???\"{/size}" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    van "!?"

    pause 0.5

    $ renpy.pause(0.1, hard='True')

    scene engineering_room_1
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

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

    $ renpy.music.set_volume(0.8, delay=0, channel='music')
    play music "music/jazz.ogg"

    pause 1.0

    show zalmona_drop_shadow
    show zalmona_panic
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    pause 1.0

    van "Suddenly, {w=0.5}I was taken aback by the appearance of an odd-looking person from the other side of the room."

    hide zalmona_drop_shadow
    hide zalmona_panic
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    pause 1.0

    van "Before I could say anything, {w=0.5}she ran around me and rushed to the gate."

    pause 1.0

    $ renpy.pause(0.1, hard='True')

    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/banging.ogg"

    with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    anon "\"Hey!!! {w=0.5}Hey!!!! {w=0.5}Let me out!!!\""

    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/banging.ogg"

    with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    van "She was yelling and banging, {w=0.5}as if she was completely unaware of my presence."

    anon "\"Hey!! {w=0.5}Hey!! {w=0.5}Can you hear me???\""

    anon "\"Hey!!!\""

    pause 1.0

    van "After carrying on for a while but earning no response, {w=0.5}she finally decided to give up."

    show zalmona_drop_shadow
    show zalmona_panic
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    pause 0.5

    window show

    anon "\"Huff... {w=0.5}huff...\""

    van "She was breathing heavily when she turned around, {w=0.5}staring straight at me with her bright, burning eyes."

    $ renpy.music.set_volume(0.4, delay=0, channel='sound')
    play sound "music/zalmona/Zalmona-huh_.ogg"

    show zalmona_angry
    hide zalmona_panic
    with Dissolve(0.2)

    pause 0.5

    anon "\"Was it you? {w=0.5}Were you the one who locked me in here?\" {w=0.5}She demanded."

    van "\"......\""

    van "(Shit.{w=0.5} I may be in trouble.)"

    window hide

    pause 1.0

    stop music fadeout 5.0

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/shock2.ogg" fadeout 2.0

    show zalmona_surprised_exclamation
    hide zalmona_angry
    with Dissolve(0.2)

    $ renpy.pause(0.1, hard='True')
    with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    anon "!?"

    pause 1.0

    van "Just when I thought I had to come up with a plan to deal with her, {w=0.5}her face looked as if she had suddenly realized something."

    van "Her eyes were still focused on me, {w=0.5}but this time she was looking me up and down."

    show zalmona_surprised
    hide zalmona_surprised_exclamation
    with Dissolve(0.2)

    pause 2.0

    anon "\"Mmm? {w=0.5}Have we met before?\" {w=0.5}She suddenly asked."

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/shock2.ogg"
    van "!?" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    van "What, {w=0.5}what did she just say!?"

    van "......"

    van "Her very surprising comment left me speechless for a moment. {w=0.5}It was not something I expected to hear from her."

    van "\"Uh... {w=0.5}I...\""

    van "\"......\""

    van "(Calm down, {w=0.5}calm down...)"

    show black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    window show

    van "This is critical. {w=0.5}I can't miss my chance."

    van "In other words-"

    van "I might be able to learn something about my past from her."

    van "But I need to be careful-"

    van "I don't have any idea whether she's a friend or foe yet."

    van "And judging from how she acted, {w=0.5}it seems that she's only had a casual acquaintance with me as well."

    van "It may not be the best idea to just start throwing questions at her about myself."

    van "More importantly, {w=0.5}if I expose the fact that I lost my memory... {w=0.5}Things may only work against me."

    van "So the safest strategy right now..."

    van "Would be to get information out of her in a less straightforward way."

    window hide

    hide black
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    pause 1.0

    van "\"...Oh hi! {w=0.5}It's been a while. {w=0.5}Do you still remember me?\""

    van "I tried my best to stay calm and greeted her."

    show zalmona_normal
    hide zalmona_surprised
    with Dissolve(0.2)

    pause 1.0

    anon "\"......\""

    pause 1.0

    stop music fadeout 3.0

    van "She looked all over me again, {w=0.5}and then her eyes rested on my face."

    pause 1.0

    $ renpy.music.set_volume(0.2, delay=0, channel='sound')
    play sound "music/zalmona/Zalmona-hnnnnn.ogg"

    anon "\"You do seem kinda familiar. {w=0.5}Let me see...\""

    anon "\"......\""

    pause 2.0

    show zalmona_surprised_exclamation
    hide zalmona_normal
    with Dissolve(0.2)

    window show

    anon "!"

    $ renpy.music.set_volume(0.8, delay=0, channel='music')
    play music "music/jazz.ogg"

    show zalmona_happy
    hide zalmona_surprised_exclamation
    with Dissolve(0.2)

    anon "\"Oh hey! {w=0.5}{color=#f00}Detective{/color}!\""

    van "She suddenly exclaimed with excitement."




    anon "\"I remember now! {w=0.5}I knew it.\""

    anon "\"You were the one {color=#f00}with that famous lawyer{/color} last time!\""

    anon "\"As was expected of me, {w=0.5}{color=#f00}Zalmona{/color}! {w=0.5}I knew we've met before!\""

    jump zalmona_intro

label zalmona_intro_end:

    window hide

    van "Zalmona? {w=0.5}Is that her name?"

    van "But more importantly- {w=0.5}did she just say I'm a Detective!?"

    van "My brain felt as if it couldn't handle all the information I had just received at once."

    van "I never thought I would be a cop -"

    van "Was I involved in a case? {w=0.5}Did something happen during my investigation that caused me to lose my memories?"

    van "But, {w=0.5}wait a minute..."

    van "She mentioned that I was with a \"famous lawyer.\" {w=0.5}Could she possibly be referring to..."

    pause 1.0

    $ renpy.music.set_volume(0.4, delay=0, channel='sound')
    play sound "music/zalmona/Zalmona-hnnnnn.ogg"

    show zalmona_normal
    hide zalmona_happy
    with Dissolve(0.2)

    window show

    zal "\"But, {w=0.5}Detective-\""

    van "Zalmona's voice interrupted my thoughts, {w=0.5}and dragged my mind back to reality."

    zal "\"I'm curious, {w=0.5}what brings you back to Myers Corporation this time?\""

    window hide

    pause 1.0

    van "Back to Myers...{w=0.5}Think think think. {w=0.5}I need to come up with an answer."

    van "If I were a cop, {w=0.5}there would be only one explanation for coming back here."

    van "\"I'm here to investigate the case of missing citizens over recent years, {w=0.5}and the truth behind the G4 Cyborg Incident.\""

    $ renpy.music.set_volume(0.4, delay=0, channel='sound')
    play sound "music/zalmona/Zalmona-huh_.ogg"

    show zalmona_surprised
    hide zalmona_normal
    with Dissolve(0.2)

    pause 1.0

    window show

    zal "\"Huh? {w=0.5}Again?\""

    zal "\"My god, {w=0.5}the G4 Investigation Bureau is as useless as ever.\""

    van "\"......\""

    show zalmona_normal
    hide zalmona_surprised
    with Dissolve(0.2)

    zal "\"Detective, {w=0.5}then it looks like your last investigation with that lawyer didn't go so well?\""

    zal "\"Why didn't you bring him along this time?\""

    stop music fadeout 3.0

    van "\"The famous lawyer... {w=0.5}Are you by any chance referring to Mr. Vincent Edgeworth?\""

    show zalmona_surprised
    hide zalmona_normal
    with Dissolve(0.2)

    zal "\"Of course. {w=0.5}Who else can it be?\""

    van "......"

    window hide

    pause 0.5

    scene black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    pause 1.0

    $ renpy.music.set_volume(0.6, delay=0, channel='music')
    play music "music/creepy.wav"

    window show

    van "So it seems that my speculation was correct."

    van "Vincent and I had indeed met before."

    van "And following this logic, {w=0.5}it would make sense that I've met Draco as well."

    van "If that's the case..."

    van "Why would Vincent hide everything from me, {w=0.5}and pretend that he didn't know me?"

    van "......"

    van "I suddenly remembered about the cyborg I saw at the mansion, {w=0.5}and how Vincent and Victor refused to explain anything about it."

    van "Myers had gone bankrupt years ago. {w=0.5}But it is clear that someone is still using the abandoned site for some kind of experiments."

    van "Draco told me, {w=0.5}Myers Corporation had become a secret underground organization after that huge incident."

    van "But even if that's true, {w=0.5}how can it explain the cyborg in Vincent's mansion?"

    van "Could it be that..."

    van "As a detective, {w=0.5}I was actually investigating Vincent, {w=0.5}and not Myers Corporation?"

    van "If we go with that explanation... {w=0.5}Vincent is most likely the person behind my memory loss."

    van "......"

    van "The more I thought about it, {w=0.5}the more worried I became."

    van "But there's something... {w=0.5}that has especially been bothering me."

    window hide

    show engineering_room_vincent_parallax_background onlayer absback:
        xalign 0.5 yalign 0.5
    show engineering_room_vincent_parallax_vincent onlayer front:
        xalign 0.5 yalign 0.5
    show engineering_room_vincent_parallax_circles onlayer inyourface:
        xalign 0.5 yalign 0.5
    show engineering_room_vincent_parallax_particles onlayer absfront:
        xalign 0.5 yalign 0.5
    show main_title_shadow onlayer ab_parallax:
        xalign 0.5 yalign 0.5
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    pause 1.0

    window show

    van "If you had asked me what kind of person Vincent was, {w=0.5}I would have answered:"

    van "Noble, {w=0.5}elegant, {w=0.5}and mysterious."

    van "His words, {w=0.5}while exuding charm, {w=0.5}could make you feel very uneasy at the same time."

    van "Is he someone we should be suspicious of?"

    van "Of course. {w=0.5}There's no doubt about it."

    van "Knowing Winston was innocent, {w=0.5}he single-handedly \"succeeded in proving\" that the entire experiment was the work of a single employee."

    van "How scary is this man, {w=0.5}for him to be able to do something like that?"

    van "Nonetheless..."

    van "When I met him at the mansion, {w=0.5}I felt that there was a subtle connection between us that I couldn't explain."

    van "I'm well aware that I've lost all of my memories."

    van "I have no idea about our past, {w=0.5}and have no reason to draw such conclusions."

    van "But this feeling... {w=0.5}was particularly strong."

    van "It was as if the part of my brain that stored memories had disappeared, {w=0.5}but the part that stored emotions was still intact."

    hide engineering_room_vincent_parallax_background onlayer absback
    hide engineering_room_vincent_parallax_vincent onlayer front
    hide engineering_room_vincent_parallax_circles onlayer inyourface
    hide engineering_room_vincent_parallax_particles onlayer absfront
    hide main_title_shadow onlayer ab_parallax
    scene black
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    pause 1.0

    stop music fadeout 3.0

    van "I have to learn about Vincent's past. {w=0.5}It is vital for me to know."

    scene engineering_room_1
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
    show zalmona_drop_shadow
    show zalmona_normal
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    pause 0.5

    window show

    van "\"Zalmona, {w=0.5}did you just come from the Legal Department?\""

    $ renpy.music.set_volume(0.4, delay=0, channel='sound')
    play sound "music/zalmona/Zalmona-huh_.ogg"

    show zalmona_surprised
    hide zalmona_normal
    with Dissolve(0.2)

    zal "\"Huh? {w=0.5}Yeah. {w=0.5}Are you planning to go there?\""

    van "\"Yes. {w=0.5}Can you take me there?\""

    window hide

    scene engineering_room_2
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
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    pause 1.0

    show zalmona_drop_shadow at zal_pos_2
    show zalmona_normal at zal_pos_2
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ say_who = _("Zalmona")

    window show

    zal "\"It's simple. {w=0.5}Just go through the door right here, {w=0.5}and you will reach the Legal Department.\""

    show zalmona_surprised at zal_pos_2
    hide zalmona_normal
    with Dissolve(0.2)

    zal "\"However... {w=0.5}hehehe.\""

    $ say_who = ""

    $ renpy.music.set_volume(0.1, delay=0, channel='sound')
    play sound "music/cloth.mp3" fadeout 2.0

    show transparent dark-small:
        alpha 0.6
    with Dissolve(0.5)

    van "She pulled out a card from her pocket."

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/scan map.ogg"

    show character_icon_box:
        xpos -350 ypos 50
        easein_expo 1.0 xpos 100 ypos 50
        xpos 100 ypos 50
    show zalmona_icon_normal:
        xpos -350 ypos 50
        easein_expo 1.0 xpos 100 ypos 48
        xpos 100 ypos 48

    show engineering_room_keycard_zoom onlayer inyourface:
        xoffset 750 ypos 100
        easein_expo 1.0 xoffset 250 ypos 100

    $ renpy.pause(1.0, hard='True')

    zal "\"Only by swiping this key card, {w=0.5}can you unlock this door.\""

    van "\"How... {w=0.5}did you get that???\""

    zal "\"No comment, {w=0.5}Miss Detective.\""

    zal "\"You know, {w=0.5}I haven't even yet dealt with you for locking us in here.\""

    van "\"......\""

    zal "\"But considering you're from the G4 Investigation Bureau, {w=0.5}I can make a deal with you.\""

    zal "\"Just like last time. {w=0.5}You do me a favor, {w=0.5}and I'll do you a favor. {w=0.5}How's that?\""

    van "\"Last time?\""

    show character_icon_box:
        xpos 100 ypos 50
    hide zalmona_icon_normal
    show zalmona_icon_surprised:
        xpos 100 ypos 48

    zal "\"Really? {w=0.5}Have you forgotten already!?\""

    zal "\"Last time you did me a little favor, {w=0.5}and in exchange I told you some secrets about Myers Corporation.\""

    hide zalmona_icon_surprised
    show zalmona_icon_normal:
        xpos 100 ypos 48

    zal "\"Let's do the same this time. {w=0.5}The truth is, {w=0.5}I accidentally lost one of my belongings here.\""

    zal "\"If you can help me find it, {w=0.5}then I'll give you this key card as a reward.\""

    van "\"......\""

    window hide

    show character_icon_box:
        xpos 100 ypos 50
        linear 0.5 xpos -350 ypos 50
    show zalmona_icon_normal:
        xpos 100 ypos 48
        linear 0.5 xpos -350 ypos 50

    show engineering_room_keycard_zoom onlayer inyourface:
        xoffset 250 ypos 100
        linear 0.5 xoffset 750 ypos 100

    hide character_icon_box
    hide zalmona_icon_normal
    hide engineering_room_keycard_zoom onlayer inyourface
    hide transparent dark-small
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(1.0, hard='True')

    window show

    van "\"Before I agree to anything... {w=0.5}Tell me, {w=0.5}what exactly have you lost?\""

    show zalmona_happy at zal_pos_2
    hide zalmona_surprised
    with Dissolve(0.2)

    zal "\"Oh, {w=0.5}a {color=#f00}round, {w=0.5}spherical{/color} object.\""

    van "\"......\""

    $ say_who = _("Zalmona")

    $ renpy.music.set_volume(0.2, delay=0, channel='sound')
    play sound "music/zalmona/Zalmona-hnnnnn.ogg"

    show zalmona_surprised at zal_pos_2
    hide zalmona_happy
    with Dissolve(0.2)

    zal "\"Hey, {w=0.5}what's that look all about?\""

    zal "\"I know, {w=0.5}I know. {w=0.5}It does sound kinda vague.\""

    zal "\"But trust me, {w=0.5}the moment you see it, {w=0.5}you'll instantly realize:\""

    show zalmona_happy at zal_pos_2
    hide zalmona_surprised
    with Dissolve(0.2)

    zal "\"'Aha! {w=0.5}This must be what Zalmona is looking for.'\""

    $ say_who = ""

    van "\"......This time, {w=0.5}I'll take your word for it.\""

    van "\"And this thing is something that you did indeed lose?\""

    show zalmona_surprised at zal_pos_2
    hide zalmona_happy
    with Dissolve(0.2)

    $ say_who = _("Zalmona")

    zal "\"Shush, {w=0.5}shush! {w=0.5}Stop asking so many questions!\""

    zal "\"We're making a deal here, {w=0.5}not playing 20 questions, {w=0.5}alright?\""

    show zalmona_normal at zal_pos_2
    hide zalmona_surprised
    with Dissolve(0.2)

    zal "\"What, {w=0.5}don't you want the key card? {w=0.5}Huh?\""

    $ say_who = ""

    van "\"......\""

    van "\"Alright. {w=0.5}Then are you sure you left the \"spherical object\" in this lab?\""

    show zalmona_surprised at zal_pos_2
    hide zalmona_normal
    with Dissolve(0.2)

    zal "\"No doubt about it! {w=0.5}I'm pretty sure it's somewhere in this lab.\""

    van "......"

    scene black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    pause 0.5

    window show

    van "Draco told me, {w=0.5}both sides of the lobby would eventually lead us to the basement-"

    van "Where the secret chamber of the G4 cyborg incident is located."

    van "In other words, {w=0.5}not only will I be able to find a lot of clues there, {w=0.5}but I could also get out of this place through the other side of the Myers lobby."

    show myers_lobby_side_gate:
        yoffset -137
    with Dissolve(0.5)

    van "At this moment, {w=0.5}still nothing could be heard from the other side of the gate. {w=0.5}I don't know what has happened to Draco."

    van "Would I ever get to see him again?"

    van "......"

    window hide

    scene engineering_room_1
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    pause 0.5

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music ["<silence 2.0>", "music/bgm/lab investigation.ogg"] fadein 3.0
    queue music "music/bgm/lab investigation.ogg"

    van "Anyway, {w=0.5}time for us to search for that \"spherical object.\""

    jump route_1_engineering_room_click_start

label winston_collab_past_end:

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    pause 3.0

    scene engineering_room_4
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

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/vanora/van heavy breath.ogg") fadeout 1.0

    van "\"Huff... {w=0.5}Huff...\""

    $ rollback_ = True

    van "Was that- {w=0.5}Vincent's memory that I just saw!?"

    show zalmona_drop_shadow at zal_pos_2
    show zalmona_panic at zal_pos_2
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    window show

    zal "\"Hey, {w=0.5}hey! {w=0.5}Are you alright?\""

    van "\"...Huh? {w=0.5}Oh, {w=0.5}uh, {w=0.5}I'm fine.\""

    van "(Come to think of it, {w=0.5}I don't think she knows I have the ability to read memories yet.)"

    zal "\"Jesus christ, {w=0.5}you scared the crap out of me!\""

    zal "\"You suddenly went expressionless, {w=0.5}and weren't moving an inch! {w=0.5}You didn't even respond to me!”\""

    van "\"Sorry that I made you worry. {w=0.5}I feel much better now.\""

    van "\"By the way, {w=0.5}I seem to have worked out what the news recorded on the tape was about.\""

    show zalmona_normal at zal_pos_2
    hide zalmona_panic
    with Dissolve(0.2)

    zal "\"Oh really? {w=0.5}Let's hear it. {w=0.5}What is it about?\""

    van "\"It's about Winston Loomis escaping from prison, {w=0.5}that one innocent employee who was framed by Myers.\""

    show zalmona_surprised at zal_pos_2
    hide zalmona_normal
    with Dissolve(0.2)

    zal "\"Oh, {w=0.5}I remember that!\""

    zal "\"From what I've heard, {w=0.5}no one knows where that guy is to this day.\""

    zal "\"But Detective, {w=0.5}you have to watch out, {w=0.5}I wouldn't have called him \"innocent\" if I were you.\""

    van "!?"

    van "\"Why do you say so?\""

    $ renpy.music.set_volume(0.6, delay=0, channel='music')
    play music "music/creepy.wav"

    hide zalmona_surprised
    show zalmona_normal at zal_pos_2
    with Dissolve(0.2)

    zal "\"It is indeed true that most rumors describe him as an innocent employee who was framed by Myers Corporation.\""

    zal "\"And I guess they're right to some extent.\""

    zal "\"The experiments on the cyborgs were not the work of Winston alone.\""

    zal "\"In fact, {w=0.5}every core member of Myers Corporation was aware of the existence of the project.\""

    zal "\"But together, {w=0.5}they chose to frame that poor researcher so as not to be implicated themselves.\""

    zal "\"However- {w=0.5}what many people forget to mention is-\""

    $ say_who = _("Zalmona")

    zal "\"Winston was indeed one of the researchers involved in the experiment.\""

    show zalmona_surprised at zal_pos_2
    hide zalmona_normal
    with Dissolve(0.2)

    $ say_who = ""

    zal "\"Speaking of which, {w=0.5}Detective, {w=0.5}you wanna know a fun fact?\""

    zal "\"Winston actually used to work right here in this lab.\""

    van "\"......\""

    show black with Dissolve(0.5)
    hide zalmona_normal
    hide zalmona_surprised
    hide zalmona_drop_shadow

    van "I see."

    van "So Winston wasn't innocent after all."

    van "However, {w=0.5}he was framed by other members of Myers Corporation to take the blame for the whole experiment."

    van "And in July 2081, {w=0.5}he managed to escape from prison with Vincent's help."

    van "Vincent mentioned that he needed Winston's knowledge, {w=0.5}but also Victor's help to master a certain technology."

    van "On one hand, {w=0.5}he wanted to use this technology to protect himself. {w=0.5}And on the other, {w=0.5}he wanted to seek out his revenge on Myers."

    van "As to what kind of technology that is... {w=0.5}I can make a good guess, {w=0.5}but I still need to confirm my suspicion."

    stop music fadeout 3.0

    hide black
    hide bedroom_dust
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    van "In any case, {w=0.5}let us continue the investigation."

    window hide

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    $ rollback_ = False
    $ renpy.block_rollback()
    $ _rollback = False

    show screen inventory_screen
    with Dissolve(0.2)

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music "music/bgm/lab investigation.ogg"

    call screen engineering_room_4_screen with Dissolve(0.2)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
