define p = Character("[pname]", color="#6c0")
define c = Character("Caller", color="#cc0")
define m = Character("Manager", color="#c06")

define global_verbs = ["hang", "refer", "blame", "insult"]
define global_nouns = ["up", "sales", "customer"]
define calls = {
    "imploded": {
        "message": "Help, my computer imploded??",
        "verbs": ["reboot", "replace", "go"],
        "nouns": ["mainframe", "floppy drive", "outside", "cable"]
    },
    "genuine": {
        "message": "The error message says my copy of Wingdows is not genuine.",
        "verbs": ["call", "install", "uninstall", "purchase"],
        "nouns": ["fbi", "gelato", "wingdows"]
    },
    "slownet": {
        "message": "The Internet is slow, what causes that?",
        "verbs": ["reboot", "cancel", "destroy", "disconnect"],
        "nouns": ["router", "internet", "computer", "time machine"]
    },
    "explorer": {
        "message": "Where's Internet Explorer?",
        "verbs": ["install", "the"],
        "nouns": ["aol", "chrome", "garbage", "start menu"]
    },
    "email": {
        "message": "I can't get my email.",
        "verbs": ["look", "reinstall", "brighten", "ask", "reset"],
        "nouns": ["harder", "outlook", "post office", "password"]
    },
    "hold": {
        "message": "I've been on hold for tech support since Tuesday.",
        "verbs": ["wait", "please", "be"],
        "nouns": ["longer", "hold", "patient"]
    },
    "password": {
        "message": "My keyboard is broken. It only types asterisks for passwords.",
        "verbs": ["change", "reboot", "defrag", "unplug"],
        "nouns": ["password", "computer", "hard drive", "keyboard"]
    },
    "broken": {
        "message": "COMPUTER'S BROKEN!",
        "verbs": ["clear", "try", "reboot", "microwave"],
        "nouns": ["cache", "again", "computer", "microwave"]
    },
    "movie": {
        "message": "The HD movie you sold me is 240p.",
        "verbs": ["lower", "raise", "reboot", "rewind", "wear"],
        "nouns": ["standards", "dvd player", "tv", "movie", "glasses"]
    },
    "modem": {
        "message": "I think my digital modem is broken.",
        "verbs": ["reboot"],
        "nouns": ["modem", "router", "computer", "refrigerator", "internet", "mainframe", "cellphone", "tablet", "yourself", "internet explorer", "network switch", "firewall", "server"]
    },
    "launchcodes": {
        "message": "I lost my launch codes.",
        "verbs": ["change", "run", "defrag", "reboot"],
        "nouns": ["codes", "away", "hard drive", "nukes"]
    },
    "mouse": {
        "message": "My mouse doesn't work.",
        "verbs": ["enable", "plug", "install", "restart"],
        "nouns": ["mouse keys", "in", "adobe", "computer", "modem"]
    }
}

default call_count = 0
default sanity = 5
default performance = 0
default strikes = 0
default countdown = 300
default countdown_range = 300

default input_value = ""

init python:
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
    scene bg office

    $ renpy.input("Who are you?")
    $ pname = input_value

    show player saner at left
    show manager normal at right

    m "Welcome to MegaCorp Industries, [pname]!"
    m "As our newest Customer Synergy Specialist, you'll be answering the phones and providing the quality technical support MegaCorp is known for."
    m "This is your new best friend: your phone. Protect it with your life."
    m "When it rings, pick it up and listen to the customer's problem. Then all you have to do is fix it!"
    m "Keep your responses simple. A {color=#09f}verb{/color} and a {color=#c00}noun{/color} will do. Don't want to confuse the customer."
    m "Our automagical tech support AI will suggest some possible solutions you can try. So convenient!"
    m "But be careful, some of them are wrong."
    m "Choose the right solution, and the customer might just be satisfied."
    m "As a last resort, you can always just {color=09f}refer{/color} the customer to our {color=#c00}sales{/color} department. Because why fix something when you can just buy another one?"
    m "This will make us happy, but it might make you feel bad. Your call."
    m "MegaCorp prides itself in its efficiency. That's why you have a time limit to complete each call in before it's automatically disconnected for your convenience."
    m "As we strive for perfection through continual improvement, this time limit will decrease each day. So never stop improving!"
    m "At the end of each day, I'll give you a performance review based on customer feedback."
    m "Three bad performance reviews and you're fired. And as you know, MegaCorp is the OnlyCorp. So when, err, {i}if{/i} you're fired, you will be forever unemployable and you will probably die alone on the streets."
    m "Hey, no pressure, but so far 100\% of our Customer Synergy Specialists have met the same fate."
    m "But we'll see how long you can {i}delay the inevitable!{/i}"

    hide manager
    jump call_loop

