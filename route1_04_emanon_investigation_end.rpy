
image emanon_investigation_claude_1 = "images/emanon murder scene/emanon_investigation_claude_1.png"
image emanon_investigation_claude_2 = "images/emanon murder scene/emanon_investigation_claude_2.png"
image emanon_investigation_claude_light = "images/emanon murder scene/emanon_investigation_claude_light.png"
image emanon_apartment_street = "images/emanon murder scene/emanon_apartment_street.png"


image basement_broken_elevator_1 = "images/chapter3-end/chapter3-end-elevator-1.png"
image basement_broken_elevator_2 = "images/chapter3-end/chapter3-end-elevator-2.png"


image emanon_investigation_vin_mansion_1 = "images/emanon murder scene/emanon_investigation_vin_man1.png"
image emanon_investigation_vin_mansion_2 = "images/emanon murder scene/emanon_investigation_vin_man2.png"
image emanon_investigation_vin_mansion_3 = "images/emanon murder scene/emanon_investigation_vin_man3.png"
image emanon_investigation_vin_mansion_4 = "images/emanon murder scene/emanon_investigation_vin_man4.png"


label finish_emanon_investigation_click:

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/UI Dark.ogg"

    window show
    stop music fadeout 2.0
    $ _skipping = True
    $ renpy.block_rollback()

    noname "Investigation completed."

    $ _skipping = True
    $ _rollback = True

    v "I believe I've gathered enough information to postulate at what may have happened."

    $ rollback_ = True

    $ renpy.music.set_volume(0.4, delay=0, channel='music')
    play music "music/myers lobby/were-loosing-time.ogg" fadein 3.0

    v "It's clear that this murder was premeditated. {w=0.5}The perpetrator was planning to kill Dr. Emanon from the very beginning."

    v "And since the window lacked any signs of force entry, {w=0.5}it's most probable that the culprit entered the apartment directly through the door."

    v "That means the murderer was invited into the apartment by Dr. Emanon himself. "

    v "In other words, {w=0.5}our murderer is most likely whoever Dr. Emanon was making his {color=#f00}\"deal\"{/color} with."

    v "Nonetheless,{w=0.5} in the midst of this, {w=0.5}a small mishap occurred."

    v "The killer intended to kill Dr. Emanon directly by hitting him on the head with the trophy."

    v "But the sudden power failure in the apartment made him miss and he failed to kill Dr. Emanon with a single blow."

    v "-Which is understandable. {w=0.5}No one could anticipate a freak blackout."

    v "However, {w=0.5}if the killer is the same person that's behind the other recent G4 disappearances, {w=0.5}then their negligence cannot be attributed to just that."

    v "The other victims who went missing disappeared without a trace, {w=0.5}as if they had vanished into thin air."

    v "But this time, {w=0.5}the murderer messed up the whole apartment and attracted the attention of other residents."

    v "If it's really the same perpetrator, {w=0.5}there has to be something else that also contributed to such a major mistake."

    v "In fact, {w=0.5}the murderer could very well..."

    window hide

