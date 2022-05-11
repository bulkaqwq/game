label to_be_continued:

    $ renpy.pause(2.0, hard='True')

    show to_be_continued
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(4.0, hard='True')

    hide to_be_continued
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    show demo_end_text
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(5.0, hard='True')

    show warning_click_to_continue_animation:
        yoffset 110

    call screen end_click_to_continue
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
