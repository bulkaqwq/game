

image dino-logo:
    "images/dino logo/dino-logo.png"
    pause 2.0
    "images/dino logo/dino-logo-2.png"
    pause 0.1
    repeat


image video_play = "images/bad tv signal/play button.png"
image rec_circle:
    "images/bad tv signal/rec circle.png"
    0.5
    "images/empty.png"
    0.5
    repeat


image email_icon_no_check_mark = "images/email sent icon/email_sent_1.png"
image email_icon_animation:
    "images/email sent icon/email_sent_1.png"
    0.1
    "images/email sent icon/email_sent_2.png"
    0.1
    "images/email sent icon/email_sent_3.png"
    0.1
    "images/email sent icon/email_sent_4.png"
    0.1
    "images/email sent icon/email_sent_5.png"
    0.1
    "images/email sent icon/email_sent_6.png"


image bad_signal_computer_desktop = "images/bad tv signal/bad_signal_background.png"
image bad_signal_computer_email = "images/Main Title/email.png"
image bad_signal_computer_email_background = "images/Main Title/email_background.png"
image bad_signal_computer_email_text = "images/Main Title/email_text.png"
image bad_signal_enter_box = "images/Main Title/enter box.png"
image bad_tv_signal:
    contains:
        "images/bad tv signal/bad_signal_layer_1.png"
    contains:
        "images/bad tv signal/bad_signal_layer_2.png"
        yoffset -1000 alpha 0.5
        linear 9.0 yoffset 0 alpha 0.5
        repeat
    contains:
        "images/transparent dark-small.png"
        alpha 0
        pause 3.0
        alpha 0.15
        pause 0.2
        alpha 0.3
        pause 0.05
        alpha 0.3
        pause 0.5
        alpha 0.15
        pause 0.35
        alpha 0.1
        pause 0.05
        alpha 0.2
        pause 1.0
        repeat
    contains:
        "images/bad tv signal/bad_signal_layer_3.png"
        alpha 0.3

image warning_text = "images/Main Title/warning text.png"
image warning_top = "images/Main Title/warning top.png"
image warning_bottom = "images/Main Title/warning bottom.png"
image key_text = "images/Main Title/key help.png"
image key_text_distorted_1 = "images/Main Title/key help distorted_1.png"
image key_text_distorted_2 = "images/Main Title/key help distorted_2.png"
image main_title_myers_corporation = "images/Main Title Myers.png"
image main_title_myers_corporation_2 = "images/Main Title Myers-2.png"
image main_title_text = "images/Main Title/Main Title Text.png"
image main_title_vanora = "images/Main Title/Main Title Vanora.png"
image main_title_vincent = "images/Main Title/Main Title Vincent.png"
image main_title_click_to_start = "images/Main Title/click to start.png"
image main_title_overlay = "gui/overlay/main_menu.png"
image main_title_door = "images/Main Title/main title door.png"
image main_title_door_2 = "images/Main Title/main title door 2.png"


image vincent-shadow-small = "images/Vin Proto/vincent-shadow-small.png"
image vincent-shadow-smile-small = "images/Vin Proto/vincent-shadow-smile-small.png"
image distorted-vincent-shadow = "images/Vin Proto/distorted vin proto.png"
image distorted-vincent-shadow-2 = "images/Vin Proto/distorted vin proto 2.png"
image proto_no_signal_og = "images/Vin Proto/no signal og.png"
image proto_no_signal = "images/Vin Proto/no signal.png"
image proto_laptop = "images/Vin Proto/proto laptop.png"
image proto_lamp:
    "images/Vin Proto/proto lamp.png"
    alpha 0.5
    block:
        pause 2.5
        alpha 0.3
        linear 1.0 alpha 0.5
        repeat
image proto_m_hand = "images/Vin Proto/proto m hand.png"
image proto_no_signal_distorted:
    "proto_no_signal"
    pause 1.0
    "images/Vin Proto/no signal distorted-1.png"
    pause 0.1
    "proto_no_signal"
    pause 1.0
    "images/Vin Proto/no signal distorted-2.png"
    pause 0.1
    "proto_no_signal"
    pause 1.0
    "images/Vin Proto/no signal distorted-1.png"
    pause 0.1
    "images/Vin Proto/no signal distorted-2.png"
    pause 0.1
    repeat

