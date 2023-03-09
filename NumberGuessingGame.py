import random
logo='''
  ________                                __  .__               ________                       
 /  _____/ __ __   ____   ______ ______ _/  |_|  |__   ____    /  _____/_____    _____   ____  
/   \  ___|  |  \_/ __ \ /  ___//  ___/ \   __\  |  \_/ __ \  /   \  ___\__  \  /     \_/ __ \ 
\    \_\  \  |  /\  ___/ \___ \ \___ \   |  | |   Y  \  ___/  \    \_\  \/ __ \|  Y Y  \  ___/ 
 \______  /____/  \___  >____  >____  >  |__| |___|  /\___  >  \______  (____  /__|_|  /\___  >
        \/            \/     \/     \/             \/     \/          \/     \/      \/     \/ 
'''

print(logo)
print("Welcome to number missing game")
print("I want to guess you the number between the range from 1 to 100")
easyTries=10
hardTries=5
numChoices=0

actualNumber=random.randint(1,100)
print(f"{actualNumber} This is the answer")
def getEasy():
    numChoices = easyTries
    return numChoices

def getHard():
    numChoices=hardTries
    return numChoices
playerChoice=input("Type which method you want to play Easy or Hard  : ?  ")


if(playerChoice=='Easy'):
    numChoices=getEasy()
    print(f"you have {numChoices} to guess the answer")
else:
    numChoices=getHard()
    print(f"you have {numChoices} to guess the answer")

def decNumChoices(num):
    numChoices=num-1
    return numChoices

while(numChoices>0):
    numberChoosen=int(input("Enter the number you would like to choose  :  "))
    numChoices=decNumChoices(numChoices)
    if(numberChoosen==actualNumber):
        print("You have won")
        exit()
    elif(numberChoosen<actualNumber):
        print("Too Low")
        print(f"You have {numChoices} choices to choose the number")
    elif(numberChoosen>actualNumber):
        print("Too High")
        print(f"You have {numChoices} choices to choose the number")

if(numChoices==0):
    print("You loose the game")


