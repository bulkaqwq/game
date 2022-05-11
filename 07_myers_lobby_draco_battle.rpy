image myers_lobby_claude = "images/Myers Lobby/myers_lobby_claude.jpg"
image myers_lobby_charles = "images/Myers Lobby/myers_lobby_charles.jpg"
image myers_lobby_emanon = "images/Myers Lobby/myers_lobby_emanon.jpg"
image myers_lobby_winston = "images/Myers Lobby/myers_lobby_winston.jpg"

image myers_lobby_draco_battle_explanation_1 = "images/Myers Lobby/draco battle explanation 1.png"
image myers_lobby_draco_battle_explanation_2 = "images/Myers Lobby/draco battle explanation 2.png"
image myers_lobby_draco_battle_explanation_wheel = "images/Myers Lobby/glitches/wheel.png"
image myers_lobby_draco_battle_explanation_wheel_2 = "images/Myers Lobby/glitches/wheel.png"




screen myers_lobby_draco_battle_chance:

    text _("{font=VHS.ttf}{color=#ffffff}CHANCES:[myers_lobby_draco_battle_chance_num]{/color}{/font}") xpos 0.985 ypos 0.02 xanchor 1.0 outlines [(2, "#000000", 0, 0,)]

screen myers_lobby_question_2_select:

    imagebutton:
        xpos 50
        ypos 80
        idle "images/Myers Lobby/myers_lobby_portrait_idle.png"
        hover "images/Myers Lobby/myers_lobby_portrait_hover.png"
        focus_mask "images/Myers Lobby/myers_lobby_portrait_hover.png"
        action Jump("myers_lobby_draco_question_2_correct")

    imagebutton:
        xpos 350
        ypos 80
        idle "images/Myers Lobby/myers_lobby_portrait_idle.png"
        hover "images/Myers Lobby/myers_lobby_portrait_hover.png"
        focus_mask "images/Myers Lobby/myers_lobby_portrait_hover.png"
        action Jump("myers_lobby_draco_question_2_wrong")

    imagebutton:
        xpos 650
        ypos 80
        idle "images/Myers Lobby/myers_lobby_portrait_idle.png"
        hover "images/Myers Lobby/myers_lobby_portrait_hover.png"
        focus_mask "images/Myers Lobby/myers_lobby_portrait_hover.png"
        action Jump("myers_lobby_draco_question_2_wrong")

    imagebutton:
        xpos 950
        ypos 80
        idle "images/Myers Lobby/myers_lobby_portrait_idle.png"
        hover "images/Myers Lobby/myers_lobby_portrait_hover.png"
        focus_mask "images/Myers Lobby/myers_lobby_portrait_hover.png"
        action Jump("myers_lobby_draco_question_2_wrong")

    add mtt_