image main_title_shadow:

    "images/Main Title/Main Title Shadow-2.png"
    pause 0.02
    "images/Main Title/Main Title Shadow-1.png"
    pause 0.02
    repeat

image main_title_click_to_start_animation:

    "images/empty-screen-small.png" with Dissolve(0.7)
    pause 1.0
    "images/Main Title/click to start.png" with Dissolve(0.7)
    pause 1.0
    repeat

image main_title_myers_puppeteer_animation:

    "images/Main Title/Main Title Myers-1-end.png"
    pause 0.2
    "images/Main Title/Main Title Myers-2-end.png"
    pause 0.2
    "images/Main Title/Main Title Myers-3-end.png"
    pause 0.39470199
    "images/Main Title/Main Title Myers-3-end.png"
    pause 0.2
    "images/Main Title/Main Title Myers-2-end.png"
    pause 0.2
    "images/Main Title/Main Title Myers-1-end.png"
    pause 0.39470199
    repeat

image missing_particles:
    contains:
        SnowBlossom("images/Main Title/Particles_1.png", count=10, border=100, xspeed=(-20, 20), yspeed=(10, 50), start=0, fast=False, horizontal=True)
    contains:
        SnowBlossom("images/Main Title/Particles_2.png", count=10, border=100, xspeed=(-20, 20), yspeed=(30, 50), start=3, fast=False, horizontal=True)
    contains:
        SnowBlossom("images/Main Title/Particles_3.png", count=3, border=500, xspeed=(-20, 20), yspeed=(20, 50), start=0, fast=False, horizontal=True)
    contains:
        SnowBlossom("images/Main Title/Particles_4.png", count=10, border=200, xspeed=(-20, 20), yspeed=(30, 50), start=3, fast=False, horizontal=True)
    contains:
        SnowBlossom("images/Main Title/Particles_5.png", count=10, border=300, xspeed=(-20, 20), yspeed=(20, 50), start=0, fast=False, horizontal=True)
    contains:
        SnowBlossom("images/Main Title/Particles_6.png", count=10, border=300, xspeed=(-20, 20), yspeed=(20, 50), start=0, fast=False, horizontal=True)
    contains:
        SnowBlossom("images/Main Title/Particles_1.png", count=2, border=100, xspeed=(-20, 20), yspeed=(10, 50), start=0, fast=False, horizontal=False)
    contains:
        SnowBlossom("images/Main Title/Particles_2.png", count=2, border=100, xspeed=(-20, 20), yspeed=(30, 50), start=3, fast=False, horizontal=False)
    contains:
        SnowBlossom("images/Main Title/Particles_3.png", count=2, border=500, xspeed=(-20, 20), yspeed=(20, 50), start=0, fast=False, horizontal=False)
    contains:
        SnowBlossom("images/Main Title/Particles_4.png", count=3, border=200, xspeed=(-20, 20), yspeed=(30, 50), start=3, fast=False, horizontal=False)
    contains:
        SnowBlossom("images/Main Title/Particles_5.png", count=3, border=300, xspeed=(-20, 20), yspeed=(20, 50), start=0, fast=False, horizontal=False)
label splashscreen:

    python:
        _preferences.set_volume('music', 1.0)
        _preferences.set_volume('sfx', 1.0)
        _preferences.set_volume('voice', 1.0)

    stop music

    scene dino game-small
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')
    with Pause(1)
    $ renpy.pause(0.1, hard='True')
    pause 1.8
    $ renpy.pause(0.1, hard='True')
    scene black
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(2.0, hard='True')

    jump donation_start

