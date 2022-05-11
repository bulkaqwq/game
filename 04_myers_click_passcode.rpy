






label myers_click_passcode_screen_initialization:

    $ myers_click_entered_passcode = list("")

    $ myers_click_num_enter_passcode = 0

    call screen myers_click_passcode_screen

screen myers_click_passcode_screen:

    add "images/myers-click/passlock-1-small.png"

    if myers_click_num_enter_passcode >= 1:
        add "images/myers-click/passcode_screen/passcode-censor.png"
    if myers_click_num_enter_passcode >= 2:
        add "images/myers-click/passcode_screen/passcode-censor.png" xpos 30
    if myers_click_num_enter_passcode >= 3:
        add "images/myers-click/passcode_screen/passcode-censor.png" xpos 60
    if myers_click_num_enter_passcode >= 4:
        add "images/myers-click/passcode_screen/passcode-censor.png" xpos 90
    if myers_click_num_enter_passcode >= 5:
        add "images/myers-click/passcode_screen/passcode-censor.png" xpos 120
    if myers_click_num_enter_passcode >= 6:
        add "images/myers-click/passcode_screen/passcode-censor.png" xpos 150
    if myers_click_num_enter_passcode >= 7:
        add "images/myers-click/passcode_screen/passcode-censor.png" xpos 181
    if myers_click_num_enter_passcode >= 8:
        add "images/myers-click/passcode_screen/passcode-censor.png" xpos 212



    imagebutton:
        hover "images/myers-click/passcode_screen/passcode-button-hover.png"
        idle "images/myers-click/passcode_screen/passcode-button-idle.png"
        focus_mask "images/myers-click/passcode_screen/passcode-button-hover.png"
        xpos 579
        ypos 195
        action Jump("myers_click_press_button_1")


    imagebutton:
        hover "images/myers-click/passcode_screen/passcode-button-hover.png"
        idle "images/myers-click/passcode_screen/passcode-button-idle.png"
        focus_mask "images/myers-click/passcode_screen/passcode-button-hover.png"
        xpos 652
        ypos 195
        action Jump("myers_click_press_button_2")


    imagebutton:
        hover "images/myers-click/passcode_screen/passcode-button-hover.png"
        idle "images/myers-click/passcode_screen/passcode-button-idle.png"
        focus_mask "images/myers-click/passcode_screen/passcode-button-hover.png"
        xpos 723
        ypos 195
        action Jump("myers_click_press_button_3")


    imagebutton:
        hover "images/myers-click/passcode_screen/passcode-button-hover.png"
        idle "images/myers-click/passcode_screen/passcode-button-idle.png"
        focus_mask "images/myers-click/passcode_screen/passcode-button-hover.png"
        xpos 579
        ypos 265
        action Jump("myers_click_press_button_4")


    imagebutton:
        hover "images/myers-click/passcode_screen/passcode-button-hover.png"
        idle "images/myers-click/passcode_screen/passcode-button-idle.png"
        focus_mask "images/myers-click/passcode_screen/passcode-button-hover.png"
        xpos 652
        ypos 265
        action Jump("myers_click_press_button_5")


    imagebutton:
        hover "images/myers-click/passcode_screen/passcode-button-hover.png"
        idle "images/myers-click/passcode_screen/passcode-button-idle.png"
        focus_mask "images/myers-click/passcode_screen/passcode-button-hover.png"
        xpos 723
        ypos 265
        action Jump("myers_click_press_button_6")


    imagebutton:
        hover "images/myers-click/passcode_screen/passcode-button-hover.png"
        idle "images/myers-click/passcode_screen/passcode-button-idle.png"
        focus_mask "images/myers-click/passcode_screen/passcode-button-hover.png"
        xpos 579
        ypos 338
        action Jump("myers_click_press_button_7")


    imagebutton:
        hover "images/myers-click/passcode_screen/passcode-button-hover.png"
        idle "images/myers-click/passcode_screen/passcode-button-idle.png"
        focus_mask "images/myers-click/passcode_screen/passcode-button-hover.png"
        xpos 652
        ypos 338
        action Jump("myers_click_press_button_8")


    imagebutton:
        hover "images/myers-click/passcode_screen/passcode-button-hover.png"
        idle "images/myers-click/passcode_screen/passcode-button-idle.png"
        focus_mask "images/myers-click/passcode_screen/passcode-button-hover.png"
        xpos 723
        ypos 338
        action Jump("myers_click_press_button_9")


    imagebutton:
        hover "images/myers-click/passcode_screen/passcode-button-hover.png"
        idle "images/myers-click/passcode_screen/passcode-button-idle.png"
        focus_mask "images/myers-click/passcode_screen/passcode-button-hover.png"
        xpos 579
        ypos 411
        action Jump("myers_click_press_button_arrow")


    imagebutton:
        hover "images/myers-click/passcode_screen/passcode-button-hover.png"
        idle "images/myers-click/passcode_screen/passcode-button-idle.png"
        focus_mask "images/myers-click/passcode_screen/passcode-button-hover.png"
        xpos 652
        ypos 411
        action Jump("myers_click_press_button_0")


    imagebutton:
        hover "images/myers-click/passcode_screen/passcode-button-hover.png"
        idle "images/myers-click/passcode_screen/passcode-button-idle.png"
        focus_mask "images/myers-click/passcode_screen/passcode-button-hover.png"
        xpos 723
        ypos 411
        action Jump("myers_click_press_button_confirm")


    imagebutton:
        xpos 568
        ypos 600
        idle "images/myers-click/myers-3-arrow-black-small-small-2.png"
        hover "images/myers-click/myers-3-arrow-white-small-small-2.png"
        focus_mask "images/myers-click/myers-3-arrow-black-small-small-2.png"
        action Jump("myers_click_figure_out_passcode")

