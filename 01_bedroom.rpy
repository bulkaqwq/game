




default say_who = ""
define narrator = Character("[say_who!t]", who_color = "#2e2d2d")


image bedroom_green = "images/bedroom-bg/evening-small.png"
image bedroom_blurred = im.Blur("images/bedroom-bg/evening-small.png", 1.5)
image bedroom_blue = "images/bedroom-bg/late night-small.png"


image dark_lobby = "images/lobby/lobby-small.png"

image lobby_shaodw_corner = "images/Main Title/Main Title Shadow-2.png"
image lobby_scene_blurred = im.Blur("images/lobby/lobby-small.png", 3.0)
image lobby_dust = Fixed(SnowBlossom(At("images/particles/dust-1.png", withAdd), count=10, border=50, xspeed=(-20, 20), yspeed=(4000, 4500), start=0, fast=False, horizontal=False), SnowBlossom(At("images/particles/dust-2.png", withAdd), count=10, border=50, xspeed=(-20, 20), yspeed=(-4500, -4000), start=0, fast=False, horizontal=False))


image lobby_robot_zoom_1 = "images/robot1-zoom-animation/robot1-close-small.png"
image lobby_robot_zoom_2 = "images/robot1-zoom-animation/robot1-close-small-creepy.png"


image ctc_blink:
    "gui/ctc.png"
    linear 0.5 alpha 1.0
    pause 0.25
    linear 0.5 alpha 0.0
    pause 0.25
    repeat

image ctc_blink_2:
    "gui/ctc2.png"
    alpha 1.0
    pause 0.45
    alpha 0.0
    pause 0.45
    repeat

init:

    transform constant_shake_robot_1_scene:
        linear 0.1 xoffset -5.5 yoffset 20
        linear 0.1 xoffset 5 yoffset -8
        linear 0.1 xoffset 20 yoffset -2
        linear 0.1 xoffset -20 yoffset 30
        linear 0.1 xoffset -10 yoffset 0
        repeat

    transform constant_shake_2_robot1:
        linear 0.1 xoffset -150 yoffset -40
        linear 0.1 xoffset -140 yoffset -80
        linear 0.1 xoffset -150 yoffset -75
        linear 0.1 xoffset -160 yoffset -40
        linear 0.1 xoffset -150 yoffset -68
        repeat


    transform constant_shake:
        linear 0.1 xoffset -40.5 yoffset 5
        linear 0.1 xoffset -30 yoffset -5
        linear 0.1 xoffset -40 yoffset -2
        linear 0.1 xoffset -43 yoffset 5
        linear 0.1 xoffset -40 yoffset 0
        repeat

init:

    python:

        import math

        class Shaker(object):
            
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
            
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                
                self.start = [ self.anchors.get(i, i) for i in start ]
                self.dist = dist
                self.child = child
            
            def __call__(self, t, sizes):
                
                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x
                
                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]
                
                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                
                return (int(nx), int(ny), 0, 0)

        def _Shake(start, time, child=None, dist=100.0, **properties):
            
            move = Shaker(start, child, dist=dist)
            
            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)





label day1:

    $ renpy.free_memory()

    $ renpy.music.set_volume(0.1, delay=0, channel='sound')
    play sound "music/alarm clock.ogg"

    pause 2.0

    noname "\"......\""

    noname "\"Моя голова... {w=0.5}болит...\""

    noname "\"Как долго... {w=0.5}я спала?\""

    noname "С трудом превозмогая боль, {w=0.5}я попыталась сесть."

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/lay down.mp3"
    $ renpy.pause(1.0, hard='True')
    scene bedroom_green
    show bedroom_blurred:
        zoom 1.5 xoffset -350 yoffset -300

    image bedroom_dust = Fixed(SnowBlossom(At("images/particles/dust-1.png", withAdd), count=2, border=50, xspeed=(-20, 20), yspeed=(20, 50), start=0, fast=False, horizontal=False), SnowBlossom(At("images/particles/dust-2.png", withAdd), count=2, border=50, xspeed=(-20, 20), yspeed=(20, 50), start=0, fast=False, horizontal=False))

    show bedroom_dust:
        alpha 0
        pause 5.0
        block:
            ease 5.0 alpha 0.5
            ease 5.0 alpha 1.0
            ease 5.0 alpha 0.5
            ease 5.0 alpha 0
            pause 5.0
            repeat

    $ renpy.transition(Dissolve(1.5))
    $ renpy.pause(1.5, hard='True')

    stop sound fadeout 3.0

    $ renpy.pause(0.5, hard='True')


    show bedroom_green:
        zoom 1.5 xoffset -30 yoffset 60
    hide bedroom_blurred

    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(2.0, hard='True')

    noname "!?"
    stop sound



    show bedroom_green:
        ease 0.3 zoom 1.5 xoffset -100 yoffset 300
        pause 0.5
        ease 0.3 zoom 1.5 xoffset -300 yoffset 100
        pause 0.5
        ease 0.3 zoom 1.5 xoffset 300 yoffset 300
        pause 0.5
        ease 0.3 zoom 1 xoffset 0 yoffset 0

    $ renpy.pause(3.0, hard=True)

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/shock2.ogg" fadeout 2.0
    noname "\"Где, {w=0.5}где я!?\"" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    noname "Передо мной предстала роскошная спальня, {w=0.5}декорированная превосходной обивкой, {w=0.5}с высококлассным декором, пренебрегающим всякой скромностью."


    transform withAdd:
        additive 1.0

    $ renpy.music.set_volume(0.5, delay=0, channel='music')
    play music ["<silence 1.0>", "music/bedroom suspense.ogg"] fadein 6.0
    queue music "music/bedroom suspense.ogg"

    noname "\"......{w=0.5}Что произошло?\""

    noname "Я изо всех сил пыталась вспомнить, как оказалась здесь."

    noname "\"Мой телефон. {w=0.5}Где мой телефон?\""

    $ renpy.music.set_volume(0.1, delay=0, channel='sound')
    play sound "music/cloth.mp3" fadeout 2.0

    noname "Я судорожно полезла в карманы."

    noname "\"......\""

    noname "Но его там не было."

    noname "Вот дерьмо. {w=0.5}Что мне делать?"

    noname "Что, черт возьми, произошло прошлой ночью?{p=0.5}Как я здесь оказалась?"

    noname "......"

    noname "Думаю, сперва я должна осмотреться.{p=0.5}Может быть, что-то поможет мне вспомнить."

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False

    $ renpy.pause(0.5, hard="True")

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/UI Dark.ogg"

    $ renpy.music.stop(channel="vhs", fadeout = 2.0)
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    show bedroom_green:
        zoom 1 xoffset 0 yoffset 0

    noname "Цель:{w=0.5} Выяснить, где вы находитесь."

    noname "Советы:{w=0.5} {color=#f00}Нажимайте на объекты,{/color} чтобы изучить их."

    noname "Завершить расследование можно с помощью{color=#f00} кнопки в правом верхнем углу{/color}."

    $ rollback_ = False
    $ renpy.block_rollback()

    jump bed_click

