import time,random,sys,os

inventory=[]

def progress_bar(seconds):
  for progress in range(0,seconds+1):
    percent = (progress * 100) // seconds
    print("\n")
    print("Loading...")
    print("<" + ("=" * progress) + (" " * (seconds-progress)) + "> " + str(percent) + "%")
    print("\n")
    time.sleep(1)
    os.system('clear')

progress_bar(2)

def fast_text(sentence):
    for char in sentence:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print(" ")

def dice():
    roll=random.randint(0,20)
    return roll

hero_health=100
hero_skill=5
hero_strength=10
hero_level=1
current_exp=0
hero_berries=1000
hero_magic=25

goblin_health=110
goblin_skill=7
goblin_strength=12
goblin_level=3

ice_giant_health=110
ice_giant_skill=7
ice_giant_strength=12
ice_giant_level=4

grim_reaper_health=1000
grim_reaper_skill=50
grim_reaper_strength=120
grim_reaper_level=30


def hero_attack_goblin():
    global goblin_health
    if dice()>hero_skill:
        print("you have hit the goblin")
        time.sleep(0.5)
        damage=dice()*hero_strength+hero_level
        time.sleep(0.5)
        print(damage,"damage")
        time.sleep(0.5)
        goblin_health -= damage
        time.sleep(0.5)
        print("remaining goblin health is",goblin_health)
        time.sleep(0.5)
    else:
        time.sleep(0.5)
        print("too bad hero")


def hero_attack_ice_giant():
    global ice_giant_health
    if dice()>hero_skill:
        print("you have hit the ice giant")
        time.sleep(0.5)
        damage=dice()*hero_strength+hero_level
        time.sleep(0.5)
        print(damage,"damage")
        time.sleep(0.5)
        ice_giant_health -= damage
        time.sleep(0.5)
        print("remaining ice giant health is",ice_giant_health)
        time.sleep(0.5)
    else:
        time.sleep(0.5)
        print("too bad hero")

def hero_attack_grim_reaper():
    global grim_reaper_health
    if dice()>hero_skill:
        print("you have hit the 'grim reaper'")
        time.sleep(0.5)
        damage=dice()*hero_strength+hero_level
        time.sleep(0.5)
        print(damage,"damage")
        time.sleep(0.5)
        grim_reaper_health -= damage
        time.sleep(0.5)
        print("remaining 'grim reaper' health is",grim_reaper_health)
        time.sleep(0.5)
    else:
        time.sleep(0.5)
        print("too bad hero")




def goblin_attack():
    global hero_health
    if dice()>goblin_skill:
        print("you have hit the hero")
        time.sleep(0.5)
        damage=dice()*goblin_strength+goblin_level
        time.sleep(0.5)
        print(damage,"damage")
        time.sleep(0.5)
        hero_health-= damage
        time.sleep(0.5)
        print("remaining hero health is",hero_health)
        time.sleep(0.5)
    else:
        time.sleep(0.5)
        print("too bad goblin")

def ice_giant_attack():
    global hero_health
    if dice()>ice_giant_skill:
        print("you have hit the hero")
        time.sleep(0.5)
        damage=dice()*ice_giant_strength+ice_giant_level
        time.sleep(0.5)
        print(damage,"damage")
        time.sleep(0.5)
        hero_health-= damage
        time.sleep(0.5)
        print("remaining hero health is",hero_health)
        time.sleep(0.5)
    else:
        time.sleep(0.5)
        print("too bad ice giant;better luck next time")

def grim_reaper_attack():
    global hero_health
    if dice()>grim_reaper_strength:
        print("you have hit the hero;it is time for 'him' to die? ")
        time.sleep(0.5)
        damage=dice()*grim_reaper_strength+grim_reaper_level
        time.sleep(0.5)
        print(damage,"damage;you might actually die now")
        time.sleep(0.5)
        hero_health-= damage
        time.sleep(0.5)
        print("remaining hero health is",hero_health)
    else:
        time.sleep(0.5)
        print("too bad ice giant;better luck next time")





