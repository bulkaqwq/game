







image myers_1 = "images/myers-click/myers-front-small.png"
image myers_2 = "images/myers-click/myers-front-2-small.png"
image myers_gate = "images/myers-click/myers-gate-small.png"

image dino_normal = "images/myers-click/dino-normal-small.png"
image dino_surprised = "images/myers-click/dino_surprised-small.png"

image myers_left_1 = "images/myers-click/myers-left-1-small.png"
image myers_left_1_door = "images/myers-click/myers-left-1-door-small.png"
image myers_left_2 = "images/myers-click/myers-left-2-small.png"
image myers_right_1 = "images/myers-click/myers-right-1-small.png"
image myers_right_1_no_eye = "images/myers-click/myers-right-1-no-eye-small.png"
image myers_right_2 = "images/myers-click/myers-right-2-small.png"
image myers_back_no_door = "images/myers-click/myers-back-no-door-small.png"
image myers_poster = "images/myers-click/myers-poster-small.png"
image eye_scan_place = "images/myers-click/eye-scan-place-small.png"
image eye_scan_place_2 = "images/myers-click/eye-scan-place-2-small.png"


image gate_robot_face_1 = "images/myers-click/myers-gate-robot-face-1-small.png"


image passlock_1 = "images/myers-click/passlock-1-small.png"
image passlock_2 = "images/myers-click/passlock-2-small.png"


image get_eyeball_1 = "images/myers-click/get-eyeball-1-small.png"
image get_eyeball_2 = "images/myers-click/get-eyeball-2-small.png"
image get_eyeball_3 = "images/myers-click/get-eyeball-3-small.png"


image gate_robot_memory_1 = "images/myers-click/gate-robot-memory-1-small.png"
image gate_robot_memory_2 = "images/myers-click/gate-robot-memory-2-small.png"
image gate_robot_memory_3 = "images/myers-click/gate-robot-memory-3-small.png"


image memory_frame = "images/myers-click/memory-frame-small.png"


init 2 python:

    iEyeball = Item("Eyeball","images/myers-click/eyeball.png")

    class testItem_eye(Action):
        
        def __init__(self, item, switch, value, remove = True):
            self.item = item
            self.switch = switch
            self.value = value
            self.remove = remove
        
        def __call__(self):
            if store.active_item != None and store.active_item == self.item:
                setattr(store, self.switch, self.value)
                if self.remove:
                    store.inventory.remove(self.item)
                    store.active_item = None
                renpy.jump("gate_end")
            renpy.restart_interaction()



transform movefromright_dino_1:
    linear 0.5 xpos -3.0

label myers_click:

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    $ renpy.music.set_volume(0.5, delay=0, channel='music')
    play music "music/wind.ogg" fadeout 3.0

    $ visit_gate = False
    $ see_dino = False
    $ see_robot = False
    $ see_passlock = False
    $ get_close_robot = False


    $ open_first_door = False
    $ see_first_door = False
    $ open_second_door = False
    $ know_eye = False


    $ gate_robot_scare = False


    $ have_eyeball = False


    $ active_item = None

    $ inventory = []
    scene myers_1


    $ renpy.pause(0.5, hard='True')

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/UI Dark.ogg"

    noname "Цель: {w=0.5}Проникнуть в Корпорацию Майерс"

    noname "Советы: Для передвижения {color=#f00}нажимайте на стрелки{/color}. {w=0.5}Собранные вами предметы будут отображаться в левом верхнем углу."

    noname "(Вы можете ускорить переходы между сценами двойным щелчком мыши)"

    $ rollback_ = False
    $ renpy.block_rollback()
    $ _rollback = False

    show screen inventory_screen

    call screen myers1 with Dissolve(0.1)

label myers__1:

    scene black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/step on dirt.ogg")

    $ renpy.pause(0.1, hard='True')

    pause 2.0

    $ renpy.pause(0.1, hard='True')

    stop sound fadeout 1.0

    scene myers_1
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    call screen myers1 with Dissolve(0.1)

label myers__2:
    scene black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/step on dirt.ogg")

    $ renpy.pause(0.1, hard='True')

    pause 2.0

    $ renpy.pause(0.1, hard='True')

    stop sound fadeout 1.0

    scene myers_2
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    call screen myers2 with Dissolve(0.1)

label myers__gate:

    scene black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/step on dirt.ogg")

    $ renpy.pause(0.1, hard='True')

    pause 2.0

    $ renpy.pause(0.1, hard='True')

    stop sound fadeout 1.0

    scene myers_gate
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    if not visit_gate:
        $ visit_gate = True

        pause 1.0

        $ _skipping = True
        $ renpy.block_rollback()
        $ _rollback = True

        van "Кажется, {w=0.5}главные ворота заперты."

        $ rollback_ = True

        van "Мне придется найти другой способ попасть внутрь."

        $ renpy.music.set_volume(1.0, delay=0, channel='sound')
        play sound "music/MGS alert.ogg"

        show dino_normal:
            xpos 2.0
            movefromright_dino_1
        $ renpy.pause(0.2, hard='True')
        $ rollback_ = False

        van "!?"

        van "Кто это был?"

        if renpy.is_skipping():
            $ renpy.choice_for_skipping()
        $ _skipping = False
        $ renpy.music.stop(channel="beep", fadeout = 0.5)

        hide dino_normal

        $ renpy.block_rollback()
        $ _rollback = False

    call screen myersgate with Dissolve(0.1)