label finish_bed_click:

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/UI Dark.ogg"

    window show

    stop music fadeout 6.0
    $ _skipping = True
    noname "Расследование завершено."
    window hide

    $ renpy.block_rollback()
    $ _skipping = True

    $ renpy.music.set_volume(0.7, delay=0, channel='sound')
    play sound ("music/drawer.ogg")

    $ renpy.pause(1.0, hard="True")

    $ rollback_ = True

    noname "Тщательно осмотрев комнату, {w=0.5}я открыла ящик тумбочки и достала из него путеводитель."

    noname "Я быстро пролистала его, {w=0.5}и на самой последней странице обнаружила карту."

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/PageFlipshorter.ogg")
    $ renpy.pause(1.0, hard="True")

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False


    scene black
    show bedroom_map_1 onlayer front:
        xalign 0.5 yalign 0.5
    show screen bedroom_map_compass
    $ renpy.transition(flipfade)
    $ renpy.pause(2.0, hard="True")

    $ renpy.music.set_volume(0.8, delay=0, channel='music')
    play music ["<silence 2.0>", "music/guilt.ogg"]
    queue music "music/guilt.ogg"

    noname "Судя по тому, что мне сейчас известно, {w=0.5}я, вероятно, в..."

    $ renpy.block_rollback()
    $ rollback_ = False
    $ renpy.free_memory()

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')

    $ renpy.call_screen("bedroom_map__1", _layer="front")

label figure_out_bedroom_location:

    $ renpy.pause(2.0, hard='True')

    window show

    noname "\"Пригород G4? {w=0.5}Как я сюда попала?\""

    noname "\"......\""

    noname "Я все больше и больше приходила в замешательство."

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/footsteps.ogg" fadeout 3.0

    noname "!?" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    stop sound fadeout 6.0

    noname "И вдруг {w=0.5}череда шагов возле моей комнаты отвлекла меня от размышлений."

    $ renpy.music.set_volume(0.5, delay=0, channel='music')
    play music ["<silence 0.8>", "music/bedroom suspense.ogg"] fadein 3.0
    queue music "music/bedroom suspense.ogg"

    noname "\"...Здесь кто-то есть? {w=0.5}Может, мне пойти проверить?\""

    window hide

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False

    $ renpy.pause(0.5, hard='True')

    noname "Советы: {w=0.5}{color=#f00}Не забывайте регулярно сохраняться.{/color}"

    $ rollback_ = False
    $ renpy.block_rollback()


    image bedroom_headache = "images/bedroom-click/bedroom-headache.png"

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')

    jump bedroom_choice_start

