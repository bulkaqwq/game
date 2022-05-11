






image myers_tunnel_1 = "images/tunnel/Myers_Tunnel_1.png"
image myers_tunnel_2 = "images/tunnel/Myers_Tunnel_2.png"
image myers_tunnel_3 = "images/tunnel/Myers_Tunnel_3.png"
image myers_tunnel_4 = "images/tunnel/Myers_Tunnel_4.png"
image myers_tunnel_3_mascot = "images/tunnel/Myers_Tunnel_3_mascot.png"
image myers_tunnel_mascot_closeup = "images/tunnel/Myers_Tunnel_mascot.png"
image myers_tunnel_mascot_closeup_blurred = im.Blur("images/tunnel/Myers_Tunnel_mascot.png", 1.5)
image myers_tunnel_4_hollow = "images/tunnel/Myers_Tunnel_4_hollow.png"
image myers_tunnel_4_door_hollow = "images/tunnel/Myers_Tunnel_4_door_hollow.png"

label chapter_2:

    $ renpy.free_memory()

    $ _skipping = True
    $ renpy.block_rollback()

    $ renpy.pause(1.0, hard="True")
    pause 1.0

    $ renpy.music.set_volume(0.2, delay=0, channel='music')
    play music "music/chapter2-haunting.ogg"

    pause 4.0

    stop sound fadeout 2.0

    $ renpy.pause(1.0, hard="True")

    $ _rollback = True

    scene myers_tunnel_1_flickering
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    pause 2.0

    window show

    $ say_who = name

    van "The first thing that caught my eyes as I entered Myers Corporation through the secret entrance was a dark and narrow passage."

    van "I couldn't see the end of the passage; {w=0.5}the only thing that allowed me to make out the outline of my surroundings was the small amount of sunlight coming in from outside."

    van "What's waiting for me at the other end of the passage? {w=0.5}I don't know."

    van "At that moment I didn't feel fear – {w=0.5}only doubt filled my heart."

    show gate_robot_memory_2
    show gate_robot_memory_2_blurred:
        ease 0.4 xoffset -10 yoffset -10 alpha 0.5

        ease 0.4 xoffset 10 yoffset -10 alpha 0.5

        ease 0.4 xoffset -10 yoffset 10 alpha 0.5

        ease 0.4 xoffset 10 yoffset 10 alpha 0.5

        ease 0.4 xoffset 0 yoffset 0 alpha 1.0

        repeat
    show memory_frame:
        linear 1.0 alpha 0.3
        linear 1.0 alpha 1
        repeat
    $ renpy.transition(Fade(.2, 0, 0.25, color="#fff"))
    $ renpy.pause(0.5, hard='True')

    van "My mind kept going back to the secret chamber I saw when I took off the eyeball, {w=0.5}and the cyborg that kept approaching me."

    van "What on earth was that? {w=0.5}Was it an illusion? {w=0.5}Or was it just my imagination?"

    hide gate_robot_memory_2
    hide memory_frame
    hide gate_robot_memory_2_blurred
    $ renpy.transition(Fade(.2, 0, 0.25, color="#fff"))
    $ renpy.pause(0.5, hard='True')

    van "And yet..."

    van "Everything seemed so real."

    van "At that moment, {w=0.5}it was as if I was really in that secret chamber."

    van "The repression, {w=0.5}fear, {w=0.5}and despair I felt..."

    van "That kind of intense feeling, {w=0.5}that I couldn't find words to describe."

    van "There are many ways to explain what I saw."

    van "Waking up to find yourself in a mysterious mansion, {w=0.5}having lost all your memories, {w=0.5}and the first thing to greet you is a broken cyborg."

    van "No matter who you are, {w=0.5}you'd start making some strange assumptions."

    van "\"This must be the result of me being overstressed.\" {w=0.5} I said to myself."

    van "But deep in my mind, {w=0.5}there seemed to be another voice whispering to me:"

    stop music fadeout 5.0

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/Tunnel/whisper tunnel.ogg"

    van "\"Everything you saw... {w=0.7}{color=#f00}really did happen{/color}.\""

    window hide

    $ say_who = ""

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False

    $ renpy.pause(1.0, hard='True')

    window show

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/UI Dark.ogg"

    noname "Objective: {w=0.5}Enter the Myers lobby."

    window hide

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music ("music/Tunnel/myersSewers.ogg")

    $ rollback_ = False
    $ renpy.block_rollback()
    $ _rollback = False


    $ myers_tunnel_see_shadow = False
    $ myers_tunnel_drop_mascot = False
    $ myers_tunnel_see_mascot_shock = False
    $ myers_tunnel_see_mascot = False
    $ myers_tunnel_travel_john_past = False
    $ myers_tunnel_see_blood = False
    $ myers_tunnel_door_code_1 = 0
    $ myers_tunnel_door_code_2 = 0
    $ myers_tunnel_door_code_3 = 0
    $ myers_tunnel_door_code_4 = 0

    $ myers_tunnel_check_door = False

    call screen myers_tunnel1 with Dissolve(0.2)

label tunnel_after_john_past:

    pause 3.0

    van "What was that...?"

    van "Just as before, {w=0.5}I seem to be seeing memories from the past that do not belong to me."

    van "What on earth is going on here?"

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False

    $ renpy.pause(0.5, hard='True')

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/UI Dark.ogg"

    noname "Tips: {w=0.5}By interacting with certain items, {w=0.5}you can trigger events from the past."

    noname "You can use this ability to {color=#f00}help you solve the puzzle you are facing right now{/color}."

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music ("music/Tunnel/myersSewers.ogg")

    $ myers_tunnel_travel_john_past = True

    $ rollback_ = False
    $ renpy.block_rollback()
    $ _rollback = False

    call screen myers_tunnel_mascot_screen
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