label myers_lobby_draco_battle_start:

    $ say_who = ""

    show draco_fisheye_4 onlayer front:
        xalign 0.5 yalign 0.5 alpha 1
    show draco_fisheye_3 onlayer front:
        xalign 0.5 yalign 0.5 alpha 0
    with Dissolve(0.3)
    $ renpy.pause(0.3, hard='True')


    window hide

    $ myers_lobby_draco_battle_chance_num = 2

    show screen myers_lobby_draco_battle_chance
    with Dissolve(0.2)

    $ renpy.pause(0.1, hard='True')
    pause 0.2
    $ renpy.pause(0.1, hard='True')
    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/wrong.ogg"
    show live-die-small onlayer ab_parallax with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')
    pause 2.0
    $ renpy.pause(0.1, hard='True')
    hide live-die-small onlayer ab_parallax with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/email sent.ogg"

    show transparent dark-small onlayer ab_parallax
    show myers_lobby_draco_battle_explanation_1 onlayer ab_parallax:
        yoffset 100
        linear 0.5 yoffset 50

    show myers_lobby_draco_battle_explanation_2 onlayer ab_parallax:
        yoffset -100
        linear 0.5 yoffset -50
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
    with Dissolve(0.5)

    noname_warning_3 "(Warning: {w=0.5}You will be able to give {color=#f00}two incorrect answers {/color}to all of Draco's questions.)"

    noname_warning_3 "(Answering incorrectly more than twice or exceeding the time limit will immediately lead to {color=#f00}death{/color}.)"

    noname_warning_3 "(Saving would be a great idea now.)"

    hide transparent dark-small onlayer ab_parallax
    hide myers_lobby_draco_battle_explanation_1 onlayer ab_parallax
    hide myers_lobby_draco_battle_explanation_2 onlayer ab_parallax
    show myers_lobby_draco_battle_explanation_1 onlayer ab_parallax:
        yoffset 50
        linear 0.5 yoffset 100 alpha 0
    show myers_lobby_draco_battle_explanation_2 onlayer ab_parallax:
        yoffset -50
        linear 0.5 yoffset -100 alpha 0
    hide myers_lobby_draco_battle_explanation_wheel onlayer ab_parallax
    hide myers_lobby_draco_battle_explanation_wheel_2 onlayer ab_parallax
    with Dissolve(0.5)
    hide myers_lobby_draco_battle_explanation_1 onlayer ab_parallax
    hide myers_lobby_draco_battle_explanation_2 onlayer ab_parallax

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)
    $ renpy.block_rollback()
    $ _rollback = False

    $ renpy.pause(0.1, hard='True')
    pause 0.2
    $ renpy.pause(0.1, hard='True')
    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/wrong.ogg"
    show question-1-small onlayer ab_parallax with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')
    pause 2.0
    $ renpy.pause(0.1, hard='True')
    hide question-1-small onlayer ab_parallax with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')

    $ _rollback = True
    $ _skipping = True

    show draco_fisheye_4 onlayer front:
        xalign 0.5 yalign 0.5 alpha 0
    show draco_fisheye_3 onlayer front:
        xalign 0.5 yalign 0.5 alpha 1
    with Dissolve(0.3)

    window show

    cyb_dra "\"In the world of peace, {w=0.5}there is nothing to be desired but the most admired works; {w=0.5}in the world of peace, {w=0.5}there is nothing to be respected but the creative tools of innovation.\""

    $ rollback_ = True

    cyb_dra "\"In order to break the shackles of tradition and develop science, {w=0.5}science needs creation and imagination.\""

    cyb_dra "\"As a super monopoly in the G4 district, {w=0.5}Myers Corporation is no exception to this.\""

    cyb_dra "\"Human beings stand out among all species because they are endowed with the ability to create and innovate.\""

    cyb_dra "\"But for Mr. Myers, {w=0.5}the application of such ability goes far beyond making tools. {w=0.5}{color=#f00}It has a more important role to play.{/color}\""

    cyb_dra "\"If things are used for their strengths, {w=0.5}then there will be no talent that is abandoned; {w=0.5}if things are used for their weaknesses, {w=0.5}then there will be no one that is satisfied.\""

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()

    cyb_dra "\"Therefore, {w=0.5}Mr. Myers has set a slogan for the company since its inception:\""

    window hide

    show draco_fisheye_4 onlayer front:
        xalign 0.5 yalign 0.5 alpha 1
    show draco_fisheye_3 onlayer front:
        xalign 0.5 yalign 0.5 alpha 0
    with Dissolve(0.3)

    $ _skipping = False
    $ rollback_ = False
    $ _rollback = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

label myers_lobby_draco_question_1:

    show screen countdown(timer_range=20, timer_jump='myers_lobby_draco_death')

    menu:
        "\"Myers Corporation - The place where dreams come true. The place where you make the rules.\"":


            jump myers_lobby_draco_question_1_wrong
        "\"Design, create, enhance. Myers Corporation.\"":


            jump myers_lobby_draco_question_1_correct
        "\"Myers Corporation - Go beyond the limits of reality. Make the impossible possible.\"":


            jump myers_lobby_draco_question_1_wrong
        "\"To mold ideas and define limits with technology. Myers Corporation.\"":


            jump myers_lobby_draco_question_1_wrong

