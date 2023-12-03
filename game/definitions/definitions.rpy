## definitions.rpy

# This file defines important stuff for DDLC and your mod!

# This variable declares if the mod is a demo or not.
# Leftover from DDLC.
define persistent.demo = False

# This variable declares whether the mod is in the 'steamapps' folder.
define persistent.steam = ("steamapps" in config.basedir.lower())

# This variable declares whether Developer Mode is on or off in the mod.
define config.developer = False

# This python statement starts singleton to make sure only one copy of the mod
# is running.
python early:
    import singleton
    me = singleton.SingleInstance()

init -3 python:
    ## Dynamic Super Position (DSP)
    # DSP is a feature in where the game upscales the positions of assets 
    # with higher resolutions (1080p).
    # This is just simple division from Adobe, implemented in Python.
    def dsp(orig_val):
        ceil = not isinstance(orig_val, float)
        dsp_scale = config.screen_width / 1280.0 
        if ceil: return math.ceil(orig_val * dsp_scale)
        # since `absolute * float` -> `float`
        # we wanna keep the same type
        return type(orig_val)(orig_val * dsp_scale)
    
    # This makes evaluating the value faster
    renpy.pure(dsp)

    ## Dynamic Super Resolution
    # DSR is a feature in where the game upscales asset sizes to higher
    # resolutions (1080p) and sends back a modified transform.
    # (Recommend that you just make higher res assets than upscale lower res ones)
    def dsr(path):
        img_bounds = renpy.image_size(path)
        return Transform(path, size=(dsp(img_bounds[0]), dsp(img_bounds[1])))

## Android Gestures (provided by Tulkas)
## These gestures allow players to access different settings using the touch screen.
# Swipe Up - Saves
# Swipe Down - Hide Dialogue Box
# Swipe Left - History
# Swipe Right - Skip Dialogue
define config.gestures = { "n" : 'game_menu', "s" : "hide_windows", "e" : 'toggle_skip', "w" : "history" }

# This init python statement sets up the functions, keymaps and channels
# for the game.
init python:
    ## More Android Gestures
    # This variable makes a keymap for the history screen.
    if renpy.android:
        config.underlay.append(renpy.Keymap(history = ShowMenu("history"))) 

        # These commented variables sets all keybinds from Rollback to History.
        # config.keymap["rollback"] = []
        # config.keymap["history"] = [ 'K_PAGEUP', 'repeat_K_PAGEUP', 'K_AC_BACK', 'mousedown_4' ]
    
    # These variable declarations adjusts the mapping for certain actions in-game.
    config.keymap['game_menu'].remove('mouseup_3')
    config.keymap['hide_windows'].append('mouseup_3')
    config.keymap['self_voicing'] = []
    config.keymap['clipboard_voicing'] = []
    config.keymap['toggle_skip'] = []

    # This variable declaration registers the music poem channel for the poem sharing music.
    renpy.music.register_channel("music_poem", mixer="music", tight=True)
    
    # This function gets the postition of the music playing in a given channel.
    def get_pos(channel='music'):
        pos = renpy.music.get_pos(channel=channel)
        if pos: return pos
        return 0

    # This function deletes all the saves made in the mod.
    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)

    # This function deletes a given character name from the characters folder.
    def delete_character(name):
        if renpy.android:
            try: os.remove(os.environ['ANDROID_PUBLIC'] + "/characters/" + name + ".chr")
            except: pass
        else:
            try: os.remove(config.basedir + "/characters/" + name + ".chr")
            except: pass

    # These functions restores all the character CHR files to the characters folder 
    # given the playthrough number in the mod and list of characters to restore.
    def restore_character(names):
        if not isinstance(names, list):
            raise Exception("'names' parameter must be a list. Example: [\"monika\", \"sayori\"].")

        for x in names:
            if renpy.android:
                try: renpy.file(os.environ['ANDROID_PUBLIC'] + "/characters/" + x + ".chr")
                except: open(os.environ['ANDROID_PUBLIC'] + "/characters/" + x + ".chr", "wb").write(renpy.file("chrs/" + x + ".chr").read())
            else:
                try: renpy.file(config.basedir + "/characters/monika.chr")
                except: open(config.basedir + "/characters/monika.chr", "wb").write(renpy.file("chrs/monika.chr").read())
                try: renpy.file(config.basedir + "/characters/sayori.chr")
                except: open(config.basedir + "/characters/sayori.chr", "wb").write(renpy.file("chrs/sayori.chr").read())
                try: renpy.file(config.basedir + "/characters/natsuki.chr")
                except: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("chrs/natsuki.chr").read())
                try: renpy.file(config.basedir + "/characters/yuri.chr")
                except: open(config.basedir + "/characters/yuri.chr", "wb").write(renpy.file("chrs/yuri.chr").read())
                try: renpy.file(config.basedir + "/characters/kotonoha.chr")
                except: open(config.basedir + "/characters/kotonoha.chr", "wb").write(renpy.file("mod_assets/kotonoha.chr").read())
                try: renpy.file(config.basedir + "/characters/rikka.chr")
                except: open(config.basedir + "/characters/rikka.chr", "wb").write(renpy.file("mod_assets/rikka.chr").read())
                try: renpy.file(config.basedir + "/characters/white.chr")
                except: open(config.basedir + "/characters/white.chr", "wb").write(renpy.file("mod_assets/white.chr").read())

    def restore_all_characters():
        if persistent.playthrough == 0:
            restore_character(["monika", "sayori", "natsuki", "yuri", "kotonoha", "rikka"])
        elif persistent.playthrough == 1:
            restore_character(["monika", "sayori", "natsuki", "yuri", "kotonoha", "rikka", "white"])
        elif persistent.playthrough == 2:
            restore_character(["monika", "natsuki", "yuri", "kotonoha", "rikka", "white"])
        elif persistent.playthrough == 20:
            restore_character(["monika", "sayori", "natsuki", "yuri", "kotonoha", "rikka"])
        else:
            restore_character(["sayori", "natsuki", "yuri"])
    
    # This function is obsolete as all characters now restores only
    # relevant characters to the characters folder.
    def restore_relevant_characters():
        restore_all_characters()

    # This function pauses the time for a certain amount of time or indefinite.
    def pause(time=None):
        global _windows_hidden

        if not time:
            _windows_hidden = True
            renpy.ui.saybehavior(afm=" ")
            renpy.ui.interact(mouse='pause', type='pause', roll_forward=None)
            _windows_hidden = False
            return
        if time <= 0: return
        _windows_hidden = True
        renpy.pause(time)
        _windows_hidden = False

    def ran(trans, st, at):
        if st >= renpy.random.random():
            return None
        else:
            return 0

## Music
define audio.t1 = "<loop 22.073>bgm/1.ogg" # Doki Doki Literature Club! - Main Theme
define audio.t2 = "<loop 4.499>bgm/2.ogg" # Ohayou Sayori! - Sayori Theme
define audio.t2g = "bgm/2g.ogg"
define audio.t2g2 = "<from 4.499 loop 4.499>bgm/2.ogg"
define audio.t2g3 = "<loop 4.492>bgm/2g2.ogg"
define audio.t3 = "<loop 4.618>bgm/3.ogg" # Main Theme - In Game 
define audio.t3g = "<to 15.255>bgm/3g.ogg"
define audio.t3g2 = "<from 15.255 loop 4.618>bgm/3.ogg"
define audio.t3g3 = "<loop 4.618>bgm/3g2.ogg"
define audio.t3m = "<loop 4.618>bgm/3.ogg"
define audio.t4 = "<loop 19.451>bgm/4.ogg" # Dreams of Love and Literature - Poem Game Theme
define audio.t4g = "<loop 1.000>bgm/4g.ogg"
define audio.t5 = "<loop 4.444>bgm/5.ogg" # Okay Everyone! - Sharing Poems Theme
define audio.wn3 = "mod_assets/bgm/warpedaltthree.ogg" # Truly Broken Club
define audio.tb = "mod_assets/bgm/warpednewfour.ogg" # The Break
define audio.wn6 = "mod_assets/bgm/warpednewsix.ogg" # Her Theme
define audio.wn7 = "mod_assets/bgm/warpednewseven.ogg" # Her Theme (Variant)
define audio.wn8 = "mod_assets/bgm/warpedneweight.ogg" # Her Theme (Variant 2)
define audio.wn9 = "mod_assets/bgm/warpednewnine.ogg" # Broken Club!
define audio.wn10 = "mod_assets/bgm/warpednewten.ogg" # Major Deja Vu
define audio.wn11 = "mod_assets/bgm/warpedneweleven.ogg" # Emerald & Silver
define audio.wn12 = "mod_assets/bgm/warpednewtwelve.ogg" # Silver & Emerald
define audio.wn13 = "mod_assets/bgm/warpednewthirteen.ogg" # White Salvation
define audio.wnw = "mod_assets/bgm/yuri-wrongopt.ogg" # Yuri-WrongOPT
define audio.wnf = "mod_assets/bgm/nat-silverforce.ogg" # Natsuki

define audio.tmonika = "<loop 4.444>bgm/5_monika.ogg" # Okay Everyone! (Monika)
define audio.tsayori = "<loop 4.444>bgm/5_sayori.ogg" # Okay Everyone! (Sayori)
define audio.tnatsuki = "<loop 4.444>bgm/5_natsuki.ogg" # Okay Everyone! (Natsuki)
define audio.tyuri = "<loop 4.444>bgm/5_yuri.ogg" # Okay Everyone! (Yuri)
define audio.trikka = "<loop 11.1515>mod_assets/bgm/club_orange.ogg" # Okay Everyone! (Rikka)
define audio.twhite = "mod_assets/bgm/club_white.ogg" # Okay Everyone! (White) 

define audio.t5b = "<loop 4.444>bgm/5.ogg"
define audio.t5c = "<loop 4.444>bgm/5.ogg"
define audio.t6 = "<loop 10.893>bgm/6.ogg" # Play With Me - Yuri/Natsuki Theme
define audio.t6g = "<loop 10.893>bgm/6g.ogg"
define audio.t6r = "<to 39.817 loop 0>bgm/6r.ogg"
define audio.t6s = "<loop 43.572>bgm/6s.ogg"
define audio.t7 = "<loop 2.291>bgm/7.ogg" # Poem Panic - Argument Theme
define audio.t7a = "<loop 4.316 to 12.453>bgm/7.ogg"
define audio.t7g = "<loop 31.880>bgm/7g.ogg"
define audio.t8 = "<loop 9.938>bgm/8.ogg" # Daijoubu! - Argument Resolved Theme
define audio.t9 = "<loop 3.172>bgm/9.ogg" # My Feelings - Emotional Theme
define audio.t9g = "<loop 1.532>bgm/9g.ogg" # My Feelings but 207% Speed
define audio.t10 = "<loop 5.861>bgm/10.ogg" # My Confession - Sayori Confession Theme
define audio.t10y = "<loop 0>bgm/10-yuri.ogg"
define audio.td = "<loop 36.782>bgm/d.ogg"

define audio.m1 = "<loop 0>bgm/m1.ogg" # Just Monika. - Just Monika.
define audio.mend = "<loop 6.424>bgm/monika-end.ogg" # I Still Love You - Monika Post-Delete Theme

define audio.ghostmenu = "<loop 0>bgm/ghostmenu.ogg"
define audio.g1 = "<loop 0>bgm/g1.ogg"
define audio.g2 = "<loop 0>bgm/g2.ogg"
define audio.hb = "<loop 0>bgm/heartbeat.ogg"

define audio.closet_open = "sfx/closet-open.ogg"
define audio.closet_close = "sfx/closet-close.ogg"
define audio.page_turn = "sfx/pageflip.ogg"
define audio.fall = "sfx/fall.ogg"
define audio.do1 = "mod_assets/sfx/do1.mp3"
define audio.wa1 = "mod_assets/sfx/warpedaltone.ogg"
define audio.wa2 = "mod_assets/sfx/warpedalttwo.ogg"
define audio.wlf = "mod_assets/sfx/leftstep.ogg"
define audio.wrf = "mod_assets/sfx/rightstep.ogg"
define audio.wsl = "mod_assets/sfx/slam.ogg"
define audio.wsn = "mod_assets/sfx/snap.ogg"
define audio.wsc = "mod_assets/sfx/scrape.ogg"

