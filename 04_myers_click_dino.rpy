

transform movefromright_dino_dino:
    linear 0.5 xpos -3.0

transform movefromleft_dino:
    linear 1.0 xpos 0.0

label dino_intro:

    $ renpy.free_memory()

    scene myers_back_no_door
    pause 0.5

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    hide screen inventory_screen
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    van "Хммм..."

    $ rollback_ = True

    van "Похоже, {w=0.5}что и черного хода здесь нет."

    $ rollback_ = False

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/MGS alert.ogg"

    show dino_normal:
        xpos 2.0
        movefromright_dino_dino
    $ renpy.pause(0.2, hard='True')

    van "!?"

    hide dino_normal

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/shake.ogg"
    van "\"Подождите, {w=0.5}подождите секунду!\" {w=0.5}Закричала я." with Shake((0.5, 1.0, 0.5, 1.0), 3.0, dist=15)

    $ rollback_ = True

    show dino_surprised:
        xpos -1.0
        movefromleft_dino

    $ renpy.pause(1.0, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music "music/Dino bgm.ogg"

    pause 0.5
    $ dino_pos = Position(xpos=0.50, ypos=1.0)

    pause 1.0

    show dino_normal at dino_pos with Dissolve(0.2)
    hide dino_surprised

    pause 0.5

    window show

    anon "\"О, {w=0.5}привет, {w=0.5}как дела?\""

    anon "\"Прошу прощения за это, {w=0.5}я был занят работой и не заметил Вас.\""

    $ dino_job_question = False
    $ dino_who_question = False

    van "......{w=0.5}Работой?"

    window hide

    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    menu:
        "Работой? Какой работой?":
            $ dino_job_question = True
            jump job_question_dino
        "Кто Вы? Что Вы здесь делаете?":

            $ dino_who_question = True
            jump who_question_dino

label job_question_dino:

    window show

    $ renpy.block_rollback()
    $ rollback_ = False

    van "\"Работой? {w=0.5}Какой работой?\""

    $ rollback_ = True

    show dino_surprised at dino_pos with Dissolve(0.2)

    anon "\"Ну, {w=0.5}как видите, {w=0.5}я уборщик.\""

    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound ["<silence 0.6>", "music/gibberish.ogg"]

    anon "\"Меня зовут ?Daeg^)an I*ssa?c N*?oel Odach$owski?. {w=0.5}Но вы можете звать меня просто {color=#f00}Дино{/color}.\""

    van "......Хах?"

    jump dino_intro_2

label who_question_dino:

    window show

    $ renpy.block_rollback()
    $ rollback_ = False

    van "\"Кто Вы? {w=0.5}Что Вы здесь делаете?\""

    $ rollback_ = True

    show dino_surprised at dino_pos with Dissolve(0.2)

    anon "\"Воу, {w=0.5}успокойтесь, {w=0.5}леди. {w=0.5}Это что, {w=0.5}какой-то допрос?\""

    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound ["<silence 0.6>", "music/gibberish.ogg"]

    anon "\"Меня зовут ?Daeg^)an I*ssa?c N*?oel Odach$owski?. {w=0.5}Но вы можете звать меня просто {color=#f00}Дино{/color}.\""

    van "...Хах?"

    jump dino_intro_2

label dino_intro_end:


    if dino_job_question:
        dino "\"Моя обязанность - содержать это место в абсолютной чистоте, {w=0.5}не оставляя ни малейшего следа пыли!\""

        hide dino_surprised with Dissolve(0.2)

        van "......Этот парень необычайно подозрительный."

    if dino_who_question:

        $ say_who = _("Дино")

        dino "\"Как Вы могли заметить, {w=0.5}прямо сейчас я занимаюсь уборкой этого места.\""

        hide dino_surprised with Dissolve(0.2)

        dino "Я могу Вам чем-нибудь помочь, {w=0.5}мисс?\""

        dino "\"Если нет, {w=0.5}то мне бы хотелось вернуться к работе.\""

        $ say_who = ""


    window hide

    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    menu:
        "На кого Вы работаете?":
            jump hire_question_dino
        "Зачем Вы подметаете снаружи Майерс?":

            jump why_question_dino


label hire_question_dino:

    window show

    $ rollback_ = False
    $ renpy.block_rollback()

    van "\"На кого Вы работаете?\""

    $ rollback_ = True

    show dino_surprised at dino_pos with Dissolve(0.2)

    $ say_who = _("Дино")

    dino "\"На кого я работаю? {w=0.5}О, нет, нет, нет.\""

    hide dino_surprised with Dissolve(0.2)

    $ say_who = ""

    dino "\"Видите ли, {w=0.5}хоть я и называю уборку своей работой, {w=0.5}на самом деле это не более чем мое хобби.\""

    dino "\"Можете считать меня... {w=0.5}самозанятым. {w=0.5}Да.\""

    van "......?"

    jump dino_other_questions

label why_question_dino:

    window show

    $ rollback_ = False
    $ renpy.block_rollback()

    van "\"Зачем Вы подметаете снаружи Майерс?\""

    $ rollback_ = True

    $ say_who = _("Дино")

    show dino_surprised at dino_pos with Dissolve(0.2)

    dino "\"Зачем же?\""

    hide dino_surprised with Dissolve(0.2)

    dino "\"Действительно ли мне нужна причина для этого? {w=0.5}Что если мне это просто нравится?\""

    $ say_who = ""

    van "...Уборщик, который любит свою работу? {w=0.5}Весьма необычно."

    jump dino_other_questions

label dino_other_questions:

    van "Есть ли что-то еще, {w=0.5}о чем мне следует спросить его?"


label dino_other_questions_2:

    window hide

    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    menu:
        "Как Вы связаны с Корпорацией Майерс?":

            window show

            van "\"Как Вы связаны с Корпорацией Майерс?\""

            show dino_surprised at dino_pos with Dissolve(0.2)

            dino "\"Корпорацией Майерс? {w=0.5}С ней я {color=#f00}никак не связан{/color}.\""

            dino "\"Я всего лишь уборщик.\""

            hide dino_surprised with Dissolve(0.2)

            jump dino_other_questions_2
        "Я не расслышала Ваше имя, не могли бы Вы повторить?":


            window show

            van "\"Я не расслышала Ваше имя, {w=0.5}не могли бы Вы повторить?\""

            show dino_surprised at dino_pos with Dissolve(0.2)

            $ renpy.music.set_volume(0.5, delay=0, channel='sound')
            play sound ["<silence 0.6>", "music/gibberish.ogg"]

            dino "\"Меня зовут ?Daeg^)an I*ssa?c N*?oel Odach?$owski?.\""

            dino "\"Но, {w=0.5}серьезно, {w=0.5}зовите меня просто Дино.\""

            hide dino_surprised with Dissolve(0.2)

            jump dino_other_questions_2
        "Знаете, вы очень похожи на Майкла Майерса.":


            window show

            van "\"Знаете, {w=0.5}вы очень похожи на Майкла Майерса.\""

            show dino_surprised at dino_pos with Dissolve(0.2)

            dino "!"

            dino "\"Хорошо подмечено, {w=0.5}Мисс!\""

            dino "\"Дело в том, {w=0.5}что я фанат Майкла Майерса номер один!\""

            dino "\"Его изящество и элегантность - это то, {w=0.5}к чему все мы должны стремиться!\""

            hide dino_surprised with Dissolve(0.2)

            van "...Зачем я вообще об этом заговорила?"

            jump dino_other_questions_2
        "Закончить разговор":


            jump new_trash

label new_trash:

    window hide

    stop music fadeout 6.0

    $ renpy.pause(1.0, hard='True')

    pause 2.0

    $ renpy.pause(0.1, hard='True')

    show dino_surprised at dino_pos with Dissolve(0.2)

    pause 1.0

    window show

    dino "\"Знаете, {w=0.5}мне кажется, {w=0.5}что Корпорация Майерс довольно удивительна.\""

    dino "\"Несмотря на то, {w=0.5}что это место закрыто уже более пяти лет, {w=0.5}здесь по-прежнему каждый день можно найти новый мусор.\""

    van "!?"

    van "\"Новый мусор? {w=0.5}Что Вы имеете под этим в виду?\""

    hide dino_surprised with Dissolve(0.2)

    dino "\"Эммм... {w=0.5}Ну, {w=0.5}знаете, {w=0.5}всякий мусор.\""

    dino "\"Порой можно найти {color=#f00}трупы киборгов{/color}, {w=0.5}а иногда - новые граффити или плакаты. {w=0.5}В общем, {w=0.5}всякие странные вещи.\""

    van "......"

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music ["<silence 1.0>", "music/dark suspense.ogg"]
    queue music "music/dark suspense.ogg"

    van "Ответ Дино вызвал еще больше вопросов в моей голове."

    van "Корпорация закрыта более пяти лет, {w=0.5}но каждый день в ее стенах появляются новые вещи?"

    van "......"

    van "......Этому есть лишь одно объяснение."

    window hide

    $ renpy.pause(0.1, hard='True')
    show myers-2-small
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    stop music fadeout 2.0
    $ renpy.pause(0.1, hard='True')


    $ renpy.pause(0.5, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/suspense 2.ogg"
    $ renpy.pause(0.6, hard='True')
    show myers-3-small with Dissolve(0.2)
    $ renpy.pause(0.2, hard='True')

    show black

    $ renpy.pause(1.0, hard='True')

    pause 1.0

    van "{color=#f00}Корпорация Майерс вовсе не полностью заброшена.{/color}"

    hide myers-3-small
    hide myers-2-small
    hide black
    with Dissolve(0.5)

    pause 0.5

    $ renpy.music.set_volume(0.5, delay=0, channel='music')
    play music "music/wind.ogg" fadein 3.0 fadeout 3.0

    window show

    van "Но чтобы убедиться в этом, {w=0.5}мне нужно найти способ проникнуть внутрь."

    van "\"Дино, {w=0.5}Вы не знаете, {w=0.5}как можно попасть внутрь Корпорации Майерс?\""

    show dino_surprised at dino_pos with Dissolve(0.2)

    dino "\"Хммм... {w=0.5}Насчет этого...\""

    dino "\"Я слышал, {w=0.5}что в Майерс есть {color=#f00}секретный проход для сотрудников{/color}.\""

    dino "\"Возможно, {w=0.5}где-то на улице есть механизм, {w=0.5}который открывает этот вход.\""

    dino "\"Но это все, {w=0.5}что я знаю.\""

    van "...Секретный проход для сотрудников?"

    window hide

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    $ renpy.pause(0.5, hard='True')

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/UI Dark.ogg"
    noname "Цель: {w=0.5}Найти потайной ход для сотрудников"

    $ rollback_ = False
    $ renpy.block_rollback()
    $ _rollback = False

    show screen inventory_screen
    hide dino_surprised
    show dino_normal

    call screen myers_back with Dissolve(0.1)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
