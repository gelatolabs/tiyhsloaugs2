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
        
        p "Well, we no longer support Internet Expeller, but we have another tool that is much better."
        
        c "You don't say. Please, enlighten me."
        
        p "It's called AOL, short for America's Open Legs."
        
        c "Sounds like a warm invitation."
        
        p "You're in for a big surprise."
        call updatePerformance(1)
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
    elif noun == "drivers":
        
        p "Let's try installing the drivers."
        
        c "I thought these things had AI drivers."
        
        p "No, AI isn't quite there yet - we still need to do some things the old fashioned way."
        
        c "Who would be crazy enough to drive one of these?"
        
        p "Buckle up, you're about to find out!"
        
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
        
        c "Oh no. You're right."
        
        p "Sorry?"
        
        c "It is in the fart menu!"
        
        p "Isn't that good?"
        
        c "No. I thought I had escaped. NOOOOOOOOOOOOOOOOOOOOOO"
        call updatePerformance(-1)
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
    elif noun == "modem" and current_call == "modem":
        
        p "Well then, let's try rebooting it."
        
        c "What, you want me to kick it?"
        
        p "Don't do that. You just need to pull the power plug from it."
        
        c "Ok, done."
        "*loud beeps over the phone*"
        
        p "I think you unplugged your security system instead."
        
        c "Haha sorry they're both square things and you know how it is with shapes."
        
        p "Of course."
        
        "*beeping stops*"
        c "Ok I unplugged the {i}moter{/i} this time."
        
        p "Now plug it back in. And wait 5 minutes."
        
        "."
        ".."
        "..."
        ".."
        "."
        c "Yes, YouToob is loading now!"
        call updatePerformance(1)
        jump call_loop
    elif noun == "modem" and current_call == "mouse":
        
        p "You may need to reboot your internet modem."
        
        c "How does that fix my mouse?"
        
        p "It doesn't, but the quality assurance agents don't listen to call after a 'solution' is given."
        
        call updatePerformance(-1)
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
    elif noun == "computer" and current_call == "imploded":
        
        p "Have you tried turning it off and on again?"
        
        c "My computer?"
        
        p "Yes."
        
        c "But it doesn't exist any more. It imploded."
        
        p "Right. Well sorry, that's the best I've got!"
        
        c "..."
        call updatePerformance(-1)
        jump call_loop
    elif noun == "computer" and current_call == "broken":
        
        p "I think it's best if we proceed with a power cycle."
        
        c "BUT I DON'T OWN A BIKE."
        
        p "That's okay, it's just the name of a process."
        
        c "LIKE A SPIN CYCLE?"
        
        p "Exactly, some rogue processes might just need to be cleaned."
        
        c "BUT HOW CAN I FIT MY PC IN THE WASHING MACHINE?"
        
        p "Just press the power button, wait for a minute and then press it again."
        
        c "SURE THING BOSS!"
        call updatePerformance(1)
        jump call_loop
    elif noun == "computer" and current_call == "mouse":
        
        p "Try restarting your computer please."
        
        c "The last person told me to do that already. It didn't do anything!"
        
        p "Please try it again anyway."
        
        c "No."
        call updatePerformance(-1)
        jump call_loop
    elif noun == "computer" and current_call == "password":
        
        p "Have you tried turning your computer off and on again?"
        
        c "No."
        
        p "Can you?"
        
        c "Well I suppose, if you tell me how."
        
        p "Press the power button."
        
        c "You broke it! It's not turning on again!"
        
        p "Press it again."
        
        c "Oh, there it is."
        
        p "Now try typing your password."
        
        c "Nope, still asterisks!"
        
        p "Darn. Well, that's all I've got."
        
        c "Can you escalate my ticket?"
        
        p "Nope."
        
        c "Why not?"
        
        p "I don't know how."
        
        c "Oh."
        
        p "Bye!"
        call updatePerformance(-1)
        jump call_loop
    elif noun == "yourself" and current_call == "modem":
        
        p "I think you need to reboot yourself."
        
        c "...What?"
        
        p "You heard me. You need to kick yourself in the ass with a boot."
        
        c "You'll be hearing from my lawyer."
        call updatePerformance(-2)
        jump call_loop
    elif noun == "refrigerator":
        
        p "Is your refrigerator running?"
        
        c "Probably, why?"
        
        p "Better go kick it to be sure."
        
        call updatePerformance(-1)
        jump call_loop
    elif noun == "cellphone":
        
        p "Let's make sure it's not a problem with your phone."
        
        c "Ok, sure."
        
        p "Can you restart it now?"
        
        c "Sure, just one seco--"
        "Works every time."
        call updatePerformance(-1)
        jump call_loop
    elif noun == "server":
        
        p "It's actually a problem with the website you're viewing. They haven't updated the hyperflux compression interchange layer they are using since 1997."
        
        c "Well what do I do? I need to see my cat pictures!"
        
        p "Go bug them about it, not me."
        
        call updatePerformance(-1)
        jump call_loop
    jump bad_answer