label dont_sleep:

    $ _skipping = True
    $ renpy.block_rollback()

    pause 1.0



    show bedroom_blurred:
        ease 0.4 xoffset -10 yoffset -10 alpha 0.5

        ease 0.4 xoffset 10 yoffset -10 alpha 0.5

        ease 0.4 xoffset -10 yoffset 10 alpha 0.5

        ease 0.4 xoffset 10 yoffset 10 alpha 0.5

        ease 0.4 xoffset 0 yoffset 0 alpha 1.0

    $ renpy.pause(0.1, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/heartbeat.ogg"

    show bedroom_headache
    $ renpy.transition(Dissolve(0.4))
    $ renpy.pause(0.4, hard='True')

    hide bedroom_headache
    $ renpy.transition(Dissolve(0.4))
    $ renpy.pause(0.4, hard='True')

    show bedroom_headache
    $ renpy.transition(Dissolve(0.4))
    $ renpy.pause(0.4, hard='True')

    hide bedroom_headache
    $ renpy.transition(Dissolve(0.4))
    $ renpy.pause(0.4, hard='True')

    $ renpy.pause(0.1, hard='True')

    hide bedroom_blurred
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    pause 1.0

    noname "\"Черт...{w=0.5}{color=#f00}Моя голова...{w=0.5}Болит...{/color}\""

    $ rollback_ = True

    noname "\"Но оставаться здесь - пустая трата времени. {w=0.5}Возможно, человек снаружи что-то знает.\""

    $ renpy.music.set_volume(0.3, delay=0, channel='sound')
    play sound "music/cloth.mp3" fadeout 2.0

    pause 1.0
    noname "Я встала с кровати и направилась к двери."

    stop music fadeout 6.0
    scene black
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/open door.ogg" fadeout 1.0

    $ renpy.pause(1.0, hard='True')

    pause 1.0

    $ renpy.pause(0.1, hard='True')
    scene black
    show dark_lobby:
        zoom 1.05 xoffset -30
    show lobby_scene_blurred:
        zoom 1.05 xoffset -30
    show transparent dark-small:
        alpha 0.6
    show lobby_shaodw_corner
    $ renpy.transition(Dissolve(0.5))

    $ renpy.pause(1.0, hard='True')
    pause 1.0
    $ renpy.pause(0.1, hard='True')

    hide lobby_scene_blurred
    hide transparent dark-small
    show bedroom_dust:
        alpha 0
        pause 5.0
        block:
            ease 5.0 alpha 0.5
            ease 5.0 alpha 1.0
            ease 5.0 alpha 0.5
            ease 5.0 alpha 0
            pause 5.0
            repeat
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    pause 3.0

    noname "\"......\""

    noname "Вестибюль погружен в кромешную темноту."

    show dark_lobby:
        ease 0.5 zoom 1.5 yoffset -150 xoffset -300

    noname "Все, что мне удалось смутно различить, - это очертания барной стойки, расположенной передо мной."

    show dark_lobby:
        ease 0.5 zoom 1.05 xoffset -30 yoffset -20

    noname "\"......{w=0.5}Барная стойка?\""

    noname "Возможно, я вырубилась здесь после того, как напилась. {w=0.5}И сейчас ощущаю похмелье."

    noname "И все же..."

    noname "Учитывая обстановку, {w=0.5}я очень сомневаюсь, что бар - это то место, где я сейчас нахожусь."

    noname "На мой взгляд, {w=0.5}это место больше напоминает {color=#f00}чью-то резиденцию{/color}."

    noname "Но чей это тогда может быть дом?"

    pause 1.0

    noname "...Я понятия не имею."

    $ renpy.music.set_volume(0.7, delay=0, channel='sound')
    play sound "music/stomp.ogg" fadeout 2.0

    show dark_lobby
    show lobby_dust:
        pause 1.0
        ease 0.5 alpha 0
    hide bedroom_dust
    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 1.5, dist=15))

    $ renpy.pause(2.0, hard='True')
    stop sound fadeout 2.0
    hide lobby_dust

    $ renpy.music.set_volume(0.5, delay=0, channel='music')
    play music "music/horror build up.ogg"

    image robot1_close_zooming:
        "images/robot1-zoom-animation/robot1-close-small.png"
        ease 2.5 zoom 1.05 xoffset 0 yoffset 0
        "images/robot1-zoom-animation/robot1-close-small.png"
        ease 2.5 zoom 1
        repeat

    image robot1_close_animation:
        "images/robot1-zoom-animation/robot1-zoom-animation-1.png"
        0.2
        "images/robot1-zoom-animation/robot1-zoom-animation-2.png"
        0.2
        "images/robot1-zoom-animation/robot1-zoom-animation-3.png"
        0.2
        "images/robot1-zoom-animation/robot1-zoom-animation-4.png"
        0.2
        "images/robot1-zoom-animation/robot1-zoom-animation-5.png"
        0.2
        "images/robot1-zoom-animation/robot1-zoom-animation-6.png"
        0.2
        "images/robot1-zoom-animation/robot1-zoom-animation-7.png"
        repeat

    noname "!?"

    noname "За спиной {w=0.5}я услышала звук чего-то надвигающегося в нарастающем темпе-"

    noname "По моим барабанным перепонкам ударил тяжелый звук, становящийся почти оглушительным, по мере того, как он набирал силу,"

    noname "И мое учащенное сердцебиение стало резонировать с ним."

    noname "Что происходит?"

    noname "С опасением {w=0.5}я оглянулась..."

    $ renpy.pause(2.0, hard='True')

    $ renpy.pause(0.1, hard='True')

    stop music
    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/vin jump.ogg")

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music "music/scary violin loop.ogg" fadeout 2.0

    $ renpy.pause(0.1, hard='True')


    image robot1_satan_flash:

        "images/robot1-zoom-animation/robot1-satan-1.png"
        pause 0.1
        "images/robot1-zoom-animation/robot1-satan-3.png"
        pause 0.1
        "images/robot1-zoom-animation/robot1-satan-4.png"
        pause 0.1
        "images/robot1-zoom-animation/robot1-satan-3.png"
        pause 0.1
        "images/robot1-zoom-animation/robot1-satan-1.png"
        pause 0.1
        "images/robot1-zoom-animation/robot1-satan-3.png"
        pause 0.1
        "images/robot1-zoom-animation/robot1-satan-4.png"
        pause 0.1
        "images/robot1-zoom-animation/robot1-satan-2.png"
        pause 0.1
        repeat

    scene black
    show robot1_satan_flash behind lobby_shaodw_corner:
        alpha 0.3
        block:
            ease 0.5 alpha 0.01
            pause 1.0
            ease 0.5 alpha 0.1
            pause 1.0
            ease 0.5 alpha 0.4
            pause 1.0
            repeat

    show lobby_robot_zoom_1 behind robot1_satan_flash:
        zoom 1.5 xoffset -200 yoffset -250
        pause 1.0
        ease 1.0 zoom 1 xoffset 0 yoffset 0
        block:
            ease 2.5 zoom 1.05 xoffset -30 yoffset -35
            ease 2.5 zoom 1 xoffset 0 yoffset 0
            repeat

    show robot1_close_animation behind robot1_satan_flash:
        zoom 1.5 xoffset -200 yoffset -250
        pause 1.0
        ease 1.0 zoom 1 xoffset 0 yoffset 0
        block:
            ease 2.5 zoom 1.05 xoffset -30 yoffset -35
            ease 2.5 zoom 1 xoffset 0 yoffset 0
            repeat

    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 0.5, dist=70))
    $ renpy.pause(0.5, hard='True')

    show lobby_shaodw_corner
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.pause(2.5, hard='True')

    noname_horror "{size=+10}\"Что, {w=0.5}что это такое !!!???\"{/size}"

    noname_horror "Передо мной развернулась невообразимо жестокая сцена: {w=0.5}обезображенное лицо, наполовину распиленное; кровь, сочащаяся из сохранившихся пор {w=0.5}и образующая маленькие лужицы на полу. "

    noname_horror "Его непропорционально большой глаз выражал презрение, а каждый разорванный капилляр и сосуд, простиравшиеся вдоль склеры, {w=0.5}испускали бесчисленные выделения."

    noname_horror "И единственным, что хоть немного походило на человека..."

    stop music fadeout 3.0

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound ("music/monster moan.ogg")

    hide robot1_close_animation

    show lobby_robot_zoom_2:
        zoom 1.3 yoffset -150 xoffset -150

    show robot1_close_animation:
        zoom 1.3 yoffset -150 xoffset -150

    $ renpy.transition(Fade(.25, 0, 0, color="#fff"))
    $ renpy.pause(0.25, hard='True')
    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15))
    $ renpy.pause(1.0, hard='True')

    $ renpy.pause(1.0, hard='True')

    pause 1.0

    noname_horror "Была его вымученная, {w=0.5}перекошенная ухмылка."

    stop sound fadeout 2.0

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music "music/intense chase.ogg"

    scene dark_lobby at constant_shake:
        zoom 1.1 xoffset -20 yoffset -10
    $ renpy.transition(Dissolve(0.2))
    $ renpy.pause(0.2, hard='True')
    show lobby_shaodw_corner
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    image robot_1:
        "images/robot1-animation/robot-1-1-small.png"
        0.2
        "images/robot1-animation/robot-1-2-small.png"
        0.2
        "images/robot1-animation/robot-1-3-small.png"
        0.2
        "images/robot1-animation/robot-1-2-small.png"
        0.2
        repeat

    image robot_1_creepy:
        "images/robot1-animation/robot-1-1-creepy.png"
        0.2
        "images/robot1-animation/robot-1-2-creepy.png"
        0.2
        "images/robot1-animation/robot-1-3-creepy.png"
        0.2
        "images/robot1-animation/robot-1-2-creepy.png"
        0.2
        repeat

    $ renpy.pause(0.2, hard='True')
    show robot_1 at constant_shake_robot_1_scene
    $ renpy.transition(Dissolve(0.2))
    $ renpy.pause(0.2, hard='True')

    $ renpy.pause(0.1, hard='True')

    pause 0.5

    $ renpy.pause(0.1, hard='True')

    window hide

    $ renpy.pause(0.1, hard='True')
    pause 0.2
    $ renpy.pause(0.1, hard='True')
    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/wrong.ogg"
    show live-die-small with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')
    pause 2.0
    $ renpy.pause(0.1, hard='True')
    hide live-die-small with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')

    noname "Я поспешно отпрянула назад {w=0.5}и смогла узреть существо во весь его рост."

    noname "Кровь сочилась из каждой расщелины его тела, {w=0.5}и казалось, что оно вот-вот превратится в груду конечностей, стоит только потянуть за одну ниточку."

    $ renpy.music.set_volume(0.7, delay=0, channel='sound')
    play sound "music/first robot growl.ogg" fadeout 1.0

    hide robot_1

    show robot_1_creepy:
        zoom 1.25 xoffset -150 yoffset -70
        constant_shake_2_robot1

    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=40))

    $ renpy.pause(1.0, hard='True')

    noname "Размахивая в воздухе своей клешней, {w=0.5}оно с непостижимой болью зарычало {w=0.5}и стало надвигаться на меня."

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    stop sound
    $ renpy.pause(0.5, hard='True')

    noname "Что мне делать !?"

    $ rollback_ = False
    $ renpy.block_rollback()

    image robot_1_death_scare:
        "images/robot1-death-animation/robot1-death-animation-3.png"
        0.07
        "images/robot1-death-animation/robot1-death-animation-5.png"
        0.07
        "images/robot1-death-animation/robot1-death-animation-4.png"
        0.07
        "images/robot1-death-animation/robot1-death-animation-1.png"
        0.07
        "images/robot1-death-animation/robot1-death-animation-2.png"
        0.07
        "images/robot1-death-animation/robot1-death-animation-1.png"
        0.07
        "images/robot1-death-animation/robot1-death-animation-5.png"
        0.07
        "images/robot1-death-animation/robot1-death-animation-4.png"
        0.07
        repeat

    show screen countdown(timer_range=10, timer_jump='too_slow')
    menu:
        "Убираться из дома":
            $ renpy.block_rollback()

            hide screen countdown

            $ renpy.pause(0.1, hard='True')
            pause 0.2
            $ renpy.pause(0.1, hard='True')
            $ renpy.music.set_volume(0.8, delay=0, channel='sound')
            play sound "music/wrong.ogg"
            show wrong-small with Dissolve(0.5)
            $ renpy.pause(0.1, hard='True')
            pause 2.0
            $ renpy.pause(0.1, hard='True')
            hide wrong-small with Dissolve(0.5)
            $ renpy.pause(0.1, hard='True')

            jump escape_mansion
        "Попытаться атаковать":

            $ renpy.block_rollback()

            hide screen countdown

            $ renpy.pause(0.1, hard='True')
            pause 0.2
            $ renpy.pause(0.1, hard='True')
            $ renpy.music.set_volume(0.8, delay=0, channel='sound')
            play sound "music/wrong.ogg"
            show wrong-small with Dissolve(0.5)
            $ renpy.pause(0.1, hard='True')
            pause 2.0
            $ renpy.pause(0.1, hard='True')
            hide wrong-small with Dissolve(0.5)
            $ renpy.pause(0.1, hard='True')

            jump attack_robot_1
        "Бежать обратно в спальню":

            $ renpy.block_rollback()

            hide screen countdown
            $ robot_1_death = 'False'

            $ renpy.pause(0.1, hard='True')
            pause 0.2
            $ renpy.pause(0.1, hard='True')
            $ renpy.music.set_volume(0.5, delay=0, channel='sound')
            play sound "music/correct.ogg"
            show correct-small with Dissolve(0.5)
            $ renpy.pause(0.1, hard='True')
            pause 2.0
            $ renpy.pause(0.1, hard='True')
            hide correct-small with Dissolve(0.5)
            $ renpy.pause(0.1, hard='True')

            jump run_bedroom



