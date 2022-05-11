
image emanon_investigation_crime_scene_dont_cross_1 = "images/emanon murder scene/crime scene do not cross 1.png"
image emanon_investigation_crime_scene_dont_cross_2 = "images/emanon murder scene/crime scene do not cross 2.png"

image emanon_investigation_apartment = "images/emanon murder scene/emanon apartment.png"

screen emanon_investigation_collect_items:

    zorder 10
    text _("{font=VHS.ttf}{color=#ffffff}EVIDENCE:[emanon_investigation_num_item]/6{/color}{/font}") xpos 0.98 ypos 0.01 xanchor 1.0 outlines [(2, "#000000", 0, 0,)]
    vbox:
        xpos 0.983
        ypos 0.05
        xanchor 1.0
        textbutton _("{font=VHS.ttf}{size=-12}FINISH INVESTIGATION{/size}{/font}"):
            text_style "finish_investigation"
            action Jump("emanon_investigation_finish_investigation")

screen emanon_investigation_screen:

    zorder 0
    imagebutton:
        xpos 100
        ypos 600
        idle "images/myers-click/dialogue-idle-crop-small.png"
        hover "images/myers-click/dialogue-hover-crop-small.png"
        focus_mask "images/myers-click/dialogue-hover-crop-small.png"
        action Jump("emanon_investigation_speech_bubble")

    imagebutton:
        xpos 220
        ypos 450
        idle "images/emanon murder scene/emanon_investigation_blood_idle.png"
        hover "images/emanon murder scene/emanon_investigation_blood_hover.png"
        focus_mask "images/emanon murder scene/emanon_investigation_blood_hover.png"
        action Jump("emanon_investigation_investigate_blood")

    imagebutton:
        xpos 1069
        ypos 0
        idle "images/emanon murder scene/emanon_investigation_curtain_idle.png"
        hover "images/emanon murder scene/emanon_investigation_curtain_hover.png"
        focus_mask "images/emanon murder scene/emanon_investigation_curtain_hover.png"
        action Jump("emanon_investigation_investigate_curtain")

    imagebutton:
        xpos 0
        ypos 61
        idle "images/emanon murder scene/emanon_investigation_door_idle.png"
        hover "images/emanon murder scene/emanon_investigation_door_hover.png"
        focus_mask "images/emanon murder scene/emanon_investigation_door_hover.png"
        action Jump("emanon_investigation_investigate_door")

    imagebutton:
        xpos 887
        ypos 549
        idle "images/emanon murder scene/emanon_investigation_trophy_idle.png"
        hover "images/emanon murder scene/emanon_investigation_trophy_hover.png"
        focus_mask "images/emanon murder scene/emanon_investigation_trophy_hover.png"
        action Jump("emanon_investigation_investigate_trophy")

    imagebutton:
        xpos 715
        ypos 166
        idle "images/emanon murder scene/emanon_investigation_chair_idle.png"
        hover "images/emanon murder scene/emanon_investigation_chair_hover.png"
        focus_mask "images/emanon murder scene/emanon_investigation_chair_hover.png"
        action Jump("emanon_investigation_investigate_chair")

    imagebutton:
        xpos 260
        ypos 181
        idle "images/emanon murder scene/emanon_investigation_cabinet_idle.png"
        hover "images/emanon murder scene/emanon_investigation_cabinet_hover.png"
        focus_mask "images/emanon murder scene/emanon_investigation_cabinet_hover.png"
        action Jump("emanon_investigation_investigate_cabinet")

    imagebutton:
        xpos 307
        ypos 0
        idle "images/emanon murder scene/emanon_investigation_art_idle.png"
        hover "images/emanon murder scene/emanon_investigation_art_hover.png"
        focus_mask "images/emanon murder scene/emanon_investigation_art_hover.png"
        action Jump("emanon_investigation_investigate_art")

