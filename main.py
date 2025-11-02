import time
from time import sleep
import random
import sys
import os
import pygame


sleep(3)

enemies = ["Skeleton", "Toxic Spider", "Goblin", "Zombie", "Dragon", "Wrathful Wraith",]
strong_enemies = ["Soul Reaper", "Rage Knight", "Great Ghoul", "Final Froggit", "Faceless Being", "Dread Devourer"]
attackdelay = 2
choice1 = None
attackchance = 10
hp = 120
char = "UNSET"
enemyalive = True
cloak = False

if os.name == "nt":
    os.system('cls')
else:
    os.system('clear')
    
def slowprint(text, speed=0.041):
    
    for char in text: 
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(speed)
        
    print()    
    
def attacknormal(hp):
    pygame.mixer.music.stop()
    pygame.mixer.music.load("combatnormal.mp3")
    pygame.mixer.music.play(-1,0.0)
    enemyhp = 120
    enemy = random.choice(enemies)
    enemyhp += random.randint(-20, 20)
    slowprint("\n!!!!!!!!!")
    sleep(3)
    slowprint("\n!!!!!!!!! AN ENEMY APPROACHES! INCOMING!")
    sleep(3)
    slowprint(f"\n A {enemy} assails you! A fight begins. This {enemy} has {enemyhp} health.\n Enemy attacks deal 20-30 damage (you have {hp}), and they have a 5 percent chance to miss. \nEnemies have a 15% chance to regain 30 hp per round! \n\n")
    
    while enemyhp > 0 and hp > 0:
        slowprint("\nYOUR TURN! Swords deal 30 damage but have a 10 percent chance to miss.\n Pikes deal anywhere from 25 to 50 but have a 20 percent chance to miss. \n Daggers are guaranteed to deal 20 damage.\n You can also choose to Heal, regaining 30 hp.")
        attack = input("\n\nWhich attack do you choose? (sword/pike/dagger/heal)\n\n")
        sleep(1)
        if attack.lower() == "devweaponaim54mk60":
            enemyhp = 0
        if attack.lower() == "sword":
            chance = random.randint(0,100)
            if chance > 10:
                enemyhp -= 30
                slowprint(f"\nYou strike the {enemy} with your sword, dealing 30 damage!\n")
            else:
                slowprint(f"\nYou swing your sword at the {enemy}, but it misses!")
        elif attack.lower() == "pike":
            chance = random.randint(0,100)
            if chance < 80:
                damage = random.randint(25,50)
                enemyhp -= damage
                slowprint(f"\nYou strike the {enemy} with your pike, dealing {damage} damage!\n")
            else:
                slowprint(f"\nYou swing your pike at the {enemy}, but it misses!")
            sleep(1)
        elif attack.lower() == "dagger":
            enemyhp -= 20
            slowprint(f"\nYou strike the {enemy} with your dagger, dealing 20 damage!\n")
            sleep(1)
        elif attack.lower() == "heal":
            if hp <= 80:
                hp = hp + 30
                slowprint(f"\nYou heal yourself, regaining 30 health!\nYou have {hp} health left.")
            elif hp + 25 > 120:
                slowprint(f"\nYou heal, but since you're so close to maximum HP, you may only heal up to 120. You have 120 hp left.\n")
                hp = 120
        else:
            slowprint(f"\nYou reach for the wrong weapon. You don't make it before the {enemy} charges.")
            sleep(1)
            
        if enemyhp <= 0:
            slowprint(f"\n\n\nYou have defeated {enemy}!")
            sleep(1)
            
            if hp > 80:
                slowprint(f"\n\nYou feel alright with {hp} health. You forge on.")
                return(None)
            else:
                hp1 = hp
                hp = random.randint(80,120)
                slowprint(f"\n\nYou are injured and have {hp1} health left. You take a moment to chug down a healing potion, returning to {hp} hp.")
                return(None)
            
        sleep(0.5)
        slowprint(f"\nThe {enemy} has {enemyhp} health remaining.")
        sleep(1)
        slowprint("\nThe enemy attacks!!")
        sleep(2)
        
        chance = random.randint(0,100)
        if chance > 5:
            damage = random.randint(20,30)
            hp -= damage
            slowprint(f"\nYou are hit!! The enemy deals {damage} damage. You have {hp} health left.")
        else:
            slowprint(f"\nThe {enemy} misses!")
            
        chance = random.randint(0,100)
        sleep(0.5)
        
        if chance > 85:
            slowprint(f"\nUnfortunately for you, the {enemy} manages to heal up 30hp!\n\n")
            enemyhp += 30
    
    if hp <= 0:
        slowprint("\n\n\nYou have been defeated!\nGAME OVER")
        exit()
        