## Backgrounds 
image black = "#000000"
image dark = "#000000e4"
image darkred = "#110000c8"
image white = "#ffffff"
image splash = "bg/splash.png"
image end:
    truecenter
    "gui/end.png"

image bg residential_day = "bg/residential.png" # Start of DDLC BG
image bg class_day = "bg/class.png" # The classroom BG
image bg corridor = "bg/corridor.png" # The hallway BG
image bg club_day = "bg/club.png" # The club BG
image bg club_night = "mod_assets/bg/clubnight.png"
image bg club_day2: # Glitched Club BG
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg/club-skill.png"

image bg closet = "bg/closet.png" # The closet BG
image bg bedroom = "bg/bedroom.png" # MC's Room BG
image bg sayori_bedroom = "bg/sayori_bedroom.png" # Sayori's Room BG
image bg house = "bg/house.png" # Sayori's House BG
image bg kitchen = "bg/kitchen.png" # MC's Kitchen BG
image bg qgsayori_bedroom:
    "mod_assets/bg/sayori_bedroomg1.png"
    pause 0.08
    "mod_assets/bg/sayori_bedroomg2.png"
    pause 0.12
    "mod_assets/bg/sayori_bedroomg3.png"
    pause 0.12
    "bg/sayori_bedroom.png"

image bg notebook = "bg/notebook.png" # Poem Game Notebook Scene
image bg notebook-glitch = "bg/notebook-glitch.png" # Glitched Poem Game BG

image bg clubdayg1 = "mod_assets/bg/clubdayg1.png"
image bg clubdayg2 = "mod_assets/bg/clubdayg2.png"
image bg clubdayg3 = "mod_assets/bg/clubdayg3.png"
image bg clubdayg4 = "mod_assets/bg/clubdayg4.png"
image bg clubdaypause = "mod_assets/bg/clubdaypause.png"
image bg qgclubday:
    "mod_assets/bg/clubdayg4.png"
    pause 0.12
    "mod_assets/bg/clubdayg3.png"
    pause 0.12
    "bg/club.png"
image bg clubdayg:
    "mod_assets/bg/clubdayg1.png"
    function ran
    pause 0.05
    "mod_assets/bg/clubdayg2.png"
    function ran
    pause 0.05
    "mod_assets/bg/clubdayg3.png"
    function ran
    pause 0.05
    "mod_assets/bg/clubdayg4.png"
    function ran
    pause 0.05
    repeat
image bg residential_dayg1 = "mod_assets/bg/residentialg1.png"
image bg residential_dayg2 = "mod_assets/bg/residentialg2.png"
image bg qgresidential_day:
    "mod_assets/bg/residentialg1.png"
    pause 0.12
    "mod_assets/bg/residentialg2.png"
    pause 0.12
    "bg/residential.png"
image bg bsod = "mod_assets/bg/bsod.png"
label kotog:
    show m_rectstatic
    show layer master:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
    show layer screens:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
    show noise onlayer front:
        alpha 0.3
        easeout 0.35 alpha 0

# This image shows a glitched screen during Act 2 poem sharing with Yuri.
image bg glitch = LiveTile("bg/glitch.jpg")

# This image transform shows a glitched scene effect
# during Act 3 when we delete Monika.
image glitch_color:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.7
        linear 0.45 alpha 0

# This image transform shows another glitched scene effect
# during Act 3 when we delete Monika.
image glitch_color2:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.7
        linear 0.45 alpha 0

# Characters
# This is where the characters bodies and faces are defined in the mod.
# They are defined by a left half, a right half and their head.
# To define a new image, declare a new image statement like in this example:
#     image sayori 1ca = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1cl.png", (0, 0), "mod_assets/sayori/1cr.png", (0, 0), "sayori/a.png")

# Sayori's Character Definitions
image sayori 1 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 1a = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 1b = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/b.png")
image sayori 1c = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/c.png")
image sayori 1d = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/d.png")
image sayori 1e = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/e.png")
image sayori 1f = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/f.png")
image sayori 1g = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/g.png")
image sayori 1h = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/h.png")
image sayori 1i = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/i.png")
image sayori 1j = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/j.png")
image sayori 1k = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/k.png")
image sayori 1l = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/l.png")
image sayori 1m = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/m.png")
image sayori 1n = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/n.png")
image sayori 1o = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/o.png")
image sayori 1p = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/p.png")
image sayori 1q = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/q.png")
image sayori 1r = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/r.png")
image sayori 1s = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/s.png")
image sayori 1t = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/t.png")
image sayori 1u = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/u.png")
image sayori 1v = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/v.png")
image sayori 1w = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/w.png")
image sayori 1x = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/x.png")
image sayori 1y = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/y.png")

image sayori 2 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 2a = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 2b = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/b.png")
image sayori 2c = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/c.png")
image sayori 2d = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/d.png")
image sayori 2e = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/e.png")
image sayori 2f = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/f.png")
image sayori 2g = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/g.png")
image sayori 2h = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/h.png")
image sayori 2i = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/i.png")
image sayori 2j = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/j.png")
image sayori 2k = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/k.png")
image sayori 2l = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/l.png")
image sayori 2m = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/m.png")
image sayori 2n = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/n.png")
image sayori 2o = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/o.png")
image sayori 2p = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/p.png")
image sayori 2q = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/q.png")
image sayori 2r = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/r.png")
image sayori 2s = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/s.png")
image sayori 2t = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/t.png")
image sayori 2u = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/u.png")
image sayori 2v = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/v.png")
image sayori 2w = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/w.png")
image sayori 2x = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/x.png")
image sayori 2y = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/y.png")

image sayori 3 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 3a = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 3b = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/b.png")
image sayori 3c = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/c.png")
image sayori 3d = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/d.png")
image sayori 3e = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/e.png")
image sayori 3f = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/f.png")
image sayori 3g = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/g.png")
image sayori 3h = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/h.png")
image sayori 3i = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/i.png")
image sayori 3j = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/j.png")
image sayori 3k = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/k.png")
image sayori 3l = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/l.png")
image sayori 3m = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/m.png")
image sayori 3n = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/n.png")
image sayori 3o = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/o.png")
image sayori 3p = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/p.png")
image sayori 3q = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/q.png")
image sayori 3r = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/r.png")
image sayori 3s = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/s.png")
image sayori 3t = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/t.png")
image sayori 3u = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/u.png")
image sayori 3v = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/v.png")
image sayori 3w = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/w.png")
image sayori 3x = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/x.png")
image sayori 3y = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/y.png")

image sayori 4 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 4a = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 4b = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/b.png")
image sayori 4c = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/c.png")
image sayori 4d = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/d.png")
image sayori 4e = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/e.png")
image sayori 4f = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/f.png")
image sayori 4g = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/g.png")
image sayori 4h = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/h.png")
image sayori 4i = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/i.png")
image sayori 4j = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/j.png")
image sayori 4k = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/k.png")
image sayori 4l = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/l.png")
image sayori 4m = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/m.png")
image sayori 4n = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/n.png")
image sayori 4o = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/o.png")
image sayori 4p = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/p.png")
image sayori 4q = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/q.png")
image sayori 4r = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/r.png")
image sayori 4s = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/s.png")
image sayori 4t = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/t.png")
image sayori 4u = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/u.png")
image sayori 4v = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/v.png")
image sayori 4w = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/w.png")
image sayori 4x = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/x.png")
image sayori 4y = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/y.png")

image sayori 5 = im.Composite((960, 960), (0, 0), "sayori/3a.png")
image sayori 5a = im.Composite((960, 960), (0, 0), "sayori/3a.png")
image sayori 5b = im.Composite((960, 960), (0, 0), "sayori/3b.png")
image sayori 5c = im.Composite((960, 960), (0, 0), "sayori/3c.png")
image sayori 5d = im.Composite((960, 960), (0, 0), "sayori/3d.png")

# Sayori in her Casual Outfit [Day 4]
image sayori 1ba = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png")
image sayori 1bb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png")
image sayori 1bc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png")
image sayori 1bd = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png")
image sayori 1be = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png")
image sayori 1bf = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png")
image sayori 1bg = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png")
image sayori 1bh = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png")
image sayori 1bi = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png")
image sayori 1bj = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png")
image sayori 1bk = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png")
image sayori 1bl = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png")
image sayori 1bm = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png")
image sayori 1bn = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png")
image sayori 1bo = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png")
image sayori 1bp = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png")
image sayori 1bq = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png")
image sayori 1br = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png")
image sayori 1bs = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png")
image sayori 1bt = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png")
image sayori 1bu = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png")
image sayori 1bv = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png")
image sayori 1bw = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png")
image sayori 1bx = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png")
image sayori 1by = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png")

image sayori 2ba = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png")
image sayori 2bb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png")
image sayori 2bc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png")
image sayori 2bd = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png")
image sayori 2be = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png")
image sayori 2bf = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png")
image sayori 2bg = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png")
image sayori 2bh = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png")
image sayori 2bi = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png")
image sayori 2bj = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png")
image sayori 2bk = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png")
image sayori 2bl = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png")
image sayori 2bm = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png")
image sayori 2bn = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png")
image sayori 2bo = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png")
image sayori 2bp = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png")
image sayori 2bq = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png")
image sayori 2br = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png")
image sayori 2bs = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png")
image sayori 2bt = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png")
image sayori 2bu = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png")
image sayori 2bv = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png")
image sayori 2bw = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png")
image sayori 2bx = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png")
image sayori 2by = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png")

image sayori 3ba = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png")
image sayori 3bb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png")
image sayori 3bc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png")
image sayori 3bd = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png")
image sayori 3be = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png")
image sayori 3bf = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png")
image sayori 3bg = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png")
image sayori 3bh = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png")
image sayori 3bi = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png")
image sayori 3bj = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png")
image sayori 3bk = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png")
image sayori 3bl = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png")
image sayori 3bm = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png")
image sayori 3bn = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png")
image sayori 3bo = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png")
image sayori 3bp = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png")
image sayori 3bq = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png")
image sayori 3br = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png")
image sayori 3bs = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png")
image sayori 3bt = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png")
image sayori 3bu = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png")
image sayori 3bv = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png")
image sayori 3bw = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png")
image sayori 3bx = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png")
image sayori 3by = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png")

image sayori 4ba = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png")
image sayori 4bb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png")
image sayori 4bc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png")
image sayori 4bd = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png")
image sayori 4be = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png")
image sayori 4bf = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png")
image sayori 4bg = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png")
image sayori 4bh = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png")
image sayori 4bi = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png")
image sayori 4bj = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png")
image sayori 4bk = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png")
image sayori 4bl = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png")
image sayori 4bm = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png")
image sayori 4bn = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png")
image sayori 4bo = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png")
image sayori 4bp = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png")
image sayori 4bq = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png")
image sayori 4br = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png")
image sayori 4bs = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png")
image sayori 4bt = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png")
image sayori 4bu = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png")
image sayori 4bv = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png")
image sayori 4bw = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png")
image sayori 4bx = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png")
image sayori 4by = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png")

# This image shows a glitched Sayori sprite during Act 2.
image sayori glitch:
    "sayori/glitch1.png"
    pause 0.01666
    "sayori/glitch2.png"
    pause 0.01666
    repeat

