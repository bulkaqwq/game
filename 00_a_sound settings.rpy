
init -1 python:
    renpy.music.register_channel("sound1", "sfx", True)
    renpy.music.register_channel("beep", "voice", True)
    renpy.music.register_channel("electricity", "sfx", True)
    renpy.music.register_channel("investigation_SE", "sfx", True)
    renpy.music.register_channel("robot memory", "sfx", False)
    renpy.music.register_channel("background noise", "sfx", True)
    renpy.music.register_channel("char name", "sfx", loop = False)
    renpy.music.register_channel("vhs", "sfx", True)
    renpy.music.register_channel("main_title_gate", "sfx", True)
    renpy.music.register_channel("sfx1", "sfx", loop = False)
    renpy.music.register_channel("sfx2", "sfx", loop = False)
    renpy.music.register_channel("sfx3_new", "sfx", loop = False)
    renpy.music.register_channel("UI Dark", "sfx", loop = False)

    def clack_play(on=False):
        if on:
            renpy.music.set_volume(0.8, delay=0, channel='beep')
            renpy.music.play("music/SingleBeep.ogg", channel="beep", loop=True)
        else:
            renpy.music.stop(channel="beep", fadeout = 0.5)

    def beep(event, **kwargs):
        if event == "show" or event == "begin":
            clack_play(True)
        
        if event == "slow_done":
            clack_play(False)



    def clack_play_2(on=False):
        if on:
            renpy.music.set_volume(0.8, delay=0, channel='beep')
            renpy.music.play("music/computer beep.ogg", channel="beep", loop=True)
        else:
            renpy.music.stop(channel="beep", fadeout = 0.5)

    def beep_2(event, **kwargs):
        if event == "show" or event == "begin":
            clack_play_2(True)
        if event == "slow_done":
            clack_play_2(False)


    def clack_play_3(on=False):
        if on:
            renpy.music.set_volume(0.4, delay=0, channel='beep')
            renpy.music.play("music/cyborg clack.ogg", channel="beep", loop=True)
        else:
            renpy.music.stop(channel="beep", fadeout = 0.5)

    def beep_3(event, **kwargs):
        if event == "show" or event == "begin":
            clack_play_3(True)
        if event == "slow_done":
            clack_play_3(False)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
