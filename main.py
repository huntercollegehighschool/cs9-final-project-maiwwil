"""
Name(s): Maia Wilson
Name of Project: The Missing Gem
"""
from time import sleep

#Write the main part of your program here. Use of the other pages is optional.

#import page1  # uncomment if you're using page1
#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4
"""
Storyline:
- You are wandeing in the woods and come across a girl who needs to collect items or she'll be sentenced to death
- you will encounter multiple characters to get items from and some to fight off
- Will she make it?

code:
"""

friendship = False
berries = False

def start():
  print(" * you blink your eyes, as your vision adjusts, you notice a blurry figure staring down at you and trees surrounding her\n")
  sleep(7)
  print("____: hi")
  sleep(1)
  print(".\n")
  sleep(1)
  print(".\n")
  sleep(1)
  print(".\n")
  sleep(1)
  print("____: im sorry i punched you earlier...\n reflexes y'know?")
  sleep(3)
  print("____: well anywho i really am sorry, my names Saph. ")
  sleep(4)
  print("\n * Saph reaches out a hand to helps you up off the ground*")
  sleep(4)
  name = str(input("Saph: so what's your name?: "))
  sleep(2)
  print("\n Saph: well hello,", name, ". I know this is sort of a bad time seeing as i just accidentily knocked you out, but i rly need your help! I'm in grave danger right now, and if I dont find a very valuable gem I think my kingdom will kill me...." )
  sleep(10)
  choice = input("\n Press A to say 'the kingdom will WHAT?', press B to say 'so what exactly do you need to find?', or press C to say 'sure, i will help you!'").upper()
  if choice == "A":
    kingdom(name)
  if choice == "B":
    find(name)
  if choice == "C":
    help(name)


def kingdom(name):
  print("\n Saph: yeahhh, long story short I lost this really valuable gem and now they have this whole execution thing set out, they have a date planned and everything... its sort of scary actually.")
  sleep(8)
  print(name, ": yeah no kidding, that's terrifying. So all we need to do is find some gem in the forest and we'll be good.")
  sleep(6)
  print("Saph: basically! The problem is I don't exactly know where to go... I mean theres some dense woods over there or that lake a bit west...")
  sleep(8)
  choice = input("\n Enter A to venture deep into the woods or B to approach the lake").upper()
  if choice == "A":
    woods(name)
  if choice == "B":
    lake(name, berries, friendship)

def find(name):
  print("\n Saph: It's this opal of the king's. See my family runs a gem polishing business and we're sort of a big deal, and naturally I offer to polish this prized gem and then BAM its lost.")
  sleep(10)
  print(name, ": how do you manage to lose the king's prized opal? did you... drop it or something?")
  sleep(5)
  print("\n Saph: DROP IT? how stupid do you think I am? Well, okay maybe I dropped it, but my theory is that it was stolen by someone when I was walking around with it out here.")
  sleep(9)
  print(name, ": so you took this prized gem out... into the middle of the woods... for a walk? *sigh* You know whatever lets find this stupid thing.")
  sleep(8)
  choice = input("\n But where to find it? Enter A to venture deeper into the tall forest, B to approach a small lake in the distance").upper()
  if choice == "A":
    woods(name)
  if choice == "B":
    lake(name, berries, friendship)

def help(name):
  print("\n Saph: REALLY? okay great, honestly I thought you'd say no and then i'd die for certain. Now my chances are at least 10%!")
  sleep(6)
  print(name,": i'm glad that having a 9 in 10 chance of death is excitable to you, but we should really start exploring...")
  sleep(6)
  choice = input("Enter A to venture deep into the woods or B to approach the lake").upper()
  if choice == "A":
    woods(name)
  if choice == "B":
    lake(name, berries, friendship)
 
 
def woods(name):
  print("\n Saph: good choice, i bet we can find clues for where it went in there")
  sleep(4)
  print("\n * you walk into the woods, and search the ground, but nothing seems out of the ordinary... that is until you notice a strange shadow in the distance, do you approach it? * ")
  sleep(6)
  choice = input("\n Enter A to approach the shadow or S to go back to the start.").upper()
  if choice == "A":
    approach(name)
  elif choice == "S":
    start(name)