# Natsuki's Character Definitions
image natsuki 11 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 1a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/a.png")
image natsuki 1b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/b.png")
image natsuki 1c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/c.png")
image natsuki 1d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/d.png")
image natsuki 1e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/e.png")
image natsuki 1f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/f.png")
image natsuki 1g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/g.png")
image natsuki 1h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/h.png")
image natsuki 1i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/i.png")
image natsuki 1j = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/j.png")
image natsuki 1k = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/k.png")
image natsuki 1l = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/l.png")
image natsuki 1m = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/m.png")
image natsuki 1n = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/n.png")
image natsuki 1o = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/o.png")
image natsuki 1p = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/p.png")
image natsuki 1q = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/q.png")
image natsuki 1r = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/r.png")
image natsuki 1s = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/s.png")
image natsuki 1t = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/t.png")
image natsuki 1u = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/u.png")
image natsuki 1v = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/v.png")
image natsuki 1w = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/w.png")
image natsuki 1x = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/x.png")
image natsuki 1y = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/y.png")
image natsuki 1z = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/z.png")

image natsuki 21 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 2a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/a.png")
image natsuki 2b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/b.png")
image natsuki 2c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/c.png")
image natsuki 2d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/d.png")
image natsuki 2e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/e.png")
image natsuki 2f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/f.png")
image natsuki 2g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/g.png")
image natsuki 2h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/h.png")
image natsuki 2i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/i.png")
image natsuki 2j = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/j.png")
image natsuki 2k = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/k.png")
image natsuki 2l = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/l.png")
image natsuki 2m = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/m.png")
image natsuki 2n = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/n.png")
image natsuki 2o = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/o.png")
image natsuki 2p = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/p.png")
image natsuki 2q = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/q.png")
image natsuki 2r = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/r.png")
image natsuki 2s = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/s.png")
image natsuki 2t = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/t.png")
image natsuki 2u = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/u.png")
image natsuki 2v = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/v.png")
image natsuki 2w = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/w.png")
image natsuki 2x = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/x.png")
image natsuki 2y = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/y.png")
image natsuki 2z = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/z.png")

image natsuki 31 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 3a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/a.png")
image natsuki 3b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/b.png")
image natsuki 3c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/c.png")
image natsuki 3d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/d.png")
image natsuki 3e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/e.png")
image natsuki 3f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/f.png")
image natsuki 3g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/g.png")
image natsuki 3h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/h.png")
image natsuki 3i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/i.png")
image natsuki 3j = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/j.png")
image natsuki 3k = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/k.png")
image natsuki 3l = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/l.png")
image natsuki 3m = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/m.png")
image natsuki 3n = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/n.png")
image natsuki 3o = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/o.png")
image natsuki 3p = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/p.png")
image natsuki 3q = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/q.png")
image natsuki 3r = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/r.png")
image natsuki 3s = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/s.png")
image natsuki 3t = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/t.png")
image natsuki 3u = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/u.png")
image natsuki 3v = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/v.png")
image natsuki 3w = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/w.png")
image natsuki 3x = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/x.png")
image natsuki 3y = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/y.png")
image natsuki 3z = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/z.png")

image natsuki 41 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 4a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/a.png")
image natsuki 4b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/b.png")
image natsuki 4c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/c.png")
image natsuki 4d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/d.png")
image natsuki 4e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/e.png")
image natsuki 4f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/f.png")
image natsuki 4g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/g.png")
image natsuki 4h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/h.png")
image natsuki 4i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/i.png")
image natsuki 4j = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/j.png")
image natsuki 4k = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/k.png")
image natsuki 4l = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/l.png")
image natsuki 4m = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/m.png")
image natsuki 4n = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/n.png")
image natsuki 4o = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/o.png")
image natsuki 4p = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/p.png")
image natsuki 4q = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/q.png")
image natsuki 4r = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/r.png")
image natsuki 4s = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/s.png")
image natsuki 4t = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/t.png")
image natsuki 4u = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/u.png")
image natsuki 4v = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/v.png")
image natsuki 4w = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/w.png")
image natsuki 4x = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/x.png")
image natsuki 4y = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/y.png")
image natsuki 4z = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/z.png")

image natsuki 12 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2t.png")
image natsuki 12a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2ta.png")
image natsuki 12b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tb.png")
image natsuki 12c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tc.png")
image natsuki 12d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2td.png")
image natsuki 12e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2te.png")
image natsuki 12f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tf.png")
image natsuki 12g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tg.png")
image natsuki 12h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2th.png")
image natsuki 12i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2ti.png")

image natsuki 42 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2t.png")
image natsuki 42a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2ta.png")
image natsuki 42b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tb.png")
image natsuki 42c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tc.png")
image natsuki 42d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2td.png")
image natsuki 42e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2te.png")
image natsuki 42f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tf.png")
image natsuki 42g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tg.png")
image natsuki 42h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2th.png")
image natsuki 42i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2ti.png")

image natsuki 51 = im.Composite((960, 960), (18, 22), "natsuki/1t.png", (0, 0), "natsuki/3.png")
image natsuki 5a = im.Composite((960, 960), (18, 22), "natsuki/a.png", (0, 0), "natsuki/3.png")
image natsuki 5b = im.Composite((960, 960), (18, 22), "natsuki/b.png", (0, 0), "natsuki/3.png")
image natsuki 5c = im.Composite((960, 960), (18, 22), "natsuki/c.png", (0, 0), "natsuki/3.png")
image natsuki 5d = im.Composite((960, 960), (18, 22), "natsuki/d.png", (0, 0), "natsuki/3.png")
image natsuki 5e = im.Composite((960, 960), (18, 22), "natsuki/e.png", (0, 0), "natsuki/3.png")
image natsuki 5f = im.Composite((960, 960), (18, 22), "natsuki/f.png", (0, 0), "natsuki/3.png")
image natsuki 5g = im.Composite((960, 960), (18, 22), "natsuki/g.png", (0, 0), "natsuki/3.png")
image natsuki 5h = im.Composite((960, 960), (18, 22), "natsuki/h.png", (0, 0), "natsuki/3.png")
image natsuki 5i = im.Composite((960, 960), (18, 22), "natsuki/i.png", (0, 0), "natsuki/3.png")
image natsuki 5j = im.Composite((960, 960), (18, 22), "natsuki/j.png", (0, 0), "natsuki/3.png")
image natsuki 5k = im.Composite((960, 960), (18, 22), "natsuki/k.png", (0, 0), "natsuki/3.png")
image natsuki 5l = im.Composite((960, 960), (18, 22), "natsuki/l.png", (0, 0), "natsuki/3.png")
image natsuki 5m = im.Composite((960, 960), (18, 22), "natsuki/m.png", (0, 0), "natsuki/3.png")
image natsuki 5n = im.Composite((960, 960), (18, 22), "natsuki/n.png", (0, 0), "natsuki/3.png")
image natsuki 5o = im.Composite((960, 960), (18, 22), "natsuki/o.png", (0, 0), "natsuki/3.png")
image natsuki 5p = im.Composite((960, 960), (18, 22), "natsuki/p.png", (0, 0), "natsuki/3.png")
image natsuki 5q = im.Composite((960, 960), (18, 22), "natsuki/q.png", (0, 0), "natsuki/3.png")
image natsuki 5r = im.Composite((960, 960), (18, 22), "natsuki/r.png", (0, 0), "natsuki/3.png")
image natsuki 5s = im.Composite((960, 960), (18, 22), "natsuki/s.png", (0, 0), "natsuki/3.png")
image natsuki 5t = im.Composite((960, 960), (18, 22), "natsuki/t.png", (0, 0), "natsuki/3.png")
image natsuki 5u = im.Composite((960, 960), (18, 22), "natsuki/u.png", (0, 0), "natsuki/3.png")
image natsuki 5v = im.Composite((960, 960), (18, 22), "natsuki/v.png", (0, 0), "natsuki/3.png")
image natsuki 5w = im.Composite((960, 960), (18, 22), "natsuki/w.png", (0, 0), "natsuki/3.png")
image natsuki 5x = im.Composite((960, 960), (18, 22), "natsuki/x.png", (0, 0), "natsuki/3.png")
image natsuki 5y = im.Composite((960, 960), (18, 22), "natsuki/y.png", (0, 0), "natsuki/3.png")
image natsuki 5z = im.Composite((960, 960), (18, 22), "natsuki/z.png", (0, 0), "natsuki/3.png")

# Natsuki in her casual outfit [Day 4 - Natsuki Route]
image natsuki 1ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/a.png")
image natsuki 1bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/b.png")
image natsuki 1bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/c.png")
image natsuki 1bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/d.png")
image natsuki 1be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/e.png")
image natsuki 1bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/f.png")
image natsuki 1bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/g.png")
image natsuki 1bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/h.png")
image natsuki 1bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/i.png")
image natsuki 1bj = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/j.png")
image natsuki 1bk = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/k.png")
image natsuki 1bl = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/l.png")
image natsuki 1bm = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/m.png")
image natsuki 1bn = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/n.png")
image natsuki 1bo = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/o.png")
image natsuki 1bp = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/p.png")
image natsuki 1bq = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/q.png")
image natsuki 1br = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/r.png")
image natsuki 1bs = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/s.png")
image natsuki 1bt = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/t.png")
image natsuki 1bu = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/u.png")
image natsuki 1bv = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/v.png")
image natsuki 1bw = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/w.png")
image natsuki 1bx = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/x.png")
image natsuki 1by = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/y.png")
image natsuki 1bz = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/z.png")

image natsuki 2ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/a.png")
image natsuki 2bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/b.png")
image natsuki 2bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/c.png")
image natsuki 2bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/d.png")
image natsuki 2be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/e.png")
image natsuki 2bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/f.png")
image natsuki 2bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/g.png")
image natsuki 2bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/h.png")
image natsuki 2bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/i.png")
image natsuki 2bj = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/j.png")
image natsuki 2bk = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/k.png")
image natsuki 2bl = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/l.png")
image natsuki 2bm = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/m.png")
image natsuki 2bn = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/n.png")
image natsuki 2bo = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/o.png")
image natsuki 2bp = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/p.png")
image natsuki 2bq = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/q.png")
image natsuki 2br = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/r.png")
image natsuki 2bs = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/s.png")
image natsuki 2bt = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/t.png")
image natsuki 2bu = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/u.png")
image natsuki 2bv = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/v.png")
image natsuki 2bw = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/w.png")
image natsuki 2bx = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/x.png")
image natsuki 2by = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/y.png")
image natsuki 2bz = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/z.png")

image natsuki 3ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/a.png")
image natsuki 3bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/b.png")
image natsuki 3bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/c.png")
image natsuki 3bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/d.png")
image natsuki 3be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/e.png")
image natsuki 3bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/f.png")
image natsuki 3bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/g.png")
image natsuki 3bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/h.png")
image natsuki 3bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/i.png")
image natsuki 3bj = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/j.png")
image natsuki 3bk = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/k.png")
image natsuki 3bl = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/l.png")
image natsuki 3bm = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/m.png")
image natsuki 3bn = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/n.png")
image natsuki 3bo = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/o.png")
image natsuki 3bp = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/p.png")
image natsuki 3bq = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/q.png")
image natsuki 3br = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/r.png")
image natsuki 3bs = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/s.png")
image natsuki 3bt = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/t.png")
image natsuki 3bu = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/u.png")
image natsuki 3bv = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/v.png")
image natsuki 3bw = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/w.png")
image natsuki 3bx = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/x.png")
image natsuki 3by = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/y.png")
image natsuki 3bz = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/z.png")

image natsuki 4ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/a.png")
image natsuki 4bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/b.png")
image natsuki 4bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/c.png")
image natsuki 4bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/d.png")
image natsuki 4be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/e.png")
image natsuki 4bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/f.png")
image natsuki 4bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/g.png")
image natsuki 4bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/h.png")
image natsuki 4bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/i.png")
image natsuki 4bj = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/j.png")
image natsuki 4bk = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/k.png")
image natsuki 4bl = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/l.png")
image natsuki 4bm = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/m.png")
image natsuki 4bn = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/n.png")
image natsuki 4bo = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/o.png")
image natsuki 4bp = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/p.png")
image natsuki 4bq = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/q.png")
image natsuki 4br = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/r.png")
image natsuki 4bs = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/s.png")
image natsuki 4bt = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/t.png")
image natsuki 4bu = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/u.png")
image natsuki 4bv = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/v.png")
image natsuki 4bw = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/w.png")
image natsuki 4bx = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/x.png")
image natsuki 4by = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/y.png")
image natsuki 4bz = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/z.png")

