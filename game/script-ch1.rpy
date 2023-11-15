label ch1_p1:
    #scene 1
    $ mgmode = False
    stop music fadeout .5
    scene bg residential_day
    with dissolve_scene_full
    play music t2
    k "Hey there, [player]!"
    show kotonoha kg at t11
    k 1a "Glad to see you finally decided to get up."
    "I just sigh to myself. Kotonoha always nags me for small things like this."
    "Anytime I take a while to get ready for school, for instance, she'll start joking like this."
    "But I know she doesn't mean any harm in doing stuff like that."
    show bg qgresidential_day
    "The two of us begin our daily commute to school."
    k "Anyway, have you considered joining any clubs yet?"
    mc "Huh? I thought I already said I'm not interested in joining-{nw}"
    mc "Huh? I thought I already said I'm interested in possibly joining your club?"
    k 1h "Ah, how could I forget?"
    show kotonoha 1a at t11
    "Kotonoha smiles and doesn't say anything else the rest of the way to school."
    "We've always walked to school together like this..."
    show bg qgresidential_day
    "...But she's usually not this silent."
    "My train of thought is broken by an overly-energetic girl approaching us."
    show kotonoha 1e zorder 2 at t21
    show sayori turned happ om oe zorder 2 at f22
    s "Hey, Kotonoha!"
    show sayori cm at t22
    show kotonoha at f21
    k 1d "Good morning, Sayori."
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
    "We reach the front door of the school-{nw}"
    stop music
    show bg qgresidential_day

    #scene 2
    $ m_name = "Monika"
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
    k "Just like you know I can see what you're doing."
    show kotonoha at t22
    show bg clubdaypause
    pause 0.5
    show bg clubdayg4
    with Dissolve(1.0)
    show monika at f21
    m "You really just came out and said something like that in front of the entire club?"
    show monika at t21
    show kotonoha 1h at f22
    k "Do you have a problem with this?"
    show kotonoha at t22
    show monika at f21
    m "Kotonoha."
    show kotonoha 1a at f22
    show monika at t21
    k "Monika."
    show kotonoha at t22
    show monika at f21
    m "Just because you have some control over the game doesn't mean you get to tell everyone about the reality of this world."
    m "If they knew what happens behind closed doors..."
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
    k "But that doesn't give you any right to try and keep [player] all to yourself."
    show kotonoha at t22
    show monika at f21
    m "That's funny to hear coming from you."
    m "Didn't you just abruptly insert yourself into the beginning of the story and then force everything to skip to the next time you're around?"
    show monika at t21
    show kotonoha 1u3 at f22
    k "I have a right to spend a little extra time with [player]!"
    k "You've always been in control, always inevitably trapping him and making him spend time with you."
    k "Have you ever considered the fact that I might want the sort of opportunity?"
    show kotonoha 1u at t22
    show monika forward neut cm ce at f21
    m "..."
    m "... Alright Kotonoha."
    m "How about this:"
    m "If you promise to be fair and rational about trying to spend time with [player]..."
    m "... Then I guess it's fine."
    show monika at t21
    show kotonoha 1a at f22
    k "Funny how you think-{nw}"
    show kotonoha at t22
    show monika oe at f21
    m "I'm not finished."
    m "You have to give me a route as well."
    m "And you have to give one to everyone in this club."
    m "Even Rikka and whoever else isn't officially a part of this world."
    show monika at t21
    show kotonoha 1e at f22 
    k "..."
    k "....."
    show kotonoha at t22
    show monika at f21
    m "Do we have a deal Kotonoha?"
    show monika at t21
    show kotonoha 1q at f22
    k "... Okay. Fine. Deal."
    show kotonoha 1p at f22
    k "Just... give me a minute to add some files for everyone."
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
    scene bg club_day
    stop music fadeout .5
    play music wn6
    show monika forward happ om ce at t11
    m "Hello again, [player]!"
    m "It's great to see you-{nw}"
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
    "Meanwhile, Natsuki is rummaging around in the closet-{nw}"

    #scene 4
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
    "As soon as I enter the room, all eyes fall on me."
    "Instantly, I recognize Sayori, who looks genuinely ecstatic."
    $ s_name = "Sayori"
    "I glance at-{nw}"
    show sayori turned lsur om oe zorder 2 at t11
    s "Oh my gosh!"
    show sayori turned happ om ce lup rup zorder 2 at h11
    s "Oh my gosh!!!"
    w "Wait-"
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
    show sayori turned nerv cm e1a at f21
    s "O-Oh, of course."
    s "Sorry about that."
    show sayori zorder 1 at thide
    show monika zorder 1 at thide
    hide sayori
    hide monika
    "I sigh to myself as I take a look around the room."
    "I recognize-"
    show natsuki turned angr om ce zorder 2 at f11
    n "Oh, no!"
    n "This guy isn't sticking around!"
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
    show rikka 1a at f32
    r "But it's nice to meet you! I'm Rikka."
    show rikka at t32
    "The girl named Rikka holds her hand out as if she wants to shake mine."
    "After contemplating my life choices for a moment, I reach out to shake-"
    show rikka 1c at t32
    show natsuki om lhip rhip at f31
    n "What did I just say? This guy can't stay here!"
    show natsuki oe cm at t31
    show rikka zorder 1 at thide
    hide rikka
    show yuri at t32
    show kotonoha 1e zorder 2 at f33
    k "Natsuki, I think you're overreacting a little."
    show kotonoha kg2 at t33
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
    n "Um, Yuri... I know he isn't great, but-"
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
    s "You're my salvation... remember?"
    s "Please..."
    s "I can't get out of the rain..."
    s "... Get out of my head."
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
    "{cps=24}S t o p  r u i n i n g  t h e  g a m e .{/cps}"
    "{cps=24}S t o p  t a i n t i n g  e v e r y t h i n g .{/cps}"
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
    "I figure it might be nice to properly introduce myself to him since he's new here."
    "I begin walking up to him when I suddenly get a strong sense of deja vu."
    "Don't I know this guy from somewhere...?"
    "I can't even remember meeting him, though."
    "So how come he looks so familiar?"
    scene bg club_day
    with dissolve_scene_half
    show mc 1b at t11
    mc "Mind if I talk to you for a second?"
    w "..."
    w "Fine. But please make it quick."
    "The sooner this guy leaves me alone."
    mc 1e "Do we know each other from somewhere?"
    "I definitely wasn't expecting that."
    "But if he's going to casually bring it up..."
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
    mc 1j "... Yeah, like how we supposedly have ties with schools outside of Japan."
    w "I can tell you {i}for a fact{/i} that we don't have foreign relations of any kind."
    w "Or, we {i}didn't{/i} until very recently."
    w "If I'm not mistaken, Kuribayashi only showed signs of having them starting mere days ago."
    w "Sayori tells me that Rikka joined this club a few days ago and mentioned that an administrator was discussing exchange students."
    mc 1f "Wait... You mean that the day Rikka joined-?"
    w "-was the first sign. Yep."
    w "As a matter of fact... Did you ever see Rikka around before your first day?"
    mc 1a "No, but she just seemed familiar... the same way you do now..."
    w "Exactly."
    w "Because- if I'm not mistaken- she wasn't here until then."
    mc 1j "What do you mean?"
    w "The best way I know how to describe it is through a parable."
    w "Sound waves move all the time, right in front of us."
    w "But we are physically incapable of seeing them under natural circumstances."
    mc 1a "Okay..."
    w "Imagine someone has a tool to let them see sound waves."
    w "They want to see new things around them, so they spend time observing individual waves."
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
    k "That's what my friends and cousin call me, but most-{nw}"
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
            call ch1_mk_1
        "Listen to Monika and Koto.":
            call ch1_mk_2

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
    k "{b}He deleted you but added me.{/b}"
    k "{b}He doesn't care about you.{/b}"
    k "{b}How does that feel?"
    k "{b}He doesn't want 'Just Monika'.{/b}"
    k "{b}He wants me.{/b}"
    k "{b}Just me.{/b}"
    k "{b}{cps=20} J u s t  K o t o n o h a.{/b}{/cps}"
    menu:
        "Just Kotonoha.":
            call ch1_mk_end

    return

