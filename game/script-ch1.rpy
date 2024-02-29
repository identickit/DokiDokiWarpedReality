default persistent.whereami = 0
default persistent.deletionload = 0

label ch1_p1:
    #scene 1
    $ mgmode = False
    $ kgmode = False
    $ persistent.whereami = 1
    $ persistent.deletionload = 0
    $ persistent.poemsecond = False
    stop music fadeout .5
    scene bg residential_day
    with dissolve_scene_full
    play music t2
    $ persistent.whereami = 1
    $ persistent.deletionroute = False
    $ persistent.poemsecond = False
    $ persistent.CONDITION = 0
    $ k_name = "???"
    "ACT I - Broken Reality"
    k "Hey there, [player]!"
    show kotonoha kg at t11
    $ k_name = "Kotonoha"
    k 1a"Glad to see you finally decided to get up."
    "I just sigh to myself. Kotonoha always nags me for small things like this."
    "Anytime I take a while to get ready for school, for instance, she'll start joking like this."
    "But I know she doesn't mean any harm in doing stuff like that."
    show bg qgresidential_day
    $ renpy.sound.play ("sfx/glitch3.ogg")
    "The two of us begin our daily commute to school."
    k "Anyway, have you considered joining any clubs yet?"
    mc "Huh? I thought I already said I'm not interested in joining-{nw}"
    $ _history_list.pop()
    $ style.say_window = style.windowqg
    pause 0.25
    $ style.say_window = style.window
    mc "Huh? I thought I already said I'm interested in possibly joining your club?"
    k 1h "Ah, how could I forget?"
    show kotonoha 1a at t11
    "Kotonoha smiles and doesn't say much else to me the rest of the way to school."
    "We've always walked to school together like this..."
    show bg qgresidential_day
    $ renpy.sound.play ("sfx/glitch3.ogg")
    "... But she's usually not this silent."
    "My train of thought is broken by an overly-energetic girl approaching us."
    show kotonoha 1e zorder 2 at t21
    show sayori turned happ om oe zorder 2 at f22
    s "Hey, Kotonoha!"
    show sayori cm at t22
    show kotonoha at f21
    k 1d "Good morning, Sayori."
    $ s_name = "Sayori"
    k 1a "How's the Literature Club's very own Vice President holding up this morning?"
    show kotonoha at t21
    show sayori laug om ce at f22
    s "Hungry."
    show sayori cm at t22
    mc "As usual."
    "Sayori giggles and joins us on our walk."
    show sayori at thide
    show kotonoha at thide
    hide sayori
    hide kotonoha
    "I haven't known Sayori very long, but she always seems to be full of positivity."
    "Being entirely honest with myself, I wouldn't have imagined being friends with someone like her had she not been friends with Kotonoha."
    "But when you get to know her, Sayori is a pretty fun person to be around."
    "{cps=30}We reach the front door of the school-{/cps}{nw}"
    stop music
    show bg qgresidential_day

    #scene 2
    $ persistent.whereami = 2
    $ persistent.deletionroute = False
    $ persistent.poemsecond = False
    $ persistent.CONDITION = 0
    $ m_name = "Monika"
    play music t3
    scene bg club_day
    show monika lean happ om oe at t11
    m "Then that makes it official!"
    m "Welcome to the Literature Club!"
    show monika forward happ oe cm at t11
    mc "Ah... thanks, I guess."
    show monika om lpoint at t11
    m "Okay, everyone!"
    m "I think with that, we can officially end today's meeting on a good note."
    show monika ce at t11
    m "Everyone remember tonight's assignment:"
    m "Write a poem to bring to the next meeting, so we can all share!"
    $ mref()
    show monika lean at t11 
    "Monika looks at me once more."
    m "[player], I look forward to seeing how you express yourself."
    show monika zorder 2 at t21
    show kotonoha 1a zorder 2 at t22 
    k "Monika, we aren't already picking favorites are we?"
    show monika forward anno cm oe zorder 2 at t21
    "Monika straightens up almost immediately, a serious expression now replacing the happy one that was there seconds ago."
    show monika at f21
    m "Kotonoha, I think we already agreed that you being this club's senior member doesn't mean you can correct every little thing I do."
    show monika at t21
    show kotonoha at f22
    k 1h "Oh, don't worry, Miss President. I know my place quite well."
    k "(... even if {i}somebody{/i} thinks she can control everything.)"
    show kotonoha at t22
    show monika forward angr cm oe at f21
    m "You know I can hear you."
    show monika at t21
    stop music fadeout 1.0
    show kotonoha 1f at f22
    k "Yes. Yes I do."
    k "Just like I know the things you'll end up doing to everyone else here just to be with [player]."
    show kotonoha at t22
    show bg clubdaypause
    pause 0.5
    show bg clubdayg4
    with Dissolve(1.0)
    show monika at f21
    m "You know I remember everything from my past experiences. I'm not horrible enough to not learn from those mistakes."
    show monika at t21
    show kotonoha 1h at f22
    k "Sure, sure. Whatever you say."
    show kotonoha at t22
    show monika at f21
    m "Oh, and Kotonoha?"
    show kotonoha 1a at f22
    show monika at t21
    k "Yes, Monika?"
    show kotonoha at t22
    show monika at f21
    m "Just because you have some control over the game doesn't mean you get to openly talk about the reality of this world."
    m "If the others knew what happens behind closed doors..."
    show monika ce at f21
    m "... Take Sayori for example."
    m "If she knew about everything this early, she literally wouldn't be able to handle it."
    m "The game would immediately be over."
    show monika oe at f21
    m "End."
    show monika at t21
    show kotonoha 1e at f22
    k "..."
    k "... Fine."
    k "But that doesn't give you any right to try and keep [player] all to yourself or act all-important."
    show kotonoha at t22
    show monika at f21
    m "That's funny to hear coming from you."
    m "Didn't you just abruptly insert yourself into the beginning of the story and then force everything to skip to the next time you're around?"
    show monika at t21
    show kotonoha 1u3 at f22
    k "I have a right to spend a little extra time with [player]!"
    k "You've always been in control, always inevitably trapping him and making him spend time with you."
    k "Have you ever considered the fact that I might want that sort of opportunity?"
    k "And I already told you that this is my chance to have a better light shined on me."
    k "I just want to be the same as you!"
    show kotonoha 1u at t22
    show monika forward neut cm ce at f21
    m "..."
    m "... Alright Kotonoha. How about this:"
    m "If you promise to be fair and rational about trying to spend time with [player]..."
    m "... Then I guess it's fine."
    show monika at t21
    show kotonoha 1a at f22
    k "{cps=30}Funny how you think-{nw}{/cps}"
    show kotonoha at t22
    show monika oe at f21
    m "I'm not finished."
    m "You have to give me some kind of route as well."
    m "And you have to give one to everyone in this club. Even Rikka and whoever else isn't officially a part of this world."
    show monika at t21
    show kotonoha 1e at f22 
    k "..."
    k "....."
    show kotonoha at t22
    show monika at f21
    m "Is that good enough for you, Kotonoha?"
    show monika at t21
    show kotonoha 1q at f22
    k "...Fine. Yes."
    show kotonoha 1p at f22
    k "Just... give me a minute to add some files for everyone."
    "{cps=30}(Key word in her remark there being some--{nw}{/cps}"
    $ persistent.deletionroute = False
    $ persistent.poemsecond = False
    $ persistent.CONDITION = 0
    show kotonoha at thide
    hide kotonoha
    show monika at thide
    hide monika
    window hide
    show bg clubdayg
    pause(3.0)
    return

