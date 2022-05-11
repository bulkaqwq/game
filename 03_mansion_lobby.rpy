
image hand_over_card = "images/business card/hand-over-card.png"
image hand_over_card_bg = "images/business card/hand-over-card-bg.png"
image hold_card = "images/business card/hold-card.png"
image hold_card_bg = "images/business card/hold-card-bg.png"
image hold_card_2 = "images/business card/hold-card-2.png"
image hold_card_2_bg = "images/business card/hold-card-bg-2.png"


image lobby_draco_pop = "images/missing/draco-pop-small.png"


image lobby_bright = "images/lobby/lobby-bright-small.png"

image lobby_vic_smoke_animation:

    "images/vic-smoke-animation/smoke 1.png"
    pause 0.2
    "images/vic-smoke-animation/smoke 0.png"
    pause 0.2
    "images/vic-smoke-animation/smoke 2.png"
    pause 0.2
    "images/vic-smoke-animation/smoke 3.png"
    pause 0.2
    "images/vic-smoke-animation/smoke 6.png"
    pause 0.2
    "images/vic-smoke-animation/smoke 4.png"
    pause 0.2
    "images/vic-smoke-animation/smoke 5.png"
    pause 0.2
    "images/vic-smoke-animation/smoke 0.png"
    pause 0.2
    repeat



image missing_1 = "images/missing/missing-1-small.png"
image missing_2 = "images/missing/missing-2-small.png"
image missing_3 = "images/missing/missing-3-small.png"
image missing_4 = "images/missing/missing-4-small.png"


image myers_small = "images/missing/myers-small.png"


image chamber_1 = "images/missing/chamber-1-small.png"
image chamber_2 = "images/missing/chamber-2-small.png"
image chamber_3 = "images/missing/chamber-3-small.png"
image blood = "images/missing/blood-small.png"


image court_1 = "images/missing/court-1-small.png"
image court_2 = "images/missing/court-2-small.png"


image winston_1 = "images/missing/winston-1-small.png"
image winston_2 = "images/missing/winston-2-small.png"


image car = "images/missing/car-small.png"


image blood_stain = "images/missing/blood stain-small.png"


image g4_street = "images/missing/g4-street-small.png"

