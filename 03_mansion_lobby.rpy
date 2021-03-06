
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
    noname "*??????????*"

    noname "???? ??????????, {w=0.5}???? ??????????, {w=0.5}???? ????????????????????..."

    noname "?????? ?????????????????? ???????? ????????, ?????? ?? ??????????????."

    show vic-smoke-low-talk-small at vic_pos with Dissolve(0.2)
    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/hmm.ogg"

    vic "\"????, {w=0.5}????????????????, {w=0.5}???? ?????????? ?????? ????????????????????.\""

    vic "\"???????????? ????, {w=0.5}???????????? ???????????????????????? ?????????? ???????? ?????????? ????????????.\""

    vic "\"???????????????????????? ???????????????????? ?????????? ?????????????????????? ?? ?????????? ?????????????????????? ????????????????????????; {w=0.5}?????? ?????? ???????? ?????? ?????????????????? ???? ??????????????????, {w=0.5}???? ?? ???? ???? ?????????? ?????????????????? ???? ??????.\""

    vic "\"???? ????????, {w=0.5}?? ???????????? ??????????????, {w=0.5}?????????? ???????????? ????????.\""

    $ say_who = _("????????????")

    show vic-smoke-talk-small at vic_pos with Dissolve(0.2)
    hide vic-smoke-low-talk-small
    vic "\"?????????? ?????? ???? ??????????????? {w=0.5}???? ???????????? ????????????, {w=0.5}???????? ?? ?????????????? ?????????????? ????????????????????.\""

    $ say_who = ""

    hide vic-smoke-talk-small with Dissolve(0.2)
    noname "...?? ??????????????, ?? ???????? ???? ????????????, {w=0.5}???? ????????????????, {w=0.5}?????? ?????????? ???????? ????????, ?????? ???????? ???????????????????"

    noname "?? ?????????? ??????????????????."

    stop music fadeout 3.0
    $ renpy.pause(0.1, hard='True')
    $ renpy.music.set_volume(0.3, delay=0, channel='sound')
    play sound "music/mad vincent.ogg" fadeout 1.0
    show vic-smoke-upset-small at vic_pos
    anon "\"????????????, {w=0.5}?????????????? ?????? ???????? ??????????????????? {w=0.5}?????????????????? ???????????? ?? ???????? ????????????????!\"" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    show vic-smoke-talk-small at vic_pos with Dissolve(0.2)
    hide vic-smoke-upset-small
    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music "music/Vincent bgm.ogg"
    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/huh.ogg"
    pause 1.0

    vic "\"????-????, {w=0.5}???????????? ??????????????. {w=0.5}?????? ???? ???? ?????? ?????????????? ???????? ??????????????!\""

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

    noname "??????????????? {w=0.5}?????? ?????? ???? ???????????????? ?????????????????"

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/vin_hmm.ogg"
    show vin-arm-angry-small at vin_pos_2
    show vic-low-brow-small-flip at vic_pos_2
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard=True)
    hide vin-black-small
    hide vic-normal-flip-small


    vin "\"??????????, {w=0.5}???????? ???????? ???????????????????? ???????????????? ?????? ??????????-???????? ????????????????????, {w=0.5}???? ?? ???????? ?????????????????? ?? ?????????????? ?? ?????????????????? ???????????????????? ?????? ??????????????????.\""

    noname "\"??????... {w=0.5}??????????, ?? ?? ??????????????. {w=0.5}?? ?????????? ????????????, ??????????????.\" {w=0.5}?????????????? ???????????????? ??."

    noname "(...?????? ???????? ?????????????????????????? ?????????????)"

    noname "\"??????????????, {w=0.5}?????????????????? ????????????, ???? ???? ???? ?????????????????? ???????????????????? ?????????? ?????????????????\""

    show vin-arm-normal-small at vin_pos_2 with Dissolve(0.2)
    hide vin-arm-angry-small
    pause 1.0
    show vin-arm-talk-small at vin_pos_2 with Dissolve(0.2)

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/Vincent.ogg"

    vin "\"????, ?????? ?? ????????.\" {w=0.5}?????????????????? ????."

    vin "\"?????????????? ?????? ?????????????????? ???? ????, ?????? ???? ???????????????????????? ?????????????? ??????????????. {w=0.5}?????? ?????? - {color=#f00}?????????????? ??????????????{/color}, {w=0.5}?? ?? ???????????????? ?????????? ????????????????.\""

    jump vin_intro