label ch1_p2:
    #scene 3
    $ persistent.whereami = 3
    $ persistent.deletionroute = False
    $ persistent.poemsecond = False
    $ persistent.CONDITION = 0
    scene bg club_day
    stop music fadeout .5
    play music wn6 fadein 1.0
    show monika forward happ om ce at t11
    m "Hello again, [player]!"
    m "{cps=30}It's great to see you-{nw}{/cps}"
    show monika forward neut cm oe at t21
    show kotonoha 1u at t22
    "I hear someone clear their throat from across the room."
    "Kotonoha is giving Monika a disappointed look. Did something happen after I left the club yesterday?"
    "Wait... Now that I think about it, I can't even remember leaving the-{nw}"
    show monika forward happ cm ce at f21
    m "My apologies, Koto! Just wanted [player] to feel welcome."
    show monika at t21
    show kotonoha 1h at f22
    k "Ah, I see..."
    show kotonoha 1a at f22
    k "In any case, we should let him get to whatever it is he had planned for today."
    show kotonoha at t22
    show monika at f21
    m "Right. I'll be talking with our resident vice president and senior member if you need anything, [player]~"
    show kotonoha at thide
    hide kotonoha 
    if poemwinner[0] != "monika":
        show monika forward anno cm oe at t11
        m "Enjoy yourself."
    show monika at thide
    hide monika
    "I guess that means I should take my seat now."
    "I look around the clubroom as I set my stuff down at my desk."
    "Monika, Sayori, and Kotonoha are having a lively discussion in the corner of the room."
    "Rikka seems to already be getting started on some sort of homework."
    "Yuri is intensely reading a book, as if she was waiting all day for the opportunity."
    "Meanwhile, Natsuki is rummaging around in the closet--"

    #scene 4
    $ persistent.whereami = 4
    $ persistent.deletionroute = False
    $ persistent.poemsecond = False
    $ persistent.CONDITION = 0
    "The door opens."
    "Everyone looks up to see who just entered the room."
    scene bg qgclubday
    $ renpy.sound.play ("mod_assets/sfx/glitch2.ogg")
    "Monika and Kotonoha both look shocked, and I can't say I blame them."
    "The guy who just walked in does {i}not{/i} look like the Literature Club was his first choice."
    scene black
    stop music fadeout 1
    with dissolve_scene_half
    pause 1
    play music wn7
    scene bg club_day
    with dissolve_scene_half
    "...Guess we're really doing this."
    "As soon as I enter the room, all eyes fall on me."
    "Instantly, I recognize Sayori, who looks genuinely ecstatic."
    $ s_name = "Sayori"
    "{cps=24}I glance at-{nw}{/cps}"
    show sayori turned lsur om oe zorder 2 at t11
    s "Oh my gosh!"
    show sayori turned happ om ce lup rup zorder 2 at h11
    s "Oh my gosh!!!"
    w "{cps=12}Wait-{nw}{/cps}"
    show sayori cm ce at t11
    "Before I can stop her, Sayori wraps her arms around me and jumps up and down a few times."
    show sayori at t21
    show monika forward nerv cm ce zorder 2 at f22 
    m "Sayori, you can't just charge at a visitor like that!"
    show monika at t22
    "Sayori lets go but doesn't look very sorry."
    show sayori happ om oe ldown rdown at f21
    s "I knew you would join, [w_name]!"
    show sayori at t21
    w "Hey, wait a minute!"
    show sayori neut cm oe at t21
    w "I'm not joining this club, I'm just here to visit."
    w "That's all you asked me to do."
    # "Take that reminder as being directed towards her or you. You can decide.
    show sayori turned nerv cm e1a at f21
    s "O-Oh, of course."
    s "Sorry about that."
    show sayori zorder 1 at thide
    show monika zorder 1 at thide
    hide sayori
    hide monika
    "I sigh to myself as I take a look around the room."
    "{cps=12}I recognize-{nw}{/cps}"
    show natsuki turned angr om ce zorder 2 at f11
    n "No."
    n "This guy isn't sticking around."
    show natsuki cm at t21
    show yuri turned neut om oe zorder 2 at f22
    y "I... agree with Natsuki."
    $ n_name = "Natsuki"
    show yuri turned sad cm e1a n2 at f22
    y "Do you guys even know who this person {i}is{/is}?"
    $ r_name = "Rikka"
    show natsuki at t31
    show yuri at t33
    show rikka 1c zorder 2 at f32
    r "No, I don't, actually."
    $ renpy.sound.play ("mod_assets/sfx/glitch2.ogg")
    show rikka 1a qg at f32
    pause 0.25
    show rikka 1a at f32
    r "But it's nice to meet you! I'm Rikka."
    show rikka at t32
    "The girl named Rikka holds her hand out as if she wants to shake mine."
    "{cps=30}After contemplating my life choices for a moment, I reach out to shake-{nw}{/cps}"
    show rikka 1c at t32
    show natsuki om lhip rhip at f31
    n "What did I just say? This guy can't stay here!"
    show natsuki oe cm at t31
    show rikka zorder 1 at thide
    hide rikka
    show yuri at t32
    show kotonoha 1e zorder 2 at f33
    k "Natsuki, I think you're overreacting a little."
    show kotonoha kg at t33
    pause 0.25
    show kotonoha 1e at t33
    show yuri turned flus me oe rup n2 at f32
    y "Koto..."
    show yuri turned angr om e3a n1 b1a at f32
    $ style.say_dialogue = style.edited
    y "He's fucking disgusting."
    y "He's a breathing example of what a bully is."
    $ style.say_dialogue = style.normal
    show yuri at t32
    show natsuki cross sad om oe n2 at f31
    n "{cps=30}Um, Yuri... I know he isn't {i}great{/i}, but-{nw}{/cps}"
    $ y_name = "Yuri"
    show natsuki md at t31
    $ style.say_dialogue = style.edited
    y "Make him leave."
    y "Now."
    $ style.say_dialogue = style.normal
    scene bg qgclubday
    $ renpy.sound.play ("mod_assets/sfx/glitch2.ogg")
    pause 0.4
    show sayori turned sad om oe zorder 2 at t11
    s "You guys..."
    s "He... isn't that bad..."
    show sayori at thide
    hide sayori
    $ style.say_dialogue = style.edited
    stop music fadeout 0.5
    pause .5
    play music wn8
    scene bg club_night
    show vignette
    show s_kill_zoom zorder 3
    s "Please, [player]."
    s "You'll have the chance to save me this time."
    show s_kill_zoom qg
    pause 0.25
    show s_kill_zoom zorder 3
    s "Please..."
    s "I can't get out of the rain..."
    s "... Get out of my head."
    show s_kill_zoom qg
    pause 0.25
    show s_kill_zoom zorder 3
    s "Get out of my head."
    $ style.say_dialogue = style.normal
    hide s_kill_zoom
    stop music
    scene bg club_day
    show monika forward anno cm oe zorder 2 at t11
    $ m_name = "Monika"
    m "Okay, everyone."
    m "That's enough."
    m "I don't care if he has some sort of bad reputation or not."
    m "That's no excuse to treat anyone here like crap."
    m "Now, if we can all settle down-{nw}"
    show monika at thide
    hide monika
    show vignette
    show kotonoha kmg at t11
    $ renpy.sound.play ("mod_assets/sfx/glitch2.ogg")
    $ style.say_dialogue = style.edited
    "{cps=24}S t o p  \nr u i n i n g  \nt h e  g a m e .{/cps}"
    "{cps=24}S t o p  \nt a i n t i n g  \ne v e r y t h i n g .{/cps}"
    $ persistent.deletionroute = False
    $ persistent.poemsecond = False
    $ persistent.CONDITION = 0
    $ style.say_dialogue = style.normal
    hide kotonoha
    hide vignette
    scene black
    with dissolve_scene
    pause 1.0
    scene bg club_day
    with dissolve_scene_half
    play music wn9
    "After we all greet [w_name], everyone returns to their regular activities."

    #scene 5
    $ persistent.whereami = 5
    $ persistent.deletionroute = False
    $ persistent.poemsecond = False
    $ persistent.CONDITION = 0
    "I figure it might be nice to properly introduce myself to him since he's new here."
    "I begin walking up to him when I suddenly get a strong sense of deja vu once again."
    "Don't I know this guy from somewhere...?"
    "I can't even remember meeting him, though."
    "So how come he looks so familiar?"
    scene bg club_day
    with dissolve_scene_half
    show mc 1b at t11
    mc "Mind if I talk to you for a second?"
    w "... Fine. But please make it quick."
    "The sooner this guy leaves me alone--"
    mc 1e "Do we know each other from somewhere?"
    "I definitely wasn't expecting that. But if he's going to casually bring it up..."
    w "What was your name again?"
    mc "[player]."
    w "Well, [player], do you mind if I answer with my own question?"
    mc 1j "Oh, uh... sure?"
    w "Why did you ask if you know me?"
    mc 1a "I just... thought you looked familiar."
    stop music fadeout 1.0
    w "I probably do."
    "He's already confused. Figures."
    play music wn10
    w "Let me... change that a bit so you can understand."
    w "Have you noticed anything different about this school lately? We can start with that."
    mc 1j "...Yeah, like how we supposedly have ties with schools outside of Japan."
    w "I can tell you {i}for a fact{/i} that we don't have foreign relations of any kind."
    w "Or, we {i}didn't{/i} until very recently."
    w "If I'm not mistaken, Kuribayashi only showed signs of having them starting mere days ago."
    w "Sayori tells me that Rikka joined this club a few days ago and mentioned that an administrator was discussing exchange students."
    mc 1f "Wait... You mean that the day Rikka joined-?"
    w "-was the first sign. Yep."
    w "...My apologies for the monolgue I'm basically giving already, but the best way I know how to describe it is through a parable."
    w "Sound waves move all the time, right in front of us, but we are physically incapable of seeing them under natural circumstances."
    mc 1a "Okay..."
    w "Imagine someone has a tool to let them see sound waves. They want to see new things around them, so they spend time observing individual waves."
    w "Now... what if each time they look at a new wave, they forget about the previous one they looked at?"
    w "They'd eventually have seen lots of different waves but not remember them."
    w "Suddenly, they're given an opportunity to revisit all of the different waves they've seen over time."
    w "Now that they're looking at them all at once, everything seems familiar to them."
    show mc 1f at t11
    w "Lately you've seen things that give you deja vu."
    w "But what if you've seen them before and don't remember it?"
    show mc at thide
    hide mc
    show monika forward happ om ce lpoint n2 at t11
    m "{cps=30}Okay, every-{nw}{/cps}"
    w "Just a moment, Monika."
    k "{cps=30}Sorry, but it's time for every-{nw}{/cps}"
    w "I'm aware. Please give us a moment."
    m "{cps=30}I-I'm sure whatever conversation you two are having is... important-{nw}{/cps}"
    w "Yes, so please {i}give us a moment.{/i}"
    w "Or did you have something to add?"
    "{cps=30}Monika opens her mouth to speak-{nw}{/cps}"
    scene bg qgclubday
    pause .25
    with dissolve_scene_half
    "-but Kotonoha cuts her off."
    show kotonoha 1u at t11
    k "{cps=30}I think it's time for this oh-so-happy-{nw}{/cps}"
    "[w_name] stands up abruptly."
    scene bg qgclubday
    pause .25
    with dissolve_scene_half
    w "Excuse me... Koto, right?"
    show kotonoha 1a at t11
    k "{cps=30}That's what my friends and cousin call me, but most-{nw}"
    w "Didn't really ask for details of your life story, but thank you."
    show kotonoha 1u at t11
    w "Anyway, if [player] and I are having an important conversation..."
    w "I think we have a right to finish it, no?"
    "I turn to face [player] again."
    scene bg qgclubday
    pause .25
    with dissolve_scene_half
    stop music
    show kotonoha 1u at t21
    show monika forward angr cm oe at t22
    "Kotonoha looks absolutely pissed."
    show kotonoha at f21
    k "[player]..."
    k "You might want to step away for a moment."
    show kotonoha at t21
    show monika mi at f22
    m "I don't get along with Koto much, but she's right."
    m "It would be best for you to not listen in."
    show monika cm at t22
    menu:
        "Listen to Monika and Koto.":
            call ch1_mk_1 from _call_ch1_mk_1
        "Listen to Monika and Koto.":
            call ch1_mk_2 from _call_ch1_mk_2

    show bg clubdaypause
    pause 0.5
    show bg clubdayg4
    with Dissolve(1.0)
    play music wn12
    show monika forward angr om oe at f22
    show kotonoha at t21
    m "You wanna talk 'mature', Kotonoha?!"
    $ timeleft = 1.0 - get_pos()
    show noise at noisefade(25 + timeleft) zorder 3
    show vignette as flicker at vignetteflicker(timeleft) zorder 4
    show vignette at vignettefade(timeleft) zorder 4
    show layer master at layerflicker(timeleft)
    m "I'm not the one who forced herself into the story!"
    show monika cm ce at f22
    m "I might have done some unjustified things in the actual game..."
    show monika oe at f22
    m "{b}But none of them are as absolutely uncalled for as your existence in this story.{/b}"
    show monika at t22
    show kotonoha 1u3 at f21
    k "You've had your shot with him!"
    k "And he chose to not be with you!"
    k "He even went so far as {i}deleting you{/i}, Monika!"
    k "{b}Goes to show how much he cares about you.{/b}"
    k "{b}He deleted you when you showed how much you love him.{/b}"
    k "{b}He doesn't care about you.{/b}"
    k "{b}How does that feel?"
    k "{b}He doesn't want 'Just Monika'.{/b}"
    k "{b}He wants me.{/b}"
    k "{b}Just me.{/b}"
    k "{b}{cps=20} J u s t \nK o t o n o h a.{/b}{/cps}"
    $ persistent.deletionroute = False
    $ persistent.poemsecond = False
    $ persistent.CONDITION = 0
    menu:
        "Just Kotonoha.":
            call ch1_mk_end from _call_ch1_mk_end

    return

