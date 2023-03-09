import data
import random
from os import system, name

play=True
score=0
logo='''

  ___ ___ .__       .__                  
 /   |   \|__| ____ |  |__   ___________ 
/    ~    \  |/ ___\|  |  \_/ __ \_  __ \
\    Y    /  / /_/  >   Y  \  ___/|  | \/
 \___|_  /|__\___  /|___|  /\___  >__|   
       \/   /_____/      \/     \/       
.____                                    
|    |    ______  _  __ ___________      
|    |   /  _ \ \/ \/ // __ \_  __ \     
|    |__(  <_> )     /\  ___/|  | \/     
|_______ \____/ \/\_/  \___  >__|        
        \/                 \/            

'''


def getPlayers():
    player1=random.choice(data.data)
    player2=random.choice(data.data)
    return player1,player2

def guessFollower(compare,againast):
    choice=input("Which player has more followers Type A or B from the above : ")
    return choice

#check which one has hight follower
def checkHighFollower(compare,againast):
    high=''
    if(compare['follower_count']>againast['follower_count']):
        high='A'
    else:
        high='B'
    return high

#clear the screen
def clear():
    if name == 'nt':
        x = system('cls')
    else:
        x = system('clear')


while(play!=False):
    compare,againast=getPlayers()

    print(logo)

    print(f'Compare A : {compare["name"] },a {compare["description"]}, from {compare["country"]} ')
    print(f'Againast B : {againast["name"]},a {againast["description"]}, from {againast["country"]}')
    playerChoosen=guessFollower(compare,againast)
    highFollower=checkHighFollower(compare,againast)
    if(playerChoosen==highFollower):
        play=True
        score = score + 1
        print(f'Your Score is {score}')
        clear()
    else:
        print(f'You lost..! and Your score is {score}')
        play=False