label vin_intro_end:
    show vin-arm-talk-small at vin_pos_2 with Dissolve(0.2)
    vin "\"???????? ?? ???????????? ???????? ??????, {w=0.5}??????????? {w=0.5}?? ???????? ???????????? ?????????????\""

    hide vin-arm-talk-small at vin_pos_2 with Dissolve(0.2)

    noname "...???????? ?????????? ????????????? {w=0.5}?????? ????????????, ?????? ?? ???????????? ?????????"

    noname "\"????????... {w=0.5}??...\" {w=0.5}?? ?? ???? ??????????, ?????? ?????? ????????????????."

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/huh.ogg"

    show vic-talk-small-flip at vic_pos_2 with Dissolve(0.2)
    vic "\"?????????? ????????????, {w=0.5}??????????????. {w=0.5}????????????, ?????? ???????? ???????????? ???????????????? ?????? ???????? ????????????????????????.\""
    hide vic-low-brow-small-flip
    hide vic-talk-small-flip with Dissolve(0.2)
    show vic-normal-small-flip at vic_pos_2

    noname "???????????? ???????????? ?????? ???? ????????????."

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/vin_hmm.ogg"
    show vin-arm-talk-small at vin_pos_2 with Dissolve(0.2)
    vin "\"??????... {w=0.5}??????????????????????????? {w=0.5}?????? ??????????????????.\""

    vin "\"?????? ??????, {w=0.5}???? ???????????? ???? ???? ?????????????? ?????? ?????? ?????????? ??????, {w=0.5}???????????\""

    hide vin-arm-talk-small with Dissolve(0.2)

    noname "??????????????, ???? ????????. {w=0.5}?????????? ???? ?????????? ?????????????????? ??????, ?????? ????????????."

    window hide

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False

    $ renpy.pause(0.5, hard='True')

    window show

    noname "????????, {w=0.5}?????????? ???? ?????? ?????? ???????????????"