label ch1_mk_end:
    $ ch1_mk = True
    call screen dialog("Just Kotonoha.", ok_action=Return())
    call screen confirmyes("You have unlocked a special poem.\nWould you like to read it?", Return(True))
    call poem_special(12) from _call_poem_special_11
    scene bg club_day
    call splashscreen from _call_splashscreen_3
    scene bg club_day 
    with dissolve
    stop music
    show kotonoha 1s at t11
    k "W... What?"
    scene bg qgclubday
    $ persistent.deletionroute = False
    $ persistent.poemsecond = False
    $ persistent.CONDITION = 0
    $ ch1_mk = False
    return
    

label ch1_mk_1:
    $ persistent.whereami = 6
    $ persistent.deletionroute = False
    $ persistent.poemsecond = False
    $ persistent.CONDITION = 0
    mc "If you have something to say regarding our conversation, I think I should hear it."
    scene bg qgclubday
    pause .25
    with dissolve_scene_half
    show mc 1a at t22
    show kotonoha 1u3 at t21
    w "I agree."
    play music wn11
    show kotonoha at f21
    k "Fine."
    k "Have it your way."
    show kotonoha 1i at t21
    "Kotonoha takes a deep breath before continuing."
    show kotonoha 1u at f21
    k "Do you genuinely believe you're better than everyone else here?"
    k "Because you're definitely acting like it."
    k "This club will not tolerate the sort of behavior that you've shown in the past few moments."
    show mc at thide
    hide mc
    show monika forward angr cm e1a at t22
    m "{cps=24}Koto, that's not your call to-{nw}{/cps}"
    scene bg qgclubday
    pause .25
    with dissolve_scene_half
    show kotonoha 1u3 at f21
    show monika forward angr cm e1a at t22
    k "Were {i}you{/i} going to do anything about it, Miss President?"
    k "If so, I would {i}love{/i} to hear what {i}your{/i} take on this situation is!"
    show kotonoha 1u2 at t21
    show monika forward angr cm oe at f22
    m "{cps=24}Okay, Koto. First of all-{nw}{/cps}"
    show monika at t22
    show kotonoha 1u3 at f21
    k "And another thing: Did you ever even {i}hear{/i} the conversation they were having?!"
    show monika ce at t22
    k "Because {i}I{/i} did, and I found the topic to be-{nw}"
    show monika oe at f22
    show kotonoha 1u2 at t21
    m "{cps=20}{i}That's enough, Kotonoha.{/i}{/cps}"
    stop music fadeout 1.0
    show kotonoha 1a at f21
    show monika at t22
    k "Ohhh, {i}somebody{/i} is stepping out of her shell, I see~"
    k "Are you finally ready to be mature enough to properly handle the-{nw}"
    return