label investigate_gate:
    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show myers_gate at Position(xpos = 0, ypos = 0)

    show myers_gate:
        ease 0.5 zoom 1.25 xoffset 0 yoffset 150

    $ renpy.pause(0.5, hard='True')

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    van "Кажется, {w=0.5}главные ворота заперты."

    $ rollback_ = True

    van "Мне придется найти другой способ попасть внутрь."

    show myers_gate:
        ease 0.5 zoom 1 xoffset 0 yoffset 0

    $ renpy.pause(0.5, hard='True')

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)
    $ renpy.block_rollback()
    $ _rollback = False

    hide myers_gate
    scene myers_gate

    call screen myersgate with Dissolve(0.1)

label myers_left__1:

    scene black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/step on dirt.ogg")

    $ renpy.pause(0.1, hard='True')

    pause 2.0

    $ renpy.pause(0.1, hard='True')

    stop sound fadeout 1.0

    if open_first_door:
        scene myers_left_1_door
    else:
        scene myers_left_1

    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    if open_first_door and not see_first_door:

        scene myers_left_1_door

        pause 1.0

        $ _skipping = True
        $ renpy.block_rollback()
        $ _rollback = True

        van "!?"

        $ rollback_ = True

        van "Это и есть тот секретный проход, {w=0.5}о котором говорил Дино?"

        if renpy.is_skipping():
            $ renpy.choice_for_skipping()
        $ _skipping = False
        $ rollback_ = False
        $ renpy.music.stop(channel="beep", fadeout = 0.5)
        $ renpy.block_rollback()
        $ _rollback = False

        $ see_first_door = True

    call screen myers_left1 with Dissolve(0.1)

label investigate_post:
    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    if not see_first_door:
        show myers_left_1 at Position(xpos = 0, ypos = 0)

        show myers_left_1:
            ease 0.5 zoom 2.0 xoffset 290 yoffset 550
    else:

        show myers_left_1_door at Position(xpos = 0, ypos = 0)

        show myers_left_1_door:
            ease 0.5 zoom 2.0 xoffset 290 yoffset 550


    $ renpy.pause(0.5, hard='True')
    show myers_poster with Dissolve(0.2)

    $ renpy.pause(0.5, hard='True')

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    noname "\"Корпорация Майерс в районе G4 является передовым предприятием и научным институтом, занимающимся реализацией средств механического протезирования.\""

    $ rollback_ = True

    noname "\"Основатель компании, {w=0.5}г-н Майерс, {w=0.5}считает, что причина, {w=0.5}по которой люди стали доминирующим видом на Земле, {w=0.5}заключается в их способности к новаторству.\""
    noname "\"И применение такой способности должно быть направлено не только на изготовление инструментов, {w=0.5}но и на {color=#f00}усиление существующих преимуществ человечества{/color}.\""
    noname "\"Поэтому Корпорация Майерс намерена пересмотреть вопрос соотношения механизмов и человеческого тела, \""
    noname "\"Большое количество сотрудников Майерс подверглось той или иной модификации.\""
    noname "\"Как следствие, {w=0.5}они демонстрируют превосходную работоспособность и являются по этой причине более компетентными, {w=0.5}чем большинство обычных людей.\""

    hide myers_poster with Dissolve(0.2)

    if not see_first_door:
        show myers_left_1:
            ease 0.5 zoom 1.0 xoffset 0 yoffset 0
        $ renpy.pause(0.5, hard='True')
        hide myers_left_1
        scene myers_left_1
    else:
        show myers_left_1_door:
            ease 0.5 zoom 1.0 xoffset 0 yoffset 0
        $ renpy.pause(0.5, hard='True')
        hide myers_left_1_door
        scene myers_left_1_door

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    $ renpy.block_rollback()
    $ _rollback = False

    call screen myers_left1 with Dissolve(0.1)

label myers_left__2:

    scene black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/step on dirt.ogg")

    $ renpy.pause(0.1, hard='True')

    pause 2.0

    $ renpy.pause(0.1, hard='True')

    stop sound fadeout 1.0

    scene myers_left_2
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    call screen myers_left2 with Dissolve(0.1)

label investigate_paint:
    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show myers_left_2 at Position(xpos = 0, ypos = 0)

    show myers_left_2:
        ease 0.5 zoom 1.5 xoffset 200 yoffset 250

    pause 0.5

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    van "\"Майерс- {w=0.5}Убийца.\""

    $ rollback_ = True

    van "Так гласит граффити на стене."

    show myers_left_2:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    $ renpy.pause(0.5, hard='True')

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    hide myers_left_2
    scene myers_left_2

    $ renpy.block_rollback()
    $ _rollback = False

    call screen myers_left2 with Dissolve(0.1)