label day_1_lobby:
    scene lobby_bright
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
    show vic-smoke-normal-small at vic_pos
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    show lobby_vic_smoke_animation:

        xoffset 70 alpha 0
        block:

            ease 5.0 xoffset 70 alpha 0
            pause 5.0
            ease 5.0 xoffset 70 alpha 0.5
            pause 5.0
            repeat

    $ renpy.music.set_volume(0.8, delay=0, channel='music')
    play music "music/jazz.ogg"
    $ renpy.pause(2.0, hard='True')
    window show
    noname "*Вздох*"

    noname "Ни имени, {w=0.5}ни денег, {w=0.5}ни документов..."

    noname "Моё положение даже хуже, чем у бродяги."

    show vic-smoke-low-talk-small at vic_pos with Dissolve(0.2)
    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/hmm.ogg"

    vic "\"Ох, {w=0.5}дорогуша, {w=0.5}не стоит так переживать.\""

    vic "\"Видишь ли, {w=0.5}потеря воспоминаний может быть также благом.\""

    vic "\"Бесчисленное количество людей оказываются в плену собственных воспоминаний; {w=0.5}они изо всех сил стараются их отпустить, {w=0.5}но в то же время цепляются за них.\""

    vic "\"Но тебе, {w=0.5}с другой стороны, {w=0.5}выпал второй шанс.\""

    $ say_who = _("Виктор")

    show vic-smoke-talk-small at vic_pos with Dissolve(0.2)
    hide vic-smoke-low-talk-small
    vic "\"Разве это не чудесно? {w=0.5}По правде говоря, {w=0.5}даже я начинаю немного завидовать.\""

    $ say_who = ""

    hide vic-smoke-talk-small with Dissolve(0.2)
    noname "...Я понимаю, к чему он клонит, {w=0.5}но серьезно, {w=0.5}что может быть хуже, чем быть бездомным?"

    noname "Я снова вздохнула."

    stop music fadeout 3.0
    $ renpy.pause(0.1, hard='True')
    $ renpy.music.set_volume(0.3, delay=0, channel='sound')
    play sound "music/mad vincent.ogg" fadeout 1.0
    show vic-smoke-upset-small at vic_pos
    anon "\"Виктор, {w=0.5}сколько раз тебе повторять? {w=0.5}Прекращай курить в моём особняке!\"" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    show vic-smoke-talk-small at vic_pos with Dissolve(0.2)
    hide vic-smoke-upset-small
    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music "music/Vincent bgm.ogg"
    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/huh.ogg"
    pause 1.0

    vic "\"Ну-ну, {w=0.5}помяни дьявола. {w=0.5}Это ли не мой дорогой друг Винсент!\""

    hide vic-smoke-talk-small

    window hide

    $ renpy.music.set_volume(0.7, delay=0, channel='sfx1')
    $ renpy.music.set_volume(0.7, delay=0, channel='sfx2')
    $ renpy.music.set_volume(0.7, delay=0, channel='sfx3_new')

    $ renpy.pause(0.01, hard=True)

    $ renpy.music.play("music/vincent-show.ogg", channel="sfx1", synchro_start=True)
    show white back
    show vin-enter-1-small
    $ renpy.transition(Fade(.2, 0, 0.2, color="#fff"))
    $ renpy.pause(0.42, hard=True)

    $ renpy.music.play("music/vincent-show.ogg", channel="sfx2", synchro_start=True)
    show vin-enter-2-small
    hide vin-enter-1-small
    $ renpy.transition(Fade(.2, 0, 0.2, color="#fff"))
    $ renpy.pause(0.42, hard=True)

    $ renpy.music.play("music/vincent-show.ogg", channel="sfx3_new", synchro_start=True)
    show vin-enter-3-small
    hide vin-enter-2-small
    $ renpy.transition(Fade(.2, 0, 0.2, color="#fff"))
    $ renpy.pause(0.42, hard=True)

    $ renpy.music.play("music/vincent-show.ogg", channel="sfx1", synchro_start=True)
    show vin-enter-small
    hide vin-enter-3-small
    $ renpy.transition(Fade(.2, 0, 0.2, color="#fff"))
    $ renpy.pause(0.42, hard=True)

    $ renpy.pause(2.0, hard='True')
    hide vin-enter-1-small
    hide vin-enter-2-small
    hide vin-enter-3-small
    hide vic-smoke-normal-small
    hide vin-enter-small
    hide white back
    hide lobby_vic_smoke_animation
    $ renpy.transition(Fade(.25, 0, 0.25, color="#fff"))
    $ renpy.pause(1.0, hard=True)

    show vic-normal-small-flip at vic_pos_2
    show vin-black-small at vin_pos_2
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard=True)


    pause 1.0

    window show

    noname "Винсент? {w=0.5}Так это он владелец особняка?"

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/vin_hmm.ogg"
    show vin-arm-angry-small at vin_pos_2
    show vic-low-brow-small-flip at vic_pos_2
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard=True)
    hide vin-black-small
    hide vic-normal-flip-small


    vin "\"Мадам, {w=0.5}если этот развратник причинил Вам какие-либо неудобства, {w=0.5}то я могу позвонить в полицию и попросить немедленно его задержать.\""

    noname "\"Ммм... {w=0.5}Думаю, я в порядке. {w=0.5}В любом случае, спасибо.\" {w=0.5}Неловко ответила я."

    noname "(...Эти двое действительно друзья?)"

    noname "\"Винсент, {w=0.5}позвольте узнать, не Вы ли являетесь владельцем этого особняка?\""

    show vin-arm-normal-small at vin_pos_2 with Dissolve(0.2)
    hide vin-arm-angry-small
    pause 1.0
    show vin-arm-talk-small at vin_pos_2 with Dissolve(0.2)

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/Vincent.ogg"

    vin "\"Да, так и есть.\" {w=0.5}Улыбнулся он."

    vin "\"Примите мои извинения за то, что не представился должным образом. {w=0.5}Моё имя - {color=#f00}Винсент Эджворт{/color}, {w=0.5}и я владелец этого особняка.\""

    jump vin_intro