def approach(name):
  print("\n Saph: you really think we should go over there? alright i mean you are the expert, not me!")
  sleep(5)
  print("\n * you appraoch the shadow and as you get close you begin to see the form of a short woman with a basket *")
  sleep(6)
  print(name, ": hello?")
  sleep(3)
  print("\n * the woman turns around, fruit flying out of her basket as she looks at you, face drained and eyes widened; terrified*")
  sleep(6)
  print("\n new girl: AH! oh, sorry!! you startled me, my names Mirasol how can i help you?")
  sleep(5)
  print(name, ": oh we didn't mean to do that we were just wondering if you had heard anything about a special gem around these parts, or saw anyone suspicious stealing anything")
  sleep(7)
  print("Mirasol: im not sure if i did... i cant quite recall im still a bit startled")
  sleep(5)
  choice = input("\n try and calm her down! enter a to talk about sunflowers, enter b to talk about people or enter c to talk about worms").upper()
  if choice == "A":
    sunflowers(name)
  if choice == "B":
    people(name)
  if choice == "C":
    worms(name, berries, friendship)

def sunflowers(name):
  print(name, ": Don't worry, everything is fine. Here, think about some nice sunflowers, swaying in the breeze.")
  sleep(6)
  print("\n Mirasol: OH GOD. no no no. not sunflowers. anything but those.")
  print("\n i like flowers, but they should not be moving, i-i mean imagine they start twisting their necks, then their heads")
  sleep(6)
  print("\n and then they are WALKING! and and you can't escape their stupid massive flower heads AHHH")
  sleep(5)
  print("\n * Mirasol has no retreated into fetal position and is trembling with wide paranoid eyes * ")
  sleep(4)
  print("Saph: ofc the girl we appraoch is afraid of flowers, Of COURSE")
  choice = input("change topic! enter A to talk about people B to talk about worms").upper()
  if choice == "A":
    people(name)
  if choice == "B":
    worms(name, berries, friendship)

def people(name):
  print(name, ": Hey, how about you think of some nice people? Do you have any friends?")
  sleep(5)
  print("\n Mirasol: Agh, not exactly, i mean, well, i used to and they were pretty nice. I think they thought i was too timid or something.")
  sleep(5)
  print(name, ": Well I have no clue where they got that from, I think you are perfectly brave in a very normal way. I'm sure tons of people like you")
  sleep(6)
  print("\n Mirasol: well... thanks, i guess not all people are mean to me! I'm thinking a bit clearer now, I think I saw something happening up north, somewhere near the river or tavern or something, i-i i don't know the north is kind of scary.")
  sleep(9)
  print(name, ": That's fine don't stress yourself, we can take it from here, thanks a million!")
  sleep(4)
  print("\n * you and Saph start heading north through the woods until you notice the three places Mirasol had described")
  sleep(5)
  choice = input("\n Press A to go to the river or Press B to go to the tavern ").upper()
  if choice == "A":
    river(name, berries, friendship)
  if choice == "B":
    tavern(name, berries)

def worms(name, berries, friendship):
  print(name, ": Hey, what if you think about... worms! Aren't they funny?")
  sleep(4)
  print("\n Mirasol: worms... worms... WORMS. You like worms? really? Do you have a collection?")
  sleep(5)
  print(name, ": A collection of worms??? Is that even a thing?")
  sleep(4)
  print("\n Mirasol: Oh...i'm sorry i thought you were into worms, they are sort of my favorite thing ever. I mean they are just so cute and they move in such a fascinating way, i mean wow.")
  sleep(7)
  print(name, ": That really does sound cool! I hope you are feeling a bit better now, so do you have any helpful hints for us to find this gem?")
  sleep(6)
  print("\n Oh yep! there is something up north going on I think, somewhere near the river or tavern or something, here take some of my berries for sustinence!")
  berries = True
  sleep(8)
  print("\n * you and Saph take the basket from Marisol and start heading north through the woods until you notice the three places Mirasol had described")
  sleep(8)
  choice = input("\n Press A to go to the river or Press B to go to the tavern ").upper()
  if choice == "A":
    river(name, berries, friendship)
  if choice == "B":
    tavern(name, berries)

