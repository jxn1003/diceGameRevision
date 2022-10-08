import time
import random



### AUTHENTICATION CODE ###

login1=False
login2=False
while login1==False:
    username=input("What is your username?: ")
    password=input("What is your password?: ")
    if username == "Katarina" or username == "Joshua" or username == "katarina" or username == "joshua":
        if password == "password":
            print("Welcome",username, "you've been authenticated")
            login1=True
            user1=username
        else:
            print("Incorrect password, try again")
    else:
        print("Incorrect username, try again")
   
while login2==False:
    username=input("What is your username, Player 2?: ")
    password=input("What is your password, Player 2?: ")
    if username == "Katarina" or username == "Joshua" or username == "katarina" or username == "joshua":
        if password == "password":
            print("Welcome",username, "you've been authenticated")
            login2=True
            user2=username
        else:
            print("Incorrect password, try again")
    else:
        print("Incorrect username, try again")


############# MAIN GAME #############
Counter1 = 0
score = 0
while Counter1 <6:

   
    Counter1 = Counter1 + 1
    diceRoll1=random.randint(1, 6)
    print(user1,"rolls")
    time.sleep(1)
    print(diceRoll1)
    diceRoll2=random.randint(1, 6)
    time.sleep(1)
    print(diceRoll2)
    Total = diceRoll1 + diceRoll2
    print("The total is",Total)
    if Total == 3 or Total == 5 or Total == 7 or Total == 9 or Total == 11:
        if score <0:
            score = score
        elif score >0:
            score = score - 5

    else:
        score = score + 10
    print("The score is ",score,)




    if Counter1 >5:
        score2 = 0
        Counter2 = 0
        while Counter2 <6:

            Counter2 = Counter2 + 1
            diceRoll3=random.randint(1, 6)
            print(user2,"rolls")
            time.sleep(1)
            print(diceRoll3)
            diceRoll4=random.randint(1, 6)
            time.sleep(1)
            print(diceRoll4)
            Total2 = diceRoll3 + diceRoll4
            print("The total is",Total2)
            if Total2 == 3 or Total2 == 5 or Total2 == 7 or Total2 == 9 or Total2 == 11:
                if score2 <0:
                    score2 = score2
                elif score2 >0:
                    score2 = score2 - 5
            else:
                score2=score2+10
            print("The score is",score2,)

##USER 1##

        if score2 == score:
            diceRoll5 = random.randint(1, 6)
            print(user1,"rolls to decide the winner!!!!!!")
            time.sleep(1)
            print(diceRoll5)
            diceRoll6 = random.randint(1, 6)
            time.sleep(1)
            print(diceRoll6)
            Total3=diceRoll5+diceRoll6
            if Total3 == 3 or Total3 == 5 or Total3 == 7:
                score = score - 5
            else:
                score = score + 10
            print("The score is",score,)
           
           


        if Counter2 >5:
            if score > score2:
                print(user1, "wins with a score of",score, "compared to",user2,"who only has a score of",score2)
            else:
                print(user2, "wins with a score of",score2,"compared to",user1,"who has",score)


           
newfile=open("Scores.txt","a")
newfile.write(user1)
newfile.write(" has ")
newfile.write(str(score))
newfile.write(" points ")
newfile.write("\n")
newfile.write("\n")
newfile.write(user2)
newfile.write(" has ")
newfile.write(str(score2))
newfile.write(" points ")
newfile.write("\n")
newfile.close()