label myers_right__1:
    if know_eye:
        if not gate_robot_scare:
            $ gate_robot_scare = True
            $ renpy.music.set_volume(1.0, delay=0, channel='sound')
            play sound ("music/zombie.ogg")
            scene myers_right_1
            show black-bg
            show gate_robot_face_1:
                linear 0.05 xoffset -70 yoffset 70
                linear 0.05 xoffset 70 yoffset -70
                linear 0.05 xoffset 0 yoffset 70
                linear 0.05 xoffset -70 yoffset -70
                linear 0.05 xoffset 0 yoffset 0
                repeat
            $ renpy.pause(0.3, hard='True')
            hide gate_robot_face_1
            hide black-bg
            $ renpy.transition(wipeLeft)
            $ renpy.pause(0.5, hard='True')

            scene myers_right_1
        else:

            scene black
            $ renpy.transition(Dissolve(0.5))
            $ renpy.pause(0.5, hard='True')

            $ renpy.music.set_volume(1.0, delay=0, channel='sound')
            play sound ("music/step on dirt.ogg")

            $ renpy.pause(0.1, hard='True')

            pause 2.0

            $ renpy.pause(0.1, hard='True')

            stop sound fadeout 1.0

            if have_eyeball == True:
                scene myers_right_1_no_eye
                $ renpy.transition(Dissolve(0.5))
                $ renpy.pause(0.5, hard='True')
            else:
                scene myers_right_1
                $ renpy.transition(Dissolve(0.5))
                $ renpy.pause(0.5, hard='True')
    else:

        scene black
        $ renpy.transition(Dissolve(0.5))
        $ renpy.pause(0.5, hard='True')

        $ renpy.music.set_volume(1.0, delay=0, channel='sound')
        play sound ("music/step on dirt.ogg")

        $ renpy.pause(0.1, hard='True')

        pause 2.0

        $ renpy.pause(0.1, hard='True')

        stop sound fadeout 1.0

        scene myers_right_1
        $ renpy.transition(Dissolve(0.5))
        $ renpy.pause(0.5, hard='True')

    if not see_robot:
        $ see_robot = True
        scene myers_right_1

        pause 0.5

        $ _skipping = True
        $ renpy.block_rollback()
        $ _rollback = True

        van "......"

        $ rollback_ = True

        van "У меня плохое предчувствие на этот счёт."

        if renpy.is_skipping():
            $ renpy.choice_for_skipping()
        $ _skipping = False
        $ rollback_ = False
        $ renpy.block_rollback()
        $ _rollback = False

    call screen myers_right1 with Dissolve(0.1)

label investigate_robot_gate:
    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show myers_right_1 at Position(xpos = 0, ypos = 0)

    show myers_right_1:
        ease 0.5 zoom 1.5 xoffset -200 yoffset 80

    pause 0.5

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    van "......"

    $ rollback_ = True

    van "Не думаю, что хочу приближаться к этому."

    show myers_right_1:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    $ renpy.pause(0.5, hard='True')

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)
    $ renpy.block_rollback()
    $ _rollback = False

    hide myers_right_1
    scene myers_right_1

    call screen myers_right1 with Dissolve(0.1)

label no_investigate_robot_gate:
    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show myers_right_1_no_eye at Position(xpos = 0, ypos = 0)

    show myers_right_1_no_eye:
        ease 0.5 zoom 1.5 xoffset -200 yoffset 80

    pause 0.5

    van "Сейчас мне незачем приближаться к этому киборгу."

    show myers_right_1_no_eye:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    $ renpy.pause(0.5, hard='True')

    hide myers_right_1_no_eye

    scene myers_right_1_no_eye

    call screen myers_right1 with Dissolve(0.1)

label investigate_robot_gate_face:

    if not get_close_robot:
        $ get_close_robot = True

        $ renpy.music.set_volume(1.0, delay=0, channel='sound')
        play sound ("music/zoom.wav")

        scene gate_robot_face_1 with Dissolve(0.5)

        $ renpy.pause(0.5, hard='True')

        pause 1.0

        $ _skipping = True
        $ renpy.block_rollback()
        $ _rollback = True

        van "......"

        $ rollback_ = True

        van "Что ж, {w=0.5}не похоже, что у меня есть выбор."

        if renpy.is_skipping():
            $ renpy.choice_for_skipping()
        $ _skipping = False
        $ rollback_ = False
        $ renpy.music.stop(channel="beep", fadeout = 0.5)
        $ renpy.block_rollback()
        $ _rollback = False
    else:

        $ renpy.music.set_volume(1.0, delay=0, channel='sound')
        play sound ("music/zoom.wav")

        scene gate_robot_face_1 with Dissolve(0.5)

        $ renpy.pause(0.5, hard='True')

    call screen gate_robot_face

label myers_right__2:

    scene black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/step on dirt.ogg")

    $ renpy.pause(0.1, hard='True')

    pause 2.0

    $ renpy.pause(0.1, hard='True')

    stop sound fadeout 1.0

    scene myers_right_2

    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    call screen myers_right2 with Dissolve(0.1)

label investigate_passcode:
    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show myers_right_2 at Position(xpos = 0, ypos = 0)

    show myers_right_2:
        ease 0.5 zoom 1.8 xoffset 400 yoffset 350

    pause 0.5

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    van "Несколько не связанных между собой английских букв и цифр."

    $ rollback_ = True

    van "Может, это какое-то закодированное послание? {w=0.5}О чем же оно?"

    show myers_right_2:
        ease 0.5 zoom 1 xoffset 0 yoffset 0
    $ renpy.pause(0.5, hard='True')

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)
    $ renpy.block_rollback()
    $ _rollback = False

    hide myers_right_2
    scene myers_right_2

    call screen myers_right2 with Dissolve(0.1)

