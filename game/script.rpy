label start:

    # This label configures the anticheat number for the game after Act 1.
    $ anticheat = persistent.anticheat

    # This variable sets the chapter number to 0 to use in the mod.
    $ chapter = 0

    # This variable controls whether the player can dismiss a pause in-game.
    $ _dismiss_pause = config.developer

    ## Names of the Characters
    $ s_name = "???"
    $ m_name = "Girl 3"
    $ n_name = "Girl 2"
    $ y_name = "Girl 1"
    $ r_name = "???"
    $ k_name = "???"

    # This variable controls whether the quick menu in the textbox is enabled.
    $ quick_menu = True

    # This variable c ontrols whether we want normal or glitched dialogue
    # For glitched dialogue, use 'style.edited'.
    $ style.say_dialogue = style.normal

    # This variable controls whether Sayori is dead. It is recommended to leave
    # this as-is.
    $ in_sayori_kill = None
    
    # These variables controls whether the player can skip dialogue or transitions.
    $ allow_skipping = True
    $ config.allow_skipping = True

    if persistent.playthrough == 0:

        call ch0_p1 from _call_ch0_p1

        call poem from _call_poem

        call ch0_p2 from _call_ch0_p2
        call poemresponse_start from _call_poemresponse_start
        call ch0_end from _call_ch0_end

    if persistent.playthrough == 1:
        $ chapter = 1 
        call ch1_p1 from _call_ch1_p1

        call poem from _call_poem_1

        call ch1_p2 from _call_ch1_p2
        
        call poem from _call_poem_2

        call ch1_p3 from _call_ch1_p3
        
        call poem from _call_poem_3

        call ch1_p4 from _call_ch1_p4

    #if persistent.playthrough == 2:
    #    $ chapter = 2
    #    call ch2_p1