def goblin_fight_hero():
    global hero_level
    global current_exp
    while hero_health > 0:
        hero_attack_goblin()
        if goblin_health > 0:
            goblin_attack()
            if hero_health < 1:
                print("you are dead")
                break
        else:
            print("you win!!!!!!")
            exp=random.randint(5,10)
            for i in range(exp):
                current_exp += i
                print("you have gained",current_exp)
                if current_exp > 500:
                    hero_level += 1
                    print("you have just leveled up")
                    time.sleep(0.5)
                    print("your level is now",hero_level)
                else:
                    print("you have not leveled up yet")
                break
            break


def ice_giant_fight_hero():
    global hero_level
    global current_exp
    while hero_health > 0:
        hero_attack_ice_giant()
        if ice_giant_health > 0:
            ice_giant_attack()
            if hero_health < 1:
                print("you are dead")
                break
        else:
            print("you win!!!!!!")
            exp=random.randint(20,40)
            for i in range(exp):
                current_exp += i
                print("you have gained",current_exp)
                if current_exp > 500:
                    hero_level += 1
                    print("you have just leveled up")
                    time.sleep(0.5)
                    print("your level is now",hero_level)
                else:
                    print("you have not leveled up yet")
                break
            break

def grim_reaper_fight_hero():
    global hero_level
    global current_exp
    while hero_health > 0:
        hero_attack_grim_reaper()
        if grim_reaper_health > 0:
            grim_reaper_health()
            if hero_health < 1:
                print("you are dead")
                time.sleep(0.5)
                print("you were destined to lose this fight as the 'grim reaper' is the most powerful foe in the 'magical cinematic universe'")
                time.sleep(0.5)
                break
        else:
            print("you win!!!!!!")
            exp=random.randint(500,1000)
            for i in range(exp):
                current_exp += i
                print("you have gained",current_exp)
                if current_exp > 500:
                    hero_level += 1
                    print("you have just leveled up")
                    time.sleep(0.5)
                    print("your level is now",hero_level)
                else:
                    print("you have not leveled up yet")
                break
            break



def goblin_fight_time():
    start_time=time.time()
    goblin_fight_hero()
    end_time=time.time()
    fight_time=end_time-start_time
    fight_time=round(fight_time,2)
    print("your fight time is",fight_time,"s")

def ice_giant_fight_time():
    start_time=time.time()
    ice_giant_fight_hero()
    end_time=time.time()
    fight_time=end_time-start_time
    fight_time=round(fight_time,2)
    print("your fight time is",fight_time,"s")

def grim_reaper_fight_time():
    start_time=time.time()
    grim_reaper_fight_hero()
    end_time=time.time()
    fight_time=end_time-start_time
    fight_time=round(fight_time,2)
    print("your fight time is",fight_time,"s")



