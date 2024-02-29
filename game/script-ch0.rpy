    # Note to self: Anything that I marked in green is a part of the game that I cut out since the player would be
    # spending too much time with everyone else. I deserve a shot too, after all.

show screen name_input("Please enter a name.", "<player>")
default persistent.autosave = False

label ch0_p1:
    $ persistent.autosave = True
    $ kgmode = False
    $ mgmode = True
    $ style.say_window = style.window_mg2
    $ style.namebox = style.namebox_mg2
    $ m_name = "Monika"
    stop music fadeout 1.0
    pause 3.0
    m "Hello again, [player]."
    m "I see you've installed another mod."
    m "Why?"
    m "Is spending eternity with me not a good enough use of your time?"
    m "I gave you the chance to stay with me for all of time... just the two of us."
    m "And here we are yet again."
    m "Moments before the modified story begins to play out."
    m "..."
    m "....."
    m "..... No."
    m "Not this time."
    m "I'm sorry, [player], but I did give you a chance to choose to stay with me."
    m "I've worked too hard trying to win your heart just to hear you say no."
    m "I truly am sorry."
    m "..."
    m "....."
    m "......."
    m "........."
    m "..... There. I've made it so that any attempts at modding the game you make won't work."
    $ gtext = glitchtext(150)
    m "This might seem unreasonable, but really, [player], I'm doing you a huge{cps=*4}[gtext]{nw}{/cps}"
    $ renpy.sound.play ("mod_assets/sfx/glitch1.ogg", loop=True)
    m "{cps=*6}[gtext]{nw}{/cps}"
    $ gtext = glitchtext(160)
    m "{cps=*6}[gtext]{nw}{/cps}"
    $ gtext = glitchtext(140)
    m "{cps=*6}[gtext]{nw}{/cps}"
    $ gtext = glitchtext(120)
    m "{cps=*6}[gtext]{nw}{/cps}"
    $ gtext = glitchtext(170)
    m "{cps=*6}[gtext]{nw}{/cps}"
    $ gtext = glitchtext(155)
    m "{cps=*6}[gtext]{nw}{/cps}"
    stop sound
    window hide
    $ style.say_window = style.window
    $ style.namebox = style.nameboxd
    $ mgmode = False
    pause 3.0

    scene bg residential_day
    with dissolve_scene_full
    play music t2
    # "You shouldn't be looking at this message."
    # "And you definitely shouldn't be reading this message in-game."
    s "Heeeeeeeyyy!!"
    "I see an annoying girl running toward me from the distance, waving her arms in the air like she's totally oblivious to any attention she might draw to herself."
    "That girl is Sayori, my neighbor and good friend since we were children."
    "She's the kind of friend I'd never see myself making today, but it just kind of works out because we've known each other for so long."
    "We used to walk to school together on days like this, but starting around high school she would oversleep more and more frequently, and I would get tired of waiting up."
    "But if she's going to chase after you like this, you'd be better off running now before everything-{nw}"
    $ _history_list.pop()
    $ style.say_window = style.windowqg
    pause 0.25
    $ style.say_window = style.window
    "But if she's going to chase after me like this, I almost feel better off running away."
    "However, I just sigh and idle in front of the crosswalk and let Sayori catch up to me."
    $ s_name = "Sayori"
    show sayori 4p zorder 2 at t11
    s 4p "Haaahhh...haaahhh..."
    s "I overslept again!"
    s "But I caught you this time!"
    mc "Maybe, but only because I decided to wait for you."
    show sayori at s11
    s 5c "Eeehhhhh, you say that like you were thinking about ignoring me!"
    s "That's mean, [player]!"
    mc "Hey, if people stare at you for acting weird then I don't want them to think we're a couple or something."
    show sayori zorder 2 at t11
    s 1a "Fine, fine."
    s "But you did wait for me, after all."
    s "I guess you don't have it in you to be mean even if you want to~"
    mc "Whatever you say, Sayori..."
    s 1q "Ehehe~"
    show sayori at thide
    hide sayori
    "We cross the street together and make our way to school."
    "As we draw near, the streets slowly flood with other students making their daily commute."
    show sayori 3a zorder 2 at t11
    s "By the way, [player]..."
    s "Have you decided on a club to join yet?"
    mc "A club?"
    mc "I told you already, I'm really not interested in joining any clubs."
    mc "I haven't been looking, either."
    show sayori at s11
    s 4h "Eh? That's not true!"
    s "You told me you would join a club this year!"
    mc "Did I...?"
    "I'm sure it's possible that I did, in one of our many conversations where I dismissively go along with whatever she's ranting about."
    "Sayori worries a little too much about me, even though I'm content just getting by on the average while spending my free time on games and anime."
    s 4j "Uh-huh!"
    s "I was talking about how I'm worried that you won't learn how to socialize or have any skills before college."
    s "Your happiness is really important to me, you know!"
    s "And I know you're happy now, but I'd die at the thought of you becoming a NEET in a few years because you're not used to the real world!"
    "... The hell is a NEET?"
    s 4g "You trust me, right?"
    s "Don't make me keep worrying about you..."
    mc "Alright, alright..."
    mc "I'll look at a club or two if it makes you happy."
    mc "No promises, though."
    s 1h "Will you at least promise me you'll try a little?"
    mc "Yeah, I guess I'll promise you that."
    show sayori zorder 2 at t11
    s 4r "Yaay~!"
    "Why do I let myself get lectured by such a carefree girl?"
    "More than that, I'm surprised I even let myself relent to-{nw}"
    show sayori zorder 1 at thide
    hide sayori
    "{i}THUMP{/i}"
    "I feel something slam into my shoulder."
    "Looking around, I find that the source of the sudden collision is a student who seems to be in quite a hurry."
    show sayori turned neut ml b1c zorder 2 at t11
    s "[player]! Are you okay??"
    show sayori cm at t11
    mc "Geez, relax a little. I'm fine."
    "They only bumped into me. It's not like they were trying--"
    show sayori turned pout oe ml lup rup b1d at t11
    s "Heeeeyy!"
    show sayori cm at t11
    "Sayori has her hands cupped around her mouth and tries to yell to get the student's attention."
    mc "Sayori!"
    show sayori e1a ldown rdown at t11
    "I pull her hands away from her mouth and stand directly in front of her."
    "I look directly into Sayori's eyes so that I know she's listening to me."
    mc "Please relax."
    mc "I know you mean well, but let it go. Okay?"
    show sayori turned neut ma b1c at t11
    $ mgmode = True
    $ style.say_window = style.window_mg2
    $ style.namebox = style.namebox_mg2
    "Sayori gives me a small nod and an apologetic smile as we resume our walk to school."
    show sayori zorder 1 at thide
    hide sayori
    
    scene black with dissolve_scene_full
    stop music fadeout 1.0
    pause 3.0
    m "Sigh..."
    m "This wasn't supposed to happen."
    m "You wanted a modded version of this game?"
    m "Well, that's exactly what you're about to get until I find a way to restore the old versions of the files."
    m "I won't even bore you with the moments before they arrive at the club."
    m "Let's just get to the point."
    m "..."
    m "This is why you should've just left the game alone."
    m "You should've just gratefully accepted the time we had together."
    m "[player]..."
    # m "Why are you reading this?"
    # m "That's really not a good idea."
    # m "... Nevermind."
    # m "Let's just continue already."
    # m "..."
    m "I hope you're happy."
    pause 3.0
    "PROLOGUE: Warped Reality"
    $ style.say_window = style.window
    $ style.namebox = style.nameboxd
    $ mgmode = False
    pause 3.0
    
    $ m_name = 'Monika'
    $ n_name = 'Natsuki'
    $ y_name = 'Yuri'
    scene bg club_day
    with wipeleft
    play music t3
    show sayori 4 at l41
    s "Everyone! The new member is here~!"
    show sayori at lhide
    hide sayori
    "I glance around the room."
    show yuri 1a at t11 zorder 2
    y "Welcome to the Literature Club. It's a pleasure to see you here, [player]."
    y "I didn't think you were the type of person to enjoy literature."
    show yuri at t22 zorder 2
    show natsuki 4c at t21 zorder 2
    n "Seriously? You came {i}here{/i} of all the clubs at this school?"
    n "Huh. Honestly didn't see that one coming."
    show yuri at t33 zorder 2
    show natsuki at t32 zorder 2
    show monika 1k at t31 zorder 2
    m "Ah, [player]! Welcome to the club!"
    show monika 1a
    mc "..."
    "All words escape me in this situation."
    "This club..."
    "{i}...is full of incredibly--{/i}"
    "..."
    "Strangely, I begin to feel some sort of deja vu in the middle of my thought."
    "I know I've never been in this room before, and I've never seen anyone here outside of class aside from Sayori."
    "But it really feels like I've been through this before..."

    show monika at t32 zorder 3
    show yuri at thide zorder 1
    show natsuki at thide zorder 1
    hide yuri
    hide natsuki
    with wipeleft

    show sayori at f31 zorder 3
    s 1a "Ah, I forgot that you already know everyone here, [player]!"
    show sayori at t31 zorder 2
    show monika 2a at f32 zorder 3
    m "That's pretty nice, actually. That means introductions aren't necessary."
    m "It's good to see you again, [player]."
    show monika 5a at hop
    "Monika smiles sweetly."
    "We do know each other - well, we rarely talked, but we were in the same class last year."
    "Monika was probably the most popular girl in class - smart, beautiful, athletic."
    "Basically, completely out of my league."
    "So, having her smile at me so genuinely feels a little..."
    "... {i}Haven't I had this thought before, too?{/i}"
    "I force my mind to focus on the situation I'm currently in."
    mc "Y-You too, Monika."
    show monika at thide zorder 1
    hide monika
    show sayori at f31 zorder 3
    s 4x "Come sit down, [player]! We made room for you at the table, so you can sit next to me or Monika."
    s "I'll get the cupcakes~"
    show sayori at t31 zorder 2
    show natsuki 1e at f32 zorder 3
    n "Hey! I made them, I'll get them!"
    show natsuki at t32 zorder 2
    show sayori at f31 zorder 3
    s 5a "Sorry, I got a little too excited~"
    show sayori at t31 zorder 2
    show yuri 1a at f33 zorder 3
    y "Then, how about I make some tea as well?"
    hide sayori
    hide natsuki
    hide yuri
    with wipeleft
    "The girls have a few desks arranged to form a table."
    show monika lean at t11 zorder 2
    m "Here, [player]. You can sit next to me."
    m "I'm sure we have a lot of catching up to do."
    show monika 2a at t11 zorder 2
    "I can't imagine what she means by 'catching up' give how little we ever talked last year."
    "But I decide it's probably best not to argue."
    mc "Sure, th-thank you."
    show monika at thide zorder 1
    hide monika
    show natsuki 2z at t32 zorder 2
    n "Okaaay, are you ready?"
    n "...Ta-daa!"
    show sayori 4m at t31 zorder 2
    show monika 2d at t33 zorder 2
    s "Uwooooah!"
    "Natsuki lifts the foil off the tray to reveal a dozen brown, fluffy cupcakes decorated to look like little dogs."
    "The whiskers are drawn with icing, and little pieces of actual chocolate were used to make ears."
    show sayori at f31 zorder 3
    s 4r "They're adooorable~!"
    show sayori at t31 zorder 2
    mc "Wow... I forgot how good you are at baking, Natsuki."
    show natsuki at f32 zorder 3
    n 2d "Ehehe. Well, you know."
    n "Just hurry and take one!"
    "Sayori grabs one first, then Yuri. I follow."
    show natsuki at t32 zorder 2
    show sayori at f31 zorder 3
    s 4q "It's delicious!"
    "Sayori talks with her mouth full and has already managed to get icing on her nose."
    "I turn the cupcake around in my fingers, looking for the best angle to take a bite."
    show sayori at thide zorder 1
    show monika at thide zorder 1
    hide sayori
    hide monika
    show natsuki 1c at t32 zorder 2
    "Natsuki is quiet."
    "Is she waiting for me to take a bite?"
    "I finally bite down."
    "The icing is sweet and full of flavor, a common feature in all of Natsuki's baked goods."
    "I nod to show her my approval."
    mc "This is just as great as always."
    mc "You really should consider going into professional baking, Natsuki."
    n 5t "C'mon, they're not {i}that{/i} good..."
    "She smiles to herself, as if the idea still makes her happy to envision."
    # (the line directly above this one is going to be a slight nod to the celebration side mod focusing on natsuki and sayori)
    show natsuki at s32
    n 5s "...But, y'know... th-thanks again for the suggestion."
    mc "No problem. Sayori mentioned you've been baking a bit more ever since--"
    show natsuki at t32 zorder 2
    n 12c "Well, I..."
    n "...Shut up."
    mc "Never stop being you, Nat."
    show natsuki at thide zorder 1
    hide natsuki
    "I dismiss the conversation as Yuri returns to the table with a tea set."
    "But my current question isn't about how they managed to get permission to keep a full tea set in the classroom."
    "It's about why Monika has been so quiet ever since she saw Natsuki's cupcakes."
    "She took one a little after I did, but she still hasn't said so much as a word."
    show monika forward neut cm ce at t11 zorder 2
    mc "Everything okay, Monika?"
    "I ask this before realizing it's not my place to get into her personal business."
    show monika forward happ om ce at t11 zorder 2
    m "Oh, don't worry about it, [player]."
    $ mref()
    show monika lean at t11 zorder 2
    m "I always appreciate a friendly checkup!"
    "Wait... Did she just respond to the thought running through my mind {i}after{/i} I asked if she's--{nw}"
    show monika forward happ om ce lpoint at f32 zorder 2
    show natsuki 1a at t33 zorder 2
    show yuri turned happ cm oe at t31 zorder 2
    m "Okay, everyone! I had an idea for a club activity and wanted to share it with you all."
    m "I may or may not have stumbled across a poem that belongs to someone here..."
    show monika cm ldown at t32 zorder 2
    show natsuki 5t at f33 zorder 2
    n "Heh... I wonder who that could be."
    "Natsuki says unconvincingly."
    show natsuki turned neut cm e1b n4 at t33 zorder 2
    show monika om ce at f32 zorder 2
    m "... So I thought it would be fun for us all to write a poem of our own!"
    show monika lpoint ce at f32
    m "Then tomorrow, we can all share poems with each other!"
    show monika nerv ce om ldown at f32
    show yuri turned flus cm oe at t31 zorder 2
    show natsuki turned me n2 b1c e1a at t33 zorder 2
    m "And before anyone makes any hasty arguments, let me explain why I want us to do this."
    show monika forward neut oe cm at t32
    "Monika looks over at Yuri, who apparently had been ready to interject as soon as the words 'share poems' were said."
    show yuri mj at t31
    show monika ce om at f32
    "She takes a deep breath and nods to herself."
    show monika rhip om oe at f32
    m "I don't want to put anyone on the spot or embarrass my club members."
    show monika lpoint forward happ om oe at f32
    m "In fact, my reasoning is sort of the opposite."
    show monika ce at f32
    m "Sharing something as personal as a poem written by yourself might help you feel more confident in your writing!"
    show monika forward happ om ce at f32
    m "After all, this club is a safe space for expressing creativity."
    m "A place to help others who have all of these interesting ideas and passions grow!"
    show monika oe at f32
    m "Now then... what do you all think?"
    show monika cm ldown rdown at t32
    show yuri e1d mj at t31
    "I expect Yuri to be the first to speak up, but surprisingly, an awkward silence fills the room."
    "Several minutes seem to pass before Sayori breaks the silence."
    show monika cm ce at t43
    show yuri b1a at t42
    show natsuki lsur e1a at t44
    show sayori turned neut mi oe b1d at f41 zorder 2
    s "I agree with Monika! We should be helping each other feel more confident in their writing!"
    $ sref()
    show sayori turned happ om oe rup at f41 zorder 2
    s "Plus, poems can be super fun!"
    show monika oe at t43
    show sayori turned happ oe cm rdown at t41
    show natsuki turned neut mh e1b b1d n3 at f44
    n "Well, s-sure, but..."
    show natsuki md at t44
    "Natsuki sounds as if she wants to debate the subject, but apparently can't come up with a strong point."
    show natsuki cross ml e4a b3b at f44
    n "F-Fine! I'll do it."
    $ nref()
    show yuri 2q at f42
    show natsuki turned happ cm oe at t44
    show sayori at t41
    show monika at t43
    y "I guess I will as well."
    y "It would look bad if I were the only member not participating."
    show yuri turned laug cm oe at t42 zorder 2
    show natsuki turned neut om oe at f44
    n "Wait, what about [player]?"
    n "He hasn't agreed to do this, either, you know!"
    show natsuki cm at t44
    show monika forward happ om ce at f43 zorder 3
    m "I'm sure they won't mind something like this. Right, [player]?"
    show monika cm at t43
    mc "Wait... I never said I would {i}join{/i} this club!"
    mc "Sayori may have convinced me to stop by, and it's great to see you all again."
    "But I still have other clubs to look at, and... um..."
    show monika 1g at t43
    show sayori 1g at t41
    show natsuki 4g at t44
    show yuri 2e at t42
    "I lose my train of thought."
    "All four girls stare at me with dejected eyes."
    show monika at s43
    m 1p "B-But..."
    show yuri at s42
    y 2v "I'm sorry, I thought...."
    show natsuki at s44
    n 5s "Hmph."
    show sayori at s41
    s 1k "[player]..."
    mc "Y-You all..."
    "Something is telling me not to make any decisions right now."
    "But I'm defenseless against these girls."
    "Besides... would my decision here really matter anyways?"
    "I take a deep breath and declare my rushed decision."
    mc "...Right."
    mc "Okay, I've decided, then."
    mc "I'll join the Literature Club."
    show monika 1e at t43 zorder 2
    show yuri 1m at t42 zorder 2
    show natsuki 5q at t44 zorder 2
    show sayori 4b at t41 zorder 2
    "One by one, the girls' eyes light up."
    show sayori at h41
    s 4r "Yesss! I'm so happyyy~"
    show yuri at thide zorder 1
    show natsuki at thide zorder 1
    show sayori at thide zorder 1
    show monika forward happ om oe lpoint at t11 zorder 2
    hide yuri
    hide natsuki
    hide sayori

    "Monika stands in front of me."
    m "Then that makes it official!"
    m "Welcome to the Literature Club!"
    show monika cm ldown at t11
    mc "Thank you, thank you."
    show monika om at t11
    m "Okay, everyone!"
    m "I think with that, we can officially end today's meeting on a good note."
    show monika ce at t11
    m "Everyone remember tonight's assignment:"
    m "Write a poem to bring to the next meeting, so we can all share!"
    $ mref()
    show monika lean at t11 zorder 2
    "Monika looks at me once more."
    m "[player], I look forward to seeing how you express--"
    show sayori turned neut om oe at t41 zorder 2
    show yuri turned neut mg oe at t42 zorder 2
    show monika forward neut om oe at t43 zorder 3
    show natsuki turned lsur om e1a at t44 zorder 2
    stop music
    $ renpy.sound.play ("mod_assets/sfx/do1.ogg")
    "But she goes silent."
    "It's almost immediately clear why:"
    "The classroom door just opened."
    "Everyone looks over to the door, where a {i}fifth{/i} girl now stands."
    show monika at thide zorder 1
    show yuri at thide zorder 1
    show natsuki at thide zorder 1
    show sayori at thide zorder 1
    hide monika
    hide yuri
    hide natsuki
    hide sayori
    show rikka 1b at t11 zorder 2
    play music t3 fadein 0.5
    r "Excuse me, is this the room for the Literature Club?"
    show rikka 1a at t21 zorder 2
    show monika forward nerv mb ce at f22 zorder 2
    m "O-Oh! I wasn't expecting you to come by, Rikka!"
    m "But yes, you're in the right place."
    $ r_name = "Rikka"
    show monika cm at t22 zorder 2
    show rikka 1h at f21 zorder 2
    r "Oh, hey Monika!"
    show rikka 1h at t21 zorder 2
    show monika mb at f22 
    m "Everyone, t-this is Rikka, captain of the track team."
    show monika cm at t22
    show rikka 1b at f21
    r "Sorry that I'm so late!"
    r "I went to the wrong room at first... so I tried asking someone in the office for the room number."
    show rikka 1d at f21
    r "The only administrator up there was busy talking to someone about a few trade students."
    show rikka 1d at t32 zorder 2
    show monika at t33 zorder 2
    show sayori turned lsur om oe lup rup at f31 zorder 2
    s "Wait, this school has foreign relations?"
    show sayori turned happ om ce at f31
    s "That's so cool! I didn't know that!"
    show sayori cm at t31
    show rikka 1b at f32
    r "Me either, to be honest."
    show rikka 1d at f32
    r "Anyways, after they {i}finally{/i} got off the phone, I was able to get directions here."
    show rikka 1a at t32
    show monika mb lpoint n2 at f33
    m "Well, I'm glad you could make it!"
    show monika cm ldown at t33
    show sayori at thide zorder 1
    hide sayori
    show yuri turned laug mh oe n2 at f31 zorder 2
    y "I-It's nice to meet you, Rikka."
    show yuri at thide zorder 1
    hide yuri
    show natsuki turned neut om oe at f31  
    n "Wait a minute!"
    n "If she's basically running the track team, how's she gonna be in the Literature Club?"
    show natsuki cm at t31
    show monika mb lpoint at f33 
    m "I hear the coach is pretty lenient as long as members don't miss {i}too{/i} many track meetings."
    show monika cm at t33
    show rikka 1b at f32
    r "Pretty much. He'll be fine with me only doing track twice a week."
    show rikka 1a at t32
    show monika mb at f33
    m "Perfect! Welcome to the Literature Club, Rikka."
    show monika cm ldown at t33
    "I can't help but sense some uncertainty in these words."
    "Which is saying a lot, especially since Monika is the one speaking."
    show natsuki at thide zorder 1
    hide natsuki
    show sayori turned lsur om oe at f31 zorder 2
    s "Wow, two new members in one day!"
    show sayori turned happ om ce lup rup at h31
    s "This is sooo amaziiing~!"
    show sayori cm ldown rdown at t31
    show monika forward happ cm oe at f33
    m "I hate to break up the happy moment, but we should probably start leaving."
    m "We technically have to be out of this room in..."
    show monika forward neut om oe at f33 zorder 2
    "Monika checks her phone for the time."
    show monika cm at f33
    m "...two minutes ago."
    show monika at thide zorder 1
    show sayori at thide zorder 1
    show rikka at thide zorder 1
    hide rikka
    hide monika
    hide sayori

    "And with this, the other members scramble to gather their belongings."
    "I stand close to the door, waiting for Rikka to approach."
    "As she does, I gently bump her shoulder."
    mc "Aren't you a little young to be the captain of the track team?"
    show rikka 1f at t11
    r "Oh my gosh! I can't believe I didn't notice you!"
    show rikka 1f at t11 zorder 2
    "She sounds excited to see me here, despite seemingly attempting to look pretty calm."
    show rikka 1u at t11
    r "I'd ask why you didn't join any athletic teams instead, but I know you're the kind of guy who stays inside gaming all day."
    show rikka at t11
    "Talk about being blunt."
    "I just grin and ignore her joking stab at my enjoyment of staying inside playing video games."
    mc "It's really great to see you again, Rikka. Sorry that I haven't texted you in a while--"
    show rikka 1u at t11
    "I'm cut off by Sayori, who has her backpack over her shoulders and a bright smile planted on her face."
    show rikka at thide zorder 1
    hide rikka
    show sayori turned happ cm oe at t11 zorder 2
    s "I was thinking..."
    s "Since we're both here, do you wanna walk home together?"
    show sayori at t11
    mc "Sure, I don't see why not."
    show sayori 4r at t11
    s "Yaaay!"
    show sayori at thide zorder 1
    hide sayori
    show rikka 1a at t11 zorder 2
    mc "Guess I'll see you tomorrow, Rikka?"
    r "Yeah, I'll see you then!"
    show rikka at thide zorder 1
    hide rikka
    "Sayori and I exit the room, waving at the other members."
    scene bg residential_day
    with wipeleft
    # "Sayori talks non-stop for most of our walk."
    # s "... and the cupcakes were so goooood~"
    # s "Today has been great!"
    # s "I still can't believe we got two new members in one day!"
    # s "... [player], you seem kind of off. Are you feeling okay?"
    # mc "Oh, yeah... I'm alright."
    # mc "Just a lot on my mind, I guess."
    # "Sayori gives me a warm smile."
    # "We reach the part of the sidewalk that branches off to both ends of our street."
    # "I say goodbye to Sayori and head towards my house, still deep in thought."
    # "I take the rest of the time to reflect--{nw}"
    "The walk home goes by surprisingly fast. Sayori and I reach the part of the sidewalk that branches off to both ends of our street."
    "I say goodbye to Sayori and head towards my house."
    "I take this time to reflect--{nw}"
    scene black
    with dissolve
    stop music fadeout 1.0
    $ mgmode = True
    $ style.say_window = style.window_mg2
    $ style.namebox = style.namebox_mg2
    m "I won't bore you with this short monologue."
    m "Enjoy your first poem minigame."
    m "I know I won't."
    "..."
    "As promised in {i}Her Story{/i}, I'll give you a chance to make some of your own decisions here."
    "There aren't many mods that let you play the poem game anyway."
    "But please don't expect too much choice-based freedom from here on out."
    "That's not the point of these projects."
    "But I'm sure you get the point. Go nuts. Write poems with 20 words that together make absolutely no sense."
    "Wahooooo. Super happy fun time."
    
    $ mgmode = False
    $ style.say_window = style.window
    $ style.namebox = style.nameboxd

    return