label main_menu_start:

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music "music/Creepy-Action.ogg"

    show main_title_shadow

    $ renpy.pause(0.1, hard='True')
    show missing_particles
    show main_title_door behind main_title_shadow:
        xalign 0.5 yalign 0.5 zoom 2.0
        ease 0.5 zoom 1.0
    show main_title_myers_corporation behind main_title_shadow:
        xalign 0.5 yalign 0.5 zoom 2.0
        ease 0.5 zoom 1.0
    $ renpy.transition(Dissolve(0.9))

    $ renpy.pause(2.9725099, hard='True')

    show main_title_myers_puppeteer_animation behind missing_particles
    $ renpy.transition(Dissolve(1.0))

    $ renpy.pause(2.0, hard='True')

    show main_title_vanora:
        xoffset 550 yoffset 0
        ease 0.5 zoom 1.0 xoffset -250 yoffset 0

    show main_title_vincent:
        xoffset -1050 yoffset 0
        ease 0.5 zoom 1.0 xoffset -250 yoffset 0

    $ renpy.transition(Dissolve(0.5))

    $ renpy.pause(1.0, hard='True')

    show main_title_text
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(1.0, hard='True')

    show main_title_click_to_start_animation

    $ renpy.pause(1.5, hard='True')

    call screen Main_Title_1

    return

screen Main_Title_1:

    add "images/empty-screen-small.png" xalign 0.5 yalign 0.0

    imagebutton:
        idle "images/empty-screen-small.png"
        action Jump("switch_to_main_title_2")


label switch_to_main_title_2:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound1')
    $ renpy.music.play("music/Click To Start.ogg", channel="sound1", loop = False)

    hide main_title_text
    $ renpy.transition(Dissolve(0.3))

    hide main_title_click_to_start_animation
    $ renpy.transition(Dissolve(0.3))
    $ renpy.pause(0.3, hard='True')

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/Main Title Evil Laugh.ogg"

    show main_title_vincent:
        pause 1.5
        ease 0.5 zoom 1.0 xoffset -1150 yoffset 0

    show main_title_vanora:
        pause 1.5
        ease 0.5 zoom 1.0 xoffset 550 yoffset 0

    with None

    hide missing_particles
    $ renpy.transition(Dissolve(2.0))

    $ renpy.pause(3.0, hard='True')

    hide main_title_myers_puppeteer_animation
    $ renpy.transition(Dissolve(2.0))
    $ renpy.pause(2.0, hard='True')

    $ renpy.pause(1.0, hard='True')

    show main_title_overlay:
        xoffset -800 yoffset 0
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    show main_title_myers_corporation:
        ease 0.5 zoom 1.0 xoffset 120 yoffset 0

    show main_title_door:
        ease 0.5 zoom 1.0 xoffset 120 yoffset 0

    $ renpy.pause(0.5, hard='True')

    return


init python:

    import time


screen countdown(timer_range, timer_jump):
    default end_time = time.time() + timer_range
    default current_time = time.time()
    timer 0.05 repeat True action If(
        current_time < end_time,
        true=SetScreenVariable('current_time', time.time()),
        false=[Hide('countdown'), Jump(timer_jump)]
    )

    bar value (end_time-current_time)*100 range timer_range*100 xalign 0.5 yalign 0.9 xmaximum 300 at notify_appear


screen email_countdown(timer_range, variable_):
    default end_time = time.time() + timer_range
    default current_time = time.time()
    timer 0.05 repeat True action If(
        current_time < end_time,
        true=SetScreenVariable('current_time', time.time()),
        false=[Hide('email_countdown'), Show('click_email_screen_poto')]
    )

init:
    $ config.keymap['self_voicing'].remove('v')
    $ config.keymap['self_voicing'].remove('V')
    $ config.keymap['hide_windows'].remove('h')
    $ config.keymap['hide_windows'].remove('mouseup_2')
    $ config.keymap['clipboard_voicing'].remove('C')

    $ config.keymap['accessibility'].remove('K_a')
    $ config.keymap['toggle_skip'].remove('K_TAB')
    $ config.keymap['skip'].remove('K_LCTRL')
    $ config.keymap['skip'].remove('K_RCTRL')
    $ config.keymap['fast_skip'].remove('>')
    $ config.keymap['stop_skipping'].append('keyup_K_LCTRL')
    $ config.keymap['stop_skipping'].append('keyup_K_RCTRL')

screen warning_click_to_continue:

    imagebutton:
        idle "images/empty-screen-small.png"
        action Jump("click_thru_warning")

screen help_click_to_continue:

    imagebutton:
        idle "images/empty-screen-small.png"
        action Jump("click_thru_help")

