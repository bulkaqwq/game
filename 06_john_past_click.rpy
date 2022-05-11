
image john_past_discord:
    contains:
        "images/john past/discord.png"
    contains:
        "images/john past/discord_cursor.png"
        alpha 0
        pause 0.5
        alpha 1
        pause 0.5
        repeat

screen john_past_tabletop:

    imagebutton:
        xpos 165
        ypos 437
        idle "images/john past/card_idle.png"
        hover "images/john past/card_hover.png"
        focus_mask "images/john past/card_hover.png"
        action Jump("john_past_investigate_card")

    imagebutton:
        xpos 362
        ypos 16
        idle "images/john past/computer_idle.png"
        hover "images/john past/computer_hover.png"
        focus_mask "images/john past/computer_hover.png"
        action Jump("john_past_investigate_computer")

    imagebutton:
        xpos 101
        ypos 17
        idle "images/john past/mascot_idle.png"
        hover "images/john past/mascot_hover.png"
        focus_mask "images/john past/mascot_hover.png"
        action Jump("john_past_investigate_mascot")

    imagebutton:
        xpos 993
        ypos 208
        idle "images/john past/calendar-idle.png"
        hover "images/john past/calendar-hover.png"
        focus_mask "images/john past/calendar-hover.png"
        action Jump("john_past_investigate_calendar")

screen john_past_calendar_screen:

    if john_past_calendar_page == 2:
        add "images/john past/february.png"
    elif john_past_calendar_page == 3:
        add "images/john past/march.png"
    elif john_past_calendar_page == 4:
        add "images/john past/april.png"

    imagebutton:
        xpos 110
        ypos 208
        idle "images/john past/arrow_left_idle.png"
        hover "images/john past/arrow_left_hover.png"
        focus_mask "images/john past/arrow_left_idle.png"
        action Jump("john_past_calendar_flip_left")

    imagebutton:
        xpos 1050
        ypos 208
        idle "images/john past/arrow_right_idle.png"
        hover "images/john past/arrow_right_hover.png"
        focus_mask "images/john past/arrow_right_idle.png"
        action Jump("john_past_calendar_flip_right")

    imagebutton:
        xpos 520
        ypos 610
        idle "images/john past/arrow_down_idle.png"
        hover "images/john past/arrow_down_hover.png"
        focus_mask "images/john past/arrow_down_idle.png"
        action Jump("john_past_calendar_leave")

label john_past_investigate_card:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show john_past_desktop at Position(xpos = 0, ypos = 0)

    show john_past_desktop:
        ease 0.5 zoom 2.5 xoffset 900 yoffset 250

    $ renpy.pause(0.5, hard='True')

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    john "A little post-it note. {w=0.5}There are two pieces of candy next to it."

    $ rollback_ = True

    noname "\"To John: {w=0.5}Welcome to Myers Corporation!\""

    noname "\"To celebrate your joining, {w=0.5}we have a very special gift for you...\""

    noname "\"That is the figurine of Myers Corporation's mascot, {w=0.5}Myer-chan!\""

    noname "\"Very lovely, {w=0.5}isn't it? {w=0.5}Ha-ha...\""

    noname "\"Anyways, {w=0.5}we hope you'll enjoy your time at Myers Corporation!\""

    noname "\"—Myers Investment Department 2081.4\""

    show john_past_desktop:
        ease 0.5 zoom 1 xoffset 0 yoffset 0
    $ renpy.pause(0.5, hard='True')

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    hide john_past_desktop
    scene john_past_desktop

    $ renpy.block_rollback()
    $ _rollback = False

    call screen john_past_tabletop

