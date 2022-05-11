
label bedroom_choice_start:

    show transparent dark-small:
        alpha 0.8

    call screen bedroom__choice with Dissolve(0.2)

transform bedroom_move_image_button_1:
    on hover:
        xpos 170 ypos 70
    on idle:
        xpos 200 ypos 100

transform bedroom_move_image_button_2:
    on hover:
        xpos 700 ypos 70
    on idle:
        xpos 730 ypos 100

screen bedroom__choice:

    imagebutton:
        xpos 200
        ypos 100
        idle "images/bedroom-click/bedroom-choice/bedroom-choice-1-idle.png"
        hover "images/bedroom-click/bedroom-choice/bedroom-choice-1-hover.png"
        hovered [Play("sound", "music/quiet open door short.ogg"), Show("bedroom_choice_1_text")]
        unhovered Hide("bedroom_choice_1_text")
        at bedroom_move_image_button_1
        action [Hide("bedroom_choice_1_text"), Jump("bedroom_choose_dont_sleep")]

    imagebutton:
        xpos 730
        ypos 100
        idle "images/bedroom-click/bedroom-choice/bedroom-choice-2-idle.png"
        hover "images/bedroom-click/bedroom-choice/bedroom-choice-2-hover.png"
        hovered [Play("sound", "music/lay down.ogg"), Show("bedroom_choice_2_text")]
        unhovered Hide("bedroom_choice_2_text")
        at bedroom_move_image_button_2
        action [Hide("bedroom_choice_2_text"), Jump("bedroom_choose_continue_sleep")]

screen bedroom_choice_1_text:
    tag bedroom_choice_1_tag
    default displayText = _(" ПОКИНУТЬ КОМНАТУ И ОСМОТРЕТЬСЯ ")
    vbox:
        xalign 0.16
        yalign 0.93
        frame:
            text displayText

screen bedroom_choice_2_text:
    tag bedroom_choice_1_tag
    default displayText = _(" ОСТАТЬСЯ И ЕЩЁ ОТДОХНУТЬ ")
    vbox:
        xalign 0.815
        yalign 0.93
        frame:
            text displayText

label bedroom_choose_continue_sleep:


    hide screen bedroom__choice

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/selectsounds.ogg"

    hide transparent dark-small

    $ renpy.transition(Dissolve(0.2))
    $ renpy.pause(0.2, hard='True')

    $ meet_robot_1 = False


    hide screen bedroom__choice

    jump continue_sleep


label bedroom_choose_dont_sleep:


    hide screen bedroom__choice

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/selectsounds.ogg"

    hide transparent dark-small

    $ renpy.transition(Dissolve(0.2))
    $ renpy.pause(0.2, hard='True')

    $ meet_robot_1 = True


    hide screen bedroom__choice

    jump dont_sleep
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