image natsuki 12ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bta.png")
image natsuki 12bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btb.png")
image natsuki 12bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btc.png")
image natsuki 12bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btd.png")
image natsuki 12be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bte.png")
image natsuki 12bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btf.png")
image natsuki 12bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btg.png")
image natsuki 12bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bth.png")
image natsuki 12bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bti.png")

image natsuki 42ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bta.png")
image natsuki 42bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btb.png")
image natsuki 42bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btc.png")
image natsuki 42bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btd.png")
image natsuki 42be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bte.png")
image natsuki 42bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btf.png")
image natsuki 42bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btg.png")
image natsuki 42bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bth.png")
image natsuki 42bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bti.png")

image natsuki 5ba = im.Composite((960, 960), (18, 22), "natsuki/a.png", (0, 0), "natsuki/3b.png")
image natsuki 5bb = im.Composite((960, 960), (18, 22), "natsuki/b.png", (0, 0), "natsuki/3b.png")
image natsuki 5bc = im.Composite((960, 960), (18, 22), "natsuki/c.png", (0, 0), "natsuki/3b.png")
image natsuki 5bd = im.Composite((960, 960), (18, 22), "natsuki/d.png", (0, 0), "natsuki/3b.png")
image natsuki 5be = im.Composite((960, 960), (18, 22), "natsuki/e.png", (0, 0), "natsuki/3b.png")
image natsuki 5bf = im.Composite((960, 960), (18, 22), "natsuki/f.png", (0, 0), "natsuki/3b.png")
image natsuki 5bg = im.Composite((960, 960), (18, 22), "natsuki/g.png", (0, 0), "natsuki/3b.png")
image natsuki 5bh = im.Composite((960, 960), (18, 22), "natsuki/h.png", (0, 0), "natsuki/3b.png")
image natsuki 5bi = im.Composite((960, 960), (18, 22), "natsuki/i.png", (0, 0), "natsuki/3b.png")
image natsuki 5bj = im.Composite((960, 960), (18, 22), "natsuki/j.png", (0, 0), "natsuki/3b.png")
image natsuki 5bk = im.Composite((960, 960), (18, 22), "natsuki/k.png", (0, 0), "natsuki/3b.png")
image natsuki 5bl = im.Composite((960, 960), (18, 22), "natsuki/l.png", (0, 0), "natsuki/3b.png")
image natsuki 5bm = im.Composite((960, 960), (18, 22), "natsuki/m.png", (0, 0), "natsuki/3b.png")
image natsuki 5bn = im.Composite((960, 960), (18, 22), "natsuki/n.png", (0, 0), "natsuki/3b.png")
image natsuki 5bo = im.Composite((960, 960), (18, 22), "natsuki/o.png", (0, 0), "natsuki/3b.png")
image natsuki 5bp = im.Composite((960, 960), (18, 22), "natsuki/p.png", (0, 0), "natsuki/3b.png")
image natsuki 5bq = im.Composite((960, 960), (18, 22), "natsuki/q.png", (0, 0), "natsuki/3b.png")
image natsuki 5br = im.Composite((960, 960), (18, 22), "natsuki/r.png", (0, 0), "natsuki/3b.png")
image natsuki 5bs = im.Composite((960, 960), (18, 22), "natsuki/s.png", (0, 0), "natsuki/3b.png")
image natsuki 5bt = im.Composite((960, 960), (18, 22), "natsuki/t.png", (0, 0), "natsuki/3b.png")
image natsuki 5bu = im.Composite((960, 960), (18, 22), "natsuki/u.png", (0, 0), "natsuki/3b.png")
image natsuki 5bv = im.Composite((960, 960), (18, 22), "natsuki/v.png", (0, 0), "natsuki/3b.png")
image natsuki 5bw = im.Composite((960, 960), (18, 22), "natsuki/w.png", (0, 0), "natsuki/3b.png")
image natsuki 5bx = im.Composite((960, 960), (18, 22), "natsuki/x.png", (0, 0), "natsuki/3b.png")
image natsuki 5by = im.Composite((960, 960), (18, 22), "natsuki/y.png", (0, 0), "natsuki/3b.png")
image natsuki 5bz = im.Composite((960, 960), (18, 22), "natsuki/z.png", (0, 0), "natsuki/3b.png")

# These image definitions are left-overs of certain Natsuki expressions 
# found in the original 1.0 release of DDLC.
image natsuki 1 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 2 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 3 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 4 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 5 = im.Composite((960, 960), (18, 22), "natsuki/1t.png", (0, 0), "natsuki/3.png")

# This image shows the realistic mouth on Natsuki on a random playthrough
# of Act 2.
image natsuki mouth = LiveComposite((960, 960), (0, 0), "natsuki/0.png", (390, 340), "n_rects_mouth", (480, 334), "n_rects_mouth")

# This image shows black rectangles on Natsuki on a random playthrough
# of Act 2.
image n_rects_mouth:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    size (20, 25)

# This image transform makes the realistic mouth move on Natsuki's face
# on a random playthrough of Act 2.
image n_moving_mouth:
    "images/natsuki/mouth.png"
    pos (615, 305)
    xanchor 0.5 yanchor 0.5
    parallel:
        choice:
            ease 0.10 yzoom 0.2
        choice:
            ease 0.05 yzoom 0.2
        choice:
            ease 0.075 yzoom 0.2
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        pass
        choice:
            ease 0.10 yzoom 1
        choice:
            ease 0.05 yzoom 1
        choice:
            ease 0.075 yzoom 1
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        repeat
    parallel:
        choice:
            0.2
        choice:
            0.4
        choice:
            0.6
        ease 0.2 xzoom 0.4
        ease 0.2 xzoom 0.8
        repeat

# These images show the Natsuki ghost sprite shown in the poemgame of 
# Act 2.
image natsuki_ghost_blood:
    "#00000000"
    "natsuki/ghost_blood.png" with ImageDissolve("images/menu/wipedown.png", 80.0, ramplen=4, alpha=True)
    pos (620,320) zoom 0.80

image natsuki ghost_base:
    "natsuki/ghost1.png"
image natsuki ghost1:
    "natsuki 11"
    "natsuki ghost_base" with Dissolve(20.0, alpha=True)
image natsuki ghost2 = Image("natsuki/ghost2.png")
image natsuki ghost3 = Image("natsuki/ghost3.png")
image natsuki ghost4:
    "natsuki ghost3"
    parallel:
        easeout 0.25 zoom 4.5 yoffset 1200
    parallel:
        ease 0.025 xoffset -20
        ease 0.025 xoffset 20
        repeat
    0.25
    "black"

# This image makes Natsuki's sprite glitch up for a bit before
# returning to normal.
image natsuki glitch1:
    "natsuki/glitch1.png"
    zoom 1.25
    block:
        yoffset 300 xoffset 100 ytile 2
        linear 0.15 yoffset 200
        repeat
    time 0.75
    yoffset 0 zoom 1 xoffset 0 ytile 1
    "natsuki 4e"

image natsuki scream = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/scream.png")
image natsuki vomit = "natsuki/vomit.png"

# These images declare alterative eyes for Natsuki on a random playthrough of
# Act 2.
image n_blackeyes = "images/natsuki/blackeyes.png"
image n_eye = "images/natsuki/eye.png"

# Yuri's Character Definitions
# Note: Sprites with a 'y' in the middle are Yuri's Yandere Sprites.
image yuri 1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/a.png")
image yuri 2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 3 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 4 = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/a2.png")

image yuri 1a = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/a.png")
image yuri 1b = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/b.png")
image yuri 1c = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/c.png")
image yuri 1d = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/d.png")
image yuri 1e = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/e.png")
image yuri 1f = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/f.png")
image yuri 1g = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/g.png")
image yuri 1h = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/h.png")
image yuri 1i = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/i.png")
image yuri 1j = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/j.png")
image yuri 1k = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/k.png")
image yuri 1l = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/l.png")
image yuri 1m = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/m.png")
image yuri 1n = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/n.png")
image yuri 1o = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/o.png")
image yuri 1p = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/p.png")
image yuri 1q = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/q.png")
image yuri 1r = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/r.png")
image yuri 1s = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/s.png")
image yuri 1t = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/t.png")
image yuri 1u = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/u.png")
image yuri 1v = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/v.png")
image yuri 1w = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/w.png")

image yuri 1y1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y1.png")
image yuri 1y2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y2.png")
image yuri 1y3 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y3.png")
image yuri 1y4 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y4.png")
image yuri 1y5 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y5.png")
image yuri 1y6 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y6.png")
image yuri 1y7 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y7.png")

image yuri 2a = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 2b = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/b.png")
image yuri 2c = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/c.png")
image yuri 2d = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/d.png")
image yuri 2e = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/e.png")
image yuri 2f = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/f.png")
image yuri 2g = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/g.png")
image yuri 2h = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/h.png")
image yuri 2i = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/i.png")
image yuri 2j = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/j.png")
image yuri 2k = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/k.png")
image yuri 2l = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/l.png")
image yuri 2m = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/m.png")
image yuri 2n = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/n.png")
image yuri 2o = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/o.png")
image yuri 2p = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/p.png")
image yuri 2q = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/q.png")
image yuri 2r = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/r.png")
image yuri 2s = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/s.png")
image yuri 2t = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/t.png")
image yuri 2u = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/u.png")
image yuri 2v = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/v.png")
image yuri 2w = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/w.png")

image yuri 2y1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y1.png")
image yuri 2y2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y2.png")
image yuri 2y3 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y3.png")
image yuri 2y4 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y4.png")
image yuri 2y5 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y5.png")
image yuri 2y6 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y6.png")
image yuri 2y7 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y7.png")

image yuri 3a = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 3b = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/b.png")
image yuri 3c = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/c.png")
image yuri 3d = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/d.png")
image yuri 3e = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/e.png")
image yuri 3f = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/f.png")
image yuri 3g = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/g.png")
image yuri 3h = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/h.png")
image yuri 3i = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/i.png")
image yuri 3j = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/j.png")
image yuri 3k = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/k.png")
image yuri 3l = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/l.png")
image yuri 3m = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/m.png")
image yuri 3n = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/n.png")
image yuri 3o = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/o.png")
image yuri 3p = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/p.png")
image yuri 3q = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/q.png")
image yuri 3r = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/r.png")
image yuri 3s = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/s.png")
image yuri 3t = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/t.png")
image yuri 3u = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/u.png")
image yuri 3v = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/v.png")
image yuri 3w = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/w.png")

image yuri 3y1 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y1.png")
image yuri 3y2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y2.png")
image yuri 3y3 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y3.png")
image yuri 3y4 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y4.png")
image yuri 3y5 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y5.png")
image yuri 3y6 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y6.png")
image yuri 3y7 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y7.png")

image yuri 4a = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/a2.png")
image yuri 4b = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/b2.png")
image yuri 4c = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/c2.png")
image yuri 4d = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/d2.png")
image yuri 4e = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/e2.png")

# Yuri in her casual outfit [Day 4 - Yuri Route]
image yuri 1ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")

image yuri 2ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")

image yuri 3ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")

image yuri 4ba = im.Composite((960, 960), (0, 0), "yuri/a2.png", (0, 0), "yuri/3b.png")
image yuri 4bb = im.Composite((960, 960), (0, 0), "yuri/b2.png", (0, 0), "yuri/3b.png")
image yuri 4bc = im.Composite((960, 960), (0, 0), "yuri/c2.png", (0, 0), "yuri/3b.png")
image yuri 4bd = im.Composite((960, 960), (0, 0), "yuri/d2.png", (0, 0), "yuri/3b.png")
image yuri 4be = im.Composite((960, 960), (0, 0), "yuri/e2.png", (0, 0), "yuri/3b.png")

#rikka neutral poses
image rikka 1 = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/a.png")
image rikka 2 = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/a.png")
image rikka 3 = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/a.png")
image rikka 4 = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/a.png")