label john_past_investigate_computer:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show john_past_desktop at Position(xpos = 0, ypos = 0)

    show john_past_desktop:
        ease 0.5 zoom 1.25 xoffset 0 yoffset 165

    $ renpy.pause(0.5, hard='True')

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    john "A computer. {w=0.5}I need to use it to finish my work."

    stop music fadeout 5.0
    $ renpy.music.stop(channel="background noise", fadeout = 5.0)

    $ rollback_ = True

    $ renpy.music.set_volume(0.4, delay=0, channel='sound')
    play sound "music/John Past/discord.ogg"

    show transparent dark-small:
        alpha 0.8
    show john_past_discord
    with Dissolve(0.5)

    $ renpy.pause(0.1, hard='True')
    pause 1.0

    window show

    john "Huh? {w=0.5}What's this...?"

    john "Looks like the last employee sitting here forgot to quit his group chat account."

    window hide

    $ renpy.music.set_volume(0.1, delay=0, channel='music')
    play music ("music/chapter2-haunting.ogg")

    pause 1.0

    window show

    noname_message "\"Member 1: {w=0.5}Hey hey, {w=0.5}have you heard?\""

    noname_message "\"Member 1: {w=0.5}{color=#f00}Winston Loomis {/color}was the one behind the G4 Cyborg Incident! {w=0.5}He got a life sentence.\""

    noname_message "\"Member 2: {w=0.5}Winston? {w=0.5}You mean the one who {color=#f00}always wears shades, {w=0.5}doesn't say a word, {w=0.5}and has a bit of a hunched back{/color}?\""

    noname_message "\"Member 2: {w=0.5}That's so unexpected. {w=0.5}It's true that he doesn't really have any friends, {w=0.5}but he doesn't seem like a bad person either.\""

    noname_message "\"Member 3: {w=0.5}I disagree. {w=0.5}This guy has always seemed kinda suspicious. {w=0.5}I feel uncomfortable every time I see him.\""

    noname_message "\"Me: {w=0.5}Is Winston really the mastermind of G4 Cyborg Incident? {w=0.5}Something doesn't add up.\""

    noname_message "\"Member 1: {w=0.5}Huh? {w=0.5}What do you mean?\""

    noname_message "\"Me: {w=0.5}How should I put this... {w=0.5}this guy {color=#f00}doesn't really seem like the type that could drag that many people into the basement to experiment on them.{/color}\""

    noname_message "\"Member 2: {w=0.5}Maybe he had helpers. {w=0.5}Who knows.\""

    noname_message "\"Me: {w=0.5}That's not what I'm saying. {w=0.5}You see, {w=0.5}this guy doesn't speak much, {w=0.5}and hardly has any friends at Myers.\""

    noname_message "\"Me: {w=0.5}In that case, {w=0.5}wouldn't he be the best person to {color=#f00}pin everything on{/color}?\""

    noname_message "\"Member 1: {w=0.5}......\""

    noname_message "\"Member 2: {w=0.5}......\""

    noname_message "\"Member 3: {w=0.5}......{w=0.5}Hey, {w=0.5}what the hell are you thinking. {w=0.5}You'll be targeted by the company for saying that.\""

    stop music fadeout 8.0

    noname_message "\"Me: {w=0.5}Huh? {w=0.5}This, {w=0.5}this is just a random thought, {w=0.5}ha-ha...\""

    noname_message "\"Member 2: {w=0.5}Anyways, {w=0.5}let's change the subject to something more uplifting.\""

    noname_message "\"Member 2: {w=0.5}I heard that if everything goes well, {w=0.5}the company will {color=#f00}host a party after all of this{/color}.\""

    noname_message "\"Member 1: {w=0.5}I'm sure it will go well. {w=0.5}After all, {w=0.5}{color=#f00}we have Vincent{/color}.\""

    noname_message "\"Member 3: {w=0.5}Party? {w=0.5}When?\""

    noname_message "\"Member 2: {w=0.5}Well... {w=0.5}I think on a {color=#f00}Thursday, {w=0.5}two months from now{/color}? {w=0.5}I don't remember the exact date.\""

    noname_message "\"Member 3: {w=0.5}Thursday? {w=0.5}Damn it, {w=0.5}I work overtime every Thursday night.\""

    noname_message "\"Me: {w=0.5}Ha-ha, {w=0.5}I know when the party is. {w=0.5}But I can't go either... {w=0.5}because {color=#f00}I will be on a vacation at that time{/color} ^ _ ^\""

    noname_message "\"Member 1: {w=0.5}Eh? {w=0.5}Vacation? {w=0.5}That sounds nice!\""

    noname_message "\"Me: {w=0.5}I'm pretty excited about it too. {w=0.5}I haven't been in touch with my parents for a long time.\""

    noname_message "\"Member 1: {w=0.5}However... {w=0.5}I'm drooling at the thought of getting close to Victor at the party~\""

    noname_message "\"Member 3: {w=0.5}...You bastard...\""

    window hide

    hide transparent dark-small
    hide john_past_discord
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    pause 1.0

    window show

    john "Hmm... {w=0.5}Speaking of that, {w=0.5}I did hear that Myers is having a party in a few days."

    john "But this is strange.{w=0.5} If the employee sitting here is just on vacation, {w=0.5}why would the company let me take over his desk?"

    window hide

    show john_past_desktop:
        ease 0.5 zoom 1 xoffset 0 yoffset 0

    $ renpy.pause(0.5, hard='True')

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    hide john_past_desktop
    scene john_past_desktop

    $ renpy.block_rollback()
    $ _rollback = False

    $ renpy.music.set_volume(0.5, delay=0, channel='music')
    play music ("music/bgm/jazz-lounge.ogg")

    $ renpy.music.set_volume(0.5, delay=0, channel='background noise')
    $ renpy.music.play("music/John Past/office background.ogg", channel="background noise", loop=True)

    call screen john_past_tabletop

label john_past_investigate_calendar:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    show john_past_desktop at Position(xpos = 0, ypos = 0)

    show john_past_desktop:
        ease 0.5 zoom 2.0 xoffset -600 yoffset 400

    $ renpy.pause(0.1, hard='True')

    if not john_past_check_calendar:

        $ john_past_check_calendar = True

        $ renpy.pause(0.5, hard='True')

        $ _skipping = True
        $ renpy.block_rollback()
        $ _rollback = True

        john "A calendar. {w=0.5}It may have been left behind by the previous employee."

    show transparent dark-small:
        alpha 0.8
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    call screen john_past_calendar_screen

