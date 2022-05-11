












define config.name = _("Винсент: Секрет Майерс")


define config.menu_include_disabled = True




define gui.show_name = False



define config.version = "1.0.0"




define gui.about = _p("""
""")





define build.name = "Vincent_Novel_alpha_ru"








define config.has_sound = True
define config.has_music = True
define config.has_voice = True












define config.main_menu_music = "music/Creepy-Action.ogg"









define config.enter_transition = dissolve
define config.exit_transition = dissolve




define config.intra_transition = dissolve




define config.after_load_transition = None




define config.end_game_transition = None















define config.window = "auto"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)






default preferences.text_cps = 35




default preferences.afm_time = 15














define config.save_directory = "Vincent_Novel_Alpha_1_0_0_En"






define config.window_icon = "gui/window_icon.png"






init python:

















    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpy', None)



    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')
    build.classify('game/images/**.png', 'archive')
    build.classify('game/music/**.ogg', 'archive')
    build.classify('game/music/**.mp3', 'archive')
    build.classify('game/music/**.wav', 'archive')
    build.classify('game/**.ttf', 'archive')
    build.classify('game/**.wav', 'archive')
    build.classify('game/**.ogg', 'archive')
    build.classify('game/**.mp3', 'archive')
    build.classify('game/**.webm', 'archive')
    build.classify('game/**.flac', 'archive')




    build.documentation('*.html')
    build.documentation('*.txt')

















define config.image_cache_size = None


define config.framerate = 60
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
