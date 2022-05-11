
image dorm1 = "images/RMU/dorm1.png"
image dorm2 = "images/RMU/dorm2.png"
image dorm3 = "images/RMU/dorm3.png"
image dorm4 = "images/RMU/dorm4.png"
image dorm5 = "images/RMU/dorm5.png"
image dorm_mono_1_1 = "images/RMU/dorm_mono_1_4.png"
image dorm_mono_1_0 = "images/RMU/dorm_mono_1_1.png"
image dorm_mono_1:
    "images/RMU/dorm_mono_1_1.png" with Dissolve(0.2)
    pause 0.15
    "images/RMU/dorm_mono_1_2.png" with Dissolve(0.2)
    pause 0.10
    "images/RMU/dorm_mono_1_3.png" with Dissolve(0.2)
image dorm_mono_1_lighting = "images/RMU/dorm_mono_1_lighting.png"
image dorm_mono_2 = "images/RMU/dorm_mono_2.png"
image dorm_mono_2_bg = "images/RMU/dorm_mono_2_bg.png"
image computer_text_box = "images/RMU/computer text box.png"
image dorm_mono_3_bg = "images/RMU/dorm_mono_3_bg.png"
image dorm_mono_3_bg_2 = "images/RMU/dorm_mono_3_bg_2.png"
image dorm_mono_3 = "images/RMU/dorm_mono_3.png"
image dorm_mono_1_shadow = "images/RMU/dorm_mono_1_shadow.png"
image dorm_mono_4_bg = "images/RMU/dorm_mono_4_bg.png"
image film_grain:
    "images/RMU/film grain 1.png"
    pause 0.2
    "images/RMU/film grain 2.png"
    pause 0.2
    "images/RMU/film grain 3.png"
    pause 0.2
    "images/RMU/film grain 4.png"
    pause 0.2
    repeat
image dorm_mono_4_1 = "images/RMU/dorm_mono_4_1.png"
image dorm_mono_4_2 = "images/RMU/dorm_mono_4_2.png"
image dorm_mono_4_3 = "images/RMU/dorm_mono_4_3.png"
image dorm_hot_coco = "images/RMU/dorm_hot_coco.png"


image dorm_door = "images/RMU/dorm_door.png"
image dorm_vincent_door_1 = "images/RMU/dorm_vincent_door_1.png"
image dorm_vincent_door_2 = "images/RMU/dorm_vincent_door_2.png"
image dorm_vincent_door_3 = "images/RMU/dorm_vincent_door_3.png"

image movie = Movie()

init python:

    def mono_zoom(st, at):
        return Transform("images/RMU/diamond.png", anchor=(0.5,0.5), pos=(0.5,0.5), zoom=at*5),0

define mono_irisout = AlphaDissolve( DynamicDisplayable(mono_zoom), 1.0 )

