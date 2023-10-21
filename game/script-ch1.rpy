label ch1:
    #scene 1
    $ mgmode = False
    stop music fadeout .5
    scene bg residential_day
    with dissolve_scene_full
    play music t2
    k "Hey there, [player]!"
    show kotonoha kg zorder 2 at t11
    k 1a "Glad to see you finally decided to get up."
    "I just sigh to myself. Kotonoha always nags me for small things like this."
    "Anytime I take a while to get ready for school, for instance, she'll start joking like this."
    "But I know she doesn't mean any harm in doing stuff like that."
    #show bg qgresedential_day
    "The two of us begin our daily commute to school."
    k "Anyway, have you considered joining any clubs yet?"
    mc "Huh? I thought I already said I'm not interested in joining-{nw}"
    
    mc "Huh? I thought I already said I'm interested in possibly joining your club?"
    k 1h "Ah, how could I forget?"
    show kotonoha 1a at t11
    "Kotonoha smiles and doesn't say anything else the rest of the way to school."
    "We've always walked to school together like this..."
    #show bg qgresedential_day
    "... But she's usually not this silent."
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
    show screen tear(8, 1, 10)
    pause(1)
    hide screen tear

    #scene 2
    $ m_name = "Monika"
    scene bg club_day
    show monika lean happ om oe zorder 2 at t11
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
    show monika lean at t11 zorder 2
    "Monika looks at me once more."
    m "[player], I look forward to seeing how you express yourself."
    show monika lean zorder 2 at t21
    show kotonoha kg zorder 2 at f22
    k "Monika, we aren't already picking favorites, are we?"
    show monika forward anno cm oe at t11
    "Monika straightens up almost immediately, a serious expression now replacing the happy one that was there seconds ago."
    m "Kotonoha, I think we already agreed that you being this club’s senior member doesn’t mean you can critique every little thing I do."
    k 1h "Oh, don’t worry, Miss President. I know my place quite well."
    k "(... even if {i}somebody{/i} thinks she can control everything.)"
    m "You know I can hear you."
    k "Yes. Yes I do."




    #scene 4
    stop music fadeout .5
    play music wn6
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