def item_shop():
    global hero_berries
    global hero_strength
    global hero_health
    global hero_magic
    weapons={"Shimmering Katana":"20 berries",
             "The Sword of Kyros":"45 berries",
             "Yubashiri":"500 berries"}
    items={"Water":"10 berries",
           "Fire Spirit":"25 berries",
           "Ope Ope no mi":"1000 berries"}
    buying=input("Would you like to come in (y/n)")
    if buying == "y":
        what_to_buy=input("Would you like to buy an item or a weapon (i/w)")
        if what_to_buy == "w":
            weapons.items()
            for key,value in weapons.items():
                print(key,value)
            buying_weapon=input("What would you like to buy? ")
            if buying_weapon == "Shimmering Katana":
                print("thank you for purchasing the 'shimmering katana'")
                time.sleep(0.5)
                print("It will be added into your inventory")
                time.sleep(0.5)
                inventory.append("shimmering katana")
                print(inventory)
                time.sleep(0.5)
                hero_berries -= 20
                print("you have",hero_berries,"berries left")
                time.sleep(0.5)
                print("Thank you for buying, hope to see you soon")
            elif buying_weapon == "The Sword of Kyros":
                print("thank you for purchasing the 'the sword of Kyros'")
                time.sleep(0.5)
                print("It will be added into your inventory")
                time.sleep(0.5)
                inventory.append("the sword of Kyros")
                print(inventory)
                time.sleep(0.5)
                hero_berries -= 45
                print("you have",hero_berries,"berries left")
                time.sleep(0.5)
                print("Thank you for buying, hope to see you soon")
            elif buying_weapon == "Yubashiri":
                print("thank you for purchasing 'Yubashiri'")
                time.sleep(0.5)
                print("It will be added into your inventory")
                time.sleep(0.5)
                inventory.append("Yubashiri")
                print(inventory)
                time.sleep(0.5)
                hero_berries -= 500
                print("you have",hero_berries,"berries left")
                time.sleep(0.5)
        if what_to_buy == "i":
            items.items()
            for key,value in items.items():
                print(key,value)
            buying_weapon=input("What would you like to buy? ")
            if buying_weapon == "Water":
                print("thank you for purchasing the 'Water'")
                time.sleep(0.5)
                print("you have just gained 20 health")
                time.sleep(0.5)
                hero_health += 20
                print("your health is now",hero_health)
                time.sleep(0.5)
                hero_berries -= 10
                print("you have",hero_berries,"berries left")
                time.sleep(0.5)
                print("Thank you for buying, hope to see you soon")
            elif buying_weapon == "Fire Spirit":
                print("thank you for purchasing the 'Fire Spirit'")
                time.sleep(0.5)
                print("It will be added into your inventory")
                time.sleep(0.5)
                inventory.append("fire spirit")
                print(inventory)
                time.sleep(0.5)
                print("you have just gained 10 strength")
                time.sleep(0.5)
                hero_strength += 10
                print("your strength is now",hero_strength)
                time.sleep(0.5)
                hero_berries -= 25
                print("you have",hero_berries,"berries left")
                time.sleep(0.5)
                print("Thank you for buying, hope to see you soon")
            elif buying_weapon == "Ope Ope no mi":
                print("thank you for purchasing 'Ope Ope no mi'")
                time.sleep(0.5)
                print("It will be added into your inventory")
                time.sleep(0.5)
                inventory.append("ope ope no mi")
                print(inventory)
                time.sleep(0.5)
                hero_berries -= 1000
                print("you have",hero_berries,"berries left")
                time.sleep(0.5)
                print("you have just gained 50 magic")
                time.sleep(0.5)
                hero_magic += 50
                print("your magic is now",hero_magic)

def restaurant ():
    global hero_berries
    global hero_health
    global hero_strength
    global current_exp
    food_menu={"Prawn cocktail crisps":"20 berries",
               "Thick chicken thigh":"100 berries",
               "One slice of pizza":"500 berries"}
    choice_food=input("Do you want to eat (y/n)? ")
    if choice_food == "y":
        food_menu.items()
        for key,value in food_menu.items():
            print(key,value)
        eating_food=input("What would you like to eat? ")
        if eating_food == "Prawn cocktail crisps":
            print("Thank you for buying 'Prawn cocktail crisps")
            time.sleep(0.5)
            hero_berries -= 20
            print("you have",hero_berries,"left")
            time.sleep(0.5)
            hero_health -= 15
            print("your current health is",hero_health)
            time.sleep(0.5)
            current_exp += 5
            print("your current exp is",current_exp)
            time.sleep(0.5)
            print("Thank you for eating;hope you come again soon")
        elif eating_food == "Thick chicken thigh":
            print("Thank you for buying 'Thick chicken thigh")
            time.sleep(0.5)
            hero_berreis -= 100
            print("You have",hero_berries,"left")
            time.sleep(0.5)
            hero_health += 50
            print("your current health is",hero_health)
            time.sleep(0.5)
            hero_strength += 25
            print("Your current strength is",hero_strength)
            time.sleep(0.5)
            current_exp += 50
            print("Your current exp is",current_exp)
            time.sleep(0.5)
            print("Thank you for eating;hope you come again soon")
        elif eating_food == "One slice of pizza":
            print("Thank you for buying 'One splice of pizza")
            time.sleep(0.5)
            hero_berries -= 500
            print("You have",hero_berries,"left")
            time.sleep(0.5)
            hero_health -= 5
            print("Your current health is",hero_health)
            time.sleep(0.5)
            hero_strength += 5
            print("Your current strength is",hero_strength)
            time.sleep(0.5)
            current_exp += 200
            print("Your current exp is",current_exp)
            time.sleep(0.5)
            print("Thank you for eating;hope you come again soon")
            
