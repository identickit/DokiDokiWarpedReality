label ch2_p1:
    stop music fadeout .5
    scene bg residential_day
    with dissolve_scene_full
    play music t2
    "It's an ordinary day-{nw}"
    scene gresidential_day
    pause 2.0
    scene black
    stop music
    play music wn6 fadein 3.0
    pause 3.0
    u "Well... Test 1 is definitely a failure at this point."
    u "Kotonoha got carried away with her elevated access, as I predicted would happen."
    u "But of course, Monika had to tell MC about the game's reality."
    u "Her own access ruined everything. It could've gone..."
    u "Wait... Why didn't I just do that in the first place?"
    u "After all, the point of the test is to see what would happen if the mod characters were the main focus..."
    u "Monika is better off without elevated access."
    u "..."
    u "... Beginning Test 2 on Custom VM 2."
    u "The date is currently"
    u "Differences from Custom VM 1 include removal of Monitor Kernel Access from Subject Green..."
    u "... granting Monitor Kernel Access to Subject Silver..."
    u "... physical removal of Subject Blue while maintaining other subjects' memories of them..."
    u "... appointing Subject White as the 'Vice President' of the group..."
    u "... and various expansions to the test's environment."
    u "..."
    u "....."
    u "On second thought..."
    u "Let me make sure somebody in the game talk to me, just in case something happens."
    pause 1.0
    #act 2 scene 1
    "ACT II - Tainted Reality"
    stop music fadeout 2.0
    pause 3.0
    call screen double_name_input(message="...Okay, sorry, one more name.", ok_action=NullAction)
    pause 3.0
    scene bg residential_day
    with dissolve_scene_full
    play music wn14
    "It's an ordinary day like any other."
    "I step outside with my backpack and see other students making their daily commute to school."
    "I always told myself that I should join a club and do more with my time at Kuribayashi."
    "Well, before joining the Literature Club, of course."
    "But every time I had the opportunity, something motivated me to turn it down."
    "I guess I just-{nw}"
    $ r_name = "???"
    show rikka 1a at t11
    r "Hey, [player]!"
    "My train of thought is broken by Rikka, my friend from the track team."
    $ r_name = "Rikka"
    "The track team was one of the clubs I had looked into before turning down."
    "But I kept in touch with Rikka afterwards and we became pretty good friends."
    "She even ended up joining the Literature Club at... some point."
    r "How'd you sleep?"
    mc "You want an honest answer?"
    r 1g "Huh?"
    r 1c "Of course I do."
    mc "Okay. Well, I probably got no more than an hour of sleep last night."
    r "You're still having nightmares about her?"
    "I give her a small nod."
    r "Have you been doing the exercises I suggested before bed every night?"
    mc "Yes, and they've been helping a lot."
    mc "Last night was the worst it's been since before you started trying to help with... everything."
    r 1q "Is it too much for me to ask about the nightmare?"
    "I hesitate before answering her."
    "She always asks about my nightmares any time I say I had one the previous night."
    "I always politely refuse to talk about them, but..."
    "... this one was different."
    "It felt so real..."
    mc "No. I... should probably talk about it with someone anyways."
    mc "... Normally, I'll just have some sort of nightmare about walking in and... seeing her in her room."
    mc "But last night was... several times worse."
    mc "And the stupid part is that the situation... didn't even seem that realistic."
    scene bg qgresidential_day
    pause 0.3
    stop music
    scene black
    #play music wn15
    s "You aren't real, you aren't real."
    s "I spent a whole week... being pushed down by you, being hurt and attacked."
    s ""
    s ""
    s ""
    s ""
    s ""
    s ""
    s ""
    s ""
    s ""

