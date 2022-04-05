define p = Character("[pname]", color="#6c0")
define c = Character("Caller", color="#cc0")
define m = Character("Manager", color="#c06")

define audio.music = "audio/music.mp3"
define audio.musicfast = "audio/music-fast.mp3"
define audio.musicfaster = "audio/music-faster.mp3"
define audio.menumusic = "audio.menumusic.mp3"
define audio.chatter = "audio/chatter.mp3"
define audio.goodcall = "audio/goodcall.mp3"
define audio.badcall = "audio/badcall.mp3"
define audio.invalidcall = "audio/invalidcall.mp3"
define audio.goodeval = "audio/goodeval.mp3"
define audio.badeval = "audio/badeval.mp3"
define audio.okayeval = "audio/okayeval.mp3"
define audio.gameover = "audio/gameover.mp3"
define audio.drinking = "audio/drinking.mp3"
define audio.ringtone1 = "audio/ringtone1.mp3"
define audio.ringtone2 = "audio/ringtone2.mp3"
define audio.ringtone3 = "audio/ringtone3.mp3"
define audio.ringtone4 = "audio/ringtone4.mp3"
define audio.hangup = "audio/hangup.mp3"

define audio.manager1 = "audio/voices/1.mp3"
define audio.manager2 = "audio/voices/2.mp3"
define audio.manager3 = "audio/voices/3.mp3"
define audio.manager4 = "audio/voices/4.mp3"
define audio.manager5 = "audio/voices/5.mp3"
define audio.manager6 = "audio/voices/6.mp3"
define audio.manager7 = "audio/voices/7.mp3"
define audio.manager8 = "audio/voices/8.mp3"
define audio.manager9 = "audio/voices/9.mp3"
define audio.manager10 = "audio/voices/10.mp3"
define audio.manager11 = "audio/voices/11.mp3"
define audio.manager12 = "audio/voices/12.mp3"
define audio.manager13 = "audio/voices/13.mp3"
define audio.manager14 = "audio/voices/14.mp3"
define audio.manager15 = "audio/voices/15.mp3"
define audio.manager16 = "audio/voices/16.mp3"
define audio.perf = "audio/voices/perf.mp3"
define audio.goodperf1 = "audio/voices/goodperf1.mp3"
define audio.goodperf2 = "audio/voices/goodperf2.mp3"
define audio.okayperf = "audio/voices/okayperf.mp3"
define audio.badperf1 = "audio/voices/badperf1.mp3"
define audio.badperf2 = "audio/voices/badperf2.mp3"
define audio.badperf3 = "audio/voices/badperf3.mp3"
define audio.badperf4 = "audio/voices/badperf4.mp3"
define audio.badperf5 = "audio/voices/badperf5.mp3"
define audio.badperf6 = "audio/voices/badperf6.mp3"

define global_verbs = ["refer", "insult"]
define global_nouns = ["sales", "customer"]
define calls = {
    "imploded": {
        "message": "Help, my computer imploded??",
        "verbs": ["reboot", "replace", "go"],
        "nouns": ["mainframe", "outside", "cable"]
    },
    "genuine": {
        "message": "The error message says my copy of Wingdows is not genuine.",
        "verbs": ["call", "install", "purchase"],
        "nouns": ["fbi", "gelato", "wingdows"]
    },
    "slownet": {
        "message": "The Internet is slow, what causes that?",
        "verbs": ["reboot", "destroy"],
        "nouns": ["router", "computer", "time machine"]
    },
    "explorer": {
        "message": "Where's Internet Expeller?",
        "verbs": ["install", "the"],
        "nouns": ["aol", "chrome", "garbage", "fart menu"]
    },
    "email": {
        "message": "I can't get my email.",
        "verbs": ["look", "reinstall", "ask"],
        "nouns": ["harder", "outlook", "post office"]
    },
    "hold": {
        "message": "I've been on hold for tech support since Tuesday.",
        "verbs": ["wait", "please", "be"],
        "nouns": ["longer", "hold", "patient"]
    },
    "password": {
        "message": "My keyboard is broken. It only types asterisks for passwords.",
        "verbs": ["change", "reboot", "unplug"],
        "nouns": ["password", "computer", "hard drive", "keyboard"]
    },
    "broken": {
        "message": "COMPUTER'S BROKEN!",
        "verbs": ["clear", "try", "reboot", "microwave"],
        "nouns": ["cache", "again", "computer"]
    },
    "movie": {
        "message": "The HD movie you sold me is 240p.",
        "verbs": ["lower", "raise", "wear", "return"],
        "nouns": ["standards", "glasses", "movie"]
    },
    "modem": {
        "message": "I think my digital modem is broken.",
        "verbs": ["reboot"],
        "nouns": ["modem", "router", "computer", "refrigerator", "cellphone", "yourself", "server"]
    },
    "launchcodes": {
        "message": "I lost my launch codes.",
        "verbs": ["change", "run", "defrag"],
        "nouns": ["codes", "away", "hard drive"]
    },
    "mouse": {
        "message": "My mouse doesn't work.",
        "verbs": ["enable", "plug", "reboot"],
        "nouns": ["mouse keys", "in", "computer", "modem"]
    },
    "printer": {
        "message": "My printer won't print.",
        "verbs": ["install", "replace", "enable"],
        "nouns": ["drivers", "ink", "wifi"]
    }
}

