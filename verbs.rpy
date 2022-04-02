label verb_hang:
    if noun == "up":
        $ performance -= 1
        "*click*"
    else:
        "Hang what?"
        jump get_response
    jump call_loop

label verb_refer:
    if noun == "sales":
        $ performance += 1
        $ sanity -= 1
        p "Let me transfer you to our sales department."
        c "Wait-"
        "*click*"
    else:
        "Refer who?"
        jump get_response
    jump call_loop

label verb_blame:
    if noun == "user" or noun == "caller" or noun =="customer":
        $ performance -= 1
        p "Sorry, it seems your problem exists between the keyboard and chair. We don't solve that kind of problem here."
        c "Huh?"
        "*click*"
    else:
        "Blame who?"
        jump get_response
    jump call_loop

label verb_insult:
    if noun == "user" or noun == "caller" or noun =="customer":
        $ performance -= 1
        p "You smell."
        "*click*"
    else:
        "Insult who?"
        jump get_response
    jump call_loop

label verb_call:
    if noun == "fbi" and current_call == 1:
        $ performance += 1
        p "Thanks for letting us know. I'll give our friends at the FBI a call. Have a nice day!"
        "*click*"
        "*ring ring*"
        p "Hello, FBI?"
        p "We've got another one."
    else:
        "Call who?"
        jump get_response
    jump call_loop

label verb_install:
    if noun == "gelato" and current_call == 1:
        $ performance -= 1
        p "Install Gelato."
        c "What's that?"
        p "The Gelato System is a free operating system from Gelato Labs."
        c "Where can I get it?"
        p "https://2k38.gelatolabs.xyz/"
        c "Okay, let me give it a try."
        "."
        ".."
        "..."
        ".."
        "."
        c "What the hell is this? Give me my Wingdows back!"
        p "Sorry, this is a one-way install."
        "*click*"
    else:
        "Install what?"
        jump get_response
    jump call_loop
