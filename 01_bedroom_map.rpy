






init -1 python:
    flipfade = ImageDissolve(im.Tile("images/bedroom-click/TransCornerFlip.jpg"), 1.0, 16)

default mtt_ = MouseTooltip(Image("images/bedroom-click/map cursor.png"), padding={"x": -1280, "y": -720})

image bedroom_map_1 = "images/bedroom-click/bedroom-map-1.png"
image bedroom_map_highlighted_g4 = "images/bedroom-click/g4-hover.png"
image bedroom_map_highlighted_g4_2 = "images/bedroom-click/g4-hover.png"

image bedroom_map_sepia = im.Sepia("images/bedroom-click/bedroom-map-1.png")
image bedroom_map_g4_sepia = im.Sepia("images/bedroom-click/g4-hover.png")

image bedroom_map_2 = "images/bedroom-click/bedroom-map-2.png"


image bedroom_window_mountain = "images/tree_animation/bedroom_window_mountain.png"
image bedroom_right_mountain = "images/tree_animation/bedroom_right_mountain.png"
image bedroom_left_mountain = "images/tree_animation/bedroom_left_mountain.png"
image bedroom_middle_mountain = "images/tree_animation/bedroom_middle_mountain.png"

image map_dust = Fixed(SnowBlossom(At("images/particles/dust-1.png", withAdd), count=1, border=50, xspeed=(-20, 20), yspeed=(20, 50), start=0, fast=False, horizontal=False), SnowBlossom(At("images/particles/dust-2.png", withAdd), count=2, border=50, xspeed=(-20, 20), yspeed=(20, 50), start=0, fast=False, horizontal=False))
image map_compass:
    "images/bedroom-click/compass.png"
    rotate 45
    block:
        ease 1.0 rotate -45
        pause 1.0
        ease 1.0 rotate 45
        pause 1.0
        repeat

image leaf_particles:
    contains:
        SnowBlossom("images/particles/leaf-1.png", count=1, border=100, xspeed=(-20, 20), yspeed=(190, 250), start=0, fast=False, horizontal=False)
    contains:
        SnowBlossom("images/particles/leaf-2.png", count=10, border=100, xspeed=(-20, 20), yspeed=(90, 150), start=3, fast=False, horizontal=True)
    contains:
        SnowBlossom("images/particles/leaf-2.png", count=2, border=100, xspeed=(-20, 20), yspeed=(200, 350), start=3, fast=False, horizontal=False)

screen bedroom_map_compass:
    add "images/bedroom-click/bedroom-map-grid.png"
    add "map_compass" xpos 1095 ypos 535
    add "map_dust"

screen map_travel_guide:
    add "images/bedroom-click/travel guide-small.png" xalign 0.5 yalign 0.5

screen wrong:
    add "images/wrong-small.png" xalign 0.5 yalign 0.5

screen correct:
    add "images/correct-small.png" xalign 0.5 yalign 0.5

screen bedroom_map__1:



    imagebutton:
        hover "images/bedroom-click/g1-hover.png"
        idle "images/bedroom-click/g1-idle.png"
        focus_mask "images/bedroom-click/g1-hover.png"
        xpos 48
        ypos -11

        action Jump("bedroom_map_1_g1")

    imagebutton:
        hover "images/bedroom-click/g2-hover.png"
        idle "images/bedroom-click/g2-idle.png"
        focus_mask "images/bedroom-click/g2-hover.png"
        xpos 460
        ypos -10

        action Jump("bedroom_map_1_g2")

    imagebutton:
        hover "images/bedroom-click/g4-hover.png"
        idle "images/bedroom-click/g4-idle.png"
        focus_mask "images/bedroom-click/g4-hover.png"
        xpos 897
        ypos -10

        action Jump("bedroom_map_1_g4")

    imagebutton:
        hover "images/bedroom-click/g5-hover.png"
        idle "images/bedroom-click/g5-idle.png"
        focus_mask "images/bedroom-click/g5-hover.png"
        xpos -18
        ypos 279

        action Jump("bedroom_map_1_g5")

    imagebutton:
        hover "images/bedroom-click/g3-hover.png"
        idle "images/bedroom-click/g3-idle.png"
        focus_mask "images/bedroom-click/g3-hover.png"
        xpos 337
        ypos 364

        action Jump("bedroom_map_1_g3")

    add mtt_

