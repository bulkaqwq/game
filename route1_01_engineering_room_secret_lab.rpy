
image engineering_room_secret_lab_zoom_cyborg_1 = "images/Engineering Room Secret Lab/Engineering_room_secret_lab_zoom_cyborg_1.png"
image engineering_room_secret_lab_zoom_cyborg_2 = "images/Engineering Room Secret Lab/Engineering_room_secret_lab_zoom_cyborg_2.png"

image engineering_room_secret_lab_1 = "images/Engineering Room Secret Lab/Engineering_room_secret_lab_1.png"

image engineering_room_secret_lab:
    contains:
        ConditionSwitch("engineering_room_secret_lab_drain_container_2 == True", "images/Engineering Room Secret Lab/Engineering_room_secret_lab_2.png", "engineering_room_secret_lab_drain_container_2 == False", "images/Engineering Room Secret Lab/Engineering_room_secret_lab_1.png")
    contains:
        "images/transparent dark-small.png"
        alpha 0
        pause 1.0
        linear 2.0 alpha 0.55
        pause 0.2
        linear 1.0 alpha 0.3
        pause 1.0
        linear 0.5 alpha 0
        repeat
    contains:
        "engineering_room_secret_lab_lighting"

image engineering_room_secret_lab_lighting:
    "images/Engineering Room Secret Lab/Engineering_room_secret_lab_lighting.png"
    alpha 0
    ease 1.0 alpha 1
    pause 2.0
    ease 1.0 alpha 0.2
    pause 2.0
    repeat

image engineering_room_secret_lab_monitor_zoom:
    contains:
        "images/Engineering Room Secret Lab/Engineering_room_secret_lab_monitor_base.png"
    contains:
        "engineering_room_secret_lab_monitor_circle_animation"
        xpos 880 ypos 330
    contains:
        "engineering_room_secret_lab_monitor_battery_animation"
        xpos 300 ypos 124

image engineering_room_secret_lab_monitor_circle_animation:
    contains:
        "images/Engineering Room Secret Lab/Engineering_room_secret_lab_monitor_circle_1.png"
        block:
            rotate 0
            linear 3.5 rotate 360
            repeat
    contains:
        "images/Engineering Room Secret Lab/Engineering_room_secret_lab_monitor_circle_2.png"
        block:
            rotate 0
            linear 3.5 rotate -360
            repeat

image engineering_room_secret_lab_monitor_battery_animation:
    "images/Engineering Room Secret Lab/Engineering_room_secret_lab_battery_animation/Engineering_room_secret_lab_battery_1.png"
    0.1
    "images/Engineering Room Secret Lab/Engineering_room_secret_lab_battery_animation/Engineering_room_secret_lab_battery_2.png"
    0.1
    "images/Engineering Room Secret Lab/Engineering_room_secret_lab_battery_animation/Engineering_room_secret_lab_battery_3.png"
    0.1
    "images/Engineering Room Secret Lab/Engineering_room_secret_lab_battery_animation/Engineering_room_secret_lab_battery_4.png"
    0.1
    "images/Engineering Room Secret Lab/Engineering_room_secret_lab_battery_animation/Engineering_room_secret_lab_battery_5.png"
    0.5
    "images/Engineering Room Secret Lab/Engineering_room_secret_lab_battery_animation/Engineering_room_secret_lab_battery_4.png"
    0.1
    "images/Engineering Room Secret Lab/Engineering_room_secret_lab_battery_animation/Engineering_room_secret_lab_battery_3.png"
    0.1
    "images/Engineering Room Secret Lab/Engineering_room_secret_lab_battery_animation/Engineering_room_secret_lab_battery_2.png"
    0.1
    "images/Engineering Room Secret Lab/Engineering_room_secret_lab_battery_animation/Engineering_room_secret_lab_battery_1.png"
    0.05
    repeat

image engineering_room_secret_lab_blackboard = "images/Engineering Room Secret Lab/Engineering_room_secret_lab_blackboard.png"
image engineering_room_secret_lab_monitor_error = "images/Engineering Room Secret Lab/Engineering_room_secret_lab_monitor_error.png"
image engineering_room_secret_lab_monitor_approved = "images/Engineering Room Secret Lab/Engineering_room_secret_lab_monitor_approved.png"
image engineering_room_secret_lab_container_2_zoom = "images/Engineering Room Secret Lab/Engineering_room_secret_lab_container_2_zoom.png"
image engineering_room_secret_lab_device = "images/Engineering Room Secret Lab/Engineering_room_secret_lab_device.png"

