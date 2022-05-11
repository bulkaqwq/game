







image bedroom_travel_guide = "images/bedroom-click/travel guide-small.png"


image bedroom_window_frame = "images/tree_animation/bedroom_window_frame.png"
image bedrrom_window_background = "images/tree_animation/tree_background.png"
image bedroom_tree_1_animation:

    "images/tree_animation/tree_1_4.png" with dissolve
    0.5
    block:
        "images/tree_animation/tree_1_1.png" with dissolve
        1.0
        "images/tree_animation/tree_1_2.png" with dissolve
        1.0
        "images/tree_animation/tree_1_3.png" with dissolve
        1.0
        "images/tree_animation/tree_1_4.png" with dissolve
        1.0
        repeat

image bedroom_tree_2_animation:

    "images/tree_animation/tree_2_4.png" with dissolve
    0.5
    block:
        "images/tree_animation/tree_2_1.png" with dissolve
        1.0
        "images/tree_animation/tree_2_2.png" with dissolve
        1.0
        "images/tree_animation/tree_2_3.png" with dissolve
        1.0
        "images/tree_animation/tree_2_4.png" with dissolve
        1.0
        repeat

label bed_click:
    $ bedroom_num_item = 0
    $ check_drawer = False
    $ check_window = False
    show bedroom_green behind bedroom_dust
    show screen bedroom_collect_items with Dissolve(0.1)
    call screen bed_room

style finish_investigation:
    color "#ffffff"
    hover_color "#FF0000"
    outlines [(2, "#000000", 0, 0,)]

screen bedroom_collect_items:

    zorder 10
    text _("{font=VHS.ttf}{color=#ffffff}УЛИКИ:[bedroom_num_item]/2{/color}{/font}") xpos 0.98 ypos 0.01 xanchor 1.0 outlines [(2, "#000000", 0, 0,)]
    vbox:
        xpos 0.983
        ypos 0.05
        xanchor 1.0
        textbutton _("{font=VHS.ttf}{size=-12}ЗАВЕРШИТЬ РАССЛЕДОВАНИЕ{/size}{/font}"):
            text_style "finish_investigation"
            action Jump("bedroom_finish_investigation")

screen bed_room:

    zorder 0
    imagebutton:

        xpos 71
        ypos 0
        idle "images/bedroom-click/window-empty-small.png"
        hover "images/bedroom-click/window-select-small.png"
        focus_mask "images/bedroom-click/window-select-small.png"
        action Jump("window")

    imagebutton:

        xpos 249
        ypos 241
        idle "images/bedroom-click/bedroom-empty-small.png"
        hover "images/bedroom-click/bedroom-select-small.png"
        focus_mask "images/bedroom-click/bedroom-select-small.png"
        action Jump("bed")

    imagebutton:

        xpos 848
        ypos 335
        idle "images/bedroom-click/drawer-empty-small.png"
        hover "images/bedroom-click/drawer-select-small.png"
        focus_mask "images/bedroom-click/drawer-select-small.png"
        action Jump("travel_guide")

    imagebutton:

        xpos 629
        ypos 0
        idle "images/bedroom-click/art-empty-small.png"
        hover "images/bedroom-click/art-select-small.png"
        focus_mask "images/bedroom-click/art-select-small.png"
        action Jump("art")

label bedroom_finish_investigation:

    if check_drawer == True and check_window == True:
        hide screen bed_room
        hide screen bedroom_collect_items
        jump finish_bed_click
    else:

        $ renpy.music.set_volume(0.8, delay=0, channel='sound')
        play sound "music/UI Dark.ogg"

        noname "Предупреждение: {w=0.5}Вы еще не закончили расследование. {p=0.5}Постарайтесь собрать больше улик."

        call screen bed_room

label bed:

    $ renpy.block_rollback()

    hide screen bedroom_collect_items
    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")
    hide bedroom_dust
    show bedroom_green:
        ease 0.5 zoom 1.5

    $ renpy.pause(0.7, hard='True')

    noname "Обычная кровать. {w=0.5}Но по ощущениям очень удобная."

    show bedroom_green:
        ease 0.5 zoom 1
    $ renpy.pause(0.5, hard='True')

    show bedroom_dust:
        alpha 0
        pause 1.0
        block:
            ease 5.0 alpha 0.5
            ease 5.0 alpha 1.0
            ease 5.0 alpha 0.5
            ease 5.0 alpha 0
            pause 5.0
            repeat

    $ renpy.block_rollback()

    show screen bedroom_collect_items with Dissolve(0.1)
    call screen bed_room

label art:
    $ renpy.block_rollback()

    hide screen bedroom_collect_items
    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")
    hide bedroom_dust
    show bedroom_green:
        ease 0.5 zoom 2 yoffset 700 xoffset -450

    $ renpy.pause(0.7, hard='True')

    noname "На стене выстроились в ряд произведения современного искусства, {w=0.5}каждое из которых привлекало к себе внимание."

    show bedroom_green:
        ease 0.5 zoom 1 yoffset 0 xoffset 0

    $ renpy.pause(0.5, hard='True')

    show bedroom_dust:
        alpha 0
        pause 1.0
        block:
            ease 5.0 alpha 0.5
            ease 5.0 alpha 1.0
            ease 5.0 alpha 0.5
            ease 5.0 alpha 0
            pause 5.0
            repeat

    $ renpy.block_rollback()

    show screen bedroom_collect_items with Dissolve(0.1)
    call screen bed_room

