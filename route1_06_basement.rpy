
image vincent_basement_bg = "images/basement/vincent-basement-bg.png"
image vincent_basement_shadow = "images/basement/vincent-basement-shadow.png"
image vincent_basement_1 = "images/basement/vincent-basement-1.png"
image vincent_basement_2 = "images/basement/vincent-basement-2.png"
image vincent_basement_cloud = "images/basement/vincent-basement-cloud.png"

label route1_basement_start:

    $ renpy.free_memory()

    $ renpy.pause(1.0, hard='True')

    $ renpy.music.set_volume(0.1, delay=0, channel='electricity')
    $ renpy.music.play("music/electricity.ogg", channel="electricity", loop=False, fadein=3.0)

    scene basement_1
    show vin_normal
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(3.0, hard='True')

    show character_icon_box:
        xpos 200 ypos 250
    show van_icon_normal:
        xpos 200 ypos 248
    with Dissolve(1.0)

    $ renpy.pause(1.0, hard='True')

    window show

    v "\"Vincent Edgeworth.\""

    $ renpy.music.set_volume(0.8, delay=0, channel='music')
    play music ["<silence 1.0>","music/creepy.wav"]
    queue music "music/creepy.wav"

    show vin_high_single_brow_talk behind character_icon_box with Dissolve(0.2)

    vin "\"It's been a long time, {w=0.5}Vanora.\""

    hide character_icon_box
    hide van_icon_normal
    hide vin_high_single_brow_talk
    with Dissolve(0.5)

    pause 0.5

    v "\"A long time? {w=0.5}Didn't we just meet last night?\""

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/Vincent.ogg"

    show vin_smile with Dissolve(0.2)

    $ say_who = _("Vincent")

    vin "\"Indeed. {w=0.5}In a sense, {w=0.5}we did.\""

    show vin_close_eye
    hide vin_smile
    hide vin_normal
    with Dissolve(0.2)

    vin "\"But I'm sure you'll agree that we're all more than just mindless walking corpses, {w=0.5}aren't we?\""

    show vin_normal
    hide vin_close_eye
    with Dissolve(0.2)

    $ say_who = ""

    v "\"......\""

    show vin_smile with Dissolve(0.2)

    vin "\"Vanora, {w=0.5}have you ever considered what decides someone's personality?\""

    window hide

    hide vin_high_single_brow_talk
    hide vin_smile
    with Dissolve(0.2)

    pause 1.0
    $ renpy.pause(0.1, hard='True')

    show character_icon_box_1:
        xpos 200 ypos 250
    show van_icon_normal:
        xpos 200 ypos 248
    show character_icon_box_2:
        xpos 200 ypos 250
    with Dissolve(0.5)

    $ renpy.pause(1.0, hard='True')

    window show

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound ("music/vanora/Vanora hmm.ogg")

    v "\"Well, {w=0.5}it should be obvious that none of us were born with a fixed personality.\""

    v "\"A person's character can change based on their living environment, {w=0.5}their family upbringing, {w=0.5}and how people behave around them.\""

    show van_icon_close_eye behind character_icon_box_2:
        xpos 200 ypos 248
    hide van_icon_normal

    v "\"In other words, {w=0.5}their life experiences forge their personality. {w=0.5}Or I should say, {w=0.5}their memories.\""

    show vin_smile behind character_icon_box_1 with Dissolve(0.2)

    $ say_who = _("Vincent")

    vin "\"Correct. {w=0.5}That means that depending on the number of memories recollected, {w=0.5}a person's demeanor and mannerisms will also change somewhat.\""

    vin "\"And it's obvious to me that the woman standing in front of me right now - {w=0.5}is {color=#f00}not the same person{/color} as the one I saw last night.\""

    show vin_high_single_brow_talk behind character_icon_box_1
    hide vin_smile
    hide vin_normal
    with Dissolve(0.2)

    vin "\"By the way, {w=0.5}I must comment, {w=0.5}your new glove suits you very well.\""

    show van_icon_normal behind character_icon_box_2:
        xpos 200 ypos 248
    hide van_icon_close_eye

    hide vin_smile
    hide vin_high_single_brow_talk
    show vin_normal behind character_icon_box_1
    with Dissolve(0.2)

    $ say_who = ""

    v "\"......\""

    jump vanora_intro