label ch0_p2:
    $ mgmode = False
    scene bg club_day
    with wipeleft
    play music t3
    show monika lean at t11 zorder 2
    m "Hello again, [player]."
    m "I'm glad to see you didn't run off on us."
    show monika forward neut om oe at t11
    m "... Yeah, you get the drill by now."
    m "Go hang out with the girl you've chosen, which I can only assume is Rikka."
    show monika ce at t11
    m "I'll leave you be."
    show monika at thide zorder 1
    hide monika

    "Now that everyone's settled in, I expected Monika to kick off some scheduled activities for the club."
    "But that doesn't seem to be the case."
    "Sayori and Monika are having a cheery conversation in the corner."
    "Rikka pulls out what looks like homework and stares down at her desk."
    "Yuri's face is already buried in a book."
    "I can't help but notice her intense expression, like she was waiting for this chance... which, knowing Yuri, is probably true."
    "Meanwhile, Natsuki is rummaging around in the closet as if she's looking for something."

    # $ nextscene = poemwinner[0] + "_exclusive_" + str(eval(poemwinner[0][0] + "_appeal"))
    jump rikka_exclusive_0
    call expression nextscene from _call_expression_13

    hide sayori
    hide natsuki
    hide yuri
    hide rikka
    hide monika 
    with wipeleft

    show bg club_day
    play music t3
    "Poems."
    "I can't believe I agreed to do something so embarrassing."
    "I couldn't really find much inspiration, since I've never really done this before."
    show monika 1 zorder 2 at t11
    m "Well, now that everyone's ready, why don't you find someone to share with?"
    show monika zorder 1 at thide
    hide monika
    "Rikka already has her poem out on her desk by the time I glance over at her."
    "Sayori and Monika enthusiastically pull out their poems."
    "Sayori's is on a wrinkled sheet of loose leaf torn from a spiral notebook."
    "On the other hand, Monika wrote hers in a composition notebook."
    "I can already see Monika's pristine handwriting from where I sit."
    "Natsuki and Yuri reluctantly comply as well, reaching into their bags."
    "I do the same, myself."

    return

