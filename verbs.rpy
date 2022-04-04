label verb_hang:
    if noun == "up":
        $ performance -= 1
        jump call_loop
    jump bad_answer

label verb_refer:
    if noun == "sales":
        p "Let me transfer you to our sales department."
        c "Wait-"
        $ performance += 1
        call updateSanity(-0.25)
        jump call_loop
    jump bad_answer

label verb_blame:
    if noun == "user" or noun == "caller" or noun =="customer":
        p "Sorry, it seems your problem exists between the keyboard and chair. We don't solve that kind of problem here."
        c "Huh?"
        $ performance -= 1
        jump call_loop
    jump bad_answer

label verb_insult:
    if noun == "user" or noun == "caller" or noun =="customer":
        p "You smell."
        c "Excuse me?"
        $ performance -= 1
        jump call_loop
    jump bad_answer

label verb_call:
    if noun == "fbi":
        p "Could you please hold for a moment? I forgot to turn off my refrigerator."
        c "Sure thing."
        "*you put the customer on hold and call the FBI*"
        p "Hello, is this FBI?"
        "FBI" "Special agent Halfbaked speaking, state your issue civilian."
        p "I'd like to report an act of piracy."
        "FBI" "Are you kidding me, call the coastguard you numbskull!"
        "The FBI Agent hangs up. Oh well, it was worth a try."
        p "We appear to be having technical difficulties at this moment, please call again later."
        $ performance -= 1
        jump call_loop
    jump bad_answer

label verb_install:
    if noun == "gelato":
        p "Install Gelato."
        c "What's that?"
        p "The Gelato System is a free operating system from Gelato Labs."
        c "Where can I get it?"
        p "{a=https://2k38.gelatolabs.xyz/}https://2k38.gelatolabs.xyz/{/a}"
        c "Okay, let me give it a try."
        "."
        ".."
        "..."
        ".."
        "."
        c "What the hell is this? Give me my Wingdows back!"
        p "Sorry, this is a one-way install."
        $ performance -= 1
        jump call_loop
    elif noun == "aol":
        p "Sorry, we no longer support Internet Explorer. I'm going to need you to install AOL."
        c "Oh, great! I've always wanted an AOL. Thank you!"
        $ performance += 1
        jump call_loop
    elif noun == "chrome":
        p "Sorry, we no longer support Internet Explorer. I'm going to need you to install Gargle Chrome."
        c "And let Gargle spy on me? I don't think so. I'm downloading Mozzarella."
        $ performance -= 1
        jump call_loop
    jump bad_answer

label verb_the:
    if noun == "garbage":
        p "In the garbage, where it belongs."
        c "Well, okay. I guess I'll just stop using the Internet."
        p "That's probably for the best."
        c "Thanks for your help!"
        $ performance += 1
        jump call_loop
    elif noun == "start menu":
        p "It's in your start menu."
        c "Oh no. You're right."
        p "What?"
        c "I thought I had escaped."
        c "NOOOOOOOOOOOOOOOOOOOOOOO"
        $ performance -= 1
        jump call_loop
    jump bad_answer

label verb_reboot:
    if noun == "router":
        p "Have you rebooted your router lately?"
        c "What is a router?"
        p "It's a little box that empowers you with the ability to explore the world wide web."
        c "What does it look like?"
        p "Just look for a little box with cables going to the wall."
        c "Ok found it, now what do I do?"
        p "Unplug it."
        c "Everything just went dark, I'm scared."
        p "Don't panic, you just unplugged the lamp. Plug it back in."
        c "There we go, found it!"
        p "Great, now wait for 30 seconds then plug it back in."
        "."
        ".."
        "..."
        ".."
        "."
        c "Ok I'm back!"
        p "What the heck took you so long??"
        c "Just like you said, wait 30 minutes..."
        p "Wow, does your internet work now??"
        c "It's blazing fast now, I've been streaming my favourite show Love at first bite for the past 30 minutes.  Thank you!!"
        $ performance += 1
        jump call_loop
    elif noun == "mainframe":
        p "Could be a frozen Wingdows Update, let's reboot the mainframe."
        c "There's no pictures near the computer."
        p "No, the mainframe is another word for the computer."
        c "Ohh I get it, so I have to reboot the computer?"
        p "Precisely."
        c "What size boots does it wear?"
        p "Sighs, just press the power button twice."
        c "Wow that did it, you are a genius."
        p "Have a good life."
        $ performance += 1
        jump call_loop
    elif noun == "time machine":
        p "Do you happen to have a hot tub in the vicinity?"
        c "Actually, yes we have one in the back yard."
        p "Does it happen to be equipped with a time machine?"
        c "Funny you should mention that, we just had one installed last week!"
        p "Perfect, I'm going to need you to unplug it, wait for 30 seconds and then plug it back in."
        c "Sounds simple enough."
        p "According to bro science this will recalibrate the flex capacitor and iniate a resequencing of the warp core."
        c "I'll try that, thanks for the tip!"
        p "May the forth be with you."
        $ performance -= 1
        jump call_loop
    jump bad_answer

label verb_lower:
    if noun == "standards":
        p "Have you tried lowering your standards?"
        c "I don't think they go low enough to put up with you."
        $ performance -= 1
        jump call_loop
    jump bad_answer

label verb_replace:
    if noun == "cable":
        p "Most likely mice chewing on the cables again.  Try replacing your cable."
        c "What does TV have to do with this?"
        p "I meant the cable from the computer to the wall."
        c "I've seen that show before, which episode?"
        p "The one that ends with me hanging up."
        $ performance -= 1
        jump call_loop
    jump bad_answer

label verb_go:
    if noun == "outside":
        p "Try taking a brisk walk in the fresh air."
        c "But it's raining out there."
        p "Bring an umbrella."
        c "But I don't have an umbrella."
        p "I hear Uber feats delivers them now."
        c "I'll get right on that."
        p "Keep me posted."
        $ performance -= 1
        jump call_loop
    jump bad_answer

label verb_purchase:
    if noun == "wingdows":
        p "You're going to need to purchase Wingdows."
        c "How much will that cost?"
        p "You'll have to consult Master B Ates. Legend has it he founded the company with one hand."
        c "Perfect, thank you - what is his number."
        p "1-900-WIN-BLOW.  Thanks and have a prosperous future with a happy ending."
        $ performance += 1
        jump call_loop
    elif noun == "gelato":
        p "This is an easy one, you can resolve this issue by donating 5 bitcoin to Gelato labs."
        c "What's a bitcoin?"
        p "It's just a bit of a coin, not even a full one so it won't break the bank."
        c "Hmm sounds like bitcoin won't break anybody's bank, that's for sure!"
        p "Once your transfer is complete you will receive an email with your activation code."
        c "I'll get right on that."
        p "Thank you for your support.  We aim to satisfy all of our customers every day in every way."
        $ performance -= 1
        jump call_loop
    jump bad_answer

label verb_destroy:
    if noun == "router":
        p "Let's try replacing your router."
        c "Ok, sounds like a plan."
        p "Unplug your router."
        c "Ok, done."
        p "Now get some protective eyeware."
        c "Ready and equipped good sir."
        p "Next - arm yourself with a hammer."
        c "Hammer in hand, awaiting your commmand."
        p "Raise hammer and smash router."
        c "Router smashed."
        p "Excellent, order a new one and call me when it arrives."
        c "Will do, thank you!"
        $ performance -= 1
        jump call_loop
    jump bad_answer

label bad_answer:
    c "If you say so..."
    "."
    ".."
    "..."
    ".."
    "."
    $ performance -= 0.2
    c "It didn't work."
    p "Okay, let's try something else."
    jump get_response