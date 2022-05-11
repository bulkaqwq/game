


image intro_vic = "images/vic-intro/vic-normal-small.png"
image intro_vic_bg = "images/vic-intro/vic-background.png"
image intro_vic_bg_1 = "images/vic-intro/vic-background-1.png"
image intro_vic_bg_2 = "images/vic-intro/vic-background-2.png"
image intro_vic_shadow = "images/vic-intro/vic-shadow.png"
image intro_vic_victor = "images/vic-intro/vic-victor.png"
image intro_vic_blake = "images/vic-intro/vic-blake.png"
image intro_vic_arrow_1 = "images/vic-intro/vic-arrow-1.png"
image intro_vic_arrow_2 = "images/vic-intro/vic-arrow-2.png"
image intro_vic_chinese = "images/vic-intro/vic-chinese.png"


image intro_vin = "images/vin-intro/vin-arm-normal-small.png"
image intro_vin_bg = "images/vin-intro/vin-intro-background.png"
image intro_vin_chinese = "images/vin-intro/vin-intro-chinese.png"
image intro_vin_vincent = "images/vin-intro/vin-intro-vincent.png"
image intro_vin_edgeworth = "images/vin-intro/vin-intro-edgeworth.png"
image intro_vin_shadow = "images/vin-intro/vin-intro-shadow.png"


image dino_back = "images/myers-click/dino-intro-background.png"
image dino_text = "images/myers-click/dino-text.png"
image dino_chinese = "images/myers-click/dino-chinese.png"
image dino_normal_2 = "images/myers-click/dino-intro-dino.png"
image dino_intro_arrow = "images/myers-click/dino-intro-arrow.png"
image dino_intro_shadow = "images/myers-click/dino-intro-shadow.png"


image draco_back = "images/draco-intro/draco-intro-background.png"
image draco_text = "images/draco-intro/draco-text.png"
image draco_chinese = "images/draco-intro/draco-chinese.png"
image draco_normal_2 = "images/draco-intro/draco_normal_2.png"
image draco_intro_shadow = "images/draco-intro/draco-intro-shadow.png"


image zalmona_back = "images/zal-intro/zalmona-intro-background.png"
image zalmona_text = "images/zal-intro/zalmona-text.png"
image zalmona_chinese = "images/zal-intro/zalmona-chinese.png"
image zalmona_normal_2 = "images/zal-intro/Zalmona_normal_2.png"
image zalmona_intro_shadow = "images/zal-intro/Zalmona-intro-shadow.png"


image winston_back = "images/win-intro/winston-intro-background.png"
image intro_winston_winston = "images/win-intro/winston-intro-winston.png"
image intro_winston_loomis = "images/win-intro/winston-intro-loomis.png"
image winston_normal_2 = "images/win-intro/winston-normal.png"
image intro_winston_shadow = "images/win-intro/winston-intro-shadow.png"
image intro_winston_chinese = "images/win-intro/winston-intro-chinese.png"


image vanora_back = "images/van-intro/van-intro-background.png"
image vanora_text = "images/van-intro/van-intro-vanora.png"
image vanora_chinese = "images/van-intro/van-intro-chinese.png"
image vanora_intro_shadow = "images/van-intro/van-intro-shadow.png"
image vanora_normal_2 = "images/van-intro/vanora_normal.png"

transform movefromright:
    linear 0.5 xpos 0.25

transform movefromleft:
    linear 0.5 xpos 0.0

transform movefromright_dino:
    linear 0.5 xpos 0.0

