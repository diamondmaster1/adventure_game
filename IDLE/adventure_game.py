import time,random,sys

inventory=[]

def read(sentence):
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

goblin_health=110
goblin_skill=7
goblin_strength=12

def hero_attack():
    global goblin_health
    if dice()>hero_skill:
        print("you have hit the goblin")
        time.sleep(0.5)
        damage=dice()*hero_strength
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


def goblin_attack():
    global hero_health
    if dice()>goblin_skill:
        print("you have hit the hero")
        time.sleep(0.5)
        damage=dice()*goblin_strength
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


def goblin_fight_hero():
    while hero_health > 0:
        hero_attack()
        if goblin_health > 0:
            goblin_attack()
            if hero_health < 1:
                print("you are dead")
                break
        else:
            print("you have won the battle but not the war")
            break


def goblin_fight_time():
    start_time=time.time()
    goblin_fight_hero()
    end_time=time.time()
    fight_time=end_time-start_time
    fight_time=round(fight_time,2)
    print("your fight time is",fight_time,"s")


read("you enter a metal gate")
time.sleep(0.5)
read("you see a goblin blocking your path;time to fight hero")
time.sleep(0.5)
goblin_fight_time()
time.sleep(0.5)
read("you have accquired the missiles")
time.sleep(0.5)
read("it will be added to your inventory")
time.sleep(0.5)
inventory=inventory.append("missiles")
print(inventory)
read("There is a collosal stone wall in front of you")
time.sleep(0.5)
read("You shoot it down with your missiles")
time.sleep(0.5)
read("you walk down a narrow, spooky road until you reach a crossroad that will determine your fate")
time.sleep(0.5)
choice_1=input("you can choose between the icy depths or the firey hellscape")
if choice_1 == "icy depths":
    read("There is a sign saying welcome and beware of any icy giants")
    time.sleep(0.5)
    read("You start to feeling empty inside and start craving a warm coat")
    time.sleep(0.5)
    read("You start to lose health by the minute")
    time.sleep(0.5)
    read("You suddenly see a snoty nosed goblin with a thick, warm coat on it")
    time.sleep(0.5)
    read("You decided to fight the being in combat;it's time to fight hero")
    time.sleep(0.5)
    goblin_fight_time()
    time.sleep(0.5)
    read("you have accquired the warm coat")
    time.sleep(0.5)
    read("It will be added into your inventory")
    time.sleep(0.5)
    print(inventory)
    read("you start to feel as if your heart is flooding in with emotions again")
    time.sleep(0.5)
    read("You start to dance as if you were a child again")
    time.sleep(0.5)
    read("But your mind rudely interupts you with your task to rescue your sister from the 'meancing monster' ")
    time.sleep(0.5)
    read("You give a shrug as in you are accepting your fate and decide to carry on the fight")
    time.sleep(0.5)
    read("You decide the head into the Caves of Despair")
    time.sleep(0.5)
    read("'But wait' your brain warns you about the dangers of the cave as you don't have a flashlight")
    time.sleep(0.5)
    choice_2=input("do you decide to 'walk as if you were blind' or 'accquire a flashlight in order to see'? ")
    if choice_2 == "walk as if you were blind":
        read("you decide the dumb option but a brave one in order to become a hero")
        time.sleep(0.5)

    