def attackstrong(hp):
    pygame.mixer.music.stop()
    pygame.mixer.music.load("strongcombat.mp3")
    pygame.mixer.music.play(-1,0.0)
    global char
    pygame.mixer.music.stop()
    pygame.mixer.music.load("strongcombat.mp3")
    pygame.mixer.music.play(-1,0.0)
    enemyhp = 400
    enemy = random.choice(strong_enemies)
    enemyhp += random.randint(-20, 60)
    slowprint("\n!!!!!!!!!")
    sleep(3)
    slowprint("\n!!!!!!!!! AN EXTREMELY STRONG ENEMY APPROACHES!! WATCH OUT!!")
    sleep(3)
    slowprint(f"\n IT'S A MEGA ENEMY!!!! A {enemy} looms over you! This {enemy} has {enemyhp} health.\n Mega enemy attacks deal 60-90 damage (you have {hp}), and they have a 15 percent chance to miss. Enemies have a 25% chance to regain 30 hp per round! {char}, you must defeat it!\n\n")
    sleep(2)
    slowprint(f"{enemyhp} health?")
    
    answer = input("\nSeems.... hopeless, no? (yes/no)")
    if answer == "yes":
        sleep(1)
        slowprint("That thing could take you out with a single swing!")
        sleep(1)
        slowprint("Actually, half a swing.")
        sleep(1)
        slowprint("You must defeat it.")
    if answer == "no":
        sleep(1)
        slowprint("THAT'S THE SPIRIT!! ONCE MORE UPON THE BREACH, DEAR FRIEND!")
        
    sleep(1)
    slowprint("And fear not! DETERMINATION fills you.")
    sleep(1)
    slowprint("What's that?")
    sleep(5)
    slowprint("...")
    sleep(5)
    slowprint("YOUR WEAPONS SENSE YOUR DETERMINATION!")
    sleep(1)
    slowprint(f"\n\nSWORD ATTACK TO 70! PIKE ATTACK TO 100! DAGGER ATTACK TO 30! ALL WEAPONS MISS CHANCE REDUCED! KNIGHT, YOUR HEALTH HAS BEEN TRIPLED!")
    sleep(1)
    hp = hp * 3
    
    while enemyhp > 0 and hp > 0:
        slowprint("\nYOUR TURN! Swords deal 70 damage but have a 6 percent chance to miss.\n Pikes deal anywhere from 65 to 100 but have a 14 percent chance to miss. \n Daggers are guaranteed to deal 40 damage.\n You can also choose to Heal, regaining 80 hp.")
        attack = input("\n\nWhich attack do you choose? (sword/pike/dagger/heal)\n\n")
        sleep(1)
        if attack.lower() == "devweaponaim54mk47":
            enemyhp = 0
        if attack.lower() == "sword":
            chance = random.randint(0,100)
            if chance > 6:
                enemyhp -= 70
                slowprint(f"\nYou strike the {enemy} with your sword, dealing 70 damage!\n")
            else:
                slowprint(f"\nYou swing your sword at the {enemy}, but it misses!")
        elif attack.lower() == "pike":
            chance = random.randint(0,100)
            if chance < 86:
                damage = random.randint(65,100)
                enemyhp -= damage
                slowprint(f"\nYou strike the {enemy} with your pike, dealing {damage} damage!\n")
            else:
                slowprint(f"\nYou swing your pike at the {enemy}, but it misses!")
            sleep(1)
        elif attack.lower() == "dagger":
            enemyhp -= 40
            slowprint(f"\nYou strike the {enemy} with your dagger, dealing 40 damage!\n")
            sleep(1)
        elif attack.lower() == "heal":
            if hp <= 280:
                hp = hp + 80
                slowprint(f"\nYou heal yourself with an Enhanced Healing Concoct, regaining 80 health!\nYou have {hp} health left.")
            elif hp + 80 > 360:
                slowprint(f"\nYou heal, but since you're so close to maximum HP, you may only heal up to 360. You have 360 hp left.\n")
                hp = 360
        else:
            slowprint("\nYou fumble for a non-existent weapon. You fail.")
            sleep(1)
        if enemyhp <= 0:
            slowprint(f"\n\n\nYou have defeated {enemy}! A FEAT TO MAKE THE GODS PROUD!")
            sleep(1)
            slowprint(f"The wash of determination leaves you. You're once again at {hp} health.")
            if hp <= 120:
                slowprint(f"\n\nYou feel no worse than usual, and your strength is unimpaired. You forge on.")
                return(None)
            else:
                hp = random.randint(80, 120)
                slowprint(f"\n\nYou are injured and have {hp} health left. You take a moment to chug down a healing potion, returning to {hp} hp.")
                pygame.mixer.music.load("tjomnaja.mp3")
                pygame.mixer.music.play(-1,0.0)
                return(None)
            
        sleep(0.5)
        slowprint(f"\nThe {enemy} has {enemyhp} health remaining.")
        sleep(1)
        slowprint("\nThe enemy attacks!!")
        sleep(2)
        
        chance = random.randint(0,100)
        if chance >= 15:
            damage = random.randint(60,90)
            hp -= damage
            slowprint(f"\nYou are hit!! The enemy deals {damage} damage. You have {hp} health left.")
        else:
            slowprint(f"\nThe {enemy} misses!")
        chance2 = random.randint(0,100)
        sleep(0.5)
        if chance2 > 75:
            slowprint(f"\nUnfortunately for you, the {enemy} manages to heal up 30hp!\n\n")
            enemyhp += 30
            
    if hp <= 0:
        slowprint("\n\n\nYou have been defeated!\nGAME OVER")
        exit()
        
