




















init -1500 python:





    _("Self-voicing disabled.")
    _("Clipboard voicing enabled. ")
    _("Self-voicing enabled. ")

    _("bar")
    _("selected")
    _("viewport")
    _("horizontal scroll")
    _("vertical scroll")
    _("activate")
    _("deactivate")
    _("increase")
    _("decrease")



    config.descriptive_text_character = None

    def alt(what, interact=True):
        """
        Uses the narrator to speak `what` if self-voicing is enabled.
        """
        
        if _preferences.self_voicing:
            
            c = config.descriptive_text_character
            
            if c is None:
                c = narrator
            
            return c(what, interact=interact)


    sv = alt


init -1500 python hide:




    store._m1_00_accessibility__opendyslexic = { }

    def opendyslexic(f):
        
        rv = store._m1_00_accessibility__opendyslexic.get(f, None)
        if rv is not None:
            return rv
        
        
        charset = "20-7e a0-107 10a-113 116-11b 11e-123 126-12b 12e-133 136-137 139-148 14a-14d 150-15b 15e-16b 16e-17e 186 188-189 18e-192 194 197 19d 1a0-1a1 1a9 1ac 1af-1b4 1c0-1c3 1cd-1df 1e6-1e7 1fe-1ff 218-21b 228-22b 241-244 24b-24c 250-254 256-259 25b-25c 261-262 265 268 26a-26b 26f-270 272 274-276 279-27a 280-281 283 289-28a 28c-28f 294-295 298-299 29b-29c 29f 2a1-2a2 2c6-2c7 2d8-2dd 309 31b 323 326 32d 331 3b2 3b8 3c0 3c7 401 403 405-408 40c 40e 410 412 415 418 41c-41e 420-422 425 427 42f-430 432 435 437 439 43e 440-441 443 445 44f 451 453 455-458 45b-45c 45e 472 498-499 4ae 4b1 4c0 4d0 4d2-4df 4e2-4f5 4f8-4f9 1e04-1e05 1e0c-1e0f 1e12-1e13 1e24-1e25 1e2e-1e2f 1e36-1e37 1e3c-1e3f 1e44-1e47 1e4a-1e4d 1e50-1e53 1e62-1e63 1e6c-1e71 1e80-1e85 1e92-1e93 1ea0-1ef9 2013-2014 2018-201a 201c-201e 2020-2022 2026 2030 2039-203a 203d 2044 20ac 2122 2126 215b-215e 2202 2206 220f 2211-2212 2219-221a 221e 222b 2248 2260 2264-2265 25ca 2c64 2c6d 2c72-2c73 2e18 fb01-fb02"
        
        rv = FontGroup()
        
        for r in charset.split():
            start, _, end = r.partition("-")
            start = int(start, 16)
            end = int(end, 16) if end else start
            
            rv.add("_OpenDyslexic3-Regular.ttf", start, end)
        
        rv.add(f, None, None)
        
        store._m1_00_accessibility__opendyslexic[f] = rv
        return rv

    config.font_transforms["opendyslexic"] = opendyslexic

    config.ftfont_scale["_OpenDyslexic3-Regular.ttf"] = .87
    config.ftfont_vertical_extent_scale["_OpenDyslexic3-Regular.ttf"] = .66

    def dejavusans(f):
        return "DejaVuSans.ttf"

    config.font_transforms["dejavusans"] = dejavusans

screen _accessibility_new():


    on "show" action Function(clack_play)
    key "shift_K_a" action ToggleScreen("_accessibility_new")

    zorder 2000
    modal True

    frame:
        style_group ""

        has side "c b":
            spacing gui._scale(10)
            xfill True
            yfill True

        fixed:

            viewport:
                scrollbars "vertical"
                mousewheel True

                has grid 2 1:
                    xfill True
                    spacing 20

                vbox:

                    label _("Font Override")


                    null height 10

                    textbutton _("Default"):

                        action Preference("font transform", None)
                        style_suffix "radio_button"

                    textbutton _("DejaVu Sans"):
                        action Preference("font transform", "dejavusans")
                        style_suffix "radio_button"

                    textbutton _("Opendyslexic"):
                        action Preference("font transform", "opendyslexic")
                        style_suffix "radio_button"

                    null height 10

                    label _("Text Size Scaling")


                    null height 10

                    bar value Preference("font size")

                    textbutton _("Reset"):

                        action Preference("font size", 1.0)

                    null height 10

                    label _("Line Spacing Scaling")


                    null height 10

                    bar value Preference("font line spacing")

                    textbutton _("Reset"):

                        action Preference("font line spacing", 1.0)


                vbox:

                    label _("Self-Voicing")


                    null height 10

                    textbutton _("Off"):

                        action Preference("self voicing", "disable")
                        style_suffix "radio_button"

                    textbutton _("Text-to-speech"):

                        action Preference("self voicing", "enable")
                        style_suffix "radio_button"

                    textbutton _("Clipboard"):

                        action Preference("clipboard voicing", "enable")
                        style_suffix "radio_button"

                    textbutton _("Debug"):
                        action Preference("debug voicing", "enable")
                        style_suffix "radio_button"

        vbox:

            text _("The options on this menu are intended to improve accessibility. They may not work with all games, and some combinations of options may render the game unplayable. This is not an issue with the game or engine. For the best results when changing fonts, try to keep the text size the same as it originally was.")


            hbox:
                spacing gui._scale(25)

                textbutton _("Return"):
                    action Hide("_accessibility_new")
                    yalign 1.0

screen keymap_accessibility():

    key "shift_K_a" action ToggleScreen("_accessibility_new")

    key "K_TAB" action Skip()

    key "keydown_K_LCTRL" action Skip()

    key "keydown_K_RCTRL" action Skip()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
