#import the lib
import requests
import sys

#import colorama specs
from colorama import Fore, Back, Style

#my api key 
token = 'c06eff39ec548433d763465a03fdd508677b082b'

#this is the beginning of the url string which will be used for all the get requests
url = "https://api.waqi.info/search/"

#this is ONE get request for the API, which takes the url and fills the rest in with my API key and the keyword request
delhiResponse = requests.get(url, params={"token": token, "keyword": "delhi"})

#after getting the response from the API, we will convert it into a .json so that we can access the data
delhiResults = delhiResponse.json()

#The two indexes of the Results are 'status' and 'data'. We only want 'data'
delhiResponseData = delhiResults['data'] 

#I am storing the names, UIDs, AQIs, etc. for later use in the script
delhiUID = delhiResponseData[2]['uid']
delhiAQI = delhiResponseData[2]['aqi']

#Here is the beginning of the script
#The terms Fore.COLOR and Style.RESET_ALL are colorama commands which affect text color
print ()
print(Fore.BLUE +"   _____ _____ _________     __  _      _____ ______ ______ ")
print("  / ____|_   _|__   __\\ \\   / / | |    |_   _|  ____|  ____|")
print(" | |      | |    | |   \\ \\_/ /  | |      | | | |__  | |__   ")
print(" | |      | |    | |    \\   /   | |      | | |  __| |  __|  ")
print(" | |____ _| |_   | |     | |    | |____ _| |_| |    | |____ ")
print("  \\_____|_____|  |_|     |_|    |______|_____|_|    |______|")
print (Style.RESET_ALL)
print("In a world of anthropomorphic cities, you rank among the filthiest. This has not been a problem for you thus far, but perhaps your status is due for a change...")
print ()
print("It is late autumn and you find yourself arriving at your destination: a nondescript alleyway with not another soul around. At least that’s what you thought, until you feel a powerful tap on the back of your shoulder.")
print ()
print("???: “Jeremy? Jeremy, is that you?”")
print ()
print ("YOU: “No… Who’s Jeremy?” you reply.")
print ()
print ("???: “My drug dealer, Jeremy! Everyone in this alley knows Jeremy! He possesses my steroids, which he will exchange for US dollars!!”")
print ()
print ("YOU: “He gives you steroids? Why would someone as beefy as you need steroids?”")
print ()
print ("???: “Ah, yes… I was a sumo wrestler in my prime. The greatest, some would say. The crowds would chant, ‘You got this, Dehli! You’re the strongest city in India, Dehli!’ Until someone stronger came along and I became nothing… Nobody…”")
print ()
print ("DELHI: “That’s when the steroids began. I’ve been stuffing my body full of steroids, toxic chemicals, really anything that’s supposed to make me stronger. But now I’m down to my last syringe and I only want more!”")
print ()
print ("YOU: “Geez, that’s rough, buddy. How bad is it, Dehli? What’s your Air Quality Index?”")
print ()
print ("DELHI: “Alas, it’s up to a whopping", delhiAQI, "…”")   #The AQI data we gathered earlier from the API get request is used here
print ()
print ("YOU: “My goodness, man. I hate to say it, but I’m not doing so hot either…”")
print ()
print ("DELHI: “Really? And who are you?”")
print ()
print (Fore.YELLOW + "_________________________")
print ("Choose your city…")

#The user gets to choose which city they want to 'play' as in the game, each with different AQIs depending on the users preference
#We place these get requests here so that we don't frontload the program with too many requests
#Since we want to display information from all three of these cities, they have to be requested at the same time, before the if-statement
saoPauloResponse = requests.get(url, params={"token": token, "keyword": "sao paulo"})
bangkokResponse = requests.get(url, params={"token": token, "keyword": "bangkok"})
tashkentResponse = requests.get(url, params={"token": token, "keyword": "tashkent"})

saoPauloResults = saoPauloResponse.json()
bangkokResults = bangkokResponse.json()
tashkentResults = tashkentResponse.json()

saoPauloResponseData = saoPauloResults['data'] 
bangkokResponseData = bangkokResults['data'] 
tashkentResponseData = tashkentResults['data'] 

saoPauloUID = saoPauloResponseData[2]['uid']
saoPauloAQI = saoPauloResponseData[2]['aqi']

bangkokUID = bangkokResponseData[2]['uid']
bangkokAQI = bangkokResponseData[2]['aqi']

