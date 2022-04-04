label verb_hang:
    if noun == "up":
        call updatePerformance(-1)
        jump call_loop
    jump bad_answer

label verb_refer:
    if noun == "sales":
        p "Let me transfer you to our sales department."
        c "Wait-"
        call updatePerformance(1)
        call updateSanity(-0.25)
        jump call_loop
    jump bad_answer

label verb_blame:
    if noun == "user" or noun == "caller" or noun =="customer":
        p "Sorry, it seems your problem exists between the keyboard and chair. We don't solve that kind of problem here."
        c "Huh?"
        call updatePerformance(-1)
        jump call_loop
    jump bad_answer

label verb_insult:
    if noun == "user" or noun == "caller" or noun =="customer":
        p "You smell."
        c "Excuse me?"
        call updatePerformance(-1)
        jump call_loop
    jump bad_answer

label verb_call:
    if noun == "fbi":
        p "Could you please hold for a moment? I forgot to turn off my refrigerator."
        c "Sure thing."
        "*You put the customer on hold and call the FBI*"
        p "Hello, is this FBI?"
        "FBI" "Special agent Halfbaked speaking, state your issue civilian."
        p "I'd like to report an act of piracy."
        "FBI" "Are you kidding me, call the coast guard you numbskull!"
        "*The FBI Agent hangs up* Oh well, it was worth a try."
        p "We appear to be having technical difficulties at this moment, please call again later."
        call updatePerformance(-1)
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
        call updatePerformance(-1)
        jump call_loop
    if noun == "wingdows":
        p "You're going to need to purchase Wingdows."
        c "How much will that cost?"
        p "You'll have to consult Master B Ates. Legend has it he founded the company with one hand."
        c "Perfect, thank you - what is his number."
        p "1-900-WIN-BLOW. Thanks and have a prosperous future with a happy ending."
        call updatePerformance(1)
        jump call_loop
    elif noun == "aol":
        p "Why would you want to use that?"
        c "To view wholesome pictures on the world wide web."
        p "Ah yes, well there's another tool that is much better."
        c "You don't say. Please, enlighten me."
        p "It's called AOL, short for America's Open Legs."
        c "Sounds like a warm invitation."
        p "You're in for a big surprise."
        call updatePerformance(-1)
        jump call_loop
    elif noun == "chrome":
        p "You're actually better off installing Gargle Chrome."
        c "Oh really, sounds complicated."
        p "Don't worry, we only have to change every default file type from Internet Expeller to Gargle Chrome."
        c "Sounds like fun."
        p "You have no idea."
        "Five hours later Chrome is still not set as default and the customer hangs up."
        call updatePerformance(-1)
        jump call_loop
    jump bad_answer

label verb_the:
    if noun == "garbage":
        p "In the garbage, where it belongs."
        c "Well, okay. I guess I'll just stop using the Internet."
        p "That's probably for the best."
        c "Thanks for your help!"
        call updatePerformance(1)
        jump call_loop
    elif noun == "fart menu":
        p "You should find a shortcut to it on the Fart Menu."
        c "Where is the fart menu?"
        p "The lower left-hand side of your screen. Unless you're on Wingdows 11, it's awkwardly in the middle."
        c "Unfortunately I upgraded, I heard this is the best way to experience the Internet."
        p "I bet you did."
        call updatePerformance(1)
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
        c "Everything just went dark! I'm scared."
        p "Don't panic, you just unplugged the lamp. Plug it back in."
        c "There we go, found it!"
        p "Great, now wait for 30 seconds and plug it back in."
        "."
        ".."
        "..."
        ".."
        "."
        c "Okay, I'm back!"
        p "What the heck took you so long??"
        c "Just like you said, wait 30 minutes..."
        p "Wow, does your internet work now??"
        c "It's blazing fast now, I've been streaming my favourite show {i}Love at First Bite{/i} for the past 30 minutes. Thank you!!"
        call updatePerformance(1)
        jump call_loop
    elif noun == "mainframe" and current_call == "imploded":
        p "Could be a frozen Wingdows Update, let's reboot the mainframe."
        c "I don't have any picture frames near my computer."
        p "No, the mainframe is another word for the computer."
        c "Ohh I get it, so I have to re-boot the computer?"
        p "Precisely."
        c "What size boots does it wear?"
        p "*sigh* Just press the power button twice."
        c "Wow, that did it! You are a genius."
        p "Have a good life."
        call updatePerformance(1)
        jump call_loop
    elif noun == "time machine":
        p "Do you happen to have a hot tub in the vicinity?"
        c "Actually yes, we have one in the backyard."
        p "Does it happen to be equipped with a time machine?"
        c "Funny you should mention that, we just had one installed last week!"
        p "Perfect, I'm going to need you to unplug it, wait for 30 seconds and then plug it back in."
        c "Sounds simple enough."
        p "According to bro science this will recalibrate the flex capacitor and iniate a resequencing of the warp core."
        c "I'll try that, thanks for the tip!"
        p "May the forth be with you."
        call updatePerformance(-1)
        jump call_loop
    elif noun == "computer":
        p "I think it's best if we proceed with a power cycle."
        c "But I don't own a bike."
        p "That's okay, it's just the name of a process."
        c "Like a spin cycle?"
        p "Exactly, some rogue processes might just need to be cleaned."
        c "But how can I fit my pc in the washing machine?"
        p "Just press the power button, wait for a minute and then press it again."
        c "Sure thing boss!"
        call updatePerformance(1)
        jump call_loop
    elif noun == "yourself" and current_call == "modem":
        p "I think you need to reboot yourself."
        c "...What?"
        p "You heard me. You need to kick yourself in the ass with a boot"
        c "You'll be hearing from my lawyer."
        call updatePerformance(-2)
        jump call_loop
    jump bad_answer

