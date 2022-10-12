import random

#dice roll
def dice():
    roll=random.randint(1,12)
    print(roll)

def ensure(): 
      global sure
      print("Type yes to continue and no to choose again")
      sure=input(str("")) #Checks to make sure the player is good with their choice

def again():
    while sure !='yes' and sure !="no": #if the user has input anything other than yes or no it will request the user to input the options given until they have
        print ("please input one the given options")
        ensure()
#ensure/again combo, ensure offers the yes or no choices and again ensures the user has picked yes or no
def name():
    print("Input the name you would like to have during this journey")
    username= input(str(""))
    ensure()
    again()


def question():
    global choice
    print("Swordsman or Archer")
    print("Swordsman Stats:Str=3 Dex=2 Int=1 Iq=1 HP=3")
    print("Archer Stats:Str=1 Dex=1 Int=3 Iq=3 HP=2")
    choice= input(str("")) #Offers the option of swordsman or archer
    
    
    print('You have picked', choice, 'is this the character you wish to choose?')

def wrongchar():
    while choice !="Swordsman" and choice !='Archer':#ensures that the user has picked one the options 
      print ("please input one the given options")
      question()
#-------------------------------------------------------------------------------------------------------------------------------
print("Welcome")
name()
while sure=='no':#if the user says no and would like to choose their name again,
    # they will recieve all the prompts again from the begininng
    #with the precaution that they have picked the an unavailible  choice
    name()

question()#poses the question of which character the user wants
wrongchar()#repeats the question function if the user has not input one of the options
#if the user has picked an option, the code continues
#the question/wrongchar combo, question asks for users role and wrongchar ensure they have input one of the options
if choice=="Swordsman" or choice=="Archer":#if the user has picked one of the options it will continue
    ensure()#checks the users confidence in their choice
    again()# ensures the user has input a correct command of yes or no

while sure=='no':#if the user says no and would like to choose again,
    # they will recieve all the prompts again from the begininng
    #with the precaution that they have picked the wrong choice
    question()
    wrongchar()
    ensure()
    again()

if sure=='yes':
    print('good choice')
    match choice:   #once the user has picked and confirmed their character, they will be assigned these attribute values
        case 'Swordsman':
             Str=3
             Dex=3
             HP=3
        case "Archer":
             Str=3
             Dex=2
             HP=3
#--------------------------------------------------------------------------------------------------------------------------
print('you come across your first fight')

#dice roll
import random
counter=0
def dice():
    global rolla
    global counter
    rolla=random.randint(1,6)
    rollb=random.randint(1,6)
    print("die two rolled", rolla)
    print("die one rolled", rollb)
    counter+=rolla
    counter+=rollb
    print ("your total roll count is",counter)
    
def bdice():
    global rolla
    global counter
    rolla=random.randint (2,3)
    rollb=random.randint(2,3)
    print("die one rolled", rolla)
    print("die two rolled", rollb)
    counter+=rolla
    counter+=rollb
    print ("your total roll count is",counter)

countere=0
def dicee():
    global countere
    global rollea
    global rolleb
    rollea=random.randint(1,6) 
    rolleb=random.randint(1,6)
    print("enemy die two rolled", rollea)
    print("enemy die one rolled", rolleb)
    countere+=rollea
    countere+=rolleb
    print ("your enemies total roll count is",countere)

times=0
while times<=3:
    toss=input(str("Would you like to roll dice a or  dice b"))
    match toss:
        case "a":
            bdice()
            times+=1
        case "b":
            dice()
            times+=1

dicee()
dicee()
dicee()

print("your total is", counter)
print ("your enemies total is", countere)
if counter<countere:
    print("you lose")
if counter>countere:
    print("you win")