#neither arm up
image rikka 1a = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/a.png")
image rikka 1aa = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/aa.png")
image rikka 1aa2 = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/aa2.png")
image rikka 1b = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/b.png")
image rikka 1c = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/c.png")
image rikka 1d = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/d.png")
image rikka 1e = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/e.png")
image rikka 1f = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/f.png")
image rikka 1g = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/g.png")
image rikka 1g2 = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/g2.png")
image rikka 1h = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/h.png")
image rikka 1i = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/i.png")
image rikka 1j = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/j.png")
image rikka 1k = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/k.png")
image rikka 1l = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/l.png")
image rikka 1m = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/m.png")
image rikka 1n = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/n.png")
image rikka 1o = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/o.png")
image rikka 1p = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/p.png")
image rikka 1q = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/q.png")
image rikka 1r = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/r.png")
image rikka 1s = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/s.png")
image rikka 1t = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/t.png")
image rikka 1u = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/u.png")
image rikka 1v = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/v.png")
image rikka 1w = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/w.png")
image rikka 1x = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/x.png")
image rikka 1y = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/y.png")
image rikka 1z = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/z.png")

#right arm up
image rikka 2a = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/a.png")
image rikka 2aa = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/aa.png")
image rikka 2aa2 = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/aa2.png")
image rikka 2b = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/b.png")
image rikka 2c = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/c.png")
image rikka 2d = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/d.png")
image rikka 2e = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/e.png")
image rikka 2f = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/f.png")
image rikka 2g = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/g.png")
image rikka 2g2 = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/g2.png")
image rikka 2h = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/h.png")
image rikka 2i = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/i.png")
image rikka 2j = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/j.png")
image rikka 2k = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/k.png")
image rikka 2l = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/l.png")
image rikka 2m = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/m.png")
image rikka 2n = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/n.png")
image rikka 2o = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/o.png")
image rikka 2p = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/p.png")
image rikka 2q = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/q.png")
image rikka 2r = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/r.png")
image rikka 2s = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/s.png")
image rikka 2t = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/t.png")
image rikka 2u = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/u.png")
image rikka 2v = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/v.png")
image rikka 2w = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/w.png")
image rikka 2x = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/x.png")
image rikka 2y = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/y.png")
image rikka 2z = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/1l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/z.png")

#left arm up
image rikka 3a = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/a.png")
image rikka 3aa = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/aa.png")
image rikka 3aa2 = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/aa2.png")
image rikka 3b = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/b.png")
image rikka 3c = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/c.png")
image rikka 3d = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/d.png")
image rikka 3e = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/e.png")
image rikka 3f = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/f.png")
image rikka 3g = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/g.png")
image rikka 3g2 = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/g2.png")
image rikka 3h = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/h.png")
image rikka 3i = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/i.png")
image rikka 3j = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/j.png")
image rikka 3k = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/k.png")
image rikka 3l = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/l.png")
image rikka 3m = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/m.png")
image rikka 3n = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/n.png")
image rikka 3o = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/o.png")
image rikka 3p = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/p.png")
image rikka 3q = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/q.png")
image rikka 3r = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/r.png")
image rikka 3s = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/s.png")
image rikka 3t = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/t.png")
image rikka 3u = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/u.png")
image rikka 3v = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/v.png")
image rikka 3w = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/w.png")
image rikka 3x = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/x.png")
image rikka 3y = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/y.png")
image rikka 3z = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/1r.png", (0, 0), "mod_assets/rikka_assets/z.png")

#both arms up
image rikka 4a = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/a.png")
image rikka 4aa = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/aa.png")
image rikka 4aa2 = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/aa2.png")
image rikka 4b = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/b.png")
image rikka 4c = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/c.png")
image rikka 4d = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/d.png")
image rikka 4e = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/e.png")
image rikka 4f = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/f.png")
image rikka 4g = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/g.png")
image rikka 4g2 = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/g2.png")
image rikka 4h = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/h.png")
image rikka 4i = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/i.png")
image rikka 4j = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/j.png")
image rikka 4k = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/k.png")
image rikka 4l = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/l.png")
image rikka 4m = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/m.png")
image rikka 4n = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/n.png")
image rikka 4o = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/o.png")
image rikka 4p = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/p.png")
image rikka 4q = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/q.png")
image rikka 4r = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/r.png")
image rikka 4s = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/s.png")
image rikka 4t = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/t.png")
image rikka 4u = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/u.png")
image rikka 4v = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/v.png")
image rikka 4w = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/w.png")
image rikka 4x = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/x.png")
image rikka 4y = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/y.png")
image rikka 4z = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/2l.png", (0, 0), "mod_assets/rikka_assets/2r.png", (0, 0), "mod_assets/rikka_assets/z.png")

#arms crossed
image rikka 5a = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/3.png",  (0, 0), "mod_assets/rikka_assets/a.png")
image rikka 5aa = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/3.png", (0, 0), "mod_assets/rikka_assets/aa.png")
image rikka 5aa2 = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/3.png", (0, 0), "mod_assets/rikka_assets/aa2.png")
image rikka 5b = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/3.png",  (0, 0), "mod_assets/rikka_assets/b.png")
image rikka 5c = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/3.png",  (0, 0), "mod_assets/rikka_assets/c.png")
image rikka 5d = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/3.png",  (0, 0), "mod_assets/rikka_assets/d.png")
image rikka 5e = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/3.png",  (0, 0), "mod_assets/rikka_assets/e.png")
image rikka 5f = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/3.png",  (0, 0), "mod_assets/rikka_assets/f.png")
image rikka 5g = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/3.png",  (0, 0), "mod_assets/rikka_assets/g.png")
image rikka 5g2 = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/3.png",  (0, 0), "mod_assets/rikka_assets/g2.png")
image rikka 5h = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/3.png",  (0, 0), "mod_assets/rikka_assets/h.png")
image rikka 5i = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/3.png",  (0, 0), "mod_assets/rikka_assets/i.png")
image rikka 5j = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/3.png",  (0, 0), "mod_assets/rikka_assets/j.png")
image rikka 5k = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/3.png",  (0, 0), "mod_assets/rikka_assets/k.png")
image rikka 5l = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/3.png",  (0, 0), "mod_assets/rikka_assets/l.png")
image rikka 5m = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/3.png",  (0, 0), "mod_assets/rikka_assets/m.png")
image rikka 5n = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/3.png",  (0, 0), "mod_assets/rikka_assets/n.png")
image rikka 5o = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/3.png",  (0, 0), "mod_assets/rikka_assets/o.png")
image rikka 5p = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/3.png",  (0, 0), "mod_assets/rikka_assets/p.png")
image rikka 5q = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/3.png",  (0, 0), "mod_assets/rikka_assets/q.png")
image rikka 5r = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/3.png",  (0, 0), "mod_assets/rikka_assets/r.png")
image rikka 5s = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/3.png",  (0, 0), "mod_assets/rikka_assets/s.png")
image rikka 5t = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/3.png",  (0, 0), "mod_assets/rikka_assets/t.png")
image rikka 5u = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/3.png",  (0, 0), "mod_assets/rikka_assets/u.png")
image rikka 5v = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/3.png",  (0, 0), "mod_assets/rikka_assets/v.png")
image rikka 5w = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/3.png",  (0, 0), "mod_assets/rikka_assets/w.png")
image rikka 5x = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/3.png",  (0, 0), "mod_assets/rikka_assets/x.png")
image rikka 5y = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/3.png",  (0, 0), "mod_assets/rikka_assets/y.png")
image rikka 5z = im.Composite((960, 960), (0, 0), "mod_assets/rikka_assets/3.png",  (0, 0), "mod_assets/rikka_assets/z.png")

image rikka 1a qg:
    Glitch("rikka 1a")

image rikka 1h qg:
    Glitch("rikka 1h")


#image rikka rg:
#    block:
#        choice:
#            "mod_assets/rikka_assets/rg1.png"
#        choice:
#            "mod_assets/rikka_assets/rg2.png"
#        choice:
#            "mod_assets/rikka_assets/rg3.png"
#    block:
#        choice:
#            pause 0.05
#        choice:
#            pause 0.1
#        choice:
#            pause 0.15
#        choice:
#            pause 0.2
#    repeat

#kotonoha arms down
image kotonoha 1a = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/1.png", (0, 0), "mod_assets/kotonoha_assets/a.png")
image kotonoha 1aa = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/1.png", (0, 0), "mod_assets/kotonoha_assets/aa.png")
image kotonoha 1b = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/1.png", (0, 0), "mod_assets/kotonoha_assets/b.png")
image kotonoha 1c = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/1.png", (0, 0), "mod_assets/kotonoha_assets/c.png")
image kotonoha 1d = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/1.png", (0, 0), "mod_assets/kotonoha_assets/d.png")
image kotonoha 1e = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/1.png", (0, 0), "mod_assets/kotonoha_assets/e.png")
image kotonoha 1e1 = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/1.png", (0, 0), "mod_assets/kotonoha_assets/e1.png")
image kotonoha 1f = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/1.png", (0, 0), "mod_assets/kotonoha_assets/f.png")
image kotonoha 1g = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/1.png", (0, 0), "mod_assets/kotonoha_assets/g.png")
image kotonoha 1h = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/1.png", (0, 0), "mod_assets/kotonoha_assets/h.png")
image kotonoha 1h1 = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/1.png", (0, 0), "mod_assets/kotonoha_assets/h1.png")
image kotonoha 1i = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/1.png", (0, 0), "mod_assets/kotonoha_assets/i.png")
image kotonoha 1j = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/1.png", (0, 0), "mod_assets/kotonoha_assets/j.png")
image kotonoha 1k = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/1.png", (0, 0), "mod_assets/kotonoha_assets/k.png")
image kotonoha 1l = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/1.png", (0, 0), "mod_assets/kotonoha_assets/l.png")
image kotonoha 1m = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/1.png", (0, 0), "mod_assets/kotonoha_assets/m.png")
image kotonoha 1n = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/1.png", (0, 0), "mod_assets/kotonoha_assets/n.png")
image kotonoha 1o = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/1.png", (0, 0), "mod_assets/kotonoha_assets/o.png")
image kotonoha 1p = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/1.png", (0, 0), "mod_assets/kotonoha_assets/p.png")
image kotonoha 1q = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/1.png", (0, 0), "mod_assets/kotonoha_assets/q.png")
image kotonoha 1r = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/1.png", (0, 0), "mod_assets/kotonoha_assets/r.png")
image kotonoha 1s = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/1.png", (0, 0), "mod_assets/kotonoha_assets/s.png")
image kotonoha 1t = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/1.png", (0, 0), "mod_assets/kotonoha_assets/t.png")
image kotonoha 1t1 = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/1.png", (0, 0), "mod_assets/kotonoha_assets/t1.png")
image kotonoha 1u = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/1.png", (0, 0), "mod_assets/kotonoha_assets/u.png")
image kotonoha 1u2 = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/1.png", (0, 0), "mod_assets/kotonoha_assets/u2.png")
image kotonoha 1u3 = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/1.png", (0, 0), "mod_assets/kotonoha_assets/u3.png")
image kotonoha 1v = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/1.png", (0, 0), "mod_assets/kotonoha_assets/v.png")
image kotonoha 1v1 = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/1.png", (0, 0), "mod_assets/kotonoha_assets/v1.png")
image kotonoha 1w = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/1.png", (0, 0), "mod_assets/kotonoha_assets/w.png")
image kotonoha 1w1 = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/1.png", (0, 0), "mod_assets/kotonoha_assets/w1.png")
image kotonoha 1x = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/1.png", (0, 0), "mod_assets/kotonoha_assets/x.png")

