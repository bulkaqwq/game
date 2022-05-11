


define black_textbox = Image("gui/textbox2.png")

define horror_textbox = Image("gui/textbox3.png")

define noname = Character("", callback=beep, who_color = "#43464f",ctc="ctc_blink", ctc_position="nestled", what_size=27, what_outlines=[(2, "#000000", 0, 0,)])
define noname_message = Character("", callback=beep_2, who_color = "#43464f",ctc="ctc_blink_2", ctc_position="nestled", what_size=27, what_outlines=[(2, "#000000", 0, 0,)])
define noname_warning_1 = Character("", callback=beep_2, who_color = "#43464f",ctc="ctc_blink_2", ctc_position="nestled", window_background=black_textbox, window_xalign=0.5,
                            window_yalign=0.47, what_xalign=0.5, what_text_align=0.52, what_font="VHS.TTF", what_line_spacing=10, what_size=29)
define noname_warning_2 = Character("", callback=beep_2, who_color = "#43464f",ctc="ctc_blink_2", ctc_position="nestled", window_background=black_textbox, window_xalign=0.5,
                            window_yalign=0.3, what_xanchor=0, what_xpos=300, what_text_align=0, what_font="VHS.TTF", what_line_spacing=10, what_size=30)
define noname_warning_3 = Character("", callback=beep_2, who_color = "#43464f",ctc="ctc_blink_2", ctc_position="nestled", window_background=black_textbox, window_xalign=0.5,
                            window_yalign=0.5, what_xalign=0.50, what_text_align=0.50, what_font="VHS.TTF", what_line_spacing=10, what_size=30)
define noname_email = Character("", callback=beep_2, who_color = "#43464f",ctc="ctc_blink_2", ctc_position="nestled", window_background=black_textbox, window_xalign=0.5,
                            window_yalign=0.46, what_xanchor=0, what_xpos=480, what_text_align=0, what_font="VHS.TTF", what_line_spacing=10, what_size=30)
define noname_email_2 = Character("", callback=beep_2, who_color = "#43464f",ctc="ctc_blink_2", ctc_position="nestled", window_background=black_textbox, window_xalign=0.5,
                            window_yalign=0.45, what_xalign=0.505, what_text_align=0, what_font="VHS.TTF", what_line_spacing=10, what_size=30)
define noname_enter = Character("", callback=beep_2, who_color = "#43464f",ctc="ctc_blink_2", ctc_position="nestled", window_background=black_textbox, window_xalign=0.5,
                            window_yalign=0.37, what_xalign=0.5, what_text_align=0.5, what_font="VHS.TTF", what_line_spacing=10, what_size=30)
define noname_enter_silent = Character("", who_color = "#43464f",ctc="ctc_blink_2", ctc_position="nestled", window_background=black_textbox, window_xalign=0.5,
                            window_yalign=0.37, what_xalign=0.5, what_text_align=0.5, what_font="VHS.TTF", what_line_spacing=10, what_size=30)
define noname_proto = Character("", callback=beep_2, who_color = "#43464f",ctc="ctc_blink", ctc_position="nestled", window_background=black_textbox, window_xalign=0.5,
                            window_yalign=0.5, what_xalign=0.52, what_text_align=0.52, what_font="VHS.TTF", what_line_spacing=10, what_size=30, what_outlines=[(2, "#000000", 0, 0,)])
define noname_proto_3 = Character("", callback=beep, who_color = "#43464f",ctc="ctc_blink", ctc_position="nestled", window_background=black_textbox, window_xalign=0.5,
                            window_yalign=0.5, what_xalign=0.52, what_text_align=0.52, what_font="VHS.TTF", what_line_spacing=10, what_size=30, what_outlines=[(2, "#000000", 0, 0,)])
define noname_proto_2 = Character("", callback=beep_2, who_color = "#43464f",ctc="ctc_blink", ctc_position="nestled", window_background=black_textbox,what_ypos = 0.0, what_xpos = 0.52, what_xalign=0.5, what_text_align=0.5, what_font="VHS.TTF", what_line_spacing=10, what_size=30, what_outlines=[(2, "#000000", 0, 0,)])
define noname_horror = Character("", callback=beep, who_color = "#43464f",ctc="ctc_blink", ctc_position="nestled", window_background=horror_textbox, what_ypos = 0.30, what_size=27, what_outlines=[(2, "#000000", 0, 0,)])
define noname_vertical = Character("", callback=beep, who_color = "#43464f",ctc="ctc_blink", ctc_position="nestled", window_background=black_textbox, window_ypos=0.87, window_xpos=0.4, what_size=27, what_outlines=[(2, "#000000", 0, 0,)])
define noname_mono = Character("", callback=beep_2, who_color = "#43464f",ctc="ctc_blink", ctc_position="nestled", window_background=black_textbox, window_xalign=0.5,
                            window_yalign=0.5, what_xalign=0.52, what_text_align=0.52, what_font="pixel.TTF", what_outlines=[(1, "#000000", 0, 0,)])
