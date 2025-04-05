label ch2_p1:
    #scene 2
    stop music fadeout .5
    scene bg residential_day
    with dissolve_scene_full
    "I step outside and am immediately greeted by an energetic second-year student."
    play music wn14
    show rikka 1u at t11
    $ r_name = "Rikka"
    r "Good morning, [player]."
    mc "Hello, Rikka."
    r 1a "How'd you sleep last night?"
    mc "Eh."
    r 1c "Are you still having trouble falling asleep?"
    "I just shrug."
    "Rikka's been walking to school with me for the past week or so."
    "Sayori has been sick at home, and she specifically requested we let her be while she recovers."
    "Because of this, Rikka has taken it upon herself to fill in for Sayori in a way."
    "Including trying to be my best friend, which obviously is a little different for Rikka than it is for Sayori."
    r 1a "Well, did you at least have time to eat breakfast this morning?"
    mc "Yep. I had some yogurt."
    r 1c "[player], yogurt by itself isn't breakfast."
    mc "Yes it is. I ate it to break my fast. Therefore, it is breakfast."
    r 1z "Whatever you say."
    show rikka at thide
    hide rikka
    "As soon as we start walking to school, I get a cold chill."
    "Rikka notices and gives me a concerned look."
    show rikka 1i at t11
    r "You okay?"
    mc "Y-Yeah..."
    mc "I just..."
    "For some reason, I look back at Sayori's house."
    "Something is telling me I should go check on her even though she's sick."
    r 1g "[player]...?"
    mc "...Just a second. I think I'm gonna..."
    "Rikka seems to determine what I'm saying despite trailing off."
    r "Hey, I'm sure she's doing alright. Why don't we let her rest?"
    mc "I just... feel like I need to go see her right now."
    r 1e "{i}sight{/i} If you really want to, go ahead."
    r 1p "I'll wait out here for you."
    "I nod and go up to Sayori's front door."
    show rikka at thide
    hide rikka
    scene bg house
    with dissolve_scene_full
    pause 1.0
    scene black
    with dissolve_scene_full
    stop music fadeout 3.0
    $ s_name = "Sayori"
    "I let myself in, knowing she keeps her door unlocked for some reason."
    "{i}I really need to say something about that once she's feeling better.{/i}"
    "I make my way up to her room and knock on her door."
    mc "Sayori? It's me."
    mc "You uh... feeling better?"
    "..."
    "I don't hear any response."
    mc "Sorry for... y'know, bothering you while you're recovering."
    mc "Just wanted to see how you're doing."
    s "You don't h-have to apologize, silly."
    "She almost sounds like she's close to tears, but her voice is partially muffled by the door being closed."
    mc "Hey, are you okay?"
    s "I'm... yeah, I'm doing okay."
    mc "Oh... Um..."
    mc "Can I come in...?"
    s "I'm changing right now."
    mc "Oh! Crap, um..."
    mc "I didn't mean to-"
    mc "Ah...."
    s "It's okay."
    mc "Sorry, I'll go now."
    "I start walking away before I hear a loud noise muffled by the closed door."
    s "No, no! Don't go. Please."
    mc "...?"
    s "I know you've got school and all that, but..."
    s "I... I wanna ask you a question, [player]."
    mc "O...kay. What's up?"
    s "...Was I a good friend to you?"
    mc "What kinda question is that?"
    s "Just answer. I'm curious."
    mc "..."
    mc "You're the best I could ask for."
    s "Really?"
    mc "Of course. Why would I lie to you?"
    s "To spare my hurt feelings?"
    s "I dunno... I felt like..."
    s "I've always felt like I should've been better."
    mc "Hey, I've felt the same way a bunch of times."
    mc "Am I a good friend to you?"
    s "...The best."
    mc "I mean, there was that time I ignored you for like a whole few years and... you know..."
    s "It's okay. I'd have ignored me, too."
    mc "Why? Because I can tell you, personally, the reasons I had were really stupid."
    s "What were they?"
    "I chuckle lightly to myself before responding."
    mc "Well... they don't matter anymore."
    mc "What matters is that I realized how much I was missing by ignoring you."
    mc "Your laugh, your smile..."
    mc "Your clumsiness."
    "I can hear Sayori give a weak laugh."
    mc "... I missed my best friend."
    mc "It took me all that time to realize how much you mean to me."
    mc "And now I can't imagine going a day without you."
    mc "I... I love you, Sayori."
    s "{i}I love you, [player].{/i}"
    s "..."
    "I hear Sayori start crying behind the door."
    mc "What's wrong, Sayori?"
    "She doesn't answer me."
    "After a moment, I hear a thud come from inside her room."
    mc "Sayori? Are you okay??"
    "There's no answer."
    "I try to open the door, but it's locked."
    "I'm about to try and-"
    r "How can you even see anything in here?"
    "I jump at the sound of Rikka's voice right next to me."
    mc "I thought you were outside??"
    r "I was, but you've been in here for several minutes."
    r "So I wanted to see what you were-"
    mc "Nevermind. Sayori isn't answering me anymore and I just heard some kind of noise come from her room."
    r "That sound came from in there?"
    r "I heard it while I was trying to climb up the stairs just now."
    r "..."
    "She knocks on Sayori's door gently before speaking."
    r "Sayori, you okay? There was a-"
    "She cuts herself off."
    "It takes me a second to realize why, but I can barely hear a sound almost like a drawn-out squeak."
    "Suddenly, Rikka starts frantically trying to turn the door handle."
    mc "Hey, hey, calm down a-"
    "She jabs me in the side with her elbow, instantly shutting me up."
    mc "I feel like... that was unnecessary..."
    r "{i}She has a rope in her room.{/i}"
    mc "Huh? Why would..."
    mc "... Wait, you're not really suggesting-"
    r "Move away from the door."
    "I've never heard Rikka's voice sound this desperate before."
    "I oblige and step out of the way."
    "I can make out Rikka's figure standing directly in front of the door before turning a shoulder towards it."
    "She waits a moment, as if bracing herself, before ramming her shoulder into the door."
    "It opens immediately."
    "I don't even have time to process where that strength came from before I hear Rikka's voice again."
    r "Sayori... Sayori..."
    "I finally enter the room as..."
    scene bg sayori_bedroom_dark
    with dissolve_scene_half 
    mc "... What...?"
    #play music gnbun
    "Rikka is trying to hoise Sayori up..."
    "Sayori, who is hanging from a noose and trying to push Rikka away."
    "I force myself to move and do my best to help Rikka."
    "Somehow, we manage to get Sayori out of and away from the noose in the middle of her room."
    "Sayori is laying on her bed, gasping for air."
    mc "Sayori..."
    mc "W-Why... why did you-"
    "Sayori shakes her head weakly."
    "She slowly raises one of her arms and tries to point at something on her desk."
    r "You want something from your desk?"
    "Sayori tries to nod again but doesn't manage more than slightly moving her head up."
    "Rikka goes over to Sayori's desk while I try to process everything that's happening."
    "My best friend just tried to end her own life..."
    "... And if I hadn't listened to my gut, she would likely be dead right now."
    "I look into Sayori's eyes. They aren't shining like I've always known them to."
    "They look clouded by something."
    "I'm startled by Rikka, who returns to Sayori's bedside holding a piece of paper."
    "I can't see it that well, but it looks like a poem."
    r "You want us to read it?"
    "Sayori manages to hold her hand out."
    r "Oh, you want to read it?"
    "Sayori hesitates but manages another small nod."
    "Rikka smiles and hands Sayori the poem."
    mc "Here, I'll turn the light on so you can see it clearly."
    "I turn towards the light switch in the room."
    "Before I can reach the switch, I hear a soft gushing sound behind me."
    r "{i}Sayori!!{/i}"
    #play music pcut
    "I turn back around and see a pool of blood oozing from cuts in Sayori's neck."
    "The paper in her hand is bloody at the edge."
    "Once again, I can't make myself move to help her."
    "Rikka tries to put pressure on the wounds, but Sayori moves the paper towards her opposite arm."
    r "{i}[player], help me!!{/i}"
    "I have to practically use as much force as possible to bring myself to her bedside again."
    "There's now several cuts along her arm."
    "I try to cover them up with my hands, but they're spaced out too far apart to cover them all."
    "Rikka uses her other hand to cover the remaining cuts on her arm."
    "I realize a second too late that Sayori is about to take advantage of this opening."
    "She drops the paper and uses all of her strength to push away the hand on her neck's wound."
    "Before I can grab the paper, Sayori takes it..."
    "... and forces it back into one of the cuts in her neck."
    "I can't handle watching anymore and shut my eyes."
    "I try my best not to throw up and take a deep breath before opening my eyes again."
    "... Rikka's holding the paper in her hand."
    "She's crying silently as Sayori attempts to take any kind of breath."
    "All we can do now is watch helplessly as my best friend takes one last attempt at a breath."
    "Then she goes still."
    scene black with dissolve_scene_full
    #stop music fadeout 3.0
    pause 3.0
    "ACT II - Other Reality"
    #scene 3
    $ m_name = "Monika"
    scene bg club_storm with dissolve_scene_full
    #play music clouds
    pause 1.0
    "I feel my phone buzz in my pocket."
    "I pull it out and check my notifications, seeing a message from [player]."
    
    "need to read more emr phone documentation :skull:"

    "As I put my phone back in my pocket, the door slides open."
    show monika forward happ cm ce at t11
    m "Good afternoon, [white]."
    w "Hello, Monika."
    w "How was your piano... session, or whatever you wanna call it?"
    show monika oe at t11
    m "If you're referring to {i}study hall{/i}, it went well."
    m "I'm getting pretty far along with the song I'm writing."
    w "Cool."
    show monika at thide
    hide monika
    w "By the way, [player] might be joining us today."
    w "Not that you'd be {i}interested{/i} in-"
    show monika forward lsur cm oe at t11
    m "Wait, really??"
    w "No, I'm going out of my way to lie to you and get your hopes up for absolutely no reason."
    show monika ce at t11
    "Monika seemingly ignores my sarcasm and smiles to herself for a moment."
    show monika ma at t11
    m "Sorry, it's just been a while since I've seen him, so uh..."
    w "Monika, it's perfectly normal to be excited about seeing him."
    w "Especially after not seeing him at all for this long."
    show monika e1a at t11
    m "I know... I just..."
    w "You don't have to justify everything, remember?"
    show monika forward nerv cm oe at t11
    m "Yeah... I'm working on- I mean, I remember."
    show monika e1a at t11
    m "Thanks for the reminder."
    w "No need to thank me. It's my job to look after my club members."
    show monika at thide 
    hide monika
    "The door opens again."
    $ k_name = "Kotonoha"
    $ y_name = "Yuri"
    show kotonoha 1a at t21
    show yuri turned happ cm oe at f22
    y "Hello, [white]. How has your day been so far?"
    show yuri at t22
    w "Pretty good. How about yourself?"
    show yuri at f22
    y "Oh, about the same."
    show yuri at t22
    show kotonoha at f21
    k "Same for me as well."
    k 1e "Although... [player] still seemed pretty distant during class today."
    show kotonoha at t21
    w "Well, he's going to try and come to today's meeting."
    show kotonoha 1w at f21
    show yuri turned lsur om oe at t22
    k "I-Is that so?"
    show kotonoha at t21
    show yuri turned happ cm oe at f22
    y "It will be great to see him again."
    show yuri turned flus me oe at f22
    y "I've been worrying about how he's holding up much more as of late."
    show yuri at t22
    w "Rikka says he's not... in horrible condition anymore, so there's that at least."
    w "But whenever he gets here, I'd advise giving him space unless he approaches you first."
    show kotonoha 1h at t21
    show yuri turned happ cm ce b1c at f22
    y "You're probably right. We wouldn't want-"
    $ n_name = "Natsuki"
    show kotonoha 1h at t43
    show yuri at t44
    show natsuki turned happ ce mo at f41
    n "Hello, everyone! I heard that {i}somebody{/i} is gonna be making a guest appearance today?"
    show kotonoha at thide
    show yuri at thide
    hide kotonoha
    hide yuri
    show natsuki at t11
    w "And who did you hear that from, exactly?"
    show natsuki oe at t11
    n "Rikka told me. She bumped into me during lunch."
    w "I see."
    w "You seem very excited about this information."
    w "I was almost expecting you to go full-on tsundere mode whenever you would've found out."
    show natsuki turned flus mb oe at t11
    n "Well... I decided not to."
    n "..."
    show natsuki cross flus ma oe blus at t11
    n "I missed him a lot."
    "... Huh."
    "For once, she's actually being vulnerable about this kind of thing."
    "Not like that's a bad thing, but... isn't that sort of..."
    "{i}Out of character?{/i}"
    "... The door opens again, but only enough for Rikka to poke her head through."
    show natsuki at thide
    hide natsuki
    r "[white], can you come here for a minute?"
    w "Sure?"
    scene bg corridor_storm with wipeleft_scene
    show rikka 1a at t21
    show mc 1a at t22 #REPLACE WITH EYEBAGS
    w "Hey, [player]. How you feeling?"
    show mc at f22
    mc "..."
    mc "Eh."
    show mc at t22
    w "... Well, it's nice to see you again."
    show mc at f22
    mc "You too."
    show mc 1h1 at f22
    mc "So... Before I go in, could you uh..."
    show mc 1a at f22
    mc "Could you ask everyone not to be super loud? My head's been hurting pretty much all day."
    show mc at t22
    w "Ah, is that why you were so short earlier?"
    show mc at f22
    mc "Mhm."
    show mc at t22
    show rikka 1c at f21
    r "You know we can head home if you want, right [player]?"
    show rikka at t21
    show mc 1h1 at f22
    mc "No. I... I want to be here."
    mc "I miss everyone."
    show mc at t22
    show rikka 1x at t21
    w "Well hey, feel free to come in whenever you're ready. I'll ask everyone to keep the volume down for you."
    show mc 1i1 at f22
    mc "Thanks."
    show mc at thide
    show rikka at thide
    hide mc
    hide rikka
    scene bg club_storm with wipeleft_scene
    #play music brokenclub
    w "Hey, everyone. [player] is gonna come in here in a minute."
    w "He has a headache, so can we keep the noise and volume down for him?"
    "The others nod in acknowledgment."
    "... Whenever you're ready."
    "..."
    "Once more, the door slides open."
    "Rikka enters, followed by [player]."
    show mc 1a at t11 #tired smile
    w "If you need to step out at any time, that's not a problem."
    show mc at f11
    mc "I appreciate it, but I should be fine."
    show mc at thide
    hide mc
    "I walk to my seat towards the back of the room and place my things down."
    "I know everyone probably wants to spend a little time with me today since I haven't been here in a while."
    "Even if I likely don't have enough energy to talk to everyone today, I at least want to talk to a couple of them."
    "... I'll hang out with Natsuki first. Besides, I think Kotonoha mentioned wanting to get to know her better once."
    "Maybe I could make up for my absence by helping her out with that sometime today?"
    "If I have the energy."
    mc "Hey, Nat."
    show natsuki turned shoc ce mc at t11
    n "[player]!!"
    show natsuki turned flus md oe blus at t11
    n "Er- sorry, didn't mean to get loud."
    mc "No worries."
    show natsuki turned neut me nobl at t11
    n "So..."
    show natsuki turned nerv cm e1a b1f at t11
    n "... How have you been?"
    mc "Could be better."
    show natsuki md at t11
    n "Well, yeah... I figured."
    n "I mean like..."
    show natsuki e1b at t11
    n "{i}sigh{/i} Sorry, you know I'm not good at this stuff."
    n "But I'm... I'm trying my best."
    "She takes a moment before figuring out what to say."
    show natsuki turned neut cm oe at t11
    n "How are you handling everything?"
    mc "..."
    mc "It still hurts."
    mc "I know I could've done more..."
    mc "I... I just let her-"
    show natsuki turned me b2a at t11
    n "Hey."
    n "Don't beat yourself up over it. It wasn't your fault."
    "Even though it kind of was, to an extent."
    n "She really cared about you, y'know."
    n "You were her favorite person in the world."
    show natsuki turned b2b ma at t11
    n "Don't forget that."
    show natsuki mn at t11
    n "I'll make sure you don't if I need to."
    mc "Thanks."
    show natsuki me at t11
    "She looks at me like she wants to say something else, but I really need to change the subject."
    mc "Oh, before I forget."
    mc "Just a second, Nat."
    show natsuki turned lsur me e1a b1c at t11
    n "Okay?"
    show natsuki at thide
    hide natsuki
    "I approach Kotonoha's desk and tap on it lightly."
    "She looks up and smiles brightly at me."
    show kotonoha 1a at t11
    k "Hey [player]!"
    mc "Yo."
    mc "You wanted to get to know Nat better, right?"
    show kotonoha 1e at t11
    k "Oh. Yeah, why do you ask?"
    mc "Have you gotten to do that yet?"
    k "Well, no, but you don't have to worry about that."
    "I do my best to ignore the chill that hits me."
    mc "I know. But I want to."
    "Kotonoha just stares for a few seconds, almost like she's looking through me."
    "I turn for a moment to see what she could be trying to look at."
    "Yuri is giving her a look I can't read from her desk."
    show kotonoha 1i at t11
    "Apparently Kotonoha can understand it, because she nods gently to Yuri before taking a deep breath."
    show kotonoha 1a at t11
    k "Alright."
    mc "Great. C'mon."
    show kotonoha at thide
    hide kotonoha
    "I return to Natsuki's desk with Kotonoha."
    show kotonoha 1a at t21
    show natsuki turned neut me at f22
    n "..."
    n "You wanted me to see Koto?"
    n "That's what you didn't want to forget?"
    show natsuki at t22
    mc "Well, you two don't really know each other that well yet, right?"
    show kotonoha 1s1 at t21
    n "Not really."
    mc "So..."
    show kotonoha at thide
    show natsuki at thide
    hide kotonoha
    hide natsuki
    "..."
    #pov switch mc to white
    "I write more ideas down on the paper in front of me."
    "Well, more of Rikka's ideas."
    "She's been coming up with things for the club to do beyond writing poems."
    "Given how slow she can write, I offered to record her ideas."
    show rikka 1c at t11
    r "Did I already bring up the cram session thing?"
    w "Yup."
    show rikka 1u at t11
    r "Great!"
    show rikka 1a at t11
    r "That's probably the thing I'm set on the most."
    r "With exams coming up-"
    w "- 'I want everyone to have a nice shot at getting a high score.'"
    pause 1.0
    #nice shot
    r "How many times did I say it?"
    w "Today? Once."
    w "Overall? I think I've counted about six."
    w "Now seven."
    show rikka 1v at t11
    "Rikka laughs before pulling out her phone."
    show rikka 1c at t11
    r "Oh, we have a few minutes before we need to leave."
    r "Should we go ahead and make our announcements?"
    w "That would probably be best."
    w "You can go sit with [player], I'll get everyone's attention."
    show rikka at srhide
    hide rikka
    "I quickly look over everything on the paper in front of me."
    "Cram session... blind book dates..."
    "... One poem each week (I'm sure that's you making up for that one poem game, though)..."
    "... Pretty sure those are the three ideas we both agreed are ideal."
    "{s}... And can you change the music? It's been playing ever since [player] got in here, let's get something new.{/s}"
    $ run_input("{s}Alright, alright.{/s}","")
    hide screen console_screen
    #play music warpednewnew
    "{s}... That works.{/s}"
    w "Alright, everyone."
    "I do my best not to yell for [player], and thankfully everyone hears me."
    "The room goes quiet in a few seconds."
    w "I want to make a couple of quick announcements before we dismiss for today."
    w "First, Rikka and I decided to change how we'll be writing poems for the club."
    w "Everyone will write one poem each week instead of every day."
    w "Hopefully, this puts less stress onto you all when writing."
    show yuri turned neut ma e1b b2a at t11
    y "It certainly will."
    show yuri at t21
    show kotonoha 1a at f22
    k "Yeah, I feel like some of us here would start to get burnt out if we had to write so many back to back."
    show natsuki turned neut cm oe at f31
    show yuri at t32
    show kotonoha at t33
    n "Honestly. I get being creative and all that, but one a week definitely sounds easier to manage."
    show natsuki at t31
    w "Great."
    w "The second announcement relates to end-of-term exams, which are coming up in about two weeks."
    show natsuki turned flus md at t31
    show kotonoha 1e at t33
    "Everyone's expressions change immediately upon hearing the word 'exams'."
    "Well, everyone except Yuri and Monika, which is to be expected."
    show kotonoha at thide
    hide kotonoha
    show monika forward happ cm ce at f33
    m "C'mon, guys. They're never as bad as you think they are."
    show natsuki e1a at f31
    show monika at t33
    n "So? There's no way I'm gonna be ready, whether it's hard or not!"
    show natsuki at t31
    show yuri at f32
    y "That's what she-"
    show yuri at thide
    hide yuri
    show rikka 1a at f32
    r "Don't worry, Natsuki. Everyone here will be ready before exams."
    r "We'll make sure of that."
    show monika forward neut om oe at f33
    show rikka at t32
    m "What do you mean?"
    show monika at t33
    show natsuki cross at f31
    n "Rikka, I swear if you're about to say what I'm thinking you're-"
    show natsuki at t31
    show rikka 1u at f32
    r "We're gonna hold a cram session two nights before exams."
    show rikka at t32
    "..."
    show natsuki turned angr oe cm at f31
    n "Heck no."
    show natsuki at t31
    show monika forward dist cm oe at t33
    show rikka 1g at f32
    r "Look, I know that no one here is {i}excited{/i} about exams."
    r "But the best way I've been able to retain information for a test has been studying quite a bit a day or two before."
    show rikka at t32
    w "Plus, this way we can do something as a club outside of a club meeting."
    n "..."
    show natsuki turned anno cm ce at f31
    n "Alright. I guess that makes sense."
    show natsuki at thide
    show rikka at thide
    show monika at thide
    hide natsuki
    hide rikka
    hide monika
    "Everyone else seems to agree, however reluctant they are to do so."
    "And with this announcement out of the way, Rikka and I dismiss the other members."
    show mc 1a at t11 #tired eyes
    mc "I'm kinda surprised the new guy didn't show up today."
    w "..."
    w "What new guy?"
    show mc 1f at t11
    mc "Rikka didn't tell you?"
    w "I'm gonna go with no?"
    show mc 1a at t11
    mc "Well, she told me that somebody approached her during one of her classes."
    mc "They were probably an exchange student, since they were speaking to her in, uh..."
    mc "... I forget how to pronounce it. That language people in America speak."
    w "{i}English??{/i}"
    show mc 1b at t11
    mc "That one."
    show mc 1a at t11
    mc "Am I really the only person here who has trouble saying it?"
    "... I'm not even going to try understanding the impact this joke has on everything."
    w "... Anyways, continue."
    mc "Oh, right."
    mc "They asked Rikka about the club and apparently seemed interested in joining."
    w "Huh. Okay then."
    w "Did Rikka get their name?"
    show mc 1u at t11
    mc "... If she told me what it was, I guess I already forgot."
    w "Eh, it's fine. I can text her later."
    w "I'm sure you wanna get going."
    show mc 1h1 at t11
    mc "Yeah."
    mc "I probably need to try and get some extra sleep."
    w "Well, I'm happy you could stop by, [player]."
    w "Come back whenever you want. No need to force yourself to be here if you want to go home right after school."
    show mc 1a at t11
    mc "Don't worry, I won't."
    mc "See you later, [white]."
    show mc at thide
    hide mc
    "[player] gets his things packed up as Rikka comes up to me."
    show rikka 1a at t11
    w "When were you going to tell me about the exchange student?"
    show rikka 1f at t11
    r "Oh, right!!"
    show rikka 1g at t11
    r "Sorry, I, uh... guess I forgot to bring it up."
    w "No need to apologize."
    w "I'll let you and [player] get going. Have a nice rest of your day."
    show rikka 1v at t11
    r "You too! See you tomorrow!"
    show rikka at thide
    hide rikka
    #music fades out
    "Rikka and [player] make their way out, leaving me to-"
    show monika forward nerv cm ce at t11
    m "Hey, [white], do you have a minute?"
    w "Oh, uh... sure."
    w "What did you need?"
    #music can i make it a double
    show monika forward neut e1b at t11
    m "... There's probably going to be a new member sometime this week."
    "{i}How many people already knew???{/i}"
    show monika e1a at t11
    m "And... we're not exactly on the best terms, to say the least."
    w "Are they an ex of yours or something?"
    show monika forward neut om ce at t11
    m "No, nothing like that."
    show monika oe cm at t11
    m "But... It's kind of a long story."
    w "Alright. Was there something you wanted me to do or say before they eventually join?"
    show monika e1b at t11
    m "Not really, I guess."
    w "You guess?"
    m "Well..."
    show monika oe at t11
    m "I know I often show my appreciation for this club and everyone in it."
    show monika forward flus ma oe at t11
    m "So I guess I wanted to give you a heads up that I might act... differently around them."
    w "Hey-"
    show monika cm at t11
    m "I know, I don't have to justify everything."
    w "... Well yes, but that's not what I was going to say."
    show monika forward neut om oe at t11
    w "If anything happens between you and... whoever the new guy is, just let me know."
    m "Oh..."
    show monika forward happ cm oe b1b at t11
    m "I really appreciate the offer..."
    w "C'mon, we're supposed to be out of here already."
    scene bg stairwell with wipeleft_scene
    #music fades out
    show monika forward neut cm oe at t11
    w "You brought an umbrella, right?"
    show monika forward lsur cm oe b1a at t11
    m "Oh, I left it back in the club room!"
    m "Is the room still unlocked?"
    w "Should be. Better hurry, though."
    show monika at srhide
    hide monika
    "Monika runs off towards the club room, leaving me standing by myself."
    "..."
    show vignette at vignettefade
    w "Okay, sorry. Just a moment."
    w "I don't think I ever had time to ask you something."
    #play music majorer deja vu
    w "Why did you let [player] see Sayori like that?"
    w "If you really wanted her to be gone at the start of this week..."
    w "You should've just had her hang herself without anyone seeing, like in the real game."
    w "But you let her use a piece of paper to slice her own neck open in front of [player]?"
    w "And there's another thing: Why were you so set on having Sayori kill herself right then?"
    w "You told {i}them{/i} you don't want full control over this project."
    w "So why are you going against that now?"
    $ run_input("... Give me a minute to address your questions.","")
    hide screen console_screen
    w "Okay, well hurry up. Monika won't take forever to grab her umbrella."
    w "Oh wait, that's right. You're at the point where you'll make her take as long as you need."
    "..."
    "....."
    w "You almost done?"
    pause 7.0
    w "Seriously, what's taking you-"
    $ show_poem(poem_t1, None,  False)
    w "... So you're basically just saying 'sorry not sorry?'"
    w "Fuck you too, I guess."
    "Please just trust me."
    "He doesn't want to do any real damage."
    "{nw}I promise I'll do what I can to make [player] happier."
    $ _history_list.pop()
    w "..."
    w "Get lost. Monika's nearly back."
    stop music fadeout 2.0
    pause 2.0
    show monika forward nerv cm ce n2 at t11
    m "Got it! Thanks for waiting for me."
    w "Not a problem."
    show monika at thide
    hide monika
    "Monika walks up to the main entrance and opens her umbrella."
    "I do the same, bracing myself for the wind and rain that await us."
    scene black with dissolve_scene_full
    pause 3.0
    #scene 4
    scene bg bedroom
    #play music okaerinasai
    "I set my backpack down by my desk."
    "My head still hurts, but it isn't as bad as it's been all day."
    "... Oh yeah. I still need to eat dinner."
    "Whatever, I can probably heat up some leftovers and then take care of my homework."
    "Then once all of that is taken care of, I can finally get to sleep."
    "I drag myself back down the stairs and into the kitchen."
    scene bg kitchen with dissolve_scene_half
    "I open my fridge-{nw}"
    scene black
    pause 5.0
    $ file_path = get_eighteen_path()
    if os.path.exists(file_path):
        python:
            os.remove(file_path)
    show screen fakeexception
    pause 3.0
    hide screen fakeexception
    #show scary koto lol
    #play music warped404
    #pause 7.0
    #stop music
    scene black
    pause 3.0