label vin_intro_end:
    show vin-arm-talk-small at vin_pos_2 with Dissolve(0.2)
    vin "\"Могу я узнать Ваше имя, {w=0.5}мадам? {w=0.5}И цель вашего визита?\""

    hide vin-arm-talk-small at vin_pos_2 with Dissolve(0.2)

    noname "...Цель моего визита? {w=0.5}Так значит, это я пришла сюда?"

    noname "\"Эммм... {w=0.5}Я...\" {w=0.5}Я и не знала, что мне ответить."

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/huh.ogg"

    show vic-talk-small-flip at vic_pos_2 with Dissolve(0.2)
    vic "\"Какая досада, {w=0.5}Винсент. {w=0.5}Похоже, что наша гостья потеряла все свои воспоминания.\""
    hide vic-low-brow-small-flip
    hide vic-talk-small-flip with Dissolve(0.2)
    show vic-normal-small-flip at vic_pos_2

    noname "Виктор пришел мне на помощь."

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/vin_hmm.ogg"
    show vin-arm-talk-small at vin_pos_2 with Dissolve(0.2)
    vin "\"Хмм... {w=0.5}действительно? {w=0.5}Как любопытно.\""

    vin "\"Раз так, {w=0.5}то почему бы не выбрать для Вас новое имя, {w=0.5}мадам?\""

    hide vin-arm-talk-small with Dissolve(0.2)

    noname "Полагаю, он прав. {w=0.5}Лучше уж иметь временное имя, чем ничего."

    window hide

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False

    $ renpy.pause(0.5, hard='True')

    window show

    noname "Итак, {w=0.5}какое же имя мне выбрать?"