#koto arm up
image kotonoha 2a = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/2.png", (0, 0), "mod_assets/kotonoha_assets/a.png")
image kotonoha 2aa = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/2.png", (0, 0), "mod_assets/kotonoha_assets/aa.png")
image kotonoha 2b = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/2.png", (0, 0), "mod_assets/kotonoha_assets/b.png")
image kotonoha 2c = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/2.png", (0, 0), "mod_assets/kotonoha_assets/c.png")
image kotonoha 2d = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/2.png", (0, 0), "mod_assets/kotonoha_assets/d.png")
image kotonoha 2e = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/2.png", (0, 0), "mod_assets/kotonoha_assets/e.png")
image kotonoha 2e1 = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/2.png", (0, 0), "mod_assets/kotonoha_assets/e1.png")
image kotonoha 2f = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/2.png", (0, 0), "mod_assets/kotonoha_assets/f.png")
image kotonoha 2g = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/2.png", (0, 0), "mod_assets/kotonoha_assets/g.png")
image kotonoha 2h = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/2.png", (0, 0), "mod_assets/kotonoha_assets/h.png")
image kotonoha 2h1 = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/2.png", (0, 0), "mod_assets/kotonoha_assets/h1.png")
image kotonoha 2i = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/2.png", (0, 0), "mod_assets/kotonoha_assets/i.png")
image kotonoha 2j = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/2.png", (0, 0), "mod_assets/kotonoha_assets/j.png")
image kotonoha 2k = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/2.png", (0, 0), "mod_assets/kotonoha_assets/k.png")
image kotonoha 2l = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/2.png", (0, 0), "mod_assets/kotonoha_assets/l.png")
image kotonoha 2m = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/2.png", (0, 0), "mod_assets/kotonoha_assets/m.png")
image kotonoha 2n = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/2.png", (0, 0), "mod_assets/kotonoha_assets/n.png")
image kotonoha 2o = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/2.png", (0, 0), "mod_assets/kotonoha_assets/o.png")
image kotonoha 2p = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/2.png", (0, 0), "mod_assets/kotonoha_assets/p.png")
image kotonoha 2q = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/2.png", (0, 0), "mod_assets/kotonoha_assets/q.png")
image kotonoha 2r = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/2.png", (0, 0), "mod_assets/kotonoha_assets/r.png")
image kotonoha 2s = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/2.png", (0, 0), "mod_assets/kotonoha_assets/s.png")
image kotonoha 2t = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/2.png", (0, 0), "mod_assets/kotonoha_assets/t.png")
image kotonoha 2t1 = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/2.png", (0, 0), "mod_assets/kotonoha_assets/t1.png")
image kotonoha 2u = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/2.png", (0, 0), "mod_assets/kotonoha_assets/u.png")
image kotonoha 2u2 = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/2.png", (0, 0), "mod_assets/kotonoha_assets/u2.png")
image kotonoha 2u3 = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/2.png", (0, 0), "mod_assets/kotonoha_assets/u3.png")
image kotonoha 2v = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/2.png", (0, 0), "mod_assets/kotonoha_assets/v.png")
image kotonoha 2v1 = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/2.png", (0, 0), "mod_assets/kotonoha_assets/v1.png")
image kotonoha 2w = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/2.png", (0, 0), "mod_assets/kotonoha_assets/w.png")
image kotonoha 2w1 = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/2.png", (0, 0), "mod_assets/kotonoha_assets/w1.png")
image kotonoha 2x = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/2.png", (0, 0), "mod_assets/kotonoha_assets/x.png")

#koto arm on chest
image kotonoha 3a = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/3.png", (0, 0), "mod_assets/kotonoha_assets/a.png")
image kotonoha 3aa = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/3.png", (0, 0), "mod_assets/kotonoha_assets/aa.png")
image kotonoha 3b = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/3.png", (0, 0), "mod_assets/kotonoha_assets/b.png")
image kotonoha 3c = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/3.png", (0, 0), "mod_assets/kotonoha_assets/c.png")
image kotonoha 3d = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/3.png", (0, 0), "mod_assets/kotonoha_assets/d.png")
image kotonoha 3e = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/3.png", (0, 0), "mod_assets/kotonoha_assets/e.png")
image kotonoha 3e1 = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/3.png", (0, 0), "mod_assets/kotonoha_assets/e1.png")
image kotonoha 3f = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/3.png", (0, 0), "mod_assets/kotonoha_assets/f.png")
image kotonoha 3g = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/3.png", (0, 0), "mod_assets/kotonoha_assets/g.png")
image kotonoha 3h = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/3.png", (0, 0), "mod_assets/kotonoha_assets/h.png")
image kotonoha 3h1 = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/3.png", (0, 0), "mod_assets/kotonoha_assets/h1.png")
image kotonoha 3i = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/3.png", (0, 0), "mod_assets/kotonoha_assets/i.png")
image kotonoha 3j = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/3.png", (0, 0), "mod_assets/kotonoha_assets/j.png")
image kotonoha 3k = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/3.png", (0, 0), "mod_assets/kotonoha_assets/k.png")
image kotonoha 3l = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/3.png", (0, 0), "mod_assets/kotonoha_assets/l.png")
image kotonoha 3m = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/3.png", (0, 0), "mod_assets/kotonoha_assets/m.png")
image kotonoha 3n = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/3.png", (0, 0), "mod_assets/kotonoha_assets/n.png")
image kotonoha 3o = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/3.png", (0, 0), "mod_assets/kotonoha_assets/o.png")
image kotonoha 3p = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/3.png", (0, 0), "mod_assets/kotonoha_assets/p.png")
image kotonoha 3q = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/3.png", (0, 0), "mod_assets/kotonoha_assets/q.png")
image kotonoha 3r = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/3.png", (0, 0), "mod_assets/kotonoha_assets/r.png")
image kotonoha 3s = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/3.png", (0, 0), "mod_assets/kotonoha_assets/s.png")
image kotonoha 3t = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/3.png", (0, 0), "mod_assets/kotonoha_assets/t.png")
image kotonoha 3t1 = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/3.png", (0, 0), "mod_assets/kotonoha_assets/t1.png")
image kotonoha 3u = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/3.png", (0, 0), "mod_assets/kotonoha_assets/u.png")
image kotonoha 3u2 = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/3.png", (0, 0), "mod_assets/kotonoha_assets/u2.png")
image kotonoha 3u3 = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/3.png", (0, 0), "mod_assets/kotonoha_assets/u3.png")
image kotonoha 3v = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/3.png", (0, 0), "mod_assets/kotonoha_assets/v.png")
image kotonoha 3v1 = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/3.png", (0, 0), "mod_assets/kotonoha_assets/v1.png")
image kotonoha 3w = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/3.png", (0, 0), "mod_assets/kotonoha_assets/w.png")
image kotonoha 3w1 = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/3.png", (0, 0), "mod_assets/kotonoha_assets/w1.png")
image kotonoha 3x = im.Composite((960, 960), (0, 0), "mod_assets/kotonoha_assets/3.png", (0, 0), "mod_assets/kotonoha_assets/x.png")

image kotonoha kg:
    Glitch("kotonoha 1a")

image kotonoha kg2:
    Glitch("kotonoha 1a")
    pause 0.25
image kotonoha kmg:
    block:
        choice:
            "mod_assets/kotonoha_assets/kmg1.png"
        choice:
            "mod_assets/kotonoha_assets/kmg2.png"
        choice:
            "mod_assets/kotonoha_assets/kmg3.png"
    block:
        choice:
            pause 0.05
        choice:
            pause 0.1
        choice:
            pause 0.15
        choice:
            pause 0.2
    repeat

image kotonoha 1xg:
    Glitch("kotonoha 1x")

# This image shows the looping Yuri glitched head in Act 2.
image y_glitch_head:
    "images/yuri/za.png"
    0.15
    "images/yuri/zb.png"
    0.15
    "images/yuri/zc.png"
    0.15
    "images/yuri/zd.png"
    0.15
    repeat

# These images shows Yuri stabbing herself at the end of Act 2 in six stages.
image yuri stab_1 = "yuri/stab/1.png"
image yuri stab_2 = "yuri/stab/2.png"
image yuri stab_3 = "yuri/stab/3.png"
image yuri stab_4 = "yuri/stab/4.png"
image yuri stab_5 = "yuri/stab/5.png"
image yuri stab_6 = LiveComposite((960,960), (0, 0), "yuri/stab/6-mask.png", (0, 0), "yuri stab_6_eyes", (0, 0), "yuri/stab/6.png")

# This image transform animates Yuri's eyes on her 6th stabbing in Act 2.
image yuri stab_6_eyes:
    "yuri/stab/6-eyes.png"
    subpixel True
    parallel:
        choice:
            xoffset 0.5
        choice:
            xoffset 0
        choice:
            xoffset -0.5
        0.2
        repeat
    parallel:
        choice:
            yoffset 0.5
        choice:
            yoffset 0
        choice:
            yoffset -0.5
        0.2
        repeat
    parallel:
        2.05
        easeout 1.0 yoffset -15
        linear 10 yoffset -15

# These images shows Yuri with a offcenter right eye moving slowing away
# from her face.
image yuri oneeye = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/oneeye.png", (0, 0), "yuri oneeye2")
image yuri oneeye2:
    "yuri/oneeye2.png"
    subpixel True
    pause 5.0
    linear 60 xoffset -50 yoffset 20

# These images show a glitched Yuri during Act 2.
image yuri glitch:
    "yuri/glitch1.png"
    pause 0.1
    "yuri/glitch2.png"
    pause 0.1
    "yuri/glitch3.png"
    pause 0.1
    "yuri/glitch4.png"
    pause 0.1
    "yuri/glitch5.png"
    pause 0.1
    repeat
image yuri glitch2:
    "yuri/0a.png"
    pause 0.1
    "yuri/0b.png"
    pause 0.5
    "yuri/0a.png"
    pause 0.3
    "yuri/0b.png"
    pause 0.3
    "yuri 1"

# These image declarations show Yuri's moving eyes in Act 2.
image yuri eyes = LiveComposite((1280, 720), (0, 0), "yuri/eyes1.png", (0, 0), "yuripupils")

# This image shows the base of Yuri's sprite as her eyes move.
image yuri eyes_base = "yuri/eyes1.png"

# This image shows Yuri's realistic moving eyes during Act 2.
image yuripupils:
    "yuri/eyes2.png"
    yuripupils_move

image yuri cuts = "yuri/cuts.png"

# This image shows another glitched Yuri from Act 2. 
image yuri dragon:
    "yuri 3"
    0.25
    parallel:
        "yuri/dragon1.png"
        0.01
        "yuri/dragon2.png"
        0.01
        repeat
    parallel:
        0.01
        choice:
            xoffset -1
            xoffset -2
            xoffset -5
            xoffset -6
            xoffset -9
            xoffset -10
        0.01
        xoffset 0
        repeat
    time 0.55
    xoffset 0
    "yuri 3"

# Monika's Character Definitions
image monika 1 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 2 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 3 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 4 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 5 = im.Composite((960, 960), (0, 0), "monika/3a.png")

image monika 1a = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 1b = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/b.png")
image monika 1c = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/c.png")
image monika 1d = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/d.png")
image monika 1e = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/e.png")
image monika 1f = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/f.png")
image monika 1g = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/g.png")
image monika 1h = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/h.png")
image monika 1i = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/i.png")
image monika 1j = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/j.png")
image monika 1k = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/k.png")
image monika 1l = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/l.png")
image monika 1m = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/m.png")
image monika 1n = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/n.png")
image monika 1o = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/o.png")
image monika 1p = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/p.png")
image monika 1q = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/q.png")
image monika 1r = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/r.png")

image monika 2a = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 2b = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/b.png")
image monika 2c = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/c.png")
image monika 2d = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/d.png")
image monika 2e = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/e.png")
image monika 2f = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/f.png")
image monika 2g = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/g.png")
image monika 2h = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/h.png")
image monika 2i = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/i.png")
image monika 2j = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/j.png")
image monika 2k = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/k.png")
image monika 2l = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/l.png")
image monika 2m = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/m.png")
image monika 2n = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/n.png")
image monika 2o = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/o.png")
image monika 2p = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/p.png")
image monika 2q = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/q.png")
image monika 2r = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/r.png")