label myers__back:

    scene black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/step on dirt.ogg")

    $ renpy.pause(0.1, hard='True')

    pause 2.0

    $ renpy.pause(0.1, hard='True')

    stop sound fadeout 1.0

    if not see_dino:

        scene myers_back_no_door

        $ renpy.transition(Dissolve(0.5))
        $ renpy.pause(0.5, hard='True')
    else:

        scene myers_back_no_door
        show dino_normal at dino_pos

        $ renpy.transition(Dissolve(0.5))
        $ renpy.pause(0.5, hard='True')

    if not see_dino:

        $ see_dino = True

        jump dino_intro

    call screen myers_back with Dissolve(0.1)

label dino_button_dialogue:
    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/selectsounds.ogg"
    if not open_first_door:

        show myers_back_no_door
        show dino_surprised

        $ _skipping = True
        $ renpy.block_rollback()
        $ _rollback = True

        dino "\"Я слышал, {w=0.5}что в Майерс есть секретный проход для сотрудников.\""

        $ rollback_ = True

        dino "\"Возможно, {w=0.5}где-то на улице есть механизм, {w=0.5}который открывает этот вход. {p=0.5}Но это все, {w=0.5}что я знаю.\""

        if renpy.is_skipping():
            $ renpy.choice_for_skipping()
        $ _skipping = False
        $ rollback_ = False
        $ renpy.music.stop(channel="beep", fadeout = 0.5)
        $ renpy.block_rollback()
        $ _rollback = False

        hide myers_back_no_door
        hide dino_surprised

        scene myers_back_no_door
        show dino_normal at dino_pos

        call screen myers_back with Dissolve(0.1)

    if open_first_door:
        if not know_eye:
            show myers_back_no_door
            show dino_surprised
            $ renpy.block_rollback()
            dino "\"Похоже, {w=0.5}Вам удалось открыть секретный проход.\""
            $ renpy.block_rollback()

            hide myers_back_no_door
            hide dino_surprised

            scene myers_back_no_door
            show dino_normal at dino_pos

            call screen myers_back with Dissolve(0.1)
        else:

            show myers_back_no_door
            show dino_surprised

            $ _skipping = True

            dino "\"Сканер сетчатки глаза?\""

            $ rollback_ = True

            dino "\"Хммм...{w=0.5}Может быть среди мусора найдётся несколько гнилых глазных яблок?\""

            van "............"

            if renpy.is_skipping():
                $ renpy.choice_for_skipping()
            $ _skipping = False
            $ rollback_ = False
            $ renpy.music.stop(channel="beep", fadeout = 0.5)

            hide myers_back_no_door
            hide dino_surprised

            scene myers_back_no_door
            show dino_normal at dino_pos

            call screen myers_back with Dissolve(0.1)

label investigate_passlock:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show myers_back_no_door at Position(xpos=0, ypos=0)

    hide dino_normal

    show myers_back_no_door:
        ease 0.5 zoom 2.2 xoffset 600 yoffset 550

    $ renpy.pause(0.5, hard='True')

    show passlock_1 with Dissolve(0.2)

    $ renpy.pause(0.1, hard='True')

    if not see_passlock:
        pause 0.5
        van "Это... {w=0.5}кодовый замок?"
        $ see_passlock = True

    window hide

    jump myers_click_passcode_screen_initialization

label myers_click_figure_out_passcode:

    $ myers_click_entered_passcode = list("")

    $ myers_click_num_enter_passcode = 0

    hide passlock_1
    hide passlock_2
    with Dissolve(0.3)

    show myers_back_no_door:
        ease 0.3 zoom 1 xoffset 0 yoffset 0

    $ renpy.pause(0.5, hard='True')


    if open_first_door:
        show dino_surprised with Dissolve(0.2)

        $ renpy.pause(0.1, hard='True')

        $ renpy.music.set_volume(0.6, delay=0, channel='sound')
        play sound "music/motor.ogg"

        with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

        $ renpy.pause(0.1, hard='True')

        pause 2.0

        $ _skipping = True
        $ renpy.block_rollback()
        $ _rollback = True

        dino "\"О, {w=0.5}похоже, {w=0.5}Вам удалось открыть секретный проход.\""

        $ rollback_ = True

        van "\"Да...\""

        van "Но где именно?"

        if renpy.is_skipping():
            $ renpy.choice_for_skipping()
        $ _skipping = False
        $ rollback_ = False
        $ renpy.music.stop(channel="beep", fadeout = 0.5)
        $ renpy.block_rollback()
        $ _rollback = False

        hide dino_surprised

    hide myers_back_no_door

    scene myers_back_no_door
    show dino_normal at dino_pos

    call screen myers_back with Dissolve(0.1)