define anon = Character("???", callback=beep, who_color = "#2e2d2d",ctc="ctc_blink", ctc_position="nestled", what_size=27, what_outlines=[(2, "#000000", 0, 0,)])
define vic = Character(_("Виктор"), callback=beep, who_color = "#2e2d2d",ctc="ctc_blink", ctc_position="nestled", what_size=27, what_outlines=[(2, "#000000", 0, 0,)])
define vin = Character(_("Винсент"), callback=beep, who_color = "#2e2d2d",ctc="ctc_blink", ctc_position="nestled", what_size=27, what_outlines=[(2, "#000000", 0, 0,)])
define cyb_vin = Character(_("В?ин?се?нт"), callback=beep_3, who_color = "#2e2d2d",ctc="ctc_blink", ctc_position="nestled", what_size=27, what_outlines=[(2, "#000000", 0, 0,)])
define vin_vertical_1 = Character(_("Винсент"), who_color = "#2e2d2d", callback=beep, who_xpos = -8.0, who_font = "pixel.ttf", ctc="ctc_blink", ctc_position="nestled", window_background=black_textbox, window_ypos=0.87, window_xpos=0.4, what_outlines=[(1, "#000000", 0, 0,)], who_outlines=[(1, "#000000", 0, 0,)], window_right_padding=1000, what_size=27)
define vin_vertical_2 = Character(_("Винсент"), who_color = "#2e2d2d", callback=beep, who_xpos = 8.0, who_font = "pixel.ttf", ctc="ctc_blink", ctc_position="nestled", window_background=black_textbox, window_ypos=0.3, window_xpos=0.995, what_outlines=[(1, "#000000", 0, 0,)], who_outlines=[(1, "#000000", 0, 0,)], window_right_padding=1000, what_size=27)
define cyb_vin_vertical_1 = Character(_("В?ин?се?нт"), who_color = "#2e2d2d", callback=beep_3, who_xpos = -8.0, who_font = "pixel.ttf", ctc="ctc_blink", ctc_position="nestled", window_background=black_textbox, window_ypos=0.87, window_xpos=0.4, what_outlines=[(1, "#000000", 0, 0,)], who_outlines=[(1, "#000000", 0, 0,)], window_right_padding=1000, what_size=27)
define cyb_vin_vertical_2 = Character(_("В?ин?се?нт"), who_color = "#2e2d2d", callback=beep_3, who_xpos = 8.0, who_font = "pixel.ttf", ctc="ctc_blink", ctc_position="nestled", window_background=black_textbox, window_ypos=0.3, window_xpos=0.995, what_outlines=[(1, "#000000", 0, 0,)], who_outlines=[(1, "#000000", 0, 0,)], window_right_padding=1000, what_size=27)
define van = Character("[name!t]", callback=beep, who_color = "#2e2d2d",ctc="ctc_blink", ctc_position="nestled", what_size=27, what_outlines=[(2, "#000000", 0, 0,)])
define dino = Character(_("Дино"), callback=beep, who_color = "#2e2d2d",ctc="ctc_blink", ctc_position="nestled", what_size=27, what_outlines=[(2, "#000000", 0, 0,)])
define john = Character(_("Джон"), callback=beep, who_color = "#2e2d2d",ctc="ctc_blink", ctc_position="nestled", what_size=27, what_outlines=[(2, "#000000", 0, 0,)])
define e1 = Character(_("Сотрудник 1"), callback=beep, who_color = "#2e2d2d",ctc="ctc_blink", ctc_position="nestled", what_size=27, what_outlines=[(2, "#000000", 0, 0,)])
define e2 = Character(_("Сотрудник 2"), callback=beep, who_color = "#2e2d2d",ctc="ctc_blink", ctc_position="nestled", what_size=27, what_outlines=[(2, "#000000", 0, 0,)])
define dra = Character(_("Драко"), callback=beep, who_color = "#2e2d2d",ctc="ctc_blink", ctc_position="nestled", what_size=27, what_outlines=[(2, "#000000", 0, 0,)])
define cyb_dra = Character(_("Д?р?а?к?о"), callback=beep_3, who_color = "#2e2d2d",ctc="ctc_blink", ctc_position="nestled", what_size=27, what_outlines=[(2, "#000000", 0, 0,)])
define radio = Character(_("Громкая связь"), callback=beep, who_color = "#2e2d2d", what_color = "#f00", ctc="ctc_blink", ctc_position="nestled", what_size=27, what_outlines=[(2, "#000000", 0, 0,)])
define radio2 = Character(_("Магнитофон"), callback=beep, who_color = "#2e2d2d", what_color = "#f00", ctc="ctc_blink", ctc_position="nestled", what_size=27, what_outlines=[(2, "#000000", 0, 0,)])
define win = Character(_("Винстон"), callback=beep, who_color = "#2e2d2d",ctc="ctc_blink", ctc_position="nestled", what_size=27, what_outlines=[(2, "#000000", 0, 0,)])
define zal = Character(_("Залмона"), callback=beep, who_color = "#2e2d2d",ctc="ctc_blink", ctc_position="nestled", what_size=27, what_outlines=[(2, "#000000", 0, 0,)])
define n1 = Character(_("Сосед 1"), callback=beep, who_color = "#2e2d2d",ctc="ctc_blink", ctc_position="nestled", what_size=27, what_outlines=[(2, "#000000", 0, 0,)])
define n2 = Character(_("Сосед 2"), callback=beep, who_color = "#2e2d2d",ctc="ctc_blink", ctc_position="nestled", what_size=27, what_outlines=[(2, "#000000", 0, 0,)])
define n3 = Character(_("Сосед 3"), callback=beep, who_color = "#2e2d2d",ctc="ctc_blink", ctc_position="nestled", what_size=27, what_outlines=[(2, "#000000", 0, 0,)])
define m = Character("???", callback=beep, who_color = "#2e2d2d",what_color = "#f00", ctc="ctc_blink", ctc_position="nestled", what_size=27, what_outlines=[(2, "#000000", 0, 0,)])
define claude = Character(_("[claude_name!t]"), callback=beep, who_color = "#2e2d2d",ctc="ctc_blink", ctc_position="nestled", what_size=27, what_outlines=[(2, "#000000", 0, 0,)])
define v = Character(_("Ванора"), callback=beep, who_color = "#2e2d2d",ctc="ctc_blink", ctc_position="nestled", what_size=27, what_outlines=[(2, "#000000", 0, 0,)])
define b = Character(_("Книга"), callback=beep, who_color = "#2e2d2d",ctc="ctc_blink", ctc_position="nestled", what_size=27, what_outlines=[(2, "#000000", 0, 0,)])
define c = Character(_("Киборг"), callback=beep, who_color = "#2e2d2d",ctc="ctc_blink", ctc_position="nestled", what_size=27, what_outlines=[(2, "#000000", 0, 0,)])