label travel_guide:

    $ renpy.block_rollback()

    hide screen bedroom_collect_items
    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")
    hide bedroom_dust
    show bedroom_green:
        ease 0.7 zoom 3 xoffset -900 yoffset 200

    $ renpy.pause(0.7, hard='True')

    $ _skipping = True

    noname "Я открыла тумбочку рядом с кроватью."

    $ rollback_ = True

    $ renpy.music.set_volume(0.7, delay=0, channel='sound')
    play sound ("music/drawer.ogg")

    show transparent dark-small:
        alpha 0.8
    with Dissolve(0.2)
    show bedroom_travel_guide onlayer inyourface

    pause 2.0

    noname "Это что... {w=0.5}{color=#f00}путеводитель{/color}?"

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/PageFlipshort.ogg"

    $ renpy.pause(1.0, hard='True')

    pause 4.0

    noname "Я мельком взглянула на некоторые страницы."

    noname "Содержимым журнала являлись детально проработанные статьи и фотографии местных достопримечательностей."

    if not check_drawer:
        stop sound
        $ bedroom_num_item = bedroom_num_item + 1

        if renpy.is_skipping():
            $ renpy.choice_for_skipping()
        $ _skipping = False

        $ renpy.pause(0.5, hard='True')

        $ renpy.music.set_volume(0.8, delay=0, channel='sound')
        play sound "music/UI Dark.ogg"

        noname "Собрана улика: {w=0.5}Путеводитель"

    stop sound fadeout 3.0

    hide bedroom_travel_guide onlayer inyourface
    hide transparent dark-small with Dissolve(0.2)

    show bedroom_green:
        ease 0.5 zoom 1 yoffset 0 xoffset 0
    $ renpy.pause(0.5, hard='True')

    $ rollback_ = False
    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    $ check_drawer = True
    $ renpy.block_rollback()

    hide bedroom_green
    scene bedroom_green
    show bedroom_dust:
        alpha 0
        pause 1.0
        block:
            ease 5.0 alpha 0.5
            ease 5.0 alpha 1.0
            ease 5.0 alpha 0.5
            ease 5.0 alpha 0
            pause 5.0
            repeat
    show screen bedroom_collect_items with Dissolve(0.1)
    call screen bed_room

label window:

    $ renpy.block_rollback()

    hide screen bedroom_collect_items
    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")
    hide bedroom_dust
    show bedroom_green:
        ease 0.5 zoom 2 xoffset 600 yoffset 500

    $ renpy.pause(0.5, hard='True')
    show bedrrom_window_background
    show bedroom_window_frame onlayer inyourface:
        xalign 0.5 yalign 0.5
    show bedroom_tree_2_animation behind bedroom_window_frame onlayer front:
        xalign 0.5 yalign 0.5
    show bedroom_tree_1_animation behind bedroom_window_frame onlayer farback:
        xalign 0.5 yalign 0.5
    show bedroom_dust onlayer ab_parallax:
        alpha 0
        pause 1.0
        block:
            ease 5.0 alpha 0.5
            ease 5.0 alpha 1.0
            ease 5.0 alpha 0.5
            ease 5.0 alpha 0
            pause 5.0
            repeat

    with Dissolve(0.2)

    $ renpy.pause(0.5, hard='True')

    $ _skipping = True

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/dust.ogg") fadeout 3.0
    noname "За окном было {color=#f00}необычайно тихо{/color}, {w=0.5}только листья шелестели в такт дуновениям ветра."

    $ rollback_ = True

    noname "Вдали виднелись лишь бескрайние горные массивы, {color=#f00}покрытые лесами{/color}, {w=0.5}простирающиеся насколько хватало глаз."

    if not check_window:
        $ bedroom_num_item = bedroom_num_item + 1

        if renpy.is_skipping():
            $ renpy.choice_for_skipping()
        $ _skipping = False

        $ renpy.pause(0.5, hard='True')

        $ renpy.music.set_volume(0.8, delay=0, channel='sound')
        play sound "music/UI Dark.ogg"

        noname "Собрана улика: {w=0.5}Вид"

    hide bedrrom_window_background
    hide bedroom_window_frame onlayer inyourface
    hide bedroom_tree_1_animation onlayer farback
    hide bedroom_tree_2_animation onlayer front
    hide bedroom_dust onlayer ab_parallax
    with Dissolve(0.2)
    show bedroom_green:
        ease 0.5 zoom 1 yoffset 0 xoffset 0
    $ renpy.pause(0.5, hard='True')

    $ rollback_ = False
    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    $ check_window = True
    $ renpy.block_rollback()

    hide bedroom_green
    scene bedroom_green
    show bedroom_dust:
        alpha 0
        pause 1.0
        block:
            ease 5.0 alpha 0.5
            ease 5.0 alpha 1.0
            ease 5.0 alpha 0.5
            ease 5.0 alpha 0
            pause 5.0
            repeat

    show screen bedroom_collect_items with Dissolve(0.1)
    call screen bed_room
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