label eye_scan__place:

    scene black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/step on dirt.ogg")

    $ renpy.pause(0.1, hard='True')

    pause 2.0

    $ renpy.pause(0.1, hard='True')

    stop sound fadeout 1.0

    scene eye_scan_place
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    if not know_eye:

        pause 1.0

        $ _skipping = True
        $ renpy.block_rollback()
        $ _rollback = True

        van "Войдя внутрь, {w=0.5}я увидела перед собой еще одну плотно закрытую дверь."

        $ rollback_ = True

        van "......"

        van "Ну, {w=0.5}видимо, {w=0.5}одной преградой не обойтись."

        pause 0.5

        $ renpy.music.set_volume(1.0, delay=0, channel='sound')
        play sound ("music/zoom.wav")

        show eye_scan_place at Position(xpos=0, ypos=0)

        show eye_scan_place:
            ease 0.5 zoom 2.2 xoffset -300 yoffset 600

        $ renpy.pause(0.5, hard='True')

        pause 0.5

        van "Что это?"

        van "Что-то вроде {color=#f00}сканера сетчатки глаза{/color}?"

        van "Я приблизила свое лицо прямо к нему."

        $ renpy.music.set_volume(1.0, delay=0, channel='sound')
        play sound "music/tech interface.ogg"

        van "......"

        van "Ну конечно."

        van "Похоже, {w=0.5}что мне придется найти другой способ обойти эту защиту."

        show eye_scan_place:
            ease 0.5 zoom 1 xoffset 0 yoffset 0

        $ renpy.pause(0.5, hard='True')

        if renpy.is_skipping():
            $ renpy.choice_for_skipping()
        $ _skipping = False
        $ rollback_ = False
        $ renpy.music.stop(channel="beep", fadeout = 0.5)
        $ renpy.block_rollback()
        $ _rollback = False

        $ know_eye = True

        scene eye_scan_place

    call screen eye_scanplace with Dissolve(0.1)

label investigate_scan_door:

    $ renpy.hide_screen("displayTextScreen")

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show eye_scan_place at Position(xpos=0, ypos=0)

    show eye_scan_place:
        ease 0.5 zoom 1.3 xoffset 10 yoffset 180

    $ renpy.pause(0.5, hard='True')

    pause 0.5

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    van "Дверь наглухо закрыта."

    $ rollback_ = True

    van "Нужно найти способ миновать систему сканирования сетчатки глаза."

    show eye_scan_place:
        ease 0.5 zoom 1 xoffset 0 yoffset 0

    $ renpy.pause(0.5, hard='True')

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)
    $ renpy.block_rollback()
    $ _rollback = False

    hide eye_scan_place
    scene eye_scan_place

    call screen eye_scanplace with Dissolve(0.1)

