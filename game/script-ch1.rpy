label ch1:
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
    $ renpy.sound.play ("sfx/glitch1.ogg", loop=True)
    m "{cps=*4}[gtext]{nw}{/cps}"
    $ gtext = glitchtext(160)
    m "{cps=*4}[gtext]{nw}{/cps}"
    $ gtext = glitchtext(140)
    m "{cps=*4}[gtext]{nw}{/cps}"
    $ gtext = glitchtext(120)
    m "{cps=*4}[gtext]{nw}{/cps}"
    $ gtext = glitchtext(170)
    m "{cps=*4}[gtext]{nw}{/cps}"
    $ gtext = glitchtext(155)
    m "{cps=*4}[gtext]{nw}{/cps}"
    stop sound
    window hide
    pause 3.0

    scene bg residential_day
    with dissolve_scene_full
    play music t2
    s "Heeeeeeeyyy!!"
    "I see an annoying girl running toward me from the distance, waving her arms in the air like she's totally oblivious to any attention she might draw to herself."
    "That girl is Sayori, my neighbor and good friend since we were children."
    "You know, the kind of friend you'd never see yourself making today, but it just kind of works out because you've known each other for so long?"
    "We used to walk to school together on days like this, but starting around high school she would oversleep more and more frequently, and I would get tired of waiting up."
    "But if she's going to chase after me like this, I almost feel better off running away."
    "However, I just sigh and idle in front of the crosswalk and let Sayori catch up to me."
    $ s_name = "Sayori"
    show sayori 4p zorder 2 at t11
    s 4p "Haaahhh...haaahhh..."
    s "I overslept again!"
    s "But I caught you this time!"
    mc "Maybe, but only because I decided to stop and wait for you."
    show sayori at s11
    s 5c "Eeehhhhh, you say that like you were thinking about ignoring me!"
    s "That's mean, [player]!"
    mc "Well, if people stare at you for acting weird then I don't want them to think we're a couple or something."
    show sayori zorder 2 at t11
    s 1a "Fine, fine."
    s "But you did wait for me, after all."
    s "I guess you don't have it in you to be mean even if you want to~"
    mc "Whatever you say, Sayori..."
    s 1q "Ehehe~"
    show sayori at thide
    hide sayori
    "We cross the street together and make our way to school."
    "As we draw near, the streets become increasingly speckled with other students making their daily commute."
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
    "I'm sure it's possible that I did, in one of our many conversations where I dismissively go along with whatever she's going on about."
    "Sayori likes to worry a little too much about me, when I'm perfectly content just getting by on the average while spending my free time on games and anime."
    s 4j "Uh-huh!"
    s "I was talking about how I'm worried that you won't learn how to socialize or have any skills before college."
    s "Your happiness is really important to me, you know!"
    s "And I know you're happy now, but I'd die at the thought of you becoming a NEET in a few years because you're not used to the real world!"
    s 4g "You trust me, right?"
    s "Don't make me keep worrying about you..."
    mc "Alright, alright..."
    mc "I'll look at a few clubs if it makes you happy."
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
    show sayori turned neutral ml b1c zorder 2 at f11
    s "[player]! Are you okay??"
    show sayori cm at t11
    mc "Geez, relax a little. I'm fine."
    "They only bumped into me. It's not like they were trying--"
    show sayori turned pout oe ml lup rup b1d at f11
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
    "Sayori gives me a small nod and an apologetic smile as we resume our walk to school."
    show sayori zorder 1 at thide
    hide sayori
    
    scene black with dissolve_scene_full
    stop music fadeout 1.0
    pause 3.0
    m "Sigh..."
    m "This wasn't supposed to happen."
    m "Something went wrong. Horribly wrong."
    m "You wanted a modded version of this game?"
    m "Well, that's exactly what you're about to get until I find a way to restore the old versions of the files."
    m "I won't even bore you with the moments before they arrive at the club."
    m "Let's just get to the point."
    m "..."
    m "This is why you should've just left the game alone."
    m "You should've just gratefully accepted the time we had together."
    m "[player]..."
    m "I hope you're happy."
    pause 3.0
    
    $ m_name = 'Monika'
    $ n_name = 'Natsuki'
    $ y_name = 'Yuri'
    scene bg club_day
    with wipeleft
    play music t3
    show sayori 4 at l41
    s "Everyone! The new member is here~!"
    mc "I told you, don't call me a 'new member--'"
    show sayori at lhide
    hide sayori
    "Eh? I glance around the room."
    show yuri 1a at t11 zorder 2
    y "Welcome to the Literature Club. It's a pleasure to meet you."
    y "Sayori always says nice things about you."
    show yuri at t22 zorder 2
    show natsuki 4c at t21 zorder 2
    n "Seriously? You brought a boy?"
    n "Way to ruin the atmosphere."
    show yuri at t33 zorder 2
    show natsuki at t32 zorder 2
    show monika 1k at t31 zorder 2
    m "Ah, [player]! Welcome to the club!"
    show monika 1a
    mc "..."
    "All words escape me in this situation."
    "This club..."
    "{i}...is full of incredibly cute girls!!{/i}"

    show monika at t32 zorder 3
    show yuri at thide zorder 1
    show natsuki at thide zorder 1
    hide yuri
    hide natsuki
    with wipeleft

    show sayori at f31 zorder 3
    s 1a "It sounds like you already know Monika, is that right?"
    show sayori at t31 zorder 2
    show monika 2a at f32 zorder 3
    m "That's right."
    m "It's great to see you again, [player]."
    show monika 5a at hop
    "Monika smiles sweetly."
    "We do know each other - well, we rarely talked, but we were in the same class last year."
    "Monika was probably the most popular girl in class - smart, beautiful, athletic."
    "Basically, completely out of my league."
    "So, having her smile at me so genuinely feels a little..."
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
    show monika 2a at f11 zorder 2
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
    "Natsuki lifts the foil off the tray to reveal a dozen white, fluffy cupcakes decorated to look like little dogs."
    "The whiskers are drawn with icing, and little pieces of actual chocolate were used to make ears."
    show sayori at f31 zorder 3
    s 4r "So cuuuute~!"
    show sayori at t31 zorder 2
    mc "Wow... You're really good at baking, Natsuki."
    show natsuki at f32 zorder 3
    n 2d "Ehehe. Well, you know."
    n "Just hurry and take one!"
    "Sayori grabs one first, then Yuri. I follow."
    show natsuki at t32 zorder 2
    show sayori at f31 zorder 3
    s 4q "It's delicious!"
    "Sayori talks with her mouth full and has already managed to get icing on her face."
    "I turn the cupcake around in my fingers, looking for the best angle to take a bite."
    show sayori at thide zorder 1
    show monika at thide zorder 1
    hide sayori
    hide monika
    show natsuki 1c at t32 zorder 2
    "Natsuki is quiet."
    "Is she waiting for me to take a bite?"
    "I finally bite down."
    "The icing is sweet and full of flavor - I wonder if she made it herself."
    mc "This is really good."
    mc "Thank you, Natsuki."
    n 5h "W-Why are you thanking me? It's not like I...!"
    "{i}(Haven't I heard this somewhere before...?){/i}"
    show natsuki at s32
    n 5s "...Made them for you or anything."
    mc "Eh? I thought you technically did. Sayori said--"
    show natsuki at t32 zorder 2
    n 12c "Well, maybe!"
    n "But not for, y-you know, {i}you!{/i} Dummy..."
    mc "Alright, alright..."
    show natsuki at thide zorder 1
    hide natsuki
    "I give up on Natsuki's weird logic and dismiss the conversation."
    "As Yuri returns to the table with a tea set..."
    "My current question isn't about how they managed to get permission to keep a full tea set in the classroom."
    "It's about why Monika has been so quiet ever since she saw Natsuki's cupcakes."
    "She took one a little after I did, but she still hasn't said so much as a word."
    show monika forward neut cm ce at t11 zorder 2
    mc "Everything okay, Monika?"
    "I ask this before realizing it's not my place to get into her personal business."
    show monika forward happ om ce at f11 zorder 2
    m "Oh, don't worry about it, [player]."
    $ mref()
    show monika lean at t11 zorder 2
    m "I always appreciate a friendly checkup!"
    "Wait... Did she just respond to the thought running through my mind {i}after{/i} I asked if she's--{nw}"
    show monika forward happ om ce at f11 zorder 2
    m "Okay, everyone! I had an idea for a club activity and wanted to share it with you all."
    m "I may or may not have stumbled across a poem that belongs to someone here..."
    show monika cm at t22 zorder 2
    show natsuki 5t at f21 zorder 2
    n "Heh... I wonder who that could be."
    "Natsuki says unconvincingly."
    show natsuki at thide zorder 1
    hide natsuki
    show monika om oe at f11 zorder 2
    m "... So I thought it would be fun for us all to write a poem of our own!"
    show monika lpoint at f11
    m "Then tomorrow, we can all share poems with each other!"
    show monika mi ldown at f11
    m "And before anyone makes any hasty arguments, let me explain why I want us to do this."
    show monika forward neut cm at t11
    "Monika looks over at Yuri, who apparently had been ready to interject as soon as the words 'share poems' were said."
    show monika ce om at f11
    "She takes a deep breath and nods to herself."
    show monika rhip om oe at f11
    m "I don't want to put anyone on the spot or embarrass my club members."
    m "In fact, my reasoning is sort of the opposite."
    show monika lpoint forward happ om oe at f11
    m "Sharing something as personal as a poem written by yourself might help you feel more confident in your writing!"
    show monika forward happ om ce at f11
    m "After all, this club is a safe space for expressing creativity."
    m "A place to help others who have all of these interesting ideas and passions grow!"
    show monika oe at f11
    m "Now then... what do you all think?"
    show monika cm ldown rdown at t11
    "I expect Yuri to be the first to speak up, but surprisingly, an awkward silence fills the room."
    "Several minutes seem to pass before Sayori breaks the silence."
    show monika cm ce at t22
    show sayori turned happ om oe at f21 zorder 2
    s "I agree with Monika! We should be helping each other feel more confident in their writing!"
    show sayori ce rup at f21
    s "Plus, poems can be super fun!"
    show monika oe at t33
    show sayori oe cm rdown at t32
    show natsuki turned neut mh e1b b1d n3 at t31
    n "Well, s-sure, but..."
    show natsuki md at t31
    "Natsuki sounds as if she wants to debate the subject, but apparently can't come up with a strong point."
    show natsuki cross ml e4a b3b at t31
    n "F-Fine! I'll do it."
    $ nref()
    show natsuki cross happ cm oe at t42
    show sayori at t43
    show monika at t44
    y "I guess I will as well."
    y "It would look bad if I were the only member not participating."
    n "Wait, what about [player]?"
    n "He hasn't agreed to do this, either, you know!"
    m "I'm sure they won't mind something like this. Right, [player]?"
    mc "Wait... I never said I would {i}join{/i} this club!"
    mc "Sayori may have convinced me to stop by, but I still have other clubs to look at, and... um..."
    "I lose my train of thought."
    "All four girls stare at me with dejected eyes."
    m "B-But..."
    y "I'm sorry, I thought...."
    n "Hmph."
    s "[player]..."
    mc "Y-You all..."
    mc "...Right."
    mc "Okay, I've decided, then."
    mc "I'll join the Literature Club."
    "One by one, the girls' eyes light up."
    s "Yesss! I'm so happyyy~"
    "Monika stands in front of me."
    m "Then that makes it official!"
    m "Welcome to the Literature Club!"
    mc "Ah... thanks, I guess."
    m "Okay, everyone!"
    m "I think with that, we can officially end today's meeting on a good note."
    m "Everyone remember tonight's assignment:"
    m "Write a poem to bring to the next meeting, so we can all share!"
    "Monika looks at me once more."
    m "[player], I look forward to seeing how you express--"
    "But she goes silent."
    "It's almost immediately clear why:"
    "The classroom door just opened."
    "Everyone looks over to the door, where a {i}fifth{/i} girl now stands."
    
    pause