label escape_mansion:
    $ renpy.block_rollback()
    noname "\"Бежать, {w=0.2}я должна бежать! {w=0.5}Я должна выбраться отсюда как можно скорее!\""

    $ rollback_ = True

    scene black with Dissolve(0.5)
    stop music fadeout 3.0
    scene grey-bg
    show black-bg
    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/run.ogg"
    noname "Я развернулась и побежала так быстро, как только могла."

    noname "Однако, {w=0.5}из-за величины этого дома я только и делала, что бегала кругами."

    noname "Поскольку вестибюль был погружен в темноту, {w=0.5}я быстро утратила всякое чувство направления."

    noname "Голова по-прежнему раскалывалась, {w=0.5}а тело с каждой секундой становилось все слабее и слабее."

    noname "Последним, что я услышала, стал надвигающийся на меня топот..."

    $ rollback_ = False
    $ renpy.block_rollback()

    stop sound

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/stomp.ogg" fadeout 2.0

    show black-bg:
        linear 0.05 xoffset -70 yoffset 70
        linear 0.05 xoffset 70 yoffset -70
        linear 0.05 xoffset 0 yoffset 70
        linear 0.05 xoffset -70 yoffset -70
        linear 0.05 xoffset 0 yoffset 0
        repeat

    $ renpy.pause(1.5, hard='True')
    scene grey-bg
    show black-bg
    stop sound fadeout 0.5
    $ renpy.pause(0.5, hard='True')

    transform mansion_robot1_death_move_in:

        zoom 1.0 xoffset 0 yoffset 1000

        ease 0.2 xoffset 0 yoffset 0

        ease 0.2 zoom 3.0 xoffset -1000 yoffset -500

    $ renpy.pause(4.0, hard='True')

    $ renpy.music.set_volume(0.8, delay=0, channel='sound1')
    $ renpy.music.play("music/first robot growl.ogg", channel="sound1", fadeout = 1.0, loop = False)

    show robot_1_death_scare at mansion_robot1_death_move_in:
        linear 0.05 xoffset -30 yoffset 30
        linear 0.05 xoffset 30 yoffset -30
        linear 0.05 xoffset -30 yoffset 30
        linear 0.05 xoffset 30 yoffset -30
        linear 0.05 xoffset 0 yoffset 0
        repeat

    $ renpy.pause(0.1, hard='True')
    show black-bg:
        linear 0.05 xoffset -70 yoffset 70
        linear 0.05 xoffset 70 yoffset -70
        linear 0.05 xoffset 0 yoffset 70
        linear 0.05 xoffset -70 yoffset -70
        linear 0.05 xoffset 0 yoffset 0
        repeat
    $ renpy.pause(0.4, hard=True)

    hide black-bg
    show black-bg

    $ renpy.music.stop(channel = "sound1", fadeout = 1.0)

    hide robot_1_death_scare
    $ renpy.transition(Dissolve(0.1))
    $ renpy.pause(0.2, hard='True')

    $ robot_1_death = 'True'

    jump death


