define p = Character("Player")
define c = Character("Caller")
define m = Character("Manager")

define global_verbs = ["hang", "refer", "blame", "insult"]
define calls = {
    "imploded": {
        "message": "Help, my computer imploded??",
        "verbs": [],
        "nouns": []
    },
    "genuine": {
        "message": "The error message says my copy of Wingdows is not genuine.",
        "verbs": ["call", "install"],
        "nouns": ["fbi", "gelato"]
    },
    "slownet": {
        "message": "The Internet is slow, what causes that?",
        "verbs": [],
        "nouns": []
    },
    "explorer": {
        "message": "Where's Internet Explorer?",
        "verbs": [],
        "nouns": []
    },
    "email": {
        "message": "I can't get my email.",
        "verbs": [],
        "nouns": []
    },
    "hold": {
        "message": "I've been on hold for tech support since Tuesday.",
        "verbs": [],
        "nouns": []
    },
    "password": {
        "message": "My keyboard is broken. It only types asterisks for passwords.",
        "verbs": [],
        "nouns": []
    },
    "broken": {
        "message": "COMPUTER'S BROKEN!",
        "verbs": [],
        "nouns": []
    },
    "movie": {
        "message": "The HD movie you sold me is 240p.",
        "verbs": [],
        "nouns": []
    },
    "modem": {
        "message": "I think my digital modem is broken.",
        "verbs": [],
        "nouns": []
    },
    "launchcodes": {
        "message": "I lost my launch codes.",
        "verbs": [],
        "nouns": []
    },
    "mouse": {
        "message": "My mouse doesn't work.",
        "verbs": [],
        "nouns": []
    }
}

default sanity = 1
default performance = 0

label start:
    scene bg office
    show player sane

    m "Welcome to MegaCorp Industries!"

    jump call_loop

label call_loop:
    "*ring ring*"
    if sanity > 0:
        p "Thank you for calling MegaCorp, how can I help you today?"
    else:
        p "Thank you for calling MegaCorp, how can I harm you today?"

    $ current_call = renpy.random.choice(list(calls))
    jump get_response

label get_response:
    $ response = renpy.input(calls[current_call]["message"]).strip().lower()
    $ verb = response.partition(' ')[0]
    $ noun = response.partition(' ')[2]

    if verb in calls[current_call]["verbs"] or verb in global_verbs:
        $ renpy.jump("verb_" + verb)
    else:
        "What?"
        jump get_response