image monika 3a = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 3b = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/b.png")
image monika 3c = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/c.png")
image monika 3d = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/d.png")
image monika 3e = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/e.png")
image monika 3f = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/f.png")
image monika 3g = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/g.png")
image monika 3h = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/h.png")
image monika 3i = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/i.png")
image monika 3j = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/j.png")
image monika 3k = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/k.png")
image monika 3l = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/l.png")
image monika 3m = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/m.png")
image monika 3n = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/n.png")
image monika 3o = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/o.png")
image monika 3p = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/p.png")
image monika 3q = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/q.png")
image monika 3r = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/r.png")

image monika 4a = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 4b = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/b.png")
image monika 4c = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/c.png")
image monika 4d = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/d.png")
image monika 4e = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/e.png")
image monika 4f = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/f.png")
image monika 4g = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/g.png")
image monika 4h = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/h.png")
image monika 4i = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/i.png")
image monika 4j = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/j.png")
image monika 4k = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/k.png")
image monika 4l = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/l.png")
image monika 4m = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/m.png")
image monika 4n = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/n.png")
image monika 4o = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/o.png")
image monika 4p = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/p.png")
image monika 4q = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/q.png")
image monika 4r = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/r.png")

image monika 5a = im.Composite((960, 960), (0, 0), "monika/3a.png")
image monika 5b = im.Composite((960, 960), (0, 0), "monika/3b.png")

# This image transform shows a glitched Monika during a special poem.
image monika g1:
    "monika/g1.png"
    xoffset 35 yoffset 55
    parallel:
        zoom 1.00
        linear 0.10 zoom 1.03
        repeat
    parallel:
        xoffset 35
        0.20
        xoffset 0
        0.05
        xoffset -10
        0.05
        xoffset 0
        0.05
        xoffset -80
        0.05
        repeat
    time 1.25
    xoffset 0 yoffset 0 zoom 1.00
    "monika 3"

# This image transform shows Monika being glitched as she is 
# deleted in Act 3.
image monika g2:
    block:
        choice:
            "monika/g2.png"
        choice:
            "monika/g3.png"
        choice:
            "monika/g4.png"
    block:
        choice:
            pause 0.05
        choice:
            pause 0.1
        choice:
            pause 0.15
        choice:
            pause 0.2
    repeat

#Canon MC arms down 
image mc 1a = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/1.png", (0, 0), "mod_assets/canonmc_assets/a.png")
image mc 1a1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/1.png", (0, 0), "mod_assets/canonmc_assets/a1.png")
image mc 1b = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/1.png", (0, 0), "mod_assets/canonmc_assets/b.png")
image mc 1b1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/1.png", (0, 0), "mod_assets/canonmc_assets/b1.png")
image mc 1c = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/1.png", (0, 0), "mod_assets/canonmc_assets/c.png")
image mc 1c1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/1.png", (0, 0), "mod_assets/canonmc_assets/c1.png")
image mc 1d = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/1.png", (0, 0), "mod_assets/canonmc_assets/d.png")
image mc 1d1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/1.png", (0, 0), "mod_assets/canonmc_assets/d1.png")
image mc 1e = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/1.png", (0, 0), "mod_assets/canonmc_assets/e.png")
image mc 1e1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/1.png", (0, 0), "mod_assets/canonmc_assets/e1.png")
image mc 1f = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/1.png", (0, 0), "mod_assets/canonmc_assets/f.png")
image mc 1f1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/1.png", (0, 0), "mod_assets/canonmc_assets/f1.png")
image mc 1g = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/1.png", (0, 0), "mod_assets/canonmc_assets/g.png")
image mc 1g1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/1.png", (0, 0), "mod_assets/canonmc_assets/g1.png")
image mc 1h = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/1.png", (0, 0), "mod_assets/canonmc_assets/h.png")
image mc 1h1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/1.png", (0, 0), "mod_assets/canonmc_assets/h1.png")
image mc 1i = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/1.png", (0, 0), "mod_assets/canonmc_assets/i.png")
image mc 1i1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/1.png", (0, 0), "mod_assets/canonmc_assets/i1.png")
image mc 1i5 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/1.png", (0, 0), "mod_assets/canonmc_assets/i5.png")
image mc 1i6 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/1.png", (0, 0), "mod_assets/canonmc_assets/i6.png")
image mc 1i7 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/1.png", (0, 0), "mod_assets/canonmc_assets/i7.png")
image mc 1j = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/1.png", (0, 0), "mod_assets/canonmc_assets/j.png")
image mc 1j1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/1.png", (0, 0), "mod_assets/canonmc_assets/j1.png")
image mc 1k = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/1.png", (0, 0), "mod_assets/canonmc_assets/k.png")
image mc 1k1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/1.png", (0, 0), "mod_assets/canonmc_assets/k1.png")
image mc 1l = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/1.png", (0, 0), "mod_assets/canonmc_assets/l.png")
image mc 1l1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/1.png", (0, 0), "mod_assets/canonmc_assets/l1.png")
image mc 1m = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/1.png", (0, 0), "mod_assets/canonmc_assets/m.png")
image mc 1n = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/1.png", (0, 0), "mod_assets/canonmc_assets/n.png")
image mc 1o = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/1.png", (0, 0), "mod_assets/canonmc_assets/o.png")
image mc 1p = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/1.png", (0, 0), "mod_assets/canonmc_assets/p.png")
image mc 1q = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/1.png", (0, 0), "mod_assets/canonmc_assets/q.png")
image mc 1r = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/1.png", (0, 0), "mod_assets/canonmc_assets/r.png")
image mc 1s = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/1.png", (0, 0), "mod_assets/canonmc_assets/s.png")
image mc 1t = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/1.png", (0, 0), "mod_assets/canonmc_assets/t.png")
image mc 1u = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/1.png", (0, 0), "mod_assets/canonmc_assets/u.png")
image mc 1v = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/1.png", (0, 0), "mod_assets/canonmc_assets/v.png")
image mc 1w = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/1.png", (0, 0), "mod_assets/canonmc_assets/w.png")
image mc 1x = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/1.png", (0, 0), "mod_assets/canonmc_assets/x.png")
image mc 1y = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/1.png", (0, 0), "mod_assets/canonmc_assets/y.png")
image mc 1z = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/1.png", (0, 0), "mod_assets/canonmc_assets/z.png")

#Canon MC arms crossed 
image mc 2a = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/2.png", (0, 0), "mod_assets/canonmc_assets/a.png")
image mc 2a1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/2.png", (0, 0), "mod_assets/canonmc_assets/a1.png")
image mc 2b = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/2.png", (0, 0), "mod_assets/canonmc_assets/b.png")
image mc 2b1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/2.png", (0, 0), "mod_assets/canonmc_assets/b1.png")
image mc 2c = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/2.png", (0, 0), "mod_assets/canonmc_assets/c.png")
image mc 2c1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/2.png", (0, 0), "mod_assets/canonmc_assets/c1.png")
image mc 2d = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/2.png", (0, 0), "mod_assets/canonmc_assets/d.png")
image mc 2d1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/2.png", (0, 0), "mod_assets/canonmc_assets/d1.png")
image mc 2e = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/2.png", (0, 0), "mod_assets/canonmc_assets/e.png")
image mc 2e1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/2.png", (0, 0), "mod_assets/canonmc_assets/e1.png")
image mc 2f = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/2.png", (0, 0), "mod_assets/canonmc_assets/f.png")
image mc 2f1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/2.png", (0, 0), "mod_assets/canonmc_assets/f1.png")
image mc 2g = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/2.png", (0, 0), "mod_assets/canonmc_assets/g.png")
image mc 2g1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/2.png", (0, 0), "mod_assets/canonmc_assets/g1.png")
image mc 2h = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/2.png", (0, 0), "mod_assets/canonmc_assets/h.png")
image mc 2h1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/2.png", (0, 0), "mod_assets/canonmc_assets/h1.png")
image mc 2i = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/2.png", (0, 0), "mod_assets/canonmc_assets/i.png")
image mc 2i1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/2.png", (0, 0), "mod_assets/canonmc_assets/i1.png")
image mc 2i5 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/2.png", (0, 0), "mod_assets/canonmc_assets/i5.png")
image mc 2i6 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/2.png", (0, 0), "mod_assets/canonmc_assets/i6.png")
image mc 2i7 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/2.png", (0, 0), "mod_assets/canonmc_assets/i7.png")
image mc 2j = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/2.png", (0, 0), "mod_assets/canonmc_assets/j.png")
image mc 2j1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/2.png", (0, 0), "mod_assets/canonmc_assets/j1.png")
image mc 2k = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/2.png", (0, 0), "mod_assets/canonmc_assets/k.png")
image mc 2k1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/2.png", (0, 0), "mod_assets/canonmc_assets/k1.png")
image mc 2l = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/2.png", (0, 0), "mod_assets/canonmc_assets/l.png")
image mc 2l1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/2.png", (0, 0), "mod_assets/canonmc_assets/l1.png")
image mc 2m = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/2.png", (0, 0), "mod_assets/canonmc_assets/m.png")
image mc 2n = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/2.png", (0, 0), "mod_assets/canonmc_assets/n.png")
image mc 2o = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/2.png", (0, 0), "mod_assets/canonmc_assets/o.png")
image mc 2p = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/2.png", (0, 0), "mod_assets/canonmc_assets/p.png")
image mc 2q = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/2.png", (0, 0), "mod_assets/canonmc_assets/q.png")
image mc 2r = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/2.png", (0, 0), "mod_assets/canonmc_assets/r.png")
image mc 2s = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/2.png", (0, 0), "mod_assets/canonmc_assets/s.png")
image mc 2t = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/2.png", (0, 0), "mod_assets/canonmc_assets/t.png")
image mc 2u = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/2.png", (0, 0), "mod_assets/canonmc_assets/u.png")
image mc 2v = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/2.png", (0, 0), "mod_assets/canonmc_assets/v.png")
image mc 2w = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/2.png", (0, 0), "mod_assets/canonmc_assets/w.png")
image mc 2x = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/2.png", (0, 0), "mod_assets/canonmc_assets/x.png")
image mc 2y = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/2.png", (0, 0), "mod_assets/canonmc_assets/y.png")
image mc 2z = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/2.png", (0, 0), "mod_assets/canonmc_assets/z.png")