label emanon_investigation_start:

    $ renpy.free_memory()

    $ renpy.pause(4.0, hard=True)

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music "music/bgm/forest.ogg"

    $ renpy.pause(4.0, hard=True)

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/emanon crime scene/police siren.ogg"

    $ renpy.pause(2.0, hard=True)

    show emanon_investigation_crime_scene_dont_cross_1:
        yoffset -600
        linear 6.0 yoffset 600
    show emanon_investigation_crime_scene_dont_cross_2:
        yoffset -700
        linear 5.0 yoffset 600
    show black as black_2:
        alpha 0
        linear 6.0 alpha 1

    $ renpy.pause(4.0, hard=True)

    stop sound fadeout 5.0



    $ claude_name = _("Police Officer")

    claude "\"Are you the new detective? {w=0.5}Good to see you here.\""

    v "\"Just call me Vanora.\""

    v "\"Where is the crime scene? {w=0.5}I heard the victim was a former employee of Myers?\""

    claude "\"Yes. {w=0.5}Room 309. {w=0.5}Come with me.\""

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/myers lobby/draco footstep.ogg"

    pause 2.0

    claude "\"Move along people, {w=0.5}nothing to see here!\""

    claude "\"And stop interfering with the work of police officers!\""

    stop sound fadeout 2.0

    $ renpy.pause(2.0, hard=True)

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/engineering room/Cupboard_open.ogg")

    pause 1.5

    claude "\"Right, {w=0.5}here we are.\""

    scene emanon_investigation_apartment
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    show dust:
        alpha 0
        pause 5.0
        block:
            ease 5.0 alpha 0.5
            ease 5.0 alpha 1.0
            ease 5.0 alpha 0.5
            ease 5.0 alpha 0
            pause 5.0
            repeat

    $ renpy.pause(2.0, hard='True')

    v "\"......\""

    claude "\"I'll leave the rest to you, {w=0.5}Vanora.\""

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    $ renpy.pause(0.5, hard="True")

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/UI Dark.ogg"

    noname "Objective: {w=0.5}Survey the crime scene."

    $ rollback_ = False
    $ renpy.block_rollback()
    $ _rollback = False


    $ emanon_investigation_investigate_blood_bool = False
    $ emanon_investigation_investigate_curtain_bool = False
    $ emanon_investigation_investigate_door_bool = False
    $ emanon_investigation_investigate_trophy_bool = False
    $ emanon_investigation_question_1_bool = False
    $ emanon_investigation_question_2_bool = False

    $ emanon_investigation_num_item = 0

    show screen emanon_investigation_collect_items

    call screen emanon_investigation_screen with Dissolve(0.1)