define diary = Character("", callback=beep, kind=nvl, who_color = "#ffffff", what_color = "#ffffff", ctc="ctc_blink", ctc_position="nestled", what_font="VHS.TTF", what_size = 28, what_line_spacing = 5, what_outlines=[(1, "#000000", 0, 0,)])
define nvl_text = Character("", kind=nvl, who_color = "#ffffff", what_color = "#ffffff", ctc="ctc_blink", ctc_position="nestled", what_font="VHS.TTF", what_size = 28, what_line_spacing = 5, what_outlines=[(1, "#000000", 0, 0,)])
define comp = Character("", callback=beep_2, kind=nvl, who_color = "#ffffff", what_color = "#ffffff", ctc="ctc_blink", ctc_position="nestled", what_font="VHS.TTF", what_size = 28, what_line_spacing = 5, what_outlines=[(1, "#000000", 0, 0,)])

define vic_pos = Position(xpos=0.55, ypos=1.0)
define vic_pos_2 = Position(xpos=0.25, ypos=1.0)
define vic_pos_temp = Position(xpos=0.45, ypos=1.0)
define vic_pos_3 = Position(xpos=0.18, ypos=1.0)


define vin_pos_2 = Position(xpos=0.73, ypos=1.0)
define vin_pos_3 = Position(xpos=0.78, ypos=1.0)

define zal_pos_2 = Position(xpos=0.70, ypos=1.0)

define dra_pos_1 = Position(xpos=0.68, ypos=1.0)
define dra_pos_2 = Position(xpos=0.73, ypos=1.0)

define van_pos_1 = Position(xpos=0.25, ypos=1.0)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
