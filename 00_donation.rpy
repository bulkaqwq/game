image donation_0 = "images/donation/0.png"
image donation_1 = "images/donation/1.png"
image donation_2 = "images/donation/2.png"

image donation_text:
    contains:
        Text(_("{color=#000000}{font=futura medium condensed bt.ttf}{size=+15}ТЕПЕРЬ ДОСТУПНЫ{/size}{/font}{/color}"))
        xalign 0.51 yalign 0.28
    contains:
        Text(_("{color=#000000}{font=futura medium condensed bt.ttf}{size=+15}ПОЖЕРТВОВАНИЯ!{/size}{/font}{/color}"))
        xalign 0.515 yalign 0.40
    contains:
        Text(_("{color=#000000}{font=futura medium condensed bt.ttf}{size=+10}DINO999Z.ITCH.IO{/size}{/font}{/color}"))
        xalign 0.51 yalign 0.53
    xalign 0.5 yalign 0.5

label donation_start:

scene donation_0
$ renpy.transition(Dissolve(0.2))
$ renpy.pause(0.7, hard='True')

$ renpy.music.set_volume(0.5, delay=0, channel='sound')
play sound ["<silence 0.3>","music/bell hit.ogg"]

show donation_text:
    alpha 0
    ease 0.5 alpha 1

show donation_1:
    xoffset 550 yoffset 0
    ease 0.3 zoom 1.0 xoffset 0 yoffset 0

show donation_2:
    xoffset -550 yoffset 0
    ease 0.3 zoom 1.0 xoffset 0 yoffset 0

$ renpy.pause(0.2, hard='True')
$ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 0.5, dist=15))
$ renpy.pause(1.5, hard='True')

dino "Спасибо, что играете в эту версию!"

dino "Впервые я принимаю пожертвования на dino999z.itch.io!"

dino "Если вам нравятся мои игры и вы хотели бы помочь мне покрыть некоторые расходы на создание Винсента,"

dino "Теперь вы можете это сделать!"

dino "Если вы не можете поддержать меня таким образом, {w=0.5}то, {w=0.5}пожалуйста,"

dino "Оставьте 5-звездочный рейтинг или порекомендуйте эту игру своим друзьям,"

dino "Это также будет многое значить для меня!"

dino "И как всегда, {w=0.5}спасибо всем за вашу любовь и поддержку!"

dino "— dino999z"

scene black
$ renpy.transition(Dissolve(1.0))
$ renpy.pause(1.5, hard='True')

jump main_menu_start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