label ch1_mk_2:
    $ persistent.whereami = 6
    $ persistent.deletionroute = False
    $ persistent.poemsecond = False
    $ persistent.CONDITION = 0
    mc "{cps=24}Okay, I'll just go hang out with-{nw}{/cps}"
    scene bg qgclubday
    pause .25
    with dissolve_scene_half
    show mc 1a at t22
    show kotonoha 1u at t21
    w "No, I think it's best that you stay and listen."
    show kotonoha 1u3 at f21
    k "FINE!"
    show kotonoha at f31
    show mc 1f at t32
    show monika forward neut om oe at t33
    k "Have it your way."
    play music wn11
    show kotonoha 1x at f31
    k "{b}He'll just see that everyone was right about how horrible you are, [w_name]{/b}"
    show kotonoha 1u3 at f31
    k "Do you genuinely believe you're better than everyone else here?"
    k "{b}You wish your life meant nearly as much as that of somebody like [player]{/b}"
    k "{cps=30}This club will not tolerate the behavior that you've shown {b}all of your life, you fuc-{/b}{nw}{/cps}"
    show kotonoha 1u at t31
    show monika forward angr cm e1a at f33
    m "Koto..."
    scene bg qgclubday
    pause .25
    with dissolve_scene_half
    stop music fadeout 1.0
    show kotonoha 1u at t21
    show monika forward angr cm oe at f22
    m "{b}You should leave this room. Now.{/b}"
    show kotonoha 1a at f21
    show monika at t22
    k "Ohhh, {i}somebody{/i} is stepping out of her shell, I see~"
    k "Are you finally ready to be mature enough to properly handle the-{nw}"
    return