#Canon MC arms down casual
image mc 3a = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/3.png", (0, 0), "mod_assets/canonmc_assets/a.png")
image mc 3a1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/3.png", (0, 0), "mod_assets/canonmc_assets/a1.png")
image mc 3b = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/3.png", (0, 0), "mod_assets/canonmc_assets/b.png")
image mc 3b1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/3.png", (0, 0), "mod_assets/canonmc_assets/b1.png")
image mc 3c = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/3.png", (0, 0), "mod_assets/canonmc_assets/c.png")
image mc 3c1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/3.png", (0, 0), "mod_assets/canonmc_assets/c1.png")
image mc 3d = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/3.png", (0, 0), "mod_assets/canonmc_assets/d.png")
image mc 3d1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/3.png", (0, 0), "mod_assets/canonmc_assets/d1.png")
image mc 3e = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/3.png", (0, 0), "mod_assets/canonmc_assets/e.png")
image mc 3e1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/3.png", (0, 0), "mod_assets/canonmc_assets/e1.png")
image mc 3f = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/3.png", (0, 0), "mod_assets/canonmc_assets/f.png")
image mc 3f1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/3.png", (0, 0), "mod_assets/canonmc_assets/f1.png")
image mc 3g = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/3.png", (0, 0), "mod_assets/canonmc_assets/g.png")
image mc 3g1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/3.png", (0, 0), "mod_assets/canonmc_assets/g1.png")
image mc 3h = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/3.png", (0, 0), "mod_assets/canonmc_assets/h.png")
image mc 3h1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/3.png", (0, 0), "mod_assets/canonmc_assets/h1.png")
image mc 3i = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/3.png", (0, 0), "mod_assets/canonmc_assets/i.png")
image mc 3i1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/3.png", (0, 0), "mod_assets/canonmc_assets/i1.png")
image mc 3i5 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/3.png", (0, 0), "mod_assets/canonmc_assets/i5.png")
image mc 3i6 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/3.png", (0, 0), "mod_assets/canonmc_assets/i6.png")
image mc 3i7 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/3.png", (0, 0), "mod_assets/canonmc_assets/i7.png")
image mc 3j = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/3.png", (0, 0), "mod_assets/canonmc_assets/j.png")
image mc 3j1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/3.png", (0, 0), "mod_assets/canonmc_assets/j1.png")
image mc 3k = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/3.png", (0, 0), "mod_assets/canonmc_assets/k.png")
image mc 3k1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/3.png", (0, 0), "mod_assets/canonmc_assets/k1.png")
image mc 3l = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/3.png", (0, 0), "mod_assets/canonmc_assets/l.png")
image mc 3l1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/3.png", (0, 0), "mod_assets/canonmc_assets/l1.png")
image mc 3m = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/3.png", (0, 0), "mod_assets/canonmc_assets/m.png")
image mc 3n = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/3.png", (0, 0), "mod_assets/canonmc_assets/n.png")
image mc 3o = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/3.png", (0, 0), "mod_assets/canonmc_assets/o.png")
image mc 3p = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/3.png", (0, 0), "mod_assets/canonmc_assets/p.png")
image mc 3q = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/3.png", (0, 0), "mod_assets/canonmc_assets/q.png")
image mc 3r = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/3.png", (0, 0), "mod_assets/canonmc_assets/r.png")
image mc 3s = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/3.png", (0, 0), "mod_assets/canonmc_assets/s.png")
image mc 3t = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/3.png", (0, 0), "mod_assets/canonmc_assets/t.png")
image mc 3u = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/3.png", (0, 0), "mod_assets/canonmc_assets/u.png")
image mc 3v = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/3.png", (0, 0), "mod_assets/canonmc_assets/v.png")
image mc 3w = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/3.png", (0, 0), "mod_assets/canonmc_assets/w.png")
image mc 3x = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/3.png", (0, 0), "mod_assets/canonmc_assets/x.png")
image mc 3y = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/3.png", (0, 0), "mod_assets/canonmc_assets/y.png")
image mc 3z = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/3.png", (0, 0), "mod_assets/canonmc_assets/z.png")

#Canon MC arms crossed casual 
image mc 4a = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/4.png", (0, 0), "mod_assets/canonmc_assets/a.png")
image mc 4a1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/4.png", (0, 0), "mod_assets/canonmc_assets/a1.png")
image mc 4b = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/4.png", (0, 0), "mod_assets/canonmc_assets/b.png")
image mc 4b1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/4.png", (0, 0), "mod_assets/canonmc_assets/b1.png")
image mc 4c = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/4.png", (0, 0), "mod_assets/canonmc_assets/c.png")
image mc 4c1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/4.png", (0, 0), "mod_assets/canonmc_assets/c1.png")
image mc 4d = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/4.png", (0, 0), "mod_assets/canonmc_assets/d.png")
image mc 4d1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/4.png", (0, 0), "mod_assets/canonmc_assets/d1.png")
image mc 4e = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/4.png", (0, 0), "mod_assets/canonmc_assets/e.png")
image mc 4e1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/4.png", (0, 0), "mod_assets/canonmc_assets/e1.png")
image mc 4f = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/4.png", (0, 0), "mod_assets/canonmc_assets/f.png")
image mc 4f1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/4.png", (0, 0), "mod_assets/canonmc_assets/f1.png")
image mc 4g = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/4.png", (0, 0), "mod_assets/canonmc_assets/g.png")
image mc 4g1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/4.png", (0, 0), "mod_assets/canonmc_assets/g1.png")
image mc 4h = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/4.png", (0, 0), "mod_assets/canonmc_assets/h.png")
image mc 4h1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/4.png", (0, 0), "mod_assets/canonmc_assets/h1.png")
image mc 4i = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/4.png", (0, 0), "mod_assets/canonmc_assets/i.png")
image mc 4i1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/4.png", (0, 0), "mod_assets/canonmc_assets/i1.png")
image mc 4i5 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/4.png", (0, 0), "mod_assets/canonmc_assets/i5.png")
image mc 4i6 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/4.png", (0, 0), "mod_assets/canonmc_assets/i6.png")
image mc 4i7 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/4.png", (0, 0), "mod_assets/canonmc_assets/i7.png")
image mc 4j = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/4.png", (0, 0), "mod_assets/canonmc_assets/j.png")
image mc 4j1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/4.png", (0, 0), "mod_assets/canonmc_assets/j1.png")
image mc 4k = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/4.png", (0, 0), "mod_assets/canonmc_assets/k.png")
image mc 4k1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/4.png", (0, 0), "mod_assets/canonmc_assets/k1.png")
image mc 4l = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/4.png", (0, 0), "mod_assets/canonmc_assets/l.png")
image mc 4l1 = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/4.png", (0, 0), "mod_assets/canonmc_assets/l1.png")
image mc 4m = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/4.png", (0, 0), "mod_assets/canonmc_assets/m.png")
image mc 4n = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/4.png", (0, 0), "mod_assets/canonmc_assets/n.png")
image mc 4o = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/4.png", (0, 0), "mod_assets/canonmc_assets/o.png")
image mc 4p = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/4.png", (0, 0), "mod_assets/canonmc_assets/p.png")
image mc 4q = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/4.png", (0, 0), "mod_assets/canonmc_assets/q.png")
image mc 4r = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/4.png", (0, 0), "mod_assets/canonmc_assets/r.png")
image mc 4s = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/4.png", (0, 0), "mod_assets/canonmc_assets/s.png")
image mc 4t = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/4.png", (0, 0), "mod_assets/canonmc_assets/t.png")
image mc 4u = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/4.png", (0, 0), "mod_assets/canonmc_assets/u.png")
image mc 4v = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/4.png", (0, 0), "mod_assets/canonmc_assets/v.png")
image mc 4w = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/4.png", (0, 0), "mod_assets/canonmc_assets/w.png")
image mc 4x = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/4.png", (0, 0), "mod_assets/canonmc_assets/x.png")
image mc 4y = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/4.png", (0, 0), "mod_assets/canonmc_assets/y.png")
image mc 4z = im.Composite((960, 960), (0, 0), "mod_assets/canonmc_assets/4.png", (0, 0), "mod_assets/canonmc_assets/z.png")

## Character Variables
# This is where the characters are declared in the mod.
# To define a new character with assets, declare a character variable like in this example:
#   define e = DynamicCharacter('e_name', image='eileen', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
# To define a new character without assets, declare a character variable like this instead:
#   define en = Character('Eileen & Nat', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

define narrator = Character(ctc="ctc", ctc_position="fixed")
define mc = DynamicCharacter('player', image='mc', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define s = DynamicCharacter('s_name', image='sayori', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define m = DynamicCharacter('m_name', image='monika', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define n = DynamicCharacter('n_name', image='natsuki', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define y = DynamicCharacter('y_name', image='yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define ny = Character('Nat & Yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define r = DynamicCharacter('r_name', image='rikka', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define k = DynamicCharacter('k_name', image='kotonoha', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define w = DynamicCharacter('w_name', image='white', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

# This variable determines whether to allow the player to dismiss pauses.
# By default this is set by config.developer which is normally set to false
# once you packaged your mod.
define _dismiss_pause = config.developer

## [BETA] Pronoun Variables
# This section adds the feature to use player pronouns within the game text easily.
# To use this feature, simply ask the user for their pronoun and use it here.
# For capitalization, use heC, himC, areC and hesC
default persistent.he = ""
default persistent.him = ""
default persistent.are = ""
default persistent.hes = ""
default he = persistent.he
default him = persistent.him
default are = persistent.are
default hes = persistent.hes
default he_capital = he.capitalize()
default him_capital = him.capitalize()
default are_capital = are.capitalize()
default hes_capital = hes.capitalize()

## Extra Settings Variables
# This section controls whether the mod is censored or is in let's play mode.
default persistent.uncensored_mode = False
default persistent.lets_play = False

## Variables
# This section declares variables when the mod runs for the first time on all saves.
# To make a new persistent variable, make a new variable with the 'persistent.' in it's name
# like in this example:
#   default persistent.monika = 1
# To make a non-persistent variable, make a new variable like this instead:
#   default cookies = False
# To make sure a variable is set to a given condition use 'define' rather than 'default'.

default persistent.playername = ""
default player = persistent.playername
default persistent.whitename = ""
default w_name = persistent.whitename
default persistent.playthrough = 0
default persistent.yuri_kill = 0
default persistent.seen_eyes = None
default persistent.seen_sticker = None
default persistent.ghost_menu = None
default persistent.seen_ghost_menu = None
default seen_eyes_this_chapter = False
default persistent.anticheat = 0
default persistent.clear = [False, False, False, False, False, False, False, False, False, False]
default persistent.special_poems = None
default persistent.clearall = None
default persistent.menu_bg_m = None
default persistent.first_load = None
default persistent.first_poem = None
default persistent.seen_colors_poem = None
default persistent.monika_back = None
default persistent.CONDITION = 0

default in_sayori_kill = None
default in_yuri_kill = None
default anticheat = 0
define config.mouse = None
default allow_skipping = True
default basedir = config.basedir
default chapter = 0
default currentpos = 0
default faint_effect = None
default ch1_mk = False
default y_splash1 = False
default y_splash2 = False

# Default Name Variables
# To define a default name make a character name variable like in this example:
#   default e_name = "Eileen"

default s_name = "Sayori"
default m_name = "Monika"
default n_name = "Natsuki"
default y_name = "Yuri"
default r_name = "Rikka"
default k_name = "Kotonoha"

# Poem Variables
# This section records how much each character likes your poem in-game.
# Syntax:
#   -1 - Bad
#   0 - Neutral
#   1 - Good
# To add a new poem person, make a poem array like in this example:
#   default e_poemappeal = [0, 0, 0]

default n_poemappeal = [0, 0, 0]
default s_poemappeal = [0, 0, 0]
default y_poemappeal = [0, 0, 0]
default m_poemappeal = [0, 0, 0]
default r_poemappeal = [0, 0, 0]
default k_poemappeal = [0, 0, 0]
default w_poemappeal = [0, 0, 0]

# This variable keeps tracks on which person won the poem session after each day.
default poemwinner = ['sayori', 'sayori', 'sayori']

# These variables keep track on who has read your poem during poem sharing
default s_readpoem = False
default n_readpoem = False
default y_readpoem = False
default m_readpoem = False
default r_readpoem = False
default k_readpoem = False
default w_readpoem = False

# This variable keeps track on how many people have read your poem.
default poemsread = 0

# These variables store the appeal a character has to your poem
default n_appeal = 0
default s_appeal = 0
default y_appeal = 0
default m_appeal = 0
default r_appeal = 0
default k_appeal = 0
default w_appeal = 0

# These variables control if we have seen Natsuki's or Yuri's exclusive scenes
default n_exclusivewatched = False
default y_exclusivewatched = False

# These variables track whether we gave Yuri our poem in Act 2 and if she
# ran away during Act 2 poem sharing.
default y_gave = False
default y_ranaway = False

# These variables track whether we read Natsuki's or Yuri's 3rd poem in poem sharing.
default n_read3 = False
default y_read3 = False

# This variable tracks which person we sided with in Day 2 of the game.
default ch1_choice = "sayori"

# This variable tracks if we gave Natsuki our poem first during poem sharing.
default n_poemearly = False

# These variables track whether we tried to help Monika or Sayori during Day 3's ending.
default help_sayori = None
default help_monika = None

# These variables track which route Day 4 will play and who is their name.
default ch4_scene = "yuri"
default ch4_name = "Yuri"

# This variable tracks whether we accepted Sayori's confession or not.
default sayori_confess = True

# This variable tracks whether we read Natsuki's 3rd poem in Act 2.
default natsuki_23 = None

default kgmode = False