label emanon_investigation_end_q_1:

    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    menu:
        "Be very handsome":


            $ renpy.block_rollback()

            $ renpy.music.set_volume(0.8, delay=0, channel='sound')
            play sound "music/selectsounds.ogg"

            $ renpy.pause(0.1, hard='True')
            pause 0.2
            $ renpy.pause(0.1, hard='True')
            $ renpy.music.set_volume(0.8, delay=0, channel='sound')
            play sound "music/wrong.ogg"
            show screen wrong with Dissolve(0.5)
            $ renpy.pause(0.1, hard='True')
            pause 0.5
            $ renpy.pause(0.1, hard='True')
            hide screen wrong with Dissolve(0.5)
            $ renpy.pause(0.1, hard='True')

            $ renpy.block_rollback()

            v "...I don't think this has anything to do with my deduction."

            $ renpy.block_rollback()

            jump emanon_investigation_end_q_1
        "Be seriously injured":


            $ renpy.block_rollback()

            $ renpy.music.set_volume(0.8, delay=0, channel='sound')
            play sound "music/selectsounds.ogg"

            $ renpy.pause(0.1, hard='True')
            pause 0.2
            $ renpy.pause(0.1, hard='True')
            $ renpy.music.set_volume(0.8, delay=0, channel='sound')
            play sound "music/wrong.ogg"
            show screen wrong with Dissolve(0.5)
            $ renpy.pause(0.1, hard='True')
            pause 0.5
            $ renpy.pause(0.1, hard='True')
            hide screen wrong with Dissolve(0.5)
            $ renpy.pause(0.1, hard='True')

            $ renpy.block_rollback()

            v "It seems unlikely that the murderer was in critical condition."

            $ renpy.block_rollback()

            jump emanon_investigation_end_q_1
        "Have been reluctant to kill Dr. Emanon":


            $ renpy.block_rollback()

            $ renpy.music.set_volume(0.8, delay=0, channel='sound')
            play sound "music/selectsounds.ogg"

            $ renpy.pause(0.1, hard='True')
            pause 0.2
            $ renpy.pause(0.1, hard='True')
            $ renpy.music.set_volume(0.8, delay=0, channel='sound')
            play sound "music/wrong.ogg"
            show screen wrong with Dissolve(0.5)
            $ renpy.pause(0.1, hard='True')
            pause 0.5
            $ renpy.pause(0.1, hard='True')
            hide screen wrong with Dissolve(0.5)
            $ renpy.pause(0.1, hard='True')

            $ renpy.block_rollback()

            v "Given the current status of Dr. Emanon, {w=0.5}I highly doubt that this was the case."

            $ renpy.block_rollback()

            jump emanon_investigation_end_q_1
        "Have an extreme fear of the dark":


            $ renpy.block_rollback()

            $ renpy.music.set_volume(0.8, delay=0, channel='sound')
            play sound "music/selectsounds.ogg"

            $ renpy.pause(0.1, hard='True')
            pause 0.2
            $ renpy.pause(0.1, hard='True')
            $ renpy.music.set_volume(0.5, delay=0, channel='sound')
            play sound "music/correct.ogg"
            show screen correct with Dissolve(0.5)
            $ renpy.pause(0.1, hard='True')
            pause 0.5
            $ renpy.pause(0.1, hard='True')
            hide screen correct with Dissolve(0.5)
            $ renpy.pause(0.1, hard='True')

    v "{color=#f00}The murderer might have an extreme fear of the dark.{/color}"

    v "The curtains in the apartment were drawn closed at the time, {w=0.5}and it would have taken a while for human eyes to adjust to the sudden darkness."

    v "So at the moment of the blackout, {w=0.5}Dr. Emanon's apartment was most likely pitch black."

    v "Our cold-blooded assassin, {w=0.5}who usually manages to keep so calm and careful, {w=0.5}completely lost control in this apartment."

    v "It is quite possible that the killer has an extreme fear of sudden darkness due to some form of previous trauma."

    v "......"

    v "{color=#f00}Sudden darkness{/color}..."

    v "I see. {w=0.5}I think I understand now."

    v "......"

    v "In addition, {w=0.5}the manner of Dr. Emanon's death is a major mystery."

    v "The killer dismembered him alive, {w=0.5}after failing to kill him with a single blow."

    v "The way they dismembered him -"

    v "Reminds me of how all the core members of the Myers Corporation were killed."

    v "As far as I know, {w=0.5}all of the core members of Myers were also killed in a similarly brutal way."

    v "Add that to the recent disappearances in the G4 district, {w=0.5}leaving many citizens paranoid,"

    v "I guess many people would think that the killer is the same person who killed all the core members."

    v "However, {w=0.5}I believe that the real reason why the killer tore Dr. Emanon into pieces, {w=0.5}was:"

label emanon_investigation_end_q_2:

    $ renpy.music.stop(channel="beep", fadeout = 0.5)

    menu:
        "To give Dr. Emanon a painful death":

            jump emanon_investigation_end_q_2_wrong
        "To mimic the murders of the Myers' core members":

            jump emanon_investigation_end_q_2_wrong
        "To threaten the Myers Corporation":

            jump emanon_investigation_end_q_2_wrong
        "To collect Dr. Emanon's body parts":

            jump emanon_investigation_end_q_2_correct

label emanon_investigation_end_q_2_wrong:

    $ renpy.block_rollback()

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/selectsounds.ogg"

    $ renpy.pause(0.1, hard='True')
    pause 0.2
    $ renpy.pause(0.1, hard='True')
    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/wrong.ogg"
    show screen wrong with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')
    pause 0.5
    $ renpy.pause(0.1, hard='True')
    hide screen wrong with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')

    $ renpy.block_rollback()

    v "I don't think that was the murderer's true intention."

    $ renpy.block_rollback()

    jump emanon_investigation_end_q_2

