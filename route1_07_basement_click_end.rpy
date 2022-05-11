
image basement_shadow_vanora = "images/basement/basement-shadow-vanora.png"
image basement_chamber = "images/basement/basement-chamber.png"
image chamber_cyborgs = "images/chamber/chamber-robot.png"
image chamber_cyborgs2 = "images/chamber/chamber-robot2.png"
image chamber_vincent = "images/chamber/chamber-vincent.png"
image chamber_vincent2 = "images/chamber/chamber-vincent2.png"
image chamber_vincent3 = "images/chamber/chamber-vincent3.png"
image chamber_vincent4 = "images/chamber/chamber-vincent4.png"
image chamber_vincent_tie = "images/chamber/chamber-vincent-tie.png"
image chamber_vincent_tie2 = "images/chamber/chamber-vincent-tie2.png"

label basement_click_end:

    $ _skipping = True
    $ renpy.block_rollback()
    $ _rollback = True
    $ rollback_ = True

    hide basement_2_computer_zoom
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    show basement_2:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    $ renpy.pause(0.5, hard='True')

    scene basement_2_1
    show basement_2_2

    hide screen inventory_screen
    with Dissolve(0.2)

    pause 0.5

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/Tunnel/GarageDoorSFX.ogg"

    $ renpy.pause(0.01, hard='True')
    show basement_2_2:
        linear 3.0 xoffset 500
    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 2.0, dist=15))
    $ renpy.pause(2.0, hard='True')

    stop sound fadeout 3.0
    stop music fadeout 5.0

    $ renpy.pause(3.0, hard='True')

    show character_icon_box_1:
        xpos 800 ypos 50
    show vin_icon_normal:
        xpos 800 ypos 48
    show character_icon_box_2:
        xpos 800 ypos 50
    with Dissolve(0.5)

    window show

    show vin_icon_smile behind character_icon_box_2:
        xpos 800 ypos 48
    hide vin_icon_normal
    with Dissolve(0.2)

    vin "\"Well done, {w=0.5}Vanora.\""

    window hide

    hide vin_icon_smile
    hide character_icon_box_1
    hide character_icon_box_2
    with Dissolve(0.5)

    $ renpy.pause(0.5, hard='True')
    pause 1.0
    $ renpy.pause(0.01, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music "music/ambience/horror ambience 2.ogg"

    show game_over_static:
        alpha 0.5
    $ renpy.transition(Dissolve(4.0))
    $ renpy.pause(5.0, hard='True')

    v "My vision blurred as soon as the secret chamber opened."

    show basement_shadow_vanora behind game_over_static:
        xoffset -100
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    pause 0.5

    v "I could no longer see my surroundings, {w=0.5}but I could vaguely sense a black shadow appearing in front of me."

    pause 1.0

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/basement/vita_female_giggle.ogg"

    anon "{color=#f00}\"Do you remember now? {w=0.5}Your mission?\"{/color}"

    v "She was staring straight at me with a creepy smile on her face."

    pause 0.5

    v "\"My mission?\""

    anon "{color=#f00}\"You know what I mean, {w=0.5}don't you? {w=0.5}I'm sure you do.\"{/color}"

    anon "{color=#f00}\"That man... {w=0.5}has to die.\"{/color}"

    show basement_shadow_vanora:
        linear 1.0 xoffset 200

    pause 1.5

    v "She turned around and began to walk slowly, {w=0.5}bit by bit, {w=0.5}towards the chamber."

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/basement/vita_female_giggle.ogg"

    hide basement_shadow_vanora
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    anon "{color=#f00}\"That man... {w=0.5}has to die.\"{/color}"

    stop music fadeout 3.0
    hide game_over_static
    $ renpy.transition(Dissolve(2.0))
    $ renpy.pause(2.0, hard='True')

    pause 1.0

    v "I watched her step into the chamber until her whole body was swallowed by the darkness."

    pause 1.0

    v "What was that thing?"

    show character_icon_box_1:
        xpos 800 ypos 50
    show vin_icon_normal:
        xpos 800 ypos 48
    show character_icon_box_2:
        xpos 800 ypos 50
    with Dissolve(0.5)

    window show

    show vin_icon_smile behind character_icon_box_2:
        xpos 800 ypos 48
    hide vin_icon_normal
    with Dissolve(0.2)

    vin "\"What is it, {w=0.5}Vanora? {w=0.5}Why are you still hesitating?\""

    hide vin_icon_smile
    show vin_icon_normal behind character_icon_box_2:
        xpos 800 ypos 48
    with Dissolve(0.2)

    v "\"......\""

    window hide

    pause 1.0

    v "Vincent didn't seem to catch that strange sight."

    pause 0.5

    show vin_icon_smile behind character_icon_box_2:
        xpos 800 ypos 48
    hide vin_icon_normal
    with Dissolve(0.2)

    pause 0.5

    window show

    vin "\"Ladies first.\""

    v "His smile still makes me feel uneasy."

    window hide

    hide vin_icon_smile
    show vin_icon_normal behind character_icon_box_2:
        xpos 800 ypos 48
    with Dissolve(0.2)

    pause 0.5

    v "I didn't say anything more."

    scene black with Dissolve(1.0)

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/myers lobby/draco footstep.ogg"

    pause 3.0

    stop sound fadeout 1.0

    v "After a few seconds of hesitation, {w=0.5}I gathered my courage and walked into the secret chamber. {w=0.5}I could feel Vincent following me closely."

    pause 1.0

    window show

    v "......"

    window hide

    $ renpy.free_memory()

    $ renpy.music.set_volume(0.8, delay=0, channel='music')
    play music "music/creepy.wav"

    scene basement_chamber
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    pause 2.0

    v "Those dark green walls and that dim light..."

    v "The sight in front of me didn't surprise me."

    v "The chamber looked exactly like the one I saw earlier in the cyborg's eyeball."

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zombie.ogg")

    show white_back:
        alpha 0
        linear 0.2 alpha 0.3
        linear 0.2 alpha 0
        linear 0.1 alpha 0.1
        linear 0.1 alpha 0
        linear 0.1 alpha 0.1
        linear 0.3 alpha 0

    show chamber_cyborgs:
        alpha 0
        linear 1.0 alpha 1.0

    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15))
    $ renpy.pause(2.5, hard='True')

    v "And all around me..."

    v "Were bloodthirsty cyborgs chained to the wall."

    show chamber_cyborgs:
        linear 1.0 alpha 0

    show gate_robot_memory_1:
        alpha 0
        linear 1.0 alpha 1.0

    v "But at that moment, {w=0.5}the only thing that caught my attention was this one cyborg in front of me."

    show gate_robot_memory_2:
        alpha 0
        linear 1.0 alpha 1.0

    v "He kept lunging at me like a murderous beast, {w=0.5}but the limb restraints made it difficult for him to move an inch."

    v "The way he looks... {w=0.5}Wait a minute, {w=0.5}there's no doubt that he is the same cyborg I saw from the memory of that eyeball."

    show gate_robot_memory_3:
        alpha 0
        linear 1.0 alpha 1.0

    v "No. {w=0.5}It's more than that."

    v "Everything I'm seeing right now... {w=0.5}feels so familiar."

    v "I very clearly remember the scene that I saw when I picked up that cyborg's eyeball -"

    v "It's {color=#f00}exactly the same{/color} as what I'm seeing now."

    hide gate_robot_memory_1
    hide gate_robot_memory_2
    hide gate_robot_memory_3
    with Dissolve(1.0)

    window show

    v "I don't understand."

    v "Was I not seeing the past memories of that cyborg, {w=0.5}but {color=#f00}my own present experience{/color}?"

    window hide

    $ renpy.pause(0.5, hard='True')

    show myers_left_2
    show memory_frame:
        linear 1.0 alpha 0.3
        linear 1.0 alpha 1
        repeat
    $ renpy.transition(Fade(.2, 0, 0.25, color="#fff"))
    $ renpy.pause(0.5, hard='True')
    hide memory_frame
    show myers_tunnel_4
    show memory_frame:
        linear 1.0 alpha 0.3
        linear 1.0 alpha 1
        repeat
    $ renpy.transition(Fade(.2, 0, 0.25, color="#fff"))
    $ renpy.pause(0.5, hard='True')
    hide memory_frame
    show myers_tunnel_3_mascot_flickering
    show transparent dark-small:
        alpha 0.5
    show myers_tunnel_invitation_zoom
    show memory_frame:
        linear 1.0 alpha 0.3
        linear 1.0 alpha 1
        repeat
    $ renpy.transition(Fade(.2, 0, 0.25, color="#fff"))
    $ renpy.pause(0.5, hard='True')
    hide memory_frame
    show basement_2
    show memory_frame:
        linear 1.0 alpha 0.3
        linear 1.0 alpha 1
        repeat
    $ renpy.transition(Fade(.2, 0, 0.25, color="#fff"))
    $ renpy.pause(0.5, hard='True')
    hide memory_frame
    show basement_4
    show transparent dark-small:
        alpha 0.6
    show basement_photo
    show memory_frame:
        linear 1.0 alpha 0.3
        linear 1.0 alpha 1
        repeat
    $ renpy.transition(Fade(.2, 0, 0.25, color="#fff"))
    $ renpy.pause(0.5, hard='True')
    hide myers_left_2
    hide myers_tunnel_4
    hide myers_tunnel_3_mascot_flickering
    hide transparent dark-small
    hide myers_tunnel_invitation_zoom
    hide basement_2
    hide basement_4
    hide basement_photo
    hide memory_frame
    $ renpy.transition(Fade(.2, 0, 0.25, color="#fff"))
    $ renpy.pause(0.5, hard='True')

    stop music fadeout 3.0

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/shock2.ogg" fadeout 2.0

    v "!?" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    v "I thought back to everything I had experienced since coming to the Myers Corporation. {w=0.5}I suddenly realized something. {w=0.5}Something that I had overlooked this whole time."

    show chamber_cyborgs:
        linear 1.0 alpha 1
    with Dissolve(1.0)

    pause 0.5

    show character_icon_box_1:
        xpos 470 ypos 50
    show vin_icon_smile:
        xpos 470 ypos 48
    show character_icon_box_2:
        xpos 470 ypos 50
    with Dissolve(1.0)

    window show

    vin "\"What is it, {w=0.5}Vanora? {w=0.5}Have you discovered anything new?\""

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music ["music/ambience/mic horror ambience 4.ogg","<silence 1.0>"] fadein 5.0

    hide vin_icon_smile
    show vin_icon_normal behind character_icon_box_2:
        xpos 470 ypos 48
    with Dissolve(0.2)

    v "\"...It was you all along, {w=0.5}wasn't it, {w=0.5}Vincent?\""

    show vin_icon_dark_smile behind character_icon_box_2:
        xpos 470 ypos 48
    hide vin_icon_normal
    with Dissolve(0.2)

    vin "\"Was it?\""

    window hide

    hide vin_icon_dark_smile
    hide character_icon_box_2
    hide character_icon_box_1
    with Dissolve(0.5)

    v "Vincent wasn't fazed at all. {w=0.5}Instead, {w=0.5}he had a contemptuous smile on his face."

    scene chamber_cyborgs2
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
    show chamber_vincent
    $ renpy.transition(Dissolve(2.0))
    $ renpy.pause(2.5, hard='True')

    v "\"The graffiti outside the Myers Corporation...\""

    v "\"The invitation letter and the four-digit code of the employee passageway...\""

    v "\"The history and philosophy books in the basement...\""

    v "\"And that college photo in the box.\""

    v "\"From the time I arrived at Myers until now, {w=0.5}I had always assumed that the experiments here were conducted by the secret underground Myers Corporation themselves.\""

    v "\"But that doesn't make any sense, {w=0.5}does it?\""

    v "\"Why would the Myers Corporation call themselves 'murderer' and use the same combination as the employee access password?\""

    v "\"And that party on the same day as your accident, {w=0.5}why would that have been the beginning of the nightmare for the Myers Corporation?\""

    v "\"Why would the bookcase in the basement here be filled with your favorite books on philosophy and history?\""

    v "\"And why is that college photo of you and Victor a clue to unlocking the secret chamber?\""

    v "\"If you think about it, {w=0.5}there can only be one explanation -\""

    v "\"{color=#f00}Because this whole time, {w=0.5}it wasn't the secret underground Myers Corporation that was still conducting experiments here at this site, {w=0.5}but you -{/color}\""

    v "\"{color=#f00}Vincent Edgeworth.{/color}\""

    pause 0.5

    show chamber_vincent2
    hide chamber_vincent
    with Dissolve(0.5)

    pause 0.5

    $ say_who = _("Vincent")

    window show

    vin "\"Hmm... {w=0.5}An interesting theory.\""

    vin "\"Indeed, {w=0.5}it seems that I can't really blame you for thinking that way.\""

    show chamber_vincent3
    hide chamber_vincent2
    with Dissolve(0.2)

    vin "\"If your suspicions are correct, {w=0.5}then why would I come here to help you expose myself?\""

    hide chamber_vincent3
    show chamber_vincent
    with Dissolve(0.2)

    $ say_who = ""

    v "\"It's simple. {w=0.5}This is all part of your plan.\""

    window hide

    scene black
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    pause 1.0

    show court_1
    show court_2
    with Dissolve(0.5)

    $ say_who = _("Vanora")

    window show

    v "\"In the case of the G4 Cyborg Incident, {w=0.5}you, {w=0.5}as the lawyer for the Myers Corporation, {w=0.5}pinned all of the blame on Winston Loomis,\""

    v "\"To cover up the fact that the cyborg experiment was planned by the Myers Corporation themselves.\""

    hide court_1
    hide court_2
    show car
    with Dissolve(0.5)

    v "\"And yet, {w=0.5}instead of being valued by the Myers Corporation, {w=0.5}you were almost killed in their carefully orchestrated car accident.\""

    v "\"You tried your very best and devoted everything you had to them, {w=0.5}but all they did was discard you like a pawn.\""

    v "\"So, {w=0.5}with this grudge against them, {w=0.5}you decided to take your revenge on the Myers Corporation.\""

    hide car
    with Dissolve(0.5)

    v "\"To defeat the Myers Corporation and become the one in control, {w=0.5}you needed to master technology even more advanced than theirs,\""

    v "\"And become even more frightening than the Myers Corporation.\""

    show lobby_bright
    show vic_suspicious_flip at vic_pos_3
    show vin_high_brow_satire at vin_pos_3
    show winston_normal
    with Dissolve(0.5)

    v "\"Having come to this conclusion, {w=0.5}you decided to rescue Winston from prison, {w=0.5}and made a deal with him to reassemble the cyborgs that the Myers Corporation had discarded,\""

    v "\"And together develop a new technology that would strike fear into Myers.\""

    scene black with Dissolve(0.5)

    v "\"That technology is what I have inside me, {w=0.5}{color=#f00}the ability to see others' past{/color}.\""

    window hide

    pause 1.0

    window show

    v "\"Not only that, {w=0.5}you actually knew very well that the Myers Corporation was conducting similar research but their progress was very slow.\""

    v "\"So you made a deal with a member of Myers' secret organization,\""

    v "\"And had him assist you in stealing all the documents and samples related to the research into this power by the Myers Corporation.\""

    show vincent-shadow-small
    show vincent-shadow-smile-small
    with Dissolve(0.5)

    v "\"Around the same time, {w=0.5}you sent Myers a threatening video suggesting that you were developing a secret weapon, {w=0.5}which caused them great paranoia.\""

    hide vincent-shadow-small
    hide vincent-shadow-smile-small
    with Dissolve(0.5)

    v "\"After you obtained everything you needed, {w=0.5}you brutally murdered that member and used his corpse as cattle feed for your reconstituted cyborgs.\""

    show engineering_room_zal_story_emanon
    with Dissolve(0.5)

    v "\"His name was Dr. Richard Emanon. {w=0.5}He was tragically found dead in his apartment with his body ripped apart.\""

    hide engineering_room_zal_story_emanon
    with Dissolve(0.5)

    v "\"And after that, {w=0.5}I was sent to your mansion as a detective to investigate the recent disappearances and the truth behind the G4 Cyborg Incident.\""

    v "\"Strangely enough, {w=0.5}I can't remember what happened after that.\""

    v "\"I woke up in your mansion, {w=0.5}and had lost all my memories.\""

    v "\"But unexpectedly, {w=0.5}I gained the power to see other people's past, {w=0.5}which I didn't possess before.\""

    show emanon_investigation_vin_mansion_3
    with Dissolve(0.5)

    v "\"But the clues I discovered at the Myers Corporation told me,\""

    v "\"On the night that I came to your mansion, {w=0.5}in fact, {w=0.5}you and I visited this building, {w=0.5}the old Myers Corporation, {w=0.5}together as a pair.\""

    hide emanon_investigation_vin_mansion_3
    with Dissolve(0.5)

    v "\"I haven't yet figured out what really happened that night, {w=0.5}but what I do know is:\""

    v "\"{color=#f00}You're the culprit behind the disappearances that have happened in the G4 district over the past few years.{/color}\""

    v "\"You've been secretly reassembling cyborgs here with Winston. {w=0.5}You need cattle feed to keep them alive.\""

    window hide

    scene chamber_cyborgs2
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
    show chamber_vincent
    with Dissolve(0.5)

    window show

    v "\"And me? {w=0.5}I was used by you as a guinea pig to test this new power you created, {w=0.5}the power to see other people's memories.\""

    v "\"Somehow, {w=0.5}you erased my memory to see if I could utilize my new power to find clues about my past.\""

    v "\"You set up the old Myers Corporation building as a testing ground for me and designed all sorts of puzzles,\""

    v "\"Then lied to me about finding a Myers Corporation business card in my pocket when I woke up in your mansion,\""

    v "\"And lured me here to begin your experiment.\""

    stop music fadeout 3.0

    v "\"Well, {w=0.5}how's that? {w=0.5}Is there anything else that I need to explain?\""

    window hide

    $ say_who = ""

    pause 0.5

    hide chamber_vincent
    show chamber_vincent2
    with Dissolve(0.5)

    pause 0.5

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/vin_hmm.ogg"

    window show

    vin "\"Well done, {w=0.5}Vanora. {w=0.5}You're truly impressive.\""

    hide chamber_vincent2
    show chamber_vincent
    with Dissolve(0.2)

    v "\"Impressive? {w=0.5}In other words, {w=0.5}you don't deny anything I have said?\""

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music ["<silence 1.0>","music/bgm/mic-epic.ogg"]

    hide chamber_vincent
    show chamber_vincent2
    with Dissolve(0.2)

    $ say_who = _("Vincent")

    vin "\"Correct. {w=0.5}I admit that I am indeed the one behind everything.\""

    hide chamber_vincent
    show chamber_vincent3
    with Dissolve(0.2)

    vin "\"However, {w=0.5}I must comment, {w=0.5}there's one fatal error in your near-perfect reasoning.\""

    hide chamber_vincent3
    show chamber_vincent2
    with Dissolve(0.2)

    vin "\"{color=#f00}How do you know that you're really Vanora, {w=0.5}cyborg lady?{/color}\""

    hide chamber_vincent2
    show chamber_vincent
    show character_icon_box:
        xpos 130 ypos 250
    show van_icon_normal:
        xpos 130 ypos 248
    with Dissolve(0.3)

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/shock2.ogg" fadeout 2.0

    $ say_who = _("Vanora")

    v "!?" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    hide van_icon_normal
    show van_icon_angry:
        xpos 130 ypos 248
    with Dissolve(0.2)

    v "\"Weren't you the one who called me 'Vanora' first?\""

    show chamber_vincent2 behind character_icon_box
    hide chamber_vincent
    with Dissolve(0.2)

    $ say_who = _("Vincent")

    vin "\"True. {w=0.5}But have you forgotten? {w=0.5}As we discussed before, {w=0.5}a person's personality is determined by how much they remember.\""

    show chamber_vincent3 behind character_icon_box
    hide chamber_vincent2
    with Dissolve(0.2)

    vin "\"The reason why I call you 'Vanora' is because your demeanor is the same as hers.\""

    vin "\"In other words, {w=0.5}I know you have recovered the memory of Vanora's and think you are her.\""

    show chamber_vincent2 behind character_icon_box
    hide chamber_vincent3
    with Dissolve(0.2)

    vin "\"But if that same memory was given to another cyborg, {w=0.5}they too would think they were Vanora, {w=0.5}wouldn't they?\""

    show chamber_vincent behind character_icon_box
    hide chamber_vincent2
    with Dissolve(0.2)

    hide van_icon_angry
    show van_icon_angry_close:
        xpos 130 ypos 248
    with Dissolve(0.2)

    $ say_who = _("Vanora")

    v "\"......\""

    hide van_icon_angry_close
    show van_icon_angry:
        xpos 130 ypos 248
    with Dissolve(0.2)

    v "\"You're toying with me. {w=0.5}I don't believe you.\""

    show chamber_vincent3 behind character_icon_box
    hide chamber_vincent
    with Dissolve(0.2)

    $ say_who = ""

    vin "\"Vanora, {w=0.5}do you perhaps remember the date of the day you came to my mansion as a detective?\""

    show chamber_vincent behind character_icon_box
    hide chamber_vincent3
    with Dissolve(0.2)

    hide van_icon_angry
    show van_icon_angry_close:
        xpos 130 ypos 248
    with Dissolve(0.2)

    v "\"Yes. {w=0.5}It was December 1, {w=0.5}2086.\""

    show chamber_vincent3 behind character_icon_box
    hide chamber_vincent
    with Dissolve(0.2)

    vin "\"And do you know what the date is today?\""

    show chamber_vincent behind character_icon_box
    hide chamber_vincent3
    with Dissolve(0.2)

    hide van_icon_angry_close
    show van_icon_angry:
        xpos 130 ypos 248
    with Dissolve(0.2)

    v "\"...No, {w=0.5}I don't.\""

    show chamber_vincent2 behind character_icon_box
    hide chamber_vincent
    with Dissolve(0.2)

    vin "\"Today is March 5, {w=0.5}2087.\""

    show chamber_vincent behind character_icon_box
    hide chamber_vincent2
    with Dissolve(0.2)

    hide van_icon_angry
    show van_icon_angry_close:
        xpos 130 ypos 248
    with Dissolve(0.2)

    v "\"......!\""

    show chamber_vincent2 behind character_icon_box
    hide chamber_vincent
    with Dissolve(0.2)

    vin "\"That's right. {w=0.5}You have absolutely no clue what has happened in the last three months. {w=0.5}{color=#f00}The real Vanora is long gone.{/color}\""

    show chamber_vincent behind character_icon_box
    hide chamber_vincent2
    with Dissolve(0.2)

    hide van_icon_angry_close
    show van_icon_angry:
        xpos 130 ypos 248
    with Dissolve(0.2)

    v "\"......\""

    window hide

    hide van_icon_angry
    hide character_icon_box
    with Dissolve(1.0)

    pause 2.0

    show chamber_vincent2 behind character_icon_box
    hide chamber_vincent
    with Dissolve(0.5)

    $ say_who = _("Vincent")

    window show

    vin "\"I apologize, {w=0.5}Vanora. {w=0.5}I'm afraid I must end our conversation here.\""

    show chamber_vincent3 behind character_icon_box
    hide chamber_vincent2
    with Dissolve(0.2)

    vin "\"If I have to be honest, {w=0.5}I too did not wish to see everything end this way.\""

    vin "\"However, {w=0.5}I have no choice but to let you spend the rest of your life here with your kind.\""

    hide chamber_vincent3
    show chamber_vincent
    with Dissolve(0.2)

    $ say_who = ""

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/zombie.ogg")

    c "\"Uh...{w=0.5}Ah...\""

    show character_icon_box:
        xpos 130 ypos 250
    show van_icon_angry:
        xpos 130 ypos 248
    with Dissolve(0.2)

    $ say_who = _("Vanora")

    v "\"......!\""

    hide van_icon_angry
    show van_icon_angry_close:
        xpos 130 ypos 248
    with Dissolve(0.2)

    v "\"But why? {w=0.5}Why are you doing this?\""

    show character_icon_box:
        xpos 130 ypos 250
    show van_icon_angry:
        xpos 130 ypos 248
    with Dissolve(0.2)

    v "\"If I'm not the real Vanora, {w=0.5}why are you doing this to me? {w=0.5}What did I do to you?\""

    window hide

    $ say_who = ""

    hide character_icon_box
    hide van_icon_angry
    hide van_icon_angry_close
    with Dissolve(0.5)

    pause 1.0

    hide chamber_vincent
    show chamber_vincent4
    with Dissolve(0.5)

    $ say_who = _("Vincent")

    window show

    vin "\"Vanora or not, {w=0.5}your heart belongs to the Myers Corporation. {w=0.5}Your body reeks of decay, {w=0.5}and your soul embodies putrid corruption.\""

    show chamber_vincent3
    hide chamber_vincent4
    with Dissolve(0.2)

    vin "\"She is yours now, {w=0.5}my friends.\""

    hide chamber_vincent3
    show chamber_vincent
    with Dissolve(0.2)

    window hide

    $ say_who = ""

    pause 0.5

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/shock2.ogg" fadeout 2.0

    v "\"Wait - {w=0.5}wait!\"" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    pause 0.5

    $ renpy.music.set_volume(0.5, delay=0, channel='sound1')
    $ renpy.music.play("music/basement/zs_loud_glitch.ogg", channel="sound1", fadeout = 3.0, loop = False)

    show white_back:
        alpha 0
        linear 0.2 alpha 0.3
        linear 0.2 alpha 0
        linear 0.2 alpha 0.3
        linear 0.2 alpha 0
        linear 0.2 alpha 0.3
        linear 0.1 alpha 0
        linear 0.1 alpha 0.3
        linear 0.1 alpha 0

    show black:
        alpha 0
        pause 1.3
        linear 0.1 alpha 1

    hide chamber_vincent
    show chamber_vincent_tie behind white_back:
    with Dissolve(0.5)

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/shake.ogg"

    $ renpy.music.stop(channel = "sound1", fadeout = 4.0)

    show chamber_vincent_tie behind white_back:
        yoffset 40
    with Shake((0.5, 1.0, 0.5, 1.0), 2.0, dist=15)

    vin "!?"

    scene grey-bg
    show black-bg
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    show black-bg:
        ease 0.4 xoffset -70 yoffset -70 alpha 0.5

        ease 0.4 xoffset 70 yoffset -70 alpha 0.5

        ease 0.4 xoffset -70 yoffset 70 alpha 0.5

        ease 0.4 xoffset 70 yoffset 70 alpha 0.5

        ease 0.4 xoffset -70 yoffset -70 alpha 0.5

        ease 0.4 xoffset 70 yoffset -70 alpha 0.5

        ease 0.4 xoffset -70 yoffset 70 alpha 0.5

        ease 0.4 xoffset 70 yoffset 70 alpha 0.5

        ease 0.4 xoffset 0 yoffset 0 alpha 1.0

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/heartbeat.ogg"
    queue sound "music/heartbeat.ogg"

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

    hide chamber_cyborgs2_blurred
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    pause 1.0

    v "Amidst the chaos, {w=0.5}I subconsciously reached out with my right hand and grabbed the closest, {w=0.5}most accessible thing to me -"

    v "Vincent's tie."

    v "I don't remember why I did that."

    v "But what I do remember is, {w=0.5}when I grabbed his tie, {w=0.5}my vision started to blur again."

    stop music fadeout 4.0

    pause 3.0

    v "The last thing I saw was a hint of panic on Vincent's face."

    scene black
    show white back
    $ renpy.transition(Dissolve(0.1))
    $ renpy.pause(0.1, hard='True')

    stop music

    $ renpy.music.set_volume(0.7, delay=0, channel='sound')
    play sound "music/teleport.ogg"

    $ renpy.pause(1.0, hard='True')

    hide white back
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    pause 1.0
    $ renpy.pause(1.0, hard=True)

    window show

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/UI Dark.ogg"

    noname "Investigation completed. {w=0.5}Successfully located the secret chamber."

    window hide

    jump graduation_start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