tashkentUID = tashkentResponseData[2]['uid']
tashkentAQI = tashkentResponseData[2]['aqi']

print ()
print ("(1) São Paulo, Brazil | UID:", saoPauloUID, "| Current AQI:", saoPauloAQI, "| Average AQI: ~60") 
print ("(2) Tashkent, Uzbekistan | UID:", tashkentUID, "| Current AQI:", tashkentAQI, "| Average AQI: ~90") 
print ("(3) Bangkok, Thailand | UID:", bangkokUID, "| Current AQI:", bangkokAQI, "| Average AQI: ~150") 
print ()

#This is the first instance of a user input
#The choices made here, and throughout the program, will affect how companions interact with you and may affect the ending
playerCityInput = input("[Type a number from 1-3] > ")

print ()
print ("_________________________")
print (Style.RESET_ALL)

#This get request is for a character introduced a little later in the story. Again, these are sprinkled throughout so that the program does not stall for too long
rotterdamResponse = requests.get(url, params={"token": token, "keyword": "rotterdam"})
rotterdamResults = rotterdamResponse.json()
rotterdamResponseData = rotterdamResults['data']
rotterdamUID = rotterdamResponseData[2]['uid']
rotterdamAQI = int(rotterdamResponseData[2]['aqi']) #AQI is specifically cast to an int because of a comparison check later on

#If-statements: depending on the users choice, their name and AQI will be set and used throughout
#If an invalid choice is made, exit the program
if (playerCityInput == "1"):
    playerCity = "São Paulo"
    playerAQI = int(saoPauloAQI)    #AQIs are specifically cast to an int because of a comparison check later on
    print("DELHI: ", playerCity, ", huh? Not surprising about your AQI, considering you're one of the most populous city in the world.") #MENTION A SPECIFIC FACT ABOUT CITY

elif(playerCityInput == "2"):
    playerCity = "Tashkent"
    playerAQI = int(tashkentAQI)
    print("DELHI: ", playerCity, ", huh? Not surprising about your AQI, considering you're the most populous city in Central Asia.")

elif(playerCityInput == "3"):
    playerCity = "Bangkok"
    playerAQI = int(bangkokAQI)
    print("DELHI: ", playerCity, ", huh? Must be tough dealing with your AQI now that you're considered the hottest city in the world.")

else:
    print("Invalid input. Terminating program.")
    sys.exit()

print () 
print ("Suddenly, a booming voice echoes through the alley.")
print ()
print ("???: “STOP CRIMINALS!”")
print ()
print ("YOU: “Whoa, whoa, we didn’t do anything!”")
print ()
#The characters will now use the variable playerCity to refer to the player
print ("DELHI: “It’s okay,", playerCity, ", he must be talking about my pal Jeremy,” the wrestler whispers to you.")
print ()
print ("DELHI: “YOU MUST BE TALKING ABOUT JEREMY! DO YOU KNOW WHERE HE IS?”")
print ()
print ("Without answering, the stranger briskly approaches and examines you and the wrestler.")
print ()
print ("???: “Hmmm, neither of you fit the bill. See that chalk outline of a body? The one you’re both standing on?”")
print ()
print ("You look toward your feet at the scuffed-up chalk marks forming the shape of a man.")
print ()
print ("???: “Somebody got to him. It’s my job to find out who…”")
print ()
print ("???: “But first, who are you two clowns? What are you doing here?”")
print ()
print (Fore.YELLOW + "_________________________")
print ("Choose how to reply…")
print ()
print ("(1) I seek to find pollutants which I can use to contaminate my water supply.")
print ("(2) I seek to capture a family of rats to populate my sewer system.")
print ("(3) I seek to collect garbage to sprinkle around my low-income neighbourhoods.")
print ("(4) Nothing, man, it’s none of your business.")
print ()
playerPurposeInput = input("[Type a number from 1-4] > ")
print ()
print ("_________________________")
print (Style.RESET_ALL)

playerPurpose = 0

#These if-statements control the response from the detective and the decision will be stored in a variable and referenced later
if (playerPurposeInput == "1"):
    playerPurpose = 1
    print("???: There's nothing like a filthy cup of H20 to start the day. Alright, kid, you get a pass this time.")

elif(playerPurposeInput == "2"):
    playerPurpose = 2
    print("???: I'm no fan of rats, and I know from experience that the feeling's mutual. But I guess there's nothing illegal about that.")

