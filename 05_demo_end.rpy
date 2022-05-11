






image to_be_continued = "images/Demo End/to-be-continued.png"
image demo_end_text = "images/Demo End/demo-end-text.png"


image demo_end_myers = "images/Demo End/mr-myers.png"
image demo_end_myers_smile = "images/Demo End/mr-myers-smile.png"
image demo_end_myers_lamp:
    "images/Demo End/mr-myers-lamp.png"
    alpha 0.5
    block:
        pause 2.5
        alpha 1.0
        linear 1.0 alpha 0.5
        pause 2.5
        alpha 1.0
        linear 1.0 alpha 0.5
        alpha 1.0
        linear 1.0 alpha 0.5
        repeat

image warning_click_to_continue_animation:

    "images/empty-screen-small.png" with Dissolve(0.5)
    pause 1.0
    "images/Main Title/click to continue.png" with Dissolve(0.5)
    pause 1.0
    repeat

screen end_click_to_continue:

    imagebutton:
        idle "images/empty-screen-small.png"
        action Jump("to_be_continued_end")

label demo_end:

    $ _skipping = True
    $ renpy.block_rollback()

    $ renpy.pause(0.5, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/flashback.ogg")

    show eye_scan_place_2 at Position(xpos=640, ypos=720)

    $ renpy.pause(4.3, hard='True')

    show eye_scan_place_2:
        ease 0.4 zoom 8.0 yoffset 3500 xoffset 800

    $ renpy.pause(0.5, hard=True)

    scene black
    stop sound fadeout 1.0

    $ renpy.pause(2.0, hard='True')

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/UI Dark.ogg"

    window show

    noname "Расследование завершено.{w=0.5} Вы успешно преодолели секретный проход."

    window hide

    $ renpy.free_memory()



    $ renpy.pause(2.0, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music ("music/TenseMusic.ogg")

    $ renpy.pause(4.0, hard='True')

    $ renpy.pause(0.1, hard='True')
    scene demo_end_myers
    show demo_end_myers_lamp
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(2.0, hard='True')

    window show

    $ _rollback = True

    anon "\"Добрый вечер,{w=0.5} месье М.\""

    $ rollback_ = True

    anon "\"Чем я могу служить Вам?\""

    window hide

    $ renpy.pause(1.5, hard=True)

    window show

    m "\"...Одна минута.\""

    m "\"Вы опоздали на одну минуту.\""

    window hide

    $ renpy.pause(1.5, hard=True)

    window show

    anon "\"......\""

    anon "\"...Прошу, {w=0.5}примите мои самые искренние извинения, {w=0.5}дорогой месье М.\""

    anon "\"Мне безумно стыдно за свое поведение.\""

    window hide

    $ renpy.pause(1.5, hard=True)

    window show

    m "\"......\""

    m "\"Я слышал, {w=0.5}что у Вас была важная информация для меня, {w=0.5}не так ли?\""

    window hide

    $ renpy.pause(1.5, hard=True)

    window show

    anon "\"...Да, {w=0.5}сэр.{w=0.5} У меня есть как хорошая, {w=0.5}так и плохая новость.\""

    m "\"Ох?\""

    anon "\"Хорошая новость - {w=0.5}согласно надежному источнику, {w=0.5}она пришла в сознание.\""

    anon "\"Но плохая новость в том, {w=0.5}что она, {w=0.5}похоже, {w=0.5}не помнит, кто она такая.\""

    window hide

    $ renpy.pause(1.0, hard=True)

    window show

    m "\"......\""

    m "\"Это весьма неожиданно.\""

    window hide

    $ renpy.pause(1.0, hard=True)

    window show

    anon "\"Что ж -\""

    anon "\"Каков Ваш план, {w=0.5}дорогой месье М?\""

    window hide

    $ renpy.pause(2.0, hard='True')

    $ say_who = "???"

    window show

    m "\"......\""

    m "\"План?\""

    m "\"У меня его нет.\""

    stop music fadeout 7.0

    show demo_end_myers_smile
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    m "\"Все, {w=0.5}что нам нужно делать... {w=0.5}Это оставаться здесь и ждать ее прибытия.\""
    window hide

    $ say_who = ""

    $ renpy.pause(0.5, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/demo end impact.ogg")
    scene black

    $ renpy.pause(5.0, hard='True')

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/UI Dark.ogg"

    window show

    noname "Глава Один: {w=0.5}Конец"

    window hide

    jump chapter_2
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