label enter_name:

    python:
        name = renpy.input(_("?????????????? ??????: "), pixel_width = 140)
        name = name.strip()

        if not name:
            name = _("??????????????")


    if name.lower().replace(" ", "") == _("??????") or name.lower().replace(" ", "") == _("dino") or name.lower().replace(" ", "") == _("????????") or name.lower().replace(" ", "") == _("dino999z") or name.lower().replace(" ", "") == _("?????????"):
        noname "????????: {w=0.5}?????????????????? ????????????????????."
        jump enter_name


    if name.lower().replace(" ", "") == _("??????") or name.lower().replace(" ", "") == _("????????????") or name.lower().replace(" ", "") == _("??????????????") or name.lower().replace(" ", "") == _("??????????????") or name.lower().replace(" ", "") == _("vincent") or name.lower().replace(" ", "") == _("edgeworth"):
        show vin-arm-angry-small at vin_pos_2 with Dissolve(0.2)
        $ renpy.music.set_volume(0.6, delay=0, channel='sound')
        play sound "music/vin_hmm.ogg"
        noname "...??????????????, {w=0.5}??????????????, {w=0.5}???? ?????????? ?????????? ??????."
        hide vin-arm-angry-small with Dissolve(0.2)
        jump enter_name


    if name.lower().replace(" ", "") == _("?????????") or name.lower().replace(" ", "") == _("?????????") or name.lower().replace(" ", "") == _("????????????") or name.lower().replace(" ", "") == _("??????????") or name.lower().replace(" ", "") == _("victor") or name.lower().replace(" ", "") == _("blake"):
        $ renpy.music.set_volume(0.8, delay=0, channel='sound')
        play sound "music/huh.ogg"
        show vic-talk-small-flip at vic_pos_2 with Dissolve(0.2)
        vic "\"????????. {w=0.5}??????????????, {w=0.5}?? ?????????? ???????? ??????????????????????, {w=0.5}?????\""
        hide vic-talk-small-flip at vic_pos_2 with Dissolve(0.2)
        jump enter_name


    if name.lower().replace(" ", "") == _("?????????") or name.lower().replace(" ", "") == _("winston") or name.lower().replace(" ", "") == _("??????????????") or name.lower().replace(" ", "") == _("??????????????"):
        label name_sus:
            noname "????????: {w=0.5}...???????? ?????????? ???????????????? ?????????????? ????????????????????."
            jump enter_name


    if name.lower().replace(" ", "") == _("?????????") or name.lower().replace(" ", "") == _("zalmona") or name.lower().replace(" ", "") == _("??????????????"):
        noname "????????: {w=0.5}???????????? ????????????????????, {w=0.5}???????? ?????????? ???????????????? ??????????????????????. {w=0.5}??????????????????, {w=0.5}?????? ???????????????? ????????????????????."
        jump enter_name


    if name.lower().replace(" ", "") == _("?????????") or name.lower().replace(" ", "") == _("draco") or name.lower().replace(" ", "") == _("??????????"):
        show vin-arm-angry-small at vin_pos_2 with Dissolve(0.2)
        noname "...?????????????? ???????????? ?? ?????? ?????????????? ???????????????????????????? ????????????, {w=0.5}?????? ?????????? ?? ???????????? ?? ??????-????, {w=0.5}???????? ???? ???????????? ???????? ??????????."
        hide vin-arm-angry-small with Dissolve(0.2)
        jump enter_name


    if name.lower().replace(" ", "") == _("?????????") or name.lower().replace(" ", "") == _("emanon") or name.lower().replace(" ", "") == _("????????????"):
        show vin-arm-angry-small at vin_pos_2 with Dissolve(0.2)
        noname "...?????????????? ???????????? ?? ?????? ?????????????? ???????????????????????????? ????????????, {w=0.5}?????? ?????????? ?? ???????????? ?? ??????-????, {w=0.5}???????? ???? ???????????? ???????? ??????????."
        hide vin-arm-angry-small with Dissolve(0.2)
        jump enter_name


    if name.lower().replace(" ", "") == _("????????????") or name.lower().replace(" ", "") == _("albert") or name.lower().replace(" ", "") == _("??????????????") or name.lower().replace(" ", "") == _("krueger") or name.lower().replace(" ", "") == _("????????????") or name.lower().replace(" ", "") == _("?????????"):
        show vin-arm-angry-small at vin_pos_2 with Dissolve(0.2)
        $ renpy.music.set_volume(0.6, delay=0, channel='sound')
        play sound "music/vin_hmm.ogg"
        noname "...??????????????, {w=0.5}????????????, {w=0.5}???? ?????????? ?????????????????????? ??????????, {w=0.5}???? ???? ???????????? ?????????????? ????????????????????????."
        hide vin-arm-angry-small with Dissolve(0.2)


    if name.lower().replace(" ", "") == _("?????????") or name.lower().replace(" ", "") == _("claude") or name.lower().replace(" ", "") == _("????????"):
        noname "????????: {w=0.5}??????, ?????????????????"
        jump enter_name


    if name.lower().replace(" ", "") == _("?????????") or  name.lower().replace(" ", "") == _("vanora") or  name.lower().replace(" ", "") == _("????????????"):
        noname "????????: {w=0.5}...???????? ?????????? ???????????????? ?????????????? ????????????????????."
        jump enter_name


    if name.lower().replace(" ", "") == _("?????????") or name.lower().replace(" ", "") == _("myers") or name.lower().replace(" ", "") == _("????????????") or name.lower().replace(" ", "") == _("m??????"):
        show vin-arm-angry-small at vin_pos_2 with Dissolve(0.2)
        noname "...?????????????? ???????????? ?? ?????? ?????????????? ???????????????????????????? ????????????, {w=0.5}?????? ?????????? ?? ???????????? ?? ??????-????, {w=0.5}???????? ???? ???????????? ???????? ??????????."
        hide vin-arm-angry-small with Dissolve(0.2)
        jump enter_name

    menu:
        van "??????????, ?????? ?????????????????? [name!t]?"
        "????":
            jump finish_name
        "??????":
            jump enter_name