def attacknarrator(hp):
    global char
    pygame.mixer.music.stop()
    pygame.mixer.music.load("narratorcombat.mp3")
    pygame.mixer.music.play(-1,0.0)
    enemyhp = "∞"
    slowprint("\n!!!!!!!!!")
    sleep(3)
    slowprint("\nA cold blade jerks towards you. You lash out just in time to twist away from it.")
    sleep(3)
    slowprint(f"\nI am the lord of the castle. I am the rightful owner of the crown. I will not allow you to take it. The world must remain dark.\n\n")
    sleep(2)
    slowprint(f"\nFoolish {char}.", 0.16)
    sleep(1)
    slowprint("Did you not know who your narrator is?", 0.22)
    slowprint(f"\nENEMY TYPE: DARK KING\nHP: {enemyhp}")
    counter = 3
    
    while counter > 0:
        answer = input("\nHopeless. (yes/no)")
        if answer == "yes":
            slowprint("\nPrudent of you. Unfortunately, survivors aren't allowed.")
            hp = 0
        if answer == "no":
            sleep(1)
            slowprint("No?")
            sleep(1)
            responses = ["Reconsider. Now. [The Lord's dark sword slices the air an inch from your chest.]", "Really? [A dagger spirals into the wall next to you.]", "Still so stubborn. [A pike is levelled at you with cruel elegance.]"]
            response = random.choice(responses)
            responses.remove(response)
            slowprint(response)
            counter -= 1
        elif counter == 0:
            sleep(5)
            slowprint("I see. So be it.")
            exit()
            
    sleep(1)
    slowprint("And fear not! DETERMINATION fills you.")
    sleep(1)
    slowprint("What's that?")
    sleep(5)
    slowprint("...")
    sleep(5)
    slowprint("Your weapons sense your determination.")
    sleep(1)
    slowprint(f"\n\nNo, even they feel hopeless.")
    sleep(1)
    
    hp = hp*3
    
    while hp > 0:
        
        slowprint("\nYour turn. Swords deal 70 damage but have a 6 percent chance to miss.\n Pikes deal anywhere from 65 to 100 but have a 14 percent chance to miss. \n Daggers are guaranteed to deal 40 damage.\n You can also choose to Heal, regaining 80 hp.")
        attack = input("\n\nWhich attack do you choose? (sword/pike/dagger/heal)\n\n")
        sleep(1)
        slowprint(f"The king deflects your attack. it deals 0 damage.")
        
        if attack.lower != "sword" or "pike" or "dagger":
            slowprint("\nYou fumble for a weapon but don't reach it in time.")
            sleep(1)
        slowprint("\nThe King attacks.")
        sleep(3)
        slowprint("\nHis spell strikes you in the chest.")
        damage = hp - 1
        slowprint(f"\nHe deals {damage} damage. You're hanging on by a thread.")
        sleep(3)
        slowprint("\nHe laughs at you.")
        sleep(3)
        slowprint("\nYou see your dagger.")
        sleep(3)
        slowprint("\nWith your last bit of strength, you swing it at him.")
        sleep(3)
        slowprint("\nIt finds a weakness in his armor.")
        sleep(3)
        slowprint("\nInto his heart. The Dark Crown tumbles to the floor.")
        sleep(3)
        slowprint("\nAnd he is no more.")
        return(None)
        break
    
def createchar(hp:int, attackchance:int):

    slowprint(f"\n{name}, what CLASS will your character be?")
    slowprint("Warlocks have reduced HP but are less likely to attract enemies.\nKnights offer enhanced HP but are more likely to be attacked.\nCivilians have no change in stats.\nBerserkers have massively increased HP, but every enemy possible will attack if given the chance.")
    char: str = input("\nWARLOCK, KNIGHT, CIVILIAN, BERSERKER? (Enter one.)").lower()
    
    classes = ["warlock","knight","civilian", "berserker"]
    
    if char in classes and isinstance(char, str) == True:
        if char == "warlock":
            slowprint("\nVery well.")
            hp -= 20
            attackchance -= 6
        elif char == "knight":
            slowprint("\nVery well.")
            hp += 20
            attackchance += 7.5
        elif char == "civilian":
            slowprint("\nVery well.")
        else:
            slowprint("\nVery well.")
            hp += 120
            attackchance += 1000
                    
        slowprint("\n... And so it begins.")
        sleep(3)
        slowprint("\n")
        return(hp, attackchance)
    else:
        print("That's not a valid input.")
        createchar(hp, attackchance)
        