label verb_lower:
    if noun == "standards":
        p "Have you tried lowering your standards?"
        c "I don't think they go low enough to put up with you."
        call updatePerformance(-1)
        jump call_loop
    jump bad_answer

label verb_replace:
    if noun == "cable":
        p "Most likely mice chewing on the cables again. Try replacing your cable."
        c "What does TV have to do with this?"
        p "I meant the cable from the computer to the wall."
        c "I've seen that show before, which episode?"
        p "The one that ends with me hanging up."
        call updatePerformance(-1)
        jump call_loop
    jump bad_answer

label verb_go:
    if noun == "outside":
        p "Try taking a brisk walk in the fresh air."
        c "But it's raining out there."
        p "Bring an umbrella."
        c "But I don't have an umbrella."
        p "I hear Uber Feats delivers them now."
        c "I'll get right on that."
        p "Keep me posted."
        call updatePerformance(-1)
        jump call_loop
    jump bad_answer

label verb_purchase:
    if noun == "wingdows":
        p "You're going to need to purchase Wingdows."
        c "How much will that cost?"
        p "You'll have to consult Master B Ates. Legend has it he founded the company with one hand."
        c "Perfect, thank you - what is his number."
        p "1-900-WIN-BLOW. Thanks and have a prosperous future with a happy ending."
        call updatePerformance(1)
        jump call_loop
    elif noun == "gelato":
        p "This is an easy one, you can resolve this issue by donating 5 bitcoin to Gelato labs."
        c "What's a bitcoin?"
        p "It's just a bit of a coin, not even a full one, so it won't break the bank."
        c "Hmm sounds like bitcoin won't break anybody's bank, that's for sure!"
        p "Once your transfer is complete you will receive an email with your activation code."
        c "I'll get right on that."
        p "Thank you for your support. We aim to satisfy all of our customers every day in every way."
        call updatePerformance(-1)
        jump call_loop
    jump bad_answer

label verb_destroy:
    if noun == "router":
        p "Let's try replacing your router."
        c "Okay, sounds like a plan."
        p "Unplug your router."
        c "Okay, done."
        p "Now get some protective eyeware."
        c "Ready and equipped good sir."
        p "Next - arm yourself with a hammer."
        c "Hammer in hand, awaiting your commmand."
        p "Raise hammer and smash router."
        c "Router smashed."
        p "Excellent, order a new one and call me when it arrives."
        c "Will do, thank you!"
        call updatePerformance(-1)
        jump call_loop
    jump bad_answer

label verb_reinstall:
    if noun == "outlook":
        p "It could be a problem with outlook."
        c "Where should I be looking?"
        p "At your computer."
        c "Ok, now what?"
        p "Buckle up buttercup, it's going to be a rough ride."
        c "Oh gracious me, what do we do now?"
        p "We must perform a complete reinstall."
        c "I've never done that before."
        p "Me neither, first time for everything!"
        "Five escalations and four hours later they are back to outlooking."
        call updatePerformance(1)
        jump call_loop
    jump bad_answer