label attack_robot_1:
    $ renpy.block_rollback()

    noname "\"Ну же, {w=0.5}я должна действовать!\""

    $ rollback_ = True

    noname "Я схватила со стола первый попавшийся предмет, {w=0.5}сделала шаг назад на достаточное расстояние и запустила им в монстра."

    noname "Но из-за изнуряющей головной боли у меня практически не осталось сил."

    stop music fadeout 3.0

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/vase.ogg"
    $ renpy.pause(0.2, hard='True')
    scene dark_lobby:
        zoom 1.1 xoffset -60 yoffset -10
    show robot-1-2-creepy:
        zoom 1.25 xoffset -150 yoffset -70

    hide robot_1
    $ renpy.pause(0.1, hard='True')
    $ renpy.transition(hpunch)
    $ renpy.pause(2.0, hard='True')

    noname "......"

    noname "Не похоже, что это имело хоть какой-то смысл."

    $ renpy.block_rollback()
    $ rollback_ = False

    scene grey-bg
    show black-bg
    $ renpy.transition(Dissolve(0.5))

    $ renpy.pause(1.5, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/heartbeat.ogg"
    queue sound "music/heartbeat.ogg"

    show black-bg:
        ease 0.4 xoffset -70 yoffset -70 alpha 0.5

        ease 0.4 xoffset 70 yoffset -70 alpha 0.5

        ease 0.4 xoffset -70 yoffset 70 alpha 0.5

        ease 0.4 xoffset 70 yoffset 70 alpha 0.5

        ease 0.4 xoffset -70 yoffset -70 alpha 0.5

        ease 0.4 xoffset 70 yoffset -70 alpha 0.5

        ease 0.4 xoffset -70 yoffset 70 alpha 0.5

        ease 0.4 xoffset 70 yoffset 70 alpha 0.5

        ease 0.4 xoffset 0 yoffset 0 alpha 1.0

    show bedroom_headache
    $ renpy.transition(Dissolve(0.4))
    $ renpy.pause(0.4, hard='True')

    hide bedroom_headache
    $ renpy.transition(Dissolve(0.4))
    $ renpy.pause(0.4, hard='True')

    show bedroom_headache
    $ renpy.transition(Dissolve(0.4))
    $ renpy.pause(0.4, hard='True')

    hide bedroom_headache
    $ renpy.transition(Dissolve(0.4))
    $ renpy.pause(0.4, hard='True')

    show bedroom_headache
    $ renpy.transition(Dissolve(0.4))
    $ renpy.pause(0.4, hard='True')

    hide bedroom_headache
    $ renpy.transition(Dissolve(0.4))
    $ renpy.pause(0.4, hard='True')

    show bedroom_headache
    $ renpy.transition(Dissolve(0.4))
    $ renpy.pause(0.4, hard='True')

    hide bedroom_headache
    $ renpy.transition(Dissolve(0.4))
    $ renpy.pause(0.4, hard='True')

    $ renpy.pause(4.0, hard='True')

    $ renpy.music.set_volume(0.8, delay=0, channel='sound1')
    $ renpy.music.play("music/first robot growl.ogg", channel="sound1", fadeout = 1.0, loop = False)

    show robot_1_death_scare at mansion_robot1_death_move_in:
        linear 0.05 xoffset -30 yoffset 30
        linear 0.05 xoffset 30 yoffset -30
        linear 0.05 xoffset -30 yoffset 30
        linear 0.05 xoffset 30 yoffset -30
        linear 0.05 xoffset 0 yoffset 0
        repeat

    $ renpy.pause(0.1, hard='True')
    show black-bg:
        linear 0.05 xoffset -70 yoffset 70
        linear 0.05 xoffset 70 yoffset -70
        linear 0.05 xoffset 0 yoffset 70
        linear 0.05 xoffset -70 yoffset -70
        linear 0.05 xoffset 0 yoffset 0
        repeat
    $ renpy.pause(0.4, hard=True)

    hide black-bg
    show black-bg

    $ renpy.music.stop(channel = "sound1", fadeout = 1.0)

    hide robot_1_death_scare
    $ renpy.transition(Dissolve(0.1))

    $ renpy.pause(0.1, hard='True')

    $ robot_1_death = 'True'

    jump death

label too_slow:

    stop music fadeout 4.0

    scene grey-bg
    show black-bg
    $ renpy.transition(Dissolve(0.2))
    $ renpy.pause(8.0, hard='True')

    $ renpy.music.set_volume(0.8, delay=0, channel='sound1')
    $ renpy.music.play("music/first robot growl.ogg", channel="sound1", fadeout = 1.0, loop = False)

    show robot_1_death_scare at mansion_robot1_death_move_in:
        linear 0.05 xoffset -30 yoffset 30
        linear 0.05 xoffset 30 yoffset -30
        linear 0.05 xoffset -30 yoffset 30
        linear 0.05 xoffset 30 yoffset -30
        linear 0.05 xoffset 0 yoffset 0
        repeat

    $ renpy.pause(0.1, hard='True')
    show black-bg:
        linear 0.05 xoffset -70 yoffset 70
        linear 0.05 xoffset 70 yoffset -70
        linear 0.05 xoffset 0 yoffset 70
        linear 0.05 xoffset -70 yoffset -70
        linear 0.05 xoffset 0 yoffset 0
        repeat
    $ renpy.pause(0.4, hard=True)

    hide black-bg
    show black-bg

    $ renpy.music.stop(channel = "sound1", fadeout = 1.0)

    hide robot_1_death_scare
    $ renpy.transition(Dissolve(0.1))

    $ renpy.pause(0.1, hard='True')

    $ robot_1_death = 'True'

    jump death


label run_bedroom:
    $ renpy.block_rollback()
    $ _skipping = True
    noname "\"С моей головной болью я не имею ни малейшего шанса против этого нечто! {w=0.5}Мне нужно спрятаться!\""
    $ rollback_ = True

    stop music fadeout 3.0
    scene black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')
    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/run and lock.ogg"
    noname "Я побежала обратно в спальню, захлопнула дверь {w=0.5}и заперла ее настолько быстро, насколько мне хватило сил."

    scene bedroom_green
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.pause(1.0, hard='True')

    pause 2.0

    $ renpy.pause(0.1, hard='True')

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/banging.ogg"
    show lobby_dust:
        pause 1.0
        ease 0.5 alpha 0
    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 1.5, dist=15))
    $ renpy.pause(1.5, hard='True')

    $ renpy.pause(1.0, hard='True')

    pause 1.0

    noname "Я затаила дыхание, {w=0.5}в то время как монстр колотил по двери, {w=0.5}стремясь разнести ее в щепки и заглушая мои тяжелые вздохи."

    $ renpy.pause(1.0, hard='True')

    play sound "music/banging.ogg"
    show lobby_dust:
        alpha 1
        pause 1.0
        ease 0.5 alpha 0
    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 1.5, dist=15))
    $ renpy.pause(1.5, hard='True')
    hide lobby_dust

    $ renpy.pause(1.0, hard='True')

    pause 2.0

    $ renpy.pause(1.0, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/footsteps.ogg" fadeout 3.0

    $ renpy.pause(1.0, hard='True')
    pause 2.0
    stop sound fadeout 3.0

    $ renpy.pause(1.0, hard='True')

    noname "......?"

    show bedroom_dust:
        alpha 0
        pause 5.0
        block:
            ease 5.0 alpha 0.5
            ease 5.0 alpha 1.0
            ease 5.0 alpha 0.5
            ease 5.0 alpha 0
            pause 5.0
            repeat

    noname "Всё закончилось? {w=0.5}Я в безопасности?"

    noname "Я постаралась вернуть себе самообладание."

    stop sound

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/shock2.ogg" fadeout 2.0
    noname "Но...{w=0.5} Теперь я заперта здесь." with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    noname "\"Что мне делать?\" {w=0.5}Меня охватило отчаяние."

    jump continue_sleep

label continue_sleep:

    $ _skipping = True

    if meet_robot_1 == False:
        $ renpy.block_rollback()
        pause 1.0



    show bedroom_blurred:
        ease 0.4 xoffset -10 yoffset -10 alpha 0.5

        ease 0.4 xoffset 10 yoffset -10 alpha 0.5

        ease 0.4 xoffset -10 yoffset 10 alpha 0.5

        ease 0.4 xoffset 10 yoffset 10 alpha 0.5

        ease 0.4 xoffset 0 yoffset 0 alpha 1.0

    $ renpy.pause(0.1, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/heartbeat.ogg"

    show bedroom_headache
    $ renpy.transition(Dissolve(0.4))
    $ renpy.pause(0.4, hard='True')

    hide bedroom_headache
    $ renpy.transition(Dissolve(0.4))
    $ renpy.pause(0.4, hard='True')

    show bedroom_headache
    $ renpy.transition(Dissolve(0.4))
    $ renpy.pause(0.4, hard='True')

    hide bedroom_headache
    $ renpy.transition(Dissolve(0.4))
    $ renpy.pause(0.4, hard='True')

    $ renpy.pause(0.1, hard='True')

    hide bedroom_blurred
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    pause 1.0

    noname "\"Ааа...{w=0.5} Моя голова...{w=0.5} Это невыносимо.\""

    $ rollback_ = True

    noname "\"Думаю,{w=0.5} для меня будет лучше,{w=0.5} если я еще немного отдохну.\""

    if meet_robot_1:
        noname "\"Я найду способ выбраться отсюда,{w=0.5} как только мне станет лучше.\""
    else:
        noname "\"Исследовать это место в моем изможденном состоянии может быть опасно, {w=0.5}так что лучше не торопиться.\""

    stop music fadeout 6.0


    image bedroom_ghost_face = "images/bedroom-click/bedroom-ghost-face.png"

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/lay down.mp3"
    noname "Я легла,{w=0.5} удобно расположилась на бархатистой кровати и укрылась одеялом."


    if meet_robot_1 == False:
        show bedroom_ghost_face
        $ renpy.transition(Dissolve(0.2))
        $ renpy.pause(0.2, hard='True')


    scene black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    pause 1.0
    $ renpy.pause(1.5, hard='True')

    noname "И уже вскоре я уснула, {w=0.5}даже не успев осознать этого."

    if meet_robot_1 == False:
        if renpy.is_skipping():
            $ renpy.choice_for_skipping()
        $ _skipping = False
        $ renpy.music.stop(channel="beep", fadeout = 0.5)
        jump bedroom_sleep_death

    window hide

    pause 1.0
    $ renpy.pause(2.0, hard='True')
    $ renpy.music.set_volume(0.6, delay=0, channel='music')
    play music "music/night.ogg" fadein 2.0 fadeout 3.0
    pause 2.0

    noname "......"

    noname "\"...А?\""

    noname "\"Который сейчас час...?\""

    stop music fadeout 3.0
    noname "Я медленно открыла глаза."



    $ renpy.pause(2.0, hard='True')


    image creepy_vic_intro_ani:

        "images/creepy victor animation/creepy_vic_1.png"
        0.1
        "images/creepy victor animation/creepy_vic_2.png"
        0.1
        "images/creepy victor animation/creepy_vic_3.png"
        0.1
        block:


            "images/creepy victor animation/creepy_vic_4.png"
            0.2
            "images/creepy victor animation/creepy_vic_5.png"
            0.2
            "images/creepy victor animation/creepy_vic_6.png"
            0.2
            "images/creepy victor animation/creepy_vic_5.png"
            0.2
            "images/creepy victor animation/creepy_vic_4.png"
            0.2
            "images/creepy victor animation/creepy_vic_7.png"
            0.2
            repeat

    scene creepy_vic_intro_ani:

        ease 10.0 zoom 1.1 xoffset -100 yoffset 0
        ease 10.0 zoom 1 xoffset 0 yoffset 0
        repeat

    show transparent dark-small:

        alpha 0.3
        pause 0.3
        alpha 0.15
        pause 0.2
        alpha 0.1
        pause 0.05
        alpha 0.3
        pause 0.5
        alpha 0.15
        pause 0.01
        alpha 0.1
        pause 0.01
        alpha 0.1
        pause 0.05
        alpha 0.05
        pause 0.05
        alpha 0.2
        pause 0.05
        alpha 0.0
        pause 0.05
        alpha 0.5
        pause 0.35
        alpha 0.1
        pause 0.05
        alpha 0.2
        pause 1.0
        repeat

    $ renpy.transition(Dissolve(0.1))
    $ renpy.pause(0.2, hard='True')
    play sound "music/vic horror.ogg"

    $ renpy.music.set_volume(0.3, delay=0, channel='electricity')
    $ renpy.music.play("music/electricity.ogg", channel="electricity", loop=False)

    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15))
    $ renpy.pause(2.0, hard='True')

    noname_vertical "{size=+8}!?{/size}"

    extend "\n{color=#f00}Передо мной возникла фигура,\nсидящая в темноте на краю моей\nкровати и уставившаяся на меня \nсвоими зловещими глазами.. {/color}"

    scene bedroom_blue
    show bedroom_dust:
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
    $ renpy.pause(1.0, hard='True')

    $ renpy.pause(1.0, hard='True')
    pause 0.5

    $ renpy.music.set_volume(0.8, delay=0, channel='music')
    play music "music/Mansion.ogg"

    $ renpy.pause(1.0, hard='True')
    pause 1.0

    $ renpy.pause(0.1, hard='True')
    show vic-normal-small at vic_pos
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.pause(1.0, hard='True')

    window show

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/shock2.ogg" fadeout 2.0
    $ renpy.pause(0.2, hard='True')
    noname "\"Кто, {w=0.5}кто ты !?\"" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    show vic-low-brow-small at vic_pos
    with Dissolve(0.2)
    noname "По какой-то причине его позабавило мое беспокойство."

    show vic-low-talk-small at vic_pos
    with Dissolve(0.2)
    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/hehe.ogg"
    pause 0.2
    anon "\"Расслабься, {w=0.5}дорогуша.\" {w=0.5}Он рассмеялся."

    anon "\"Владелец особняка просто попросил меня присмотреть за тобой и убедиться, что ты не доставишь неприятностей.\""

    hide vic-low-talk-small with Dissolve(0.2)

    noname "{color=#f00}Особняка{/color}? {w=0.5}Я в особняке?"

    hide vic-low-brow-small
    hide viv-normal-small
    with Dissolve(0.2)

    noname "\"Как я сюда попала? {w=0.5}И кто Вы такой?\""

    noname "Я бросила на него настороженный взгляд и еще больше укрыла свое тело одеялом."

    show vic-talk-small at vic_pos
    with Dissolve(0.2)

    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/huh.ogg"
    pause 0.5
    anon "\"Кто я такой?\""

    noname "Он смотрел на меня, {w=0.5}наклонив голову, {w=0.5}и,{w=0.5} как будто развлекался."

    anon "\"Меня зовут {color=#f00}Виктор Блейк{/color}, {w=0.5}и я хороший друг владельца этого особняка.\""

    show vic-normal-small at vic_pos
    hide vic-talk-small with Dissolve(0.2)

    noname "Виктор Блейк?"

    jump vic_intro