elif(playerPurposeInput == "3"):
    playerPurpose = 3
    print("???: The ol' rigamarole! Ahah, I like the way you think, kid. Don't know anyone who'd turn up their nose at some mass littering.")

elif(playerPurposeInput == "4"):
    playerPurpose = 4
    print("???: Remarkable. You just happen to be loitering at the site of a gruesome murder? Yet your immediate, instinctual defensiveness proves to me that you clearly had nothing to do with this.")

else:
    print("Invalid input. Terminating program.")
    sys.exit()

print ()
print ("Satisfied with his interrogation, the stranger looks at the empty bottle of whisky in his hand.")
print ()
print ("???: “Damn… I’m all out. This crappy job… I’ll need another bottle if I stand any chance of solving this.”")
print ()
print ("???: Thank god! There’s still some alcohol in this abandoned beer can on the floor!”")
print ()
print ("YOU: “You don’t look so good. All those substances you’re trying to cram into your body, they’re really taking a toll. At the end of the day, you’re not so different than the two of us.")
print ()
print ("???: “Bah, I’m leagues different than you, kid. I’m Rotterdam, last name Netherlands, badge number", rotterdamUID, ".”")
print ()
print ("ROTTERDAM: “I indulge in my vices to make it through each day at work. Neither of you have to tell Mary down the street that her husband isn’t coming home.”")
print ()
print ("DELHI: “That does sound miserable, sir, truly miserable.”")
print ()
print ("ROTTERDAM: “Yeah, I guess so. I mean, it’s not like I’ve actually done that, it’s my first day on the job after all. Just sorta making some assumptions here.”")
print ()
print ("DELHI: “Oh.”")
print ()
print ("YOU: “Well, it’s one hell of a first day you're having. You’re what - a few hours in? You’re barely holding it together, man! What’s your Air Quality Index?”")
print ()
print ("ROTTERDAM: “My AQI? Bah… let’s hear yours first.”")
print ()
print (Fore.YELLOW + "_________________________")
print ("Choose how to reply…")
print ()
print ("(1) Reveal you AQI.")
print ("(2) Refuse.")
print ()
revealAQIInput = input("[Type a number from 1-2] > ")
print ()
print ("_________________________")
print (Style.RESET_ALL)

#More get requests for later characters
dohaResponse = requests.get(url, params={"token": token, "keyword": "doha"})
haNoiResponse = requests.get(url, params={"token": token, "keyword": "ha noi"})

dohaResults = dohaResponse.json()
haNoiResults = haNoiResponse.json()

dohaResponseData = dohaResults['data'] 
haNoiResponseData = haNoiResults['data']


dohaUID = dohaResponseData[2]['uid']
dohaAQI = dohaResponseData[2]['aqi']

haNoiUID = haNoiResponseData[2]['uid']
haNoiAQI = haNoiResponseData[2]['aqi']

if (revealAQIInput == "1"):

    print("YOU: “Alright, I'll play along. I'm AQI", playerAQI, ".”")
    print ()

    #If the user chooses to reveal their AQI, it will be tested against the AQI of the detective, resulting in varying responses
    if (playerAQI > rotterdamAQI):
        print("ROTTERDAM: “You gotta get yourself cleaned up, kid. That's BAD, and this is coming from a", rotterdamAQI, ". But I digress…”")

    elif (playerAQI == rotterdamAQI):
        print("ROTTERDAM: “Okay, I don't know what sorta trick the fates are playing on us but… we have the exact same indexes. Maybe our paths were meant to cross. Anyway…”")

    else:
        print("ROTTERDAM: “OKAY FINE I'M", rotterdamAQI, ". BIG DEAL. I always get by, and after I solve this case it WON'T MATTER what my damn AQI is. Speaking of, can I get back to it?? Look…”")

#If the user refuses to divulge their AQI, the detective will reference the victim, whose data is gathered from the following get request
elif (revealAQIInput == "2"):

    detroitResponse = requests.get(url, params={"token": token, "keyword": "detroit"})
    detroitResults = detroitResponse.json()
    detroitResponseData = detroitResults['data']
    detroitUID = detroitResponseData[0]['uid']
    detroitLat = detroitResponseData[0]['station']['geo'][0]
    detroitLong = detroitResponseData[0]['station']['geo'][1]

    print("ROTTERDAM: “You hold your cards close to your chest. Admirable. It's what you have to do to survive on these lawless streets.”")
    print ()
    print("ROTTERDAM: “If only our vic knew that. Poor Detroit, Michigan - he kept telling people his lattitude and longitude were", detroitLat, "and", detroitLong, ".”")
    print ()
    print("ROTTERDAM: “Wasn't long before they found him… Ol' UID", detroitUID, ", taken before his time. But I digress…”")

