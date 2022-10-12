import random
import sys,time,os
import role2
import role 
import Game 
def scroll(words):#app
	for c in words:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.02)

def ensure():#app #the function used to ensure the user has picked the choice they want
              #while also checking if the user has input an option provided by the function
              # ensure offers the yes or no choices and again ensures the user has picked yes or n
      global sure #makes the variable sure maintain the value outside of the function
      scroll("\nType yes to continue and no to choose again\n")#scrolls the questions if the user would like to continue or choose again
      sure=input(str("")).lower().strip() #Takes the users input and assigns it to the variable sure
      while sure !='yes' and sure !="no": #if the user has input anything other than yes or no it will request the user to input the options given until they have
        scroll("please input one the given options\n")#tells the users to input yes or no
        scroll("Type yes to continue and no to choose again\n")#prints the questions if the user would like to continue or choose again
        sure=input(str("")).lower().strip() #Takes the users input and assigns it to the variable sure

def name():#app: #this function ask the user for their character name
    scroll("Input the name you would like to have during this journey\n")#tells the user to input their characters name
    username= input(str(""))#takes the users, characters name and assigns it to username
    
def question():
    global choice
    scroll("Swordsman or Archer\n")
    scroll("Swordsman Stats:\nStr=4 Dex=3 HP=2\n")
    scroll("Archer Stats:\nStr=3 Dex=2 HP=4\n")
    choice= input(str("")).lower() #Offers the option of swordsman or archer

def wrongchar():
    question()
    while choice !="swordsman" and choice !='archer':#ensures that the user has picked one the options 
      scroll ("please input one the given options\n")
      question()
    if choice=="Swordsman" or choice=="Archer":#if the user has picked one of the options it will continue
        scroll('You have picked ' + str(choice) +' is this the character you wish to choose?')

def inc(): 
      global increase
      scroll("\nWould you like to increase the stat, HP, STR, Or DEX?\n")
      increase=input(str(""))
      while increase !='STR' and increase!="HP" and increase!="DEX": #if the user has input anything other than yes or no it will request the user to input the options given until they have
        scroll ("Please input one the given options\n")
        scroll("\nWould you like to increase the stat, HP, STR, Or DEX?\n")
        increase=input(str("")) #Checks to make sure the player is good with their choice

def winorlose():
    if counter<countere:
     scroll("you lose\n")
    if counter>countere:
     scroll("you win\n")

def check():
    scroll('\nYour stats are \nStr='+ str(Game.Str)+'\nDex='+ str(Game.Dex)+ '\nHP=' +str(Game.HP)+"\n")

#-------------------------------------------------------------------------------------------------------------------------------
scroll("Welcome to\n")
scroll(f"""\033[96m 𝕿𝖍𝖊 𝕶𝖓𝖎𝖌𝖍𝖙𝖘 𝕲𝖆𝖒𝖇𝖎𝖙 \033[0m\n""")  

#app
name()
ensure()
while sure=='no':#if the user says no and would like to choose their name again,
   name() # they will recieve all the prompts again from the begininng
   ensure()  #with the precaution that they have picked the an unavailible  choice

wrongchar()
ensure()
while sure=='no':#if the user says no and would like to choose again,
    # they will recieve all the prompts again from the begininng
    #with the precaution that they have picked the wrong choice
    wrongchar()
    ensure()

#poses the question of which character the user wants
#repeats the question function if the user has not input one of the options
#if the user has picked an option, the code continues
#the question/wrongchar combo, question asks for users role and wrongchar ensure they have input one of the options
scroll("You are an "+ choice +" in a kingdom, and at the age of 25 you decide to enter a contest like no other. \nThe winner of this contest will win a fortune")
scroll("\nAt the beginning of these trials you find yourself up against your long time rival. \nRonaldo")
scroll("\nIn order to win this contest you will have to pass three various trials")
scroll("\nThe first challenge is a challenge of health.\n")
scroll("\nWhoever can stay underwater the longest is the winner\n")
scroll("\nThe second trial is a trial of strength.\nYou must prove your abilities greater than those of Ronaldo in a competition of arm wrestling")