label bedroom_map_1_g1:

    $ renpy.block_rollback()

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/selectsounds.ogg"

    $ renpy.pause(0.1, hard='True')
    pause 0.2
    $ renpy.pause(0.1, hard='True')
    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/wrong.ogg"
    show screen wrong with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')
    pause 0.5
    $ renpy.pause(0.1, hard='True')
    hide screen wrong with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')

    $ renpy.block_rollback()

    noname "...не думаю, что я нахожусь в районе G1."

    $ renpy.block_rollback()


    $ renpy.call_screen("bedroom_map__1", _layer="front")

label bedroom_map_1_g2:

    $ renpy.block_rollback()

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/selectsounds.ogg"

    $ renpy.pause(0.1, hard='True')
    pause 0.2
    $ renpy.pause(0.1, hard='True')
    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/wrong.ogg"
    show screen wrong with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')
    pause 0.5
    $ renpy.pause(0.1, hard='True')
    hide screen wrong with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')

    $ renpy.block_rollback()

    noname "...не думаю, что я нахожусь в районе G2."

    $ renpy.block_rollback()


    $ renpy.call_screen("bedroom_map__1", _layer="front")

label bedroom_map_1_g3:

    $ renpy.block_rollback()

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/selectsounds.ogg"

    $ renpy.pause(0.1, hard='True')
    pause 0.2
    $ renpy.pause(0.1, hard='True')
    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/wrong.ogg"
    show screen wrong with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')
    pause 0.5
    $ renpy.pause(0.1, hard='True')
    hide screen wrong with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')

    $ renpy.block_rollback()

    noname "...не думаю, что я нахожусь в районе G3."

    $ renpy.block_rollback()


    $ renpy.call_screen("bedroom_map__1", _layer="front")

label bedroom_map_1_g5:

    $ renpy.block_rollback()

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/selectsounds.ogg"

    $ renpy.pause(0.1, hard='True')
    pause 0.2
    $ renpy.pause(0.1, hard='True')
    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/wrong.ogg"
    show screen wrong with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')
    pause 0.5
    $ renpy.pause(0.1, hard='True')
    hide screen wrong with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')

    $ renpy.block_rollback()

    noname "...не думаю, что я нахожусь в районе G5."

    $ renpy.block_rollback()


    $ renpy.call_screen("bedroom_map__1", _layer="front")