label emanon_investigation_investigate_blood:
    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    hide dust
    hide screen emanon_investigation_collect_items

    show emanon_investigation_apartment at Position(xpos=0, ypos=0)

    show emanon_investigation_apartment:
        ease 0.5 zoom 1.5 xoffset 0 yoffset 0

    $ renpy.pause(0.5, hard='True')

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    if not emanon_investigation_investigate_blood_bool:

        $ emanon_investigation_investigate_blood_bool = True

        v "\"The body has already been cleared? {w=0.5}The G4 Investigation Bureau sure is efficient.\""

        $ rollback_ = True

        claude "\"That's correct. {w=0.5}As the victim had been dismembered, {w=0.5}we were unable to outline the exact location of the body on the floor.\""

        claude "\"However, {w=0.5}the autopsy report from the investigation bureau has been released.\""

        claude "\"The cause of death was due to {color=#f00}the rapid dismemberment of the body in a short period of time{/color}.\""

        v "\"So you're saying, {w=0.5}the murderer dismembered the victim while he was still alive?\""

        claude "\"Yes. {w=0.5}It was a very gruesome death.\""

        claude "\"But according to the autopsy report, {w=0.5}the victim's head did show signs of {color=#f00}being struck by an object{/color}, {w=0.5}but it was not fatal.\""

        claude "\"In addition, {w=0.5}the body displayed signs of a struggle before death, {w=0.5}so it's unlikely that he was unconscious for the ordeal.\""

        if emanon_investigation_investigate_trophy_bool:

            v "\"Struck by an object? {w=0.5}Is it the trophy on the floor?\""

            claude "\"Correct. {w=0.5}The shape of the wound does correspond to the pointed corner of the trophy.\""

        claude "\"Besides that, {w=0.5}there's something else that's strange: \""

        claude "\"{color=#f00}Some of the dismembered body parts of the deceased have disappeared{/color}.\""

        v "\"Disappeared?\""

        claude "\"Yes. {w=0.5}we couldn't fully reconstruct the victim's body with the pieces left in the room.\""

        claude "\"We searched the entire apartment building, {w=0.5}but we couldn't find any of the missing body parts.\""

        claude "\"We did take into the consideration that the perpetrator could be non-human,\""

        claude "\"But the report has made it clear that the dismemberment is not a result of a beast attack.\""

        v "\"......\""

        if renpy.is_skipping():
            $ renpy.choice_for_skipping()

        $ emanon_investigation_num_item += 1

        $ renpy.pause(0.5, hard="True")

        $ renpy.music.set_volume(0.8, delay=0, channel='sound')
        play sound "music/UI Dark.ogg"

        noname "Collected evidence: {w=0.5}Disappearing Body Parts"
    else:


        v "Where the victim's body was originally found."

        $ rollback_ = True

        v "The cause of death was the rapid dismemberment of the victim, {w=0.5}but there are also marks from blows to the head."

        v "The victim also showed clear signs of a struggle."

        v "But the strange thing is, {w=0.5}the victim's body was incomplete. {w=0.5}Some body parts were missing."

    show emanon_investigation_apartment:
        ease 0.5 zoom 1 xoffset 0 yoffset 0
    $ renpy.pause(0.5, hard='True')

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ _rollback = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    hide emanon_investigation_apartment
    scene emanon_investigation_apartment
    show dust:
        alpha 0
        pause 5.0
        block:
            ease 5.0 alpha 0.5
            ease 5.0 alpha 1.0
            ease 5.0 alpha 0.5
            ease 5.0 alpha 0
            pause 5.0
            repeat

    show screen emanon_investigation_collect_items
    call screen emanon_investigation_screen with Dissolve(0.1)

label emanon_investigation_investigate_curtain:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    hide dust
    hide screen emanon_investigation_collect_items

    show emanon_investigation_apartment at Position(xpos=0, ypos=0)

    show emanon_investigation_apartment:
        ease 0.5 zoom 3.0 xoffset -1280 yoffset 1200

    $ renpy.pause(0.5, hard='True')

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/emanon crime scene/curtain.ogg")

    show black:
        alpha 0
        ease 0.5 alpha 0.5

    v "I opened the curtain."

    $ rollback_ = True

    pause 1.0

    v "It's the only window in this apartment."

    v "The lock appears to not be tampered with, {w=0.5}so it's unlikely that the murderer entered the room through here."

    if not emanon_investigation_investigate_curtain_bool:

        $ emanon_investigation_investigate_curtain_bool = True

        v "\"Was the curtain here closed before?\""

        claude "\"Yes of course. {w=0.5}{color=#f00}We haven't moved a thing{/color}.\""

        if renpy.is_skipping():
            $ renpy.choice_for_skipping()

        $ emanon_investigation_num_item += 1

        $ renpy.pause(0.5, hard="True")

        $ renpy.music.set_volume(0.8, delay=0, channel='sound')
        play sound "music/UI Dark.ogg"

        noname "Collected evidence: {w=0.5}Closed curtains"

    hide black with Dissolve(0.5)

    show emanon_investigation_apartment:
        ease 0.5 zoom 1 xoffset 0 yoffset 0

    $ renpy.pause(0.5, hard='True')

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ _rollback = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    hide emanon_investigation_apartment
    show emanon_investigation_apartment
    show dust:
        alpha 0
        pause 5.0
        block:
            ease 5.0 alpha 0.5
            ease 5.0 alpha 1.0
            ease 5.0 alpha 0.5
            ease 5.0 alpha 0
            pause 5.0
            repeat

    show screen emanon_investigation_collect_items
    call screen emanon_investigation_screen with Dissolve(0.1)

