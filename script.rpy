define p = Character("Player")
define c = Character("Caller")
define m = Character("Manager")

define calls = [
    "Help, my computer imploded??",
    "The error message says my copy of Wingdows is not genuine.",
    "The Internet is slow, what causes that?",
    "Where's Internet Explorer?",
    "I can't get my email.",
    "I've been on hold for tech support since Tuesday.",
    "My keyboard is broken. It only types asterisks for passwords.",
    "COMPUTER'S BROKEN!",
    "The HD movie you sold me is 240p.",
    "I think my digital modem is broken.",
    "I lost my launch codes.",
    "My mouse doesn't work."
]

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

    $ current_call = renpy.random.randint(0, len(calls) - 1)
    jump get_response

label get_response:
    $ response = renpy.input(calls[current_call]).strip().lower()
    $ verb = response.partition(' ')[0]
    $ noun = response.partition(' ')[2]

    if renpy.has_label("verb_" + verb):
        $ renpy.jump("verb_" + verb)
    else:
        "What?"
        jump get_response