label vic_intro:
    window hide
    $ renpy.pause(0.1, hard='True')
    $ renpy.music.set_volume(0.7, delay=0, channel='sound')
    play sound "music/teleport.ogg"
    show intro_vic_bg
    show intro_vic_bg_1:
        xoffset -2000
        linear 0.8 xoffset -200
        linear 6.0 xoffset 0
    show intro_vic_bg_2:
        xoffset 2000
        linear 0.8 xoffset 200
        linear 6.0 xoffset 0
    show intro_vic_arrow_1:
        xoffset 1800 yoffset -275
        pause 0.8
        linear 0.2 xoffset -200 yoffset 25
    show intro_vic_victor:
        xoffset 2000 yoffset -320
        pause 0.8
        linear 0.2 xoffset 0 yoffset -8
        linear 4 xoffset -70 yoffset 0
    show intro_vic_arrow_2:
        xoffset -2000 yoffset 300
        pause 0.8
        linear 0.2 xoffset 0 yoffset 0
    show intro_vic_blake:
        xoffset -2000 yoffset 300
        pause 0.8
        linear 0.2 xoffset -55 yoffset 8
        linear 4 xoffset 15 yoffset 0
    show intro_vic_shadow:
        xpos 1.5
        pause 0.5
        linear 0.52 xpos 0.22
    show intro_vic:
        xpos 1.5
        pause 0.5
        linear 0.5 xpos 0.25
        linear 4 xoffset 50
    $ renpy.transition(Fade(.25, 0, 0.25, color="#fff"))
    $ renpy.pause(1.0, hard='True')
    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/bell hit.ogg"
    $ renpy.music.set_volume(0.5, delay=0, channel='char name')
    $ renpy.music.play("music/Victor Blake name.ogg", channel="char name", loop=False)
    show intro_vic_chinese
    $ renpy.transition(Dissolve(0.5))
    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15))
    $ renpy.pause(0.5, hard='True')
    pause 2.5

    $ renpy.pause(0.1, hard='True')
    show intro_vic_arrow_1:
        linear 0.2 xoffset -2200 yoffset 300
    show intro_vic_victor:
        linear 0.2 xoffset -2200 yoffset 300
    show intro_vic_arrow_2:
        linear 0.2 xoffset 2000 yoffset -300
    show intro_vic_blake:
        linear 0.2 xoffset 2000 yoffset -300
    show intro_vic_chinese:
        alpha 0
    show intro_vic_shadow:
        linear 0.52 xpos 1.5
    show intro_vic:
        linear 0.52 xpos 1.5
    show intro_vic_bg_1:
        linear 0.8 xoffset -2000
    show intro_vic_bg_2:
        linear 0.8 xoffset 2000

    $ renpy.pause(0.1, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/teleback.ogg"
    $ renpy.pause(0.2, hard='True')
    hide intro_vic_bg
    hide intro_vic_bg_1
    hide intro_vic_bg_2
    hide intro_vic_arrow_1
    hide intro_vic_victor
    hide intro_vic_arrow_2
    hide intro_vic_blake
    hide intro_vic_shadow
    hide intro_vic
    hide intro_vic_chinese
    $ renpy.transition(Fade(.25, 0, 0.25, color="#fff"))
    $ renpy.pause(1.0, hard='True')

    window show

    jump vic_intro_end


label vin_intro:
    window hide
    $ renpy.pause(0.1, hard='True')
    $ renpy.music.set_volume(0.7, delay=0, channel='sound')
    play sound "music/teleport.ogg"
    show intro_vin_bg
    show intro_vic_bg_1:
        xoffset -2000
        linear 0.8 xoffset -200
        linear 6.0 xoffset 0
    show intro_vic_bg_2:
        xoffset 2000
        linear 0.8 xoffset 200
        linear 6.0 xoffset 0
    show intro_vic_arrow_1:
        xoffset 1800 yoffset -275
        pause 0.8
        linear 0.2 xoffset -200 yoffset 25
    show intro_vin_vincent:
        xoffset 2000 yoffset -320
        pause 0.8
        linear 0.2 xoffset 0 yoffset -3
        linear 4 xoffset -70 yoffset 10
    show intro_vic_arrow_2:
        xoffset -2000 yoffset 300
        pause 0.8
        linear 0.2 xoffset 0 yoffset 0
    show intro_vin_edgeworth:
        xoffset -2000 yoffset 290
        pause 0.8
        linear 0.22 xoffset -30 yoffset 0
        linear 4 xoffset 10 yoffset -5
    show intro_vin_shadow behind intro_vic_bg_1:
        xpos 1.5 ypos 3
        pause 0.5
        linear 0.52 xpos 0.22
    show intro_vin:
        xpos 1.5
        pause 0.5
        linear 0.5 xpos 0.25
        linear 4 xoffset 50
    $ renpy.transition(Fade(.25, 0, 0.25, color="#fff"))
    $ renpy.pause(1.0, hard='True')
    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/bell hit.ogg"
    $ renpy.music.set_volume(1.0, delay=0, channel='char name')
    $ renpy.music.play("music/Vincent Edgeworth name.ogg", channel="char name", loop=False)
    show intro_vin_chinese
    $ renpy.transition(Dissolve(0.5))
    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15))
    $ renpy.pause(0.5, hard='True')
    pause 2.5

    $ renpy.pause(0.1, hard='True')
    show intro_vic_arrow_1:
        linear 0.2 xoffset -2200 yoffset 300
    show intro_vin_vincent:
        linear 0.22 xoffset -2200 yoffset 300
    show intro_vic_arrow_2:
        linear 0.2 xoffset 2000 yoffset -300
    show intro_vin_edgeworth:
        linear 0.2 xoffset 2000 yoffset -300
    show intro_vin_chinese:
        alpha 0
    show intro_vin_shadow:
        linear 0.52 xpos 1.5
    show intro_vin:
        linear 0.52 xpos 1.5
    show intro_vic_bg_1:
        linear 0.8 xoffset -2000
    show intro_vic_bg_2:
        linear 0.8 xoffset 2000

    $ renpy.pause(0.1, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/teleback.ogg"
    $ renpy.pause(0.2, hard='True')
    hide intro_vin_bg
    hide intro_vic_bg_1
    hide intro_vic_bg_2
    hide intro_vic_arrow_1
    hide intro_vin_vincent
    hide intro_vic_arrow_2
    hide intro_vin_edgeworth
    hide intro_vin_shadow
    hide intro_vin
    hide intro_vin_chinese
    $ renpy.transition(Fade(.25, 0, 0.25, color="#fff"))
    $ renpy.pause(1.0, hard='True')

    window show

    jump vin_intro_end


label dino_intro_2:
    window hide
    $ renpy.pause(0.1, hard='True')
    $ renpy.music.set_volume(0.7, delay=0, channel='sound')
    play sound "music/teleport.ogg"
    show dino_back
    show intro_vic_bg_1:
        xoffset -2000
        linear 0.8 xoffset -200
        linear 6.0 xoffset 0
    show intro_vic_bg_2:
        xoffset 2000
        linear 0.8 xoffset 200
        linear 6.0 xoffset 0
    show dino_intro_arrow:
        xoffset -2000 yoffset 300
        pause 0.8
        linear 0.2 xoffset 0 yoffset 0
    show dino_text:
        xoffset -2000 yoffset 290
        pause 0.8
        linear 0.22 xoffset -70 yoffset 10
        linear 4 xoffset -30 yoffset 5
    show dino_intro_shadow behind dino_intro_arrow:
        xpos 1.5 ypos 3
        pause 0.5
        linear 0.52 xpos 0.25
    show dino_normal_2:
        xpos 1.5
        pause 0.5
        linear 0.5 xpos 0.27
        linear 4 xoffset 50
    $ renpy.transition(Fade(.25, 0, 0.25, color="#fff"))
    $ renpy.pause(1.0, hard='True')
    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/bell hit.ogg"
    $ renpy.music.set_volume(1.0, delay=0, channel='char name')
    $ renpy.music.play("music/Dino name.ogg", channel="char name", loop=False)
    show dino_chinese:
        linear 4 xoffset -50 yoffset 5
    $ renpy.transition(Dissolve(0.5))
    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15))
    $ renpy.pause(0.5, hard='True')
    pause 2.5

    $ renpy.pause(0.1, hard='True')
    show dino_intro_arrow:
        linear 0.2 xoffset -2000 yoffset 290
    show dino_text:
        linear 0.2 xoffset 2000 yoffset -300
    show dino_chinese:
        alpha 0
    show dino_intro_shadow:
        linear 0.52 xpos 1.5
    show dino_normal_2:
        linear 0.52 xpos 1.5
    show intro_vic_bg_1:
        linear 0.8 xoffset -2000
    show intro_vic_bg_2:
        linear 0.8 xoffset 2000

    $ renpy.pause(0.1, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/teleback.ogg"
    $ renpy.pause(0.2, hard='True')
    hide dino_back
    hide intro_vic_bg_1
    hide intro_vic_bg_2
    hide intro_vic_arrow_1
    hide intro_vin_vincent
    hide intro_vic_arrow_2
    hide intro_vin_edgeworth
    hide intro_vin_shadow
    hide intro_vin
    hide dino_chinese
    $ renpy.transition(Fade(.25, 0, 0.25, color="#fff"))
    $ renpy.pause(1.0, hard='True')

    window show

    jump dino_intro_end

label draco_intro:
    window hide
    $ renpy.pause(0.1, hard='True')
    $ renpy.music.set_volume(0.7, delay=0, channel='sound')
    play sound "music/teleport.ogg"
    show draco_back
    show intro_vic_bg_1:
        xoffset -2000
        linear 0.8 xoffset -200
        linear 6.0 xoffset 0
    show intro_vic_bg_2:
        xoffset 2000
        linear 0.8 xoffset 200
        linear 6.0 xoffset 0
    show dino_intro_arrow:
        xoffset -2000 yoffset 300
        pause 0.8
        linear 0.2 xoffset 0 yoffset 0
    show draco_text:
        xoffset -2000 yoffset 290
        pause 0.8
        linear 0.22 xoffset -70 yoffset 10
        linear 4 xoffset -30 yoffset 5
    show draco_intro_shadow behind dino_intro_arrow:
        xpos 1.5 ypos 3
        pause 0.5
        linear 0.52 xpos 0.25
    show draco_normal_2:
        xpos 1.3
        pause 0.5
        linear 0.5 xpos 0.25
        linear 4 xoffset 50
    $ renpy.transition(Fade(.25, 0, 0.25, color="#fff"))
    $ renpy.pause(1.0, hard='True')
    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/bell hit.ogg"
    $ renpy.music.set_volume(1.0, delay=0, channel='char name')
    $ renpy.music.play("music/draco/draco.ogg", channel="char name", loop=False)
    show draco_chinese:
        linear 4 xoffset -50 yoffset 5
    $ renpy.transition(Dissolve(0.5))
    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15))
    $ renpy.pause(0.5, hard='True')
    pause 2.5

    $ renpy.pause(0.1, hard='True')
    show dino_intro_arrow:
        linear 0.2 xoffset -2000 yoffset 290
    show draco_text:
        linear 0.2 xoffset 2000 yoffset -300
    show draco_chinese:
        alpha 0
    show draco_intro_shadow:
        linear 0.52 xpos 1.5
    show draco_normal_2:
        linear 0.52 xpos 1.5
    show intro_vic_bg_1:
        linear 0.8 xoffset -2000
    show intro_vic_bg_2:
        linear 0.8 xoffset 2000

    $ renpy.pause(0.1, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/teleback.ogg"
    $ renpy.pause(0.2, hard='True')
    hide draco_back
    hide intro_vic_bg_1
    hide intro_vic_bg_2
    hide dino_intro_arrow
    hide draco_text
    hide draco_intro_shadow
    hide draco_chinese
    $ renpy.transition(Fade(.25, 0, 0.25, color="#fff"))
    $ renpy.pause(1.0, hard='True')

    window show

    jump draco_intro_end


label zalmona_intro:
    window hide
    $ renpy.pause(0.1, hard='True')
    $ renpy.music.set_volume(0.7, delay=0, channel='sound')
    play sound "music/teleport.ogg"
    show zalmona_back
    show intro_vic_bg_1:
        xoffset -2000
        linear 0.8 xoffset -200
        linear 6.0 xoffset 0
    show intro_vic_bg_2:
        xoffset 2000
        linear 0.8 xoffset 200
        linear 6.0 xoffset 0
    show dino_intro_arrow:
        xoffset -2000 yoffset 300
        pause 0.8
        linear 0.2 xoffset 0 yoffset 0
    show zalmona_text:
        xoffset -2000 yoffset 290
        pause 0.8
        linear 0.22 xoffset -70 yoffset 10
        linear 4 xoffset -30 yoffset 5
    show zalmona_intro_shadow behind dino_intro_arrow:
        xpos 1.5 ypos 3
        pause 0.5
        linear 0.52 xpos 0.22
    show zalmona_normal_2:
        xpos 1.5
        pause 0.5
        linear 0.5 xpos 0.25
        linear 4 xoffset 50

    $ renpy.transition(Fade(.25, 0, 0.25, color="#fff"))
    $ renpy.pause(1.0, hard='True')
    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/bell hit.ogg"
    $ renpy.music.set_volume(0.6, delay=0, channel='char name')
    $ renpy.music.play("music/zalmona/Zalmona-zalmanaa.ogg", channel="char name", loop=False)
    show zalmona_chinese:
        linear 4 xoffset -50 yoffset 5
    $ renpy.transition(Dissolve(0.5))
    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15))
    $ renpy.pause(0.5, hard='True')
    pause 2.5

    $ renpy.pause(0.1, hard='True')
    show dino_intro_arrow:
        linear 0.2 xoffset -2000 yoffset 290
    show zalmona_text:
        linear 0.2 xoffset 2000 yoffset -300
    show zalmona_chinese:
        alpha 0
    show zalmona_intro_shadow:
        linear 0.52 xpos 1.5
    show zalmona_normal_2:
        linear 0.52 xpos 1.5
    show intro_vic_bg_1:
        linear 0.8 xoffset -2000
    show intro_vic_bg_2:
        linear 0.8 xoffset 2000

    $ renpy.pause(0.1, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/teleback.ogg"
    $ renpy.pause(0.2, hard='True')
    hide zalmona_back
    hide intro_vic_bg_1
    hide intro_vic_bg_2
    hide dino_intro_arrow
    hide zalmona_text
    hide draco_intro_shadow
    hide zalmona_chinese
    $ renpy.transition(Fade(.25, 0, 0.25, color="#fff"))
    $ renpy.pause(1.0, hard='True')

    jump zalmona_intro_end


label winston_intro:
    window hide
    $ renpy.pause(0.1, hard='True')
    $ renpy.music.set_volume(0.7, delay=0, channel='sound')
    play sound "music/teleport.ogg"
    show black:
        zoom 2.0 xalign 0.5 yalign 0.5
    show winston_back
    show intro_vic_bg_1:
        xoffset -2000
        linear 0.8 xoffset -200
        linear 6.0 xoffset 0
    show intro_vic_bg_2:
        xoffset 2000
        linear 0.8 xoffset 200
        linear 6.0 xoffset 0
    show intro_vic_arrow_1:
        xoffset 1800 yoffset -275
        pause 0.8
        linear 0.2 xoffset -200 yoffset 25
    show intro_winston_winston:
        xoffset 2000 yoffset -320
        pause 0.8
        linear 0.2 xoffset -20 yoffset -3
        linear 4 xoffset -60 yoffset 7
    show intro_vic_arrow_2:
        xoffset -2000 yoffset 300
        pause 0.8
        linear 0.2 xoffset 0 yoffset 0
    show intro_winston_loomis:
        xoffset -2000 yoffset 290
        pause 0.8
        linear 0.22 xoffset -30 yoffset 6
        linear 4 xoffset 10 yoffset 0
    show intro_winston_shadow behind intro_vic_bg_1:
        xpos 1.5 ypos 3
        pause 0.5
        linear 0.52 xpos 0.22
    show winston_normal_2:
        xpos 1.5
        pause 0.5
        linear 0.5 xpos 0.25
        linear 4 xoffset 50
    $ renpy.transition(Fade(.25, 0, 0.25, color="#fff"))
    $ renpy.pause(1.0, hard='True')
    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/bell hit.ogg"
    $ renpy.music.set_volume(1.0, delay=0, channel='char name')
    $ renpy.music.play("music/winston/cough2.ogg", channel="char name", loop=False)
    show intro_winston_chinese
    $ renpy.transition(Dissolve(0.5))
    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15))
    $ renpy.pause(0.5, hard='True')
    pause 2.5

    $ renpy.pause(0.1, hard='True')
    show intro_vic_arrow_1:
        linear 0.2 xoffset -2200 yoffset 300
    show intro_winston_winston:
        linear 0.22 xoffset -2200 yoffset 300
    show intro_vic_arrow_2:
        linear 0.2 xoffset 2000 yoffset -300
    show intro_winston_loomis:
        linear 0.2 xoffset 2000 yoffset -300
    show intro_winston_chinese:
        alpha 0
    show intro_winston_shadow:
        linear 0.52 xpos 1.5
    show winston_normal_2:
        linear 0.52 xpos 1.5
    show intro_vic_bg_1:
        linear 0.8 xoffset -2000
    show intro_vic_bg_2:
        linear 0.8 xoffset 2000

    $ renpy.pause(0.1, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/teleback.ogg"
    $ renpy.pause(0.2, hard='True')
    hide winston_back
    hide intro_vic_bg_1
    hide intro_vic_bg_2
    hide intro_vic_arrow_1
    hide intro_winston_winston
    hide intro_vic_arrow_2
    hide intro_winston_loomis
    hide intro_winston_shadow
    hide winston_normal_2
    hide intro_winston_chinese
    hide black
    $ renpy.transition(Fade(.25, 0, 0.25, color="#fff"))
    $ renpy.pause(1.0, hard='True')

    jump win_intro_end

label vanora_intro:
    window hide
    $ renpy.pause(0.1, hard='True')
    $ renpy.music.set_volume(0.7, delay=0, channel='sound')


    hide character_icon_box_1
    hide van_icon_normal
    hide character_icon_box_2

    play sound "music/teleport.ogg"
    show vanora_back
    show intro_vic_bg_1:
        xoffset -2000
        linear 0.8 xoffset -200
        linear 6.0 xoffset 0
    show intro_vic_bg_2:
        xoffset 2000
        linear 0.8 xoffset 200
        linear 6.0 xoffset 0
    show dino_intro_arrow:
        xoffset -2000 yoffset 300
        pause 0.8
        linear 0.2 xoffset 0 yoffset 0
    show vanora_text:
        xoffset -2000 yoffset 290
        pause 0.8
        linear 0.22 xoffset -70 yoffset 10
        linear 4 xoffset -30 yoffset 5
    show vanora_intro_shadow behind intro_vic_bg_2:
        xpos 1.5 ypos 3
        pause 0.5
        linear 0.52 xpos 0.22
    show vanora_normal_2:
        xpos 1.5
        pause 0.5
        linear 0.5 xpos 0.26
        linear 4 xoffset 50

    $ renpy.transition(Fade(.25, 0, 0.25, color="#fff"))
    $ renpy.pause(1.0, hard='True')
    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/bell hit.ogg"
    $ renpy.music.set_volume(1.0, delay=0, channel='char name')
    $ renpy.music.play("music/vanora/Vanora.ogg", channel="char name", loop=False)
    show vanora_chinese:
        linear 4 xoffset -50 yoffset 5
    $ renpy.transition(Dissolve(0.5))
    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15))
    $ renpy.pause(0.5, hard='True')
    pause 2.5

    $ renpy.pause(0.1, hard='True')
    show dino_intro_arrow:
        linear 0.2 xoffset -2000 yoffset 290
    show vanora_text:
        linear 0.2 xoffset 2000 yoffset -300
    show vanora_chinese:
        alpha 0
    show vanora_intro_shadow:
        linear 0.52 xpos 1.5
    show vanora_normal_2:
        linear 0.52 xpos 1.5
    show intro_vic_bg_1:
        linear 0.8 xoffset -2000
    show intro_vic_bg_2:
        linear 0.8 xoffset 2000

    $ renpy.pause(0.1, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/teleback.ogg"
    $ renpy.pause(0.2, hard='True')
    hide vanora_back
    hide intro_vic_bg_1
    hide intro_vic_bg_2
    hide dino_intro_arrow
    hide vanora_text
    hide vanora_intro_shadow
    hide vanora_chinese
    $ renpy.transition(Fade(.25, 0, 0.25, color="#fff"))
    $ renpy.pause(1.0, hard='True')

    jump vanora_intro_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