label start:


    show screen keymap_accessibility

    scene black

    $ quick_menu = False

    stop music fadeout 6.0

    show main_title_door:
        zoom 1.0 xoffset -139 yoffset 0

    show main_title_myers_corporation:
        zoom 1.0 xoffset -139 yoffset 0

    show main_title_overlay:
        zoom 1.0 xoffset 0 yoffset 0

    show main_title_shadow

    $ renpy.pause(0.1, hard=True)

    show main_title_door:
        ease 0.5 zoom 1.0 xoffset -260 yoffset 0

    show main_title_myers_corporation:
        ease 0.5 zoom 1.0 xoffset -260 yoffset 0

    show main_title_overlay:
        ease 0.5 zoom 1.0 xoffset -800 yoffset 0

    $ renpy.pause(1.0, hard=True)

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/flashback.ogg")

    $ renpy.music.set_volume(1.0, delay=0, channel='main_title_gate')
    $ renpy.music.play("music/myers gate open .ogg", channel="main_title_gate", loop=False)

    show main_title_door:
        linear 0.5 yoffset 6
        linear 2.5 yoffset -100

    show main_title_door_2 behind main_title_myers_corporation:
        alpha 0 xalign 0.5
        linear 0.5 yoffset 6 alpha 0
        linear 2.5 yoffset -100 alpha 1

    show main_title_myers_corporation_2:
        alpha 0 xalign 0.5
        linear 4.0 alpha 1 xalign 0.5

    $ renpy.pause(4.2, hard=True)

    hide main_title_door
    hide main_title_door_2
    hide main_title_myers_corporation
    show main_title_myers_corporation_2:
        ease 0.5 zoom 20.0 xoffset -50 yoffset -9500

    $ renpy.pause(0.5, hard=True)


    if select_chapter == True:
        $ select_chapter = False
        $ quick_menu = True
        jump chapter_select_prep

    $ renpy.free_memory()


    scene black
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(2.0, hard='True')
    pause 1.0

    $ renpy.music.set_volume(0.8, delay=0, channel='vhs')
    $ renpy.music.play("music/vhs tape.ogg", channel="vhs", loop=False)
    $ renpy.music.queue("music/vhs tape 2.ogg", channel='vhs', loop=True)

    $ renpy.pause(0.1, hard='True')
    show bad_signal_computer_desktop
    show bad_tv_signal onlayer tvsignal
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(2.0, hard='True')

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ _rollback = False


    $ _history = False


    $ renpy.pause(0.1, hard='True')
    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/misc_menu.wav"
    show warning_text:
        zoom 0.01
        linear 0.2 zoom 1.0
    $ renpy.pause(1.0, hard='True')

    window hide
    noname_warning_1 "ЭТА ИГРА СОДЕРЖИТ ПУГАЮЩИЕ И ЯРКИЕ ИЗОБРАЖЕНИЯ, А ТАКЖЕ ДРУГИЕ ЭЛЕМЕНТЫ ХОРРОРА. {w=0.5}ПОЖАЛУЙСТА, ВОЗДЕРЖИТЕСЬ ОТ ПРОХОЖДЕНИЯ ДАННОЙ ИГРЫ, ЕСЛИ ВЫ СЧИТАЕТЕ, ЧТО ОНА МОЖЕТ КАКИМ-ЛИБО ОБРАЗОМ ОТРАЗИТЬСЯ НА ВАШЕМ СОСТОЯНИИ."

label click_thru_warning:


    $ checked_proto_email = False

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/misc_menu.wav"

    show warning_top
    show warning_bottom
    hide warning_text


    $ renpy.pause(0.1, hard='True')
    show warning_top:
        linear 0.5 yoffset -100
    show warning_bottom:
        linear 0.5 yoffset 100

    $ renpy.pause(0.2, hard='True')

    $ bool_email_showed_up = False
    show screen email_countdown(7.0, bool_email_showed_up)

    play sound [ "<silence 6.5>", "music/email.ogg" ]

    show bad_signal_computer_email:
        yoffset 190
        6.5
        linear 0.5 yoffset 0

    image proto_email_text_1 = Text(_("{font=VHS.TTF}{size=+1}{/size}{/font}"))
    image proto_email_text_2 = Text(_("{font=VHS.TTF}{size=-6}{u}{/u}{/size}{/font}"))

    show proto_email_text_1 onlayer tvsignal at Position(xpos = 1080, ypos = 767, xanchor = 0.5):
        6.5
        linear 0.5 yoffset -190
    show proto_email_text_2 onlayer tvsignal at Position(xpos = 1040, ypos = 837, xanchor = 0.5):
        6.5
        linear 0.5 yoffset -190

    noname_warning_2 "{u}ESC/ПРАВЫЙ КЛИК{/u}: МЕНЮ ИГРЫ\n {p=0.5}{u}ЛЕВЫЙ КЛИК/ENTER{/u}: ПРОДВИЖЕНИЕ ДИАЛОГА И АКТИВАЦИЯ ИНТЕРФЕЙСА\n {p=0.5}{u}SPACE{/u}: ПРОДВИЖЕНИЕ ДИАЛОГА БЕЗ ОСУЩЕСТВЛЕНИЯ ВЫБОРА\n {p=0.5}{u}КНОПКА S{/u}: СКРИНШОТЫ"

    jump proto_not_check_email