label john_past_calendar_flip_left:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/John Past/Page_flip.ogg")

    if john_past_calendar_page != 2:
        $ john_past_calendar_page -= 1

    call screen john_past_calendar_screen

label john_past_calendar_flip_right:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/John Past/Page_flip.ogg")

    if john_past_calendar_page != 4:
        $ john_past_calendar_page += 1

    call screen john_past_calendar_screen

label john_past_calendar_leave:

    hide transparent dark-small with Dissolve(0.5)

    show john_past_desktop:
        ease 0.5 zoom 1 xoffset 0 yoffset 0

    $ renpy.pause(0.5, hard='True')

    hide john_past_desktop

    scene john_past_desktop

    $ renpy.block_rollback()
    $ _rollback = False

    call screen john_past_tabletop

label john_past_investigate_mascot:

    if not john_past_check_mascot:

        $ john_past_check_mascot = True

        $ renpy.music.set_volume(1.0, delay=0, channel='sound')
        play sound ("music/zoom.wav")

        show john_past_desktop at Position(xpos = 0, ypos = 0)

        show john_past_desktop:
            ease 0.5 zoom 1.75 xoffset 480 yoffset 450

        $ renpy.pause(0.5, hard='True')

        $ _skipping = True
        $ renpy.block_rollback()
        $ _rollback = True

        john "The mascot of Myers Corporation -{w=0.5} Myer-Chan."

        $ rollback_ = True

        john "While many people are not fond of its look, {w=0.5}it is rumored that Mr. Myers designed it himself, {w=0.5}so no one dares to say anything."

        stop music fadeout 5.0
        $ renpy.music.stop(channel="background noise", fadeout = 5.0)

        $ renpy.music.stop(channel="beep", fadeout = 0.5)

        show john_past_desktop:
            ease 0.5 zoom 1 xoffset 0 yoffset 0

        $ renpy.pause(1.0, hard='True')

        pause 1.0

        hide john_past_desktop

        scene john_past_desktop



        show john_past_desktop_blurred:
            ease 0.4 xoffset -10 yoffset -10 alpha 0.5

            ease 0.4 xoffset 10 yoffset -10 alpha 0.5

            ease 0.4 xoffset -10 yoffset 10 alpha 0.5

            ease 0.4 xoffset 10 yoffset 10 alpha 0.5

            ease 0.4 xoffset 0 yoffset 0 alpha 1.0

        $ renpy.pause(0.1, hard='True')

        $ renpy.music.set_volume(1.0, delay=0, channel='sound')
        play sound "music/heartbeat.ogg"

        show bedroom_headache
        $ renpy.transition(Dissolve(0.4))
        $ renpy.pause(0.4, hard='True')

        hide bedroom_headache
        $ renpy.transition(Dissolve(0.4))
        $ renpy.pause(0.4, hard='True')

        show bedroom_headache
        $ renpy.transition(Dissolve(0.4))
        $ renpy.pause(0.4, hard='True')

        hide bedroom_headache
        $ renpy.transition(Dissolve(0.4))
        $ renpy.pause(0.4, hard='True')

        $ renpy.pause(0.1, hard='True')

        hide john_past_desktop_blurred
        $ renpy.transition(Dissolve(1.0))
        $ renpy.pause(1.0, hard='True')

        pause 1.0

        van "!?"

        scene myers_tunnel_mascot_closeup
        show white back
        $ renpy.transition(Dissolve(0.1))
        $ renpy.pause(0.1, hard='True')

        stop music

        $ renpy.music.set_volume(0.7, delay=0, channel='sound')
        play sound "music/teleport.ogg"

        $ renpy.music.set_volume(1.0, delay=0, channel='robot memory')
        $ renpy.music.play("music/magic teleport.ogg", channel="robot memory", loop=False)

        $ renpy.pause(0.3, hard='True')

        hide white back
        $ renpy.transition(Dissolve(1.0))
        $ renpy.pause(1.0, hard='True')

        jump tunnel_after_john_past
    else:


        scene myers_tunnel_mascot_closeup
        show white back
        $ renpy.transition(Dissolve(0.1))
        $ renpy.pause(0.1, hard='True')

        stop music
        $ renpy.music.stop(channel="background noise", fadeout = 1.0)

        $ renpy.music.set_volume(0.7, delay=0, channel='sound')
        play sound "music/teleport.ogg"

        $ renpy.pause(0.3, hard='True')

        hide white back
        $ renpy.transition(Dissolve(1.0))
        $ renpy.pause(1.0, hard='True')

        $ renpy.music.set_volume(1.0, delay=0, channel='music')
        play music ("music/Tunnel/myersSewers.ogg")

        call screen myers_tunnel_mascot_screen
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