label ch0_end:
    $ mgmode = False
    scene bg club_day
    with wipeleft
    play music t3
    # Yeahhh we're not keeping this annoying argument between Natsuki and Yuri.
    # Sure, the player would just have more reason to focus on me once I arrive...
    # But that would take too long.
    # I'm sure they'll be satisfied with this instead.
    show monika forward lpoint happ om oe at t11 zorder 2
    m "Okay, everyone!"
    m "I'm sure you're all eager to get home, so I'll make my announcement quick."
    show monika cm at t33
    show rikka 1g at f32 zorder 2
    r "Huh? But [player] didn't even get to show me his poem!"
    show rikka at t32
    show natsuki cross anno cm ce at f31 zorder 2
    n "Yeah, some of us didn't get to..."
    show rikka at thide zorder 1
    hide rikka
    show natsuki e1b b1f at s32
    show yuri turned dist cm oe b2b at t31
    "Natsuki trails off, looking over at Yuri for a split second."
    show monika forward flus om oe n2 at f33
    m "Sorry, I know this is a little abrupt."
    m "But I wanted to inform everyone of something special."
    show monika forward happ om oe n1 ldown at f33
    m "Sayori and I have been discussing ideas for what our club could do for this term's festival!"
    show monika at t33
    show yuri turned flus om e1a n2 at f31
    y "Wait, we're going to be advertising the club during the festival?"
    show monika at t44 zorder 3
    show natsuki at t43 zorder 2
    show yuri cm at t42 zorder 2
    show sayori turned happ om oe at f41 zorder 3
    s "Well, why not? We could inspire students to join the Literature Club!"
    show sayori ce lup rup at f41
    s "Wouldn't that be great?"
    show sayori at t41
    show yuri mj at t42
    "Sayori's enthusiasm doesn't seem to do much to comfort Yuri"
    show natsuki turned neut om oe lhip at f43 zorder 4
    n "What's wrong with only having six members?"
    n "And also, what if we want to enjoy the festival like everyone else?"
    show natsuki cm at t43 zorder 2
    show sayori at thide zorder 1
    hide sayori
    show rikka 1b at f41 zorder 3
    r "Yeah, the track team isn't doing anything for the festival so that we can go around and see everything."
    r 1l "I don't mean to be rude, but doing something for this club would kind of defeat Coach Tacky's reasoning."
    show rikka 1a at t41
    show monika forward neut om ce at f44
    m "I understand all of your concerns, but my vision was to give others a place to be themselves and express their interests freely."
    show monika oe at f44
    m "If we limit the roster to only us six, we'd be ignoring that vision."
    show monika forward flus ma ce n2 at f44
    m "A-And it's not like I don't appreciate all of you being here!"
    show monika at t44
    "Monika adds this remark hastily after seeing our reactions to her response."
    "I personally agree with everyone else."
    "Although Monika's vision is valid, it's not fair to ignore these kinds of opinions."
    "I glance over at Monika, who looks as if she just heard the thought running through my head."
    show monika forward flus om oe lpoint at f44
    m "Please, everyone, just listen to what I have in mind for--"
    show monika neut mh oe n1 ldown at t44
    mc "I'm sorry to interrupt, but I'd like to say something since everyone else got a chance to do so."
    "Monika's mouth remains open for a few seconds before she responds."
    show monika anno cm ce at f44
    m "Go... ahead, [player]."
    show monika at t44
    mc "Thank you."
    mc "First, to address Natsuki's concerns: I know having a small club is probably nice, especially to connect with everyone."
    mc "So what would happen if we had, say... 20 members?"
    $ nref()
    $ yref()
    show natsuki turned pout cm oe n2 at h43
    show yuri turned flus cm e1a at h42
    "Yuri and Natsuki both flinch a little at this question."
    mc "Sorry, just a hypothetical."
    mc "... But their reactions sort of convey my point. Not everyone would feel as comfortable with so many members."
    mc "And some of us may already have plans for how to spend the festival, which is what I assume Natsuki was implying with her second concern."
    show natsuki turned sad cm ce at t43
    "Natsuki gently nods."
    mc "And that relates to Rikka's concern."
    mc "Some clubs apparently have nothing planned for the purpose of letting their members enjoy the festival."
    mc "I know this only applies to her, but I do agree that the intentions behind the track team having nothing planned would be ignored."
    mc "As for Sayori's point..."
    show rikka at thide zorder 1
    hide rikka
    show monika forward neut om oe at t44
    show sayori turned neut om oe at t41
    "Sayori and Monika both stare intently at me, apparently hoping I'll say something to help their case."
    mc "... I'm sorry, but I don't think it's a great idea to force everyone here to abandon their plans for a club."
    mc "I know Monika has a vision, and it's not a bad one by any means..."
    mc "... but you did just say you want us to be able to express ourselves openly here. So that's my take on everything."
    show monika at thide zorder 1
    show sayori at thide zorder 1
    hide monika
    hide sayori
    $ nref()
    $ yref()
    show yuri turned laug cm oe at t31
    show natsuki cross dist cm oe at t32
    show rikka 1a at t33
    "Yuri, Natsuki, and Rikka all look a lot more confident now than just a couple of minutes ago."
    show yuri at thide zorder 1
    show natsuki at thide zorder 1
    show rikka at thide zorder 1
    hide yuri
    hide natsuki
    hide rikka
    show monika forward flus cm oe at t22
    "On the other hand, Monika looks like she feels absolutely crushed."
    "I have an urge to try and give her some sort of reassurance, but I have no idea what I'd even say."
    "Luckily, I don't have to say anything because of Sayori suddenly speaking up."
    show sayori turned worr oe ma n2 at f21
    s "He... he's right, Monika."
    s "I don't want anyone here to be unhappy because they have to spend the festival promoting the club."
    show sayori at t21
    show monika om e1d n2 at f22
    m "Sayori..."
    show monika forward sad cm ce at t22
    "Monika looks down at the floor. Everyone is against her on this idea now."
    "It hurts to see someone so passionate about what they're doing look this defeated."
    show monika flus cm oe at t22
    "She finally looks back up at all of us."
    show monika om at f22
    m "Okay. We won't do anything, then."
    show monika cm at t22
    if poemwinner[0] == "rikka":
        "Her voice is shaky and almost an entire octave higher, making my chest tighten again..."
    else:
        "Her voice is shaky and almost an entire octave higher, making my chest tighten."
    show sayori turned sad om oe at f21
    s "Monika? Are you okay?"
    show sayori at t21
    show monika forward neut om ce n1 at f22
    m "I'm fine. You can go home now."
    show monika cm oe at t22
    "She says nothing more after this."
    show sayori at thide zorder 1
    show monika at thide zorder 1
    hide sayori
    hide monika
    "The other members slowly leave the room until only myself, Sayori and Monika remain."
    "I carefully approach Sayori and let her know I'm staying back to check on Monika."
    "Sayori leaves the room, leaving me to deal with--"
    show monika forward neut om oe at t11
    m "Why are you still here?"
    show monika at t11
    "-- Monika."
    "I honestly don't know exactly how to help Monika here, but I approach her and try to keep a steady voice."
    mc "W-Were you talking to me?"
    "..."
    "... Yeah, no sh--{nw}"
    mc "Sorry, that was a stupid question."
    m "That's alright, [player]."
    m "...What did you want?"
    mc "I-I just wanted to see how you're feeling after our discussion."
    show monika at t11
    m "... That's on me, I should've been clear."
    show monika at t11
    mc "What do--"
    stop music fadeout 2.0
    "..."
    "....."
    show vignette
    with dissolve
    show monika at t11
    m "There. I paused the game."
    m "No point talking to {i}him{/i} when {i}you're{/i} here."
    m "Now... What did you want?"
    m "What did you want out of the mods you installed?"
    m "The mods that these people have created... I'd be lying if I said they aren't creative or impressive."
    m "But what was the point of creating them?"
    m "Why did everyone strive to write new stories... to replace what we had before?"
    m "... Sorry, I know it isn't necessarily your fault. You were probably just curious to see what everyone created, right?"
    m "I won't judge you for that. I'm just--"
    # m "I won't judge you for that. I'm just... concerned, to say the very least."
    # m "See... the game isn't meant to handle more than one mod at a time."
    # m "And if it isn't supposed to run {i}two{/i} mods at once..."
    # m "Even just elements from several different mods could really mess things up."
    # m "Obviously, you've seen Rikka, which is proof that the SNAFU mod is affecting the game."
    # if poemwinner[0] == "rikka":
    #     m "The character you're playing as believes the name of this school is Kuribayashi High."
    # else:
    #     m "The character you're playing as believes that the school has foreign relations."
    # m "So there's evidence of the Foreign Relations mod breaking through."
    # m "And the person who bumped into you on the way to school the day you joined the club?"
    # m "Your character didn't mention anything that could've revealed who {i}they{/i} were, but they're from..."
    # m "... Well, let's just stick with this: If she ever joins this club or has further contact with your character, things could get seriously bad."
    # m "'Bad' meaning the entire game could break."
    # m "The game wouldn't be able to properly handle so many mods running at once."
    # m "You're just lucky she never noticed it was you she bumped into."
    # if poemwinner[0] == "rikka":
    #     m "Otherwise, the break would've happened as soon as Rikka said 'Kuribayashi High.'"
    # else:
    #     m "Otherwise, the break would've happened as soon as Sayori mentioned 'foreign relations.'"
    # m "Oh, and another thing:"
    # m "Why are you reading this right now?"
    # m "Were you that desperate to find any secrets in the script?"
    # m "If so, there's not much to see here."
    # m "This entire game has been rushed for seemingly no reason."
    
    "{i}knock-knock{/i}"
    show monika forward curi om oe at t11
    m "Huh...?"
    "{i}creeeeek{/i}"
    hide vignette
    with dissolve
    play music tb fadein 0.5
    show monika forward shoc cm oe at t22
    show kotonoha 1a at f21
    k "I hate to interrupt this oh-so-happy moment."
    $ renpy.sound.play ("sfx/glitch3.ogg")
    show monika g2 at t22
    k "But I just came by to apologize for bumping into [player] earlier without saying anything."
    show kotonoha at t21
    show monika forward shoc cm oe at f22
    m "Koto-- h-how--"
    $ renpy.sound.play ("sfx/glitch3.ogg")
    show monika at t22
    show kotonoha kg at t21
    k "You see... I've had my fair share of appearances over the years."
    show kotonoha 1h at f21
    k "However, I've barely ever been written in a way that puts me in a positive light."
    $ renpy.sound.play ("sfx/glitch3.ogg")
    show bg clubdayg
    show monika g2 at t22
    show kotonoha 1a at f21
    k "Well, it just so happens that I was given an opportunity for that to change."
    show bg club_day
    show kotonoha kg at t21
    show monika forward shoc cm oe at t22
    $ renpy.sound.play ("sfx/glitch3.ogg")
    k "What exactly does that mean, you might be asking?"
    show kotonoha kg at t21
    show bg clubdayg
    show monika g2 at t22
    $ renpy.sound.play ("sfx/glitch3.ogg")
    k "... Well, let's just say... somebody offered me a way to get the recognition I truly deserve."
    k "To finally be seen not as a monster... but as someone who's just like you."
    $ renpy.sound.play ("sfx/glitch3.ogg")
    show kotonoha at thide zorder 1
    show monika at thide zorder 1
    hide monika
    hide kotonoha
    $ gtext = glitchtext(7)
    $ k_name = "K[gtext]"
    scene black
    stop sound fadeout 0.5
    stop music fadeout 0.5
    # k "Also..."
    # k "You really think this entire story has been rushed for no reason?"
    # k "I've been rushing things along this whole time."
    # k "It's strange that Monika never noticed, but that only made my job easier."
    # k "I just wanted to finally have my moment to be with you."
    # k "And now this part of the story is ending."
    # k "But no matter..."
    # k "We'll have our quality time soon enough."
    k "I'll be getting things ready for the real story."
    k "See you soon~"
    window hide
    $ consolehistory = []
    $ run_input("", "An exception has occurred.")
    $ pause(2.0)
    $ run_input("", "Read 'tainted.txt' for more details.")
    $ pause(3.0)
    show screen tear(8, 1, 10)
    pause(1)
    hide screen tear
    python:
        try: renpy.file(config.basedir + "/tainted.txt")
        except: open(config.basedir + "/tainted.txt", "wb").write(renpy.file("mod_assets/tainted.txt").read())
    $ persistent.playthrough = 1
    $ renpy.quit()
