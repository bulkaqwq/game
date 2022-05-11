define unacceptable_names = [_("迪诺"), _("dino"), _("дино"), _("吴德者"), _("dino999z"), _("дино999з"), _("文森"), _("埃奇沃思"), _("vincent"), _("винсент"), _("edgeworth"), _("эджворт"), _("victor"), _("виктор"), _("维克多"), _("blake"), _("блэйк"), _("布莱克"), _("德拉克"), _("draco"), _("драко"), _("薇诺拉"), _("vanora"), _("ванора"), _("claude"), _("клод"), _("克洛德"), _("zalmona"), _("залмона"), _("佐莫娜"), _("winston"), _("винстон"), _("温斯顿"), _("myers"), _("майерс"), _("梅尔斯"), _("m先生"), _("emanon"), _("эманон"), _("埃曼诺")]

define select_chapter = False
define select_chapter_2 = False
define select_chapter_3 = False
define select_chapter_4 = False
define route_2_available = False

screen chapter_select():
    tag menu


    use game_menu(_("{size=-5}ГЛАВЫ{/size}")):

        text _("Глава 1") xpos 55 ypos 30 style_prefix "about"
        text _("Глава 2") xpos 343 ypos 30 style_prefix "about"
        text _("Глава 3") xpos 628 ypos 30 style_prefix "about"
        text _("Глава 4") xpos 55 ypos 245 style_prefix "about"
        text _("Глава 5") xpos 343 ypos 245 style_prefix "about"
        text _("Глава 6") xpos 628 ypos 245 style_prefix "about"

        imagebutton:
            xpos 45
            ypos 70
            idle "gui/chapter select/chapter 1 slot idle.png"
            hover "gui/chapter select/chapter 1 slot hover.png"
            focus_mask "gui/chapter select/chapter slot.png"
            action [Play("click2", "music/Click To Start.ogg"), Start()]

        imagebutton:
            xpos 333
            ypos 70
            idle "gui/chapter select/chapter 2 slot idle.png"
            hover "gui/chapter select/chapter 2 slot hover.png"
            focus_mask "gui/chapter select/chapter slot.png"
            action [Play("click2", "music/Click To Start.ogg"), SetVariable("select_chapter", True), SetVariable("select_chapter_2", True), Start()]

        imagebutton:
            xpos 618
            ypos 70
            idle "gui/chapter select/chapter 3 slot idle.png"
            hover "gui/chapter select/chapter 3 slot hover.png"
            focus_mask "gui/chapter select/chapter slot.png"
            action [Play("click2", "music/Click To Start.ogg"), SetVariable("select_chapter", True), SetVariable("select_chapter_3", True), Start()]

        imagebutton:
            xpos 45
            ypos 285
            idle "gui/chapter select/chapter 4 slot idle.png"
            hover "gui/chapter select/chapter 4 slot hover.png"
            focus_mask "gui/chapter select/chapter slot.png"
            action [Play("click2", "music/Click To Start.ogg"), SetVariable("select_chapter", True), SetVariable("select_chapter_4", True), Start()]

        imagebutton:
            xpos 333
            ypos 285
            idle "gui/chapter select/chapter slot coming soon.png"
            hover "gui/chapter select/chapter slot coming soon.png"
            focus_mask "gui/chapter select/chapter slot coming soon.png"
            action NullAction()

        imagebutton:
            xpos 618
            ypos 285
            idle "gui/chapter select/chapter slot coming soon.png"
            hover "gui/chapter select/chapter slot coming soon.png"
            focus_mask "gui/chapter select/chapter slot coming soon.png"
            action NullAction()

label chapter_select_prep:

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False

    $ renpy.pause(2.0, hard='True')

    window show

label chapter_reenter_name:

    python:
        name = renpy.input(_("Введите имя: "), pixel_width = 140)
        name = name.strip()

        if not name:
            name = _("Валерия")

        for x in range(0, len(unacceptable_names)):
            if name.lower().replace(" ", "") == unacceptable_names[x]:
                renpy.jump("chapter_name_unacceptable")

    menu:
        van "Меня зовут [name!t]?"
        "Да":
            jump finish_chapter_enter_name
        "Нет":
            jump chapter_reenter_name

label chapter_name_unacceptable:

    noname "Пожалуйста, введите допустимое имя."

    jump chapter_reenter_name

label finish_chapter_enter_name:

    noname "С возвращением, {w=0.5}[name!t]."

    $ _skipping = True

    window hide

    if select_chapter_2:
        $ select_chapter_2 = False
        jump chapter_2
    elif select_chapter_3:
        $ select_chapter_3 = False
        jump route1_start
    elif select_chapter_4:
        $ select_chapter_4 = False
        jump college_start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