def section1(hp:int):
    
    global attackchance
    global enemyalive
    while hp > 0:
        slowprint("\nYou are standing in front of the castle gates. There is a tall fence blocking your path. The gate is locked.")
        sleep(0.5)
        
        while True:
            choice = input("\nDo you want flip the fence, attempt to find gaps or search the castle grounds? (fence/gaps/search)").lower()
            if choice.lower() == "fence":
                slowprint("\nYou have chosen to parkour!")
                sleep(0.5)
                slowprint("\nYou vault over... but fall down and hurt yourself.")
                sleep(0.5)
                hp -= 10
                slowprint(f"\nYou're in, but you've been injured. \n\nYour hp is slightly reduced to {hp}.")
                break
                
            elif choice.lower() == "gaps":
                slowprint("\nYou attempt to route the Tall Fence by slinking through the bushes and squeezing between two bars. \n You manage to avoid most of the obstacles and continue on your way. \n However, flowers in the bushes leave their scent on you.\n\n Enemies will attack you more often.")
                attackchance += 10
                break
            elif choice.lower() == "search":
                slowprint("\nYou take a route around the castle.\nYou find a rusty, dilapidated garden gate. You force it open, and enter the garden.")
                slowprint("\nIt used to be a rose garden and a greenhouse. However, years of darkness have made the plants wilted and close to death.")
                if input("\nDo you enter the old greenhouse or approach the castle? (enter/approach)").lower() == "enter":
                    slowprint("\nThe greenhouse doors are covered with moss and vines. You enter to the sight of a room full of dead flowers.")
                    sleep(2)
                    if enemyalive == True:
                        slowprint("\n!!! There's an enemy in the corner!")
                    attacknormal(hp)
                    enemyalive = False
                    slowprint("\nInteresting, it seems the enemy was carrying some sort of magic potion.")
                    slowprint("\nDo you want to drink it?")
                    if input("\n(y/n)").lower() == "y":
                        slowprint("\nYou pinch your nose and have at it. It doesn't taste bad at all. You feel a little stronger.")
                        hp += 10
                    else:
                        print("\nYou don't trust it and pour it into a potted plant.\nThe plant instantly comes to life.\nMaybe it was a mistake.")
                slowprint("\nYou exit the greenhouse and return to the garden.")
                slowprint("\nThe beaten track merges with a path of pebbles. It splits in two.")
                if input("\nWhich way, adventurer? (L/R)").lower() == "l":
                    slowprint("\nThe path curls around the back of the castle. It leads to a wooden latch.\nThere's a stone staircase leading underground.")
                    slowprint("\nUnderground?")
                    if input("\n(Y/N)") == "y":
                        section4(hp)
                        break
                    else:
                        slowprint("\nYou return and decide to take the other path.")
                        section5(hp)
                        break
                else:
                    slowprint("You decide to take the other side.")
                    section5(hp)
            else:
                slowprint("\nYou make an invalid choice. Dude. One letter isn't that hard.")
                pass
        sleep(2)
        slowprint("You now face the castle. It's very intimidatingly large. \nAnd whoever decided to paint brick walls with poor quality black paint needs to spend a few days in a dungeon.")
        
        while True:
            choice = input("How will you get in? Door? Window? Unexpected entrance by demolishing a wall? (door/window/wall)")
            if choice.lower() == "wall":
                slowprint("What..... were you expecting, exactly??????? You bounce off the wall slightly rattled and lose 5 hp. Try again.")
                hp -= 5
                while True:
                    choice = input("How will you get in now? Door? Window? Wall? (door/window/wall-NO YOU MAY NOT PICK THE WALL AGAIN)")
                    if choice.lower() == "door":
                        slowprint("You kick down the front door (so much for subtlety) HALO-style and rush in the atrium of the castle.")
                        sleep(3)
                        slowprint("....... and immediately attract the attention of all the monsters in the room. Look at you go, Master Chief!")
                        hp1 = hp
                        hp = attacknormal(hp)
                        sleep(5)
                        if hp == hp1:
                            slowprint("Huh, guess those idiots were too clumsy. You somehow make past them completely unscathed.")
                        else:
                            slowprint("After demolishing every enemy that comes your way, you make your way out.")
                        choice = input("Upstairs or down? (u/d)")
                        if choice == "u":
                            chance = random.randint(0,1000)
                            if chance > 981:
                                slowprint("aaaaaaaaaaaaaaaaaaand you slip and fall. -5hp!")
                            hp -= 5
                            section2(hp)
                        else:
                            section6(hp)
                        break
                    elif choice.lower() == "window":
                        slowprint("You climb and swing through an open window, making an embarassingly loud noise by catching your foot on the windowframe.")
                        if random.randint(1,100) > attackchance + 60:
                            attacknormal(hp)
                            section2(hp)
                            break
                    else:
                        slowprint("\nYou're indecisive. Pick again.")
            if choice.lower() == "door":
                slowprint("You kick down the front door (so much for subtlety) HALO-style and rush in the atrium of the castle.")
                sleep(3)
                slowprint("....... and immediately attract the attention of all the monsters in the room. Look at you go, Master Chief!")
                hp1 = hp
                hp = attacknormal(hp)
                sleep(5)
                if hp == hp1:
                    slowprint("Huh, guess those idiots were too clumsy. You somehow make past them completely unscathed.")
                else:
                    slowprint("After demolishing every enemy that comes your way, you make your way upstairs.")
                chance = random.randint(0,1000)
                if chance > 500:
                    slowprint("aaaaaaaaaaaaaaaaaaand you slip and fall. -5hp!")
                hp -= 5
                section2(hp)
            elif choice.lower() == "window":
                slowprint("You climb and swing through an open window, making an embarassingly loud noise by catching your foot on the windowframe.")
                v1 = attackchance
                attackchance += 30
                if attackchance > random.randint(0,100):
                    hp = attacknormal(hp)
                attackchance = v1
                slowprint("You forge on.")
                section2(hp)
                return(None)
            else:
                slowprint("\nInvalid. Pick again.")
                
    if hp <= 0:
        slowprint("\n\nYou died of non-combat causes! Good job, you managed to die... while not in combat??? Rest in peace.\nGAME OVER")      
         