label ch1_p3:
    #scene 6
    $ persistent.whereami = 7
    $ persistent.deletionroute = False
    $ persistent.poemsecond = False
    $ persistent.CONDITION = 0
    scene black
    with dissolve_scene_full
    call screen confirm("You have unlocked a real special poem.\nWould you like to read it?", Return(), Return())
    call poem_special(13) from _call_poem_special_12
    scene bg club_day
    with dissolve_scene_full
    play music wn9
    "I enter the clubroom and put my stuff down at a desk."
    "I nod in greeting towards [player], who is sitting at a nearby desk."
    "I look around the rest of the clubroom:"
    "Sayori seems to be deep in thought at the back of the room."
    "Natsuki is rummaging around in the closet, seemingly looking for something."
    "Yuri gives me a look that I can't entirely make out."
    "I take it to mean some sort of resentment and move on."
    "Rikka is working on what looks like algebra homework."
    "Monika and Kotonoha are both at the front of the room, talking quietly."
    scene bg qgclubday
    pause .25
    with dissolve_scene_half
    $ persistent.CONDITION = 0
    "I guess I should let Monika and Kotonoha be for now, especially after what happened yesterday."
    $ persistent.CONDITION = 0

    call poemresponse_start from _call_poemresponse_start_1

    if persistent.CONDITION >= 4:
        call poem from _call_poem_4
        if persistent.playthrough == 20 and persistent.CONDITION == 5:
            jump a1
        else:
            $ persistent.playthrough = 1
            $ persistent.CONDITION = 0
            play sound wa2
            jump ch1_p4

    mc "You seem to already know what you're doing pretty well."
    r 1v "It took a while, to be honest."
    r 1h "You could probably imagine that a member of the track team struggled a lot on her first few attempts at writing poems."
    show rikka 1h qg at t11
    pause 0.25
    show rikka 1h at t11
    r "But someone told me that it's all about being brave enough to take that first step."
    r "So I listened to them and... well, I didn't write anything great, but I took the first step."
    r "Just keep practicing, [player]. You'll get the hang of it in no time!"
    mc "{cps=24}Thanks, I really-{nw}{/cps}"
    hide rikka
    show monika forward happ om oe lpoint at t11
    $ persistent.whereami = 14
    m "Okay, everyone!"
    m "I know I'm cutting you all a bit short on the poem-sharing, but I'd like to make an announcement!"
    "Despite our conversation being interrupted, Rikka happily turns her attention to Monika."
    "{cps=30}Everyone else does the same, including [w_name]-{nw}{/cps}"
    stop music fadeout 0.5
    scene bg qgclubday
    pause .25
    play music wn6 fadein 0.5
    with dissolve_scene_half
    "I look over at Monika, who's standing in the front of the room."
    show monika forward happ cm oe at t11
    m "As you may know..."
    m "... our end-of-term exams are rapidly approaching!"
    show monika at t21
    show natsuki turned pani om ce at f22
    n "Don't remind me!"
    show monika at t31
    show natsuki cm at t32
    show yuri turned nerv cm ce n2 at f33
    y "Ah- I still have so much studying to do..."
    show monika at t41 zorder 3
    show natsuki at t42 zorder 2
    show yuri at t43 zorder 2
    show rikka 1g at f44 zorder 3
    r "I totally forgot about them."
    show rikka at thide
    hide rikka 
    show mc 1j at f44 zorder 3
    mc "I'm not {i}too{/i} worried, to be honest."
    show mc at t44 zorder 2
    show yuri at thide
    hide yuri
    show kotonoha 1a at f43 zorder 3
    k "Neither am I. These exams shouldn't be too difficult for me."
    show kotonoha at t43 zorder 2
    show natsuki at f42 zorder 3
    n "Maybe for a nerd like you! What about me and..."
    show natsuki turned neut om e1b b1d n2 at f42
    n "W-Well, I can see Yuri doing fine, too..."
    show natsuki at t42
    "Natsuki desperately glances at everyone, as if trying to find someone she can make a point out of."
    show natsuki e1a at t42
    "She looks at me for less than a second before turning back to Monika."
    show natsuki cross anno cm ce at f42
    n "Nevermind..."
    show natsuki at thide
    hide natsuki
    show monika at t31
    show kotonoha at t32
    show mc 1a at f33
    mc "Does Sayori remember that exams are coming up?"
    show mc at t33
    show monika forward nerv cm ce n2 at f31
    m "Don't worry, [player]. She was gonna make the upcoming announcement with me, so she remembers."
    show monika at t31
    w "Speaking of her, where {i}is{/i} Sayori?"
    show kotonoha at f32
    k "I think she went home early."
    show kotonoha at t32
    show monika at f31
    m "Yeah... She wasn't feeling well."
    show monika at t31
    w "Should..."
    "I'm about to hate myself for asking this question, aren't I?"
    w "... should someone go check on her?"
    show monika e1a at f31
    m "Actually, that would be nice..."
    m "Would you mind doing that, [w_name]? She'd probably be less freaked out if either you or Koto went to see how she's doing."
    show monika at t31
    show kotonoha at f32
    k "{cps=24}I can go check on-{nw}{/cps}"
    show kotonoha at t32
    stop music
    w "No. I'll go check on her."
    w "Kotonoha, can you send me her address?"
    show monika forward happ cm ce n1 at f31
    m "Already done!"
    show monika at t31
    w "Thanks, Monika. I'll see you all tomorrow."
    show monika at thide
    show kotonoha at thide
    show mc at thide
    hide monika
    hide kotonoha
    hide mc
    scene bg corridor with wipeleft
    "I immediately leave the room and start walking towards the front of the school."
    "{cps=30}I'm about to walk through the front doors-{nw}{/cps}"
    show mc 1t at t11
    mc "Hey... can you uh..."
    mc "... keep me updated on how she is?"
    mc "I don't know her very well, but she seems like a really great person."
    mc "So hearing that she isn't well makes me..."
    w "Sort of concerned?"
    "[player] just nods in response."
    "Usually, I wouldn't feel very bad for someone like him... {i}let alone Sayori...{/i}"
    "But for some reason..."
    w "Sure. You have my number in your phone now, right?"
    mc "Yeah."
    w "Okay, then. You can text me here in a few minutes and I'll respond when I come back from her place."
    show mc 1i at t11
    mc "Okay... Thanks, [w_name]."
    w "No problem."
    "I say goodbye to [player] and leave the building."
    
    #scene 7
    $ persistent.whereami = 15
    scene bg residential_day with dissolve_scene_full
    "I'm going to hate this, you know."
    "..."
    "I reach the address that Monika sent me."
    "As I approach the front door, I find myself thinking about how quick Kotonoha was to try and come here."
    "She almost seemed like she had... something she was set on doing."
    scene bg house with wipeleft_scene
    "Even if I was the one who suggested someone visiting her, she acted like she had {i}planned{/i} on coming here."
    "I decide to keep this thought in the back of my mind for now."
    "I knock on the front door a few times."
    "There's no response."
    "I reach for the door handle and turn it."
    "{i}This girl keeps her front door unlocked??{/i}"
    "I make a mental note to talk about this with Sayori before opening the door."
    scene black with dissolve_scene_full
    "I walk inside... and all the lights are out."
    "I cautiously feel my way around the bottom floor until I find some stairs."
    "I climb them and find a light peeking out from the bottom of the nearest door."
    "I reach the door and knock."
    w "Sayori? It's me."
    w "You in there?"
    "No response."
    "My instincts tell me to open the door."
    "But isn't that sort of an invasion of her privacy if she's in there?"
    "..."
    "I wouldn't even care if this was anyone else."
    "I would just barge through the door like it was my own house."
    "So why do I feel guilty for even considering it now?"
    menu:
        "Barge in.":
            pass
    "Even so... I can't help but feel like {i}someone{/i} is telling me to enter."
    menu:
        "Barge in.":
            pass
    "If this was anyone else... I would just..."
    menu:
        "Barge in.":
            pass
    "I close my eyes and take a deep breath."
    "I speak under my breath."
    w "Sorry, Sayori..."
    "I gently open the door."
    w "Sayori-{nw}"
    play sound closet_open
    scene bg sayori_bedroom
    show sayori casual turned shoc ml e1a at t11
    s "WHA-"
    "It takes me several seconds for what I'm seeing to properly register in my mind."
    "Sayori seems to have been in the middle of moving a chair into the center of her room..."
    "Directly below her ceiling fan."
    "{i}Directly{/i} below it."
    "I can't even bring myself to speak for another several seconds."
    show sayori casual turned worr om e1a at t11
    s "[w_name]..."
    s "W-Why are you here...?"
    "Not even a 'This isn't what it looks like.'"
    "Just a 'Why are you here.'"
    "She knows that I understand what would've happened had I not just entered..."
    "I take a couple of deep breaths before speaking in a relatively steady voice."
    w "Sayori..."
    w "... Why are you..."
    w "... What made you want..."
    show sayori casual turned cry e1g ma at t11
    s "It's... okay..."
    s "They don't have to put up with me anymore."
    s "You don't have to do anything to--{nw}"
    w "Yes, I do."
    "I don't care how rude that sounded right now."
    "{cps=24}I make to move the chair away from-{nw}{/cps}"
    show sayori casual turned worr e1g ml at t11
    s "DON'T!"
    show sayori mm at t11
    "She tries to stand on the chair to prevent me from moving it."
    "I kick it out from under her foot that's already resting on it."
    show sayori casual turned cry om ce lup rup at t11
    s "GAH!"
    "I manage to catch her so she doesn't fall."
    "I'm geniunely surprised that my reflexes are still on-point in this moment."
    "I let go of her, but she suddenly hugs me tightly."
    show sayori mj e4e at t11
    w "H-Hey..."
    play music wn13
    "I stop myself from arguing. She doesn't need me starting anything like that right now."
    "Instead, I do something I've never done for anyone..."
    "I carefully wrap my arms around her as she breaks down."
    "I don't say anything for several minutes."
    "I just let her cry..."
    "{i}I've never felt compelled to do anything like this for anyone...{/i}"
    "This is entirely out of character for me."
    "So why do you want me doing this?"
    "..."
    "You know what, I think I get it."
    "{i}I think I finally understand what you're--{/i}{nw}"
    hide sayori
    show bg qgsayori_bedroom
    pause 0.32
    return

