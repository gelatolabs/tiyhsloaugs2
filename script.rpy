define p = Character("Player")
define c = Character("Caller")
define m = Character("Manager")

default sanity = 1

label start:
    scene bg office
    show player sane

    m "Welcome to MegaCorp Industries!"
    p "oh no"

    jump call_start

    return

label call_start:
    if sanity > 0:
        p "Thank you for calling MegaCorp, how can I help you today?"
    else:
        p "Thank you for calling MegaCorp, how can I harm you today?"

    $ renpy.jump("call_" + str(renpy.random.randint(0, 11)))

    return

label call_0:
    c "Help, my computer imploded??"
    return

label call_1:
    c "The error message says my copy of Wingdows is not genuine."
    return

label call_2:
    c "The Internet is slow, what causes that?"
    return

label call_3:
    c "Where's Internet Explorer?"
    return

label call_4:
    c "I can't get my email."
    return

label call_5:
    c "I've been on hold for tech support since Tuesday."
    return

label call_6:
    c "My keyboard is broken. It only types asterisks for passwords."
    return

label call_7:
    c "COMPUTER'S BROKEN!"
    return

label call_8:
    c "The HD movie you sold me is 240p."
    return

label call_9:
    c "I think my digital modem is broken."
    return

label call_10:
    c "I lost my launch codes."
    return

label call_11:
    c "My mouse doesn't work."
    return
