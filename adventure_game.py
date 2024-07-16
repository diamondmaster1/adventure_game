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

progress_bar(10)

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

goblin_health=110
goblin_skill=7
goblin_strength=12
goblin_level=3

ice_giant_health=110
ice_giant_skill=7
ice_giant_strength=12
ice_giant_level=4


def hero_attack_goblin():
    global goblin_health
    if dice()>hero_skill:
        print("you have hit the goblin")
        time.sleep(0.5)
        damage=dice()*hero_level
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



def goblin_attack():
    global hero_health
    if dice()>goblin_skill:
        print("you have hit the hero")
        time.sleep(0.5)
        damage=dice()*goblin_level
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
        damage=dice()*ice_giant_level
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
    