default ringtone = 1
default call_count = 0
default sanity = 5
default performance = 0
default strikes = 0
default countdown = 300
default countdown_range = 300

default input_value = ""

init python:
    renpy.music.register_channel("chatter", "sfx", True)

    def Typing(what):
        global input_value
        renpy.music.play("audio/keytap-0"+str(renpy.random.randint(1,5))+".mp3", channel="audio")
        input_value = what

    def wordMove(st):
        num = 0
        for i in wordSprites:  
            # renpy why you no use python 3.10, i want switch/case :(
            if (wordDirection[num] == "U"):
                i.y -= 1
            elif (wordDirection[num] == "D"):
                i.y += 1
            elif (wordDirection[num] == "L"):
                i.x -= 1
            elif (wordDirection[num] == "R"):
                i.x += 1
            elif (wordDirection[num] == "UL"):
                i.y -= 1
                i.x -= 1
            elif (wordDirection[num] == "UR"):
                i.y -= 1
                i.x += 1
            elif (wordDirection[num] == "DL"):
                i.y += 1
                i.x -= 1
            elif (wordDirection[num] == "DR"):
                i.y += 1
                i.x += 1
            
            if i.x > 1920:
                wordDirection[num] = wordDirection[num].replace("R", "L")
            if i.x < 0:
                wordDirection[num] = wordDirection[num].replace("L", "R")
            if i.y > 752:
                wordDirection[num] = wordDirection[num].replace("D", "U")
            if i.y < 27:
                wordDirection[num] = wordDirection[num].replace("U", "D")
            num += 1
        return 0.03        

transform text_shake:
    parallel:
        block:
            linear 0.1 xoffset -2 yoffset 2 
            linear 0.1 xoffset 3 yoffset -3 
            linear 0.1 xoffset 2 yoffset -2
            linear 0.1 xoffset -3 yoffset 3
            linear 0.1 xoffset 0 yoffset 0
            repeat
    parallel:
        block:
            alpha .2
            linear 1.0 alpha .9
            linear 1.0 alpha .2
            repeat    

label start:
    play chatter chatter volume 0.2
    stop music fadeout 2
    scene bg "#b1b1b1"
    image smoothoffice = "images/bg office.png"
    show smoothoffice:
        alpha 0.2 xalign 0.5 yalign 0.5 zoom 1.2
        ease 1.0 alpha 1.0 zoom 1.0
    #scene bg office
    #hide office

    $ renpy.input("Who are you?")
    $ pname = input_value

    show player saner at left with Dissolve(0.5, alpha=True)
    show manager normal at right with Dissolve(0.5, alpha=True)

    voice manager1
    m "Welcome to MegaCorp Industries, [pname]!"
    voice manager2
    m "As our newest Customer Synergy Specialist, you'll be answering the phones and providing the quality technical support MegaCorp is known for."
    voice manager3
    m "This is your new best friend: your phone. Protect it with your life."
    jump choose_ringtone

