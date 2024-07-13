import time,random,sys

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


print("you enter a metal gate")
time.sleep(1)
print("you see a goblin blocking your path;time to fight")
time.sleep(1)
goblin_fight_time()
time.sleep(1)