def section2(hp: int):

    global attackchance
    global char
    slowprint("\nUpstairs. Left or right?")
    if input("(L/R)").lower() == "r":
        sleep(1)
        slowprint("\nYou find your way into an important-looking place with 2 doors. \nOne is red, and is decorated with all the best grandeur. \n\nOne is blue and gives off a simple sense of tranquility. \nA strong feeling of malevolence radiates from the red door. Strangely, you feel compelled to go in.\n")
        sleep(1)
        slowprint("\nOh wait, what's this?")
        sleep(1)
        slowprint("\nA note on the wall! Suspiciously convenient.")
        sleep(1)
        slowprint("'Blue, the Sage's path. Red, the Warrior's path..'")
        
        while True:
            choice1 = input("Choose one, adventurer!! (Red/Blue)")
            sleep(2)
            
            if choice1.lower() == "blue":
                slowprint("\nYou step past the blue door. Inside is a small room with a ornate, game-like lock on the door on the other wall.")
                sleep(1)
                slowprint("\nYou step closer. It's a small brass skull with a candle in its jaw, some strange stars and a three-digit dial above. A plaque is below.")
                sleep(1)
                slowprint("\n'1000 numbers. \nNine guesses. Get it in 9, thou shalt pass. \nFail, and be destroyed. \nThus is the gamble of the Sage. \nThe Hallowed Soul shall guide you: shining cerulean for too low, and crimson for too high.'")
                sleep(1)
                slowprint("You should choose.")
                guesses = 9
                
                while True:
                    number = random.randint(0,999)
                    if guesses == 0:
                        slowprint("\nYou have failed.")
                        sleep(3)
                        slowprint("\nA thin blade shoots out from somewhere inside the lock and impales you.\n A trapdoor opens beneath you and you")
                        slowprint("F",0.55)
                        slowprint("A",0.65)
                        slowprint("L",0.75)
                        slowprint("L",0.85)
                        sleep(3)
                        slowprint(f"\nGoodbye, {char}.")
                        hp -= 30
                        slowprint("You hit the ground with a dull thud.")
                        sleep(3)
                        slowprint("You're.... not dead?")
                        section4(hp)
                    slowprint("Dial. 000 to 999.")
                    
                    guess = input("(000-999, choose one.)")
                    try:
                        guess = int(guess)
                    except TypeError as guess:
                        slowprint("NO")
                    if isinstance(int(guess), int) == True:
                        guess = int(guess)
                        
                    elif isinstance(int(guess),int) == False:
                        slowprint("\nNO")
                        
                    elif guess == number:
                        sleep(2)
                        slowprint("\nThe skull shines green from its eyes. A whirr sounds from inside the locks.")
                        break
                    elif guess < number:
                        guesses -= 1
                        sleep(2)
                        slowprint(f"\nThe skull shines blue. A star flips upside-down. {guesses} chances left.")
                        
                    elif guess > number: 
                        guesses -= 1
                        sleep(2)
                        slowprint(f"\nThe skull shines red. A star rotates upside-down. {guesses} chances left.")
                        
                    elif guess > 999 or guess <0:
                        slowprint("\nYou've entered an invalid number.")
                        sleep(2)
                        slowprint("\nQuit trying to break the damn dial.")
                    
                        
                sleep(2)
                slowprint("\nA second mechanism is revealed. It consists of a 2-digit dial and an inscription.")
                sleep(2)
                slowprint("\nThe Great Kingdom was founded -- years ago.")
                sleep(1)
                slowprint("\nThe inscription is scratched and rusted over the number. \nYou feel the space and feel two numbers.")
                sleep(1)
                slowprint("\nFor one-sixth of this time, the Kingdom flourished in light.")
                sleep(1)
                slowprint("\nAfter one more twelfth there arrived a wizard of great skill.")
                sleep(1)
                slowprint("\nOne more seventh-life later, he came upon a Dark Crown of great power in an ancient crypt.")
                sleep(1)
                slowprint("\nThe wizard was horrified of its power and sealed it away, living in peace for five years.")
                sleep(1)
                slowprint("\nThe wizard found love and was blessed with a son.")
                sleep(1)
                slowprint("\nAfter attaining one-quarter of the Kingdom's age, the prince of the Kingdom slew him over the heart of a girl.")
                sleep(1)
                slowprint("\nIn a fit of great rage the Wizard unleashed the darkness on the Kingdom, four years ago.")
                sleep(1)
                answer = int(input("\nTell me, wise soul, how long ago was the Kingdom founded? [enter 00-99]"))
                sleep(3)

                while True:
                    if answer == 84:
                        slowprint("You fiddle with the lock and it yields. The third mechanism is revealed.")
                        break
                    elif 99 >= answer >= 0:
                        slowprint("Only a hollow rattle answers you.")
                        answer: int = input("\nTell me, wise soul, how long ago was the Kingdom founded? [enter 00-99]")
                    elif isinstance(answer,int) != True:
                        slowprint("That's not a valid input... the lock doesn't yield.")
                    else:
                        slowprint("That's not a valid input... the lock doesn't yield.")
                    choice1 = "blue"
                    
                sleep(1)
                slowprint("\nThe final mechanism shows.")
                sleep(1)
                slowprint("\nIt's yet another puzzle.")
                sleep(1)
                slowprint("\nThis one seems to be relatively simple.")
                sleep(1)
                slowprint("\nThe inscription reads: \nTell me, adventurer, how many numbers are there between the one and the myriad that cannot be split but by themself and one?")
                while True:
                    answer = int(input("You seem to need to reuse the dial. You're allowed four digits. (Enter 1-9999)"))
                    if answer == 1229:
                        slowprint("\nYou answer correctly. The door swings open. You forge on.")
                        section3(hp)
                        break
                    else:
                        slowprint("\nYour only answer is an empty thunk. Again.")
                
            elif choice1.lower() == "red":
                slowprint("\nYou step.... and find yourself in some sort of dueling room.")
                sleep(1)
                slowprint("\nROOM!")
                sleep(1)
                slowprint("\nSomething is in the corridor on the other side.")
                attackstrong(hp)
                slowprint("\nYou survive against all odds. You forge on.")
                slowprint("\nWait, what's this? It's a small corridor tucked away to the side.")
                section3(hp)
                choice1 = "red"
                break
                
            else:
                slowprint("\nYou attempt to walk through a wall. You can't.")
                slowprint("...",0.16)
    else:
        section6(hp)
       