label vanora_intro_end:

    show vin_smile behind character_icon_box_1 with Dissolve(0.2)

    window show

    vin "\"However -\""

    vin "\"What I'm curious to know is: {w=0.5}How much of your memory has truly come back?\""

    window hide

    hide vin_smile with Dissolve(0.2)

    pause 2.0

    show character_icon_box_1:
        xpos 200 ypos 250
    show van_icon_normal:
        xpos 200 ypos 248
    show character_icon_box_2:
        xpos 200 ypos 250
    with Dissolve(0.5)

    $ say_who = _("Vanora")

    window show

    v "\"Only a bit.\""

    show van_icon_close_eye behind character_icon_box_2:
        xpos 200 ypos 248
    hide van_icon_normal
    with Dissolve(0.2)

    v "\"I remember that I was a detective from the G4 Investigation Bureau.\""

    v "\"I remember that I came to your mansion to investigate the case of missing citizens over recent years -\""

    v "\"And the truth behind the G4 Cyborg Incident.\""

    show vin_smile behind character_icon_box_1 with Dissolve(0.2)

    $ say_who = ""

    vin "\"And after that?\""

    hide vin_smile
    show van_icon_normal behind character_icon_box_2:
        xpos 200 ypos 248
    hide van_icon_close_eye
    with Dissolve(0.2)

    v "\"I don't remember what happened after that.\""

    $ renpy.music.set_volume(0.8, delay=0, channel='sound1')
    $ renpy.music.play("music/dorm/zs_uneasy impact.ogg", channel="sound1", fadeout = 1.0, loop = False)

    show vin_dark
    hide vin_normal
    hide van_icon_normal
    hide character_icon_box_1
    hide character_icon_box_2
    with Dissolve(0.2)

    vin "\"......\""

    window hide

    pause 2.0

    window show

    show vin_dark_smile
    hide vin_dark
    with Dissolve(0.2)

    $ say_who = _("Vincent")

    vin "\"Is that so?\""

    hide vin_dark_smile
    show vin_smile
    with Dissolve(0.2)

    vin "\"That's fine. {w=0.5}We should take everything one step at a time, {w=0.5}wouldn't you agree? {w=0.5}It's certainly not a wise idea to rush things.\""

    hide vin_smile
    show vin_normal
    with Dissolve(0.2)

    $ say_who = ""

    v "\"......\""

    window hide

    pause 2.0

    window show

    v "\"Vincent.\""

    v "\"You knew exactly who I was all along. {w=0.5}Why were you hiding everything from me?\""

    show vin_smile with Dissolve(0.2)

    vin "\"Me? {w=0.5}Hiding everything? {w=0.5}You've got it all wrong, {w=0.5}Madam.\""

    vin "\"If I didn't wish to help you, {w=0.5}why would I go through all this trouble to offer you leads?\""

    hide vin_smile with Dissolve(0.2)

    v "\"That business card?\""

    v "\"It was your intention to give me that business card to lead me back to the Myers Corporation to find my memories?\""

    show vin_high_single_brow_talk with Dissolve(0.2)

    vin "\"You have a special power in you, {w=0.5}don't you?\""

    hide vin_high_single_brow_talk with Dissolve(0.2)

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/shock2.ogg" fadeout 2.0

    v "\"!?\"" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    $ say_who = _("Vincent")

    show vin_smile with Dissolve(0.2)

    vin "\"As I expected, {w=0.5}you've discovered it as well. {w=0.5}You are able to see past memories contained in certain objects.\""

    vin "\"If that's the case, {w=0.5}do you even need me to tell you about your past?\""

    hide vin_smile
    hide vin_normal
    show vin_high_single_brow_talk
    with Dissolve(0.2)

    vin "\"Even if I had told you the truth while we were in the mansion,\""

    vin "\"That would be nothing more than just a bedtime story for you. {w=0.5}It wouldn't have helped you find your true self, {w=0.5}would it?\""

    hide vin_high_single_brow_talk
    show vin_normal
    with Dissolve(0.2)

    $ say_who = ""

    v "\"In other words, {w=0.5}you wanted me to utilize this power myself so that I could truly realize my own past?\""

    window hide

    stop music fadeout 5.0

    pause 2.0

    show character_icon_box_1:
        xpos 200 ypos 250
    show van_icon_normal:
        xpos 200 ypos 248
    show character_icon_box_2:
        xpos 200 ypos 250
    with Dissolve(0.5)

    $ say_who = _("Vanora")

    window show

    v "\"...I don't believe anything you say. {w=0.5}You have no reason to help me at all.\""

    v "\"As the former lawyer for the Myers Corporation, {w=0.5}you pinned all of the blame on Winston for the G4 Cyborg incident.\""

    v "\"You were willing to do anything to get what you were after.\""

    v "\"There has to be another reason for you to do everything you did for me.\""

    show van_icon_close_eye behind character_icon_box_2:
        xpos 200 ypos 248
    hide van_icon_normal
    with Dissolve(0.2)

    v "\"I don't care what's going on between you and the Myers Corporation at the present time, {w=0.5}but what I do know is, {w=0.5}{color=#f00}you're not a righteous person{/color} and cannot be trusted.\""

    window hide

    hide van_icon_close_eye
    hide character_icon_box_1
    hide character_icon_box_2
    with Dissolve(0.2)

    $ renpy.pause(2.0, hard='True')

    show vin_dark_smile
    hide vin_normal
    with Dissolve(0.2)

    $ say_who = _("Vincent")

    window show

    vin "\"...A righteous person? {w=0.5}Ha, {w=0.5}haha.\""

    window hide

    $ renpy.music.set_volume(0.8, delay=0, channel='music')
    play music ["music/bgm/hl_song3.ogg", "<silence 2.0>"] fadeout 6.0

    $ renpy.pause(2.0, hard='True')

    show vin_laugh
    hide vin_dark_smile
    $ renpy.transition(Dissolve(0.2))

    $ renpy.pause(0.1, hard='True')

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/shake.ogg"

    vin "\"Hahaha! {w=0.5}Vanora, {w=0.5}with all due respect, {w=0.5}you're even more humorous without your memory than with it.\"" with Shake((0.5, 1.0, 0.5, 1.0), 3.0, dist=15)

    v "!?"

    pause 1.0

    hide vin_laugh
    show vin_dark_smile
    with Dissolve(0.2)

    $ renpy.pause(0.5, hard='True')

    window show

    vin "\"Have you ever heard of something like this, {w=0.5}Vanora?\""

    vin "\"'Kill one man, {w=0.5}and you are a murderer.'\""

    vin "\"'Kill millions of men, {w=0.5}and you are a conqueror.'\""

    vin "\"'Kill them all, {w=0.5}and you are a God.'\" "

    vin "\"And how would you define a 'righteous person,' {w=0.5}Vanora? {w=0.5}Are you telling me that you think you qualify as one?\""

    window hide

    pause 2.0

    $ renpy.pause(0.1, hard='True')

    scene black with Dissolve(0.5)

    pause 2.0

    window show

    vin "\"In this world, {w=0.5}there is nothing that is absolutely right, {w=0.5}nor is there anything that is absolutely wrong.\""

    vin "\"The essence of good and evil is really just success and failure, {w=0.5}just a matter of different perspectives.\""

    vin "\"All things could be just from one point of view, {w=0.5}but may be immoral from another.\""

    vin "\"But that doesn't really matter either. {w=0.5}In the end, {w=0.5}none of us are entitled to stand for what we think is right and criticize others.\""

    vin "\"Every human being, {w=0.5}living and dead, {w=0.5}every species - {w=0.5}has done selfish things for their own benefit.\""

    vin "\"But humans, {w=0.5}and only humans, {w=0.5}have invented one set of moral concepts after another to justify their self-centered actions.\""

    vin "\"How many things that used to be considered taboo are now acceptable?\""

    vin "\"And how many things that were considered harmless in the past are now unacceptable?\""

    vin "\"Righteousness and wickedness, {w=0.5}justice and evil, {w=0.5}these are all just fabrications created by human society.\""

    vin "\"As time passes, {w=0.5}as the ruling groups change, {w=0.5}they find that the reasoning of the past no longer justifies their actions today.\""

    vin "\"Time and time again, {w=0.5}humans find new justifications and rewrite their norms over and over again,\""

    vin "\"In order to label themselves as righteous, {w=0.5}to stand in the shoes of an omniscient God, {w=0.5}and to judge others by their so-called morality.\""

    vin "\"But these moral judgments about good and evil cannot exist until they are decreed by a society's central authority.\""

    vin "\"Once removed from legal and social constraints, {w=0.5}these definitions no longer hold water.\""

    window hide

    pause 1.0

    $ say_who = ""

    window show

    v "\"...What exactly are you getting at?\""

    window hide

    $ renpy.pause(1.0, hard='True')

    scene black
    show vincent_basement_bg:
        yalign 1.0 xalign 0.5
    show vincent_basement_shadow:
        yalign 1.0 alpha 1.0
        ease 0.05 alpha 0.9
        ease 0.05 alpha 1.0
        repeat
    show vincent_basement_1
    show vincent_basement_cloud:
        yoffset 300
        xoffset -1280
        linear 10.0 xoffset 0
        repeat
    show red-bg
    $ renpy.transition(Dissolve(0.3))
    $ renpy.pause(0.3, hard='True')

    hide red-bg
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.pause(1.0, hard='True')
    pause 2.0

    window show

    vin "\"Heroes and villains don't exist. {w=0.5}All that really exists are losers and winners.\""

    vin "\"Become a winner in society, {w=0.5}become the conqueror of the world, {w=0.5}and you will be on the right side of history.\""

    window hide

    $ renpy.pause(0.5, hard='True')


    hide vincent_basement_1
    show vincent_basement_2 behind vincent_basement_cloud
    with Dissolve(0.2)



    pause 1.0

    window show

    vin "\"By the same token, {w=0.5}become a loser... {w=0.5}and you will be on the side of wrongdoing.\""

    vin "\"It is not up to you or me to decide who is righteous between us.\""

    show character_icon_box_1:
        xpos 100 ypos 250
    show van_icon_close_eye:
        xpos 100 ypos 248
    show character_icon_box_2:
        xpos 100 ypos 250
    with Dissolve(0.5)

    v "\"It all depends on who comes out on top, {w=0.5}right?\""

    hide van_icon_close_eye
    hide character_icon_box_2
    hide character_icon_box_1
    with Dissolve(0.5)

    vin "\"...Hmph.\""

    window hide

    scene black
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')


    scene basement_1
    show vin_normal
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    $ say_who = _("Vincent")

    pause 2.0

    show vin_close_eye
    hide vin_normal
    with Dissolve(0.2)

    window show

    vin "\"Not only that, {w=0.5}but the tip of the iceberg you're remembering now only serves to distort the truth.\""

    vin "\"When you get all your memories back, {w=0.5}perhaps you will be enlightened. {w=0.5}You will understand why I have done all those things.\""

    hide vin_close_eye
    show vin_smile
    with Dissolve(0.2)

    vin "\"But of course, {w=0.5}I don't really care about that either.\""

    vin "\"The thought of winning your approval has never crossed my mind once, {w=0.5}Vanora. {w=0.5}Nor do I need it at all.\""

    window hide

    hide vin_smile
    show vin_normal
    with Dissolve(0.2)

    pause 2.0

    $ say_who = ""

    window show

    v "\"......\""

    stop music fadeout 6.0

    v "\"I never said what you did was without reason, {w=0.5}Vincent.\""

    v "\"On the contrary, {w=0.5}I am pretty sure that you do have one.\""

    v "\"Righteous or not, {w=0.5}all I want is the truth and only the truth.\""

    window hide

    pause 2.0

    $ say_who = _("Vincent")

    $ renpy.pause(0.1, hard='True')

    show vin_close_eye with Dissolve(0.2)

    window show

    vin "\"The truth, {w=0.5}is it? {w=0.5}I see.\""

    hide vin_close_eye
    show vin_smile
    with Dissolve(0.2)

    vin "\"In that case, {w=0.5}may I offer you a proposition? {w=0.5}Why don't we explore that room together? {w=0.5}The room filled with truth?\""

    hide vin_smile with Dissolve(0.2)

    v "\"!?\""

    v "\"Are you saying...\""

    show vin_close_eye with Dissolve(0.2)

    vin "\"That's correct.\""

    hide vin_close_eye
    show vin_smile
    with Dissolve(0.2)

    vin "\"The secret chamber of the G4 Cyborg Incident - {w=0.5}is hidden somewhere in this room.\""

    hide vin_smile with Dissolve(0.2)

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/shock2.ogg" fadeout 2.0

    v "\"!?\"" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    show vin_high_single_brow_talk
    hide vin_normal
    with Dissolve(0.2)

    vin "\"What do you think, {w=0.5}Vanora? {w=0.5}Why not use your power to solve the mystery here?\""

    window hide

    $ say_who = ""

    hide vin_high_single_brow_talk
    show vin_normal
    with Dissolve(0.2)

    hide vin_normal
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    jump route1_basement_click_start