label enter_name:

    python:
        name = renpy.input(_("Введите имя: "), pixel_width = 140)
        name = name.strip()

        if not name:
            name = _("Валерия")


    if name.lower().replace(" ", "") == _("迪诺") or name.lower().replace(" ", "") == _("dino") or name.lower().replace(" ", "") == _("дино") or name.lower().replace(" ", "") == _("dino999z") or name.lower().replace(" ", "") == _("吴德者"):
        noname "Дино: {w=0.5}Прекращай дурачиться."
        jump enter_name


    if name.lower().replace(" ", "") == _("文森") or name.lower().replace(" ", "") == _("埃奇沃思") or name.lower().replace(" ", "") == _("винсент") or name.lower().replace(" ", "") == _("эджворт") or name.lower().replace(" ", "") == _("vincent") or name.lower().replace(" ", "") == _("edgeworth"):
        show vin-arm-angry-small at vin_pos_2 with Dissolve(0.2)
        $ renpy.music.set_volume(0.6, delay=0, channel='sound')
        play sound "music/vin_hmm.ogg"
        noname "...Винсент, {w=0.5}кажется, {w=0.5}не очень этому рад."
        hide vin-arm-angry-small with Dissolve(0.2)
        jump enter_name


    if name.lower().replace(" ", "") == _("维克多") or name.lower().replace(" ", "") == _("布莱克") or name.lower().replace(" ", "") == _("виктор") or name.lower().replace(" ", "") == _("блэйк") or name.lower().replace(" ", "") == _("victor") or name.lower().replace(" ", "") == _("blake"):
        $ renpy.music.set_volume(0.8, delay=0, channel='sound')
        play sound "music/huh.ogg"
        show vic-talk-small-flip at vic_pos_2 with Dissolve(0.2)
        vic "\"Хаха. {w=0.5}Кажется, {w=0.5}я успел тебе понравиться, {w=0.5}да?\""
        hide vic-talk-small-flip at vic_pos_2 with Dissolve(0.2)
        jump enter_name


    if name.lower().replace(" ", "") == _("温斯顿") or name.lower().replace(" ", "") == _("winston") or name.lower().replace(" ", "") == _("уинстон") or name.lower().replace(" ", "") == _("винстон"):
        label name_sus:
            noname "Дино: {w=0.5}...Твой выбор вызывает большие подозрения."
            jump enter_name


    if name.lower().replace(" ", "") == _("佐莫娜") or name.lower().replace(" ", "") == _("zalmona") or name.lower().replace(" ", "") == _("залмона"):
        noname "Дино: {w=0.5}Должен признаться, {w=0.5}твой выбор довольно специфичный. {w=0.5}Настолько, {w=0.5}что вызывает подозрения."
        jump enter_name


    if name.lower().replace(" ", "") == _("德拉克") or name.lower().replace(" ", "") == _("draco") or name.lower().replace(" ", "") == _("драко"):
        show vin-arm-angry-small at vin_pos_2 with Dissolve(0.2)
        noname "...Винсент бросил в мою сторону подозрительный взгляд, {w=0.5}как будто я узнала о чем-то, {w=0.5}чего не должна была знать."
        hide vin-arm-angry-small with Dissolve(0.2)
        jump enter_name


    if name.lower().replace(" ", "") == _("埃曼诺") or name.lower().replace(" ", "") == _("emanon") or name.lower().replace(" ", "") == _("эманон"):
        show vin-arm-angry-small at vin_pos_2 with Dissolve(0.2)
        noname "...Винсент бросил в мою сторону подозрительный взгляд, {w=0.5}как будто я узнала о чем-то, {w=0.5}чего не должна была знать."
        hide vin-arm-angry-small with Dissolve(0.2)
        jump enter_name


    if name.lower().replace(" ", "") == _("艾尔博特") or name.lower().replace(" ", "") == _("albert") or name.lower().replace(" ", "") == _("альберт") or name.lower().replace(" ", "") == _("krueger") or name.lower().replace(" ", "") == _("крюгер") or name.lower().replace(" ", "") == _("克鲁格"):
        show vin-arm-angry-small at vin_pos_2 with Dissolve(0.2)
        $ renpy.music.set_volume(0.6, delay=0, channel='sound')
        play sound "music/vin_hmm.ogg"
        noname "...Винсент, {w=0.5}похоже, {w=0.5}не очень обрадовался этому, {w=0.5}но не сделал никаких комментариев."
        hide vin-arm-angry-small with Dissolve(0.2)


    if name.lower().replace(" ", "") == _("克洛德") or name.lower().replace(" ", "") == _("claude") or name.lower().replace(" ", "") == _("клод"):
        noname "Дино: {w=0.5}Что, простите?"
        jump enter_name


    if name.lower().replace(" ", "") == _("薇诺拉") or  name.lower().replace(" ", "") == _("vanora") or  name.lower().replace(" ", "") == _("ванора"):
        noname "Дино: {w=0.5}...Твой выбор вызывает большие подозрения."
        jump enter_name


    if name.lower().replace(" ", "") == _("梅尔斯") or name.lower().replace(" ", "") == _("myers") or name.lower().replace(" ", "") == _("майерс") or name.lower().replace(" ", "") == _("m先生"):
        show vin-arm-angry-small at vin_pos_2 with Dissolve(0.2)
        noname "...Винсент бросил в мою сторону подозрительный взгляд, {w=0.5}как будто я узнала о чем-то, {w=0.5}чего не должна была знать."
        hide vin-arm-angry-small with Dissolve(0.2)
        jump enter_name

    menu:
        van "Может, мне назваться [name!t]?"
        "Да":
            jump finish_name
        "Нет":
            jump enter_name

label finish_name:

    $ renpy.block_rollback()

    window show

    van "[name!t]. {w=0.5}Пожалуйста, зовите меня [name!t]."

    $ _skipping = True

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/Amazing.ogg"

    show vin-arm-talk-small at vin_pos_2 with Dissolve(0.2)
    stop music fadeout 6.0
    vin "\"[name!t]? {w=0.5}Замечательно. {w=0.5}Я очень рад познакомиться с вами, {w=0.5}[name!t].\""

    vin "\"Вы сейчас в затруднительном положении, {w=0.5}и я предполагаю, {w=0.5}что у Вас накопилось немало вопросов.\""

    vin "\"Может быть я смогу чем-то помочь Вам?\""

    hide vin-arm-talk-small with Dissolve(0.2)

    van "Винсент может знать ценную информацию, {w=0.5}которая поможет мне восстановить память. {w=0.5}Что же мне у него спросить?"

    window hide

    $ renpy.music.set_volume(0.8, delay=0, channel='music')
    play music "music/jazz.ogg"

    $ ask_vin_q1 = False
    $ ask_vin_q2 = False

label ask_vincent:

    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    menu:
        "Как я здесь оказалась?":
            $ ask_vin_q1 = True
            jump ask_how_get_here

        "Что это был за монстр?" if ask_vin_q1  == True:
            $ ask_vin_q2 = True
            jump ask_vin_robot_1

        "Было ли у меня что-нибудь с собой?" if ask_vin_q2  == True:
            jump ask_brought_items