def lake(name, berries, friendship):
  print("\n Saph: the lake, huh? I wonder if there's a fisherman there or something. That would be helpful!")
  sleep(5)
  print("\n * you walk towards the lake and notice a form within the deep green water... is it a fish? a human? * ")
  sleep(5)
  print("\n", name, ": hello? is someone there?")
  sleep(3)
  print("\n * you and Saph get closer towards the lake as you see strands of hair and scales peaking through the water. * ")
  sleep(6)
  print("\n ____: WOOH! HIYA!")
  sleep(3)
  print("Saph: ... is that... a mermaid?")
  sleep(3)
  print("\n ____: ABSOLUTELY, I'M NAIA! Gosh, nobody comes around these parts i'm so EXCITED for visitors!")
  sleep(6)
  print(name, ": We are too, but we need to find something, could you help us?")
  sleep(5)
  print("Naia: hmmm under one condition, do you know what 3 + 3 is")
  sleep(5)
  print('\n', name, ": I'm sorry but this is a serious matter we don't have time for-")
  sleep(3)
  number = int(input("\n Naia: i AM serious, what. is. 3+3:"))
  total = 0
  if number == 6:
    print("\n Naia: DING DING DING")
    total = total + 1
  else:
    print("\n NOPE, try again,")
  sleep(3)
  print("Saph: what in the world is up with this girl.")
  sleep(4)
  number1 = int(input("\n Naia: I'm not a girl remember, now go, 30 times 70:"))
  if number1 == 210:
    print("\n Naia: correct!")
    sleep(2)
    total = total + 1
  else:
    print("\n nuh uh,")
    sleep(2)
  number2 = int(input("\n Naia: 32 times 49"))
  if number2 == 1568:
    print("\n Naia: WOOH, one last one")
    sleep(3)
    total = total + 1
  else:
    print("\n wrong! just one last one, okay? ")
    sleep(3)
  number3 = int(input("\n Naia: 189 TIMES 2 PLUS 6 DIVIDED BY 3"))
  if number3 == 128:
    print("\n Naia: YEPP")
    sleep(1)
    total = total + 1
  else:
    print("\n incorrect!")
    sleep(1)
  if total == 4:
    print("\n Naia: You got them all right WOOHOO! Alright so where were we... DIRECTIONS to help you find that gem...hmm I think i saw something near the tavern or around the river area!")
    friendship = True
  else:
    print("\n Naia: Well... you did pretty okay, so where were we... DIRECTIONS to help you find that gem...hmm I think i saw something near the tavern or around the river area")
  sleep(7)
  print(name, "Okay! Thanks Naia for the tip, have a fun time with your... math?")
  sleep(4)
  print("\n * You and Saph walk away from the strange mermaid girl and continue towards the river area... but where to go? *")
  sleep(5)
  choice = input("\n Press A to go to the river or Press B to go to the tavern ").upper()
  if choice == "A":
    river(name, berries, friendship)
  if choice == "B":
    tavern(name, berries)

def river(name, berries, friendship):
  print("\n Saph: The river feels like a place a dropped gem might be... or where a THIEF would go.")
  sleep(5)
  print(name, ": Right of course, a 'thief'")
  sleep(3)
  print("\n * You and Saph approach the river, noticing something small and shiny in the water and an ominous shadow approach in the water *")
  sleep(8)
  print("\n Saph: wait- IS THAT MY GEM?")
  sleep(3)
  print(name, ": I think so... how do we get it out? The water doesn't look super... safe")
  sleep(5)
  if berries == True:
    print("\n Saph: I've got an idea, I can use the berries Mirasol gave us as bait to lure them away")
    sleep(5)
    print(name, "not bad thinking... ")
    sleep(3)
    print("\n * Saph kneels down next to the river, ofering out a hand filled with delicious berries. You feel a presense come closer until... *")
    sleep(6)
    print("\n Saph: AHHHHH")
    sleep(2)
    print("\n * A strange fish-like creature had not only taken the berries, but her arm with it... I suppose her plan wasn't too good after all.")
    sleep(7)
    print(name, ": SAPH! Saph are you okay? I'll get a bandage or a- a piece of cloth, Saph can you hear me?")
    sleep(5)
    print("\n * no response *")
    sleep(2)
    print(name, ": Saph... saph... I wish, If only I could just redo it all, so that this would never have happened...")
    sleep(1)
    print(".\n")
    sleep(1)
    print(".\n")
    sleep(1)
    print(".\n")
    sleep(1)
    print("\n * The end * ")
  if friendship == True:
    print("\n Saph: I have... no clue, it looks pretty unsafe")
    sleep(4)
    print(name, ": There's got to be a way to get it out of there hmmm")
    sleep(5)
    print("\n * As you say this, the shadow in the water comes closer and closer, swimming faster as it approaches you *")
    sleep(6)
    print("\n Naia: You called?")
    sleep(2)
    print(name, ": GAHh, Jeez you scared me Naia, how did you even get here?")
    sleep(4)
    print("\n Naia: Well the lake and river are connected and so I thought I'd check it out to try and help, especially since your math skills impressed me!")
    sleep(8)
    print("\n Saph: I'm glad you are impressed by their skills, but could you pick up the gem for us?")
    sleep(6)
    print("\n * Naia dips back under the water and returns with a large, shiny opal in her hand. She places it in Saph's open palm. * ")
    sleep(6)
    print("\n Saph: THANK YOU! You two are really the best, I'm glad you found this for me, truly!")
    sleep(7)
    print(name, ": no problem, I'm glad that we could help you!")
    sleep(4)
    print(".\n")
    sleep(1)
    print(".\n")
    sleep(1)
    print(".\n")
    sleep(1)
    print("\n * The end * ")
  else:
    print("\n Saph: I have... no clue, it looks pretty unsafe")
    sleep(4)
    print(name, ": There's got to be a way to get it out of there hmmm")
    sleep(5)
    print("\n .....")
    sleep(1)
    print("\n Saph: Whatever, I'm sorry to have bothered you so much, thanks for your help...")
    sleep(4)
    print(name, ": No, no I NEED to help you, we can figure this out-")
    sleep(4)
    print("\n Saph: It isn't worth it. It's fine... just go home, It was impossible anyways, thank you, dearly.")
    sleep(6)
    print(" * Saph gives you a small smile before turning around and walking off into the distance * ")
    sleep(4)
    print(".\n")
    sleep(1)
    print(".\n")
    sleep(1)
    print(".\n")
    sleep(1)
    print("\n * The end * ")
          
