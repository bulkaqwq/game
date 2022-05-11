

image game_over_banner = "images/game over/game over-banner.png"

image game_over_static:
    "images/tv-static/tv-static-1.png"
    0.07
    "images/tv-static/tv-static-2.png"
    0.07
    "images/tv-static/tv-static-3.png"
    0.07
    "images/tv-static/tv-static-4.png"
    0.07
    repeat

image game_over = "images/game over/game over-small.png"



image Main_Title_static:
    "images/empty-screen-small.png" with Dissolve(1.0)
    pause 5.0
    "game_over_static" with Dissolve(1.0)
    pause 3.0
    repeat

label death:

    $ renpy.music.set_volume(0.7, delay=0, channel='sound')
    play sound "music/stab.ogg"
    $ renpy.pause(0.1, hard='True')
    show blood-2

    pause 3.0
    $ renpy.pause(1.0, hard='True')

label death_without_blood:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/static.ogg"

    $ renpy.pause(0.1, hard='True')
    show game_over_static
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')
    show game_over behind game_over_static
    $ renpy.pause(0.1, hard='True')

    hide game_over_static
    $ renpy.transition(Dissolve(3.0))
    $ renpy.pause(3.0, hard='True')

    scene game_over
    $ renpy.pause(0.5, hard='True')


    show game_over_banner with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')

    pause 4

    $ renpy.pause(0.1, hard='True')
    show black with Dissolve(0.5)

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