label emanon_investigation_investigate_door:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    hide dust
    hide screen emanon_investigation_collect_items

    show emanon_investigation_apartment at Position(xpos=0, ypos=0)

    show emanon_investigation_apartment:
        ease 0.5 zoom 3.0 xoffset 1280 yoffset 1000

    $ renpy.pause(0.5, hard='True')

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    show black:
        alpha 0
        ease 0.5 alpha 0.5

    v "The door into the apartment."

    $ rollback_ = True

    if not emanon_investigation_investigate_door_bool:

        $ emanon_investigation_investigate_door_bool = True

        claude "\"The residents of the apartment building claimed that the murderer eluded them and escaped through here.\""

        claude "\"The suspect's name is Zalmona, {w=0.5}a resident on this floor.\""

        claude "\"Something worth mentioning is, {w=0.5}she is a {color=#f00}mutant{/color}.\""

        v "\"A mutant? {w=0.5}Is she from G3?\""

        claude "\"We're unsure at the moment.\""

        claude "\"Countless tourists visit G3 district every year to receive modifications. {w=0.5}We can't draw any conclusions yet.\""

        claude "\"We thoroughly searched her apartment, {w=0.5}but strangely enough, {w=0.5}we couldn't find any form of identification.\""

        claude "\"For now, {w=0.5}it seems that the murderer has escaped.\""

        v "\"What about the blood stains in the hallway outside the apartment?\""

        claude "\"Before we arrived, {w=0.5}Dr. Emanon's screams attracted a lot of curious residents.\""

        claude "\"These guys trampled over the entire apartment building. {w=0.5}And now there's blood everywhere outside the apartment.\""

        claude "\"Even if there were any useful clues in the hallway, {w=0.5}they've probably trampled them into oblivion by now.\""

        if renpy.is_skipping():
            $ renpy.choice_for_skipping()

        $ emanon_investigation_num_item += 1

        $ renpy.pause(0.5, hard="True")

        $ renpy.music.set_volume(0.8, delay=0, channel='sound')
        play sound "music/UI Dark.ogg"

        noname "Collected Evidence: {w=0.5}The suspect"
    else:


        v "The residents of the apartment building claimed that Zalmona eluded them and escaped through here."

        v "The outside of the door was tampered with by the residents of the apartment. {w=0.5}Any useful clues here might have been tainted and destroyed."

    hide black with Dissolve(0.5)

    show emanon_investigation_apartment:
        ease 0.5 zoom 1 xoffset 0 yoffset 0
    $ renpy.pause(0.5, hard='True')

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ _rollback = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    hide emanon_investigation_apartment
    scene emanon_investigation_apartment
    show dust:
        alpha 0
        pause 5.0
        block:
            ease 5.0 alpha 0.5
            ease 5.0 alpha 1.0
            ease 5.0 alpha 0.5
            ease 5.0 alpha 0
            pause 5.0
            repeat

    show screen emanon_investigation_collect_items
    call screen emanon_investigation_screen with Dissolve(0.1)

label emanon_investigation_investigate_trophy:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    hide dust
    hide screen emanon_investigation_collect_items

    show emanon_investigation_apartment at Position(xpos=0, ypos=0)

    show emanon_investigation_apartment:
        ease 0.5 zoom 4.0 xoffset -1300 yoffset 0

    $ renpy.pause(0.5, hard='True')

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    v "A trophy. {w=0.5}It's stained with blood."

    $ rollback_ = True

    v "Looks like it was used as a weapon of some kind."

    if not emanon_investigation_investigate_trophy_bool:

        $ emanon_investigation_investigate_trophy_bool = True

        v "\"Did we find fingerprints from any suspects on the trophy?\""

        claude "\"No. {w=0.5}We only managed to collect Dr. Emanon's.\""

        if emanon_investigation_investigate_blood_bool:

            claude "\"But it's worth mentioning - {w=0.5}the wound on the victim's head matches the shape of the trophy's pointed corner.\""

        if renpy.is_skipping():
            $ renpy.choice_for_skipping()

        $ emanon_investigation_num_item += 1

        $ renpy.pause(0.5, hard="True")

        $ renpy.music.set_volume(0.8, delay=0, channel='sound')
        play sound "music/UI Dark.ogg"

        noname "Collected evidence: {w=0.5}Blood-stained trophy"

    show emanon_investigation_apartment:
        ease 0.5 zoom 1 xoffset 0 yoffset 0
    $ renpy.pause(0.5, hard='True')

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ _rollback = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    hide emanon_investigation_apartment
    scene emanon_investigation_apartment
    show dust:
        alpha 0
        pause 5.0
        block:
            ease 5.0 alpha 0.5
            ease 5.0 alpha 1.0
            ease 5.0 alpha 0.5
            ease 5.0 alpha 0
            pause 5.0
            repeat

    show screen emanon_investigation_collect_items
    call screen emanon_investigation_screen with Dissolve(0.1)