label verb_lower:
    if noun == "standards":
        
        p "240p you say?  That's amazing, how did you manage that?"
        
        c "Shouldn't it be a higher number?"
        
        p "No no no, that's 240x better than single p format!"
        
        c "Wow, when you put it that way I guess I'm lucky!"
        
        p "You got that right, you just need to lower your standards."
        
        c "I suppose the picture isn't all that bad."
        
        p "Use your imagination to see past the pixels."
        
        call updatePerformance(1)
        jump call_loop
    jump bad_answer

label verb_raise:
    if noun == "standards":
        
        p "Try raising your standards."
        
        c "Wouldn't that just make this worse?"
        
        p "Uh... I mean, lower them."
        
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
    elif noun == "computer":
        
        p "Well... I don't think there's much we can do in that case but replace it."
        
        c "Can't you un-implode it?"
        
        p "I'm a Customer Synergy Specialist, not a magician."
        
        c "Well, alright. But I don't think you sell any computers as good as mine."
        
        p "We're the only computer company on the planet. Surely we do."
        
        c "My computer has 512 kilobytes of RAM."
        
        p "We can do, like, 128 gigabytes."
        
        c "But 512 is way more than 128!"
        
        p "...please just trust me on this one."
        
        c "Can it run Minesweeper?"
        
        p "Yes."
        
        c "Can it run Solitaire?"
        
        p "Yes."
        
        c "Can it run Netscape?"
        
        p "No."
        
        c "Hmm... I guess 2 for 3 ain't bad. I'll take it."
        
        p "Great. I'll transfer you to our sales department."
        
        call updatePerformance(1)
        jump call_loop
    elif noun == "ink":
        
        p "It may be out of ink, do you have a spare cartridge?"
        
        c "I'm afraid not, the supply shortage has left me empty-handed."
        
        p "That's ok, we can proceed with a manual reload."
        
        c "Perfect, what's involved?"
        
        p "You're going to need a pair of scissors, and all the ballpoint pens you can find..."
        
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
        
        p "This is an easy one, you can resolve this issue by donating 5 bitcoin to Gelato Labs."
        
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
        
        p "Let's try some percussive maintenance."
        
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
        
        c "Wait, I thought we were fixing this one!?!?"
        call updatePerformance(-1)
        jump call_loop
    elif noun == "time machine":
        
        p "Do you have a time machine?"
        
        c "As a matter of fact I do. What does that have to do with anything?"
        
        p "Well it could be causing interference with your router and slowing it down."
        
        c "Huh, I guess that makes sense. What can I do about it?"
        
        p "You're going to have to destroy your time machine."
        
        c "I would sure miss it. It was a gift from my great-great-great-great-great grandson."
        
        p "Well, do you want to fix your Internet or not?"
        
        c "Yeah, the time machine is cool but I don't know what I'd do without my Bookface. I'll go destroy it."
        "."
        ".."
        "..."
        ".."
        "."
        c "I destroyed it, but the Internet is still slow!"
        
        p "Oh. Well, it was worth a try."
        
        c "No it wasn't! What have you done??"
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
        
        p "In that case, check the dongle."
        
        c "There's no dongle."
        
        p "Oh, it's a bluetooth keyboard?"
        
        c "Yes."
        
        p "In that case, throw it in the garbage."
        
        c "Thanks for the tip."
        call updatePerformance(1)
        jump call_loop
    elif noun == "computer":
        
        p "Try unplugging your computer."
        
        c "Okay."
        
        p "Now try typing your password."
        
        c "Okay."
        
        p "Still asterisks?"
        
        c "No."
        
        p "You're welcome!"
        
        c "But my computer is off. I don't see anything."
        
        p "You're welcome!!!"
        
        call updatePerformance(-1)
        jump call_loop
    elif noun == "hard drive":
        
        p "Try unplugging your hard drive."
        
        c "How is that supposed to help?"
        
        p "If you want to fix your password, you're going to need to trust me."
        
        c "If you say so..."
        c "It says something about corruption?"
        
        p "Did you turn your computer off before you unplugged your hard drive?"
        
        c "No. Should I have?"
        
        p "Yes."
        
        c "Now what?"
        
        p "Please don't tell my manager."
        
        call updatePerformance(-1)
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
        
        p "Just one - use only asterisks."
        
        c "Thanks! I hope I can remember it."
        call updatePerformance(1)
        jump call_loop
    elif noun == "codes":
        
        p "You will need your backup code to allow us to change your main nuclear codes."
        
        c "What makes you think I have the backup code?"
        
        p "Sorry sir, without that I cannot le--"
        
        c "er, 1234?"
        
        p "Correct. What would you like to change it to?"
        
        c "0000"
        
        p "Excellent choice. Have a nice day."
        
        call updatePerformance(1)
        jump call_loop
    elif noun == "keyboard":
        
        p "Do you have another keyboard you can try?"
        
        c "Yes, I do."
        
        p "Okay, see if it works."
        
        c "Now it doesn't type anything."
        
        p "Did you plug it in?"
        
        c "Plug what in?"
        
        p "The keyboard. Into your computer."
        
        c "Oh, right."
        c "Now it types, but still just asterisks!"
        
        p "Hmm... I guess it must be a software problem."
        
        c "Okay, can you fix it?"
        
        p "Nope, sorry. I'm more of a hardware person. Good luck with that!"
        
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
        
        c "HOW MUCH CASH DO YOU NEED?"
        
        p "You can make a transfer of $1,000 at the following link."
        p "{a=https://ko-fi.com/gelatolabs}https://ko-fi.com/gelatolabs{/a}"
        
        c "DONE."
        
        p "Perfect, now I will wait until the payment is verified and get back to you in 3-5 business days."
        
        c "THANKS!"
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
    elif noun == "wifi":
        
        p "The issue may be with your connection. Let's make sure the WiFi is enabled."
        
        c "What's a WiFi?"
        
        p "It's that thing that miraculously connects network devices wirelessly."
        
        c "Sounds like magic."
        
        p "Only when it works. Try enabling WiFi on your printer."
        
        c "I'm waving my phone at my printer but it doesn't seem to be enabling anything."
        
        p "It's going to be a long night..."
        
        call updatePerformance(-1)
        jump call_loop
    jump bad_answer