def tavern(name, berries):
  print("\n Saph: The tavern feels like a great place to find a stolen gem!")
  sleep(5)
  print(name, ": And that's why I chose it.")
  sleep(3)
  print("\n * You and Saph approach the tavern, noticing the bright yellow lights eminating from the inside, you hear a loud mans voice coming from inside, and enter. *")
  sleep(8)
  print("\n Random Man: 400 coins for my gem? I'd need at LEAST 4000 HAH hah!")
  sleep(4)
  print("\n Saph: hold on", name, "that guy... he's holding my gem!")
  sleep(3)
  print(name, ": Hey! That gem you're trying to sell is my friends, give it back.")
  sleep(5)
  print("\n * The man walks menaningly towards you, holding the gem in his hand. *")
  sleep(5)
  print("\n Random Man: Or what? Finders keepers, you and your little friend are too late.")
  sleep(5)
  if berries == True:
    print("\n Saph: Hey! Why don't we make a trade. I've got a whole basket of gold in exchange for my gem.")
    sleep(5)
    print(name, ": No we don-")
    sleep(3)
    print("\n Random Man: Now that's what i like to hear, gimme that")
    sleep (5)
    print("\n * Saph tosses him the berry basket, covered with a cloth as to not reveal its true contents and he tosses over the gem, and you two RUN *")
    sleep(8)
    print("\n Saph: WOOH! I can't believe I fooled that guy with those berries!")
    sleep(5)
    print(name, ": Yeah me neither, thank god we had them, and now you'll be safe.")
    sleep(4)
    print("\n Saph: Yep, and it's all thanks to you. Thank you so much for helping me. I couldn't have done this alone.")
    sleep(6)
    print(".\n")
    sleep(1)
    print(".\n")
    sleep(1)
    print(".\n")
    sleep(1)
    print("\n * The end * ")
  else:
    print("\n Saph: Uhh...uhhh")
    sleep(3)
    print("\n Random Man: Hey aren't you that criminal girl in the papers, HAH she is, isn't she. Trying to save yourself from excecution?")
    print("\n Saph: I'm not a criminal, I-I just really need that gem back")
    sleep(5)
    print("\n Random Man: Well that's too bad, but you know what happens to those who upset the king...")
    sleep (6)
    print("\n * Other people in the bar crowd around Saph, one putting her in handcuffs and the others escorting her outside *")
    sleep(8)
    print("\n Random Man: Don't try to run away and fix your problems like that again!")
    sleep(5)
    print("\n * You watch as she's escorted onto a carriage and you stand back, unable to stop the authorities from taking her.")
    sleep(6)
    print("\n", name, ": I've failed her... I wish I could go back and fix this all, but I can't.")
    sleep(6)
    print(".\n")
    sleep(1)
    print(".\n")
    sleep(1)
    print(".\n")
    sleep(1)
    print("\n * The end * ")
      
print(start())