label choose_ringtone:
    menu:
        "Choose a ringtone for your phone!"
        "School Day":
            play sound ringtone1
            menu:
                "Use this ringtone?"
                "Confirm":
                    stop sound fadeout 1
                    $ ringtone = 1
                    jump continue_intro
                "Back":
                    jump choose_ringtone
        "Chime Time":
            play sound ringtone2
            menu:
                "Use this ringtone?"
                "Confirm":
                    stop sound fadeout 1
                    $ ringtone = 2
                    jump continue_intro
                "Back":
                    jump choose_ringtone
        "Game Boing":
            play sound ringtone3
            menu:
                "Use this ringtone?"
                "Confirm":
                    stop sound fadeout 1
                    $ ringtone = 3
                    jump continue_intro
                "Back":
                    jump choose_ringtone
        "Over The Horizon":
            play sound ringtone4
            menu:
                "Use this ringtone?"
                "Confirm":
                    stop sound fadeout 1
                    $ ringtone = 4
                    jump continue_intro
                "Back":
                    jump choose_ringtone

label continue_intro:
    voice manager4
    m "When it rings, pick it up and listen to the customer's problem. Then all you have to do is fix it!"
    voice manager5
    m "Keep your responses simple. A {color=#09f}verb{/color} and a {color=#c00}noun{/color} will do. Don't want to confuse the customer."
    voice manager6
    m "Our automagical tech support AI will suggest some possible solutions you can try. So convenient!"
    voice manager7
    m "But be careful, some of them are wrong."
    voice manager8
    m "Choose the right solution, and the customer might just be satisfied."
    voice manager9
    m "As a last resort, you can always just {color=09f}refer{/color} the customer to our {color=#c00}sales{/color} department. Because why fix something when you can just buy another one?"
    voice manager10
    m "This will make us happy, but it might make you feel bad. Your call."
    voice manager11
    m "MegaCorp prides itself in its efficiency. That's why you have a time limit to complete each call in before it's automatically disconnected for your convenience."
    voice manager12
    m "As we strive for perfection through continual improvement, this time limit will decrease each day. So never stop improving!"
    voice manager13
    m "At the end of each day, I'll give you a performance review based on customer feedback."
    voice manager14
    m "Three bad performance reviews and you're fired. And as you know, MegaCorp is the OnlyCorp. So when, err, {i}if{/i} you're fired, you will be forever unemployable and you will probably die alone on the streets."
    voice manager15
    m "Hey, no pressure, but so far 100\% of our Customer Synergy Specialists have met the same fate."
    voice manager16
    m "But we'll see how long you can {i}delay the inevitable!{/i}"

    hide manager with Dissolve(0.5, alpha=True)
    play music music fadein 2.0
    jump call_loop