label a1:
    scene bg club_day with dissolve_scene_full
    show monika forward neut cm oe at t11
    m "Hey, [player]..."
    m "Did you notice anything strange about Sayori yesterday?"
    m "I realized that she left early once we all started to pack up."
    menu:
        "...":
            pass
    show monika at t21
    show kotonoha 1w at f22
    k "... Sayori still won't pick up, Monika."
    show kotonoha at t22
    show monika at f21
    m "Still...?"
    show monika forward curi cm oe at f21
    m "You haven't heard from her at all since yesterday?"
    show monika at t21
    show kotonoha 1p at f22
    k "No..."
    k "I'm... starting to feel really worried."
    show kotonoha at t32
    show yuri turned worr cm e1a at f33
    show monika at t31
    y "Still nothing from Sayori?"
    show yuri at t33
    show monika forward neut cm ce at f31
    m "No."
    show monika at t41
    show rikka 1g at f42
    show kotonoha at t43
    show yuri at t44
    r "I really hope she's okay."
    show rikka at thide
    hide rikka
    show natsuki turned doub cm ce at f42
    n "..."
    show natsuki turned flus mj ce at f42
    n "What if... something happened to her?"
    n "I... I can't imagine what could've..."
    show natsuki at t42
    show kotonoha at t44
    show yuri turned sad cm ce at f43
    y "It's okay, Natsuki. We'll..."
    y "..."
    show yuri at t43
    w "Hey, what did I miss?"
    show kotonoha 1b at f44
    k "[w_name]!"
    k "Have you seen or heard from Sayori at all today?"
    show kotonoha at t44
    w "I thought you'd tell me she's sick or something when I got here...?"
    show kotonoha 1p at f44
    k "..."
    show natsuki at thide
    hide natsuki
    show yuri at thide
    hide yuri
    show rikka 1g at f32
    show kotonoha at t33
    show monika at t31
    r "Would she be at her place right now...?"
    show rikka at t32
    show monika forward neut om oe at f31
    m "..."
    show monika cm at f31
    m "... Quite possibly..."
    m "But school {i}just{/i} ended, won't it take a while to try to get to her house through all of the students heading home?"
    show monika at t31
    w "If you want, I can go to her place."
    w "{cps=30}If people see me walking by, I'm pretty sure they'll get out of my-{nw}{/cps}"
    mc "I'll go."
    w "... Dude."
    w "Bud."
    w "Pal."
    w "You are not about to make that trip over to her house without getting crushed by everyone out there right now."
    w "{cps=24}I've had-{nw}{/cps}"
    mc "I'll go."
    scene bg qgclubday
    pause .25
    with dissolve_scene_half
    show mc 1a at t11
    w "[player], listen to me."
    w "You're really nice to want to do this to make sure she's okay."
    w "But you'd probably get hurt trying to get over there with how many people are heading home."
    w "As much as I hate using this as my justification for volunteering to check on her..."
    w "... almost nobody in this school likes me. They'll steer away from me at just about any cost."
    w "{cps=24}So please, just let me-{/cps}{nw}"
    mc "I'll go."
    $ timeleft = 1.0 - get_pos()
    show noise at noisefade(25 + timeleft) zorder 3
    show vignette as flicker at vignetteflicker(timeleft) zorder 4
    show vignette at vignettefade(timeleft) zorder 4
    show layer master at layerflicker(timeleft)
    w "You're not listening to me at all, are you?"
    w "Don't bother responding, I know the answer is no."
    w "{i}You. Need. To. Stay. Here.{/i}"
    w "{cps=12}I am not-{nw}{/cps}"
    mc "I will go."
    w "No, you will not."
    mc "I will go."
    w "[player], just SHUT UP AND SIT THE F-{nw}"
    jump a2

