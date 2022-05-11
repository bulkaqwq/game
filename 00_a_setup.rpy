
init python:
    config.layers = [ 'master', 'transient', 'overlay', 'tvsignal', 'screens']

init -2:
    style say_dialogue:
        line_spacing 10


screen countdown_(timer_range, timer_jump, timer_yalign):
    default end_time = time.time() + timer_range
    default current_time = time.time()
    timer 0.05 repeat True action If(
        current_time < end_time,
        true=SetScreenVariable('current_time', time.time()),
        false=[Hide('countdown_'), Jump(timer_jump)]
    )

    bar value (end_time-current_time)*100 range timer_range*100 xalign 0.5 yalign timer_yalign xmaximum 300 at notify_appear
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