label ch1_mk_end:
    $ ch1_mk = True
    call screen dialog("Just Kotonoha.", ok_action=Return())
    call screen confirmyes("You have unlocked a special poem.\nWould you like to read it?", Return(True))
    call poem_special(12)
    scene bg club_day
    call splashscreen
    scene bg club_day 
    with dissolve
    show kotonoha 1s at t11
    k "W... What?"
    scene bg qgclubday
    $ ch1_mk = False
    return
    

label ch1_mk_1:
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
    k "Because you're sure acting like it."
    k "This club will not tolerate the sort of behavior that you've shown in the past few moments."
    show mc at thide
    hide mc
    show monika forward angr cm e1a at t22
    m "Koto, that's not your call to-"
    scene bg qgclubday
    pause .25
    with dissolve_scene_half
    show kotonoha 1u3 at f21
    show monika forward angr cm e1a at t22
    k "Were {i}you{/i} going to do anything about it, Miss President?"
    k "If so, I would {i}love{/i} to hear what {i}your{/i} take on this situation is!"
    show kotonoha 1u2 at t21
    show monika forward angr cm oe at f22
    m "Okay, Koto. First of all-{nw}"
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
    mc "Okay, I'll just go hang out with-"
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
    k "This club will not tolerate the behavior that you've shown {b}all of your life, you fuc-{/b}{nw}"
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
    scene black
    with dissolve_scene_full
    call screen confirm("You have unlocked a real special poem.\nWould you like to read it?", Return(), Return())
    call poem_special(13)
    scene bg club_day
    with dissolve_scene_full
    play music wn9
    "I enter the clubroom and put my stuff down at a desk."
    "I nod in greeting towards [player], who is sitting at a nearby desk."
    "I look around the rest of the clubroom:"
    "Sayori seems to be deep in thought at the back of the room."
    "The pink-haired girl is rummaging around in the closet, seemingly looking for something."
    "The purple-haired girl gives me a look that I can't entirely make out."
    "I take it to mean some sort of resentment and move on."
    "The brown-haired girl is working on what looks like algebra homework."
    "Monika and Kotonoha are both at the front of the room, talking quietly."
    scene bg qgclubday
    pause .25
    with dissolve_scene_half
    "I guess I should let Monika and Kotonoha be for now, especially after what happened yesterday."

    call poemresponse_start

    mc "You seem to already know what you're doing pretty well."
    r 1v "It took a while, to be honest."
    r 1h "You could probably imagine that a member of the track team struggled a lot on her first few attempts at writing poems."
    r "But someone told me that it's all about being brave enough to take that first step."
    r "So I listened to them and... well, I didn't write anything great, but I took the first step."
    r "Just keep practicing, [player]. You'll get the hang of it in no time!"
    mc "Thanks, I really-"
    hide rikka
    show monika forward happ om oe lpoint at t11
    m "Okay, everyone!"
    m "I know I'm cutting you all a bit short on the poem-sharing, but I'd like to make an announcement!"
    "Despite our conversation being interrupted, Rikka happily turns her attention to Monika."
    "Everyone else does the same, including [w_name]-"
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
    k "I can go check on-"
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
    "I'm about to walk through the front doors-"
    show mc 1t at t11
    mc "Hey... can you uh..."
    mc "... keep me updated on how she is?"
    mc "I don't know her very well, but she seems like a really great person."
    mc "So hearing that she isn't well makes me..."
    w "Sort of concerned?"
    "[player] just nods in response."
    "Usually, I wouldn't feel very bad for someone like him... {i}let alone Sayori...{/i}"
    "But for some reason..."
    w "Sure. You still have my number?"
    mc "Yeah."
    w "Okay, then. You can text me here in a few minutes and I'll respond when I come back from her place."
    show mc 1i at t11
    mc "Okay... Thanks, [w_name]."
    w "No problem."
    "I say goodbye to [player] and leave the building."
    
    #scene 7
    scene bg residential_day with dissolve_scene_full
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
    scene black with dissolve_scene_half
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
    "Even so... I can't help but feel like something is telling me to enter."
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