label finish_name:

    $ renpy.block_rollback()

    window show

    van "[name!t]. {w=0.5}????????????????????, ???????????? ???????? [name!t]."

    $ _skipping = True

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/Amazing.ogg"

    show vin-arm-talk-small at vin_pos_2 with Dissolve(0.2)
    stop music fadeout 6.0
    vin "\"[name!t]? {w=0.5}????????????????????????. {w=0.5}?? ?????????? ?????? ?????????????????????????? ?? ????????, {w=0.5}[name!t].\""

    vin "\"???? ???????????? ?? ?????????????????????????????? ??????????????????, {w=0.5}?? ?? ??????????????????????, {w=0.5}?????? ?? ?????? ???????????????????? ???????????? ????????????????.\""

    vin "\"?????????? ???????? ?? ?????????? ??????-???? ???????????? ???????\""

    hide vin-arm-talk-small with Dissolve(0.2)

    van "?????????????? ?????????? ?????????? ???????????? ????????????????????, {w=0.5}?????????????? ?????????????? ?????? ???????????????????????? ????????????. {w=0.5}?????? ???? ?????? ?? ???????? ?????????????????"

    window hide

    $ renpy.music.set_volume(0.8, delay=0, channel='music')
    play music "music/jazz.ogg"

    $ ask_vin_q1 = False
    $ ask_vin_q2 = False

label ask_vincent:

    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    menu:
        "?????? ?? ?????????? ???????????????????":
            $ ask_vin_q1 = True
            jump ask_how_get_here

        "?????? ?????? ?????? ???? ?????????????" if ask_vin_q1  == True:
            $ ask_vin_q2 = True
            jump ask_vin_robot_1

        "???????? ???? ?? ???????? ??????-???????????? ?? ???????????" if ask_vin_q2  == True:
            jump ask_brought_items

label ask_how_get_here:

    window show
    van "\"???????????? ??????????????, {w=0.5}??????????????, ????????????????????, {w=0.5}?????? ?? ?????????? ???????????????????\""

    show vin-arm-talk-small at vin_pos_2 with Dissolve(0.2)

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/Vincent.ogg"
    vin "\"?????? ???? ?????????? ??????????????????? {w=0.5}[name!t], {w=0.5}?? ?????????? ??????????????????, ?? ???????? ???? ????????.\""

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
    vin "\"???????? ?? ??????, ?????? {w=0.5}{color=#f00}?????? ??????????????????{/color} ?????????? ?????????????? ?????????????? ???????????????? ???????? ?? ??????????.\""

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
    vin "\"?????????? ???? ???????????? ????, {w=0.5}???? ???????????? ??????, {w=0.5}?????????????? ???? ??????????????. {w=0.5}{color=#f00}?????? ????????????????{/color}.\""

    hide van-faint-small
    hide black
    $ renpy.transition(Fade(.4, 0, 0.25, color="#fff"))
    $ renpy.pause(1.0, hard='True')

    window show
    vin "\"?????????????????? ???? ???????????? ???? ?????????? ???? ?? ??????, {w=0.5}???? ?? ??????, ?? ?????????? ?????????? ???? ??????????????, {w=0.5}???? ???????????? ???? ?????????? ???????????????????? ?????? ?? ?????????????? ?????? ????????????.\""

    hide vin-arm-talk-small with Dissolve(0.2)

    van "......"

    van "?????????????????? ?????????????????? ?????????????????? ???????? ?????????????? ????????????????????."

    van "?????????? ?? ?????????? ???????????????? ?? ?????? ???????????????"

    window hide

    jump ask_vincent