label verb_run:
    if noun == "away":
        
        p "Where do you think you left them?"
        
        c "I think it may have been at the J20 conference over in Europe..."
        
        p "Sir, I would recommend running away as soon as possible. Our systems indicate targeting systems are locking in on your position."
        
        c "OH SH--"
        call updatePerformance(-1)
        jump call_loop

label verb_defrag:
    if noun == "hard drive":
        
        p "I think we're going to need to defragment your hard drive to find them."
        
        c "hard drive? The only hard thing here is my rock hard di--"
        
        p "Nope, I'm not looking to be caught beneath the Concave Office desk."
        
        call updatePerformance(-1)
        call updateSanity(-0.3)
        jump call_loop
        
label verb_try:
    if noun == "again":
        
        p "Try again."
        
        c "NO."
        
        p "Why not?"
        
        c "NO."
        
        p "No what?"
        
        c "NO."
        
        p "What are you trying to do?"
        
        c "NO."
        
        p "Yes."
        
        c "NO."
        
        p "YES."
        
        c "NO."
        
        p "Good bye."
        
        call updatePerformance(-1)
        jump call_loop
    jump bad_answer

label verb_return:
    if noun == "movie":
        
        p "If you are not happy with the picture you can always initiate a return."
        
        c "Let's go ahead with that option."
        
        p "A return shipping label will be mailed to you."
        
        c "It's a digital movie so how can I ship it back?"
        
        p "Print out the code, and securely package it."
        
        c "Thank you!"
        call updatePerformance(1)
        jump call_loop
    jump bad_answer

label verb_wear:
    if noun == "glasses":
        
        p "Do you happen to wear glasses?"
        
        c "As a matter of fact, I do."
        
        p "Try putting them on."
        
        c "Never thought of that, wow this is much better!"
        
        p "If you would like to upgrade to 3D, \"borrow\" a pair of 3D glasses from the movie theatre."
        
        c "Thanks for the tip!"
 
        call updatePerformance(1)
        jump call_loop
    jump bad_answer