label emanon_investigation_investigate_chair:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    hide dust
    hide screen emanon_investigation_collect_items

    show emanon_investigation_apartment at Position(xpos=0, ypos=0)

    show emanon_investigation_apartment:
        ease 0.5 zoom 2.0 xoffset -300 yoffset 500

    $ renpy.pause(0.5, hard='True')

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    v "A bloodstained chair. {w=0.5}Nothing special about it."

    show emanon_investigation_apartment:
        ease 0.5 zoom 1 xoffset 0 yoffset 0
    $ renpy.pause(0.5, hard='True')

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ _rollback = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    hide emanon_investigation_apartment
    scene emanon_investigation_apartment
    show dust:
        alpha 0
        pause 5.0
        block:
            ease 5.0 alpha 0.5
            ease 5.0 alpha 1.0
            ease 5.0 alpha 0.5
            ease 5.0 alpha 0
            pause 5.0
            repeat

    show screen emanon_investigation_collect_items
    call screen emanon_investigation_screen with Dissolve(0.1)

label emanon_investigation_investigate_cabinet:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    hide dust
    hide screen emanon_investigation_collect_items

    show emanon_investigation_apartment at Position(xpos=0, ypos=0)

    show emanon_investigation_apartment:
        ease 0.5 zoom 2.0 xoffset 300 yoffset 400

    $ renpy.pause(0.5, hard='True')

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    v "A bloodstained cabinet. {w=0.5}Nothing special about it."

    show emanon_investigation_apartment:
        ease 0.5 zoom 1 xoffset 0 yoffset 0
    $ renpy.pause(0.5, hard='True')

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ _rollback = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    hide emanon_investigation_apartment
    scene emanon_investigation_apartment
    show dust:
        alpha 0
        pause 5.0
        block:
            ease 5.0 alpha 0.5
            ease 5.0 alpha 1.0
            ease 5.0 alpha 0.5
            ease 5.0 alpha 0
            pause 5.0
            repeat

    show screen emanon_investigation_collect_items
    call screen emanon_investigation_screen with Dissolve(0.1)

label emanon_investigation_investigate_art:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zoom.wav")

    hide dust
    hide screen emanon_investigation_collect_items

    show emanon_investigation_apartment at Position(xpos=0, ypos=0)

    show emanon_investigation_apartment:
        ease 0.5 zoom 3.0 xoffset 300 yoffset 1440

    $ renpy.pause(0.5, hard='True')

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    v "Some paintings hanging on the wall."

    $ rollback_ = True

    v "But the closer you look, {w=0.5}the more obvious it is that they're just print outs."

    show emanon_investigation_apartment:
        ease 0.5 zoom 1 xoffset 0 yoffset 0
    $ renpy.pause(0.5, hard='True')

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ _rollback = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    hide emanon_investigation_apartment
    scene emanon_investigation_apartment
    show dust:
        alpha 0
        pause 5.0
        block:
            ease 5.0 alpha 0.5
            ease 5.0 alpha 1.0
            ease 5.0 alpha 0.5
            ease 5.0 alpha 0
            pause 5.0
            repeat

    show screen emanon_investigation_collect_items
    call screen emanon_investigation_screen with Dissolve(0.1)