scroll("\nThe third trial is a of dexterity.\nWho has the greater stamina, determined through who can run the longest\n")




Game.roleassign(sure,choice)
#--------------------------------------------------------------------------------------------------------------------------
scroll('\nyou come across your first fight\n')
scroll('''Tutorial: You have three varying choices. 
    \nChoice a: \nRoll two dice with values from 1-6. 
    \nChoice b:\nRoll two dice with values from 2-3 and gain 1 point in an attribute of your choice.
    \nChoice c: \nNo roll and gain 2 points in an attribute of your choice\n''')
scroll('''\nIn order to win each challenge, you must roll the dice three times and finish the challenge with a higher
roll score than that of your enemies\n''')
scroll('''Winning a challenge by a margin of less than 5 will result in the increase of a stat based on the\ntype of challenge\n''')
scroll("However scroll losing a challenge by a margin of less than 5 will result in the decrease of a stat\nbased on the type of challenge\n")
scroll('''Winning the challenge by a margin of 5 of greater will increase a stat by 2 depending on the type of challenge.\n
Example: In a challenge of HP, your enemy has a score of 20 but you have a score of 26. Your HP will increase by 2\n''') 
scroll('''However, losing by a margin of 5 or greater will result in the decrease of a stat by 2\n''')
scroll('''By the end of the game you must have a total of 5 points in each stat in order to win. Any stat less than 5 will result in a loss\n''')
def dicechoice():
    global toss
    scroll("\nWould you like to roll dice a or dice b or c\n")
    toss=input(str(""))
    while toss!= "a" and toss!="b" and toss!="c":
        scroll("please input a,b ,or c\n")
        scroll("Would you like to roll dice a or dice b or no roll\n")
        toss=input(str(""))


def ffight():
    times=0
    global counter
    global countere
    Game.counter=0
    Game.countere=0
    while times<=2:
     dicechoice()
     ensure()
     while sure=='no':
        dicechoice()
        ensure()
     if sure=="yes":
        match toss:
         case "a":
          Game.adice()
          counter=Game.counter 
          times+=1
         case "b":
            Game.bdice()
            counter=Game.counter 
            check()
            inc()
            ensure()
            while sure=="no":
             check()
             inc()
             ensure()
            if sure=="yes":
             Game.up(increase)
            check()
            times+=1
         case "c":
            scroll("you've decided to not roll and instead increase two values\n")
            check()
            inc()
            ensure()
            while sure=='no':
             check()
             inc()
             ensure()
            Game.up(increase)
            check()
            inc()
            ensure()
            while sure=='no':
             check()
             inc()
             ensure()
            Game.up(increase)
            check()
            times+=1
        Game.diceenemy()
    #scroll("Your total roll count is "+ str(counter)+"\n")
    countere=Game.countere
            
check()
scroll ('you are entering the first fight. This is a test of Health. Depending on the outcome of this game, \nyou may lose HP or gain HP')

ffight()
winorlose()
if countere>counter:#if the enemy has rolled a total greater than the user, it will enter this if statement, otherwise it will enter the else statement
 if countere-counter>=5:#if the enemy has won by a margin greater than or equal to 5, the user will lose 2 HP stats
    Game.HP-=2
    scroll("\nRonaldo has beaten you in the underwater challenge\n")
    scroll("\nyou have suffered a critical loss, leading to a -2 decrease in HP\n")
 else:#if the user has lost by a margin greater less than 5, they will lose 1 HP stat
    Game.HP-=1
    scroll("\nRonaldo has beaten you in the underwater challenge\n")
    scroll("\nyou have suffered a loss, leading to a -1 decrease in HP\n")