else:
    print("Invalid input. Terminating program.")
    sys.exit()

print ()
print ("ROTTERDAM: “You two citizens see a criminal around here? Anyone suspicious?”")
print ()
print ("Two metal trash cans clatter loudly on the floor a few yards from where you stand. Suddenly, a woman walks into view, muttering to herself.")
print ()
print ("???: “The last alley at least had some trinkets…,” she murmurs, kicking a stray tin can down the path toward you.")
print ()
print ("???: “Hey! Anyone come across anything valuable here? Haha, of course I mean something that looks valuable - it probably isn't actually valuable, which is why y’all should fork it on over my way. No sense in keeping junk around, haha!”")
print ()
print ("DELHI: “Ma’am, you are dripping with trash. Please, allow me to assist you.”")
print ()
print ("???: “HANDS OFF! NOBODY lays a finger on DOHA, QATAR - OR her trash if they plan on keeping it.”")
print ()
print ("DELHI: “Whoa, calm down! I do not intend any harm, I am just trying to help!”")
print ()
print ("DOHA: “Nobody TOUCHES my junk - I MEAN - my valuables. Get close and I’ll show ya what I’m made of.”")
print ()
print ("She assumes an offensive stance, but slowly slumps back into her regular posture.")
print ()
print ("DOHA: “What am I saying… All I do is drive people away.”")
print ()
print ("DOHA: “My obsession with trash - my", dohaAQI, "AQI MINIMUM. It's what drove my sisters away, my friends. But I just can’t help myself.”")
print ()
print ("She takes a handful of random garbage and throws it in the air, showering herself with empty boxes of Chinese food.")
print ()
print ("ROTTERDAM: “You poor, wayward soul. I can see your AQI skyrocketing by the second, Doha.”")
print ()
print ("YOU: “Clearly, we are all in a similar situation.”")
print ()
print ("Behind you, a loud, confident voice rings out.")
print ()
print ("HÀ NÔI: “AHA! I knew I would find you lot here! Filthy cities - I have come to purge you of your grime! It is I - Hà Nôi, Vietnam! But you may know me as UID", haNoiUID, "! Hear my genius and you will prosper!”")
print ()
print ("He tosses what appears to be a business card on the floor in front of you. In big bold font, it simply reads: “The cleanest city you'll ever meet. Current AQI:", haNoiAQI, "(but usually it's MUCH lower, trust me).”")
print ()
print ("DOHA: “Who the heck is this guy? Y’all know him?”")
print ()
print ("DELHI: “He’s no Jeremy, I can tell you that much. He’s too clean, his eyes look perfectly sane, no foul stench. That’s not my boy.”")
print ()
print ("ROTTERDAM: “Look at his swagger, his confidence… maybe we should listen to him? I mean, if there’s a chance we can change…?”")
print ()
print ("The group looks to you.")
print ()
print (Fore.YELLOW + "_________________________")
print ("Choose how to respond…")
print ()
#These two decisions are pivotal. Decision 1 leads to another brancing path and decision 2 leads to an ending
print ("(1) Give this strange individual a chance.")
print ("(2) Drag him down in the mud with the rest of you.")
print ()
strangerInteractionOneInput = input("[Type a number from 1-2] > ")
print ()
print ("_________________________")
print (Style.RESET_ALL)