label bedroom_map_1_g4:

    $ renpy.block_rollback()

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/selectsounds.ogg"

    $ renpy.pause(0.1, hard='True')
    pause 0.2
    $ renpy.pause(0.1, hard='True')
    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/correct.ogg"
    show screen correct with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')
    pause 0.5
    $ renpy.pause(0.1, hard='True')
    hide screen correct with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')

    $ renpy.pause(0.5, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/scan map.ogg"


    show bedroom_map_highlighted_g4 onlayer front:
        xalign 1.023 yalign 0.5
    $ renpy.transition(wipeDown)
    $ renpy.pause(0.5, hard='True')

    window show

    $ _skipping = True

    noname "Район G4."

    window hide

    $ renpy.pause(0.1, hard='True')


    show screen map_travel_guide
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    window show

    $ rollback_ = True

    noname "Этот {color=#f00}\"Путеводитель по G4\"{/color}, который я держу в руках, скорее всего, был подготовлен владельцем дома для гостей, остановившихся в этой комнате."

    noname "В таком случае я,{w=0.5} вероятно,{w=0.5} нахожусь в районе G4."


    hide screen map_travel_guide
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    noname "Однако {w=0.5}G4 нельзя назвать небольшим районом."

    noname "Чтобы точнее понять ситуацию, в которой я нахожусь, {w=0.5}я должна все вспомнить и быть более конкретной."

    window hide

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)


    $ renpy.pause(0.6, hard='True')

    show bedroom_map_highlighted_g4_2 onlayer ab_parallax:

        xalign 1.023 yalign 0.5
        ease 1.0 xalign 0.5

    $ renpy.pause(0.1, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ["<silence 0.6>", "music/map move.ogg"]

    show bedroom_map_sepia behind bedroom_map_highlighted_g4_2 onlayer front:
        xalign 0.5 yalign 0.5
    show transparent dark-small behind bedroom_map_highlighted_g4_2 onlayer front:
        xalign 0.5 yalign 0.5 alpha 0.5
    hide bedroom_map_highlighted_g4 onlayer front
    hide screen bedroom_map_compass
    hide bedroom_map_1 onlayer front
    $ renpy.transition(Dissolve(2.0))
    $ renpy.pause(2.5, hard='True')

    show bedroom_map_2 onlayer ab_parallax:
        xalign 0.5 yalign 0.5
    hide bedroom_map_highlighted_g4_2 onlayer ab_parallax
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.5, hard='True')

    noname "В какой части района G4 я предположительно могу находиться?"

    $ rollback_ = False
    $ renpy.block_rollback()

    call screen bedroom_map__2

screen bedroom_map__2:


    imagebutton:
        idle "images/bedroom-click/pin-idle.png"
        hover "images/bedroom-click/pin-hover.png"
        xpos 490
        ypos 10
        hovered Play("sound", "music/click.wav")
        action Jump("bedroom_map_2_suburb")


    imagebutton:
        idle "images/bedroom-click/pin-idle.png"
        hover "images/bedroom-click/pin-hover.png"
        xpos 610
        ypos 253
        hovered Play("sound", "music/click.wav")
        action Jump("bedroom_map_2_city")


    imagebutton:
        idle "images/bedroom-click/pin-idle.png"
        hover "images/bedroom-click/pin-hover.png"
        xpos 513
        ypos 417
        hovered Play("sound", "music/click.wav")
        action Jump("bedroom_map_2_industry")


    imagebutton:
        idle "images/bedroom-click/pin-idle.png"
        hover "images/bedroom-click/pin-hover.png"
        xpos 445
        ypos 568
        hovered Play("sound", "music/click.wav")
        action Jump("bedroom_map_2_loading_dock")

    add mtt_

label bedroom_map_2_city:

    $ renpy.block_rollback()

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/selectsounds.ogg"

    $ renpy.pause(0.1, hard='True')
    pause 0.2
    $ renpy.pause(0.1, hard='True')
    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/wrong.ogg"
    show screen wrong with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')
    pause 0.5
    $ renpy.pause(0.1, hard='True')
    hide screen wrong with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')

    $ renpy.block_rollback()

    noname "...не думаю, что я нахожусь в центре."

    $ renpy.block_rollback()

    call screen bedroom_map__2

label bedroom_map_2_industry:

    $ renpy.block_rollback()

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/selectsounds.ogg"

    $ renpy.pause(0.1, hard='True')
    pause 0.2
    $ renpy.pause(0.1, hard='True')
    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/wrong.ogg"
    show screen wrong with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')
    pause 0.5
    $ renpy.pause(0.1, hard='True')
    hide screen wrong with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')

    $ renpy.block_rollback()

    noname "...не думаю, что я нахожусь в промзоне."

    $ renpy.block_rollback()

    call screen bedroom_map__2