label ask_vin_robot_1:

    window show

    van "\"?????????? ?????????????? ?? ?????????????? ?????????? ????????????????, {w=0.5}???????????????? ?????????????? ???????????? ???? ????????????.\""

    van "\"?????????? ?????????????? ????... {w=0.5}????????????????????????-????????????????????.\""

    van "\"?????? ?????? ???????????? ?????????\""

    show vin-arm-talk-small at vin_pos_2 with Dissolve(0.2)

    $ renpy.music.set_volume(0.3, delay=0, channel='sound')
    play sound "music/vin_hmm.ogg"

    vin "\"??, ?????????????? [name!t]. {w=0.5}????????????, ?????? ???? ?????? ?????????????????????? ???????????? ???? ???????? ????????????.\""

    vin "\"????, {w=0.5}????????????????????, {w=0.5}???????????????????? ??????, {w=0.5}?????? ???? ?????????????? ???????????? ???? ???????????????????????????? ????????, {w=0.5}?????????? ?? ???????? ?????? ??????????????????????????.\""

    hide vin-arm-talk-small with Dissolve(0.2)

    van "...???????????????????????????? ????????? {w=0.5}?????? ???? ?????? ???????"

    window hide

    jump ask_vincent

label ask_brought_items:

    window show

    van "\"?? ???????? ???????? ??????-???????????? ?? ??????????, ?????????? ?? ???????? ?????????????\""

    $ renpy.music.set_volume(0.3, delay=0, channel='sound')
    play sound "music/vin_hmm.ogg"

    show vin-arm-talk-small at vin_pos_2 with Dissolve(0.2)

    vin "\"????... {w=0.5}?????? ???? ???? ???????????????????? ???? ????????, {w=0.5}???? ?????????? ?????? ?????? ???????? {color=#f00}?? ?????????? ??????????????{/color}.\""

    hide vin-arm-talk-small with Dissolve(0.2)

    van "???? ???????????????? ?????? ???????????????? ????????????????."

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

    van "???? ?????????????? ?????????? ?????????????? ???????? ???? ????????????????????, {w=0.5}???? ?????????????????????? ?????????????????? {color=#f00}???????????????? ?? ???????? ?????????? ??????{/color}."

    hide hand_over_card_bg
    hide hand_over_card onlayer inyourface
    with Dissolve(0.5)

    window show

    van "\"???????????????????? ?????????????\" {w=0.5}?? ????????????????????, {w=0.5}?????? ?? ?????????? ?????????????? ?????? ????????????????."

    van "???????????? ?? ???????? ???????? ???????????????? ???????????????? ????????-????, ?????? ?????? ?????????????????"

    pause 0.5

    van "\"?????? ?????? ???? ???????????????????? ?????????????\" {w=0.5}???????????????? ??, ???????????? ????????????."

    pause 0.3

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/hmm.ogg"
    show vic-talk-small-flip at vic_pos_2 with Dissolve(0.2)

    vic "\"???????????????????? ???????????? - {w=0.5}?????????????? ???????????????????????????????????? ????????????????, {w=0.5}?????????????????????????? ?? ???????????? G4.\" {w=0.5}???????????? ????????????."

    vic "\"?????????? ????????, {w=0.5}?????? ???????????? ????????????????, {w=0.5}?????????????? ???????????? ?????????????????????? ?????????????????????????????? ???????????????????????? ??????????????.\""

    vic "\"????, ?? ??????????????????, {w=0.5}?????? ???????????????? ???????? ?????????????????? ???????????????? ?? ?????????????????????? ????-???? {color=#f00}?????????????????????? ??????????????????,{/color} {w=0.5}?????????????????????????? {color=#f00}???????? ?????? ??????????{/color}.\""

    hide vic-talk-small-flip with Dissolve(0.2)

    van "\"?????????????????????? ???????????????????\""

    show vin-dark-small at vin_pos_2 with Dissolve(0.2)
    stop music fadeout 6.0
    $ renpy.music.set_volume(0.3, delay=0, channel='sound')
    play sound "music/vin_hmm.ogg"
    vin "\"???????????????? ?????????????? G4.\""

    van "?????????????? ???????????????? ?????????????????????? ?????????? ???????? ?????????????????????? ???? ????????."

    van "\"???????????????? ?????????????? G4? {w=0.5}?????? ?????????? ???????????????????\""

    show vic-low-brow-small-flip at vic_pos_2 with Dissolve(0.2)

    van "?????????????? ?? ???????????? ???? ?????????????????? ??????????????????, {w=0.5}???????????? ????????????????????, {w=0.5}?????????? ???? ?????? ???????????? ?????????? ???? ???????? ??????????????. "

    show vic-talk-small-flip at vic_pos_2 with Dissolve(0.2)
    hide vic-low-brow-small-flip

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/hmm.ogg"

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music "music/creepy.wav"

    vic "\"?? ???????????? 2080 ???????? ???? ???????? ???????????? ???????????????????????? ?????????????? ?????????????? ???????????????? ???????????????????? ??????????????.\""

    van "???????????? ??????????????-???? ?????????? ??????????????????."

    window hide

    show black
    $ renpy.transition(Fade(.2, 0, 0.25, color="#fff"))
    $ renpy.pause(0.5, hard='True')

    show missing_1 with Dissolve(0.5)
    $ renpy.pause(0.5, hard='True')

    window show

    $ say_who = _("????????????")

    vic "\"?????? ?????????????? ???????? ?????????????? ??????????, {w=0.5}?????? ?????????? ?????????????????????????? ?? ??????????????.\""

    show missing_2 with Dissolve(0.5)
    hide missing_1
    vic "\"???? ??????????????????, {w=0.5}???? ????????????, {w=0.5}???? ?????????? ??????????. {w=0.5}???????????? ???? ????????????????.\""

    show missing_3 with Dissolve(0.5)
    hide missing_2
    vic "\"???? ?? ???????? ?????????? ???????? ??????-?????? ??????????: {w=0.5}?????? ?????? ?? ?????????????????? ?????? ???????? ???????????????? ?? {color=#f00}???????????? G4{/color}.\""

    show missing_4 with Dissolve(0.5)
    hide missing_3
    vic "\"?? ?????? ???????????????? ?????????? ??????????????, {w=0.5}?????????? ?????????????????? ?????????? ?????????????? ?????????????????? ???? ???????? ?????????????\""

    show myers_small with Dissolve(0.5)
    hide missing_4
    vic "\"??????????????????????, {w=0.5}?????????????? ?????????????????????? ???????????????????? ????????????, {w=0.5}???????????????????? ?????????????????????????? ??????????????????, {w=0.5}?????????????????????????? ?? ???????????? G4.\""

    vic "\"?????? ???? ??????????, {w=0.5}???????????????????? ???????????? ???????????????? ??????????-???????? ???????????????????????? ?? ?????????? ????????.\""

    show chamber_1 with Dissolve(0.5)
    hide myers_small
    vic "\"???????????? ?????? ?????????????????????????? ?????????????? ???????????????????? ???????????????????? {color=#f00}?????????????????? ??????????????????, {w=0.5}?????????????????????????? ?? ?????????????? ????????????????????{/color}.\""

    show chamber_2 with Dissolve(0.5)
    hide chamber_1
    vic "\"???????????? ???????? ??????????????... {w=0.5}{color=#f00}???????????????????? ???????????? ????????????????{/color}.\""

    van "(????????????????? {w=0.5}???? ?? ?????????? ???? ?????????????????? ?? ?????????????????????? ??????????...?)"

    vic "\"???????????? ?????????????? ???????? ???? ????????????????????????, {w=0.5}?????? ?????? ?????????????? ?? ???????? ???????????????????? ????????????????????.\""

    vic "\"???? ???????????? ?????????????????? ?????? ??????????????.\""

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

    vic "\"?? ???????????????????????????????? ?????? ?????????????????? ???????????????? ???????? ???????????????????????? ?? ???????????????? {color=#f00}??????????{/color} ?????? ????????????????.\""

    hide blood-2
    hide chamber_3
    with Dissolve(0.25)

    vic "\"?????? ???????????????? ????????, {w=0.5}???????????? ?????????????????? ???????? ??????????????... {p=0.5}{color=#f00}?????????? ?????????? ???? ????????{/color}.\""

    show court_1 with Dissolve(0.5)
    vic "\"???? ???????? ?? ?????????? ???????? ???????????????????????? ???????????????????? ????-???????????????? ???????????????? ????, {w=0.5}?????? ??????????-???????? ???????????? ???????????????????? ???? ???????????????????? ?????????? ???????????????????????????? ????????????????????????.\""

    show court_2 with Dissolve(0.5)
    hide court_1
    vic "\"?????????????????? ???????????? {color=#f00}????????????????{/color} ?????? ?????????????? ???????? ???????????????????? ??????????????????.\""

    show winston_1 with Dissolve(0.5)
    hide court_2
    vic "\"???? ?????? ???????????????????? ?? ???????????????????????? ???????????????????? ?????? ?????????? ???? ?????????????????? ????????????????????????, {w=0.5}?? ???? ?????????? ?????? ?? ?????????? ???????????????? ???????? ?????????? ?????? ??????????????????.\""
    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ["<silence .25>", "music/prison.ogg"]
    show winston_2 at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=30) with wipeDown
    $ renpy.pause(0.1, hard='True')
    hide winston_1
    hide winston_2
    with Dissolve(0.5)
    vic "\"???????????? ???? ???????? ?????????????? ???? ??????????????????????.\""

    show car with Dissolve(0.5)
    vic "\"?????? ???????????? ???????????? ?????????????? ?????????????? ?????????????????? ???????????? ?? {color=#f00}?????????????????????????? ????????????{/color} ?? ???????? ???? ??????????.\""
    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ["music/car crash.ogg"]
    hide car with Fade(.25, 0, 0.25, color="#fff")

    vic "\"?? ?????????????? ???????? ???? ???????? {color=#f00}?????? ?????????????? ???????????????????? ???????????????????? ???????????? ???????? ?????????????? ?????????????? ??????????????{/color}.\""

    $ renpy.pause(0.1, hard='True')
    show blood_stain with Dissolve(1.0)
    vic "\"????????????????????, {w=0.5}?????????????? ???? ???????? ????????, {w=0.5}?????? ?????????????? ?? ???? ?????? ????????????.\""

    hide blood_stain with Dissolve(0.5)
    pause 0.5
    $ renpy.pause(0.1, hard='True')
    show g4_street with Dissolve(0.5)

    pause 0.5

    vic "\"?? ???? ?????? ?????? ?? ???????????? G4 ???????????????????????? ?????????????? ???????????????? ????????.\""

    pause 0.3

    stop music fadeout 8.0
    vic "\"?????????? ??????????, {w=0.5}?????? ???????? ?????????? ???????????????????????? ?????? ?????? ???????????? ???? ????????????, {w=0.5}?????????????? ?????????? ?????? ????????????????????, {w=0.5}?????? ???????????????????? ?? ????????...\""

    $ say_who = ""

    hide g4_street
    hide blood_stain
    hide black
    $ renpy.transition(Dissolve(1.5))
    $ renpy.pause(1.5, hard='True')

    hide vic-talk-small-flip with Dissolve(0.5)

    window show

    van "......"

    van "???? ???????????????? ?????????????? ?? ???????? ???? ?????????? ???????????????? ??????????????."

    van "?? ???????????????????? ???? ?????????????? ?????????? ???????????????? ?????????????????? ?????????????? ???? ???????????? G4."

    van "\"????????????, {w=0.5}???????? ?? ????????????????????????????????, {w=0.5}???????????? ???? ?????? ?????? ?????????????\""

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/hmm.ogg"
    show vic-talk-small-flip at vic_pos_2 with Dissolve(0.2)

    pause 0.2

    vic "\"?????????? ???? ???????? ???????????? ???????????????? ??????????,\" {w=0.3}???????????????????? ????????????."

    vic "{color=#f00}\"???? ?? ?????????????????? ?????? ?? ?????????????? ???????? ???????????????????????? ???????????????????? ????????????.\"{/color}"

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

    vin "\"????????????, {w=0.5}???????????? ??????????????, ?? ??????????????????, {w=0.5}?????????????????? ???????????????? ???? ???????????????? ?????????????? ?? ????????????.\" {w=0.5}???????????????????? ???????????????? ??????????????."
    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/cough.ogg" fadeout 2.0
    show vic-low-talk-small-flip at vic_pos_2 with Dissolve(0.2)
    vic "\"??????, {w=0.5}??????, ??????...\""

    van "???????????? ??????????????????????."


    show vic-unhappy-small-flip:
        yoffset 20 xoffset -320
        ease 0.2 yoffset 0
    show vic-low-talk-small-flip:
        alpha 0
    show vic-normal-small-flip:
        alpha 0

    van "???? ???????????? ???????????? ???? ?????????????????? ???????? ??, {w=0.5}???????? ???? ??????????, {w=0.5}?????????????????????????? ???????????? ??????????????."

    show vic-low-talk-small-flip:
        alpha 1
    hide vic-unhappy-small-flip with Dissolve(0.2)

    vic "\"?????? ??, {w=0.5}?????????? ?????? ?????????????? ??????????????????????. {w=0.5}???????????? ?? ???????????????? ?? ???????? ??????????????????????.\""

    vic "\"??????????????, {w=0.5}???? ???????????? ???? ???????????? ???? ???????? ?? ???????? ???????????? ??????????????? {w=0.7}?? ?????????? ?????????????? ???????? ?????????????????????????? ?? ??????????, {w=0.5}?????? ?????????????? [name!t].\""

    show vic-normal-small-flip:
        alpha 1
    hide vic-low-talk-small-flip with Dissolve(0.2)
    $ renpy.pause(0.01, hard=True)
    show vic-normal-small-flip:
        linear 0.3 xoffset -1000
    $ renpy.pause(1.0, hard=True)
    hide vic-normal-small-flip


    van "???????????? ?????????????? ??????????????."

    window hide

    stop music fadeout 4.0

    $ renpy.pause(0.1, hard='True')
    scene black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(2.0, hard='True')

    van "?????????? ?????????? ?????????????? ?????????? ?????? ???????????????????? ?? ???????????????? ??????????????."

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/hallway door.ogg"

    pause 2.0

    van "?? ?????????????????????????? ??????, {w=0.5}?? ?????????? ?????????????????? ?? ???????? ??????????????, {w=0.5}?????????? ?????????????? ??????????????????."

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

    van "???????? ?????????? ????????????????, {w=0.5}?????????? ?? ?????????? ???????????? ?? ?????????? ??????????????, {w=0.5}?? ?????? ?????????? ???? ??????????????????."

    van "?? ???????????????????? ???????????? ?? ??????, {w=0.5}?????? ???????????? ?????? ????????????-"

    van "?????????????????? ???????????????? ???? G4, {w=0.5}?????????????? ???? ?????????????????? ??????????????..."

    van "?? ???????????????????????? {color=#f00}???????????????????? ????????????{/color}."


    show hold_card_bg
    show hold_card onlayer inyourface:
        xalign 0.5 yalign 0.5
    show hold_card_2 onlayer inyourface:
        alpha 0 xalign 0.5 yalign 0.5
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard='True')

    van "?? ?????????????? ???? ?????????????? ???????????????? ?? ?????????????????????? ?????????????????????? ???? ?????? ?????????? ????????."

    van "?????????? ?? ???????????????? ?????? ?????????????? ?? ?????????????? ?????????????????"

    van "?????????? ?????????????????? ?? ???????? ?? ???????????????????? ????????????? "

    van "......"

    van "???????? ???????? ???????? ??????????, {w=0.5}?????? ?? ?????????? ???????????????? ??????."

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

    van "{color=#f00}???????? ???????????????????? ????????????.{/color}"

    hide hold_card_2 onlayer inyourface
    scene myers_1
    with Dissolve(1.0)

    pause 1.0

    jump myers_click
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
