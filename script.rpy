define p = Character("Player")
define c = Character("Caller")
define m = Character("Manager")

define global_verbs = ["hang", "refer", "blame", "insult"]
define global_nouns = ["up", "sales", "customer"]
define calls = {
    "imploded": {
        "message": "Help, my computer imploded??",
        "verbs": ["reboot", "replace", "go"],
        "nouns": ["mainframe", "floppy drive", "outside"]
    },
    "genuine": {
        "message": "The error message says my copy of Wingdows is not genuine.",
        "verbs": ["call", "install", "uninstall", "purchase"],
        "nouns": ["fbi", "gelato", "windows"]
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
default sanity = 4
default performance = 0
default strikes = 0

label start:
    scene bg office
    show player saner at left
    show manager normal at right

    m "Welcome to MegaCorp Industries!"
    m "As our newest Customer Synergy Specialist, you'll be answering the phones and providing the quality technical support MegaCorp is known for."
    m "This is your new best friend: your phone. Protect it with your life."
    m "When it rings, pick it up and listen to the customer's problem. Then all you have to do is fix it!"
    m "Our automagical tech support AI will suggest some possible solutions you can try. So convenient!"
    m "But be careful, some of them are wrong."
    m "Choose the right solution, and the customer might just be satisfied."
    m "As a last resort, you can always just refer the customer to our sales department. Because why fix something when you can just buy another one?"
    m "This will make us happy, but it might make you feel bad. Your call."
    m "After the call, the customer will rate your service, and each day I'll give you a performance review based on their feedback."
    m "Three bad performance reviews and you're fired. And as you know, MegaCorp is the OnlyCorp™. So when, err, {i}if{/i} you're fired, you will be forever unemployable and you will probably die alone on the streets."
    m "Hey, no pressure, but so far 100\% of our Customer Synergy Specialists have met the same fate."
    m "But we'll see how long you can {i}delay the inevitable!{/i}"

    hide manager
    jump call_loop

label call_loop:
    $ call_count += 1
    if call_count % 10 == 0:
        jump performance_review

    "*ring ring*"
    call updateSanity(-1)
    if sanity >= 3:
        p "Thank you for calling MegaCorp, how can I help you today?"
    else:
        p "Thank you for calling MegaCorp, how can I harm you today?"

    $ current_call = renpy.random.choice(list(calls))
    jump get_response

label get_response:
    $ response = renpy.input(calls[current_call]["message"]).strip().lower()
    $ verb = response.partition(' ')[0]
    $ noun = response.partition(' ')[2]

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
        m "Your performance today was terrible!"
        $ strikes += 1
        if strikes < 2:
            m "Keep this up and you'll be fired. Get it together."
        elif strikes == 2:
            m "If this happens one more time, you're fired. Get it together."
        else:
            m "Three strikes aaaand you're fired. Get out of my sight."
            hide manager
            jump game_over

    $ performance = 0
    hide manager
    jump call_loop

label game_over:
    show player drinking at left
    "GAME OVER"
    return