label get_eyeball:

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/selectsounds.ogg"

    window show

    van "Стоит ли мне вынуть глазное яблоко?"

    window hide

    menu:
        "Да":
            $ renpy.pause(0.1, hard='True')

            $ have_eyeball = True
            $ _skipping = True

            $ renpy.block_rollback()
            $ _rollback = True

            stop music fadeout 1.0

            hide screen inventory_screen with Dissolve(0.2)
            $ renpy.pause(0.5, hard='True')

            show get_eyeball_1
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.7, hard='True')
            show get_eyeball_2
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.7, hard='True')
            $ renpy.music.set_volume(1.0, delay=0, channel='sound')
            play sound "music/squish.ogg"
            show get_eyeball_3
            $ renpy.transition(Dissolve(0.2))
            $ renpy.pause(0.7, hard='True')
            pause 0.5



            image gate_robot_memory_1_blurred = im.Blur("images/myers-click/gate-robot-memory-1-small.png", 1.5)
            image gate_robot_memory_2_blurred = im.Blur("images/myers-click/gate-robot-memory-2-small.png", 1.5)
            image gate_robot_memory_3_blurred = im.Blur("images/myers-click/gate-robot-memory-3-small.png", 1.5)

            van "!?"

            $ renpy.music.set_volume(1.0, delay=0, channel='robot memory')
            $ renpy.music.play("music/Incoming Suspense.ogg", channel="robot memory", loop=False)

            show memory_frame
            show gate_robot_memory_1 behind memory_frame

            show gate_robot_memory_1_blurred:
                ease 0.4 xoffset -10 yoffset -10 alpha 0.5

                ease 0.4 xoffset 10 yoffset -10 alpha 0.5

                ease 0.4 xoffset -10 yoffset 10 alpha 0.5

                ease 0.4 xoffset 10 yoffset 10 alpha 0.5

                ease 0.4 xoffset 0 yoffset 0 alpha 1.0

                repeat

            $ renpy.transition(Fade(.2, 0, 0.25, color="#fff"))
            $ renpy.pause(0.5, hard='True')

            $ renpy.pause(4.0, hard='True')

            hide gate_robot_memory_1_blurred

            show gate_robot_memory_2 behind memory_frame

            show gate_robot_memory_2_blurred:
                ease 0.4 xoffset -10 yoffset -10 alpha 0.5

                ease 0.4 xoffset 10 yoffset -10 alpha 0.5

                ease 0.4 xoffset -10 yoffset 10 alpha 0.5

                ease 0.4 xoffset 10 yoffset 10 alpha 0.5

                ease 0.4 xoffset 0 yoffset 0 alpha 1.0

                repeat

            $ renpy.transition(Fade(.2, 0, 0.25, color="#fff"))
            $ renpy.pause(0.5, hard='True')

            $ renpy.pause(4.2, hard='True')

            hide gate_robot_memory_2_blurred

            show gate_robot_memory_3 behind memory_frame

            show gate_robot_memory_3_blurred:
                ease 0.4 xoffset -10 yoffset -10 alpha 0.5

                ease 0.4 xoffset 10 yoffset -10 alpha 0.5

                ease 0.4 xoffset -10 yoffset 10 alpha 0.5

                ease 0.4 xoffset 10 yoffset 10 alpha 0.5

                ease 0.4 xoffset 0 yoffset 0 alpha 1.0

                repeat

            $ renpy.transition(Fade(.2, 0, 0.25, color="#fff"))
            $ renpy.pause(0.5, hard='True')

            $ renpy.pause(4.5, hard='True')

            $ renpy.music.set_volume(1.0, delay=0, channel='sound')
            play sound "music/magic teleport.ogg"

            hide gate_robot_memory_3_blurred
            hide gate_robot_memory_1
            hide gate_robot_memory_2
            hide gate_robot_memory_3
            hide memory_frame
            $ renpy.transition(Fade(.2, 0, 0.25, color="#fff"))
            $ renpy.pause(0.5, hard='True')

            $ renpy.pause(0.1, hard='True')
            pause 1.0

            van "!?"

            van "Что...{w=0.5} это было?"

            $ rollback_ = True

            van "Что за {color=#f00}комнату{/color} я увидела?"

            $ renpy.music.set_volume(0.2, delay=0, channel='music')
            play music "music/wind.ogg" fadeout 3.0

            scene myers_right_1_no_eye with Dissolve(0.2)

            if renpy.is_skipping():
                $ renpy.choice_for_skipping()
            $ _skipping = False
            $ renpy.music.stop(channel="robot memory", fadeout = 0.5)
            $ renpy.music.stop(channel="beep", fadeout = 0.5)

            pause 0.5
            $ renpy.pause(0.5, hard='True')

            $ renpy.music.set_volume(0.8, delay=0, channel='sound')
            play sound "music/UI Dark.ogg"

            noname "Получен предмет: {w=0.5}Глазное яблоко киборга"

            noname "Советы: {w=0.5}Щелкните {color=#f00}левой кнопкой мыши{/color}, {w=0.5}чтобы выбрать объект, {w=0.5}который вы хотите использовать; {w=0.5}выбранный объект будет выделен {color=#f00}красным цветом{/color}."

            noname "Нажав на объект еще раз, {w=0.5}можно снять выделение и продолжить обычное исследование."

            $ renpy.block_rollback()
            $ _rollback = False
            $ rollback_ = False

            show screen inventory_screen with Dissolve(0.2)


            $ store.inventory.append(iEyeball)
            $ store.active_item = None
            $ renpy.restart_interaction()

            $ setattr(iEyeball, "selected", False)


            call screen myers_right1 with Dissolve(0.1)
        "Нет":



            van "...Аргх, {w=0.5}я просто не могу этого сделать."

            call screen gate_robot_face