label myers_lobby_draco_question_1_wrong:

    $ myers_lobby_draco_battle_chance_num -= 1

    if myers_lobby_draco_battle_chance_num == 0:
        hide screen myers_lobby_draco_battle_chance

    $ renpy.block_rollback()

    hide screen countdown

    $ renpy.pause(0.1, hard='True')
    pause 0.2
    $ renpy.pause(0.1, hard='True')
    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/wrong.ogg"
    show wrong-small onlayer ab_parallax with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')
    pause 2.0
    $ renpy.pause(0.1, hard='True')
    hide wrong-small onlayer ab_parallax with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')

    if myers_lobby_draco_battle_chance_num > 0:
        jump myers_lobby_draco_question_1
    else:
        jump myers_lobby_draco_death

label myers_lobby_draco_question_1_correct:

    $ renpy.block_rollback()

    hide screen countdown

    $ renpy.pause(0.1, hard='True')
    pause 0.2
    $ renpy.pause(0.1, hard='True')
    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/correct.ogg"
    show correct-small onlayer ab_parallax with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')
    pause 2.0
    $ renpy.pause(0.1, hard='True')
    hide correct-small onlayer ab_parallax with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')

    $ _rollback = True
    $ _skipping = True

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/email sent.ogg"

    show transparent dark-small onlayer ab_parallax
    show myers_lobby_draco_battle_explanation_1 onlayer ab_parallax:
        yoffset 100
        linear 0.5 yoffset 50

    show myers_lobby_draco_battle_explanation_2 onlayer ab_parallax:
        yoffset -100
        linear 0.5 yoffset -50
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
    with Dissolve(0.5)

    noname_warning_3 "(Correct answer: Design, create, enhance. Myers Corporation.)"

    $ rollback_ = True

    noname_warning_3 "(For Mr. Myers, {w=0.5}humanity has lasted because it was endowed with the ability to innovate.)"

    noname_warning_3 "(And the application of such ability should be used not only in tool-making, {w=0.5}but also in amplification of mankind's advantages.)"

    noname_warning_3 "(Compared with ordinary people, {w=0.5}the modified Myers employees exemplify better working abilities.)"

    noname_warning_3 "(Therefore, {w=0.5}Myers Corporation focuses on designing, creating, and enhancing human strengths.)"

    hide transparent dark-small onlayer ab_parallax
    hide myers_lobby_draco_battle_explanation_1 onlayer ab_parallax
    hide myers_lobby_draco_battle_explanation_2 onlayer ab_parallax
    show myers_lobby_draco_battle_explanation_1 onlayer ab_parallax:
        yoffset 50
        linear 0.5 yoffset 100 alpha 0

    show myers_lobby_draco_battle_explanation_2 onlayer ab_parallax:
        yoffset -50
        linear 0.5 yoffset -100 alpha 0
    hide myers_lobby_draco_battle_explanation_wheel onlayer ab_parallax
    hide myers_lobby_draco_battle_explanation_wheel_2 onlayer ab_parallax
    with Dissolve(0.5)
    hide myers_lobby_draco_battle_explanation_1 onlayer ab_parallax
    hide myers_lobby_draco_battle_explanation_2 onlayer ab_parallax

    $ _skipping = False
    $ rollback_ = False
    $ _rollback = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