label verb_wait:
    if noun == "longer":
        
        p "If you could just wait a bit longer I'll get this issue resolved for you."
        
        c "HOW MUCH LONGER???"
        
        p "No need to raise your voice, please remain calm."
        
        c "I AM NOT CALM, GIVE ME AN ANSWER!!"
        
        p "We do not tolerate that type of harassment here at MegaCorp Industries.  Have a pleasant day!"
        
        c "NOOOO, DON'T HANNGG UUU"
        call updatePerformance(-1)
        jump call_loop
    jump bad_answer

label verb_please:
    if noun == "hold":
        
        p "Thank you for your concern, please hold."
        
        c "WAIT!"
        "*You place the customer on hold*"
        
        p "Thank you for holding, please continue to hold."
        
        c "NOOOOOO!"
        "*You place the customer on hold*"
        
        p "Unfortunately none of our agents are currently able to take your call, please leave a message."
        
        call updatePerformance(-1)
        jump call_loop
    jump bad_answer

label verb_be:
    if noun == "patient":
        
        p "Tuesday, that's nearly 24 hours!"
        
        c "I know, this is driving me crazy!"
        
        p "I'm terribly sorry for your inconvenience."
        
        c "Please just give me some help."
        
        p "I ask you to please be patient while I retrieve your file."
        
        c "You expect me to be patient, after all this?"
        
        p "Let me guide you through a little breathing exercise."
        
        c "What?"
        
        p "Please take a deep breath in through your nose."
        
        c "*inhales*"
        
        p "One."
        p "Two."
        p "Three."
        p "Four."
        p "Five."
        p "Out through your nose."
        c "*exhales*"
        p "One."
        p "Two."
        p "Three."
        p "Four."
        p "Five."
        p "In."
        c "*inhales*"
        p "One."
        p "Two."
        p "Three."
        p "Four."
        p "Five."
        p "Out."
        c "*exhales*"
        p "One."
        p "Two."
        p "Three."
        p "Four."
        p "Five."
        p "In."
        c "*inhales*"
        p "One."
        p "Two."
        p "Three."
        p "Four."
        p "Five."
        p "Out."
        c "*exhales*"
        
        p "Feeling better?"
        
        c "Wow, yes I am!"
        
        p "Ready to be patient?"
        
        c "Absolutely."
        
        p "It seems that you have been transferred to the wrong department."
        
        c "WHATT??!!??!"
        
        p "Please remain on the line and an agent will be with you shortly."
        
        c "AHHHHHHHHHHHHHHHHHHHHHH!!!"
        call updatePerformance(1)
        jump call_loop
    jump bad_answer

label verb_plugin:
    if noun == "power bar":
        p "Have you tried restarting your computer?"
        c "Yes, it's still showing nothing."
        p "Have you checked all the monitor cables?"
        c "Yes, they're all connected."
        p "Are the lights on?"
        c "No."
        p "Do you by chance happen to be using a power bar?"
        c "Yes."
        p "Try plugging it in."
        c "Why would I do that - the power comes from that bar already!"
        p "Just do it."
        c "If you say so... WOW, it worked, you're a genius!"
        p "Just doing my job. Have a great day."
        call updatePerformance(1)
        jump call_loop
    elif noun == "cables":
        p "Have you checked all the cables?"
        c "Yes, they are all where they should be."
        p "Do you have any pets of the feline variety?"
        c "You mean cats? Yes - two actually."
        p "Inspect those cables for bite marks."
        c "Aha, I found one but it appears to be human!"
        p "You may want to evacuate the area, sounds like you have a zombie problem."
        c "They're coming for me, AHHHHH!!!!"
        call updatePerformance(1)
        jump call_loop
    jump bad_answer

label verb_clean:
    if noun == "screen":
        p "Look closely at your screen to determine if there is a residue on it."
        c "Okay, it appears as though there may be."
        p "Lick your finger and run it over the screen to confirm."
        c "Ahhh, my finger turned black!"
        p "Just as I figured, you've been hit by the Sharpie Bandits."
        c "Sharpie bandits??"
        p "Yes, they've been reported in your area - sick individuals that black out screens with sharpies."
        c "Is there anything I can do?"
        p "I'm afraid you'll need to purchase a new screen, and don't forget to lock your doors!"
        call updatePerformance(1)
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