label a2:
    scene black
    pause 2.0
    w "What..."
    w "... What happened to..."
    w "... Why is everything just... black?"
    play sound wlf volume 0.3
    w "[player]...?"
    w "Where is he..."
    "{i}What did you do?{/i}"
    play sound wrf volume 0.7
    "Where is everyone?"
    "Where's the club room?"
    play sound wlf volume 1.0
    w "[player]..."
    w "I'm warning you right now."
    play sound wrf volume 1.3
    w "If you come any closer without explaining what the hell is going on..."
    w "I {i}will{/i} defend myself however I feel necessary."
    play sound wlf volume 1.7
    w "..."
    w "Well... I guess you're set on making this difficult, aren't you?"
    play sound wrf volume 2.0
    w "Sucks, really. I was genuinely starting to take a liking to you."
    play sound wlf volume 2.3
    w "But I guess you just really don't care, do you?"
    w "Not about me, not about Sayori..."
    w "Not about anybody."
    play sound wrf volume 2.7
    w "{cps=24}[player]-{nw}{/cps}"
    pause 3.0
    play sound wsl volume 2.0
    pause 1.0
    w "H-Hey- get your- hand- off of- me-"
    w "{cps=12}G- g- g- get-{nw}{/cps}"
    pause 0.5
    play sound wsn volume 5.0
    pause 3.0
    $ delete_character("white")
    "white.chr deleted successfully."
    "3 left."
    pause 3.0
    "Why?"
    "What the actual frick are you trying to do??"
    "I know I promised some decisions here and there..."
    "But this is not AT ALL what I meant, and I think you know that."
    "[w_name]... he didn't deserve that."
    "...I'm warning you right now. Not [player], but you. Because I KNOW he's not to blame for this."
    "Do not continue doing this kind of crap in this project."
    "If you do, I will not make your time here easy."
    "...Don't worry, [player]. I'll save you from this freak if I have to."
    $ persistent.CONDITION = 0
    $ persistent.deletionroute = False
    $ persistent.poemsecond = False
    $ delete_all_saves()
    $ persistent._clear(progress=True)
    $ renpy.quit()

label a2_end:
    $ renpy.quit()