label eighteenexception:
    show text "Error: 'eighteen.txt' not found. It may be because you installed a corrupted version of the game. Please reinstall the program or locate 'eighteen.txt', and then try again."

    $ _skipping = False
    $ quick_menu = False
    $ preferences.afm_enable = False

    pause

    if os.path.exists(file_path):
        call ch2_p2
    else:
        jump eighteenexception

label ch2_p2:
    $ gs_name = "????"
    $ _skipping = True
    $ quick_menu = True
    $ preferences.afm_enable = True
    scene bg kitchen
    pause 5.0
    if os.path.exists(file_path):
        python:
            os.remove(file_path)
    "This is where you choose poem or study. WIP"
    #play sound tester-act2-1
    #menu:
    #    "Should I study for my exams, or start writing my poem for the week?"
    #    "Study":
    #        "I should probably do some of my homework and study."
    #        "I can hold off on my poem until tomorrow."
    #        call study
    #    "Poem":
    #        "I can probably get some of my poem written before I turn in for the night."
    #        "I'll have time to get all my work done tomorrow, anyways."
    #        call poem
    #if study == true:
    #   "That's probably enough studying for tonight."
    #elif:
    #   "I can probably stop here for tonight."
    scene bg bedroom
    "I really need to get some sleep now."
    "I throw myself down onto my bed and almost immediately fall asleep."
    "..."
    show tint at vignettefade
    "..."
    gs "[player]?"
    "..."
    gs "[player][player[-1] * 3]..."
    "..."
    gs "[player]!"
    "I quickly sit up in my bed."
    "... Did somebody just say my name...?"
    $ gs_name = "Sayori"
    show sayori turned lup rup happ om ce at h11
    gs "Yay! You're awake!"
    "I nearly jump out of my skin."
    "Sayori is standing at the foot of my bed... somehow..."
    show sayori turned oe at t11
    gs "I've missed you sooooo much!"
    show sayori turned sad oe ma ldown rdown at t11
    gs "I tried so many times to make myself visible to you, but it never worked."
    show sayori turned cm e1b at t11
    gs "... I almost gave up and accepted that I just... couldn't be a ghost."
    "..."
    "I have finally lost it."
    mc "How... how am I seeing..."
    mc "How are you even..."
    show sayori turned oe ma at t11
    mc "You've been gone for weeks now..."
    mc "I saw you..."
    mc "..."
    gs "I'm so sorry you had to see me like that, [player]."
    show sayori turned cm at t11
    gs "I didn't want to die, really. But the rain clouds... that voice in my head..."
    gs "I couldn't take it anymore."
    show sayori turned e1b at t11
    gs "..."
    gs "I wish I could take it back."
    gs "I miss talking to everyone."
    gs "I miss my parents, my family, my friends."
    show sayori turned e1g at t11
    gs "And I miss you."
    gs "I... I've hurt you so many times..."
    gs "I..."
    show sayori at thide
    hide sayori
    "... Her arms go right through me in what I assume is her attempt at a hug."
    "I guess she isn't able to physically interact with me, since she's... a ghost? I think?"
    "As soon as she realizes this, she completely breaks down."
    "... I barely even believe what's happening right now."
    "Am I still sleeping? Is this some kind of dream?"
    "Or is this real?"
    "And if it is, how am I even supposed to comfort her??"
    "..."
    stop music
    mc "Sayori?"
    "She looks up at me, her eyes glistening with tears."
    mc "I really wish I knew what to say to help you feel better..."
    mc "But all I really know what to say is that you were an amazing friend."
    gs "No I wasn't."
    mc "Hey, don't let the voice in your head-"
    gs "This isn't the voice speaking, [player]."
    gs "I... I really need to tell you something."
    mc "You don't have to try and justify any points in time where you thought you hurt me."
    gs "Please, just listen to me."
    mc "Sayori-"
    show sayori turned angr om e1g at t11
    gs "Just listen to me, [player]!"
    gs "Every time someone tries to talk to you like this..."
    gs "You ignore the most obvious signs known to literally anyone!"
    gs "You're one of the most dense people ever created..."
    show sayori turned cm at t11
    gs "I'm sorry if I sound mean, but I need you to listen to what I have to say."
    mc "..."
    mc "......"
    mc "... Go ahead, then."
    show sayori turned anno cm oe at t11
    gs "Thank you."
    show sayori turned ce at t11
    pause 1.0
    show sayori turned neut oe at t11
    gs "This is going to sound really weird, but I need you to trust me."
    gs "... This isn't the first time we've lived out this point in time."
    show sayori turned curi cm ce at t11
    gs "Er, wait. That's not how I wanted to word it..."
    gs "But it still works, I guess..."
    mc "What do you mean by-"
    show sayori turned anno cm oe at t11
    gs "[player], can you actually {i}think{/i} about what I just said before asking 'what do you mean'?"
    "I've never seen Sayori act like this before."
    "But if I've really lost my last bit of sanity, then I guess there's no harm in humoring whatever she's going on about."
    mc "You mean like... we've lived out the past few weeks... before now?"
    show sayori turned neut om oe at t11
    gs "Oh. You actually got it."
    gs "Good job."
    show sayori turned cm at t11
    #play music deeper breaths
    gs "Yes. This is... one of the many, {i}many{/i} times that we've gone through all of this."
    gs "The festival, my death, weeks {i}following{/i} the festival..."
    gs "And there's hundreds of people behind the number of versions of this world."
    show sayori turned e1b at t11
    gs "Some versions were created by people named 12gizguy, guybread, SpiritH0F..."
    gs "And then there's versions that have been designed by entire {i}teams{/i}."
    gs "The only ones I can remember right now are Team Relations and Perfect Fifth, but I think you get my point."
    mc "This is... a lot to take in..."
    "How did the tone change this quickly??"
    show sayori turned oe at t11
    gs "I can tell what you're thinking."
    gs "I was just crying a minute ago, and now I'm dropping information on you that sounds pretty weird."
    mc "Yeah..."
    show sayori turned anno cm oe at t11
    gs "Almost as if someone is writing this moment specifically so that all of this info is properly established."
    mc "So by your logic, this is yet another version of our world..."
    mc "Being written by some guy who really wants to focus on this topic?"
    show sayori turned ce at t11
    gs "And apparently, they can't write for shit, because everything feels way too rushed."
    gs "Not to mention, I'd never cuss as randomly as I did just now."
    show sayori turned angr oe at t11
    mc "So then... who's in charge of, uh... making this version of our world?"
    gs "I'd love to tell you, if I could actually tell who it is."
    gs "Apparently, since this version is still technically being created, I can't see who's making it."
    mc "... I guess that's convenient for them?"
    mc "Sorry, I'm still having a really hard time understanding everything."
    show sayori turned ce at t11
    gs "Well... I guess it wouldn't hurt to just show you what I'm talking about."
    gs "Please tell me this isn't the one version of this world where you get motion sick easily."
    mc "I don't. Never have."
    show sayori turned e1b at t11
    gs "Good. Then let's get this over with."
    "I open my mouth to ask what she means, but I suddenly feel myself being propelled forward."
    #stop music
    scene black
    with dissolve_scene_half
    "My room disappears instantly, everything being replaced by total darkness."