label ask_how_get_here:

    window show
    van "\"Мистер Эджворт, {w=0.5}скажите, пожалуйста, {w=0.5}как я здесь оказалась?\""

    show vin-arm-talk-small at vin_pos_2 with Dissolve(0.2)

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/Vincent.ogg"
    vin "\"Как Вы здесь оказались? {w=0.5}[name!t], {w=0.5}к моему сожалению, я тоже не знаю.\""

    window hide

    $ renpy.pause(0.1, hard='True')

    show black
    $ renpy.transition(Fade(.2, 0, 0.25, color="#fff"))
    $ renpy.pause(0.5, hard='True')

    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/knock.ogg"

    pause 1.0

    $ renpy.pause(0.1, hard='True')

    show lobby_draco_pop
    $ renpy.transition(Dissolve(0.2))
    $ renpy.pause(1.0, hard='True')

    window hide
    vin "\"Дело в том, что {w=0.5}{color=#f00}мой дворецкий{/color} вчера вечером услышал странный стук в дверь.\""

    hide lobby_draco_pop
    $ renpy.transition(Dissolve(0.2))
    $ renpy.pause(1.0, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/open door.ogg" fadeout 1.0

    pause 1.0

    $ renpy.pause(0.1, hard='True')

    show van-faint-small
    hide lobby_draco_pop
    $ renpy.transition(Dissolve(0.2))
    $ renpy.pause(1.0, hard='True')
    vin "\"Когда он открыл ее, {w=0.5}то увидел Вас, {w=0.5}лежащую на крыльце. {w=0.5}{color=#f00}Без сознания{/color}.\""

    hide van-faint-small
    hide black
    $ renpy.transition(Fade(.4, 0, 0.25, color="#fff"))
    $ renpy.pause(1.0, hard='True')

    window show
    vin "\"Поскольку мы ничего не знали ни о Вас, {w=0.5}ни о том, с какой целью Вы прибыли, {w=0.5}мы решили на время разместить Вас в комнате для гостей.\""

    hide vin-arm-talk-small with Dissolve(0.2)

    van "......"

    van "Сказанное Винсентом заставило меня глубоко задуматься."

    van "Зачем я могла приехать в его особняк?"

    window hide

    jump ask_vincent

label ask_vin_robot_1:

    window show

    van "\"Ранее сегодня я увидела некое существо, {w=0.5}которого никогда раньше не видела.\""

    van "\"Нечто похожее на... {w=0.5}получеловека-полуробота.\""

    van "\"Что это вообще было?\""

    show vin-arm-talk-small at vin_pos_2 with Dissolve(0.2)

    $ renpy.music.set_volume(0.3, delay=0, channel='sound')
    play sound "music/vin_hmm.ogg"

    vin "\"О, дорогая [name!t]. {w=0.5}Похоже, что Вы уже повстречали одного из моих друзей.\""

    vin "\"Но, {w=0.5}пожалуйста, {w=0.5}пообещайте мне, {w=0.5}что не станете давать им дополнительную пищу, {w=0.5}когда в этом нет необходимости.\""

    hide vin-arm-talk-small with Dissolve(0.2)

    van "...Дополнительная пища? {w=0.5}Это он обо мне?"

    window hide

    jump ask_vincent

label ask_brought_items:

    window show

    van "\"У меня было что-нибудь с собой, когда я сюда попала?\""

    $ renpy.music.set_volume(0.3, delay=0, channel='sound')
    play sound "music/vin_hmm.ogg"

    show vin-arm-talk-small at vin_pos_2 with Dissolve(0.2)

    vin "\"Хм... {w=0.5}Раз уж мы заговорили об этом, {w=0.5}мы нашли вот эту вещь {color=#f00}в Вашем кармане{/color}.\""

    hide vin-arm-talk-small with Dissolve(0.2)

    van "Он протянул мне визитную карточку."

    window hide

    $ renpy.music.set_volume(0.1, delay=0, channel='sound')
    play sound "music/cloth.mp3" fadeout 2.0

    $ renpy.pause(0.1, hard='True')

    show hand_over_card_bg
    show hand_over_card onlayer inyourface:
        xalign 0.5 yalign 0.5
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    pause 1.0

    van "По большей части визитку было не разглядеть, {w=0.5}за исключением огромного {color=#f00}логотипа в виде буквы «М»{/color}."

    hide hand_over_card_bg
    hide hand_over_card onlayer inyourface
    with Dissolve(0.5)

    window show

    van "\"Корпорация Майерс?\" {w=0.5}Я задумалась, {w=0.5}где я могла слышать это название."

    van "Почему у меня были визитная карточка кого-то, кто там работает?"

    pause 0.5

    van "\"Что это за Корпорация Майерс?\" {w=0.5}Спросила я, подняв голову."

    pause 0.3

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/hmm.ogg"
    show vic-talk-small-flip at vic_pos_2 with Dissolve(0.2)

    vic "\"Корпорация Майерс - {w=0.5}ведущая машиностроительная компания, {w=0.5}расположенная в районе G4.\" {w=0.5}Сказал Виктор."

    vic "\"Кроме того, {w=0.5}это первая компания, {w=0.5}которая смогла разработать высокоподвижные механические протезы.\""

    vic "\"Но, к сожалению, {w=0.5}эта компания была вынуждена объявить о банкротстве из-за {color=#f00}чудовищного инцидента,{/color} {w=0.5}произошедшего {color=#f00}пять лет назад{/color}.\""

    hide vic-talk-small-flip with Dissolve(0.2)

    van "\"Чудовищного инцидента?\""

    show vin-dark-small at vin_pos_2 with Dissolve(0.2)
    stop music fadeout 6.0
    $ renpy.music.set_volume(0.3, delay=0, channel='sound')
    play sound "music/vin_hmm.ogg"
    vin "\"Инцидент киборга G4.\""

    van "Винсент выглядел недовольным одним лишь упоминанием об этом."

    van "\"Инцидент киборга G4? {w=0.5}Что тогда случилось?\""

    show vic-low-brow-small-flip at vic_pos_2 with Dissolve(0.2)

    van "Винсент и Виктор на мгновение замолчали, {w=0.5}словно раздумывая, {w=0.5}стоит ли мне вообще знать об этом событии. "

    show vic-talk-small-flip at vic_pos_2 with Dissolve(0.2)
    hide vic-low-brow-small-flip

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/hmm.ogg"

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music "music/creepy.wav"

    vic "\"В январе 2080 года за одну неделю таинственным образом пропало огромное количество граждан.\""

    van "Виктор наконец-то снова заговорил."

    window hide

    show black
    $ renpy.transition(Fade(.2, 0, 0.25, color="#fff"))
    $ renpy.pause(0.5, hard='True')

    show missing_1 with Dissolve(0.5)
    $ renpy.pause(0.5, hard='True')

    window show

    $ say_who = _("Виктор")

    vic "\"Они исчезли безо всякого следа, {w=0.5}как будто растворившись в воздухе.\""

    show missing_2 with Dissolve(0.5)
    hide missing_1
    vic "\"Ни завещаний, {w=0.5}ни трупов, {w=0.5}ни пятен крови. {w=0.5}Ничего не осталось.\""

    show missing_3 with Dissolve(0.5)
    hide missing_2
    vic "\"Но у этих людей было кое-что общее: {w=0.5}все они в последний раз были замечены в {color=#f00}районе G4{/color}.\""

    show missing_4 with Dissolve(0.5)
    hide missing_3
    vic "\"И кто обладает такой властью, {w=0.5}чтобы заставить сотни граждан исчезнуть за одну неделю?\""

    show myers_small with Dissolve(0.5)
    hide missing_4
    vic "\"Естественно, {w=0.5}полиция заподозрила Корпорацию Майерс, {w=0.5}крупнейшую международную монополию, {w=0.5}расположенную в районе G4.\""

    vic "\"Тем не менее, {w=0.5}Корпорация Майерс отрицала какую-либо причастность к этому делу.\""

    show chamber_1 with Dissolve(0.5)
    hide myers_small
    vic "\"Спустя год расследования полиция неожиданно обнаружила {color=#f00}секретное помещение, {w=0.5}расположенное в подвале корпорации{/color}.\""

    show chamber_2 with Dissolve(0.5)
    hide chamber_1
    vic "\"Внутри этой комнаты... {w=0.5}{color=#f00}Находилась группа киборгов{/color}.\""

    van "(Киборгов? {w=0.5}Не с таким ли существом я столкнулась ранее...?)"

    vic "\"Вполне логично было бы предположить, {w=0.5}что эти киборги и были пропавшими гражданами.\""

    vic "\"Но правда оказалась еще ужаснее.\""

    window hide

    show chamber_3
    show blood-2
    $ renpy.transition(Fade(.25, 0, 0.25, color="#fff"))
    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/scream.ogg"
    $ renpy.pause(0.1, hard='True')
    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=30))
    $ renpy.pause(1.0, hard='True')
    hide chamber_2

    window show

    vic "\"В действительности эти пропавшие граждане были использованы в качестве {color=#f00}корма{/color} для киборгов.\""

    hide blood-2
    hide chamber_3
    with Dissolve(0.25)

    vic "\"Что касается того, {w=0.5}откуда появились сами киборги... {p=0.5}{color=#f00}Никто точно не знал{/color}.\""

    show court_1 with Dissolve(0.5)
    vic "\"Но даже в свете этих подробностей корпорация по-прежнему отрицала то, {w=0.5}что когда-либо давала разрешение на проведение столь бесчеловечного эксперимента.\""

    show court_2 with Dissolve(0.5)
    hide court_1
    vic "\"Благодаря помощи {color=#f00}адвоката{/color} был осужден один невиновный сотрудник.\""

    show winston_1 with Dissolve(0.5)
    hide court_2
    vic "\"Он был приговорен к пожизненному заключению без права на досрочное освобождение, {w=0.5}в то время как с самой компании были сняты все обвинения.\""
    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ["<silence .25>", "music/prison.ogg"]
    show winston_2 at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=30) with wipeDown
    $ renpy.pause(0.1, hard='True')
    hide winston_1
    hide winston_2
    with Dissolve(0.5)
    vic "\"Однако на этом история не закончилась.\""

    show car with Dissolve(0.5)
    vic "\"Два месяца спустя адвокат получил серьезные травмы в {color=#f00}автомобильной аварии{/color} и чуть не погиб.\""
    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ["music/car crash.ogg"]
    hide car with Fade(.25, 0, 0.25, color="#fff")

    vic "\"В течение того же года {color=#f00}все ведущие сотрудники Корпорации Майерс были найдены зверски убитыми{/color}.\""

    $ renpy.pause(0.1, hard='True')
    show blood_stain with Dissolve(1.0)
    vic "\"Преступник, {w=0.5}стоящий за всем этим, {w=0.5}так никогда и не был найден.\""

    hide blood_stain with Dissolve(0.5)
    pause 0.5
    $ renpy.pause(0.1, hard='True')
    show g4_street with Dissolve(0.5)

    pause 0.5

    vic "\"И до сих пор в районе G4 таинственным образом исчезают люди.\""

    pause 0.3

    stop music fadeout 8.0
    vic "\"Ходят слухи, {w=0.5}что духи жертв эксперимента все еще бродят по улицам, {w=0.5}забирая жизни тех несчастных, {w=0.5}кто столкнулся с ними...\""

    $ say_who = ""

    hide g4_street
    hide blood_stain
    hide black
    $ renpy.transition(Dissolve(1.5))
    $ renpy.pause(1.5, hard='True')

    hide vic-talk-small-flip with Dissolve(0.5)

    window show

    van "......"

    van "От рассказа Виктора у меня по спине побежали мурашки."

    van "Я совершенно не ожидала такой пугающей городской легенды от района G4."

    van "\"Виктор, {w=0.5}могу я поинтересоваться, {w=0.5}откуда ты все это знаешь?\""

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/hmm.ogg"
    show vic-talk-small-flip at vic_pos_2 with Dissolve(0.2)

    pause 0.2

    vic "\"Ответ на твой вопрос довольно прост,\" {w=0.3}Рассмеялся Виктор."

    vic "{color=#f00}\"Мы с Винсентом оба в прошлом были сотрудниками Корпорации Майерс.\"{/color}"

    hide vic-talk-small-flip

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/shock2.ogg" fadeout 2.0
    van "!?" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    pause 0.5

    $ renpy.music.set_volume(0.3, delay=0, channel='sound')
    play sound "music/vin_hmm.ogg"
    $ renpy.music.set_volume(0.8, delay=0, channel='music')
    play music ["<silence 4.0>", "music/jazz.ogg"]
    queue music "music/jazz.ogg"
    show vin-satire-small at vin_pos_2 with Dissolve(0.2)
    hide vin-dark-small

    vin "\"Виктор, {w=0.5}должен сказать, я впечатлен, {w=0.5}насколько подробно ты сохранил историю в памяти.\" {w=0.5}Язвительно произнес Винсент."
    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/cough.ogg" fadeout 2.0
    show vic-low-talk-small-flip at vic_pos_2 with Dissolve(0.2)
    vic "\"Кхм, {w=0.5}кхм, кхм...\""

    van "Виктор прокашлялся."


    show vic-unhappy-small-flip:
        yoffset 20 xoffset -320
        ease 0.2 yoffset 0
    show vic-low-talk-small-flip:
        alpha 0
    show vic-normal-small-flip:
        alpha 0

    van "Он бросил взгляд на настенные часы и, {w=0.5}судя по всему, {w=0.5}забеспокоился насчет времени."

    show vic-low-talk-small-flip:
        alpha 1
    hide vic-unhappy-small-flip with Dissolve(0.2)

    vic "\"Что ж, {w=0.5}время для историй закончилось. {w=0.5}Сейчас я вынужден с вами попрощаться.\""

    vic "\"Винсент, {w=0.5}не хочешь ли выпить со мной в пабе завтра вечером? {w=0.7}И очень приятно было познакомиться с тобой, {w=0.5}моя дорогая [name!t].\""

    show vic-normal-small-flip:
        alpha 1
    hide vic-low-talk-small-flip with Dissolve(0.2)
    $ renpy.pause(0.01, hard=True)
    show vic-normal-small-flip:
        linear 0.3 xoffset -1000
    $ renpy.pause(1.0, hard=True)
    hide vic-normal-small-flip


    van "Виктор покинул особняк."

    window hide

    stop music fadeout 4.0

    $ renpy.pause(0.1, hard='True')
    scene black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(2.0, hard='True')

    van "После этого Винсент помог мне устроиться в гостевой комнате."

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/hallway door.ogg"

    pause 2.0

    van "Я поблагодарила его, {w=0.5}а затем вернулась в свою комнату, {w=0.5}чтобы немного отдохнуть."

    pause 2.0
    $ renpy.pause(1.0, hard='True')
    $ renpy.music.set_volume(0.6, delay=0, channel='music')
    play music "music/night.ogg" fadein 2.0 fadeout 6.0
    $ renpy.pause(0.1, hard='True')
    scene late-night-small
    show firefly_particles
    $ renpy.transition(Dissolve(2.0))
    $ renpy.pause(2.0, hard='True')

    $ renpy.pause(0.1, hard='True')
    pause 2.0

    window hide

    van "Было около полуночи, {w=0.5}когда я мирно лежала в своей кровати, {w=0.5}а мои мысли не унимались."

    van "Я продолжала думать о том, {w=0.5}что сказал мне Виктор-"

    van "Пропавшие граждане из G4, {w=0.5}киборги из секретной комнаты..."

    van "И таинственная {color=#f00}Корпорация Майерс{/color}."


    show hold_card_bg
    show hold_card onlayer inyourface:
        xalign 0.5 yalign 0.5
    show hold_card_2 onlayer inyourface:
        alpha 0 xalign 0.5 yalign 0.5
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard='True')

    van "Я достала из кармана карточку и внимательно рассмотрела ее при свете луны."

    van "Зачем я принесла эту визитку в особняк Винсента?"

    van "Какое отношение я имею к Корпорации Майерс? "

    van "......"

    van "Есть лишь одно место, {w=0.5}где я смогу выяснить это."

    window hide

    $ renpy.free_memory()

    stop music fadeout 3.0
    show hold_card_2_bg
    show hold_card_2 onlayer inyourface:
        ease 1.0 alpha 1 xalign 0.5 yalign 0.5
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')
    hide hold_card onlayer inyourface

    pause 3.0

    van "{color=#f00}Сама Корпорация Майерс.{/color}"

    hide hold_card_2 onlayer inyourface
    scene myers_1
    with Dissolve(1.0)

    pause 1.0

    jump myers_click
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