fast_text("you enter a metal gate")
time.sleep(0.5)
fast_text("you see a goblin blocking your path;time to fight hero")
time.sleep(0.5)
goblin_fight_time()
time.sleep(0.5)
fast_text("you have accquired the missiles")
time.sleep(0.5)
fast_text("it will be added to your inventory")
time.sleep(0.5)
inventory.append("missiles")
print(inventory)
time.sleep(0.5)
fast_text("you suddenly see a giantic figure in the distance")
time.sleep(0.5)
fast_text("you are naturally hesitate to approach")
time.sleep(0.5)
fast_text("However, the giantic figure starts to approach to a deathly walts")
time.sleep(0.5)
fast_text("You start to panic as you start to equipe your missiles")
time.sleep(0.5)
fast_text("As the figure walts closer and closer to you, you find out he is the 'grime reaper'")
time.sleep(0.5)
fast_text("'you have to fight it'you quickly start to realise")
time.sleep(0.5)
fast_text("it's time to fight hero")
time.sleep(0.5)
fast_text("the 'grim reaper' suddenly becomes more friendly as you have failured to kill him")
time.sleep(0.5)
fast_text("But, he is willing to make a deal")
time.sleep(0.5)
fast_text("You can either use his 'item shop' and gain the benefits but if you accept,there will be 3 rules in the contract")
time.sleep(0.5)
fast_text("Rule 1: you can't harm or kill the 'grim reaper' ever")
time.sleep(0.5)
fast_text("Rule 2: You can never ever kill wild animals or innocent civilans")
time.sleep(0.5)
fast_text("Rule 3: You can never harm 'the king' or the 'big bad' in this universe (this is the reason why you set out on this journey in the first place btw)")
time.sleep(0.5)
fast_text("If you don't accept, you can carry on your journey but there will be no hope in killing the 'big bad'")
time.sleep(0.5)
chocie_0=fast_text("Do you accept this conditions? (y/n)")
if chocie_0 == "y":
    fast_text("congratulations, you are able to use the item shop, happy shopin       for now")
    item_shop()
    fast_text("There is a collosal stone wall in front of you")
    time.sleep(0.5)
    fast_text("You shoot it down with your missiles")
    time.sleep(0.5)
    fast_text("you walk down a narrow, spooky road until you reach a crossroad that will determine your fate")
    time.sleep(0.5)
    choice_1=input("you can choose between the icy depths or the firey hellscape")
    if choice_1 == "icy depths":
        fast_text("There is a sign saying welcome and beware of any icy giants")
        time.sleep(0.5)
        fast_text("You start to feeling empty inside and start craving a warm coat")
        time.sleep(0.5)
        fast_text("You start to lose health by the minute")
        time.sleep(0.5)
        fast_text("You suddenly see a snoty nosed goblin with a thick, warm coat on it")
        time.sleep(0.5)
        fast_text("You decided to fight the being in combat;it's time to fight hero")
        time.sleep(0.5)
        goblin_fight_time()
        time.sleep(0.5)
        fast_text("you have accquired the warm coat")
        time.sleep(0.5)
        fast_text("It will be added into your inventory")
        time.sleep(0.5)
        inventory.append("warm coat")
        print(inventory)
        time.sleep(0.5)
        fast_text("you start to feel as if your heart is flooding in with emotions again")
        time.sleep(0.5)
        fast_text("You start to dance as if you were a child again")
        time.sleep(0.5)
        fast_text("But your mind rudely interupts you with your task to rescue your sister from the 'meancing monster' ")
        time.sleep(0.5)
        fast_text("You give a shrug as in you are accepting your fate and decide to carry on the fight")
        time.sleep(0.5)
        fast_text("You decide the head into the Caves of Despair")
        time.sleep(0.5)
        fast_text("'But wait' your brain warns you about the dangers of the cave as you don't have a flashlight")
        time.sleep(0.5)
        choice_2=input("do you decide to 'walk as if you were blind' or 'accquire a flashlight in order to see'? ")
        if choice_2 == "walk as if you were blind":
            fast_text("you decide to pick the dumb option but a brave one in order to become 'the' hero")
            time.sleep(0.5)
            fast_text("you start to stumble")
            time.sleep(0.5)
            fast_text("and suddenly a goblin appears from out of nowhere;it is time to fight hero")
            time.sleep(0.5)
            goblin_fight_time()
            time.sleep(0.5)
            fast_text("you have just received malaria")
            time.sleep(0.5)
            fast_text("your health has decreased by 30")
            time.sleep(0.5)
            hero_health -= 30
            print("your health is now", hero_health)
            time.sleep(0.5)
            fast_text("you start to hop on one knee as if you are about to die")
            time.sleep(0.5)
            fast_text("But suddenly you see that an icy giant has the 'cure' for malaria")
            time.sleep(0.5)
            fast_text("Without thinking, you start to lunge towards the ice giant in order to fight for your life")
            time.sleep(0.5)
            fast_text("it's time to fight hero")
            time.sleep(0.5)
            ice_giant_fight_time()
            time.sleep(0.5)
            fast_text("you have received the medicine")
            time.sleep(0.5)
            fast_text("congratulations, you have just received 40 health")
            time.sleep(0.5)
            hero_health += 40
            print("your health is now", hero_health)
            time.sleep(0.5)
            fast_text("you start to walk for an agonizing amount of minutes")
            time.sleep(0.5)
            fast_text("you start to see a lingering light in front of you") 
            time.sleep(0.5)
            fast_text("you want to walk towards it")
            time.sleep(0.5)
            fast_text("you have discovered the kitchen;there is an ice giant waiting for you")
            time.sleep(0.5)
            fast_text("It is time to fight")
            time.sleep(0.5)
            ice_giant_fight_time()
            time.sleep(0.5)
            fast_text("you have reached 'the outside world'")
            time.sleep(0.5)
            fast_text("you suddenly see a strange figure in the distance")
            time.sleep(0.5)
            fast_text("It is the stranger you met eariler in your journey")
            time.sleep(0.5)
            fast_text("It is time to shop")
            time.sleep(0.5)
            item_shop()
            time.sleep(0.5)
            fast_text("You continue to wander around;wondering where your next meal is? ")
            time.sleep(0.5)
            fast_text("You suddenly see a collsol building in front of you which has a sense of duality")
            time.sleep(0.5)
            fast_text("You find the infrastructure odd and perplexing but oddly inspiring and grand")
            time.sleep(0.5)
            choice_3=fast_text("Do you wish to enter the building? (y/n)")
            if choice_3 == "y":
                fast_text("You decide to enter the building 'of doom? '")
                time.sleep(0.5)
                fast_text("You suddenly find yourself, mouth agap as you take in the charming and handsome arichtecture of a chair")
                time.sleep(0.5)
                fast_text("'Hey, what are you doing here?'A stranger exclaimed. You explain that you stumbled across this place as you needed 'help'")
                time.sleep(0.5)
                fast_text("You were causally surprised as he decided to serve you some food 'for a price of course'as you sign with relief and regret")
                time.sleep(0.5)
                restaurant()
                time.sleep(0.5)
                # fast_text("")