label emanon_investigation_end_q_2_correct:

    $ renpy.block_rollback()

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/selectsounds.ogg"

    $ renpy.pause(0.1, hard='True')
    pause 0.2
    $ renpy.pause(0.1, hard='True')
    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    play sound "music/correct.ogg"
    show screen correct with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')
    pause 0.5
    $ renpy.pause(0.1, hard='True')
    hide screen correct with Dissolve(0.5)
    $ renpy.pause(0.1, hard='True')

    window show

    v "Some of Dr. Emanon's body parts have gone missing. {w=0.5}I don't remember that happening to any of the core members."

    v "The real reason why the killer dismembered Dr. Emanon in a panic, {w=0.5}was to obtain his body parts."

    v "In the G4 Cyborg Incident, {w=0.5}Myers Corporation was found to be using the human flesh of ordinary G4 citizens as feed for the cyborgs."

    v "But since Dr. Emanon's body did not have any signs of a beast attack,"

    v "The killer was most likely trying to obtain Dr. Emanon's body parts to use as feed for cyborgs at a later time."

    v "But if they were working for Myers..."

    v "Wouldn't it be more likely that they would want to make a cyborg out of Dr. Emanon?"

    v "Why would they choose to turn him into cyborg feed instead?"

    v "......"

    window hide

    stop music fadeout 3.0

    pause 3.0

    window show

    claude "\"Detective Vanora?\""

    v "!?"

    v "\"Yes?\""

    claude "\"Have you reached any conclusions to who the killer is?\""

    v "\"......\""

    v "\"Put out a warrant for the arrest of Zalmona. {w=0.5}She is undoubtedly the perpetrator we have been trying to search for all along.\""

    claude "\"...As you wish, {w=0.5}Detective Vanora.\""

    window hide

    show black
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    pause 2.0
    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/emanon crime scene/police siren.ogg"
    $ renpy.pause(2.0, hard='True')

    pause 2.0

    hide black
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    stop sound fadeout 5.0

    claude "\"The warrant has been issued.\""

    claude "\"But Detective Vanora, {w=0.5}would you mind coming outside with me for a moment? {w=0.5}There are some important matters I'd like to discuss with you.\""

    v "\"......?\""

    scene black
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(2.0, hard='True')

    $ renpy.music.set_volume(0.6, delay=0, channel='music')
    play music "music/night.ogg" fadein 2.0 fadeout 6.0

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/step on dirt.ogg")

    v "I followed him to the street outside the apartment."

    v "It was getting quite late, {w=0.5}and the temperature had dropped quite dramatically."

    v "But he was just walking in front of me silently, {w=0.5}as if the cold weather did not bother him."

    claude "\"......\""

    stop sound fadeout 2.0

    v "After a while, {w=0.5}he finally stopped in an alley where no one was nearby."

    pause 2.0

    v "\"What was it that you wanted to discuss?\"{w=0.5} I decided to speak first."

    claude "\"Well then, {w=0.5}let's hear it. {w=0.5}Who's the actual killer?\""

    v "\"......\""

    v "\"Excuse me?\""

    claude "\"...You're called the Inspector. {w=0.5}Yet you don't even realize who I am this whole time.\""

    stop music fadeout 2.0

    v "The man in front of me slowly took off his police hat, {w=0.5}and what followed was a sight that I couldn't have expected."

    window hide

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music ["<silence 1.0>", "music/bgm/lab investigation.ogg"]
    queue music "music/bgm/lab investigation.ogg"

    show grey-blue-bg:
        alpha 0
        ease 1.0 alpha 1.0

    show emanon_investigation_claude_1:
        xoffset 1000
        easein_expo 1.0 xoffset 0
    show emanon_investigation_claude_2:
        xoffset 1000 alpha 1
        easein_expo 1.0 xoffset 0 alpha 1
        ease 1.0 alpha 0
    show emanon_investigation_claude_light:
        alpha 0
        linear 1.0 alpha 0.5
        block:
            pause 1.5
            alpha 1.0
            linear 1.0 alpha 0.5
            pause 2.5
            alpha 1.0
            linear 1.0 alpha 0.5
            alpha 1.0
            linear 1.0 alpha 0.5
            repeat
    show dust


    $ renpy.pause(2.0, hard=True)
    pause 2.0

    v "He suddenly grabbed a corner of his cheek and tore the skin off his head."

    v "What was revealed beneath it was his blue skin and white hair."

    show emanon_investigation_claude_1:
        xoffset 0
        ease 0.8 xoffset -1400 alpha 0
    show emanon_investigation_claude_light:
        linear 1.0 alpha 0.5
    hide emanon_investigation_claude_2

    $ renpy.pause(0.3, hard=True)

    scene emanon_apartment_street
    show dust
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    pause 1.0

    $ claude_name = _("Police Officer?")

    v "\"...It's you.\""

    show claude_normal
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    pause 2.0

    window show

    v "But him revealing his true form only made me more vigilant."

    $ renpy.music.set_volume(0.7, delay=0, channel='sound')
    play sound "music/claude/Claude-1.ogg"

    show claude_speak with Dissolve(0.2)

    claude "\"Inspector, {w=0.5}it appears the fact that you still see me as a threat.\""

    claude "\"Believe it or not, {w=0.5}I don't have time to play Mr. triple agent for that stupid organization from G3.\""

    hide claude_speak with Dissolve(0.2)

    v "\"What are you doing here?\""

    show claude_speak with Dissolve(0.2)

    $ say_who = claude_name

    claude "\"What else can I be doing here? {w=0.5}Our boss gave me clear instructions to make sure you succeeded in your mission.\""

    claude "\"But it seems that you have everything under control.\""

    stop music fadeout 5.0

    show claude_annoyed with Dissolve(0.2)

    claude "\"However, {w=0.5}you know very well who the actual killer is, {w=0.5}don't you?\""

    claude "\"Just what the hell happened back there? {w=0.5}I thought he was good at this. {w=0.5}How could he screw up things this badly?\""

    show claude_annoyed_2 with Dissolve(0.2)

    v "\"......\""

    v "\"Why don't you just go ask him yourself?\""

    hide claude_annoyed_2
    hide claude_annoyed
    hide claude_speak
    with Dissolve(0.2)

    claude "\"......\""

    window hide

    $ renpy.music.set_volume(0.6, delay=0, channel='music')
    play music "music/night.ogg" fadein 2.0 fadeout 6.0

    pause 2.0

    window show

    $ renpy.music.set_volume(0.7, delay=0, channel='sound')
    play sound "music/claude/Claude-2.ogg"

    show claude_speak with Dissolve(0.2)

    claude "\"You're as tough as ever.\""

    claude "\"Suit yourself then. {w=0.5}I don't really give a damn about that guy's past.\""

    claude "\"But do we really have to pin it on that woman from the same floor?\""

    hide claude_speak with Dissolve(0.2)

    v "\"Each sacrifice is for the future of the company. {w=0.5}Each one is necessary.\""

    show claude_annoyed with Dissolve(0.2)

    claude "\"Cheh. {w=0.5}Our boss's really getting to you, {w=0.5}isn't he?\""

    claude "\"Company this, {w=0.5}company that... {w=0.5}That's all he ever talks about.\""

    claude "\"All of us are merely little pawns in his hands.\""

    v "\"What did you say?\""

    hide claude_annoyed
    show claude_speak
    with Dissolve(0.2)

    claude "\"No offense, {w=0.5}but this is nothing but a job to me.\""

    claude "\"I'm not trying to debate the ethics of what we do. {w=0.5}Nor am I interested in his 'great vision.'\""

    claude "\"And why don't you use your brain once, {w=0.5}and think about what you truly want instead of being a slave to his company all day?\""

    hide claude_speak with Dissolve(0.2)

    v "\"What I truly want?\""

    show claude_speak with Dissolve(0.2)

    claude "\"You know, {w=0.5}finding the love of your life, {w=0.5}forming a family, {w=0.5}that sort of thing.\""

    claude "\"Don't end up like me, {w=0.5}an old guy who still doesn't have a single clue what he should be doing in his life.\""

    hide claude_speak with Dissolve(0.2)

    $ say_who = ""

    v "\"......\""

    window hide

    pause 2.0

    show claude_speak with Dissolve(0.2)

    window show

    claude "\"*Sigh* {w=0.5}It's been an exhausting day. {w=0.5}I'll see you later.\""

    window hide

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/step on dirt.ogg")

    hide claude_speak
    hide claude_normal
    with Dissolve(1.0)

    stop sound fadeout 1.0

    pause 1.0

    v "He was about to turn to leave, {w=0.5}but he suddenly stopped again."

    show claude_normal with Dissolve(0.5)

    v "He once again turned his head at me."

    pause 1.0

    window show

    claude "\"......\""

    v "\"?\""

    show claude_speak with Dissolve(0.2)

    claude "\"Vanora? {w=0.5}Did you come up with that name yourself?\""

    hide claude_speak with Dissolve(0.2)

    v "\"......\""

    v "\"Yes.\""

    show claude_smile with Dissolve(0.2)

    $ renpy.music.set_volume(0.7, delay=0, channel='sound')
    play sound "music/claude/Claude-laugh.ogg"

    claude "\"...Hmm.\""

    v "The everso gloomy look of his face unusually perked up out of nowhere."

    show claude_smile_talk with Dissolve(0.2)

    claude "\"I didn't think you'd be so good at naming yourself.\""

    claude "\"That's a really nice name. {w=0.5}Why don't you keep it for yourself?\""

    hide claude_smile_talk with Dissolve(0.2)

    $ renpy.music.set_volume(0.1, delay=0, channel='sound')
    play sound "music/cloth.mp3" fadeout 2.0

    hide claude_smile
    hide claude_normal
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    v "With that, {w=0.5}he put on his police hat again."

    claude "\"See you later, {w=0.5}Vanora. {w=0.5}Make sure you report to that guy on time. {w=0.5}He's kind of anal about that.\""

    window hide

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/step on dirt.ogg")

    pause 2.0

    window show

    v "With that, {w=0.5}he disappeared across the street and once again became part of the crowd."

    window hide

    pause 2.0

    window show

    v "......"

    v "Finding the love of my life, {w=0.5}and starting my own family..."

    v "Is that still possible for someone like me?"

    window hide

    pause 2.0

    window show

    v "......"

    v "What am I thinking."

    v "......"

    stop music fadeout 3.0

    v "No matter what, {w=0.5}my mission here is accomplished."

    v "As long as the G4 Investigation Bureau can't figure out who the true killer is, {w=0.5}everything will still be under our control."

    v "It is time for me to move on to my next destination, {w=0.5}and complete my next mission."

    window hide

    scene black
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(1.0, hard='True')

    v "G4 suburbs -"

    v "{color=#f00}The mansion of Myers' former lawyer and traitor - {/color}"

    v "{color=#f00}Vincent Edgeworth.{/color}"

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "music/suspense 2.ogg"

    show white back as white_back:
        alpha 0.5
        ease 0.2 alpha 0
        alpha 0.5
        ease 0.2 alpha 0
        alpha 0.5
        ease 0.2 alpha 0
        alpha 0.5
        ease 0.2 alpha 0
        alpha 0.5
        ease 0.2 alpha 0
    show memory_frame behind white_back:
        linear 1.0 alpha 0.3
        linear 1.0 alpha 1
        repeat
    show emanon_investigation_vin_mansion_1 behind memory_frame
    $ renpy.pause(0.2, hard='True')
    show emanon_investigation_vin_mansion_2 behind memory_frame
    $ renpy.pause(0.2, hard='True')
    show emanon_investigation_vin_mansion_3 behind memory_frame
    $ renpy.pause(0.2, hard='True')
    show emanon_investigation_vin_mansion_4 behind memory_frame
    $ renpy.pause(0.2, hard='True')
    $ renpy.transition(Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15))
    scene black

    $ renpy.pause(4.0, hard='True')

    $ renpy.music.set_volume(0.1, delay=0, channel='electricity')
    $ renpy.music.play("music/electricity.ogg", channel="electricity", loop=True, fadein=3.0)

    show basement_broken_elevator_2
    show legal_department_elevator_2:
        alpha 0
        pause 0.2
        alpha 0.3
        pause 1.0
        alpha 0.2
        pause 0.5
        alpha 0
        pause 0.1
        alpha 0.4
        pause 0.1
        alpha 0.3
        pause 0.1
        alpha 1.0
        alpha 0.1
        repeat
    show basement_broken_elevator_1
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(3.0, hard='True')

    $ renpy.music.set_volume(0.5, delay=0, channel='music')
    play music "music/horror build up.ogg"

    window show

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/vanora/van heavy breath.ogg") fadeout 1.0

    van "\"Vincent Edgeworth! {w=0.5}That name, {w=0.5}I remember now!\""

    van "\"That man... {w=0.5}is {color=#f00}far more frightening than Myers.{/color}\""

    van "\"I've been set up! {w=0.5}I have to get out of here!\""

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "music/vin_hmm.ogg"

    vin "\"Is that my name I'm hearing, {w=0.5}[name!t]?\""

    van "!?"

    show vin_smile
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    vin "\"Or should I call you...\""

    show vin_smile:
        linear 0.5 xpos 0.73

    $ renpy.pause(0.5, hard='True')

    $ renpy.music.stop(channel="electricity", fadeout = 4.0)

    show vanora_normal at van_pos_1
    show vin_dark_smile at vin_pos_2
    hide vin_smile
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    vin "\"{color=#f00}Vanora{/color}?\""

    window hide

    $ renpy.pause(2.0, hard='True')

    stop music fadeout 1.0

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ("music/demo end impact.ogg")
    scene black

    $ renpy.pause(1.0, hard='True')
    pause 3.0

    if renpy.is_skipping():
        $ renpy.choice_for_skipping()
    $ _skipping = False

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/UI Dark.ogg"

    window show

    noname "Chapter Three: {w=0.5}The End"



    window hide


    jump college_start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