label emanon_investigation_speech_bubble:

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/selectsounds.ogg"

    hide screen emanon_investigation_collect_items

    show black:
        alpha 0
        ease 0.5 alpha 0.5

    pause 0.5

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True

    claude "\"*Sigh* {w=0.5}Is there anything I can assist with, {w=0.5}Detective Vanora?\""

    $ rollback_ = True

label emanon_investigation_claude_questions:

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    menu:
        "Ask about known facts of the case":
            jump emanon_investigation_claude_question_1
        "Ask for information about the victim":
            jump emanon_investigation_claude_question_2
        "End the conversation":
            jump emanon_investigation_claude_questions_end

label emanon_investigation_claude_question_1:

    $ renpy.block_rollback()

    claude "\"According to our conversations with the residents of this building, {w=0.5}there was a short power outage in the building around when the crime was occuring.\""

    $ rollback_ = True

    claude "\"However, {w=0.5}after our investigation, {w=0.5}it seems the building's blackout was not the murderer's work. {w=0.5}{color=#f00}It was a mere coincidence{/color}.\""

    v "\"So the victim was {color=#f00}killed at the exact time of the power outage{/color}?\""

    claude "\"Correct.\""

    if not emanon_investigation_question_1_bool:

        $ emanon_investigation_question_1_bool = True

        $ emanon_investigation_num_item += 1

        if renpy.is_skipping():
            $ renpy.choice_for_skipping()
        $ _rollback = False
        $ rollback_ = False

        $ renpy.pause(0.5, hard="True")

        $ renpy.music.set_volume(0.8, delay=0, channel='sound')
        play sound "music/UI Dark.ogg"

        noname "Collected evidence: {w=0.5}A brief blackout of the building"

    jump emanon_investigation_claude_questions

label emanon_investigation_claude_question_2:

    $ renpy.block_rollback()

    claude "\"The name of the victim is {color=#f00}Dr. Richard Emanon{/color}, {w=0.5}a former researcher at Myers Corporation.\""

    $ rollback_ = True

    claude "\"According to our investigation, {w=0.5}although the victim holds a PhD, {w=0.5}his position at Myers was rather unremarkable.\""

    claude "\"We don't know much about his current occupation, {w=0.5}but judging by the apartment, {w=0.5}it's not hard to deduce that the pay wasn't getting any better.\""

    claude "\"A resident on the same floor claimed to have last seen him in the hallway outside his apartment last night.\""

    claude "\"Allegedly, {w=0.5}Dr. Emanon was on the phone at the time and seemed to be talking about some sort of {color=#f00}'deal.'{/color}\""

    v "\"...A deal?\""

    if not emanon_investigation_question_2_bool:

        $ emanon_investigation_question_2_bool = True

        $ emanon_investigation_num_item += 1

        if renpy.is_skipping():
            $ renpy.choice_for_skipping()
        $ _rollback = False
        $ rollback_ = False

        $ renpy.pause(0.5, hard="True")

        $ renpy.music.set_volume(0.8, delay=0, channel='sound')
        play sound "music/UI Dark.ogg"

        noname "Collected evidence: {w=0.5}Dr. Emanon's deal"

    jump emanon_investigation_claude_questions

label emanon_investigation_claude_questions_end:

    hide black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False
    $ rollback_ = False
    $ _rollback = False
    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    show dust:
        alpha 0
        pause 5.0
        block:
            ease 5.0 alpha 0.5
            ease 5.0 alpha 1.0
            ease 5.0 alpha 0.5
            ease 5.0 alpha 0
            pause 5.0
            repeat

    show screen emanon_investigation_collect_items
    call screen emanon_investigation_screen with Dissolve(0.1)

label emanon_investigation_finish_investigation:

    if emanon_investigation_num_item == 6:

        hide screen emanon_investigation_collect_items
        hide screen emanon_investigation_screen

        jump finish_emanon_investigation_click
    else:


        $ renpy.music.set_volume(0.8, delay=0, channel='sound')
        play sound "music/UI Dark.ogg"

        noname "Warning: {w=0.5}You have not finished your investigation yet. {p=0.5}Please try to collect more evidence."

        call screen emanon_investigation_screen
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