label verb_ask:
    if noun == "post office":
        p "Have you tried asking the post office?"
        c "They still carry email these days?"
        p "Well, mostly just the postmaster - especially when mail goes missing!"
        c "Perfect, I'll give them a call."
        p "Good luck!"
        call updatePerformance(-1)
        jump call_loop
    jump bad_answer

label verb_look:
    if noun == "harder":
        p "Perhaps you should expand your search."
        c "How can I do that?"
        p "Well, where have you looked so far?"
        c "Under the bed, in the closet, inbetween the sofa cushions."
        p "Try looking inside the internet."
        c "Inside the internet, how do I get there?"
        p "Just rent a VHS copy of the Matrix and you'll have everything you need."
        call updatePerformance(-1)
        jump call_loop
    jump bad_answer

label verb_unplug:
    if noun == "keyboard":
        p "Have you tried unplugging it and plugging it back in again?"
        c "How can I do that?"
        p "Follow the cable from your keyboard to the back of your computer."
        c "There's no cable."
        p "Oh, its a wireless keyboard?"
        c "Yes."
        p "In that case, check the batteries."
        c "There's no batteries."
        p "Oh, it has an internal battery?"
        c "Yes."
        p "In that case, check that the dongle."
        c "There's no dongle."
        p "Oh, it's a bluetooth keyboard?"
        c "Yes."
        p "In that case, throw it in the garbage."
        c "Thanks for the tip."
        call updatePerformance(1)
        jump call_loop
    jump bad_answer

label verb_change:
    if noun == "hard drive":
        p "Perhaps it is an issue with your hard drive."
        c "My hard what?"
        p "Drive, it's part of the RAID - Redundant Array of Inexpensive Disks."
        c "Great, what should we do?"
        p "It's going to be a long night..."
        call updatePerformance(-1)
        jump call_loop
    elif noun == "password":
        p "We're going to have to change your password."
        c "Okay, what do I do?"
        p "First, click reset password."
        c "Done."
        p "Perfect, now type a new password."
        c "Any special requirements?"
        p "Just one - use only asterisks. Have a nice day!"
        call updatePerformance(-1)
        jump call_loop
    jump bad_answer

label verb_microwave:
    if noun == "computer":
        p "Maybe it's an issue with the cooling system, it might be frozen."
        c "Wow, what can we do?"
        p "Let's try microwaving it."
        c "Are you sure, what setting should I use?"
        p "Definitely popcorn."
        c "Here goes nothing!"
        "Audible snap crackle pops can be heard in the background before the connection is lost."
        call updatePerformance(-1)
        jump call_loop
    jump bad_answer

label verb_clear:
    if noun == "cache":
        p "The memory buffer could be full, let's try clearing the cache."
        c "How much cash do you need?"
        p "You can make a transfer of $1,000 at the following link."
        p "{a=https://ko-fi.com/gelatolabs}https://ko-fi.com/gelatolabs{/a}"
        c "Done."
        p "Perfect, now I will wait until the payment is verified and get back to you in 3-5 business days."
        c "Thanks!"
        call updatePerformance(-1)
        jump call_loop
    jump bad_answer

label verb_plug:
    if noun == "in":
        p "Have you tried plugging in your mouse?"
        c "Do you think I'm dumb? Of course my mouse is plugged in! I want to speak to your m--"
        p "I'm sorry sir, let's try one more thing. Can you try unplugging the purple plug from the back of your computer, and putting it back in?"
        c "Fine."
        "..."
        c "Oh hey, it worked! Told you my mouse was plugged in."
        call updatePerformance(1)
        call updateSanity(-0.2)
        jump call_loop
    jump bad_answer

label verb_enable:
    if noun == "mouse keys":
        p "You need to enable a feature called Mouse Keys on your computer."
        c "Keys? Why do I need to put my keys in my mouse?"
        p "Your mouse has an ignition key slot just like your car. Flip your mouse over, and find the small round slot."
        c "Okay..."
        p "Put your key in there. Don't be afraid to put some force into it, it may be a tight fit on the first time."
        "*crunch*"
        call updatePerformance(-1)
        jump call_loop
    jump bad_answer

label bad_answer:
    $ badAns = renpy.random.randint(1,3)
    if badAns == 1:
        c "If you say so..."
        "."
        ".."
        "..."
        ".."
        "."
        c "It didn't work."
    elif badAns == 2:
        c "What are you talking about? Just fix my problem already!"
    elif badAns == 3:
        c "Stop wasting my time. I have things to do!"
    p "Okay, let's try something else."
    call updateSanity(-0.1)
    call updatePerformance(-0.2)
    jump get_response