def section3(hp: int):
    global char
    attacknormal(hp)
    slowprint("\nYou pass a wide, dark corridor and suddenly come upon the Throne Room. A massive, imposing throne stands before you, its surface covered in dust.")    
    sleep(3)
    if random.randint(1,3) == 2:
        attackstrong(hp)     
    slowprint("\nTo one side of the throne is a small table with a dark, majestic crown resting on a cushion.\nIt radiates darkness, so much so you almost can't see it. This must be the dark crown.")
    sleep(3)
    slowprint("\nWill you take it and become the new King of Darkness, or destroy the crown and return light to the kingdom?")
    sleep(1)
    slowprint("\nChoose wisely, adventurer.")
    
    while True:
        
        choice = input("(Take/Destroy)")
        
        if choice.lower() == "take":
            attacknarrator(hp)
            sleep(5)
            slowprint("\nYou take the crown and step forward. \n\nYou rest on the throne. \n\nYou are the new King of Darkness. \n\nYour rule is eternal.")
            sleep(5)
            slowprint("\nHail, Majesty.")
            slowprint("\n\n\nGAME OVER - ENDING: [THE ETERNAL DARKNESS]\n\n")
            slowprint("####TITLES GAINED:####\n'INFINITE SUCCOR'\n'OVER HELL'")

            break
        
        if choice.lower() == "destroy":
            attacknarrator(hp)
            sleep(3)
            slowprint("\nYou win. Yet, you're bleeding mortally from his attacks.")
            sleep(3)
            slowprint("\nYou carve through the crown with your dagger and cleave it clean in half.\nYou limp yourself over to one of the windows, and look up one last time.")
            sleep(4)
            slowprint(f"\nThe clouds part.\nFor the first time in years, light shines upon the kingdom.\nYou have done well, {char}.")
            sleep(5)
            slowprint("\n\nGAME OVER - ENDING: [FORWARD UNTO DAWN]\n\n")
            sleep(0.1)
            slowprint("####TITLES GAINED:####\n 'MORNING STAR'\n'OVER HEAVEN'")

            break
        
        else:
            pass
        
    sleep(3)
    slowprint("\n\n---- CREDITS ----\nGame Development: Jacob\nLogic design: Jacob\nPlaytesters:\nTony Q\nAika B\nMitchell S\nOlivia S\nCoco W\n\n",0.054) 
    slowprint("THANK YOU FOR PLAYING!",0.2)      
    exit()

def section4(hp: int):
    print("ACHIEVEMENT MADE: UP IS DOWN")
    slowprint("\nYou enter a dark dungeon. You pluck a torch off the wall and ignite it.")
    slowprint("\nYou pick an old, moldy map off the floor.")
    slowprint("\nYou can still turn back, adventurer.")
    if input("Turn back? (y/n)").lower() == "y":
        slowprint("\nYou turn back and leave the dungeon. You exit out the back and walk around again.")
        section1(hp)
    slowprint("\nIt seems there are seven levels.")
    slowprint("\nYou descend into the first level.")
    sleep(1)
    slowprint("...")
    slowprint("\nA barracks.")
    slowprint("\nYou forge on.")
    slowprint("\nOn the second level, there seems to be a potionmaker's shop of some sort.")
    slowprint("\nYou pilfer a healing potion and drink it.")
    hp += 10
    slowprint("\nThere are vaguely sounds coming from below.")
    slowprint("\nYou bite your cheek and tentatively walk down the stairs.")
    sleep(2)
    slowprint("...",0.3)
    sleep(1)
    slowprint("\nJust a dripping tap and a leaky cauldron.")
    slowprint("\nFourth level. You're so deep inside the ground the only sound you hear is deathly silence.")
    sleep(4)
    slowprint("YOUR TORCH SUDDENLY EXTINGUISHES!")
    sleep(2)
    slowprint("\nA horrible shriek suddenly sounds behind you.",0.005)
    attacknormal(hp)
    slowprint("\nYou wipe monster slime off your weapons and go down. You tell yourself there are only three levels left.")
    slowprint("\nThe fifth and sixth level consists of regular cells.")
    slowprint("\nNothing to see here.")
    slowprint("\nLevel Seven. It's cavernously large.")
    slowprint("\nA junction. Left or right?")
    if input("(L/R)") == "l":
        slowprint("\nSome sort of interrogation room.")
        attackstrong(hp)
    slowprint("\nYou head right. It seems to be some special torture cell.")
    slowprint("\nThere is a dusty skeleton shackled to the wall. \nFurther inspection reveals a crown on its skull.")
    sleep(1)
    slowprint("\nIt can't be.")
    slowprint("\nThis... is the last King.",0.25)
    attacknarrator(hp)
    slowprint("\nIn his fury, his spell hit a stone in a pillar.")
    slowprint("\nThe dungeon collapses. \nYou do not know whether the Dark Crown was destroyed with the Dark King.")
    for i in range(7):
        sleep(1)
        slowprint("You head up.",0.15)
    slowprint("\nYou attempt to exit, but the mouth of the dungeon is collapsed. These stones have 99999999999999999999999 HP.")
    slowprint("\nYou strike the stones. You deal 1HP of damage. 99999999999999999999998 left.")
    slowprint("\nA faint spot of light peeks in through a gap in the stone.")
    sleep(1)
    slowprint("\nIt might be sunlight, or just an unextinguished torch.")
    slowprint("\nYou do not know.",0.2)
    slowprint("\n\nGAME OVER - ENDING: [AGNOSTIC]\n\n")
    sleep(0.2)
    slowprint("####TITLES GAINED:####\n 'IN GRANITE CLAD'\n'ENTOMBED WITHIN'")
    slowprint("\n\n---- CREDITS ----\nGame Development: Jacob\nLogic design: Jacob\nPlaytesters:\nTony Q\nAika B\nMitchell S\nOlivia S\nCoco W\n\n",0.054) 
    slowprint("THANK YOU FOR PLAYING!",0.2)
    exit()      
    