label bedroom_map_2_loading_dock:

    $ renpy.block_rollback()

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/selectsounds.ogg"

    $ renpy.pause(0.1, hard='True')
    pause 0.2
    $ renpy.pause(0.1, hard='True')
    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/wrong.ogg"
    show screen wrong with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')
    pause 0.5
    $ renpy.pause(0.1, hard='True')
    hide screen wrong with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')

    $ renpy.block_rollback()

    noname "...не думаю, что я нахожусь в порту."

    $ renpy.block_rollback()

    call screen bedroom_map__2

label bedroom_map_2_suburb:

    $ renpy.block_rollback()

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/selectsounds.ogg"

    $ renpy.pause(0.1, hard='True')
    pause 0.2
    $ renpy.pause(0.1, hard='True')
    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/correct.ogg"
    show screen correct with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')
    pause 0.5
    $ renpy.pause(0.1, hard='True')
    hide screen correct with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')



    hide bedroom_map_2 onlayer ab_parallax
    hide bedroom_map_sepia onlayer front
    hide transparent dark-small onlayer front
    show bedrrom_window_background

    show main_title_shadow onlayer ab_parallax:
        alpha 0
        ease 5.0 alpha 1
    show leaf_particles onlayer ab_parallax:
        alpha 0
        pause 5.0
        ease 1.0 alpha 1
    show bedroom_window_frame onlayer ab_parallax
    show bedroom_tree_2_animation behind bedroom_window_frame onlayer absfront:
        xalign 0.5 yoffset 20
        pause 2.5
        ease 1.0 yoffset 300
    show bedroom_tree_1_animation behind bedroom_window_frame onlayer inyourface:
        xalign 0.5 yoffset 20
        pause 2.5
        ease 1.0 yoffset 300
    $ renpy.transition(Fade(.2, 0, 0.25, color="#fff"))
    $ renpy.pause(0.5, hard='True')

    $ renpy.pause(0.5, hard='True')

    show bedroom_window_frame onlayer ab_parallax:
        ease 1.5 zoom 5.0 alpha 0
    $ renpy.pause(1.0, hard=True)

    show bedroom_window_mountain behind bedroom_tree_2_animation onlayer absback:
        yoffset 500 xalign 0.5
        ease 1.5 yoffset 0
    show bedroom_middle_mountain behind bedroom_tree_2_animation onlayer farback:
        yoffset 500 xalign 0.5
        ease 1.6 yoffset 0
    show bedroom_left_mountain behind bedroom_tree_2_animation onlayer back:
        yoffset 500 xalign 0.5
        ease 1.7 yoffset 0
    show bedroom_right_mountain behind bedroom_tree_2_animation onlayer front:
        yoffset 500 xalign 0.5
        ease 1.8 yoffset 0

    $ renpy.pause(2.0, hard=True)

    window show

    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/mountain wind.ogg"

    $ _skipping = True

    noname "Будь я в городе, это не имело бы никакого смысла."

    $ rollback_ = True

    noname "Из окна я видела только огромный лесной ландшафт, {w=0.5}и совершенно никаких других строений поблизости не было."

    noname "Место, настолько изолированное, {w=0.5}настолько тихое, что можно было бы услышать падение булавки, {w=0.5}должно быть в пригороде G4."

    window hide

    stop music fadeout 6.0
    stop sound fadeout 3.0
    $ renpy.pause(0.1, hard='True')

    hide bedroom_right_mountain behind bedroom_tree_2_animation onlayer front
    hide bedroom_left_mountain behind bedroom_tree_2_animation onlayer back
    hide bedroom_middle_mountain behind bedroom_tree_2_animation onlayer farback
    hide bedroom_window_mountain behind bedroom_tree_2_animation onlayer absback
    hide bedroom_window_frame onlayer ab_parallax
    hide leaf_particles onlayer ab_parallax
    hide bedroom_tree_1_animation behind bedroom_window_frame onlayer inyourface
    hide bedroom_tree_2_animation behind bedroom_window_frame onlayer absfront
    hide main_title_shadow onlayer ab_parallax
    scene bedroom_green
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

    jump figure_out_bedroom_location
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
