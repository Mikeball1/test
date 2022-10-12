import sys,time,os

def scroll(words):
	for c in words:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.02)

def question():
    global choice
    scroll("Swordsman or Archer\n")
    scroll("Swordsman Stats:\nStr=3 Dex=2 HP=3\n")
    scroll("Archer Stats:\nStr=1 Dex=2 HP=5\n")
    choice= input(str("")) #Offers the option of swordsman or archer

def wrongchar():
    question()
    while choice !="Swordsman" and choice !='Archer':#ensures that the user has picked one the options 
      scroll ("please input one the given options\n")
      question()

def ensure():#the function used to ensure the user has picked the choice they want
              #while also checking if the user has input an option provided by the function
              # ensure offers the yes or no choices and again ensures the user has picked yes or n
      global sure #makes the variable sure maintain the value outside of the function
      scroll("\nType yes to continue and no to choose again\n")#scrolls the questions if the user would like to continue or choose again
      sure=input(str("")).lower().strip() #Takes the users input and assigns it to the variable sure
      while sure !='yes' and sure !="no": #if the user has input anything other than yes or no it will request the user to input the options given until they have
        scroll("please input one the given options\n")#tells the users to input yes or no
        scroll("Type yes to continue and no to choose again\n")#prints the questions if the user would like to continue or choose again
        sure=input(str("")).lower().strip() #Takes the users input and assigns it to the variable sure
    
def smth(a):
  a
  ensure()
  global sure
  while sure=='no':    
    a
    ensure()


smth(wrongchar)