label college_start:

    $ renpy.free_memory()
    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = True
    $ _rollback = True

    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    $ renpy.pause(2.0, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music ("music/ambience/crowd.ogg") fadein 3.0 fadeout 3.0

    pause 4.0

    window show

    anon "\"Vincent Edgeworth, {w=0.5}is it? {w=0.5}Welcome to RMU!\""

    anon "\"Here's the key to your dorm. {w=0.5}Enjoy meeting your new roommate!\""

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

    $ renpy.pause(2.0, hard='True')

    show college_vin_normal
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    window show

    vin "\"......\""

    $ say_who = _("Vincent")

    show college_vin_think with Dissolve(0.2)

    vin " (......New roommate?)"

    window hide

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/dorm/knock door.ogg" fadeout 2.0

    pause 2.0

    show college_vin_surprised
    hide college_vin_think
    hide college_vin_normal
    with Dissolve(0.2)

    anon "\"Pardon me, {w=0.5}is anyone there? {w=0.5}I'm coming in.\""

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/open door.ogg" fadeout 1.0

    show college_vin_surprised:
        linear 0.5 xpos 0.73

    $ renpy.pause(1.0, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music ["<silence 1.0>", "music/bgm/dorm.ogg"]
    queue music "music/bgm/dorm.ogg"

    $ renpy.pause(1.0, hard='True')

    show college_vic_normal_flip at vic_pos_2
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.5, hard='True')

    show college_victor_talk_flip at vic_pos_2 with Dissolve(0.2)

    $ say_who = _("Victor")

    window show

    $ renpy.music.set_volume(0.7, delay=0, channel='sound')
    play sound "music/hehe.ogg"

    vic "\"Oh, {w=0.5}hello there! {w=0.5}Pleasure to meet you. {w=0.5}You're Vincent, {w=0.5}right?\""

    show college_victor_close_eye_talk_flip at vic_pos_2 with Dissolve(0.2)

    vic "\"Please allow me to introduce myself. {w=0.5}I am your roommate, {w=0.5}Victor Blake. {w=0.5}I'm majoring in Economics.\""

    hide college_victor_close_eye_talk_flip with Dissolve(0.2)

    vic "\"It is an incredible chance of fate for us to meet each other at this place, {w=0.5}don't you think?\""

    window hide

    hide college_victor_talk_flip
    with Dissolve(0.2)

    pause 1.0

    show college_vin_unpleased at vin_pos_2
    hide college_vin_surprised
    with Dissolve(0.2)

    $ say_who = _("Vincent")

    window show

    $ renpy.music.set_volume(0.4, delay=0, channel='sound')
    play sound "music/vin_hmm.ogg"

    vin "\"......An incredible chance of fate? {w=0.5}Don't make me laugh.\""

    show college_vin_unpleased2 at vin_pos_2 with Dissolve(0.2)

    vin "\"Everything exists for a reason. {w=0.5}Our life experiences are shaped by our own actions, {w=0.5}not fate.\""

    $ say_who = _("Victor")

    show college_victor_close_eye_talk_flip at vic_pos_2 with Dissolve(0.2)

    vic "\"Haha, {w=0.5}if you say so.\""

    show college_victor_talk_flip at vic_pos_2 with Dissolve(0.2)

    vic "\"But that also means, {w=0.5}there has to be a reason for both of us to be standing here, {w=0.5}correct?\""



    hide college_victor_talk_flip
    hide college_victor_close_eye_talk_flip
    with Dissolve(0.2)

    $ say_who = _("Vincent")

    vin "\"......\""

    window hide

    pause 1.0

    show college_vin_think at vin_pos_2
    hide college_vin_unpleased2
    with Dissolve(0.5)

    $ renpy.pause(0.5, hard='True')

    window show

    vin "\"I'd rather live in a single room.\""

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/shake.ogg"

    show college_victor_sweat_flip at vic_pos_2

    vic "\"......\"" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    $ say_who = _("Victor")

    show college_victor_sweat_talk_flip at vic_pos_2 with Dissolve(0.2)

    vic "\"I see that you're a pretty straightforward guy, {w=0.5}huh?\""

    hide college_victor_sweat_talk_flip
    hide college_victor_sweat_flip
    show college_victor_talk_flip at vic_pos_2
    with Dissolve(0.2)

    vic "\"I understand. {w=0.5}First day of school is always quite nerve-wracking, {w=0.5}isn't it?\""

    show college_victor_close_eye_talk_flip at vic_pos_2 with Dissolve(0.2)

    vic "\"But you can quote me on this, {w=0.5}I'm sure we're going to become great friends.\""

    hide college_victor_close_eye_talk_flip with Dissolve(0.2)

    vic "\"Anyway, {w=0.5}shall we start with some simple introductions? {w=0.5}Why don't we get to know each other a bit first?\""

    vic "\"Which district are you from, {w=0.5}Vincent?\""

    show college_vin_normal at vin_pos_2
    hide college_victor_talk_flip
    with Dissolve(0.2)

    vin "\"...The G4 district.\""

    show college_victor_close_eye_talk_flip at vic_pos_2 with Dissolve(0.2)

    vic "\"G4, {w=0.5}is it? {w=0.5}Same here. {w=0.5}Then it looks like we're both domestic students.\""

    show college_victor_talk_flip at vic_pos_2
    hide college_victor_close_eye_talk_flip
    with Dissolve(0.2)

    vic "\"What do you like about G4? {w=0.5}Where do you usually go to have fun?\""

    show college_vin_awk at vin_pos_2
    hide college_victor_talk_flip
    with Dissolve(0.2)

    vin "\"I... {w=0.5}I don't really go out much.\""

    show college_victor_speechless_flip at vic_pos_2
    with Dissolve(0.2)

    vic "\"I see...\""

    hide college_victor_speechless_flip
    show college_victor_talk_flip at vic_pos_2
    with Dissolve(0.2)

    vic "\"What about hobbies? {w=0.5}What do you like to do in your spare time?\""

    hide college_vin_awk
    hide college_victor_talk_flip
    with Dissolve(0.2)

    vin "\"...I enjoy reading about history and philosophy.\""

    show college_victor_talk_flip at vic_pos_2 with Dissolve(0.2)

    vic "\"Oh, {w=0.5}that's exciting! {w=0.5}What else?\""

    hide college_victor_talk_flip
    show college_vin_mad at vin_pos_2
    hide college_vin_normal
    hide college_vin_think
    with Dissolve(0.2)

    vin "\"...That's it. {w=0.5}Is that not enough?\""

    show college_victor_speechless_flip at vic_pos_2
    with Dissolve(0.2)

    vic "\"I see... {w=0.5}It seems like you've been working pretty hard huh, {w=0.5}Vincent?\""

    $ say_who = _("Vincent")

    show college_victor_close_eye_flip at vic_pos_2
    hide college_vin_mad
    with Dissolve(0.2)

    vin "\"......\""

    hide college_vin_normal
    hide college_vin_unpleased2
    show college_vin_think at vin_pos_2
    with Dissolve(0.2)

    vin "\"You think I'm boring?\""

    $ say_who = _("Victor")

    hide college_victor_speechless_flip
    hide college_victor_close_eye_flip
    show college_victor_sweat_talk_2_flip at vic_pos_2
    with Dissolve(0.2)

    vic "\"No no, {w=0.5}why would I? {w=0.5}If anything, {w=0.5}I should learn to be more like you.\""

    hide college_victor_sweat_talk_2_flip
    show college_victor_talk_flip at vic_pos_2
    with Dissolve(0.2)

    vic "\"Anyway, {w=0.5}I heard that there's going to be a freshman party tonight. {w=0.5}Would you like to come with me, {w=0.5}Vincent?\""

    hide college_vin_think
    hide college_victor_talk_flip
    show college_vin_unpleased at vin_pos_2
    with Dissolve(0.2)

    vin "\"...Not interested.\""

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/shake.ogg"

    show college_victor_sweat_flip at vic_pos_2
    vic "\"......\"" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    hide college_victor_sweat_flip
    show college_victor_talk_flip at vic_pos_2
    with Dissolve(0.2)

    vic "\"...Okay. {w=0.5}But what's wrong with making some new friends?\""

    show college_vin_think at vin_pos_2
    hide college_victor_talk_flip
    with Dissolve(0.2)

    $ say_who = _("Vincent")

    vin "\"Do I look like I'm here to make friends?\""

    hide college_vin_think
    hide college_vin_unpleased2
    show college_vin_unpleased at vin_pos_2
    with Dissolve(0.2)

    vin "\"You have absolutely no clue how much work I've put in over the last few years. {w=0.5}Being accepted by RMU is a well deserved milestone for me.\""

    show college_vin_unpleased2 at vin_pos_2
    with Dissolve(0.2)

    vin "\"But all the other idiots here think that just by getting here, {w=0.5}it means they've won in life.\""

    hide college_vin_unpleased2
    hide college_vin_unpleased
    show college_vin_close_eye_unpleased at vin_pos_2
    with Dissolve(0.2)

    vin "\"All the G4 students, {w=0.5}and even people from other districts, {w=0.5}want to study at this prestigious school.\""

    hide college_vin_close_eye_unpleased
    show college_vin_unpleased at vin_pos_2
    with Dissolve(0.2)

    vin "\"But for those people, {w=0.5}those three letters of 'RMU' merely serve as a title for them to show off.\""

    show college_vin_unpleased2 at vin_pos_2
    with Dissolve(0.2)

    vin "\"The true reason for them to celebrate on the first day is that their goal was just to get admitted here.\""

    $ say_who = _("Victor")

    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/hehe.ogg"

    show college_victor_close_eye_talk_flip at vic_pos_2 with Dissolve(0.2)

    vic "\"I see that you have pretty high expectations for others as well huh, {w=0.5}Vincent.\""

    show college_victor_talk_flip at vic_pos_2 with Dissolve(0.2)

    vic "\"However, {w=0.5}please allow me to disagree with you.\""

    vic "\"You're wrong to assume that those students are celebrating because they believe they no longer need to work hard,\""

    hide college_victor_talk_flip with Dissolve(0.2)

    vic "\"Perhaps for them, {w=0.5}RMU symbolizes the beginning of a new chapter in their life.\""

    hide college_victor_close_eye_talk_flip
    hide college_vin_unpleased2
    show college_vin_think at vin_pos_2
    with Dissolve(0.2)

    $ say_who = _("Vincent")

    vin "\"I could care less about what you think. {w=0.5}What remains unchanged is that they're wasting their time.\""

    hide college_vin_think
    show college_vin_unpleased2 at vin_pos_2
    with Dissolve(0.2)

    vin "\"But I am different. {w=0.5}I know I still have a long way to go.\""

    show college_vin_mad at vin_pos_2
    hide college_vin_unpleased2
    with Dissolve(0.2)

    vin "\"We are at the top university in the G4 district, {w=0.5}and not to mention, {w=0.5}the most competitive one. {w=0.5}RMU's acceptance rate is only 4.5 percent.\""

    vin "\"And because of that, {w=0.5}I will cherish my time here even more. {w=0.5}I will be focusing on my studies, {w=0.5}and only my studies. {w=0.5}Nothing else.\""

    hide college_vin_mad
    show college_vin_unpleased2 at vin_pos_2
    with Dissolve(0.2)

    vin "\"The competition is far from over. {w=0.5}If I dawdle now, {w=0.5}it will be no different than admitting defeat to others here.\""

    stop music fadeout 3.0

    show college_vin_close_eye_unpleased at vin_pos_2
    hide college_vin_unpleased
    hide college_vin_unpleased2
    with Dissolve(0.2)

    vin "\"I will only consider myself a success... {w=0.5}when I get hired by that place.\""

    window hide

    $ renpy.pause(1.0, hard='True')

    $ say_who = _("Victor")

    $ renpy.music.set_volume(0.8, delay=0, channel='sound1')
    $ renpy.music.play("music/dorm/zs_uneasy impact.ogg", channel="sound1", fadeout = 1.0, loop = False)

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music ("music/TenseMusic.ogg") fadein 6.0

    show college_victor_dark_flip at vic_pos_2
    with Dissolve(0.2)

    $ renpy.pause(2.0, hard='True')

    show college_victor_evil_flip at vic_pos_2
    hide college_victor_dark_flip
    with Dissolve(0.2)

    window show

    vic "\"...By that place?\""

    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/huh.ogg"

    hide college_vin_unpleased2
    hide college_victor_evil_flip
    show college_victor_mocking_2_flip at vic_pos_2
    show college_victor_mocking_flip at vic_pos_2
    hide college_victor_mocking_2_flip
    with Dissolve(0.5)

    vic "\"Well well well. {w=0.5}Let me guess, {w=0.5}could you possibly be aiming for... {w=0.5}{color=#f00}the Myers Corporation{/color}?\""

    show college_vin_unpleased2 at vin_pos_2
    show college_victor_mocking_3_flip at vic_pos_2
    hide college_vin_close_eye_unpleased
    with Dissolve(0.2)

    vic "\"That is hilarious.\""

    show college_vin_mad at vin_pos_2
    hide college_vin_unpleased2
    show college_victor_mocking_2_flip at vic_pos_2
    hide college_victor_mocking_flip
    hide college_victor_mocking_3_flip
    with Dissolve(0.2)

    $ renpy.music.set_volume(0.4, delay=0, channel='sound')
    play sound "music/vin_hmm.ogg"

    vin "\"...Are you mocking me?\""

    hide college_victor_mocking_2_flip
    show college_victor_close_eye_talk_flip at vic_pos_2
    with Dissolve(0.2)

    vic "\"Oh no. {w=0.5}Don't get me wrong.\""

    $ say_who = _("Victor")

    vic "\"I just think Vincent's adorable, {w=0.5}so adorable that I want to laugh.\""

    vic "\"I was worried for a second that my roommate was going to be boring as hell, {w=0.5}but now I see that I was terribly wrong.\""

    show college_victor_mocking_flip at vic_pos_2
    with Dissolve(0.2)

    vic "\"Every word you say can entertain me all day long.\""

    hide college_victor_mocking_flip
    show college_victor_mocking_2_flip at vic_pos_2
    show college_vin_mad_2 at vin_pos_2
    with Dissolve(0.2)

    vin "\"What did you just say?\""

    hide college_victor_mocking_2_flip
    with Dissolve(0.2)

    vic "\"My dear Vincent, {w=0.5}do you mind if I ask what your major is?\""

    show college_victor_close_eye_2_flip at vic_pos_2
    hide college_vin_mad_2
    with Dissolve(0.2)

    vin "\"...I am a law student.\""

    hide college_victor_close_eye_2_flip
    show college_victor_mocking_flip at vic_pos_2
    with Dissolve(0.2)

    vic "\"Law student, {w=0.5}huh? {w=0.5}Indeed, {w=0.5}you certainly don't look like an engineering student.\""

    hide college_victor_mocking_flip with Dissolve(0.2)

    vic "\"Do you really think studying hard is all you need to do to get into a top company in G4? {w=0.5}Quit joking around.\""

    show college_victor_mocking_flip at vic_pos_2
    with Dissolve(0.2)

    vic "\"Pure hard work is not the only thing that matters in the workplace; {w=0.5}socializing is also an integral part of it. {w=0.5}This is especially important for your chosen profession.\""

    show college_vin_mad_2 at vin_pos_2
    show college_victor_mocking_3_flip at vic_pos_2
    with Dissolve(0.2)

    vic "\"With such a lousy personality, {w=0.5}I shudder to think of the lonely life you lead.\""

    $ say_who = _("Victor")

    vic "\"Even if you do get into the Myers Corporation, {w=0.5}you will just be ostracized by everyone.\""

    hide college_victor_mocking_3_flip
    hide college_victor_mocking_flip
    with Dissolve(0.2)

    vic "\"Your co-workers won't like you, {w=0.5}and your boss will just think you're useless and incapable of understanding the ways of the world.\""

    vic "\"{color=#f00}It will be your fate to end up being an outcast, {w=0.5}and be forced to leave the Myers Corporation because you don't belong there.{/color}\""

    show college_victor_mocking_3_flip at vic_pos_2
    with Dissolve(0.2)

    vic "\"Oh, {w=0.5}wait. {w=0.5}Or should I say, {w=0.5}{color=#f00}this will be a life experience shaped by your own actions{/color}?\""

    hide college_victor_mocking_3_flip
    show college_victor_mocking_2_flip at vic_pos_2
    with Dissolve(0.2)

    vin "\"......\""

    stop music fadeout 6.0

    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/hehe.ogg"

    hide college_victor_mocking_2_flip
    with Dissolve(0.2)

    vic "\"But since you've already made up your mind, {w=0.5}there's nothing I can do about it. {w=0.5}I respect your decision.\""

    vic "\"But if you change your mind at any time, {w=0.5}please feel free to join us at the party.\""

    hide college_victor_close_eye_talk_flip
    show college_victor_talk_flip at vic_pos_2
    with Dissolve(0.2)

    vic "\"I hope to see you at the freshman party, {w=0.5}Vincent! {w=0.5}We'll catch up later.\""

    hide college_victor_talk_flip with Dissolve(0.2)

    window hide

    $ renpy.pause(0.5, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/open door.ogg" fadeout 1.0

    $ renpy.pause(0.8, hard='True')


    show college_victor_mocking_2_flip at vic_pos_2 with Dissolve(0.2)

    hide college_vic_normal_flip
    hide college_victor_mocking_2_flip
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')
    hide college_vin_mad
    hide college_vin_normal
    hide college_vin_unpleased
    hide college_vin_unpleased2

    $ say_who = ""
    $ renpy.pause(1.0, hard='True')

    show college_vin_mad_2:
        linear 0.5 xalign 0.5

    $ renpy.pause(1.0, hard='True')


    show college_vin_mad_2:
        xalign 0.5

    window show

    vin "\"......\""

    window hide

    $ renpy.pause(1.0, hard='True')

    show college_vin_sad
    hide college_vin_mad_2
    with Dissolve(0.5)

    pause 1.0

    window show

    vin "\"......\""

    window hide

    pause 2.0

    hide college_vin_sad
    show college_vin_mad_2
    with Dissolve(0.2)

    pause 2.0

    $ say_who = _("Vincent")

    window show

    vin "Unforgivable."

    vin "He had such a sickening smile on his face, {w=0.5}and his words were filled with nothing but sarcasm."

    vin "I resent hypocritical, arrogant scums like him more than those unproductive good-for-nothing students."

    show college_vin_mad_3 with Dissolve(0.2)

    vin "\"Myers' outcast\"... {w=0.5}My destiny is mine to decide."

    vin "I have not asked for your worthless opinions, {w=0.5}and certainly don't need a loser like you to mock my dreams."

    window hide

    pause 2.0

    hide college_vin_mad_3
    hide college_vin_mad_2
    hide college_vin_mad_1
    show college_vin_sad
    with Dissolve(0.2)

    window show

    vin "......"

    window hide

    pause 2.0

    hide college_vin_sad
    show college_vin_unpleased2
    with Dissolve(0.2)

    vin "I shouldn't be thinking about these useless matters."

    vin "Thank god he's left the room. {w=0.5}It will give me at least one more night alone."

    pause 1.0

    $ renpy.music.set_volume(0.1, delay=0, channel='sound')
    play sound "music/cloth.mp3" fadeout 2.0

    hide college_vin_unpleased2
    show transparent dark-small:
        alpha 0.8
    with Dissolve(1.0)

    pause 0.5

    show character_icon_box_1:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 700 ypos 50
        xpos 700 ypos 50
    show college_vin_icon_normal:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 700 ypos 48
        xpos 700 ypos 48
    show character_icon_box_2:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 700 ypos 50
        xpos 700 ypos 50

    vin "Instead of getting indignant about a guy like that, {w=0.5}I might as well use the evening to improve my knowledge furthermore."


    show character_icon_box_1:
        xpos 700 ypos 50
    show college_vin_icon_normal:
        xpos 700 ypos 48
    show character_icon_box_2:
        xpos 700 ypos 50

    vin "So, {w=0.5}which book should I start with today?"

    show college_vin_icon_think:
        xpos 700 ypos 48
    hide college_vin_icon_normal
    with Dissolve(0.5)

    pause 0.5

    vin "\"Being and Nothingness\", {w=0.5}\"Republic\", {w=0.5}\"The Birth of Tragedy\"..."

    pause 1.0

    show college_vin_icon_unpleased2:
        xpos 700 ypos 48
    with Dissolve(0.5)

    pause 1.0

    window show

    vin "Hmm... {w=0.5}Why don't we start with \"Leviathan\" today?"

    window hide

    $ say_who = ""

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/PageFlipshort.ogg"

    $ renpy.pause(1.0, hard='True')

    hide character_icon_box_1
    hide character_icon_box_2
    hide college_vin_icon_normal
    hide college_vin_icon_unpleased2
    hide college_vin_icon_think
    hide transparent dark-small
    with Dissolve(2.0)

    $ renpy.pause(2.0, hard='True')
    pause 2.0

    $ renpy.music.set_volume(0.7, delay=0, channel='music')
    play music "music/bgm/lonely night.ogg"

    $ renpy.pause(2.0, hard='True')
    pause 1.0

    scene dorm2
    with Dissolve(3.0)

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

    $ renpy.pause(2.0, hard='True')

    window show

    b "\"...And from this diffidence of one another, {w=0.5}there is no way for any man to secure himself so reasonable as anticipation; \""

    b "\"That is, {w=0.5}by force, {w=0.5}or wiles, {w=0.5}to master the persons of all men he can so long till he see no other power great enough to endanger him.\""

    window hide

    pause 2.0

    window show

    vin "\"......\""

    window hide

    $ renpy.pause(1.0, hard='True')

    show transparent dark-small:
        alpha 0.5
    with Dissolve(0.5)

    pause 0.5

    show character_icon_box_1:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 700 ypos 50
        xpos 700 ypos 50
    show college_vin_icon_unpleased2:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 700 ypos 48
        xpos 700 ypos 48
    show character_icon_box_2:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 700 ypos 50
        xpos 700 ypos 50

    $ renpy.pause(1.0, hard='True')

    $ say_who = _("Vincent")

    window show

    vin "\"Victor Blake\" was his name, {w=0.5}wasn't it?"


    show character_icon_box_1:
        xpos 700 ypos 50
    show college_vin_icon_unpleased2:
        xpos 700 ypos 48
    show character_icon_box_2:
        xpos 700 ypos 50

    vin "Come to think of it, {w=0.5}he was my first roommate and the first person I ever met here."

    show college_vin_icon_think:
        xpos 700 ypos 48
    hide college_vin_icon_unpleased2
    with Dissolve(0.2)

    vin "Maybe I shouldn't have given him the cold shoulder on the first day. {w=0.5}It wasn't the wisest thing to do."

    vin "After all, {w=0.5}I will be spending most of my time here in this tiny room with him."

    window hide

    pause 2.0

    show college_vin_icon_unpleased2:
        xpos 700 ypos 48
    hide college_vin_icon_think
    with Dissolve(0.2)

    pause 1.0

    window show

    vin "...No, {w=0.5}that's not true. {w=0.5}I should be able to move out and live alone next year."

    vin "I have no reason to put on a smile for this guy. {w=0.5}And I'm not in the mood to do that."

    window hide

    $ say_who = ""

    hide character_icon_box_1
    hide character_icon_box_2
    hide college_vin_icon_think
    hide college_vin_icon_unpleased2
    hide transparent dark-small
    hide dust
    with Dissolve(2.0)

    $ renpy.pause(2.0, hard='True')

    $ renpy.music.set_volume(0.6, delay=0, channel='background noise')
    $ renpy.music.play("music/night.ogg", channel="background noise", fadeout = 6.0, fadein = 6.0, loop = True)

    scene dorm3
    show firefly_particles
    with Dissolve(5.0)

    pause 2.0

    window show

    b "\"...Law can never be against reason, {w=0.5}our lawyers are agreed: \""

    b "\"And that not the letter (that is, {w=0.5}every construction of it), {w=0.5}but that which is according to the intention of the legislator, {w=0.5}is the law.\""

    window hide

    pause 2.0

    window show

    vin "\"......\""

    window hide

    $ renpy.pause(1.0, hard='True')

    show transparent dark-small:
        alpha 0.5
    with Dissolve(0.5)

    pause 0.5

    show character_icon_box_1:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 700 ypos 50
        xpos 700 ypos 50
    show college_vin_icon_unpleased2:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 700 ypos 48
        xpos 700 ypos 48
    show character_icon_box_2:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 700 ypos 50
        xpos 700 ypos 50

    $ renpy.pause(1.0, hard='True')


    show character_icon_box_1:
        xpos 700 ypos 50
    show college_vin_icon_unpleased2:
        xpos 700 ypos 48
    show character_icon_box_2:
        xpos 700 ypos 50

    window show

    vin "It's 12 o'clock. {w=0.5}When is this guy going to return?"

    window hide

    pause 2.0

    show college_vin_icon_think:
        xpos 700 ypos 48
    hide college_vin_icon_unpleased2
    with Dissolve(0.2)

    window show

    vin "...Why am I thinking about him? {w=0.5}His lifestyle is definitely none of my business."

    vin "lt feels as if I'm eagerly waiting for him to come back? {w=0.5}...I don't understand."

    window hide

    window hide

    hide character_icon_box_1
    hide character_icon_box_2
    hide college_vin_icon_think
    hide college_vin_icon_unpleased2
    hide transparent dark-small
    with Dissolve(2.0)

    $ renpy.pause(2.0, hard='True')

    $ renpy.music.stop(channel="background noise", fadeout = 6.0)

    show dorm4 behind firefly_particles
    with Dissolve(5.0)

    $ say_who = ""

    window show

    b "\"...Not that the death of one man, {w=0.5}though without sin, {w=0.5}can satisfy for the offences of all men,\""

    b "\"In the rigour of justice, {w=0.5}but in the mercy of God, {w=0.5}that ordained such sacrifices for sin as he was pleased in his mercy to accept.\""

    window hide

    pause 1.0

    $ renpy.pause(1.0, hard='True')

    show transparent dark-small:
        alpha 0.5
    with Dissolve(0.5)

    pause 0.5

    show character_icon_box_1:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 700 ypos 50
        xpos 700 ypos 50
    show college_vin_icon_mad_4:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 700 ypos 48
        xpos 700 ypos 48
    show character_icon_box_2:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 700 ypos 50
        xpos 700 ypos 50

    $ renpy.pause(1.0, hard='True')


    show character_icon_box_1:
        xpos 700 ypos 50
    show college_vin_icon_mad_4:
        xpos 700 ypos 48
    show character_icon_box_2:
        xpos 700 ypos 50

    window show

    $ say_who = _("Vincent")

    vin "\"......\""

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/shake.ogg"

    show college_vin_icon_mad_2:
        xpos 700 ypos 48
    hide college_vin_icon_mad_4

    vin "It's 3:30 in the morning. {w=0.5}This is inexcusable!" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    show college_vin_icon_mad_4:
        xpos 700 ypos 48
    hide college_vin_icon_mad_2
    with Dissolve(0.2)

    vin "Victor, {w=0.5}on your very first day at RMU, {w=0.5}all you do is party until the wee hours of the morning. {w=0.5}Where did you get the confidence to speak to me like that?"

    window hide

    $ say_who = ""

    stop music fadeout 6.0

    pause 2.0

    show college_vin_icon_sad:
        xpos 700 ypos 48
    hide college_vin_icon_mad_4
    with Dissolve(0.5)

    pause 2.0

    window show

    vin "......"

    window hide

    pause 2.0

    hide character_icon_box_1
    hide character_icon_box_2
    hide college_vin_icon_sad
    hide transparent dark-small
    with Dissolve(2.0)

    pause 2.0

    window show

    vin "What was I even worried about?"

    vin "After all, {w=0.5}I'll be spending this year alone again, {w=0.5}but in this room, {w=0.5}won't I?"

    window hide


    stop music fadeout 2.0

    $ renpy.music.set_volume(0.8, delay=0, channel='music')
    play music ["<silence 2.0>", "music/bgm/hl_song3.ogg"] fadeout 6.0

    $ renpy.pause(2.0, hard='True')
    pause 2.0
    $ renpy.pause(0.1, hard='True')

    show black
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    pause 2.0

    show movie:
        alpha 0.2
    play movie "movies/vb_light.webm"
    show myers_lobby_draco_battle_explanation_1 onlayer ab_parallax:
        yoffset 50
    show myers_lobby_draco_battle_explanation_2 onlayer ab_parallax:
        yoffset -50
    show myers_lobby_draco_battle_explanation_wheel onlayer ab_parallax:
        parallel:
            rotate 0
            linear 8.0 rotate 360
            repeat
        parallel:
            xpos -425 ypos 0
    show myers_lobby_draco_battle_explanation_wheel_2 onlayer ab_parallax:
        parallel:
            rotate 0
            linear 8.0 rotate -360
            repeat
        parallel:
            xpos 975 ypos 0
    with Dissolve(2.0)

    pause 1.0

    $ renpy.music.set_volume(0.3, delay=0, channel='background noise')
    $ renpy.music.play("music/John Past/gossip-whispers.ogg", channel="background noise", loop = True, fadeout = 10.0, fadein = 3.0)

    noname_proto_3 "{cps=15}\"Geniuses are often born in isolation, {p=0.5}with a lonely destiny.\"{/cps}"

    noname_proto_3 "{cps=15}\"They often have a tendency for self-abandonment,\"{/cps}"

    noname_proto_3 "{cps=15}\"To abandon everything for \ntheir ideals.\"{/cps}"

    hide myers_lobby_draco_battle_explanation_1 onlayer ab_parallax
    hide myers_lobby_draco_battle_explanation_2 onlayer ab_parallax
    hide myers_lobby_draco_battle_explanation_wheel onlayer ab_parallax
    hide myers_lobby_draco_battle_explanation_wheel_2 onlayer ab_parallax
    hide movie
    with Dissolve(1.0)

    stop movie
    hide movie

    $ renpy.pause(2.0, hard='True')

    scene black
    show dorm_mono_1_lighting:
        linear 0.01 alpha 0.9
        linear 0.01 alpha 1
        repeat
    show firefly_particles

    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    $ renpy.music.stop(channel="background noise", fadeout=3.0)
    pause 1.0

    window show

    vin "Nothing is predestined in life."

    vin "I've always believed that ever since I was a child."

    vin "A person's destiny can be changed by no one but themselves."

    window hide

    pause 2.0

    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/KILLSWITCH.ogg" fadeout 5.0

    show movie behind firefly_particles:
        alpha 0.7 zoom 0.7
    play movie "movies/vb_particle.webm"
    show dorm_mono_1 behind firefly_particles:
        zoom 0.8 xalign 0.8 yalign 0.45
    $ renpy.transition(Dissolve(0.2))
    $ renpy.pause(1.0, hard=True)

    show textbox4:
        xanchor 0.5 yanchor 0.5 ypos 140 xpos 1020 alpha 1.0 zoom 1.0 xzoom 1.05
    $ renpy.transition(Dissolve(0.2))
    $ renpy.pause(0.2, hard=True)

    vin_vertical_2 "Ordinary people obey fate - "

    vin_vertical_2 "But the strong ones become rulers of their own destiny."

    show dorm_mono_1 behind firefly_particles:
        ease 0.5 zoom 0.5 xalign 0.5 yalign 0.5
    show textbox4:
        linear 0.2 alpha 0 yzoom 0.01

    $ renpy.pause(0.2, hard='True')

    show textbox4:
        xanchor 0.5 yanchor 0.5 ypos 540 xpos 260 zoom 1.0 xzoom 1.05 yzoom 0.01 alpha 0
        linear 0.2 alpha 1.0 yzoom 1.0

    vin_vertical_1 "To enter Myers Corporation, "

    vin_vertical_1 "And become the crème de la crème of the crème de la crème,"

    vin_vertical_1 "Is my goal."

    $ renpy.pause(0.01, hard='True')

    $ renpy.music.set_volume(0.2, delay=0, channel='sound')
    play sound "music/static_long.ogg"

    hide movie
    hide dorm_mono_1
    show dorm_mono_2 behind textbox4
    show dorm_mono_2_bg behind dorm_mono_2:
        alpha 0.1
        linear 3.0 alpha 0.9
    show game_over_static behind dorm_mono_2_bg:
        alpha 0.4
        ease 2.0 alpha 0.5
    show film_grain behind textbox4:
        alpha 0.8
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.5, hard=True)

    stop movie
    hide movie

    vin_vertical_1 "But why?"

    vin_vertical_1 "Why do I still feel so helpless sometimes..."

    vin_vertical_1 "...in the face of so-called \"fate\"?"

    show textbox4:
        linear 0.3 alpha 0
    $ renpy.pause(1.5, hard=True)
    show dorm_mono_2:
        alpha 1
        linear 1.0 alpha 0
    $ renpy.pause(0.1, hard=True)
    show ab_particles
    show transparent dark-small:
        alpha 0.8
    show myers_lobby_draco_battle_explanation_1 onlayer ab_parallax:
        yoffset 50
    show myers_lobby_draco_battle_explanation_2 onlayer ab_parallax:
        yoffset -50
    show myers_lobby_draco_battle_explanation_wheel onlayer ab_parallax:
        parallel:
            rotate 0
            linear 8.0 rotate 360
            repeat
        parallel:
            xpos -425 ypos 0
    show myers_lobby_draco_battle_explanation_wheel_2 onlayer ab_parallax:
        parallel:
            rotate 0
            linear 8.0 rotate -360
            repeat
        parallel:
            xpos 975 ypos 0
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard=True)

    pause 1.0

    $ renpy.music.set_volume(0.3, delay=0, channel='background noise')
    $ renpy.music.play("music/John Past/gossip-whispers.ogg", channel="background noise", loop = True, fadeout = 10.0, fadein = 3.0)

    noname_proto_3 "{cps=15}\"The real loneliness is a deep void, {p=0.5}an emptiness that will drive you crazy.\"{/cps}"

    noname_proto_3 "{cps=15}\"Even in the midst of cheering,\"{/cps}"

    $ renpy.music.stop(channel="background noise", fadeout=4.0)

    noname_proto_3 "{cps=15}\"You feel nothing but emptiness,{p=0.5} melancholy and frustration inside you.\"{/cps}"

    $ renpy.music.stop(channel="background noise")

    $ renpy.music.set_volume(0.3, delay=0, channel='sound')
    play sound "music/dorm/zs_whoosh.ogg"

    $ renpy.music.set_volume(0.5, delay=0, channel='background noise')
    $ renpy.music.play("music/ambience/crowd.ogg", channel="background noise", loop = True, fadeout = 10.0, fadein = 3.0)

    hide myers_lobby_draco_battle_explanation_1 onlayer ab_parallax
    hide myers_lobby_draco_battle_explanation_2 onlayer ab_parallax
    hide myers_lobby_draco_battle_explanation_wheel onlayer ab_parallax
    hide myers_lobby_draco_battle_explanation_wheel_2 onlayer ab_parallax
    show transparent dark-small:
        linear 0.5 alpha 0
    hide dorm_mono_2
    scene dorm_mono_3_bg
    show film_grain
    show dorm_mono_3:
        zoom 0.9
        parallel:
            alpha 0
            ease 0.5 alpha 1
            pause 6.5
            ease 3.0 alpha 0
        parallel:
            xalign 0.8 yalign 1.0
            linear 10.0 yalign 0.80
    show black-bg as black_bg_1:
        ypos -700
        ease 1.0 ypos -650
    show black-bg as black_bg_2:
        ypos 600
        ease 1.0 ypos 650
    $ renpy.transition(mono_irisout)
    $ renpy.pause(1.0, hard=True)

    pause 1.0

    show textbox4:
        xanchor 0.5 yanchor 0.5 ypos 540 xpos 260 xzoom 1.05 yzoom 0.01 alpha 0
        linear 0.2 alpha 1.0 yzoom 1.0
    $ renpy.pause(0.1, hard=True)

    vin_vertical_1 "When I stand in the middle of a crowd,"

    vin_vertical_1 "I feel even more lonely and out of place than I do when I am alone."

    show textbox4:
        linear 0.2 alpha 0

    hide dorm_mono_3
    show dorm_mono_3_bg_2 behind film_grain
    show dorm_mono_3 as dorm_mono_3_2 behind black_bg_1:
        zoom 0.9
        parallel:
            alpha 0
            ease 0.5 alpha 1
            pause 6.5
            ease 3.0 alpha 0
        parallel:
            xalign 1.1 yalign 0.28
            linear 15.0 yalign -0.10
    show black-bg as black_bg_1:
        ease 1.0 ypos -680
    show black-bg as black_bg_2:
        ease 1.0 ypos 620
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(1.0, hard=True)

    show textbox4:
        xanchor 0.5 yanchor 0.5 ypos 140 xpos 1020 xzoom 1.1 yzoom 0.01 alpha 0
        linear 0.2 alpha 1.0 yzoom 1.0
    $ renpy.pause(0.1, hard=True)

    vin_vertical_2 "I look at all the people drinking and chatting, {w=0.5}and can only ask myself:"

    scene dorm_mono_4_bg
    show film_grain
    show dorm_mono_4_2 behind film_grain
    show dorm_mono_4_3 behind film_grain
    show dorm_mono_4_1 behind film_grain
    hide dorm_mono_3_2
    show black-bg as black_bg_1:
        ypos -685
    show black-bg as black_bg_2:
        ypos 650
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard=True)

    show textbox4:
        xanchor 0.5 yanchor 0.5 ypos 540 xpos 260 xzoom 1.05 yzoom 0.01 alpha 0
        linear 0.2 alpha 1.0 yzoom 1.0

    vin_vertical_1 "\"Why don't I feel the same joy as they do?\""

    vin_vertical_1 "\"Have I really abandoned everything that I deserve...\""

    vin_vertical_1 "\"...to pursue my dream?\""

    vin_vertical_1 "\"Is the loneliness that I feel...\""

    vin_vertical_1 "\"...A price that I must pay?\""

    show textbox4:
        linear 0.2 alpha 0
    $ renpy.pause(0.2, hard=True)

    $ renpy.music.set_volume(0.3, delay=0, channel='sound')
    play sound "music/dorm/zs_whoosh.ogg"

    show dorm_mono_4_1:
        ease 1.0 xoffset -900
    show dorm_mono_4_2:
        ease 1.0 xoffset 500
    show dorm_mono_4_3:
        ease 1.0 zoom 2.0 xoffset 510
    scene black
    $ renpy.transition(mono_irisout)
    $ renpy.pause(1.0, hard=True)

    $ renpy.music.stop(channel="background noise", fadeout=6.0)

    show dorm_mono_1_lighting:
        alpha 0
    show firefly_particles:
        alpha 0

    pause 1.5

    window show

    vin "I know better than anyone else that coming here won't change anything."

    vin "\"It's a brand-new year, {w=0.5}I hope all the misfortunes will go away.\""

    vin "\"I'm going to be an adult soon, {w=0.5}perhaps I'll be more mature then.\""

    vin "Or maybe..."

    show dorm_mono_1_lighting:
        linear 1.0 alpha 0.9
        block:
            linear 0.01 alpha 0.9
            linear 0.01 alpha 1
            repeat
    show firefly_particles:
        linear 1.0 alpha 1

    vin "\"{color=#f00}I'll finally be able to make real friends when I go to my new school.{/color}\""

    window hide

    show movie behind dorm_mono_1_lighting:
        alpha 0.05
    play movie "movies/vb_light.webm"
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard=True)

    pause 1.0

    window show

    vin "Birthdays, {w=0.5}New Years, {w=0.5}New Schools..."

    vin "I've heard similar prayers all my life."

    vin "Humans always like to place hopes on useless things that make them feel like a turnaround will come out of nowhere."

    vin "They willingly blind themselves,"

    vin "And are reluctant to see the truth that many of the changes in their lives need to be done by themselves."

    vin "What will change in the New Year if you don't do anything?"

    vin "How will you become more mature if you don't even try to improve yourself?"

    window hide

    stop music fadeout 10.0

    hide movie
    scene black
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard=True)

    stop movie
    hide movie

    window show

    vin "But in the end, {w=0.5}I realized:"

    vin "I'm really not that different from them."

    vin "I had hoped that my life would change when I came to RMU."

    vin "{color=#f00}I had hoped that I would find real friends at RMU.{/color}"

    window hide

    pause 2.0
    $ renpy.pause(0.1, hard=True)

    scene dorm5
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
    $ renpy.transition(Dissolve(2.0))
    $ renpy.pause(2.0, hard=True)

    pause 3.0

    show character_icon_box_1:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 700 ypos 50
        xpos 700 ypos 50
    show college_vin_icon_unpleased2:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 700 ypos 48
        xpos 700 ypos 48
    show character_icon_box_2:
        xpos 1350 ypos 50
        easein_expo 1.0 xpos 700 ypos 50
        xpos 700 ypos 50

    $ renpy.pause(1.0, hard='True')


    show character_icon_box_1:
        xpos 700 ypos 50
    show college_vin_icon_unpleased2:
        xpos 700 ypos 48
    show character_icon_box_2:
        xpos 700 ypos 50

    window show

    vin "......"

    show college_vin_icon_normal:
        xpos 700 ypos 48
    hide college_vin_icon_unpleased2

    vin "It's 5 in the morning. {w=0.5}Looks like I won't be getting any sleep today."

    vin "I might as well pack up and get ready for the first day of school."

    window hide

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/dorm/knock door.ogg" fadeout 2.0

    pause 2.0

    hide college_vin_icon_normal
    show college_vin_icon_surprised:
        xpos 700 ypos 48
    with Dissolve(0.5)

    vin "!?"

    hide character_icon_box_1
    hide college_vin_icon_surprised
    hide character_icon_box_2
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard=True)

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/open door.ogg" fadeout 1.0

    pause 1.0

    $ renpy.pause(0.1, hard=True)

    show college_vin_surprised_2
    with Dissolve(1.0)

    pause 1.0

    $ renpy.music.set_volume(0.6, delay=0, channel='music')
    play music "music/scary violin loop.ogg" fadein 5.0 fadeout 2.0

    show college_vin_surprised
    hide college_vin_surprised_2
    with Dissolve(0.2)

    vin "\"...Victor?\""

    show college_vin_surprised:
        linear 0.5 xpos 0.73

    $ renpy.pause(1.0, hard='True')

    show college_victor_sick_flip at vic_pos_2
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard=True)

    show college_victor_sick_2_flip at vic_pos_2
    with Dissolve(0.2)

    $ say_who = _("Victor")

    window show

    vic "\"Vin, {w=0.5}Vincent? {w=0.5}You're still awake?\""

    hide college_victor_sick_2_flip at vic_pos_2
    with Dissolve(0.2)

    vic "\"I, {w=0.5}I'm not feeling so well...\""

    vic "\"I, {w=0.5}I think I might be...\""

    window hide

    $ say_who = ""

    $ renpy.pause(0.2, hard=True)

    $ renpy.music.set_volume(0.6, delay=0, channel='sound1')
    $ renpy.music.play("music/jumpscare/jumpscare 1.ogg", channel="sound1", fadeout = 1.0, loop = False)

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/dorm/zs_collapse.ogg" fadeout 1.0

    show black:
        alpha 0 zoom 1.5 xalign 0.5 yalign 0.5
        linear 0.2 alpha 1

    show college_victor_sick_flip:
        xanchor 0.5 yanchor 0.75
        linear 0.2 rotate 45 ypos 1.4 xpos 0.5

    $ renpy.pause(0.2, hard=True)

    stop music fadeout 1.0

    with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    vin "!?"

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/shock2.ogg" fadeout 2.0

    vin "\"Victor?{w=0.5} Victor!\"" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    $ renpy.pause(1.0, hard=True)
    pause 4.0
    $ renpy.pause(0.1, hard=True)

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
    $ renpy.pause(1.0, hard=True)

    $ renpy.music.set_volume(0.6, delay=0, channel='background noise')
    $ renpy.music.play("music/ambience/zs_birds.ogg", channel="background noise", fadeout = 6.0, fadein = 6.0, loop = True)

    pause 2.0
    $ renpy.pause(0.1, hard=True)

    show character_icon_box_1 as second_character_icon_box_1:
        xpos -300 ypos 250 alpha 0
        easein 1.0 xpos 200 ypos 250 alpha 1
        xpos 200 ypos 250
    show college_vic_icon_unwell_flip:
        xpos -300 ypos 248 alpha 0
        easein 1.0 xpos 200 ypos 248 alpha 1
        xpos 200 ypos 248
    show character_icon_box_2 as second_character_icon_box_2:
        xpos -300 ypos 250 alpha 0
        easein 1.0 xpos 200 ypos 250 alpha 1
        xpos 200 ypos 250

    pause 3.0

    window show
    vic "\"Ugh......\""
    window hide

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music ("music/bgm/dorm.ogg")

    pause 2.0
    $ renpy.pause(0.1, hard=True)

    show character_icon_box_1:
        xpos 1350 ypos 50 alpha 0
        easein 1.0 xpos 700 ypos 50 alpha 1
        xpos 700 ypos 50
    show college_vin_icon_normal:
        xpos 1350 ypos 50 alpha 0
        easein 1.0 xpos 700 ypos 48 alpha 1
        xpos 700 ypos 48
    show character_icon_box_2:
        xpos 1350 ypos 50 alpha 0
        easein 1.0 xpos 700 ypos 50 alpha 1
        xpos 700 ypos 50

    pause 1.0

    window show
    vin "\"You're awake? {w=0.5}Are you feeling any better?\""
    window hide

    show character_icon_box_1 as second_character_icon_box_1:
        xpos 200 ypos 250
    show character_icon_box_2 as second_character_icon_box_2:
        xpos 200 ypos 250
    show college_vic_icon_sad_flip behind character_icon_box_2:
        xpos 200 ypos 248
    hide college_vic_icon_unwell_flip
    with Dissolve(0.5)

    pause 1.0

    window show
    vic "\"......\""
    window hide

    $ renpy.music.stop(channel="background noise", fadeout = 5.0)

    hide character_icon_box_1
    hide college_vic_icon_sad_flip
    hide character_icon_box_2
    hide second_character_icon_box_1
    hide second_character_icon_box_2
    hide college_vin_icon_normal
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard=True)

    pause 1.0
    $ renpy.pause(0.1, hard=True)

    show college_victor_sad_3_flip at vic_pos_2
    show college_vin_normal at vin_pos_2
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard=True)

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/hmm.ogg"

    show college_victor_sad_2_flip at vic_pos_2
    hide college_victor_sad_3_flip
    with Dissolve(0.5)

    window show

    vic "\"...What time is it? {w=0.5}How long have I been asleep?\""

    show college_vin_unpleased at vin_pos_2
    hide college_vin_normal
    with Dissolve(0.2)

    vin "\"It's already noon.\""

    show college_victor_sad_3_flip at vic_pos_2
    hide college_victor_sad_2_flip
    with Dissolve(0.2)

    vic "\"...Oh god. {w=0.5}I've missed all my morning classes.\""

    $ renpy.music.set_volume(0.4, delay=0, channel='sound')
    play sound "music/vin_hmm.ogg"

    show college_vin_mad_2 at vin_pos_2
    hide college_vin_unpleased
    with Dissolve(0.2)

    vin "\"Well, {w=0.5}am I supposed to congratulate you? {w=0.5}Not only that, {w=0.5}but you've made me miss all my morning classes as well.\""

    show college_victor_sad_2_flip at vic_pos_2
    hide college_victor_sad_3_flip
    with Dissolve(0.3)

    vic "\"I'm, {w=0.5}I'm sorry...\""

    $ say_who = _("Vincent")

    hide college_vin_mad_2
    show college_vin_normal at vin_pos_2
    with Dissolve(0.5)

    vin "\"Perhaps you don't remember, {w=0.5}but the doctor from the infirmary has visited here.\""

    show college_vin_unpleased at vin_pos_2
    hide college_vin_normal
    with Dissolve(0.2)

    vin "\"I was worried that you were seriously ill, {w=0.5}but the doctor said that it seemed to be a case of over-exhaustion and stress.\""

    hide college_vin_unpleased
    show college_vin_normal at vin_pos_2
    with Dissolve(0.2)

    vin "\"She said that with some rest, {w=0.5}you should be able to recover soon.\""

    $ say_who = _("Victor")

    show college_victor_sad_3_flip at vic_pos_2
    hide college_victor_sad_2_flip
    with Dissolve(0.2)

    vic "\"...Is that so. {w=0.5}Thank goodness.\""

    show college_victor_sad_2_flip at vic_pos_2
    hide college_victor_sad_3_flip
    with Dissolve(0.2)

    vic "\"But if that's the case, {w=0.5}why are you still here with me?\""

    $ say_who = _("Vincent")

    show college_vin_awk at vin_pos_2
    hide college_vin_normal
    with Dissolve(0.3)

    vin "\"......\""

    show college_vin_normal at vin_pos_2
    hide college_vin_awk
    with Dissolve(0.3)

    vin "\"I guess I just wanted to make sure you were feeling better when you woke up with my own eyes.\""

    window hide

    $ renpy.music.set_volume(0.1, delay=0, channel='sound')
    play sound "music/cloth.mp3" fadeout 2.0

    $ renpy.pause(1.0, hard=True)

    show college_vin_normal:
        xpos 0.73 alpha 1
        linear 0.3 xpos 0.78 alpha 1
    show college_victor_sad_2_flip:
        xpos 0.25 alpha 1
        linear 0.3 xpos 0.18 alpha 1

    $ renpy.pause(0.3, hard=True)

    show transparent dark-small:
        alpha 0.8
    show dorm_hot_coco
    show college_vin_awk at vin_pos_3
    show college_victor_surprised_flip at vic_pos_3
    with Dissolve(0.5)

    window show

    vin "\"I wasn't quite sure what I was supposed to do, {w=0.5}so I bought you a cup of hot chocolate. {w=0.5}I also asked them to make the foam on top in the shape of a kitten.\""

    window hide

    $ say_who = ""

    pause 1.5

    window show

    vic "\"......\""

    show college_victor_happy_flip at vic_pos_3
    hide college_victor_surprised_flip
    hide college_victor_sad_2_flip
    $ renpy.transition(Dissolve(0.2))
    $ renpy.pause(0.2, hard='True')

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/shake.ogg"

    vic "\"Pfft hahahahaha!\"" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    $ renpy.music.set_volume(0.4, delay=0, channel='sound')
    play sound "music/vin_hmm.ogg"

    show college_vin_mad_2 at vin_pos_3
    hide college_vin_awk
    hide college_vin_normal
    with Dissolve(0.2)

    vin "\"...What's so funny?\""

    show college_victor_talk_2_flip at vic_pos_3
    hide college_victor_happy_flip
    with Dissolve(0.2)

    vic "\"No, {w=0.5}nothing.\""

    hide transparent dark-small
    hide dorm_hot_coco
    with Dissolve(0.3)

    show college_vin_mad_2:
        xpos 0.78 alpha 1
        linear 0.3 xpos 0.73 alpha 1
    show college_victor_talk_2_flip:
        xpos 0.18 alpha 1
        linear 0.3 xpos 0.25 alpha 1

    $ renpy.pause(0.3, hard=True)

    show college_victor_sad_flip at vic_pos_2
    hide college_victor_talk_2_flip
    with Dissolve(0.2)

    vic "\"But why, {w=0.5}Vincent? {w=0.5}After all that I said?\""

    $ say_who = _("Vincent")

    show college_vin_think at vin_pos_2
    hide college_vin_mad_2
    with Dissolve(0.2)

    vin "\"To be honest, {w=0.5}I'd rather just turn a blind eye to you. {w=0.5}I don't want to have anything to do with your life or death.\""

    show college_vin_close_eye_unpleased at vin_pos_2
    hide college_vin_think
    with Dissolve(0.2)

    vin "\"But you're my roommate, {w=0.5}so you're part of my responsibilities. {w=0.5}I had no other choice.\""

    $ say_who = ""

    show college_victor_sad_3_flip at vic_pos_2
    hide college_victor_sad_flip
    with Dissolve(0.2)

    vic "\"......\""

    show college_vin_mad_2 at vin_pos_2
    hide college_vin_close_eye_unpleased
    with Dissolve(0.2)

    vin "\"What were you thinking? {w=0.5}Ruining your body by partying into the early hours of the morning the day before school started?\""

    window hide

    pause 1.5

    window show

    show college_victor_sad_flip at vic_pos_2
    hide college_victor_sad_3_flip
    with Dissolve(0.2)

    vic "\"...{w=0.5}I didn't go.\""

    show college_vin_surprised at vin_pos_2
    hide college_vin_mad_2
    with Dissolve(0.2)

    vin "\"What?\""

    show college_victor_sad_2_flip at vic_pos_2
    hide college_victor_sad_flip
    with Dissolve(0.2)

    vic "\"I didn't go to the freshman party.\""

    window hide

    pause 1.5

    window show

    show college_vin_surprised_2 at vin_pos_2
    hide college_vin_surprised
    with Dissolve(0.2)

    vin "\"Then what were you doing all night?\""

    show college_victor_sad_3_flip at vic_pos_2
    hide college_victor_sad_2_flip
    with Dissolve(0.2)

    vic "\"*Sigh* {w=0.5}Isn't it obvious? {w=0.5}I wanted to get away from you.\""

    show college_vin_mad_3 at vin_pos_2
    hide college_vin_surprised_2
    with Dissolve(0.2)

    vin "\"...Get away from me? {w=0.5}Am I that obnoxious to you?\""

    stop music fadeout 3.0

    show college_victor_sad_2_flip at vic_pos_2
    hide college_victor_sad_3_flip
    with Dissolve(0.2)

    vic "\"No, {w=0.5}it's because of the things you said.\""

    show college_victor_sad_3_flip at vic_pos_2
    hide college_victor_sad_2_flip
    show college_vin_normal at vin_pos_2
    hide college_vin_mad_3
    with Dissolve(0.2)

    vic "\"It may not seem like it, {w=0.5}but I haven't slept well for days on end.\""
    window hide

    pause 2.0
    $ renpy.pause(0.1, hard='True')

    scene black
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    pause 1.0

    show dorm_mono_1_lighting:
        linear 0.01 alpha 0.9
        linear 0.01 alpha 1
        repeat
    show firefly_particles

    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')
    pause 1.0

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music "music/what happened.ogg"

    window show

    vic "\"Late into every night, {w=0.5}I'm plagued by a million thoughts.\""

    vic "\"I never knew what I was going to do when I got here.\""

    vic "\"Everything about the future terrifies me.\""

    vic "\"My goal was to get accepted to RMU, {w=0.5}but a lot of the time it felt like I was just carrying out my family's expectations of me.\""

    vic "\"'You have to make us proud.' {w=0.5}That was what my parents would always say to me.\""

    vic "\"But when I finally got here, {w=0.5}I just felt lost and overwhelmed.\""

    vic "\"I made it to RMU. {w=0.5}I have succeeded, {w=0.5}right?\""

    vic "\"But then what? {w=0.5}What happens after that?\""

    vic "\"Why isn't anyone telling me what to do next?\""

    vic "\"It was as if I was standing on the last step of a staircase, {w=0.5}but it didn't lead anywhere.\""

    vic "\"That's when I realized: {w=0.5}{color=#f00}I had not a single clue what I wanted{/color}.\""

    window hide

    pause 1.0

    window show

    vic "\"And then I met you. {w=0.5}And that feeling became stronger and stronger.\""

    vic "\"Everything about you irritated me.\""

    vic "\"Your condescending attitude and the way you talked without any consideration for others made me want to punch you in the face.\""

    vic "\"- If only that was the truth.\""

    vic "\"One night spent in the cold sobered me up: {w=0.5}I was not actually angry with you. {w=0.5}I was just disappointed in myself.\""

    vic "\"Because you're different from me, {w=0.5}Vincent. {w=0.5}You're an admirable person.\""

    vic "\"Unlike me, {w=0.5}and many of the students here, {w=0.5}you know exactly what you want.\""

    vic "\"You have a clear goal in your mind, {w=0.5}and every drop of your effort goes toward it.\""

    window hide

    pause 1.0

    scene black
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    pause 2.0

    window show

    stop music fadeout 5.0

    vic "\"You came here because you wanted to be here.\""

    vic "\"And I came here... {w=0.5}simply because that was what I had been told to do my whole life.\""

    window hide

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
    show college_victor_sad_3_flip at vic_pos_2
    show college_vin_shy at vin_pos_2
    $ renpy.transition(Dissolve(1.5))
    $ renpy.pause(1.5, hard=True)

    $ say_who = _("Victor")

    window show

    vic "\"The loss I felt for myself when I heard you say those words had never been stronger.\""

    show college_victor_sad_flip at vic_pos_2
    hide college_victor_sad_3_flip
    with Dissolve(0.2)

    vic "\"But I was unwilling to face the truth, {w=0.5}and I turned it into jealousy. {w=0.5}I'm sorry,{w=0.5} Vincent. {w=0.5}I said terrible things to you.\""

    $ say_who = ""

    vin "\"......\""

    show college_victor_surprised_flip at vic_pos_2
    hide college_victor_sad_flip
    with Dissolve(0.2)

    vic "\"Huh?\""

    vic "\"Are you blushing?\""

    show college_vin_awk at vin_pos_2
    hide college_vin_shy
    with Dissolve(0.2)

    vin "\"No no. {w=0.5}I just didn't expect you to be so honest with me.\""

    show college_victor_talk_2_flip at vic_pos_2
    hide college_victor_surprised_flip
    with Dissolve(0.2)

    $ say_who = _("Victor")

    vic "\"Is it because I called you an admirable person?\""

    $ renpy.music.set_volume(0.7, delay=0, channel='sound')
    play sound "music/hehe.ogg"

    show college_victor_happy_flip at vic_pos_2
    hide college_victor_talk_2_flip
    with Dissolve(0.2)

    vic "\"You enjoyed being complimented like that, {w=0.5}didn't you?\""

    show college_vin_mad_3 at vin_pos_2
    hide college_vin_awk
    with Dissolve(0.2)

    $ say_who = ""

    vin "\"...I don't know what you're talking about.\""

    show college_victor_talk_2_flip at vic_pos_2
    hide college_victor_happy_flip
    with Dissolve(0.2)

    vic "\"Come to think of it, {w=0.5}you still have classes this afternoon, {w=0.5}don't you? {w=0.5}There's no point in staying here for me.\""

    show college_victor_low_brow_flip at vic_pos_2
    hide college_victor_talk_2_flip
    show college_vin_normal at vin_pos_2
    hide college_vin_mad_3
    with Dissolve(0.2)

    vin "\"......\""

    show college_vin_close_eye_unpleased at vin_pos_2
    hide college_vin_normal
    with Dissolve(0.2)

    vin "\"In that case, {w=0.5}I'll take my leave then.\""

    window hide

    $ renpy.music.set_volume(0.1, delay=0, channel='sound')
    play sound "music/cloth.mp3" fadeout 2.0

    hide college_vin_close_eye_unpleased
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard=True)

    pause 1.0

    window show

    $ say_who = _("Vincent")

    vin "\"......\""

    $ renpy.music.set_volume(0.7, delay=0, channel='music')
    play music "music/bgm/lonely night.ogg"

    show college_victor_surprised_flip at vic_pos_2
    hide college_victor_low_brow_flip
    with Dissolve(0.2)

    vin "\"Two more things.\""

    window hide

    scene dorm_door
    show dust:
        alpha 0
        block:
            ease 5.0 alpha 0.5
            ease 5.0 alpha 1.0
            ease 5.0 alpha 0.5
            ease 5.0 alpha 0
            pause 5.0
            repeat
    show dorm_vincent_door_1
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard=True)

    window show

    vin "\"First,\""

    vin "\"Maybe I don't fully understand how you feel, {w=0.5}and I’m not sure what to say to make you feel better,\""

    vin "\"But you're here for four years, {w=0.5}aren't you?\""

    vin "\"I'm sure you'll find your goal eventually. {w=0.5}A goal that's just for you.\""

    vin "\"If all you need is someone to talk to when you're feeling down, {w=0.5}I'll be here for you.\""

    show dorm_vincent_door_3
    hide dorm_vincent_door_1
    with Dissolve(0.2)

    vin "\"Second,\""

    vin "\"You have the right to be angry with me if I make you upset. {w=0.5}And I allow you to do that.\""

    window hide

    $ say_who = ""

    show character_icon_box_1:
        xpos -600 ypos 250 alpha 0
        easein 1.5 xpos 150 ypos 250 alpha 1
        xpos 150 ypos 250
    show college_vic_icon_shy_flip:
        xpos -600 ypos 248 alpha 0
        easein 1.5 xpos 150 ypos 248 alpha 1
        xpos 150 ypos 248
    show character_icon_box_2:
        xpos -600 ypos 250 alpha 0
        easein 1.5 xpos 150 ypos 250 alpha 1
        xpos 150 ypos 250

    pause 1.6

    window show

    vic "\"......\""

    window hide

    hide character_icon_box_1
    hide college_vic_icon_shy_flip
    hide character_icon_box_2
    with Dissolve(0.5)

    pause 1.0

    window show

    show dorm_vincent_door_1
    hide dorm_vincent_door_3
    with Dissolve(0.2)

    vin "\"See you this evening, {w=0.5}Victor.\""

    vic "\"Wait a minute, {w=0.5}Vincent!\""

    show character_icon_box_1:
        xpos 150 ypos 250
    show college_vic_icon_happy_flip:
        xpos 150 ypos 248
    show character_icon_box_2:
        xpos 150 ypos 250
    with Dissolve(0.5)

    vic "\"Thanks for the hot chocolate.\""

    hide character_icon_box_1
    hide college_vic_icon_happy_flip
    hide character_icon_box_2
    with Dissolve(0.2)

    pause 0.5

    show dorm_vincent_door_2 behind character_icon_box_1
    hide dorm_vincent_door_1
    with Dissolve(0.5)

    vin "\"...Hmph.\""

    window hide

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/open door.ogg" fadeout 1.0

    scene black
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard=True)

    pause 1.0

    window show

    anon "{color=#DC143C}\"And just like that, {w=0.5}they became college roommates for the next four years.\"{/color}"

    window hide

    stop music fadeout 3.0

    pause 1.0

    window show

    anon "{color=#00BFFF}\"......\"{/color}"

    anon "{color=#00BFFF}\"And why exactly are you telling me these?\"{/color}"

    window hide

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music ("music/TenseMusic.ogg") fadein 6.0

    pause 1.0

    window show

    anon "{color=#DC143C}\"I know who you really are, {w=0.5}Infiltrator.\"{/color}"

    anon "{color=#00BFFF}\"!?\"{/color}"

    anon "{color=#DC143C}\"What you should be scared of is... {w=0.5}If Monsieur M finds out, {w=0.5}it'll be all over for you.\"{/color}"

    anon "{color=#00BFFF}\"......\"{/color}"

    anon "{color=#DC143C}\"But I know what you want. {w=0.5}Believe it or not, {w=0.5}to a certain extent, {w=0.5}we actually share the same goal.\"{/color}"

    stop music fadeout 4.0

    anon "{color=#00BFFF}\"The same goal?\"{/color}"

    window hide

    pause 3.0

    anon "{color=#DC143C}\"Say... {w=0.5}Want to collaborate with me, {w=0.5}my dear Infiltrator?\"{/color}"

    pause 3.0

    jump route1_basement_start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