label vic_intro_end:
    noname "Я успокоилась и начала присматриваться к этому человеку."

    $ _skipping = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")
    show vic-normal-small:
        ease .5 zoom 1.5

    $ renpy.pause(1.0, hard='True')

    play sound ("music/zoom.wav")
    show vic-normal-small:
        ease .5 zoom 1.5 yoffset 320

    $ renpy.pause(1.0, hard='True')

    show vic-normal-small at vic_pos:
        ease .5 zoom 1.0 yoffset 0

    $ renpy.pause(1.5, hard='True')

    $ _skipping = True

    noname "Он носил со вкусом подобранный черный галстук и у него были яркие стильные рыжие волосы."

    noname "Но самым поразительным в нем были его необычные глаза и руки."

    noname "Это... {w=0.5}{color=#f00}механические протезы{/color}?"

    $ say_who = _("Виктор")

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/hmm.ogg"
    show vic-talk-small at vic_pos with Dissolve(0.2)
    vic "\"Ну, {w=0.5}а что касается того, как ты здесь оказалась,\""

    show vic-low-talk-small at vic_pos with Dissolve(0.2)
    vic "\"Мне лично это тоже весьма любопытно.\""

    $ say_who = ""

    show vic-normal-small at vic_pos
    hide vic-talk-small
    hide vic-low-talk-small with Dissolve(0.2)

    noname "Значит... {w=0.5}он тоже понятия не имеет, как я здесь оказалась?"

    noname "О чем мне еще стоит его спросить?"


    $ renpy.music.stop(channel="electricity", fadeout = 1.0)

    window hide

    $ explain_vincent = False

    label ask_vic_mansion:

        $ renpy.music.stop(channel="beep", fadeout = 0.5)

        menu:
            "Кто владелец этого особняка?":
                window show
                $ explain_vincent = True
                jump mansion_owner
            "Ты все это время наблюдал за тем, как я сплю?":

                window show
                jump stare_sleep
            "Что случилось с твоими глазами и руками?":

                window show
                jump arms
            "Что это была за... штука?":

                window show
                jump ask_vic_robot_1
            "Закончить разговор":

                window show
                jump stop_ask