label call_loop:
    hide screen countdown
    hide words
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
        "*click*"
    if call_count % 9 == 8:
        jump performance_review

    show text "{size=72}*ring ring*{/size}" at text_shake
    "..."
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
        for verb in calls[current_call]["verbs"] + global_verbs:
            renpy.random.seed(verb)
            wordSprites.append(words.create(Text(verb, size=64, color="#09f", outlines=[ (absolute(1), "#000", absolute(0), absolute(0)) ])))
            wordDirection.append(renpy.random.choice(["L", "R", "U", "D", "UL", "UR", "DL", "DR"]))
        for noun in calls[current_call]["nouns"] + global_nouns:
            renpy.random.seed(noun)
            wordSprites.append(words.create(Text(noun, size=64, color="#c00", outlines=[ (absolute(1), "#000", absolute(0), absolute(0)) ])))
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
     
    if renpy.has_label("verb_" + verb) and verb in calls[current_call]["verbs"] and noun in calls[current_call]["nouns"] or verb in global_verbs:
        $ renpy.jump("verb_" + verb)
    else:
        jump bad_answer

label updateSanity(change):
    $ sanity += change
    if sanity >= 4:
        show player saner at left
    elif sanity >= 3:
        show player sane at left
    elif sanity >= 2:
        show player insane at left
    else:
        show player insaner at left
        if sanity <= 0:
            "Your blood begins to boil as your grasp on the sane world slips away."
            "Closing your eyes provides no relief as the voices of unhappy customers echo in your mind."
            "Erupting in a manical laughter, you somehow manage to squeal out the words."
            p "I QUEEEEEEEEEEEEEEEET!"
            jump game_over
    return

label performance_review:
    show manager normal at right
    m "Time for your performance review! Let's see..."
    
    if performance >= 3:
        show manager happy at right
        m "Your performance today was excellent! Keep up the good work. But don't get too comfortable!"
        m "After all, your failure is inevitable."
    elif performance >= -2:
        m "Your performance today was okay. But remember, our expectations rise every day. I trust you'll do better tomorrow."
    else:
        show manager angry at right
        $ strikes += 1
        if strikes < 2:
            m "Your performance today was terrible!"
            m "Keep this up and you'll be fired. Get it together."
        elif strikes == 2:
            m "Your performance today was terrible!"
            m "If this happens one more time, you're fired. Get it together."
        else:
            m "Nice work, that was an absolutely stellar performance! This type of dedication and team spirit is precisely what we're looking for here at MegaCorp Industries."
            m "We're happy to offer you a promotion, raise, and best of all a reserved parking space!"
            m "April Fool's genius - you're fired!"
            hide manager
            jump game_over

    $ performance = 0
    hide manager
    jump call_loop

label game_over:
    show player drinking at left
    "Our underpaid hero's brief foray into the glorious world of customer support has come to a bitter end."
    "It's time to be reunited with a couple of old friends who have always been there during times like this - Jack and Daniels."
    "You survived [call_count] calls."
    "GAME OVER"
    $ renpy.quit()