label engineering_room_secret_lab_start:

    if not engineering_room_visit_secret_lab:

        $ engineering_room_secret_lab_monitor_num[0] = 0
        $ engineering_room_secret_lab_monitor_num[1] = 0
        $ engineering_room_secret_lab_monitor_num[2] = 0

        $ engineering_room_visit_secret_lab = True
        $ engineering_room_secret_lab_drain_container_2 = False
        $ engineering_room_secret_lab_investigate_blackboard_bool = False
        $ engineering_room_secret_lab_investigate_container_2 = False

        $ _skipping = True

        $ renpy.block_rollback()
        $ _rollback = True

        $ renpy.music.set_volume(1.0, delay=0, channel='sound')
        play sound "music/Click To Start.ogg"

        hide screen inventory_screen
        $ renpy.transition(Dissolve(0.5))
        $ renpy.pause(0.5, hard='True')

        stop music fadeout 6.0

        $ renpy.pause(2.0, hard='True')

        $ renpy.music.set_volume(1.0, delay=0, channel='sound')
        play sound ("music/engineering room/Cupboard_open.ogg")

        $ renpy.pause(2.0, hard='True')

        scene black
        $ renpy.transition(Dissolve(0.3))
        $ renpy.pause(0.5, hard='True')

        pause 2.0

        van "The room behind the door was much darker."

        $ rollback_ = True

        van "My eyes had a hard time adjusting to the sudden darkness."

        pause 1.0

        $ renpy.music.set_volume(1.0, delay=0, channel='sound')
        play sound "music/squish.ogg"

        pause 1.0

        van "......!"

        van "What was that? {w=0.5}I just stepped on some kind of wet, {w=0.5}sticky substance."

        van "I bent down and tried to reach for it, {w=0.5}but my arm was nicked by something sharp."

        van "Ouch. {w=0.5}Are these... {w=0.5}shards of glass?"

        van "That was when I suddenly realized that there was a huge glass chamber standing in front of me."

        van "And inside it, {w=0.5}was..."

        $ renpy.music.set_volume(1.0, delay=0, channel='sound')
        play sound ("music/vin jump.ogg")

        $ renpy.music.set_volume(0.6, delay=0, channel='music')
        play music "music/myers lobby/lobby horror.ogg"

        scene engineering_room_secret_lab_zoom_cyborg_2:
            block:
                ease 2.5 zoom 1.05 xoffset -30 yoffset -35
                ease 2.5 zoom 1 xoffset 0 yoffset 0
                repeat

        show robot1_satan_flash:
            alpha 0.3
            block:
                ease 0.5 alpha 0.2
                pause 1.0
                ease 0.5 alpha 0.3
                pause 1.0
                ease 0.5 alpha 0.4
                pause 1.0
                repeat

        $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 0.5, dist=70))
        $ renpy.pause(0.5, hard='True')

        pause 2.0

        van "!?"

        show character_icon_box:
            xpos 1350 ypos 300
            easein_expo 1.0 xpos 800 ypos 300
        show zalmona_icon_panic:
            xpos 1350 ypos 298
            easein_expo 1.0 xpos 800 ypos 298
            xpos 800 ypos 298

        zal "\"Get back, {w=0.5}get back!\""

        hide character_icon_box
        hide zalmona_icon_panic
        with Dissolve(0.3)

        scene black
        $ renpy.transition(Dissolve(1.0))
        $ renpy.pause(1.0, hard='True')

        pause 0.5

        scene engineering_room_secret_lab
        $ renpy.transition(Dissolve(1.0))
        $ renpy.pause(1.0, hard='True')

        pause 3.0

        show character_icon_box:
            xpos 1350 ypos 300
            easein_expo 1.0 xpos 800 ypos 300
        show zalmona_icon_normal:
            xpos 1350 ypos 298
            easein_expo 1.0 xpos 800 ypos 298
            xpos 800 ypos 298

        zal "\"......\""

        zal "\"Thank god, {w=0.5}it looks like that thing is dead.\""

        van "\"...Look there! {w=0.5}Someone's in there!\""


        show character_icon_box:
            xpos 800 ypos 300
        hide zalmona_icon_normal
        show zalmona_icon_surprised:
            xpos 800 ypos 298

        zal "\"Huh?\""

        van "\"Someone's in that glass chamber in the middle!\""

        hide zalmona_icon_surprised
        show zalmona_icon_normal:
            xpos 800 ypos 298

        zal "\"Oh. {w=0.5}That's probably just a cyborg too.\""

        van "\"A cyborg? {w=0.5}But they look as if they are...\""

        zal "\"......\""

        zal "\"...Detective, {w=0.5}didn't you know?\""

        zal "\"There are many kinds of cyborg.\""

        van "\"Many kinds? {w=0.5}What do you mean?\""

        zal "\"......\""

        zal "\"I'm not really an expert myself but...\""

        zal "\"Let me just read this part out for you.\""

        window hide

        $ renpy.music.set_volume(0.1, delay=0, channel='sound')
        play sound "music/cloth.mp3" fadeout 2.0

        $ renpy.pause(1.0, hard='True')

        window show

        van "With that, {w=0.5}Zalmona took out a journal from her pocket."

        window hide

        $ renpy.music.set_volume(1.0, delay=0, channel='sound')
        play sound "music/PageFlipshort.ogg"

        $ renpy.pause(2.0, hard='True')

        pause 4.0

        nvl show Dissolve(0.5)

        diary "Due to different bodies' varying ability to withstand semi-mechanization,"

        diary "The phenomenon of intellectual polarization often appears in each batch of experimental subjects."

        diary "Subjects that are able to withstand mechanization generally retain human facial features."

        diary "And with their newly modified bodies, {w=0.5}they exhibit superhuman abilities superior to those of ordinary humans."

        nvl clear

        diary "On the other hand, {w=0.5}subjects that failed to successfully withstand mechanization exhibited severe intellectual degradation,"

        diary "Thus making them behave like wild beasts."

        diary "At the same time, {w=0.5}the bodies of these failed subjects would exhibit an obvious rejection of mechanization,"

        diary "Resulting in them often giving the impression that they were falling apart."

        nvl clear

        diary "We refer to these cyborgs that have lost their intelligence as \"husks.\""

        diary "It is worth noting, {w=0.5}however, {w=0.5}that some of the experimental subjects seem to require an \"acclimation period,\""

        diary "That is, {w=0.5}their bodies exhibit repulsion similar to that of a husk when they first undergo mechanization."

        diary "But as long as they are fed regularly, {w=0.5}and are given ample time,"

        nvl clear

        diary "Eventually their bodies will be able to successfully accept the modifications they are given."

        diary "Thus, {w=0.5}after each batch of experimental subjects have been modified,"

        diary "We tend to leave them in the secret chamber for a period of observation."

        diary "If, {w=0.5}after that time, {w=0.5}the subject still does not demonstrate signs of successful mechanization,"

        diary "We would then dismember it and dump its body parts in the wastewater pool outside the G4 district."

        nvl clear

        nvl hide Dissolve(1.0)

        $ renpy.pause(1.0, hard='True')

        zal "\"The above was recorded in an experiment journal I found here at this corporation.\""

        van "\"In other words, {w=0.5}there are two kinds of cyborgs:\""

        van "\"The first kind looks like a monster because its body could not withstand mechanization.\""

        van "\"And the other is able to retain its intelligence and look exactly like a normal person because it has been successfully transformed?\""

        zal "\"Yes. {w=0.5}But not only that.\""

        zal "\"Pay attention to this next part:\""

        nvl show Dissolve(0.5)

        diary "Since often only a small number of subjects possess the ability to withstand mechanization,"

        diary "We often have to dismember and discard most of the cyborgs in the chamber,"

        diary "And this is definitely very costly and burdensome for us."

        diary "Therefore, {w=0.5}thanks to the tireless efforts of several researchers,"

        diary "We have successfully developed a method to create new types of cyborg through genetic cloning technology."

        nvl clear

        diary "As a result, {w=0.5}we no longer need to search for the minority that can withstand mechanization in batch after batch of experimental subjects."

        diary "All we need to do is to extract the genes of the subjects that have been successfully modified, {w=0.5}and then we can produce them again."

        diary "Nonetheless-"

        diary "Since these new cyborgs do not possess any memory, {w=0.5}we need to install a memory core inside them,"

        nvl clear

        diary "Giving them memories that do not exist, {w=0.5}thus giving them a unique personality."

        diary "These memories can be extracted from any existing employee to achieve the desired personality."

        nvl clear

        nvl hide Dissolve(1.0)

        $ renpy.pause(1.0, hard='True')

        zal "\"In other words, {w=0.5}there are cyborgs that are not directly modified from human beings, {w=0.5}but are created through genetic cloning technology.\""

        zal "\"But it's hard to tell them apart just by looking at them.\""

        van "\"......\""

        van "\"You mean,\""

        van "\"It is possible that there are cyborgs lurking around that look just like us ordinary humans?\""

        zal "\"Yes, {w=0.5}in a manner of speaking.\""

        if renpy.is_skipping():
            $ renpy.choice_for_skipping()
        $ _skipping = False
        $ rollback_ = False
        $ _rollback = False
        $ renpy.music.stop(channel="beep", fadeout = 0.5)

        hide zalmona_icon_normal
        hide character_icon_box
        $ renpy.transition(Dissolve(1.0))
        $ renpy.pause(1.0, hard='True')

        show screen inventory_screen
        with Dissolve(0.2)

        call screen engineering_room_secret_lab_click_screen with Dissolve(0.2)
    else:


        stop music fadeout 1.0

        $ renpy.music.set_volume(1.0, delay=0, channel='sound')
        play sound ("music/engineering room/Cupboard_open.ogg")

        $ renpy.pause(0.5, hard='True')

        scene black
        $ renpy.transition(Dissolve(0.5))
        $ renpy.pause(0.5, hard='True')

        $ renpy.pause(0.5, hard='True')

        $ renpy.music.set_volume(0.6, delay=0, channel='music')
        play music "music/myers lobby/lobby horror.ogg"

        scene engineering_room_secret_lab
        $ renpy.transition(Dissolve(1.0))
        $ renpy.pause(1.0, hard='True')

        call screen engineering_room_secret_lab_click_screen with Dissolve(0.2)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