label myers_click_press_button_1:

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound ("music/passcode beep.ogg")

    if myers_click_num_enter_passcode < 8:
        $ myers_click_entered_passcode.append('1')
        $ myers_click_num_enter_passcode = myers_click_num_enter_passcode + 1

    call screen myers_click_passcode_screen

label myers_click_press_button_2:

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound ("music/passcode beep.ogg")

    if myers_click_num_enter_passcode < 8:
        $ myers_click_entered_passcode.append('2')
        $ myers_click_num_enter_passcode = myers_click_num_enter_passcode + 1

    call screen myers_click_passcode_screen

label myers_click_press_button_3:

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound ("music/passcode beep.ogg")

    if myers_click_num_enter_passcode < 8:
        $ myers_click_entered_passcode.append('3')
        $ myers_click_num_enter_passcode = myers_click_num_enter_passcode + 1

    call screen myers_click_passcode_screen

label myers_click_press_button_4:

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound ("music/passcode beep.ogg")

    if myers_click_num_enter_passcode < 8:
        $ myers_click_entered_passcode.append('4')
        $ myers_click_num_enter_passcode = myers_click_num_enter_passcode + 1

    call screen myers_click_passcode_screen

label myers_click_press_button_5:

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound ("music/passcode beep.ogg")

    if myers_click_num_enter_passcode < 8:
        $ myers_click_entered_passcode.append('5')
        $ myers_click_num_enter_passcode = myers_click_num_enter_passcode + 1

    call screen myers_click_passcode_screen

label myers_click_press_button_6:

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound ("music/passcode beep.ogg")

    if myers_click_num_enter_passcode < 8:
        $ myers_click_entered_passcode.append('6')
        $ myers_click_num_enter_passcode = myers_click_num_enter_passcode + 1

    call screen myers_click_passcode_screen

label myers_click_press_button_7:

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound ("music/passcode beep.ogg")

    if myers_click_num_enter_passcode < 8:
        $ myers_click_entered_passcode.append('7')
        $ myers_click_num_enter_passcode = myers_click_num_enter_passcode + 1

    call screen myers_click_passcode_screen

label myers_click_press_button_8:

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound ("music/passcode beep.ogg")

    if myers_click_num_enter_passcode < 8:
        $ myers_click_entered_passcode.append('8')
        $ myers_click_num_enter_passcode = myers_click_num_enter_passcode + 1

    call screen myers_click_passcode_screen

label myers_click_press_button_9:

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound ("music/passcode beep.ogg")

    if myers_click_num_enter_passcode < 8:
        $ myers_click_entered_passcode.append('9')
        $ myers_click_num_enter_passcode = myers_click_num_enter_passcode + 1

    call screen myers_click_passcode_screen

label myers_click_press_button_arrow:

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound ("music/passcode beep.ogg")

    if myers_click_num_enter_passcode > 0:
        $ del myers_click_entered_passcode[-1]
        $ myers_click_num_enter_passcode = myers_click_num_enter_passcode - 1

    call screen myers_click_passcode_screen

label myers_click_press_button_0:

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound ("music/passcode beep.ogg")

    if myers_click_num_enter_passcode < 8:
        $ myers_click_entered_passcode.append('0')
        $ myers_click_num_enter_passcode = myers_click_num_enter_passcode + 1

    call screen myers_click_passcode_screen

label myers_click_press_button_confirm:

    $ myers_click_correct_passcode = [u'7', u'9', u'2', u'1', u'5', u'2', u'5', u'2']

    if myers_click_entered_passcode == myers_click_correct_passcode:

        $ renpy.music.set_volume(0.6, delay=0, channel='sound')
        play sound "music/weapon click.ogg"
        noname "Доступ разрешен."
        $ open_first_door = True

        jump myers_click_figure_out_passcode
    else:


        $ renpy.music.set_volume(0.7, delay=0, channel='sound')
        play sound "music/tech interface.ogg"
        noname "Доступ запрещен."

        $ myers_click_entered_passcode = list("")

        $ myers_click_num_enter_passcode = 0

        call screen myers_click_passcode_screen
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