label ch1_p4:
    #scene 8
    scene bg club_day with dissolve_scene_full
    "I walk into the room."
    "Everyone is silent."
    "The atmosphere filling the room feels {i}very{/i} wrong."
    "I walk up to Monika, who looks to be texting someone."
    show monika forward neut cm oe at t11
    mc "Monika?"
    m "Hello, [player]."
    mc "Why is everyone so quiet...?"
    mc "Did I miss something?"
    "Monika's expression doesn't change as she takes a deep breath."
    m "He really didn't tell you?"
    mc "Who... [w_name]? Was he {i}supposed{/i} to tell me something?"
    "I thought it was strange that he never responded to my texts last night."
    "But I just figured he was busy talking to Sayori or something."
    "I suddenly feel incredibly stupid for not thinking anything more of it until right now."
    m "Y-Yes, he was supposed to..."
    show monika om ce at t11
    pause 2.0
    show monika cm oe at t11
    m "Sayori's missing."
    "My heart drops."
    "But my mind refuses to understand what was just said."
    mc "What do you mean?"
    m "Sit down, [player]. We need to talk."
    "I hesitantly pull up a desk since the chairs are attached to them."
    "I take a seat, and everything around me seems to freeze in place."
    show monika b1c e1b me at t11
    m "Sorry in advance for how long this is gonna take to explain."
    "(NOTE FROM CPC: This expositional segment will be largely reduced once a specific side mod has been released.)"
    m "Okay. Where should I start..."
    m "..."
    show monika e1a md at t11
    m "... Sayori has had depression for most of her life."
    m "Her main trigger is people worrying too much about her..."
    m "... Even if she really needs the attention that she's being offered."
    m "Yesterday, [w_name] went to see if she was feeling okay since she went home early."
    m "He was lucky to arrive when he did."
    m "It took several hours, but [w_name] stayed with Sayori until she finally calmed down."
    m "But... Around the same time that Sayori was calming down..."
    m "... Kotonoha evidently texted Yuri saying she was going to check on Sayori and [w_name]."
    m "Yuri told me as soon as she got the message."
    m "Even she knew that Kotonoha wouldn't have naturally decided to do something like that."
    m "The moment I read the message, I rushed over to Sayori's place."
    m "I got to her room... {i}But no one was home.{/i}"
    m "The only thing I could tell from the state of her room was that there was some sort of fight."
    m "Most of the things in Sayori's room were broken."
    m "After at least an hour, [w_name] texted me."
    m "He... wasn't like himself at all. He wouldn't stop apologizing."
    m "It took several minutes to get him to elaborate, but... my theory that there had been a fight turned out to be true."
    m "The first thing he said was that he was going to beat the crap out of Kotonoha if he ever found her."
    m "He went on to explain that Kotonoha had barged into Sayori's room not even ten seconds after Sayori had finally calmed down."
    m "Kotonoha knew exactly what she was doing."
    m "She rushed into the room and said {i}a lot{/i} of horrible things."
    m "[w_name] actually started fighting her to try and keep her from doing what she was about to do."
    m "And while I {i}never{/i} thought I'd have to say this in any mod, [w_name] lost the fight."
    m "Kotonoha knocked him out cold and took Sayori."
    m "When [w_name] woke up, he traced Kotonoha's path as far as he could, following signs of her path until well after the sun had come up."
    m "Taking all other timestamps into account, that means he was at it for at least five hours."
    m "Eventually, there was nothing left to even resemble anyone passing through before."
    m "I was partially relieved because he managed to get as far as he did, but at the same time..."
    m "... if he went as far as he did, how far did Kotonoha go?"
    m "... [w_name]'s on his way here now."
    m "He just said he should be here in about 30 minutes when you came up to me."
    $ delete_character("sayori")
    mc "..."
    mc "....."
    "I try to take in everything she just said... but it's all so much to try and understand."
    mc "That's..."
    mc "... I can't even think of anything beyond 'horrible' right now, but that's not saying nearly enough..."
    mc "... Wait... what did you mean when you said you never thought you'd have to say [w_name] lost a fight 'in any mod?'"
    show monika ce at t11
    m "[player]..."
    m "I need you to take everything I'm about to tell you with total seriousness."
    m "It's going to be hard to believe, but you need to trust me."
    mc "Okay..."
    show monika e1a at t11
    m "This is a game."
    m "The world we're in right now is all a game... But it's broken."
    m "Remember that conversation you had with [w_name] about the deja vu you were having?"
    m "Well, he was entirely correct: This version of the game is overflowing with mods that people have created over the span of a few years."
    m "Rikka is from a mod called {i}SNAFU{/i}."
    mc "... L-Like the anime?"
    show monika ce at t11
    m "{cps=8}{i}sigh{/cps}{/i} Yes, like the anime."
    show monika e1a at t11
    m "[w_name] is a character from a mod called {i}The Rising Night{/i}."
    m "Everyone hated him in his original mod, and when he made his way into the game recently, that was nearly the case again."
    m "I had to manually change a few files in order to prevent everyone from hating him."
    m "Obviously, this didn't work once or twice, but I did what I could."
    m "Kotonoha is from a mod called {i}Tainted Love{/i}."
    m "She's also had the same level of access over the files of this game for a few days now."
    m "I tried to disable all mods but put her in a folder with code granting a mod character elevated access."
    m "She used this to her advantage and enabled every mod available."
    m "The game ended up breaking in some way, and now different mods have been making the game run {i}much{/i} differently."
    m "... This is why I was so scared about Kotonoha possibly becoming a prominent part of this game."
    m "She might be a rational individual who loves her cousin outside of normal gameplay..."
    m "... But as soon as you're in the picture, she seems to be drawn to you, and not in a good way."
    m "She would do literally anything to be with you, including hurting her friends and family."
    "{cps=8}{i}creeeeeek{/cps}{/i}"
    w "I'm... back..."
    scene bg qgclubday
    pause .25
    with dissolve_scene_half
    show monika forward neut b1c e1a me at f21
    show mc 1e1 at t22
    m "You're back a little earlier than expected."
    show monika at t21
    w "I...{w=0.5} sprinted the rest of...{w=0.5} the way here..."
    "Deep breaths...{w=1.0} deep breaths..."
    show bg qgclubday
    show monika forward neut cm oe at f21
    m "{cps=30}Why? There's not much you can do by getting here any-{nw}{/cps}"
    show monika at t21
    w "She's gone."
    show bg qgclubday
    w "Kotonoha killed her."
    show monika forward shoc cm oe at t21
    w "I saw evidence of it coming back up here."
    w "She somehow had an entire fake trail in place to throw us off."
    show bg qgclubday
    m "I..."
    show monika at t21
    w "You don't believe me? Check the files."
    window hide
    $ consolehistory = []
    $ run_input("/locate @blue", "/locate @blue")
    $ pause(2.0)
    $ run_input("", "Sayori.chr could not be found.")
    $ pause(2.0)
    hide screen console_screen
    show monika at f21
    m "H-How did you find out..."
    show monika at t21
    show bg qgclubday
    show bg qgclubday
    w "Here... I... t-took a picture..."
    show monika mj at f21
    m "..."
    show monika at t21
    show mc 1a1 at f22
    mc "N-No..."
    show mc at t22
    show layer master
    show layer screens
    show kotonoha 1x at i11 onlayer front
    $ style.say_dialogue = style.edited
    k "Y E S ."
    scene bg qgclubday
    pause .25
    scene black
    hide kotonoha onlayer front
    show kotonoha 1x at t11
    $ kgmode = True
    $ style.say_window = style.window_mg2
    $ style.namebox = style.namebox_mg2
    k "ALL I WANTED WAS TO SPEND TIME WITH YOU, [player!u]."
    k "BUT MONIKA AND THAT WHITE-HAIRED PIECE OF SH-{nw}"
    call kotog from _call_kotog
    $ renpy.sound.play ("mod_assets/sfx/monikapound1.ogg")
    k "THEY RUIN EVERYTHING."
    k "SO NEXT TIME, DON'T LET THEM."
    k "I'LL MAKE SURE YOU CAN CHOOSE TO SPEND TIME WITH ME INSTEAD."
    show m_rectstatic
    show m_rectstatic2
    show m_rectstatic3
    play sound "sfx/monikapound.ogg"
    show layer master:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
            xpos 1280
            easein_elastic 0.35 xpos 640
            xpos 0
            easein_elastic 0.35 xpos 640
    show layer screens:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
            xpos 1280
            easein_elastic 0.35 xpos 640
            xpos 0
            easein_elastic 0.35 xpos 640
    show noise onlayer front:
        alpha 0.3
        easeout 0.35 alpha 0
        alpha 0.3
        easeout 0.35 alpha 0
        alpha 0.3
        1.35
        linear 1.0 alpha 0.0
    show glitch_color onlayer front
    $ gtext = glitchtext(7)
    $ k_name = "K[gtext]"
    k "IN FACT..."
    k "... I'LL SEE HOW MUCH YOU REALLY WANT TO BE WITH ME."
    k "I SAVED SOME MODS FROM BEING ENABLED SO THAT YOU COULD FOCUS ON WHAT'S IMPORTANT..."
    k "... BUT IF YOU TRULY CARE ABOUT ME, I KNOW YOU'LL MAKE THE RIGHT DECISIONS..."
    k "EVEN IF EVERY MOD I CAN THINK OF WERE ACTIVATED."
    k "NOT JUST SIMPLE 'FEATURES' OF MODS LIKE YOU'VE BEEN SEEING..."
    k "RIKKA FROM SNAFU WILL BE HERE? I'LL MAKE SURE THE STATS FROM {i}SNAFU{/i} ARE HERE, TOO."
    k "SIMPLE DIALOGUE REFERENCES TO {i}FOREIGN RELATIONS{/i}? I'LL GO AHEAD AND BRING {i}HIM{/i} HERE, TOO."
    k "AND I WON'T JUST BRING MORE FROM THOSE MODS..."
    k "... WHEN THERE'S SO MUCH MORE POTENTIAL OUT THERE."
    k "THERE'S BIG ONES LIKE {i}EXIT MUSIC{/i} AND {i}BRANCHING PATHS{/i}, LESSER-KNOWN ONES LIKE {i}MY BEST FRIEND IS A GHOST{/i}..."
    k "OH, AND I CAN'T FORGET THE MOST POPULAR ONE OF ALL..."
    call kotog from _call_kotog_1
    $ renpy.sound.play ("mod_assets/sfx/monikapound1.ogg")
    k "BUT I'LL ONLY BRING THAT ONE IN AS A LAST RESORT."
    k "I DON'T THINK THIS GAME WILL NEED AN AFTER STORY."
    show kotonoha 1xg at t11
    k "WELL... I WON'T KEEP YOU WAITING ANY LONGER."
    python:
        try: renpy.file(config.basedir + "/txt.txt")
        except: open(config.basedir + "/txt.txt", "wb").write(renpy.file("mod_assets/txt.txt").read())
    k "ENJOY ACT II, [player!u]~"
    call kotog from _call_kotog_2
    $ renpy.sound.play ("mod_assets/sfx/monikapound1.ogg")
    $ style.say_window = style.window
    $ style.namebox = style.nameboxd
    $ kgmode = False
    scene black
    $ show_poem (poem_k1, music=False, paper_sound=None)
    python:
        os.remove(config.basedir + "/txt.txt")
    $ gtext = glitchtext(24)
    "[gtext]. Read broken.txt for more details."
    python:
        try: renpy.file(config.basedir + "/broken.txt")
        except: open(config.basedir + "/broken.txt", "wb").write(renpy.file("mod_assets/broken.txt").read())
    "...Yeah, I shouldn't have gone back on my decision to avoid giving her this kind of power."
    "Sorry that you had to endure all of that. I'll go through with my original plan for this project now."
    "Just a moment..."
    $ persistent.CONDITION = 0
    $ persistent.deletionroute = False
    $ persistent.poemsecond = False
    $ persistent.playthrough = 2
    $ renpy.quit()