label myers_lobby_draco_question_2_start:

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()

    $ renpy.pause(0.1, hard='True')
    pause 0.2
    $ renpy.pause(0.1, hard='True')
    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/wrong.ogg"
    show question-2-small onlayer ab_parallax with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')
    pause 2.0
    $ renpy.pause(0.1, hard='True')
    hide question-2-small onlayer ab_parallax with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')

    $ _rollback = True
    $ _skipping = True

    show draco_fisheye_4 onlayer front:
        xalign 0.5 yalign 0.5 alpha 0
    show draco_fisheye_3 onlayer front:
        xalign 0.5 yalign 0.5 alpha 1
    with Dissolve(0.3)
    $ renpy.pause(0.3, hard='True')

    window show

    cyb_dra "\"Rivers and mountains can only nourish a limited amount of soil, {w=0.5}but the number of mediocre souls is infinite.\""

    $ rollback_ = True

    cyb_dra "\"The sinful souls do not deserve to be judged, {w=0.5}and can only be redeemed by repaying their bodies to the world that has allowed it to take so much.\""

    cyb_dra "\"The above excerpt is from a gospel discovered by the police during the investigation of Myers Corporation.\""

    cyb_dra "\"The gospel is considered to be the embodiment of the ideas and concepts of the mastermind of the G4 Cyborg Incident.\""

    cyb_dra "\"The so-called \"mastermind\" was sentenced to life in prison, {w=0.5}yet Myers Corporation itself was never charged.\""

    cyb_dra "\"Nonetheless, {w=0.5}a series of mysterious murders took place afterwards led to the belief that there was more to it than met the eye.\""

    cyb_dra "\"On July 20, {w=0.5}2081, {w=0.5}several small explosions occurred near the G4 central prison area, {w=0.5}destroying part of the prison walls.\""

    cyb_dra "\"Since then the whereabouts of this former researcher from Myers, {w=0.5}who is also known as the mastermind of the G4 Cyborg Incident, {w=0.5}has been unknown.\""

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False

    cyb_dra "\"So, {w=0.5}which of the following is the infamous Mr. {color=#f00}Winston Loomis{/color}? \""

    $ _skipping = False
    $ rollback_ = False
    $ _rollback = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    window hide

    show draco_fisheye_4 onlayer front:
        xalign 0.5 yalign 0.5 alpha 1
    show draco_fisheye_3 onlayer front:
        xalign 0.5 yalign 0.5 alpha 0
    with Dissolve(0.3)
    $ renpy.pause(0.3, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/scan map.ogg"

    show myers_lobby_winston onlayer ab_parallax:
        xpos 50 ypos 80
    show myers_lobby_emanon onlayer ab_parallax:
        xpos 350 ypos 80
    show myers_lobby_charles onlayer ab_parallax:
        xpos 650 ypos 80
    show myers_lobby_claude onlayer ab_parallax:
        xpos 950 ypos 80
    $ renpy.transition(wipeDown)
    $ renpy.pause(0.5, hard='True')

label myers_lobby_draco_question_2:

    show screen countdown(timer_range=20, timer_jump='myers_lobby_draco_death')

    call screen myers_lobby_question_2_select

label myers_lobby_draco_question_2_wrong:

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/selectsounds.ogg"

    $ myers_lobby_draco_battle_chance_num -= 1

    if myers_lobby_draco_battle_chance_num == 0:
        hide screen myers_lobby_draco_battle_chance

    $ renpy.block_rollback()

    hide screen countdown

    $ renpy.pause(0.1, hard='True')
    pause 0.2
    $ renpy.pause(0.1, hard='True')
    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/wrong.ogg"
    show wrong-small onlayer ab_parallax with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')
    pause 2.0
    $ renpy.pause(0.1, hard='True')
    hide wrong-small onlayer ab_parallax with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')

    if myers_lobby_draco_battle_chance_num > 0:
        jump myers_lobby_draco_question_2
    else:
        hide myers_lobby_winston onlayer ab_parallax
        hide myers_lobby_emanon onlayer ab_parallax
        hide myers_lobby_charles onlayer ab_parallax
        hide myers_lobby_claude onlayer ab_parallax
        $ renpy.transition(wipeDown)
        jump myers_lobby_draco_death

label myers_lobby_draco_question_2_correct:

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/selectsounds.ogg"

    $ renpy.block_rollback()

    hide screen countdown

    $ renpy.pause(0.1, hard='True')
    pause 0.2
    $ renpy.pause(0.1, hard='True')
    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/correct.ogg"
    show correct-small onlayer ab_parallax with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')
    pause 2.0
    $ renpy.pause(0.1, hard='True')
    hide correct-small onlayer ab_parallax with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')

    $ _rollback = True
    $ _skipping = True

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/email sent.ogg"

    hide myers_lobby_winston onlayer ab_parallax
    hide myers_lobby_emanon onlayer ab_parallax
    hide myers_lobby_charles onlayer ab_parallax
    hide myers_lobby_claude onlayer ab_parallax
    $ renpy.transition(wipeDown)

    show transparent dark-small onlayer ab_parallax
    show myers_lobby_draco_battle_explanation_1 onlayer ab_parallax:
        yoffset 100
        linear 0.5 yoffset 50

    show myers_lobby_draco_battle_explanation_2 onlayer ab_parallax:
        yoffset -100
        linear 0.5 yoffset -50
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
    with Dissolve(0.5)

    noname_warning_3 "(Correct answer: Picture 1)"

    $ rollback_ = True

    noname_warning_3 "(Because of his shyness and lack of friends, {w=0.5}Winston Loomis was chosen by Myers as a scapegoat for the G4 Cyborg Incident.)"

    noname_warning_3 "(He was described in the group chat as \"the guy who always wears shades, {w=0.5}doesn't say a word, {w=0.5}and has a bit of a hunched back.\")"

    noname_warning_3 "(The former employee who used John's desk also pointed out that..."

    noname_warning_3 "...he \"doesn't seem like the type that could drag that many people into the basement to experiment on them.\")"

    hide transparent dark-small onlayer ab_parallax
    hide myers_lobby_draco_battle_explanation_1 onlayer ab_parallax
    hide myers_lobby_draco_battle_explanation_2 onlayer ab_parallax
    show myers_lobby_draco_battle_explanation_1 onlayer ab_parallax:
        yoffset 50
        linear 0.5 yoffset 100 alpha 0
    show myers_lobby_draco_battle_explanation_2 onlayer ab_parallax:
        yoffset -50
        linear 0.5 yoffset -100 alpha 0
    hide myers_lobby_draco_battle_explanation_wheel onlayer ab_parallax
    hide myers_lobby_draco_battle_explanation_wheel_2 onlayer ab_parallax
    with Dissolve(0.5)
    hide myers_lobby_draco_battle_explanation_1 onlayer ab_parallax
    hide myers_lobby_draco_battle_explanation_2 onlayer ab_parallax

    $ _skipping = False
    $ rollback_ = False
    $ _rollback = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

label myers_lobby_draco_question_3_start:

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()

    $ renpy.pause(0.1, hard='True')
    pause 0.2
    $ renpy.pause(0.1, hard='True')
    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/wrong.ogg"
    show question-3-small onlayer ab_parallax with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')
    pause 2.0
    $ renpy.pause(0.1, hard='True')
    hide question-3-small onlayer ab_parallax with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')

    $ _rollback = True
    $ _skipping = True

    show draco_fisheye_4 onlayer front:
        xalign 0.5 yalign 0.5 alpha 0
    show draco_fisheye_3 onlayer front:
        xalign 0.5 yalign 0.5 alpha 1
    with Dissolve(0.3)
    $ renpy.pause(0.3, hard='True')

    window show

    cyb_dra "\"Innovation is not enough for a giant enterprise like Myers to succeed. {w=0.5}It also needs to make proper use of resources.\""

    $ rollback_ = True

    cyb_dra "\"Humans did not create the earth, {w=0.5}so the earth itself is not human property.\""

    cyb_dra "\"Humans' property is through re-creation, {w=0.5}and every private owner owes rent to society for his possessions.\""

    cyb_dra "\"For most people, {w=0.5}the nightmare of the G4 Cyborg Incident began in that week in 2080.\""

    cyb_dra "\"Many ordinary citizens disappeared without a sign. {w=0.5}They were all last seen near the G4 district.\""

    cyb_dra "\"However, {w=0.5}what's really strange is – \""

    cyb_dra "\"According to the investigation of the G4 police, {w=0.5}these ordinary citizens were not the cyborgs made in the basement.\""

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()

    cyb_dra "\"If that is the case, {w=0.5}where did the material for Myers' cyborgs come from?\""

    window hide

    show draco_fisheye_4 onlayer front:
        xalign 0.5 yalign 0.5 alpha 1
    show draco_fisheye_3 onlayer front:
        xalign 0.5 yalign 0.5 alpha 0
    with Dissolve(0.3)

    $ _skipping = False
    $ rollback_ = False
    $ _rollback = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

label myers_lobby_draco_question_3:

    show screen countdown(timer_range=20, timer_jump='myers_lobby_draco_death')

    menu:
        "Vagrants in G4 district":


            jump myers_lobby_draco_question_3_wrong
        "Employees of Myers Corporation":


            jump myers_lobby_draco_question_3_correct
        "Prisoners from G4 Central Prison":


            jump myers_lobby_draco_question_3_wrong
        "Primates in G4 district":


            jump myers_lobby_draco_question_3_wrong

label myers_lobby_draco_question_3_wrong:

    $ myers_lobby_draco_battle_chance_num -= 1

    if myers_lobby_draco_battle_chance_num == 0:
        hide screen myers_lobby_draco_battle_chance

    $ renpy.block_rollback()

    hide screen countdown

    $ renpy.pause(0.1, hard='True')
    pause 0.2
    $ renpy.pause(0.1, hard='True')
    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/wrong.ogg"
    show wrong-small onlayer ab_parallax with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')
    pause 2.0
    $ renpy.pause(0.1, hard='True')
    hide wrong-small onlayer ab_parallax with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')

    if myers_lobby_draco_battle_chance_num > 0:
        jump myers_lobby_draco_question_3
    else:
        jump myers_lobby_draco_death

label myers_lobby_draco_question_3_correct:

    $ renpy.block_rollback()

    hide screen countdown

    $ renpy.pause(0.1, hard='True')
    pause 0.2
    $ renpy.pause(0.1, hard='True')
    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/correct.ogg"
    show correct-small onlayer ab_parallax with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')
    pause 2.0
    $ renpy.pause(0.1, hard='True')
    hide correct-small onlayer ab_parallax with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')

    $ _rollback = True
    $ _skipping = True

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/email sent.ogg"

    show transparent dark-small onlayer ab_parallax
    show myers_lobby_draco_battle_explanation_1 onlayer ab_parallax:
        yoffset 100
        linear 0.5 yoffset 50

    show myers_lobby_draco_battle_explanation_2 onlayer ab_parallax:
        yoffset -100
        linear 0.5 yoffset -50
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
    with Dissolve(0.5)

    noname_warning_3 "(Correct answer: Employees of Myers Corporation)"

    $ rollback_ = True

    noname_warning_3 "(By removing the cyborg's eyeball, {w=0.5}[name!t] successfully entered the secret employee passageway of Myers Corporation.)"

    noname_warning_3 "(The memory of the former Myers employee, {w=0.5}John, {w=0.5}also seems to suggest that the previous employee sitting at John's desk, "

    noname_warning_3 "as well as John himself, {w=0.5}was tragically killed.)"

    noname_warning_3 "(Because of the many classified experiments that Myers has been conducting for a long time,"

    noname_warning_3 "many of its employees have little contact with their families.)"

    noname_warning_3 "(As a result, {w=0.5}no one would have been aware of their disappearance.)"

    hide transparent dark-small onlayer ab_parallax
    hide myers_lobby_draco_battle_explanation_1 onlayer ab_parallax
    hide myers_lobby_draco_battle_explanation_2 onlayer ab_parallax
    show myers_lobby_draco_battle_explanation_1 onlayer ab_parallax:
        yoffset 50
        linear 0.5 yoffset 100 alpha 0
    show myers_lobby_draco_battle_explanation_2 onlayer ab_parallax:
        yoffset -50
        linear 0.5 yoffset -100 alpha 0
    hide myers_lobby_draco_battle_explanation_wheel onlayer ab_parallax
    hide myers_lobby_draco_battle_explanation_wheel_2 onlayer ab_parallax
    with Dissolve(0.5)
    hide myers_lobby_draco_battle_explanation_1 onlayer ab_parallax
    hide myers_lobby_draco_battle_explanation_2 onlayer ab_parallax

label myers_lobby_draco_question_4_start:

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()

    $ renpy.pause(0.1, hard='True')
    pause 0.2
    $ renpy.pause(0.1, hard='True')
    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/wrong.ogg"
    show question-4-small onlayer ab_parallax with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')
    pause 2.0
    $ renpy.pause(0.1, hard='True')
    hide question-4-small onlayer ab_parallax with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')

    $ _rollback = True
    $ _skipping = True

    show draco_fisheye_4 onlayer front:
        xalign 0.5 yalign 0.5 alpha 0
    show draco_fisheye_3 onlayer front:
        xalign 0.5 yalign 0.5 alpha 1
    with Dissolve(0.3)
    $ renpy.pause(0.3, hard='True')

    window show

    cyb_dra "\"Scientists don't rely on the ideas of individuals, {w=0.5}but on the combined wisdom of thousands of people.\""

    $ rollback_ = True

    cyb_dra "\"Only when everyone thinks about a problem, {w=0.5}and everyone does part of the work, {w=0.5}will it be added to the great edifice of knowledge that is being built.\""

    cyb_dra "\"Similarly, {w=0.5}in order to work more effectively, {w=0.5}Myers Corporation is divided into many departments, {w=0.5}large and small.\""

    cyb_dra "\"In addition, {w=0.5}each elite is assigned to their own dedicated department.\""

    cyb_dra "\"This included the outstanding graduates, {w=0.5}Mr. Blake and Mr. Edgeworth.\""

    cyb_dra "\"There are no smooth paths in science. {w=0.5}Only those who climb the steep hills without fear of hardship can hope to reach the summit of glory.\""

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()

    cyb_dra "\"So may I ask which two departments Mr. Blake and Mr. Edgeworth, {w=0.5}as former employees of Myers, {w=0.5}came from?\""

    window hide

    show draco_fisheye_4 onlayer front:
        xalign 0.5 yalign 0.5 alpha 1
    show draco_fisheye_3 onlayer front:
        xalign 0.5 yalign 0.5 alpha 0
    with Dissolve(0.3)

    $ _skipping = False
    $ rollback_ = False
    $ _rollback = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

label myers_lobby_draco_question_4:

    show screen countdown(timer_range=20, timer_jump='myers_lobby_draco_death')

    menu:
        "Economy Department and Legal Department":


            jump myers_lobby_draco_question_4_wrong
        "Investment Department and Legal Department":


            jump myers_lobby_draco_question_4_correct
        "Finance Department and Administration Department":


            jump myers_lobby_draco_question_4_wrong
        "Investment Department and Administration Department":


            jump myers_lobby_draco_question_4_wrong

label myers_lobby_draco_question_4_wrong:

    $ myers_lobby_draco_battle_chance_num -= 1

    if myers_lobby_draco_battle_chance_num == 0:
        hide screen myers_lobby_draco_battle_chance

    $ renpy.block_rollback()

    hide screen countdown

    $ renpy.pause(0.1, hard='True')
    pause 0.2
    $ renpy.pause(0.1, hard='True')
    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/wrong.ogg"
    show wrong-small onlayer ab_parallax with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')
    pause 2.0
    $ renpy.pause(0.1, hard='True')
    hide wrong-small onlayer ab_parallax with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')

    if myers_lobby_draco_battle_chance_num > 0:
        jump myers_lobby_draco_question_4
    else:
        jump myers_lobby_draco_death

label myers_lobby_draco_question_4_correct:

    $ renpy.block_rollback()

    hide screen countdown

    $ renpy.pause(0.1, hard='True')
    pause 0.2
    $ renpy.pause(0.1, hard='True')
    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/correct.ogg"
    show correct-small onlayer ab_parallax with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')
    pause 2.0
    $ renpy.pause(0.1, hard='True')
    hide correct-small onlayer ab_parallax with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')

    $ _rollback = True
    $ _skipping = True

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/email sent.ogg"

    show transparent dark-small onlayer ab_parallax
    show myers_lobby_draco_battle_explanation_1 onlayer ab_parallax:
        yoffset 100
        linear 0.5 yoffset 50

    show myers_lobby_draco_battle_explanation_2 onlayer ab_parallax:
        yoffset -100
        linear 0.5 yoffset -50
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
    with Dissolve(0.5)

    noname_warning_3 "(Correct answer: Investment Department and Legal Department)"

    $ rollback_ = True

    noname_warning_3 "(We know from John's past memories that Victor is John's boss, {w=0.5}and also Chief Investment Officer at Myers Corporation.)"

    noname_warning_3 "(And Vincent's encounter with John revealed that he was the lawyer in charge of exonerating Myers... "

    noname_warning_3 "...from the G4 Cyborg Incident, {w=0.5}and implied that he came from the Legal Department \"on the other side of the company.\")"

    hide transparent dark-small onlayer ab_parallax
    hide myers_lobby_draco_battle_explanation_1 onlayer ab_parallax
    hide myers_lobby_draco_battle_explanation_2 onlayer ab_parallax
    show myers_lobby_draco_battle_explanation_1 onlayer ab_parallax:
        yoffset 50
        linear 0.5 yoffset 100 alpha 0
    show myers_lobby_draco_battle_explanation_2 onlayer ab_parallax:
        yoffset -50
        linear 0.5 yoffset -100 alpha 0
    hide myers_lobby_draco_battle_explanation_wheel onlayer ab_parallax
    hide myers_lobby_draco_battle_explanation_wheel_2 onlayer ab_parallax
    with Dissolve(0.5)
    hide myers_lobby_draco_battle_explanation_1 onlayer ab_parallax
    hide myers_lobby_draco_battle_explanation_2 onlayer ab_parallax

    jump myers_lobby_draco_battle_end


label myers_lobby_draco_death:

    hide myers_lobby_winston onlayer ab_parallax
    hide myers_lobby_emanon onlayer ab_parallax
    hide myers_lobby_charles onlayer ab_parallax
    hide myers_lobby_claude onlayer ab_parallax
    $ renpy.transition(wipeDown)

    $ renpy.block_rollback()

    hide screen myers_lobby_draco_battle_chance

    stop music fadeout 6.0

    show black-bg onlayer front:
        parallel:
            zoom 1.5 xalign 0.5 yalign 0.5
        parallel:
            alpha 0.3
            pause 0.3
            alpha 0.15
            pause 0.6
            alpha 0.1
            pause 0.05
            alpha 0.9
            pause 0.5
            alpha 0.15
            pause 0.01
            alpha 0.4
            pause 0.01
            alpha 0.5
            pause 0.05
            alpha 0.05
            pause 0.05
            alpha 0.7
            pause 0.05
            alpha 0.0
            pause 0.05
            alpha 0.5
            pause 0.35
            alpha 0.95
            pause 1.0
            repeat
    show draco_fisheye_eye onlayer front:
        xalign 0.5 yalign 0.5
    hide bad_tv_signal onlayer tvsignal

    $ renpy.transition(Dissolve(0.1))

    $ renpy.music.set_volume(0.3, delay=0, channel='electricity')
    $ renpy.music.play("music/electricity.ogg", channel="electricity", loop=False)

    $ renpy.pause(4.0, hard=True)

    show draco_fisheye_4 onlayer front:
        xalign 0.5 yalign 0.5 alpha 0
    show draco_fisheye_3 onlayer front:
        xalign 0.5 yalign 0.5 alpha 1
    with Dissolve(0.3)
    $ renpy.pause(0.3, hard=True)

    cyb_dra "\"Sorry, {w=0.5}Lady [name!t].\" "

    $ renpy.music.stop(channel="electricity", fadeout = 1.0)

    $ renpy.pause(0.5, hard=True)

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/myers lobby/engine off.ogg"

    show black-bg onlayer front:
        zoom 1.5 xalign 0.5 yalign 0.5 alpha 1

    $ renpy.pause(2.0, hard=True)

    cyb_dra "\"The game is over.\""

    $ renpy.pause(1.0, hard=True)

    hide draco_fisheye_eye onlayer front
    hide draco_fisheye_4 onlayer front
    hide draco_fisheye_3 onlayer front
    hide black-bg onlayer front
    scene black-bg

    $ renpy.pause(1.0, hard=True)

    jump death
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