label basement_m_past_to_present:

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    scene basement_4
    show vin_normal at vin_pos_2
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    pause 2.0

    v "\"......\""

    $ rollback_ = True

    pause 2.0

    $ renpy.music.set_volume(0.4, delay=0, channel='sound')
    play sound "music/vin_hmm.ogg"

    show vin_smile at vin_pos_2
    with Dissolve(0.2)

    window show

    vin "\"What is it, {w=0.5}Vanora? {w=0.5}Were you able to see anything?\""

    window hide

    hide vin_smile with Dissolve(0.2)

    pause 2.0

    show character_icon_box:
        xpos 200 ypos 250
    show van_icon_close_eye:
        xpos 200 ypos 248
    with Dissolve(0.5)

    window show

    v "\"...No, {w=0.5}not really.\""

    window hide

    hide character_icon_box
    hide van_icon_close_eye
    with Dissolve(0.5)

    pause 1.0

    $ say_who = _("Vincent")

    window show

    show vin_close_eye at vin_pos_2
    hide vin_normal
    with Dissolve(0.5)

    vin "\"Is that so? {w=0.5}Then please forgive me for asking such a question.\""

    hide vin_close_eye
    show vin_smile at vin_pos_2
    with Dissolve(0.2)

    vin "\"Is there something that's bothering you? {w=0.5}You've been looking dazed for a while.\""

    window hide

    $ say_who = ""

    hide vin_smile
    show vin_normal at vin_pos_2
    with Dissolve(0.2)

    pause 1.0

    v "\"......\""

    pause 1.0

    show character_icon_box:
        xpos 200 ypos 250
    show van_icon_normal:
        xpos 200 ypos 248
    with Dissolve(0.5)

    window show

    v "\"Actually, {w=0.5}yes. {w=0.5}There is indeed something that I just don't understand.\""

    show vin_high_single_brow_talk at vin_pos_2
    hide vin_normal
    with Dissolve(0.2)

    vin "\"Oh?\""

    hide van_icon_normal
    hide vin_high_single_brow_talk
    show vin_normal at vin_pos_2
    show van_icon_close_eye:
        xpos 200 ypos 248
    with Dissolve(0.2)

    $ renpy.music.set_volume(0.8, delay=0, channel='music')
    play music ["<silence 1.0>","music/creepy.wav"]
    queue music "music/creepy.wav"

    v "\"Have you ever wondered why Myers chose to build 'half-human half-robotic' cyborgs specifically?\""

    v "\"It seemed like something trivial at first, {w=0.5}but I just can't think of an explanation for it.\""

    window hide

    hide van_icon_close_eye
    hide character_icon_box
    with Dissolve(0.5)

    pause 1.0

    window show

    v "\"Myers Corporation is a mechanical engineering corporation; {w=0.5}producing fully mechanical bionic robots should be much easier for them.\""

    v "\"If that's the case, {w=0.5}why build half-human, {w=0.5}half-robotic ones instead?\""

    v "\"These cyborgs have to constantly feed on human flesh to even maintain their human appearance.\""

    v "\"No matter how you look at it, {w=0.5}that's only going to place a lot more burden on Myers Corporation's shoulders.\""

    v "\"And that's also what led to the continuous disappearance of citizens in the G4 district. {w=0.5}They were being used as cattle feed, {w=0.5}which eventually uncovered the whole experiment.\""

    show vin_close_eye at vin_pos_2
    hide vin_normal
    with Dissolve(0.2)

    $ say_who = _("Vincent")

    vin "\"Hmm... {w=0.5}I see where you're coming from. {w=0.5}That's indeed a reasonable question to ask.\""

    hide vin_close_eye
    show vin_smile at vin_pos_2
    with Dissolve(0.2)

    vin "\"But Vanora, {w=0.5}may I ask what you think the real reason for the Myers Corporation's experimentation with cyborgs is?\""

    show vin_normal at vin_pos_2
    hide vin_smile
    with Dissolve(0.2)

    show character_icon_box:
        xpos 200 ypos 250
    show van_icon_normal:
        xpos 200 ypos 248
    with Dissolve(0.5)

    $ say_who = ""

    v "\"This may sound absurd, {w=0.5}but I think the Myers Corporation wants to conquer the world. {w=0.5}They want to become a new God.\""

    show vin_smile at vin_pos_2
    hide vin_normal
    with Dissolve(0.2)

    vin "\"And what good would it do them to conquer the world?\""

    hide van_icon_normal
    show van_icon_close_eye:
        xpos 200 ypos 248
    show vin_normal at vin_pos_2
    hide vin_smile
    with Dissolve(0.2)

    v "\"Isn't it obvious? {w=0.5}They would possess endless money and power.\""

    hide van_icon_close_eye
    show van_icon_normal:
        xpos 200 ypos 248
    hide vin_normal
    show vin_smile at vin_pos_2
    with Dissolve(0.2)

    vin "\"Is that so? {w=0.5}So, {w=0.5}you think the Myers Corporation is building half-human half-robotic cyborgs purely for the sake of power and money?\""

    hide vin_smile
    show vin_normal at vin_pos_2
    with Dissolve(0.2)

    v "\"......\""

    hide van_icon_normal
    show van_icon_close_eye:
        xpos 200 ypos 248

    v "\"......\""

    hide van_icon_close_eye
    hide character_icon_box
    with Dissolve(0.5)

    $ say_who = _("Vincent")

    show vin_smile at vin_pos_2
    hide vin_normal
    with Dissolve(0.2)

    vin "\"You have realized as well. {w=0.5}If that's all Myers Corporation wants, {w=0.5}then it's enough for them to keep making the artificial prosthetics they do.\""

    hide vin_smile
    show vin_close_eye at vin_pos_2
    with Dissolve(0.2)

    vin "\"Theoretically, {w=0.5}they've already conquered the G4 district, {w=0.5}haven't they? {w=0.5}It wouldn't be a stretch to bring other districts to their knees in the same way.\""

    hide vin_close_eye
    show vin_smile at vin_pos_2
    with Dissolve(0.2)

    vin "\"In that case, {w=0.5}I'm sure you can easily conclude that there must be other reasons for the Myers Corporation to start this series of experiments.\""

    vin "\"Vanora, {w=0.5}let's think about it another way:\""

    vin "\"If you are the Myers Corporation and you think you are God, {w=0.5}what are these cyborgs to you?\""

    hide vin_smile
    show vin_normal at vin_pos_2
    with Dissolve(0.2)

    $ say_who = ""

    v "\"If I am Myers Corporation and I think I am God...\""

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/shock2.ogg" fadeout 2.0

    v "\"!?\"" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    v "\"These cyborgs... {w=0.5}{color=#f00}are a new species that I have created{/color}.\""

    hide vin_normal
    show vin_smile at vin_pos_2
    with Dissolve(0.2)

    vin "\"Correct. {w=0.5}The Myers Corporation wants more than just money and power, {w=0.5}{color=#f00}they want to create a new world order{/color}.\""

    vin "\"Vanora, {w=0.5}have you heard of the {color=#f00}Voorhees Corporation{/color} by any chance?\""

    hide vin_smile
    show vin_normal at vin_pos_2
    with Dissolve(0.2)

    v "\"Voorhees Corporation... {w=0.5}That's {color=#f00}a bioengineering corporation located in the G3 district{/color}, {w=0.5}isn't it?\""

    hide vin_normal
    show vin_smile at vin_pos_2
    with Dissolve(0.2)

    vin "\"Yes. {w=0.5}Just like Myers, {w=0.5}Voorhees used to be an international super-monopoly. {w=0.5}They shared a similar goal as well.\""

    vin "\"The mutants as we know them today were actually the product of Voorhees.\""

    hide vin_smile
    show vin_normal at vin_pos_2
    with Dissolve(0.2)

    v "\"!?\""

    hide vin_normal
    show vin_close_eye at vin_pos_2
    with Dissolve(0.2)

    $ say_who = _("Vincent")

    vin "\"Similar to the Myers Corporation, {w=0.5}Voorhees Corporation aimed to replace the current human race with a newly created species.\""

    hide vin_close_eye
    show vin_smile at vin_pos_2
    with Dissolve(0.2)

    vin "\"But the difference is, {w=0.5}Voorhees' mutants don't need to feed on humans to survive.\""

    vin "\"Even though these mutants have special abilities compared to ordinary humans, {w=0.5}people don't necessarily agree that this makes them more superior.\""

    hide vin_smile
    show vin_close_eye at vin_pos_2
    with Dissolve(0.2)

    vin "\"Presently, {w=0.5}tensions between mutants and humans are particularly high in the G3 district.\""

    vin "\"Some mutants do believe that they are better than ordinary humans,\""

    vin "\"But many humans believe that the mutants are monsters that should not exist, {w=0.5}and that humans are the rightful ruler of the earth.\""

    hide vin_close_eye
    show vin_smile at vin_pos_2
    with Dissolve(0.2)

    vin "\"Of course, {w=0.5}there are also those who believe that the two can live together in harmony.\""

    hide vin_smile
    show vin_close_eye at vin_pos_2
    with Dissolve(0.2)

    vin "\"The Myers Corporation witnessed all of that.\""

    hide vin_close_eye
    show vin_smile at vin_pos_2
    with Dissolve(0.2)

    vin "\"They came to the conclusion that {color=#f00}if they were going to create a species that is one hundred percent above humans,{/color}\""

    vin "\"{color=#f00}The survival of that species must depend on the death of humans.{/color}\""

    show vin_high_single_brow_talk at vin_pos_2
    hide vin_smile
    with Dissolve(0.2)

    vin "\"'Mediocre humans must give up their lives in order to create our utopia. {w=0.5}It is a necessary sacrifice.' {w=0.5}That's what the Myers Corporation thought.\""

    window hide

    $ say_who = ""

    hide vin_high_single_brow_talk
    show vin_normal at vin_pos_2
    with Dissolve(0.2)

    pause 1.0

    stop music fadeout 6.0

    show character_icon_box:
        xpos 200 ypos 250
    show van_icon_close_eye:
        xpos 200 ypos 248
    with Dissolve(0.5)

    $ say_who = _("Vanora")

    window show

    v "\"...I understand now.\""

    v "\"It is not a flaw that the cyborgs Myers produces need to feed on humans.\""

    hide van_icon_close_eye
    show van_icon_normal:
        xpos 200 ypos 248

    v "\"In fact, {w=0.5}it is quite the opposite - {w=0.5}that's the intention of the Myers Corporation to begin with.\""

    hide van_icon_normal
    show van_icon_close_eye:
        xpos 200 ypos 248
    with Dissolve(0.5)

    v "\"If the cyborgs are placed at the top of the food chain above humans, {w=0.5}there will never be a chance for equality between the two.\""

    show vin_smile at vin_pos_2
    hide vin_normal
    with Dissolve(0.2)

    $ say_who = ""

    vin "\"Correct.\""

    window hide

    hide vin_smile
    hide van_icon_close_eye
    hide character_icon_box
    with Dissolve(0.5)

    $ renpy.block_rollback()
    $ _rollback = False
    $ rollback_ = False
    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music ("music/Tunnel/myersSewers.ogg")

    show screen inventory_screen
    with Dissolve(0.2)

    $ basement_see_flashback = True

    call screen basement_room_4_screen with Dissolve(0.2)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
