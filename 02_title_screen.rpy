
image title_screen_1 = "images/title screen/title-screen-1.png"
image title_screen_1_name = "images/title screen/title-screen-1-my-name.png"
image title_screen_2 = "images/title screen/title-screen-2.png"

label vincent_title_screen:

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/KILLSWITCH.ogg" fadeout 5.0

    show title_screen_1

    $ renpy.pause(2.0, hard='True')

    show title_screen_1_name
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.pause(2.0, hard='True')

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/title screen static.ogg" fadeout 5.0

    show game_over_static:
        alpha 0.0

        linear 1.0 alpha 0.5


    show title_screen_2 behind game_over_static:
        ease 2.0 alpha 0
    hide title_screen_1_name
    hide title_screen_1

    $ renpy.pause(0.1, hard='True')

    stop sound fadeout 3.0

    $ renpy.pause(2.0, hard='True')


    jump day_1_lobby
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