label call_loop:
    hide screen countdown with Dissolve(0.5, alpha=True)
    hide words with Dissolve(0.5, alpha=True)
    python:
        try:
            del words
            del wordSprites
            del wordDirection
        except:
            # this may be the first call loop, in which case the word sprites do not exist
            pass

    $ call_count += 1
    if call_count > 1 and call_count % 9 != 0:
        play sound hangup
        "*click*"
    if call_count % 9 == 8:
        jump performance_review

    window hide
    $ renpy.pause(renpy.random.randint(2,10), hard=True)
    $ renpy.play("audio/ringtone" + str(ringtone) + ".mp3", channel="sound")
    show text "{size=72}*ring ring*{/size}" at text_shake
    "..."
    stop sound
    window show
    hide text

    $ countdown_range = 130 - (call_count // 9 + 1) * 10
    $ countdown = countdown_range
    show screen countdown

    call updateSanity(-0.1)
    if sanity >= 3:
        p "Thank you for calling MegaCorp, how can I help you today?"
    else:
        p "Thank you for calling MegaCorp, how can I harm you today?"

    $ current_call = renpy.random.choice(list(calls))
    python:
        words = SpriteManager(update=wordMove)
        wordSprites = []
        wordDirection = []
        for verb in calls[current_call]["verbs"]:
            renpy.random.seed(verb)
            wordSprites.append(words.create(Text(verb, size=64, color="#09f", outlines=[ (absolute(1), "#000", absolute(0), absolute(0)) ])))
            wordDirection.append(renpy.random.choice(["L", "R", "U", "D", "UL", "UR", "DL", "DR"]))
        for verb in global_verbs:
            renpy.random.seed(verb)
            wordSprites.append(words.create(Text(verb, size=64, color="#036", outlines=[ (absolute(1), "#000", absolute(0), absolute(0)) ])))
            wordDirection.append(renpy.random.choice(["L", "R", "U", "D", "UL", "UR", "DL", "DR"]))
        for noun in calls[current_call]["nouns"]:
            renpy.random.seed(noun)
            wordSprites.append(words.create(Text(noun, size=64, color="#c00", outlines=[ (absolute(1), "#000", absolute(0), absolute(0)) ])))
            wordDirection.append(renpy.random.choice(["L", "R", "U", "D", "UL", "UR", "DL", "DR"]))
        for noun in global_nouns:
            renpy.random.seed(noun)
            wordSprites.append(words.create(Text(noun, size=64, color="#900", outlines=[ (absolute(1), "#000", absolute(0), absolute(0)) ])))
            wordDirection.append(renpy.random.choice(["L", "R", "U", "D", "UL", "UR", "DL", "DR"]))
        for i in wordSprites:
            i.x = renpy.random.randint(300, 1620)
            i.y = renpy.random.randint(100, 752)
    jump get_response

label get_response:
    show expression words as words  
    python:
        input_value = ""
        renpy.input(calls[current_call]["message"]) 
        response = input_value.strip().lower()
        verb = response.partition(' ')[0]
        noun = response.partition(' ')[2]
     
    if verb in calls[current_call]["verbs"] and noun in calls[current_call]["nouns"] or verb in global_verbs:
        if renpy.has_label("verb_" + verb):
            $ renpy.jump("verb_" + verb)
        else:
            jump bad_answer
    else:
        play sound invalidcall
        c "Huh, what are you saying? I couldn't understand you."
        jump get_response

label updatePerformance(change):
    $ performance += change
    if change == 1:
        play sound goodcall
    elif change == -1:
        play sound badcall
    elif change == -0.2:
        play sound invalidcall
    return

label updateSanity(change):
    $ sanity += change
    if sanity >= 4:
        if renpy.music.get_playing() != "audio/music.mp3":
            play music music
        show player saner at left
    elif sanity >= 3:
        if renpy.music.get_playing() != "audio/music.mp3":
            play music music
        show player sane at left
    elif sanity >= 2:
        if renpy.music.get_playing() != "audio/music-fast.mp3":
            play music musicfast
        show player insane at left
    else:
        if renpy.music.get_playing() != "audio/music-faster.mp3":
            play music musicfaster
        show player insaner at left
        if sanity <= 0:
            hide screen countdown with Dissolve(0.5, alpha=True)
            "Your blood begins to boil as your grasp on the sane world slips away."
            "Closing your eyes provides no relief as the voices of unhappy customers echo in your mind."
            "Erupting in a manical laughter, you somehow manage to squeal out the words."
            p "I QUEEEEEEEEEEEEEEEET!"
            jump game_over
    return

label performance_review:
    show manager normal at right with Dissolve(0.5, alpha=True)
    stop music fadeout 1.0
    voice perf
    m "Time for your performance review! Let's see..."
    
    if performance >= 3:
        show manager happy at right
        play sound goodeval
        voice goodperf1
        m "Your performance today was excellent! Keep up the good work. But don't get too comfortable!"
        voice goodperf2
        m "After all, your failure is inevitable."
    elif performance >= -2:
        play sound okayeval
        voice okayperf
        m "Your performance today was okay. But remember, our expectations rise every day. I trust you'll do better tomorrow."
    else:
        show manager angry at right
        play sound badeval
        $ strikes += 1
        if strikes < 2:
            voice badperf1
            m "Your performance today was terrible!"
            voice badperf2
            m "Keep this up and you'll be fired. Get it together."
        elif strikes == 2:
            voice badperf1
            m "Your performance today was terrible!"
            voice badperf3
            m "If this happens one more time, you're fired. Get it together."
        else:
            voice badperf4
            m "Nice work, that was an absolutely stellar performance! This type of dedication and team spirit is precisely what we're looking for here at MegaCorp Industries."
            voice badperf5
            m "We're happy to offer you a promotion, raise, and best of all a reserved parking space!"
            voice badperf6
            m "April Fool's genius - you're fired!"
            hide manager
            jump game_over

    $ performance = 0
    hide manager fadeout 1.0
    call updateSanity(0) # hacky way of restarting the correct music track
    jump call_loop

label game_over:
    stop chatter fadeout 1
    play music gameover
    play sound drinking
    scene black
    show player drinking at left
    "Our underpaid hero's brief foray into the glorious world of customer support has come to a bitter end."
    "It's time to be reunited with a couple of old friends who have always been there during times like this - Jack and Daniels."
    "You survived [call_count] calls."
    "GAME OVER"
    $ renpy.quit()
