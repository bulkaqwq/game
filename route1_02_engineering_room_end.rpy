
image engineering_room_zal_story_apartment = "images/Engineering Room Zal Story/engineering_room_zal_story_apartment.png"
image engineering_room_zal_story_apartment_blood = "images/Engineering Room Zal Story/engineering_room_zal_story_apartment_blood.png"
image engineering_room_zal_story_zal_normal = "images/Engineering Room Zal Story/engineering_room_zal_story_zal_normal.png"
image engineering_room_zal_story_zal_panic = "images/Engineering Room Zal Story/engineering_room_zal_story_zal_panic.png"
image engineering_room_zal_story_shadow = "images/Engineering Room Zal Story/engineering_room_zal_story_shadow.png"
image engineering_room_zal_story_emanon = "images/Engineering Room Zal Story/engineering_room_zal_story_emanon.png"
image engineering_room_zal_watch = "images/Engineering Room Zal Story/egineering_room_zal_watch.png"
image engineering_room_door_to_legal_1 = "images/Engineering Room Zal Story/engineering_room_door_to_legal_1.png"
image engineering_room_door_to_legal_2 = "images/Engineering Room Zal Story/engineering_room_door_to_legal_2.png"

label engineering_room_end:

    pause 2.0

    $ renpy.pause(0.1, hard='True')

    scene engineering_room_2
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    show zalmona_drop_shadow at zal_pos_2
    show zalmona_surprised at zal_pos_2
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    pause 2.0

    van "\"......\""

    pause 2.0

    zal "\"Detective, {w=0.5}are you alright?\""

    van "\"......\""

    pause 2.0

    zal "\"Detective?\""

    show zalmona_panic at zal_pos_2
    hide zalmona_surprised

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/shake.ogg"
    van "\"Stop calling me Detective! {w=0.5}You don't even know who I am!\"" with Shake((0.5, 1.0, 0.5, 1.0), 3.0, dist=15)

    van "\"You saw it too.\""

    van "\"That cyborg we just saw...\""

    van "\"{color=#f00}She looked exactly like me!{/color}\""

    zal "\"......\""

    van "\"I don't even know who you are, {w=0.5}Zalmona! {w=0.5} I don't remember anything at all!\""

    van "\"I thought coming here would find me the answers I wanted, {w=0.5}but now I just feel completely lost.\""

    van "\"I could be someone who doesn't even exist! {w=0.5}Just one of a million other identical cyborgs!\""

    van "\"Draco was right all along. {w=0.5}I shouldn't even be here to begin with!\""

    zal "\"......\""

    pause 2.0

    van "Even with my sudden breakdown, {w=0.5}Zalmona didn't show one ounce of anger with me."

    hide zalmona_panic
    show zalmona_normal at zal_pos_2
    with Dissolve(0.5)

    pause 2.0

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music "music/bgm/ankari-sad.ogg"

    window show

    van "After a moment of silence, {w=0.5}she started to speak."

    window hide

    pause 2.0

    window show

    zal "\"You feel that the truth you seek is meaningless now, {w=0.5}don't you?\""

    $ say_who = _("Zalmona")

    zal "\"You've lost all hope, {w=0.5}because you are worried that you are merely a replica.\""

    show zalmona_accepting at zal_pos_2 with Dissolve(0.2)

    zal "\"But you shouldn't let your past define you.\""

    zal "\"You're right. {w=0.5}There's no way to be certain if you are or aren't the Detective I met.\""

    zal "\"But whoever each of us is, {w=0.5}is up to us.\""

    hide zalmona_accepting with Dissolve(0.2)

    zal "\"The moment you open your eyes, {w=0.5}you are who you are. {w=0.5}And not anyone else.\""

    zal "\"So what if there's someone else, {w=0.5}somewhere in the world, {w=0.5}who looks exactly like you?\""

    zal "\"It's each of our own unique experiences that make up who we are, {w=0.5}isn't it?\""

    zal "\"At this moment, {w=0.5}only you and I are standing here.\""

    zal "\"This experience belongs to just us, {w=0.5}and no one else.\""

    zal "\"What motivates each of us to go on with our lives is the countless exciting possibilities that lie in store.\""

    zal "\"And in the near future, {w=0.5}you are bound to meet new people, {w=0.5}and make new friends.\""

    zal "\"And maybe... {w=0.5}they will become your new family. {w=0.5}{color=#f00}People who are willing to sacrifice their lives for you{/color}.\""

    $ say_who = ""

    van "\"...People who would...{w=0.5}sacrifice their lives for me...?\""

    window hide

    pause 2.0

    window show

    van "Zalmona's words were somehow very reassuring. {w=0.5}It was very different from how I had imagined her to be."

    van "\"I never thought I would hear such words from you.\""

    show zalmona_happy at zal_pos_2 with Dissolve(0.2)

    $ renpy.music.set_volume(0.2, delay=0, channel='sound')
    play sound "music/zalmona/Zalmona-hnnnnn.ogg"

    zal "\"Ha-ha, {w=0.5}probably something I picked up during my previous profession.\""

    van "\"Huh?\""

    hide zalmona_happy with Dissolve(0.2)

    zal "\"Don't worry too much about it, {w=0.5}it's irrelevant now.\""

    zal "\"Anyway, {w=0.5}thanks a lot for your help.\""

    zal "\"You have no idea how important this device is to me.\""

    stop music fadeout 5.0

    van "\"......\""

    van "\"Zalmona, {w=0.5}why do you need the cyborg's memory core?\""

    show zalmona_accepting at zal_pos_2 with Dissolve(0.2)

    $ say_who = _("Zalmona")

    zal "\"......{w=0.5}It's a long story.\""

    hide zalmona_accepting with Dissolve(0.2)

    zal "\"You said you've lost all your memories.\""

    zal "\"But seeing that you've found your way into Myers, {w=0.5}I think it's safe to assume that you've heard the Urban Legends about the G4 district?\""

    van "\"G4 district's Urban Legend? {w=0.5}Do you mean the infamous G4 Cyborg Incident?\""

    show zalmona_accepting at zal_pos_2 with Dissolve(0.2)

    zal "\"Close, {w=0.5}but I'm thinking particularly about the end of that legend.\""

    hide zalmona_accepting with Dissolve(0.2)

    zal "\"It should sound something like this: \""

    zal "\" 'To this day, {w=0.5}people still mysteriously vanish in the G4 district.' \""

    zal "\" 'Rumour says that the spirits of the victims from the experiment are still wandering the streets, {w=0.5}taking the lives of those unfortunate enough to cross paths with them...' \""

    van "\"Ah, {w=0.5}I remember.\""

    zal "\"Right. {w=0.5}And you don't need me to tell you that {color=#f00}ghosts don't exist{/color}.\""

    zal "\"These recent disappearances in the G4 district are the deliberate work of a certain someone as well.\""

    van "\"Are you suggesting that Myers Corporation is behind these recent disappearances as well? {w=0.5}The Myers Corporation that is continuing operations covertly?\""

    show zalmona_accepting at zal_pos_2 with Dissolve(0.2)

    zal "\"Yeah, {w=0.5}something like that.\""

    zal "\"But here's the thing, {w=0.5}a lot of details about these cases are... {w=0.5}different from the original G4 Cyborg Incident.\""

    zal "\"In the G4 Cyborg Incident, {w=0.5}Myers Corporation turned their own employees into cyborgs, {w=0.5}and kidnapped ordinary citizens to use as cattle feed,\""

    zal "\"But most of the people who go missing nowadays aren't ordinary citizens; {w=0.5}it's people who either had a history with Myers, {w=0.5}or who were former employees of Myers.\""

    hide zalmona_accepting with Dissolve(0.2)

    zal "\"Did Myers Corporation turn them into cyborgs as well? {w=0.5}Or were they just used as cattle feed?\""

    van "\"Hmm... {w=0.5}If they were all once somehow once associated with Myers, {w=0.5}it makes sense that Myers would simply want them gone.\""

    zal "\"Precisely. {w=0.5}But many people believe that this series of disappearances is the work of just one person.\""

    zal "\"A dangerous criminal who is extremely careful, {w=0.5}so much so that they've never left a single fingerprint behind, {w=0.5}or a clue as to what really happened to the victims.\""

    zal "\"And this person- {w=0.5}is known as {color=#f00}the most wanted criminal in the G4 district{/color}.\""

    zal "\"As for how they are connected to Myers... {w=0.5}no one is really sure. {w=0.5}But there is one person who has seen them that is still alive.\""

    van "\"Only one person? {w=0.5}Who is that?\""

    show zalmona_accepting at zal_pos_2 with Dissolve(0.2)

    zal "\"That person... {w=0.5}{color=#f00}is me{/color}.\""

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/shock2.ogg" fadeout 2.0

    van "!?" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    hide zalmona_accepting with Dissolve(0.2)

    zal "\"Yes. {w=0.5}The most wanted criminal in the G4 district messed up once, {w=0.5}and I was there when it happened.\""

    scene black with Dissolve(1.0)

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music "music/creepy.wav"

    pause 3.0

    zal "\"It was a dark and windy night...\""

    window hide

    scene engineering_room_zal_story_apartment with Dissolve(1.0)
    show engineering_room_zal_story_shadow:
        xoffset 600
        ease 2.0 xoffset 0
    show engineering_room_zal_story_zal_normal:
        xoffset 600
        ease 2.0 xoffset 0
    show dust:
        alpha 0
        block:
            ease 5.0 alpha 0.5
            ease 5.0 alpha 1.0
            ease 5.0 alpha 0.5
            ease 5.0 alpha 0
            pause 5.0
            repeat
    $ renpy.pause(1.0, hard='True')

    zal "\"I had just gotten back to my apartment building, {w=0.5}and was about to go inside my apartment to relax.\""

    show electricity_going_out

    $ renpy.music.set_volume(0.3, delay=0, channel='electricity')
    $ renpy.music.play("music/electricity.ogg", channel="electricity", loop=False)

    pause 2.0
    $ renpy.pause(1.5, hard='True')
    $ renpy.music.stop(channel="electricity", fadeout = 1.0)
    hide electricity_going_out
    scene black

    pause 2.0

    zal "\"But as I was walking past an apartment on the same floor, {w=0.5}the power went out.\""

    zal "\"The hallway was enveloped in complete darkness. {w=0.5}I couldn't see anything around me.\""

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/engineering room/emanon_scream.ogg"

    pause 3.0

    zal "\"Just then-\""

    zal "\"I heard blood curdling screams accompanied with what sounded like flesh being torn off the bone from the apartment next to me.\""

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/engineering room/DoorBreakDown.ogg"
    queue sound "music/run.ogg"

    pause 2.0

    zal "\"A person rushed out of the apartment and brushed past me.\""

    zal "\"They were in such a panic that I wasn't even sure if they noticed my presence.\""

    pause 1.0

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/KILLSWITCH.ogg"

    scene engineering_room_zal_story_apartment_blood
    show engineering_room_zal_story_shadow
    show engineering_room_zal_story_zal_normal
    with Dissolve(0.5)

    $ renpy.pause(0.5, hard='True')
    pause 1.0

    zal "\"Shortly afterwards, {w=0.5}the power came back on. {w=0.5}But that person was long gone.\""

    hide engineering_room_zal_story_zal_normal
    show engineering_room_zal_story_zal_panic
    with Dissolve(0.2)

    pause 1.0

    zal "\"And the hallway that had been spotless beforehand...\""

    zal "\"Was completely different after the power was restored.\""

    zal "\"The walls and floor were painted red with blood.\""

    zal "\"And the apartment's door, {w=0.5}which had previously been closed, {w=0.5}was half ajar.\""

    zal "\" 'Holy shit. {w=0.5}This is serious!' \""

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/quiet open door.ogg"

    scene black with Dissolve(1.0)

    zal "\"Without thinking much, {w=0.5}I pushed open the door of the apartment to check in on my neighbor.\""

    pause 2.0

    stop music fadeout 3.0

    zal "\"And what I saw before me-\""

    zal "\"Was the most horrible thing I have ever seen in my life.\""

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music "music/scary violin loop.ogg" fadeout 2.0

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/jumpscare/jumpscare 1.ogg")

    scene engineering_room_zal_story_emanon:
        zoom 1.5 xoffset -20 yoffset -20
        pause 1.0
        ease 1.0 zoom 1 xoffset 0 yoffset 0
        block:

            ease 2.5 zoom 1.05 xoffset -30 yoffset -35

            ease 2.5 zoom 1 xoffset 0 yoffset 0

            repeat
    show bad_tv_signal onlayer tvsignal:
        linear 1.0 alpha 0.5
        linear 1.0 alpha 0.2
        repeat
    show white back:
        zoom 1.5 alpha 1
        ease 0.5 alpha 0
    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 0.5, dist=70))
    $ renpy.pause(0.5, hard='True')

    hide white back

    $ renpy.pause(1.0, hard='True')

    zal "\"A man on the floor, {w=0.5}his body shredded to bits.\""

    zal "\"The room was strewn with pieces of his body and entrails.\""

    zal "\"But that wasn't even the worst part. {w=0.5}The scariest thing was-\""

    zal "{color=#f00}\"Even though his head was completely detached from his body, {w=0.5}his mouth was still opening and closing, {w=0.5}as if he were desperately trying to catch his breath.\"{/color}"

    show character_icon_box:
        xpos 1350 ypos 300
        easein_expo 1.0 xpos 800 ypos 300
    show zalmona_icon_panic:
        xpos 1350 ypos 298
        easein_expo 1.0 xpos 800 ypos 298
        xpos 800 ypos 298

    zal "\" 'Hey, {w=0.5}hey! {w=0.5}Hang in there! {w=0.5}I'll call an ambulance right away!' \""

    hide character_icon_box
    hide zalmona_icon_panic
    with Dissolve(0.5)

    zal "\"I impulsively rushed to help him, {w=0.5}even though I knew very well that it was much too late.\""

    scene black
    hide bad_tv_signal onlayer tvsignal
    with Dissolve(1.0)

    zal "\"Just then, {w=0.5}some of the neighbors had heard the scream and rushed over.\""

    zal "\"But my attempts to help the victim were misunderstood.\""

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/shake.ogg"

    n1 "{size=+8}\" 'Hey! {w=0.5}What do you think you're doing!' \"{/size}" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    n2 "{size=+8}\" 'Murderer! {w=0.5}She's a murderer!' \"{/size}"

    n3 "{size=+8}\" 'Grab her! {w=0.5}Don't let her get away!' \"{/size}"

    show character_icon_box:
        xpos 1350 ypos 300
        easein_expo 1.0 xpos 800 ypos 300
    show zalmona_icon_panic:
        xpos 1350 ypos 298
        easein_expo 1.0 xpos 800 ypos 298
        xpos 800 ypos 298

    zal "\" 'Wait, {w=0.5}wait! {w=0.5}I can explain!' \""

    hide character_icon_box
    hide zalmona_icon_panic
    with Dissolve(0.5)

    pause 2.0

    stop music fadeout 3.0

    zal "\"But it was too late for me to say anything.\""

    $ say_who = ""

    scene engineering_room_2
    show zalmona_drop_shadow at zal_pos_2
    show zalmona_normal at zal_pos_2
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    window show

    van "\"And then? {w=0.5}What happened after that?\""

    $ say_who = _("Zalmona")

    $ renpy.music.set_volume(0.2, delay=0, channel='sound')
    play sound "music/zalmona/Zalmona-hnnnnn.ogg"

    show zalmona_happy at zal_pos_2
    with Dissolve(0.2)

    zal "\"After that... {w=0.5}As embarrassing as it sounds, {w=0.5}{color=#f00}I became G4's most wanted criminal{/color}.\""

    zal "\"Although I've managed to escape from the G4 police,\""

    zal "\"It's getting so much harder finding a new apartment these days.\""

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/shake.ogg"

    hide zalmona_happy
    show zalmona_panic at zal_pos_2

    zal "\"But please believe me-\"" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    zal "\"I really wasn't the one who killed him! {w=0.5}I wouldn't even hurt a fly!\""

    $ say_who = ""

    window hide

    pause 1.0

    window show

    van "\"I believe you, {w=0.5}Zalmona.\""

    van "\"But then... {w=0.5}you didn't actually get a good look at him either.\""

    hide zalmona_panic
    show zalmona_accepting at zal_pos_2
    with Dissolve(0.2)

    $ say_who = _("Zalmona")

    zal "\"*Sigh* {w=0.5}You're right.\""

    zal "\"The corridor was completely dark when I met him. {w=0.5}I didn't get to see what he looked like either.\""

    van "\"If that's the case, {w=0.5}how can you be so sure that the killer is the same person who is responsible for the recent series of disappearances in G4?\""

    hide zalmona_accepting
    with Dissolve(0.2)

    $ renpy.music.set_volume(0.4, delay=0, channel='music')
    play music ["<silence 1.0>", "music/myers lobby/were-loosing-time.ogg"] fadein 3.0

    zal "\"Honestly, {w=0.5}I can't.\""

    zal "\"But I later learned that the victim, {w=0.5}my neighbor, {w=0.5}was {color=#f00}Dr. Richard Emanon{/color}, {w=0.5}a former employee of Myers.\""

    zal "\"And, {w=0.5}as always, {w=0.5}the police found no fingerprints from any suspects at the scene.\""

    show zalmona_happy at zal_pos_2
    with Dissolve(0.2)

    zal "\"*Whisper* {w=0.5}Of course, {w=0.5}except for mine...\""

    hide zalmona_happy with Dissolve(0.2)

    zal "\"That's too much of a coincidence, {w=0.5}don't you think?\""

    zal "\"So my guess is-\""

    zal "\"The killer was originally going to kidnap Dr. Emanon and murder him somewhere else.\""

    show zalmona_accepting at zal_pos_2 with Dissolve(0.2)

    zal "\"But for some reason, {w=0.5}he screwed up that time.\""

    zal "\"So he killed Dr. Emanon in a hurry, {w=0.5}and ran away.\""

    hide zalmona_accepting with Dissolve(0.2)

    zal "\"And what's even more interesting is-\""

    zal "\"The way Dr. Emanon was murdered was very similar to how the core members were killed in the G4 Cyborg Incident-\""

    zal "\"They were all ripped to pieces.\""

    zal "\"So it's quite possible that this is the same person who got away with killing the core members.\""

    window hide

    pause 1.0

    window show

    van "\"Then the reason you were looking for the cyborg's memory core is...\""

    show zalmona_accepting at zal_pos_2 with Dissolve(0.2)

    zal "\"Yes. {w=0.5}As I was saying, {w=0.5}many of the victims of the recent unexplained disappearances have some connection to Myers.\""

    zal "\"It's hard not to conclude that the murderer also has a very close relationship with Myers.\""

    hide zalmona_accepting with Dissolve(0.2)

    zal "\"And each of the cyborgs that Myers produces through cloning will have a memory core.\""

    zal "\"Each device stores certain memories, {w=0.5}giving the cyborgs the personalities they would lack otherwise.\""

    zal "\"Most of these memories are extracted from Myers employees.\""

    van "\"I understand now. {w=0.5}You want to find the real murderer by reading the memories in each memory core, {w=0.5}thus proving your innocence.\""

    show zalmona_accepting at zal_pos_2 with Dissolve(0.2)

    zal "\"Exactly. {w=0.5}Not just for my own sake, {w=0.5}but also for the safety of the G4 district.\""

    hide zalmona_accepting with Dissolve(0.2)

    zal "\"I will keep searching until I find out the truth. {w=0.5}Even if it's Myers Corporation who's behind all of this.\""

    window hide

    stop music fadeout 3.0

    pause 4.0

    $ renpy.music.set_volume(0.2, delay=0, channel='sound')
    play sound "music/zalmona/Zalmona-hnnnnn.ogg"

    show zalmona_happy at zal_pos_2 with Dissolve(0.2)

    window show

    zal "\"Alright, {w=0.5}that's all I have to say.\""

    zal "\"Anyway, {w=0.5}thanks again for helping me out.\""

    zal "\"Go ahead and take this key card.\""

    window hide

    $ renpy.music.set_volume(0.1, delay=0, channel='sound')
    play sound "music/cloth.mp3" fadeout 2.0

    pause 2.0

    van "I took the key card to the legal department that Zalmona handed to me."

    pause 2.0

    hide zalmona_happy with Dissolve(0.5)

    window show

    zal "\"But- {w=0.5}are you still going to continue your investigation?\""

    zal "\"You know, {w=0.5}if you want to get out of here with me right now, {w=0.5}that wouldn't be impossible.\""

    van "\"Huh? {w=0.5}But isn't the gate to the lobby... {w=0.5}closed?\""

    show zalmona_happy at zal_pos_2 with Dissolve(0.2)

    zal "\"I know I know. {w=0.5}But the truth is, {w=0.5}I accidentally forgot about this:\""

    $ say_who = ""

    $ renpy.music.set_volume(0.1, delay=0, channel='sound')
    play sound "music/cloth.mp3" fadeout 2.0

    show transparent dark-small:
        alpha 0.8
    with Dissolve(0.5)

    van "Zalmona took a watch out of her pocket."

    show engineering_room_zal_watch with Dissolve(0.5)

    $ renpy.music.set_volume(0.8, delay=0, channel='music')
    play music ["<silence 2.0>", "music/jazz.ogg"]
    queue music "music/jazz.ogg"

    van "\"Umm... {w=0.5}a watch?\""

    $ say_who = _("Zalmona")

    zal "\"Oh, {w=0.5}darling. {w=0.5}This watch is more than meets the eyes.\""

    zal "\"It was originally a gift from an old friend of mine, {w=0.5}but I have made a few modifications to it.\""

    zal "\"Just by wearing it, {w=0.5}I can teleport myself anywhere.\""

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/shake.ogg"

    van "(...How did you forget something this important!?)" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    hide transparent dark-small
    hide engineering_room_zal_watch
    with Dissolve(0.5)

    hide zalmona_happy
    show zalmona_surprised at zal_pos_2
    with Dissolve(0.2)

    zal "\"But the downside is...\""

    zal "\"It can teleport me anywhere.\""

    van "\"...What do you mean?\""

    hide zalmona_surprised
    show zalmona_happy at zal_pos_2
    with Dissolve(0.2)

    zal "\"As in...\""

    zal "\"I can't decide where we'll be teleported to. {w=0.5}Hehe.\""

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/shake.ogg"

    van "\"......\"" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

    hide zalmona_happy
    show zalmona_surprised at zal_pos_2
    with Dissolve(0.2)

    zal "\"I was once teleported inside a men's bathhouse- {w=0.5}incredibly embarrassing situation.\""

    hide zalmona_surprised
    show zalmona_happy at zal_pos_2
    with Dissolve(0.2)

    zal "\"But hey, {w=0.5}there's risks with anything, {w=0.5}wouldn't you agree?\""

    hide zalmona_happy with Dissolve(0.2)

    stop music fadeout 3.0

    zal "\"So, {w=0.5}are you gonna come with me? {w=0.5}Let's get the hell out of here.\""

    $ say_who = ""

    van "\"......\""

    window hide

    pause 2.0

    window show

    $ renpy.music.set_volume(0.8, delay=0, channel='music')
    play music ["<silence 2.0>", "music/bgm/ankari-sad-2.ogg"]
    queue music "music/bgm/ankari-sad-2.ogg"

    van "\"I'm sorry, {w=0.5}Zalmona. {w=0.5}I can't leave just yet.\""

    van "\"There's this person that, {w=0.5}even though I can't remember how we're connected or why, {w=0.5}he was willing to risk his life for me.\""

    van "\"And that person is currently trapped in the Myers lobby. {w=0.5}I'm worried about him.\""

    $ say_who = _("Zalmona")

    zal "\"......\""

    show zalmona_accepting at zal_pos_2
    with Dissolve(0.2)

    zal "\"I see.\""

    hide zalmona_accepting with Dissolve(0.2)

    zal "\"Do you want me to come with you?\""

    van "\"No, {w=0.5}Zalmona, {w=0.5}that would be too dangerous.\""

    van "\"This is all my fault. {w=0.5}I should never have come here.\""

    van "\"I can't get another one of my friends involved. {w=0.5}I don't want to see them get hurt.\""

    zal "\"......\""

    show zalmona_accepting at zal_pos_2
    with Dissolve(0.2)

    zal "\"I understand.\""

    hide zalmona_accepting with Dissolve(0.2)

    zal "\"If that's the case, {w=0.5}promise me that you will take care of yourself. {w=0.5}I hope we can meet again someday.\""

    zal "\"Maybe then... {w=0.5}you will be able to tell me your real name.\""

    show zalmona_happy at zal_pos_2
    with Dissolve(0.2)

    zal "\"I'll see you later, {w=0.5}Miss. {w=0.5}When you get your memories back, {w=0.5}be sure to tell me all the stories about your past, {w=0.5}alright?\""

    van "\"Of course. {w=0.5}Goodbye, {w=0.5}Zalmona!\""

    stop music fadeout 6.0

    window hide

    show white back
    hide zalmona_happy
    hide zalmona_normal
    hide zalmona_drop_shadow
    $ renpy.transition(Dissolve(0.1))
    $ renpy.pause(0.1, hard='True')

    $ renpy.music.set_volume(0.7, delay=0, channel='sound')
    play sound "music/teleport.ogg"

    $ renpy.pause(1.0, hard='True')

    hide white back
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(1.0, hard='True')

    $ say_who = ""

    pause 1.0

    van "!?"

    van "She's gone."

    van "I wonder where she will be teleported to this time..."

    pause 2.0

    van "Well then, {w=0.5}it is time for me to push forward as well."

    scene black with Dissolve(0.5)

    pause 1.0

    van "Next stop..."

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/engineering room/swipe card.ogg"

    $ renpy.pause(1.5, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/engineering room/door accept beep.ogg"

    van "{color=#f00}The Legal Department.{/color}"

    $ renpy.pause(0.5, hard='True')

    show engineering_room_door_to_legal_2
    show engineering_room_door_to_legal_1
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(1.0, hard='True')

    $ renpy.music.set_volume(0.7, delay=0, channel='sound1')
    $ renpy.music.play("music/engineering room/electric garage door.ogg", channel="sound1", loop=False)

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/flashback.ogg")

    $ renpy.pause(0.2, hard='True')

    show engineering_room_door_to_legal_2:
        zoom 1 xoffset 0 yoffset 0
        ease 2.0 xoffset 0 yoffset -700
    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 2.0, dist=15))
    $ renpy.pause(2.0, hard='True')

    $ renpy.music.stop(channel = "sound1", fadeout = 1.0)

    $ renpy.pause(2.0, hard='True')

    show engineering_room_door_to_legal_1:
        ease 0.4 zoom 10.0 yoffset 3500 xoffset 2500
    $ renpy.pause(0.4, hard='True')
    scene black

    $ renpy.pause(1.5, hard='True')

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ renpy.music.stop(channel="beep", fadeout = 0.5)
    $ _skipping = False

    $ renpy.pause(0.5, hard='True')

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/UI Dark.ogg"

    noname "Investigation completed. {w=0.5}Successfully located the cyborg's memory core."

    jump legal_department_start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