label gate_end:

    hide screen inventory_screen

    scene eye_scan_place

    $ renpy.pause(0.5, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/weapon click.ogg"

    $ renpy.pause(0.1, hard='True')

    pause 0.5

    $ renpy.pause(0.1, hard='True')

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/motor.ogg"

    show eye_scan_place_2 with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')

    pause 1.0

    stop music fadeout 1.0

    van "Сработало."

    jump demo_end


screen myers1:
    add "images/myers-click/myers-front-small.png"

    imagebutton:
        xpos 468
        ypos 360
        idle "images/myers-click/myers-1-arrow-black-small-small.png"
        hover "images/myers-click/myers-1-arrow-white-small-small.png"
        focus_mask "images/myers-click/myers-1-arrow-white-small-small.png"
        action Jump("myers__2")

screen myers2:
    add "images/myers-click/myers-front-2-small.png"

    imagebutton:
        xpos 584
        ypos 470
        idle "images/myers-click/myers-2-arrow-black-small-small-up.png"
        hover "images/myers-click/myers-2-arrow-white-small-small-up.png"
        focus_mask "images/myers-click/myers-2-arrow-black-small-small-up.png"
        action Jump("myers__gate")

    imagebutton:
        xpos 588
        ypos 620
        idle "images/myers-click/myers-2-arrow-black-small-small.png"
        hover "images/myers-click/myers-2-arrow-white-small-small.png"
        focus_mask "images/myers-click/myers-2-arrow-black-small-small.png"
        action Jump("myers__1")

screen myersgate:
    add "images/myers-click/myers-gate-small.png"

    imagebutton:
        xpos 520
        ypos 600
        idle "images/myers-click/myers-3-arrow-black-small-small-2.png"
        hover "images/myers-click/myers-3-arrow-white-small-small-2.png"
        focus_mask "images/myers-click/myers-3-arrow-black-small-small-2.png"
        action Jump("myers__2")

    imagebutton:
        xpos 30
        ypos 560
        idle "images/myers-click/left-black-arrow-small-small.png"
        hover "images/myers-click/left-white-arrow-small-small.png"
        focus_mask "images/myers-click/left-black-arrow-small-small.png"
        action Jump("myers_left__1")

    imagebutton:
        xpos 1030
        ypos 560
        idle "images/myers-click/right-black-arrow-small-small.png"
        hover "images/myers-click/right-white-arrow-small-small.png"
        focus_mask "images/myers-click/right-black-arrow-small-small.png"
        action Jump("myers_right__1")


    imagebutton:
        xpos 295
        ypos 71
        idle "images/myers-click/gate-idle-crop-small.png"
        hover "images/myers-click/gate-hover-crop-small.png"
        focus_mask "images/myers-click/gate-hover-crop-small.png"
        action checkInteractionValid("myersgate", "investigate_gate")

screen myers_left1:
    if not open_first_door:
        add "images/myers-click/myers-left-1-small.png"
    else:
        add "images/myers-click/myers-left-1-door-small.png"

    imagebutton:
        xpos 30
        ypos 560
        idle "images/myers-click/left-black-arrow-small-small.png"
        hover "images/myers-click/left-white-arrow-small-small.png"
        focus_mask "images/myers-click/left-black-arrow-small-small.png"
        action Jump("myers_left__2")

    imagebutton:
        xpos 1030
        ypos 560
        idle "images/myers-click/right-black-arrow-small-small.png"
        hover "images/myers-click/right-white-arrow-small-small.png"
        focus_mask "images/myers-click/right-black-arrow-small-small.png"
        action Jump("myers__gate")

    imagebutton:
        xpos 397
        ypos 169
        idle "images/myers-click/poster-idle-crop-small.png"
        hover "images/myers-click/poster-hover-crop-small.png"
        focus_mask "images/myers-click/poster-hover-crop-small.png"
        action checkInteractionValid("myers_left1", "investigate_post")

    if open_first_door:
        imagebutton:
            xpos 650
            ypos 570
            idle "images/myers-click/myers-2-arrow-black-small-small-up.png"
            hover "images/myers-click/myers-2-arrow-white-small-small-up.png"
            focus_mask "images/myers-click/myers-2-arrow-black-small-small-up.png"
            action Jump("eye_scan__place")

screen myers_left2:
    add "images/myers-click/myers-left-2-small.png"

    imagebutton:
        xpos 30
        ypos 560
        idle "images/myers-click/left-black-arrow-small-small.png"
        hover "images/myers-click/left-white-arrow-small-small.png"
        focus_mask "images/myers-click/left-black-arrow-small-small.png"
        action Jump("myers__back")

    imagebutton:
        xpos 1030
        ypos 560
        idle "images/myers-click/right-black-arrow-small-small.png"
        hover "images/myers-click/right-white-arrow-small-small.png"
        focus_mask "images/myers-click/left-black-arrow-small-small.png"
        action Jump("myers_left__1")


    imagebutton:
        xpos 166
        ypos 114
        idle "images/myers-click/paint-idle-crop-small.png"
        hover "images/myers-click/paint-hover-crop-small.png"
        focus_mask "images/myers-click/paint-hover-crop-small.png"
        action checkInteractionValid("myers_left2", "investigate_paint")

screen myers_right1:
    if not have_eyeball:
        add "images/myers-click/myers-right-1-small.png"
    if have_eyeball:
        add "images/myers-click/myers-right-1-no-eye-small.png"

    imagebutton:
        xpos 30
        ypos 560
        idle "images/myers-click/left-black-arrow-small-small.png"
        hover "images/myers-click/left-white-arrow-small-small.png"
        focus_mask "images/myers-click/left-white-arrow-small-small.png"
        action Jump("myers__gate")

    imagebutton:
        xpos 1030
        ypos 560
        idle "images/myers-click/right-black-arrow-small-small.png"
        hover "images/myers-click/right-white-arrow-small-small.png"
        focus_mask "images/myers-click/right-white-arrow-small-small.png"
        action Jump("myers_right__2")


    if not have_eyeball:
        if not gate_robot_scare:
            imagebutton:
                xpos 560
                ypos 200
                idle "images/myers-click/myers-robot-idle-crop-small.png"
                hover "images/myers-click/myers-robot-hover-crop-small.png"
                focus_mask "images/myers-click/myers-robot-hover-crop-small.png"
                action Jump("investigate_robot_gate")
        else:
            imagebutton:
                xpos 560
                ypos 200
                idle "images/myers-click/myers-robot-idle-crop-small.png"
                hover "images/myers-click/myers-robot-hover-crop-small.png"
                focus_mask "images/myers-click/myers-robot-hover-crop-small.png"
                action Jump("investigate_robot_gate_face")

    if have_eyeball:
        imagebutton:
            xpos 560
            ypos 200
            idle "images/myers-click/myers-robot-idle-crop-small.png"
            hover "images/myers-click/myers-robot-hover-crop-small.png"
            focus_mask "images/myers-click/myers-robot-hover-crop-small.png"
            action checkInteractionValid("myers_right1", "no_investigate_robot_gate")


screen myers_right2:
    add "images/myers-click/myers-right-2-small.png"

    imagebutton:
        xpos 30
        ypos 560
        idle "images/myers-click/left-black-arrow-small-small.png"
        hover "images/myers-click/left-white-arrow-small-small.png"
        focus_mask "images/myers-click/left-white-arrow-small-small.png"
        action Jump("myers_right__1")

    imagebutton:
        xpos 1030
        ypos 560
        idle "images/myers-click/right-black-arrow-small-small.png"
        hover "images/myers-click/right-white-arrow-small-small.png"
        focus_mask "images/myers-click/right-black-arrow-small-small.png"
        action Jump("myers__back")

    imagebutton:
        xpos 160
        ypos 120
        idle "images/myers-click/passcode-idle-crop-small.png"
        hover "images/myers-click/passcode-hover-crop-small.png"
        focus_mask "images/myers-click/passcode-hover-crop-small.png"
        action checkInteractionValid("myers_right2", "investigate_passcode")

screen myers_back:
    if not see_dino:
        add "images/myers-click/myers-back-no-door-small.png"
    if see_dino:
        add "images/myers-click/myers-back-no-door-small.png"

        add "images/myers-click/dino-normal-small.png"

    imagebutton:
        xpos 30
        ypos 560
        idle "images/myers-click/left-black-arrow-small-small.png"
        hover "images/myers-click/left-white-arrow-small-small.png"
        focus_mask "images/myers-click/left-black-arrow-small-small.png"
        action [Hide("displayTextScreen_left"), Jump("myers_right__2")]

    imagebutton:
        xpos 1030
        ypos 560
        idle "images/myers-click/right-black-arrow-small-small.png"
        hover "images/myers-click/right-white-arrow-small-small.png"
        focus_mask "images/myers-click/right-black-arrow-small-small.png"
        action [Hide("displayTextScreen_left"), Jump("myers_left__2")]

    imagebutton:
        xpos 700
        ypos 280
        idle "images/myers-click/dialogue-idle-crop-small.png"
        hover "images/myers-click/dialogue-hover-crop-small.png"
        focus_mask "images/myers-click/dialogue-hover-crop-small.png"
        action [Hide("displayTextScreen_left"), Jump("dino_button_dialogue")]

    if not open_first_door:
        imagebutton:
            xpos 324
            ypos 213
            idle "images/myers-click/passlock-idle-crop-small.png"
            hover "images/myers-click/passlock-hover-crop-small.png"
            action Jump("investigate_passlock")

    if open_first_door:
        imagebutton:
            xpos 324
            ypos 213
            idle "images/myers-click/passlock-idle-crop-small.png"
            hover "images/myers-click/passlock-hover-crop-small.png"
            action NullAction()
            hovered Show("displayTextScreen_left", displayText = _(" Я открыла секретный проход "))
            unhovered Hide("displayTextScreen_left")

screen eye_scanplace:
    if not open_second_door:
        add "images/myers-click/eye-scan-place-small.png"

    imagebutton:
        xpos 480
        ypos 630
        idle "images/myers-click/eye-scan-arrow.png"
        hover "images/myers-click/myers-2-arrow-white-small-small.png"
        focus_mask "images/myers-click/myers-2-arrow-white-small-small.png"
        action [Hide("displayTextScreen"), Jump("myers_left__1")]


    if iEyeball not in inventory:
        imagebutton:
            xpos 738
            ypos 240
            idle "images/myers-click/scanner-idle-crop-small.png"
            hover "images/myers-click/scanner-hover-crop-small.png"
            action NullAction()
            hovered Show("displayTextScreen", displayText = _(" Я должна обойти сканер сетчатки глаза. "))
            unhovered Hide("displayTextScreen")
    else:
        imagebutton:
            xpos 738
            ypos 240
            idle "images/myers-click/scanner-idle-crop-small.png"
            hover "images/myers-click/scanner-hover-crop-small.png"
            action [Hide("displayTextScreen"), testItem_eye(iEyeball,"open_second_door", True)]
            hovered Show("displayTextScreen", displayText = _(" Я должна обойти сканер сетчатки глаза. "))
            unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 413
        ypos 66
        idle "images/myers-click/scan-gate-idle-crop-small.png"
        hover "images/myers-click/scan-gate-hover-crop-small.png"
        action [Hide("displayTextScreen"), checkInteractionValid("eye_scanplace", "investigate_scan_door")]

screen gate_robot_face:
    add "images/myers-click/myers-gate-robot-face-1-small.png"

    imagebutton:
        xpos 280
        ypos 630
        idle "images/myers-click/eye-scan-arrow.png"
        hover "images/myers-click/myers-2-arrow-white-small-small.png"
        focus_mask "images/myers-click/eye-scan-arrow.png"
        action Jump("myers_right__1")

    imagebutton:
        xpos 696
        ypos 124
        idle "images/myers-click/eyeball-idle-crop-small.png"
        hover "images/myers-click/eyeball-hover-crop-small.png"
        focus_mask "images/myers-click/eyeball-hover-crop-small.png"
        action Jump("get_eyeball")



screen displayTextScreen:
    tag bedroom_choice_1_tag
    default displayText = ""
    vbox:
        xalign 0.6
        yalign 0.55
        frame:
            text displayText

screen displayTextScreen_left:
    tag bedroom_choice_1_tag
    default displayText = ""
    vbox:
        xalign 0.2
        yalign 0.5
        frame:
            text displayText
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