label mansion_owner:
    noname "\"Ты упомянул, что не являешься владельцем этого места... {w=0.5}Но кто тогда владелец?\""

    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/huh.ogg"
    show vic-talk-small at vic_pos with Dissolve(0.2)

    pause 0.5

    vic "\"Владелец? {w=0.5}Его зовут {color=#f00}Винсент Эджворт{/color}.\""

    vic "\"Как бы мне выразиться... {w=0.5}он довольно очаровательный мужчина. Но в то же время он может быть {color=#f00}чрезвычайно опасен{/color}.\""

    hide vic-talk-small with Dissolve(0.2)
    noname "Винсент Эджворт?"

    noname "Хммм... {w=0.5}По какой-то причине его имя показалось мне знакомым."

    window hide

    jump ask_vic_mansion

label stare_sleep:
    noname "\"Ты все это время наблюдал за тем, как я сплю?\""

    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/hehe.ogg"
    show vic-talk-small at vic_pos with Dissolve(0.2)

    vic "\"Да,{w=0.5} это так,{w=0.5} дорогуша.\""

    vic "\"По правде говоря, {w=0.5}я даже начал завидовать тому,{w=0.5} как мирно ты спала.\""

    hide vic-talk-small with Dissolve(0.2)
    show vic-normal-small at vic_pos

    noname "...Я ощутила, как порозовели мои щеки, {w=0.5}хоть я и не была с ним знакома. "

    window hide

    jump ask_vic_mansion