else:#if the user has won it will enter this else statement
 if counter-countere>=5:#if the user has won by a margin greater than or equal to 5, the user will gain 2 HP stats
    Game.HP+=2
    scroll("\nYou have beaten Ronaldo in the underwater challenge\n")
    scroll("\nyou came out of the battle victorius with a critical win, leading to a +2 increase in HP\n")
 else:#if the user has won by a margin less than 5, they will receive a HP increase of 1
    Game.HP+=1
    scroll("\nYou have beaten Ronaldo in the underwater challenge\n")
    scroll("\nyou came out of the battle victorius with a win, leading to a +1 increase in HP\n")


check()
print("--------------------------------------------")
scroll('''You are entering the second fight. This is a test of Strength. Depending on the outcome of this game, \nyou may lose STR or gain STR''')
ffight()
winorlose()
if countere>counter:#if the enemy has rolled a total greater than the user, it will enter this if statement, otherwise it will enter the else statement
 if countere-counter>=5:#if the enemy has won by a margin greater than or equal to 5, the user will lose 2 Str stats
    Game.Str-=2
    scroll("\nRonaldo has beaten you in the arm wrestling challenge\n")
    scroll("\nyou have suffered a critical loss, leading to a -2 decrease in Str\n")
 else:#if the user has lost by a margin greater less than 5, they will lose 1 Str stat
    Game.Str-=1
    scroll("\nRonaldo has beaten you in the armwrestling challenge\n")
    scroll("\nyou have suffered a loss, leading to a -1 decrease in Str\n")
else:#if the user has won it will enter this else statement
 if counter-countere>=5:#if the user has won by a margin greater than or equal to 5, the user will gain 2 Str stats
    Game.Str+=2
    scroll("\nYou have beaten Ronaldo in the armwrestling challenge\n")
    scroll("\nyou came out of the battle victorius with a critical win, leading to a +2 increase in Str\n")
 else:#if the user has won by a margin less than 5, they will receive a Str increase of 1
    Game.Str+=1
    scroll("\nYou have beaten Ronaldo in the armwrestling challenge\n")
    scroll("\nyou came out of the battle victorius with a win, leading to a +1 increase in Str\n")
check()
print("--------------------------------------------")
scroll('''You are entering the third fight. This is a test of dexerity. Depending on the outcome of this game, \nyou may lose DEX or gain DEX''')

ffight()
winorlose()
if countere>counter:#if the enemy has rolled a total greater than the user, it will enter this if statement, otherwise it will enter the else statement
 if countere-counter>=5:#if the enemy has won by a margin greater than or equal to 5, the user will lose 2 Str stats
    Game.Dex-=2
    scroll("\nRonaldo has beaten you in the running challenge\n")
    scroll("\nyou have suffered a critical loss, leading to a -2 decrease in Dex\n")
 else:#if the user has lost by a margin greater less than 5, they will lose 1 Dex stat
    Game.Dex-=1
    scroll("\nRonaldo has beaten you in the running challenge\n")
    scroll("\nyou have suffered a loss, leading to a -1 decrease in Dex\n")
else:#if the user has won it will enter this else statement
 if counter-countere>=5:#if the user has won by a margin greater than or equal to 5, the user will gain 2 Dex stats
    Game.Dex+=2
    scroll("\nYou have beaten Ronaldo in the running challenge\n")
    scroll("\nyou came out of the battle victorius with a critical win, leading to a +2 increase in Dex\n")
 else:#if the user has won by a margin less than 5, they will receive a Dex increase of 1
    Game.Dex+=1
    scroll("\nYou have beaten Ronaldo in the running challenge\n")
    scroll("\nyou came out of the battle victorius with a win, leading to a +1 increase in Dex\n")
check()
#fix these conditions at the end

if Game.HP<5 or Game.Str<5 or Game.Dex<5:
    scroll('you lost restart the game to try again')
if Game.HP>=5 and Game.Str>=5 and Game.Dex>=5:
    scroll('You have beaten Ronaldo and have been awarded a fortune. Congrats!')