if (strangerInteractionOneInput == "1"):
    print ("You look back at your new comrades, then at the stranger.")
    print ()
    print ("YOU: With a sigh, you reply, “Alright, fine. Preach it, sister…”")
    print ()
    print ("His face lights up with a mixture of shock and relief.")
    print ()
    print ("HÀ NÔI: “OH! OHOHO! Well, if you insist!! Ahem~”")
    print ()
    print ("HÀ NÔI: “First and foremost, understand that what I offer will come at a cost. Your large corporations will leave you…”")
    print ()
    print ("DELHI: (“No - my sponsors!)")
    print ()
    print ("HÀ NÔI: “… Your homeless population may have to migrate to a nearby location…”")
    print ()
    print ("DOHA: (“Heheh, suck it Bahrain!”)")
    print ()
    print ("HÀ NÔI: “… You will have to increase your sanitation budget…”")
    print ()
    print ("ROTTERDAM: (“Pfft, like I can afford that on this salary!”)")
    print ()
    print ("HÀ NÔI: “… But you will be pure. And purity is everything.”")
    print ()
    print ("DELHI: “Hmmm, that is a steep cost indeed. But balance it may bring.”")
    print ()
    print ("DOHA: “Nahh, I ain’t buying it. Nothing’s ever fairytales and sunshine where I’m from. What say you, detective/sergeant/private-eye - whatever the hell you are?”")
    print ()
    print ("ROTTERDAM: “You know something… You’re right.”")
    print ()
    print ("HÀ NÔI: “AHAH! I knew you would come to your senses!”")
    print ()
    print ("ROTTERDAM: “No, not you. The hoarder. What am I? Who am I?”")
    print ()
    print ("Your companion ponders his life for a moment.")
    print ()
    print ("ROTTERDAM: “Bah, I’m not cut out for another midlife crisis. Let's ask", playerCity, ".”")
    print ()
    print (Fore.YELLOW + "_________________________")
    print ("Will you accept Hà Nôi’s teachings?")
    print ()
    print ("(1) Commit yourself to a new way of life.")
    print ("(2) Reject his wisdom.")
    print ()
    acceptHindexInput = input("[Type a number from 1-2] > ")    #If decision 2, then initiate battle ending. Else, initiate conform ending
    print ()
    print ("_________________________")
    print (Style.RESET_ALL)

    if (acceptHindexInput == "1"):
        print ("YOU: “I don’t know about you all, but I could use a makeover”")
        print ()
        print ("Although the hoarder seems reluctant, your other companions murmur in agreement.")
        print ()
        print ("HÀ NÔI: “Fantastic! Wonderful!”")
        print ()
        print ("HÀ NÔI: “Let’s start with you, hoarder. Have you tried hoarding… less?”")
        print ()
        print ("DOHA: “Woahhh. You know what - this guy knows his stuff!”")
        print ()
        print ("The discussion continues until each city learns what it takes to be clean.")
        print ()
        print ("It’s not an easy journey. You four lost some of your main sources of income now that the corporations have no place to dump their waste. But despite your economic setbacks, you’ve all found peace.")
        print ()
        print ("Every Sunday, the four of you gather together and reminisce over brunch, speaking of the great times you had in that alleyway. In a single afternoon, the paths of your lives were irreversibly changed. You’ve found each other, but more importantly, you’ve achieved the clout associated with a low Air Quality Index.")
        print ()
        print (Fore.GREEN + "~ GLOWUP ACHIEVED ~")  #The end of one pathway (conform ending)
        print (Style.RESET_ALL)
        sys.exit()

    elif (acceptHindexInput == "2"):
        print ("YOU: “Guys, I have a bad feeling about this. This stranger is not to be trusted.”")
        print ()
        print ("DOHA: “Exactlyyyy. There’s no way this will lead to prosperity. He’s probably just out for our trash.”")
        print ()
        print ("DELHI: “I could go either way. Detective?”")
        print ()
        print ("The grisly man hesitates. He glances down at his empty beer can with a look of uncertainty.")
        print ()
        print ("ROTTERDAM: “Are you sure about this,", playerCity, "? This may be our only chance to be free from all this.”")
        print ()
        print ("YOU: “You can trust me, detective. I know for certain that we should turn down his deal. Please, allow me to explain…”")
        print ()
        print (Fore.YELLOW + "_________________________")
        print ("Type as much as you want to try and persuade your companions:")
        print ()
        #As there would be no way to interpret whatever the user types, their response will be immediately discarded
        #This input is meant to act as a joke because no matter what, the villain will respond the same way
        blankInput = input("> ")   
        print ()
        print ("_________________________")
        print (Style.RESET_ALL)
        print ("The detective looks up at you, misty-eyed. Before he can respond, Hà Nôi chimes in: ")
        print ()
        print ("HÀ NÔI: “Fascinating. Truly fascinating. If I were listening to your speech, I might have accepted your decision. Alas, I neglected to remove my AirPods from my ears. And if you four aren’t with me… then I shall commence my BATTLE PLAYLISTE!! There is nothing you can do to stop me now!”")
        print ()
        print ("YOU: “What the hell-”")     #This pathway is now routed to the battle ending

    else:
        print("Invalid input. Terminating program.")
        sys.exit()
    