label arms:

    noname "\"Что случилось с твоими глазами и руками?\""


    show vic-normal-small at vic_pos:
        alpha 0
    show vic-unhappy-small:
        xoffset 64 yoffset 20
        ease 0.2 yoffset 0

    vic "\"......\""

    noname "Виктор на мгновение замолчал."

    show vic-low-talk-small at vic_pos with Dissolve(0.2)
    hide vic-unhappy-small
    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/hmm.ogg"
    vic "\"Ну, что я могу сказать, {w=0.5}{color=#f00}есть вещи в нашей жизни, {w=0.5}которые не всегда складываются так, {w=0.5}как мы того желаем, {w=0.5}не находишь{/color}?\""

    show vic-low-brow-small at vic_pos with Dissolve(0.2)
    hide vic-low-talk-small
    noname "Он пожал плечами, {w=0.5}улыбнулся, {w=0.5}и мой вопрос, по-видимому, {w=0.5}вскоре был забыт. "

    show vic-normal-small at vic_pos:
        alpha 1
    hide vic-low-brow-small with Dissolve(0.2)

    window hide

    jump ask_vic_mansion

label ask_vic_robot_1:
    noname "\"Ты видел того жуткого монстра, {w=0.5}из тела которого сочится кровь?\""

    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/huh.ogg"
    show vic-low-talk-small at vic_pos with Dissolve(0.2)

    $ say_who = _("Виктор")

    vic "\"Монстра?\" {w=0.5}Он выглядел озадаченным."

    show vic-talk-small at vic_pos with Dissolve(0.2)
    hide vic-low-talk-small
    vic "\"Дай угадаю, {w=0.5}ты имеешь в виду тех {color=#f00}киборгов{/color}, хах?\""

    $ say_who = ""

    hide vic-talk-small with Dissolve(0.1)

    noname "Киборги? {w=0.5}И не один?"

    show vic-talk-small at vic_pos with Dissolve(0.2)
    vic "\"Не переживай так, дорогуша. {w=0.5}Они всего лишь {color=#f00}маленькие питомцы Винсента{/color}.\""

    hide vic-talk-small with Dissolve(0.2)
    if explain_vincent == True:

        noname "Питомцы !?"

        noname "Эта штука чуть не съела меня на ужин..."
    else:

        noname "Винсент? {w=0.5}Кто же он такой?"
        noname "И что за человек стал бы держать этих существ в качестве домашних животных...?"

    show vic-normal-small at vic_pos

    window hide

    jump ask_vic_mansion

label stop_ask:

    noname "Если и Виктор не знает, {w=0.5}как я здесь оказалась, {w=0.5}то мне нет нужды продолжать задавать ему вопросы."

    stop music fadeout 5.0
    noname "\"Ну что ж, {w=0.5}пожалуй, {w=0.5}мне пора уходить.\""

    $ renpy.music.set_volume(0.1, delay=0, channel='sound')
    play sound "music/cloth.mp3" fadeout 2.0
    noname "Я отодвинула в сторону роскошное одеяло и поднялась с кровати."

    if explain_vincent == True:
        noname "\"Пожалуйста, {w=0.5}поблагодари господина Эджворта от моего имени за то, {w=0.5}что он предоставил мне столь прекрасную комнату.\""

    if explain_vincent == False:
        noname "\"Пожалуйста, {w=0.5}поблагодари владельца от моего имени за то, {w=0.5}что он предоставил мне столь хорошую комнату.\""

    noname "Я направилась к двери."

    pause 0.5

    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/huh.ogg"
    show vic-talk-small at vic_pos with Dissolve(0.2)
    vic "\"Позволь спросить, {w=0.5}куда ты направляешься, {w=0.5}дорогуша?\""

    noname "Виктор посмотрел на меня с любопытством."

    hide vic-talk-small with Dissolve(0.2)

    noname "\"Куда? {w=0.5}Я возвращаюсь обратно в...\""

    noname "\"Обратно в...\""

    scene black with Dissolve(0.5)
    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music ["<silence 2.0>", "music/what happened.ogg"]
    queue music "music/what happened.ogg"

    noname "Я ощутила, {w=0.5}как моя ладонь сжалась на дверной ручке, {p=0.5}словно в тисках. {w=0.5}Я всеми силами пыталась подобрать ответ."

    noname "Куда... {w=0.5}я иду?"

    noname "Где... {w=0.5}мой дом?"

    noname "Теперь мне стало ясно, {w=0.5}что я не просто забыла произошедшее прошлой ночью."

    noname "Я..."

    noname "{color=#f00}Потеряла все свои воспоминания.{/color}"

    window hide
    stop music fadeout 6.0
    $ renpy.pause(8.0, hard='True')

    jump vincent_title_screen


label bedroom_sleep_death:

    scene grey-bg
    show black-bg

    $ renpy.pause(1.0, hard='True')

    pause 1.0

    noname "{color=#f00}Однако проснуться снова мне было не суждено.{/color}"
    $ rollback_ = False
    $ renpy.block_rollback()

    $ renpy.music.set_volume(0.5, delay=0, channel='music')
    play music "music/horror build up.ogg"

    pause 2.0

    $ renpy.pause(1.0, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/quiet open door.ogg"

    $ renpy.pause(10.0, hard='True')

    stop music fadeout 1.0

    $ renpy.music.set_volume(0.8, delay=0, channel='sound1')
    $ renpy.music.play("music/first robot growl.ogg", channel="sound1", fadeout = 1.0, loop = False)

    show robot_1_death_scare at mansion_robot1_death_move_in:
        linear 0.05 xoffset -30 yoffset 30
        linear 0.05 xoffset 30 yoffset -30
        linear 0.05 xoffset -30 yoffset 30
        linear 0.05 xoffset 30 yoffset -30
        linear 0.05 xoffset 0 yoffset 0
        repeat

    $ renpy.pause(0.1, hard='True')
    show black-bg:
        linear 0.05 xoffset -70 yoffset 70
        linear 0.05 xoffset 70 yoffset -70
        linear 0.05 xoffset 0 yoffset 70
        linear 0.05 xoffset -70 yoffset -70
        linear 0.05 xoffset 0 yoffset 0
        repeat
    $ renpy.pause(0.4, hard=True)

    $ renpy.music.stop(channel = "sound1", fadeout = 1.0)

    hide robot_1_death_scare with Dissolve(0.1)
    hide black-bg
    show black-bg

    $ renpy.pause(0.1, hard=True)

    $ robot_1_death = 'True'

    jump death
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