def section5(hp:int):
    global cloak
    cloak = False
    global attackchance
    slowprint("\nThe path takes you around to the rear court of the castle.")
    slowprint("\nA dilapidated door is all that stops you.")
    slowprint("\nYou break it down easily. There is a sweeping staircase leading upstairs and two corridors.\nHowever, the right one is blocked by some ruined walls.")
    if input("\nWhich way shall it be, adventurer? Up or down? (up/down)").lower == "up":
        section2(hp)
    else:
        slowprint("\nYou head left and find yourself in a wing of the castle.")
        slowprint("\nIt opens into a courtyard.")
        slowprint("\nThis place offers three choices: forward into the Servants' Quarters, turn into the Trophy Room, or up into an Ancient Belltower.")
        direction = input("\nChoose, adventurer. (forward/turn/up)").lower()
        while True:
            if direction == "up":
                slowprint("\nYou climb into the Tower. It takes you a while to get to the top.")
                slowprint("\nAt the top, you are offered a sight over the entire Kingdom.")
                slowprint("\nIt is nothing but darkness and mist and rot.")
                slowprint("\nYou discover an old cloak in a corner. Will you take it?")
                if input("(y/n)").lower() == "y":
                    slowprint("This cloak seems to have some sort of enchantment. You become slightly less visible.")
                    attackchance -= 5
                    cloak = True
                else:
                    slowprint("You decide it will only hinder you.")
                slowprint("\nYou walk down the spiral staircase in the tower...\nBut you're not alone.")
                attacknormal(hp)
                slowprint("\nAfter you finish the fight, you return to the courtyard.")
            elif direction == "turn":
                slowprint("\nYou enter the trophy room. Its walls are lined with proofs of bygone glamour.")
                slowprint("\nYou see a piece of armor in the corner. It's in excellent condition despite the years.")
                slowprint("\nAfter a not-so-careful moral debate, you take the armor.")
                hp += 15
                slowprint("\nIt opens into a series of corridors. You follow the widest one.")
                slowprint("\nYou are directed to the Atrium. There are numerous monsters wandering around here.")
                if cloak == True:
                    slowprint("\nThanks to the cloak, you're not detected by any of the monsters.")
                else:
                    attacknormal(hp)
                slowprint("\nThere are two ways here: up the staircase or keep going on the ground floor.")
                if input("Pick, adventurer! (ground/up)").lower == "up":
                    section2(hp)
                else:
                    slowprint("You head along the ground floor.")
                    section6(hp)
                    break
            else: 
                slowprint("\nThe Quarters are clearly the most desirable option. You proceed.")
                section7(hp)
                break

def section6(hp:int):
    slowprint("\nYou head along the ground floor of the castle.")
    slowprint("\nAs you proceed, more and more rooms are blocked. \nYou eventually arrive at a staircase as your only option.")
    slowprint("\nYou proceed up several, and come onto a fifth floor armory.")
    slowprint("\nThere are hundreds of barrels of gunpowder here. \nEnough to take out the castle, and hopefully the Crown.")
    slowprint("\nHowever, the ground is so damp you cannot detonate it outside. \nYou know what this means.")
    bomb = input("\nDo you wish to destroy the castle? It is not too late to turn back.(y/n)").lower()
    if bomb == "y":
        slowprint("\nYou take a while to roll the explosive barrels around the castle.")
        slowprint("\nYou open one and lay trails of powder to every one.")
        slowprint("\nIn your haste, your flint strikes a metal door. The fatal spark hits a pile of powder behind you.")
        success = random.randint(0,1)
        if success == 1:
            slowprint("The explosion hits you, and you're thrown out of the window -- \nBut in a dash of fortune, so does it hit the other explosive.")
            sleep(3)
            slowprint("You are fortituous. The extra explosion boosted you into the moat. You're unharmed.")
            slowprint("Above the flaming ruins, the Sun shines. The darkness dissolves.")
            slowprint("")
            slowprint("\n\nGAME OVER - ENDING: [SPIRIT OF FIRE]\n\n")
            sleep(0.2)
            slowprint("####TITLES GAINED:####\n 'DEMOLITIONS EXPERT'\n'VIERY SOUL'")
        else:
            slowprint("\nYou're thrown against a wall like a ragdoll. Your death is inglorious.")
            slowprint("\nThe darkness persists.")
            hp = 0
            slowprint("\n\nGAME OVER - ENDING: [LONG NIGHT OF SOLACE]\n\n")
            sleep(0.2)
            slowprint("####TITLES GAINED:####\n 'DETONATOR'\n'RAPID FULMINATION'")
        slowprint("\n\n---- CREDITS ----\nGame Development: Jacob\nLogic design: Jacob\nPlaytesters:\nTony Q\nAika B\nMitchell S\nOlivia S\nCoco W\n\n",0.054) 
        slowprint("THANK YOU FOR PLAYING!",0.2)
        exit()     
    elif bomb == "n":
        slowprint("\nWise.\nYou are presented with two choices. Back along the first floor or the ground floor.")
        way = str(input("Choose one. (1/G)")).lower()
        if way == "g":
            section7(hp)
        elif way == "1":
            section2(hp)