elif (strangerInteractionOneInput == "2"):
    print ("YOU: “Screw it. Why fix what’s not broken?”")
    print ()
    print ("DELHI: “What wisdom do you speak,", playerCity, "?”")
    print ()
    print ("YOU: “I mean, think about it a sec. We don't need his hollow words of advice. We're fine as we are.”")
    print ()
    print ("YOU: “In fact, it's him that's the problem. Maybe it's time to break what’s already been fixed?”")
    print ()
    print ("The group whips their heads around to look at Hà Nôi.")
    print ()
    print ("HÀ NÔI: “Ermm????” he exclaims, fumbling to take his AirPods out of his ears.")
    print ()
    print ("DOHA: “YEAH! I’M SMELLING WHAT YOU’RE STEPPIN’ IN,", playerCity.upper(), "!”")  #.upper() preserves Doha's capitalizations
    print ()
    print ("ROTTERDAM: “You mean… even the playing field, so to speak,” he says before taking a swig from his beer can, “There are worse things to do on a Thursday night.”")
    print ()
    print ("DELHI: “If it must be done, then let it be done.”")
    print ()
    print ("HÀ NÔI: “Waitwaitwaitwait, gimme a sec!!!!”")
    print ()
    print ("The frantic stranger scrambles to shove his AirPods back in his ears.")
    print ()
    print ("HÀ NÔI: “If you truly mean to challenge me, then let’s see what you got! With my BATTLE PLAYLISTE playing there’s NOTHING you can do to stop me!”")

else:
    print("Invalid input. Terminating program.")
    sys.exit()

print ()
print (Fore.RED + "_________________________")
print ("COMMENCE BATTLE")       #The start of the battle ending
print (Style.RESET_ALL)
print ("DELHI: “Ah, so it seems we are really doing this,” the wrestler says, injecting himself with his last syringe of steroids. He cracks his knuckles menacingly.")
print ()
print ("The detective takes his empty whiskey bottle and smashes it on the wall, wielding the broken glass as a weapon.")
print ()
print ("ROTTERDAM: “You’re on, pal.”")
print ()
print ("DOHA: “Haha! Just my type of party!!” the hoarder yells, fashioning some of her trash into a makeshift baton.")
print ()
print ("The ensuing battle is surprisingly short-lived. At the first sight of actual danger, Hà Nôi turns tail, but slips on a banana peel in his escape and knocks himself out. The distant sounds of sirens ring louder and louder.")
print ()
print ("ROTTERDAM: “Crap! It’s the 5-0. Scatter, friends!”")
print ()
print ("DELHI: “Wait - are you not a cop yourself?”")
print ()
print ("The detective chuckles, then shrugs his shoulders. Within an instant, he bolts away.")
print ()
print ("DOHA: “It’s been fun, y’all!” the hoarder shouts back at you as she collects as much garbage as she can carry and stumbles into the distance.")
print ()
print ("DELHI: “What a waste of some perfectly fine steroids. Anyhoo, farewell", playerCity, "!” The wrestler leaps onto an adjacent fire escape and clambers upward, out of sight.")
print ()

#Depending on why the player claimed they were in the alleyway, the ending to this will be slightly different
if (playerPurpose == 1):
    print("You find some vials of toxic chemicals scattered around, place a few into your satchel, then march away into the sunset, comforted by the thought that they’ll make an excellent beverage for the coral reefs.")

elif(playerPurpose == 2):
    print("You capture the largest rat you can find, then mosey on into the sunset, with hundreds of magnificent rat children trailing behind you.")

elif(playerPurpose == 3):
    print("You scoop up as much garbage as you can fit in your satchel, knowing they’ll find a fantastic home next to an underfunded middle school.")

elif(playerPurpose == 4):
    print("You hastily finish removing any evidence still lying next to the chalk outline, then mosey away with the knowledge that you can get away with anything.")

print ()
print (Fore.GREEN + "~ STATUS-QUO MAINTAINED ~")    #The end of another pathway (battle ending)
print (Style.RESET_ALL)

sys.exit()