screen click_email_screen_poto:

    imagebutton:
        xpos 901
        ypos 535
        idle "images/Main Title/email-idle.png"
        hover "images/Main Title/email-hover.png"
        action Jump("show_proto_email")

label show_proto_email:


    $ checked_proto_email = True

    hide proto_email_text_1 onlayer tvsignal
    hide proto_email_text_2 onlayer tvsignal
    hide bad_signal_computer_email
    hide screen click_email_screen_poto

    $ renpy.pause(0.1, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/misc_menu.wav"

    show bad_signal_computer_email_background:
        zoom 0.2 xoffset 1000 yoffset 500
        linear 0.3 zoom 1.0 xoffset 70 yoffset 40

    $ renpy.pause(0.3, hard='True')

    show bad_signal_computer_email_text:
        xoffset 70 yoffset 40

    show text _ ("{font=VHS.TTF}НОВАЯ ГОЛОВНАЯ БОЛЬ{/size}") onlayer tvsignal at Position(xpos=650, ypos=180)

    $ renpy.pause(0.3, hard='True')

    noname_email "{size=-10}ДОРОГОЙ МЕСЬЕ М,{p=0.5}С ОГРОМНЫМ СОЖАЛЕНИЕМ ВЫНУЖДЕН СООБЩИТЬ \nВАМ, ЧТО МЫ СТОЛКНУЛИСЬ С НОВОЙ ПРОБЛЕМОЙ -{p=0.5}КАК МЫ И ПРЕДПОЛАГАЛИ, {p=0.5}{color=#f00}ТА ЖЕНЩИНА ЕЩЕ ЖИВА.{/color}{/size}"
    noname_email "{size=-10}И ТА {color=#f00}\"ВЕЩЬ\",{/color} ЧТО МЫ ТАК ДАВНО ИСКАЛИ, {p=0.5}У НЕЁ.{/size}"
    noname_email "{size=-10}ПОЖАЛУЙСТА, СООБЩИТЕ МНЕ, КАК ВЫ НАМЕРЕВАЕТЕСЬ \nДЕЙСТВОВАТЬ ДАЛЬШЕ.\n{p=0.5}С УВАЖЕНИЕМ,{p=0.5}{color=#f00}ПРЕСЛЕДОВАТЕЛЬ{/color}{/size}"

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/typing.ogg"

    extend "{size=-12}\n\n\n\n\n{/size}{size=-10}{color=#f00}СЕГОДНЯ В 10. {/color}{p=0.5}ВСТРЕЧАЕМСЯ В ТОМ ЖЕ МЕСТЕ, \nГДЕ И ВСЕГДА.{/size}"

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/return key.ogg"

    $ renpy.pause(0.3, hard='True')

    show email_icon_no_check_mark:
        parallel:
            rotate 90
            linear 0.3 rotate 0
        parallel:
            zoom 0.01 xalign 0.5 yalign 0.5
            linear 0.3 zoom 1.0

    $ renpy.pause(0.8, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/email sent.ogg"

    hide email_icon_no_check_mark
    show email_icon_animation:
        xalign 0.499 yalign 0.499

    noname_email_2 "{size=-5}\n\n\n\n\n{/size}СООБЩЕНИЕ ОТПРАВЛЕНО"

    hide email_icon_animation
    hide text onlayer tvsignal
    show email_icon_no_check_mark:
        parallel:
            rotate 0
            linear 0.3 rotate 90
        parallel:
            zoom 1.0 xalign 0.5 yalign 0.5
            linear 0.3 zoom 0.01

    hide bad_signal_computer_email_text

    show bad_signal_computer_email_background:
        zoom 1.0 xoffset 70 yoffset 40
        linear 0.3 zoom 0.2 xoffset 1000 yoffset 500

    $ renpy.pause(0.3, hard=True)

    hide bad_signal_computer_email_background

    noname_warning_2 "{u}ESC/RIGHT CLICK{/u}: МЕНЮ ИГРЫ\n {p=0.5}{u}LEFT CLICK/ENTER{/u}: ПРОДВИЖЕНИЕ ДИАЛОГА И АКТИВАЦИЯ ИНТЕРФЕЙСА\n {p=0.5}{u}SPACE{/u}: ПРОДВИЖЕНИЕ ДИАЛОГА БЕЗ ОСУЩЕСТВЛЕНИЯ ВЫБОРА\n {p=0.5}{u}S KEY{/u}: СКРИНШОТЫ{fast}"

    jump proto_check_email

label proto_not_check_email:

    hide screen click_email_screen_poto
    hide screen email_countdown

    hide text onlayer tvsignal
    show bad_signal_computer_email:
        linear 0.5 yoffset 190
    show proto_email_text_1 onlayer tvsignal:
        linear 0.5 yoffset 5
    show proto_email_text_2 onlayer tvsignal:
        linear 0.5 yoffset 5

label proto_check_email:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/misc_menu.wav"


    $ renpy.pause(0.1, hard=True)
    show warning_top:
        linear 0.5 yoffset 6
    show warning_bottom:
        linear 0.5 yoffset -6

    show key_text
    $ renpy.transition(PushMove(1.0, "pushright"))
    $ renpy.pause(1.0, hard=True)



    image instructions_screen_text:
        contains:
            Text(_("{font=VHS.TTF}{size=-10}НАЗАД{/size}{/font}"))
            xalign 0.5
            xpos 307 ypos 425
        contains:
            Text(_("{font=VHS.TTF}{size=-10}ЛОГ{/size}{/font}"))
            xalign 0.5
            xpos 415 ypos 425
        contains:
            Text(_("{font=VHS.TTF}{size=-10}ПРОПУСТИТЬ{/size}{/font}"))
            xalign 0.5
            xpos 532 ypos 425
        contains:
            Text(_("{font=VHS.TTF}{size=-10}АВТО{/size}{/font}"))
            xalign 0.5
            xpos 637 ypos 425
        contains:
            Text(_("{font=VHS.TTF}{size=-10}СОХР.{/size}{/font}"))
            xalign 0.5
            xpos 740 ypos 425
        contains:
            Text(_("{font=VHS.TTF}{size=-10}Б. СОХР.{/size}{/font}"))
            xalign 0.5
            xpos 850 ypos 425
        contains:
            Text(_("{font=VHS.TTF}{size=-10}НАСТРОЙКИ{/size}{/font}"))
            xalign 0.5
            xpos 964 ypos 425

    show instructions_screen_text
    $ renpy.transition(CropMove(0.5, "wiperight"))

    noname_warning_3 "{cps=*2}{size=-1}\n\n\n{/size}{alpha=0}lololololo{space=550}{/alpha}{/cps}"

    hide instructions_screen_text

    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/computer glitch.ogg"

    hide warning_top
    hide warning_bottom
    hide key_text
    show key_text_distorted_1
    show game_over_static:
        alpha 0
        linear 0.3 alpha 0.3
    $ renpy.pause(0.2, hard=True)
    show key_text_distorted_1
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.1, hard=True)
    show key_text_distorted_1
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.1, hard=True)
    hide key_text_distorted_1
    show key_text_distorted_2
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.1, hard=True)
    show key_text_distorted_2
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.1, hard=True)
    show key_text_distorted_2
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.1, hard=True)
    show key_text_distorted_2
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.1, hard=True)
    hide key_text_distorted_2
    hide game_over_static
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.1, hard=True)

    show bad_signal_enter_box:
        yoffset 5

    noname_enter "{size=+20}ИНИЦИАЛИЗАЦИЯ ЗАВЕРШЕНА.{p=0.5}ОЖИДАНИЕ КОМАНДЫ.{/size}{nw}"
    noname_enter_silent "{size=+20}ИНИЦИАЛИЗАЦИЯ ЗАВЕРШЕНА.{p=0.5}ОЖИДАНИЕ КОМАНДЫ.{/size}{fast}"
    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/typing2.ogg"
    extend "{size=-20}\n\n\n{/size}{size=+1}ПРИСТУПИТЬ К ВЫПОЛНЕНИЮ{/size}"

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/return key.ogg"
    hide bad_signal_enter_box

    default myClock = Clock(False, 3, 0, 150, True, False)
    $ myClock.runmode("real")

    screen clock_screen:
        add myClock:
            xalign 0.12
            yalign 0.85
        text _("{font=VHS.ttf}{size=+5}2086 ЯНВ 20-ОЕ{/size}{/font}") xalign 0.11 yalign 0.9
        text _("{font=VHS.ttf}{size=+5}PLAY{/size}{/font}") xalign 0.09 yalign 0.1
        add "video_play"
        add "rec_circle" yoffset 3
        text _("{font=VHS.ttf}{color=#f00}{size=+5}REC{/size}{/color}{/font}") xalign 0.91 yalign 0.1

    $ renpy.music.set_volume(0.8, delay=0, channel='vhs')
    $ renpy.music.play("music/insert vhs.ogg", channel="vhs", loop=False)

    show screen clock_screen
    $ renpy.transition(Dissolve(1.0))

    show game_over_static:
        alpha 0
        linear 0.3 alpha 0.3
        pause 2.0
        linear 5.0 alpha 0

    $ renpy.pause(1.0, hard=True)

    $ quick_menu = True
    $ _skipping = True


    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music "music/novel-protologue.ogg"

    $ renpy.pause(1.0, hard='True')

    hide bad_signal_computer_email
    hide proto_email_text_1 onlayer tvsignal
    hide proto_email_text_2 onlayer tvsignal
    hide bad_signal_computer_desktop
    show black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(1.0, hard='True')

    $ renpy.pause(0.1, hard='True')

    show dino-logo
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')
    with Pause(1)
    $ renpy.pause(0.1, hard='True')
    pause 1.8
    $ renpy.pause(0.1, hard='True')
    hide dino-logo
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')
    with Pause(1)

    $ renpy.pause(2.0, hard='True')

    pause 4

    window hide

    $ _rollback = True


    $ _history = True

    noname_proto "Существует мнение, что"

    noname_proto "Личность формируется \nблагодаря опыту-"

    noname_proto "Что когда мы рождаемся,{p=0.5}Мы ничем не отличаемся от куска глины."

    noname_proto "В течение всего жизненного пути{p=0.5}Мы постоянно меняемся,"

    noname_proto "Формируемся под влиянием как травмирующих событий, {w=0.5}так и обыденности повседневной жизни."

    noname_proto "Даже если это такая мелочь, {w=0.5}как \n {w=0.5}еда, которую вы едите, {w=0.5}кофе, который вы покупаете, {w=0.5}или время, {w=0.5}когда вы приходите на работу,"

    noname_proto "Эти непритязательные мелочи,{p=0.5}Они определяют наши судьбы,{p=0.5}а мы этого не замечаем."

    noname_proto "И конечно,{p=0.5}когда человек теряет свои воспоминания,{p=0.5}он лишается и своей личности."

    noname_proto "Но есть одна вещь, которая не выходит у меня из головы:"

    noname_proto "Что произойдет, если кто-либо обретет воспоминания...{p=0.5}{color=#f00}не принадлежащие ему?{/color}"

    noname_proto "......"

    window hide

    $ renpy.pause(1.0, hard='True')

    scene vincent-shadow-small
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')
    pause 1.0

    stop music fadeout 10.0

    $ renpy.pause(0.1, hard='True')

    scene vincent-shadow-smile-small
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    noname_proto_2 "{color=#f00}Я бы с удовольствием посмотрел, \nчто из этого получится.{/color}"
    window hide

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/vincent proto glitch.ogg"

    image distorted_vin_proto:
        "distorted-vincent-shadow"
        pause 0.1
        "images/empty.png"
        pause 1.0
        "distorted-vincent-shadow-2"
        pause 0.1
        "images/empty.png"
        pause 1.0
        "distorted-vincent-shadow"
        pause 0.1
        "distorted-vincent-shadow-2"
        pause 0.1
        "images/empty.png"
        pause 1.0
        repeat

    image distorted_vin_proto_3 = "images/Vin Proto/distorted vin proto 3.png"

    show game_over_static:
        alpha 0
        linear 4.0 alpha 0.1
    show distorted_vin_proto behind game_over_static
    $ renpy.pause(2.0, hard='True')
    hide distorted_vin_proto
    show distorted_vin_proto_3 behind game_over_static
    $ renpy.transition(PushMove(0.07, "pushup"))
    $ renpy.pause(0.07, hard=True)
    $ renpy.transition(PushMove(0.07, "pushup"))
    $ renpy.pause(0.07, hard=True)
    $ renpy.transition(PushMove(0.07, "pushup"))
    $ renpy.pause(0.07, hard=True)
    $ renpy.transition(PushMove(0.07, "pushup"))
    $ renpy.pause(0.07, hard=True)
    $ renpy.transition(PushMove(0.07, "pushup"))
    $ renpy.pause(0.07, hard=True)
    $ renpy.transition(PushMove(0.07, "pushup"))
    $ renpy.pause(0.07, hard=True)
    $ renpy.transition(PushMove(0.07, "pushup"))
    $ renpy.pause(0.07, hard=True)
    $ renpy.transition(PushMove(0.07, "pushup"))
    $ renpy.pause(0.07, hard=True)
    $ renpy.transition(PushMove(0.07, "pushup"))
    $ renpy.pause(0.07, hard=True)
    hide game_over_static
    hide screen clock_screen
    show proto_laptop:
        zoom 3.0 xalign 0.5 yalign 0.2
    show proto_no_signal:
        alpha 0 zoom 3.0 xalign 0.5 yalign 0.2
    show proto_no_signal_og:
        zoom 3.0 xalign 0.5 yalign 0.2
    show proto_lamp:
        zoom 3.0 xalign 0.5 yalign 0.2
        alpha 0
    $ renpy.pause(0.01, hard=True)

    hide bad_tv_signal onlayer tvsignal
    show proto_no_signal_og:
        parallel:
            linear 3.0 alpha 0
        parallel:
            linear 3.0 zoom 1.0 xalign 0.5 yoffset 0
    show proto_no_signal:
        parallel:
            linear 3.0 alpha 1
        parallel:
            linear 3.0 zoom 1.0 xalign 0.5 yoffset 0
    show proto_laptop:
        linear 3.0 zoom 1.0 xalign 0.5 yoffset 0
    show proto_lamp:
        parallel:
            linear 3.0 alpha 1
        parallel:
            linear 3.0 zoom 1.0 xalign 0.5 yoffset 0

    pause 3.0

    hide proto_no_signal_og
    show proto_no_signal:
        zoom 1.0 xalign 0.5 yoffset 0
    show proto_laptop:
        zoom 1.0 xalign 0.5 yoffset 0
    show proto_lamp:
        zoom 1.0 xalign 0.5 yoffset 0

    hide proto_no_signal
    show proto_no_signal_distorted behind proto_lamp

    $ renpy.pause(2.0, hard=True)
    show proto_m_hand:
        yoffset -50
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard=True)

    show proto_m_hand:
        linear 0.1 yoffset 55

    image proto_tv_turn_off:
        "images/TV turn off/tv turn off-1.png"
        pause 0.05
        "images/TV turn off/tv turn off-2.png"
        pause 0.05
        "images/TV turn off/tv turn off-3.png"
        pause 0.05
        "images/TV turn off/tv turn off-4.png"
        pause 0.05
        "images/TV turn off/tv turn off-5.png"
        pause 0.05
        "images/TV turn off/tv turn off-6.png"
        pause 0.05
        "images/empty.png"

    $ renpy.pause(0.15, hard='True')

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/tv turn off.ogg"

    scene black
    show proto_tv_turn_off

    $ renpy.pause(4.0, hard='True')
    pause 2.0

    jump day1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
