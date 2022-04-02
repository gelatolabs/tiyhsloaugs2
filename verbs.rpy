label verb_hang:
    if noun == "up":
        $ performance -= 1
        "*click*"
        jump call_loop

    "Hang what?"
    jump get_response

label verb_refer:
    if noun == "sales":
        $ performance += 1
        $ sanity -= 1
        p "Let me transfer you to our sales department."
        c "Wait-"
        "*click*"
        jump call_loop

    "Refer who?"
    jump get_response

label verb_blame:
    if noun == "user" or noun == "caller" or noun =="customer":
        $ performance -= 1
        p "Sorry, it seems your problem exists between the keyboard and chair. We don't solve that kind of problem here."
        c "Huh?"
        "*click*"
        jump call_loop

    "Blame who?"
    jump get_response

label verb_insult:
    if noun == "user" or noun == "caller" or noun =="customer":
        $ performance -= 1
        p "You smell."
        "*click*"
        jump call_loop

    "Insult who?"
    jump get_response

label verb_call:
    if noun in calls[current_call]["nouns"]:
        if noun == "fbi":
            $ performance += 1
            p "Thanks for letting us know. I'll give our friends at the FBI a call. Have a nice day!"
            "*click*"
            "*ring ring*"
            p "Hello, FBI?"
            p "We've got another one."
            jump call_loop

    "Call who?"
    jump get_response

label verb_install:
    if noun in calls[current_call]["nouns"]:
        if noun == "gelato":
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
            jump call_loop
        if noun == "aol":
            $ peformance += 1
            p "Sorry, we no longer support Internet Explorer. I'm going to need you to install AOL."
            c "Oh, great! I've always wanted an AOL. Thank you!"
            "*click*"
            jump call_loop
        if noun == "chrome":
            $ performance -= 1
            p "Sorry, we no longer support Internet Explorer. I'm going to need you to install Gargle Chrome."
            c "And let Gargle spy on me? I don't think so. I'm downloading Mozzarella."
            "*click*"
            p "...Mozzarella?"
            jump call_loop

    "Install what?"
    jump get_response

label verb_the:
    if noun in calls[current_call]["nouns"]:
        if noun == "garbage":
            $ performance += 1
            p "In the garbage, where it belongs."
            c "Well, okay. I guess I'll just stop using the Internet."
            p "That's probably for the best."
            c "Thanks for your help!"
            jump call_loop
        if noun == "start menu":
            $ performance -= 1
            p "It's in your start menu."
            c "Oh no. You're right."
            p "What?"
            c "I thought I had escaped."
            c "NOOOOOOOOOOOOOOOOOOOOOOO"
            "*click*"
            jump call_loop

    "The what?"
    jump get_response

label verb_reboot:
    if noun in calls[current_call]["nouns"]:
        if noun == "router":
            $ performance += 1
            p "Try rebooting your router."
            c "Do I look like I know what a router is?"
            p "The Internet box."
            c "Oh, why didn't you just say so?"
            c "Okay, it's restarting."
            "."
            ".."
            "..."
            ".."
            "."
            c "Wow, it worked! Thanks!"
            "*click*"
            jump call_loop

    "Reboot what?"
    jump get_response

label verb_lower:
    if noun in calls[current_call]["nouns"]:
        if noun == "standards":
            $ performance -= 1
            p "Have you tried lowering your standards?"
            c "I don't think they go low enough to put up with you."
            "*click*"
            jump call_loop
    
    "Lower what?"
    jump get_response