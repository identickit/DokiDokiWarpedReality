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