def section7 (hp:int):
    global cloak
    slowprint("\nYou proceed.")
    slowprint("\nIt's a set of servants' quarters. Nothing to see here....")
    sleep(1)
    slowprint("\nOh, no. You are not alone...",0.12)
    if cloak == False:
        attacknormal(hp)
    else:
        sleep(1)
        slowprint("\nJust your imagination.")
    slowprint("\nAn interesting suit of armor. Take it?")
    if input("\n(y/n)").lower() == "y":
        slowprint("\nNeat. Little bulky, though.")
        hp += 15
    slowprint("\nNothing more here. You press on.")
    slowprint("\nThere are two paths here. One is a set of stairs leading up, and another a flight of grim stone leading down.")
    slowprint("\nAnd a third path, this time forward, to the Throne Room.\nAnd a stealthy fourth road, to the left.")
    slowprint("\nWhich way will it be?")
    choice = input("\n(up/down/forward/left)").lower()
    if choice == "up":
        slowprint("\nHuh, a junction that seems... familiar.")
        section2(hp)
        return
    elif choice == "down":
        slowprint("\nA gamble, but it may well be a worthy one.")
        section4(hp)
    elif choice == "forward":
        slowprint("\nThe objective is foremost. In and out, quick and easy.")
        section3(hp)
    else:
        slowprint("\nYou duck into the left path.")
        slowprint("\nCaution!!!!! A monster is posted as guard here.")
        attackstrong(hp)
        slowprint("\nIt leads to a set of bare, functional quarters. The living room shows that clearly, someone lives here.")
        slowprint("\nYou proceed to the bedroom.")
        sleep(2)
        slowprint("\nQuiet! The Dark King himself is sleeping.")
        assassinate = input("\nA difficult choice, but a necessary one... what will you do with him?\nYou can either end his life and the crown, or destroy the crown without waking him, or take the crown for yourself.\n(kill/take/destroy)").lower()
        if assassinate == "take":
            sleep(1)
        if assassinate == "kill":
            slowprint("\nOne more death to the pyre.")
            sleep(1)
            slowprint("\nYou close your eyes and swing.")
            sleep(2)
            slowprint("\nYour sword does a clean job.")
            slowprint("\nYou turn and leave, not wanting to stay here a second longer than you have to.")
            slowprint("\nThere is light and peace have returned. Monsters are changing back into human form.\nChildren and parents, families, lovers. They reunite. The world is whole.\nAll is blooming.")
            slowprint("\nYet, you will never wash the blood off your hands.")
            slowprint("\n\nGAME OVER - ENDING: [REGICIDAL]\n")
            sleep(0.2)
            slowprint("####TITLES GAINED:####\n 'THANE OF CAWDOR'\n'INVISBLE HAND'")
            slowprint("\n\n---- CREDITS ----\nGame Development: Jacob\nLogic design: Jacob\nPlaytesters:\nTony Q\nAika B\nMitchell S\nOlivia S\nCoco W\n\n",0.054) 
            slowprint("THANK YOU FOR PLAYING!",0.2)
            exit()
        if assassinate == "destroy":
            slowprint("\nYou drive a dagger into the crown's centrepiece jewel, and fracture the brittle metal.")
            slowprint("\nThe Dark King does not rouse.")
            slowprint("\nYou leave him be.")
            slowprint("\nYou climb to the highest tower of the castle and hail the eastern Sun.")
            slowprint("\n\nGAME OVER - ENDING: [SILENT DAWN]\n\n")
            sleep(0.2)
            slowprint("####TITLES GAINED:####\n 'THE MERCIFUL'\n'SUNBRINGER'")
            slowprint("\n\n---- CREDITS ----\nGame Development: Jacob\nLogic design: Jacob\nPlaytesters:\nTony Q\nAika B\nMitchell S\nOlivia S\nCoco W\n\n",0.054) 
            slowprint("THANK YOU FOR PLAYING!",0.2)
            exit()
        if assassinate == "take":
            slowprint("\nYou wedge the crown squarely onto your head.")
            slowprint("\nThe King, sensing the disturbance in the power, rouses in a fit of terror.")
            slowprint("\nHe shouts a frenzied warning at you, but the Crown has already taken hold of you.")
            slowprint("\nYou understand now, why the Darkness exists.\nThe Dark King was merely attempting to contain the true horrors of the Crown with his mind, a mind impossibly strong.")
            sleep(1)
            slowprint("\nAlas, you are no King. Neither is your mind fit to be one.")
            slowprint("\nThe visions start. They don't stop. The horror doesn't endtheydon'tstopitneverstopsitneverstopsitneverstopsitneverstopsIneedoutIneedoutIneedoutIneedoutIneedoutSTOPSTOPITSTOPITSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP")
            sleep(5)
            slowprint("\n\nGAME OVER - ENDING: [PLEASURE IN BEING MAD THAT ONLY MADMEN KNOW]\n\n")
            sleep(3)
            slowprint("####TITLES GAINED:####\n 'MADMAN'\n'OUTER GOD'")
            slowprint("\n\n---- CREDITS ----\nGame Development: Jacob\nLogic design: Jacob\nPlaytesters:\nTony Q\nAika B\nMitchell S\nOlivia S\nCoco W\n\n",0.054) 
            slowprint("THANK YOU FOR PLAYING!",0.2)
            exit()


if __name__ == "__main__":
    slowprint("\n\n                    Initializing......",0.2)
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("tjomnaja.mp3")
    unix = round(time.time())
    slowprint("PYTHON 3.11 INTITIALIZED")
    slowprint("LOGIC MODULE INITIALIZED")
    slowprint("TIME, DELAY, ATTACK, MATHEMATIC MODULES INITIALIZED")
    slowprint("MUSIC AND AUDIO MODULE INITIALIZED")
    sleep(0.5)
    slowprint("INITALIZING COMPLETE",0.1)
    name = input("Please enter your name: ")
    hp, attackchance = createchar(hp, attackchance)
    pygame.mixer.music.play(-1,0.0)
    slowprint(f"\nThe year is Unix Time {unix}.",0.105)
    slowprint("\nDarkness is upon the Kingdom. There has not been a sunrise for years.\nEverywhere there is mist and darkness and rot.\nMonsters roam free and hunt down dozens and dozens every day.\nFamilies ripped apart, farming ravaged by monsters that roam in the eternal night.\nAnd with the disappearance of the Sun, it is as if all good magic has gone out of the world with it.\n")
    slowprint("\nThere are no more sages. \nThere are no more brave men, just powerless people trying to survive.\nThe source of this is the Dark King, who assassinated the True King and unleashed this upon the world.")
    slowprint("\nThe people call this the Nichevo'ya. \nAbyssal monsters killing and ravaging under the cold, strange Moon.")
    slowprint("\nThere is a rumour.. of the Dark Castle's location. You will attempt to rise against the night.")
    slowprint("\nYou were the most talented magic wielder in the land. \nHowever, even you have been reduced to a shadow. \nYou are the last of the magic in this world. ")
    slowprint("\nIf you are to fail....")
    slowprint("\nDo not even think of it.",0.2)
    slowprint(f"\n{name}, your goal is to restore light to this world. Forward be you unto dawn.")
    sleep(1)
    section1(hp)