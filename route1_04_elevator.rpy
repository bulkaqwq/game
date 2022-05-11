image legal_department_elevator_inside = "images/Legal Department/legal department elevator inside.png"

label legal_department_elevator_start:

    $ renpy.free_memory()

    $ renpy.pause(1.0, hard='True')

    scene legal_department_elevator_inside
    show main_title_shadow
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    pause 2.0

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/vanora/van heavy breath.ogg") fadeout 1.0

    van "\"Huff... {w=0.5}huff...\""

    $ renpy.music.set_volume(0.5, delay=0, channel='music')
    play music "music/ambience/horror ambience 1.ogg" fadein 3.0

    pause 2.0

    van "I could still feel my heart pounding."

    pause 2.0

    van "\"......\""

    van "That monster doesn't seem to be pursuing us. {w=0.5}I think we're safe for now."

    van "What exactly...{w=0.5}was that thing...?"

    stop music fadeout 1.0

    dra "\"[name!t]......\""

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/shock2.ogg"
    van "!?" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    van "\"Draco!?\""

    show draco_blood_upset
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    window show

    dra "\"I'm sorry, {w=0.5}[name!t]...{w=0.5}I couldn't stop him.\""

    van "Slowly, {w=0.5}Draco stood up. {w=0.5}He sounded very weak."

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/shock2.ogg"
    van "\"Draco, {w=0.5}are you okay!?\"" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    show draco_blood_stubborn with Dissolve(0.2)
    hide draco_blood_upset

    dra "\"No need to worry about me...{w=0.5} It's just a few scratches.\""

    van "\".........\""

    show draco_blood_shocked
    hide draco_blood_stubborn

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/shake.ogg"
    van "\"Stop acting like a hero at a time like this!!!\"" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    window hide

    $ renpy.pause(0.5, hard='True')

    $ renpy.music.set_volume(0.8, delay=0, channel='music')
    play music "music/bgm/ankari-sad-2.ogg"

    pause 3.0

    window show

    van "Draco froze in the face of my emotional outburst."

    van "At that moment, {w=0.5}we were both just looking at each other, {w=0.5}and stuck in silence."

    window hide

    pause 2.0

    window show

    van "\"Draco, {w=0.5}are you serious? {w=0.5}Stop it with the act!\""

    van "\"You have been saying strange, incomprehensible bullshit ever since we met in the lobby!\""

    van "\"You're badly hurt, {w=0.5}yet you're making light of it!\""

    van "\"You're really starting to piss me off!\""

    van "\"I don't give a damn about how cool you are.\""

    van "\"And at this point, {w=0.5}I really don't care how many lies you've told me.\""

    van "\"But I do know that, {w=0.5}what I'm worried about now, {w=0.5}is you!\""

    window hide

    pause 2.0

    window show

    dra "\"......\""

    window hide

    pause 0.5

    show draco_blood_sad with Dissolve(0.2)
    hide draco_blood_shocked

    pause 2.0

    window show

    dra "\"You...{w=0.5}reminded me of that time.\""

    window hide

    pause 2.0

    window show

    van "Draco's face broke and began to show a deep sorrow. {w=0.5}A sadness that I would never expect to see from him."

    van "\"...That time?\""

    show draco_blood_upset
    hide draco_blood_sad
    with Dissolve(0.5)

    dra "\"......[name!t], {w=0.5}I'm sorry.\""

    dra "\"If only I had told you... {w=0.5}the truth earlier...\""

    dra "\"Maybe things wouldn't be the way they are.\""

    window hide

    pause 2.0

    window show

    van "\"......{w=0.5}Draco......\""

    hide draco_blood_upset
    show draco_blood_sad
    with Dissolve(0.5)

    dra "\"There are times when I ask myself, {w=0.5}can we go back in time?\""

    dra "\"But for you, {w=0.5}our past is long gone.\""

    $ say_who = name

    van "\"We can go back!!! {w=0.5}We will!!!\""

    van "\"That's what we're here for, {w=0.5}isn't it? {w=0.5}To search for our past, {w=0.5}the past we shared!\""

    show draco_blood_shocked with Dissolve(0.2)

    van "\"Even if I've completely forgotten you, {w=0.5}I'd like to get to know you again!\""

    van "\"So when we escape from here, {w=0.5}please tell me everything about our past!\""

    $ say_who = ""

    window hide

    pause 2.0

    show draco_blood_obey
    hide draco_blood_shocked
    hide draco_blood_sad
    $ renpy.transition(Dissolve(0.2))
    $ renpy.pause(1.0, hard='True')

    window show

    dra "\"As you wish, {w=0.5}Lady [name!t].\""

    window hide

    stop music fadeout 3.0

    $ renpy.pause(1.0, hard='True')

    show draco_blood_serious with Dissolve(0.5)
    hide draco_blood_obey

    $ renpy.pause(1.0, hard='True')

    dra "\"...But there is a more urgent issue at hand.\""

    dra "\"Where is he right now?\""

    van "\"...What happened there? {w=0.5}What the hell is that thing?\""

    $ renpy.pause(1.0, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    queue music "music/bgm/mic-epic.ogg"

    show draco_blood_stubborn with Dissolve(0.5)
    hide draco_blood_serious

    $ renpy.pause(2.0, hard='True')

    dra "\"He's not... {w=0.5}a thing.\""

    dra "\"He's someone you already know.\""

    dra "\"The truth is-\""

    window hide

    $ renpy.pause(0.3, hard=True)

    $ renpy.music.set_volume(0.6, delay=0, channel='sound1')
    $ renpy.music.play("music/monster moan 2.ogg", channel="sound1", fadeout = 1.0, loop = False)

    show draco_blood_shocked with Dissolve(0.2)
    hide draco_blood_stubborn

    $ renpy.pause(3.0, hard=True)

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/legal department/elevator crash 3.ogg"

    show white back:
        zoom 1.25 xalign 0.5 yalign 0.5
        alpha 1.0
        ease 0.2 alpha 0.4
        alpha 1.0
        ease 0.2 alpha 0.4
        alpha 1.0
        ease 0.2 alpha 0.4
        ease 0.5 alpha 0

    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=20))

    scene black
    show legal_department_elevator_inside:
        ease 0.1 yoffset 1000
    show draco_blood_shocked:
        ease 0.1 yoffset 1000
    show main_title_shadow
    show black:
        alpha 0
        ease 0.1 alpha 1.0

    $ renpy.pause(3.0, hard=True)

    $ renpy.pause(1.0, hard=True)

    window show

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/shock2.ogg"
    dra "\"{color=#f00}Vanora{/color}!!!!!!!!!!!!!!!!\"" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    window hide

    pause 2.0

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/legal department/elevator crash 2.ogg"

    $ renpy.pause(6.0, hard=True)

    scene demo_end_myers
    show demo_end_myers_lamp
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(2.0, hard='True')

    pause 2.0

    window show

    m "\"My precious Chaser, {w=0.5}tell me, {w=0.5}is there someone you love?\""

    anon "\"A loved one? {w=0.5}My dear Monsieur M, {w=0.5}why would you ask such a question?\""

    m "\"Let's assume, {w=0.5}one day a disaster were to happen to your loved one.\""

    m "\"Say they lose their body, {w=0.5}but their memories are still intact.\""

    m "\"Would you still love them like that?\""

    anon "\"...Of course I would. {w=0.5}No matter what body they change into, {w=0.5}they're still them.\""

    m "\"What a heartwarming answer!\""

    m "\"Well, {w=0.5}let's change the scenario, {w=0.5}shall we?\""

    m "\"Let's say... {w=0.5}What if the person you love – {w=0.5}is physically intact, {w=0.5}but has lost all their memories.\""

    m "\"Would you still love such a person?\""

    anon "\"Of course I would. {w=0.5}Even if they lose all their memories, {w=0.5}I would still love them.\""

    m "\"Even if they completely forgot about your existence?\""

    m "\"Even if all the memories you two shared... {w=0.5}are gone?\""

    anon "\"This would make me miserable. {w=0.5}But I would still love them.\""

    m "\"What an amusing answer. {w=0.5}Humans always have been able to entertain me.\""

    m "\"Well then-\""

    m "\"Since you don't mind them losing their body, {w=0.5}and you don't mind them losing their memory, {w=0.5}what exactly do you love about them?\""

    anon "\"......\""

    show demo_end_myers_smile
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    m "\"What you love is merely a self-fulfilling illusion. {w=0.5}What you love is a person from your past that no longer exists.\""

    window hide

    scene black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(1.0, hard='True')

    window show

    m "\"The brutal truth is -\""

    m "\"The moment one loses their memory... {w=0.5}they will no longer be themselves. {w=0.5}And they will never be able to go back.\""

    window hide

    $ renpy.pause(4.0, hard='True')

    stop music fadeout 6.0

    $ renpy.pause(2.0, hard='True')

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/UI Dark.ogg"

    window show

    $ renpy.pause(0.1, hard=True)

    noname "{color=#f00}Investigation completed. {w=0.5}Successfully retrieved the glove.{/color}"

    window hide

    jump emanon_investigation_start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
