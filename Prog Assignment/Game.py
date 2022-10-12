import role
import role2
import random
import sys,time,os

def scroll(words):#app
	for c in words:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.02)

def roleassign(sure,choice):
 global Str
 global HP
 global Dex 
 if sure=='yes':
    if choice=='swordsman':   #once the user has picked and confirmed their character, they will be assigned these attribute values
     role2.assign()
     Str=role2.Str
     HP=role2.HP
     Dex=role2.Dex
    if choice=="archer":
     role.assign()
     Str=role.Str
     HP=role.HP
     Dex=role.Dex

def up(increase):
    global Str
    global Dex
    global HP
    match increase:
        case "STR": 
         Str+=1
         #app
         scroll("Youve increased STR by 1\n")
        case "HP":
         HP+=1
         #app
         scroll("Youve increased HP by 1\n")
        case "DEX":
         Dex+=1
         #app
         scroll("Youve increased DEX by 1\n")

counter=0
countere=0 
def adice():
    global rolla
    global counter
    rolla=random.randint(1,6)
    rollb=random.randint(1,6)
    scroll("Die two rolled "+ str(rolla))
    scroll("\nDie one rolled "+ str(rollb))
    counter+=rolla
    counter+=rollb
    
def bdice():
    global rolla
    global counter
    rolla=random.randint (2,3)
    rollb=random.randint(2,3)
    scroll("\nDie one rolled "+str(rolla))
    scroll("\nDie two rolled "+ str(rollb))
    counter+=rolla
    counter+=rollb

def diceenemy():
    global countere
    global rollea
    global rolleb
    rollea=random.randint(1,5) 
    rolleb=random.randint(1,4)
    scroll("\nEnemy die two rolled "+ str(rollea))
    scroll("\nEnemy die one rolled "+ str(rolleb))
    countere+=rollea
    countere+=rolleb
    print('\n---------------------------------------------')
    scroll("Your total roll count is "+ str(counter)+"\n")
    scroll("Your enemies total roll count is "+ str( countere)+'\n')
    print('---------------------------------------------')

    