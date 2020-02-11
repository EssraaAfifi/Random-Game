import random

#VARIABLES
sn = random.randint(1, 5)

try:
    #Starters
    print ("Welcome to the GUESSING GAME!")
    print ("I'm thinking of a number between 1 and 5")
    print ("Take a Guess");
    g1 = int(input())
    if g1 > sn:
        print ("Wrong TRY AGAIN! \nLOWER!")
    elif g1 < sn:
        print("Wrong TRY AGAIN! \nHIGHER!")
    else:
        print("WHAT! HOW DID YOU GUESS IT FROM THE FIRST TIME! IT'S BEGINNERS LUCK! \nPress F5 to Restart")

    #Loop/Actual game
    if g1 != sn:
        for lp in range (3):
            g = int(input())
            if g > sn:
                print ("Wrong TRY AGAIN! \nLOWER!")
                continue
            elif g < sn:
                print("Wrong TRY AGAIN! \nHIGHER!")
                continue
            else:
                break

    #Ending the Game
    if g1 != sn:
        lp = lp + 2
        if g == sn:
            print("GREAT JOB! YOU GUESSED " + str(lp) + " TIMES!\nPress F5 to Restart")
        else:
            print("I was thinking of " + str(sn) + "\n Press F5 to Restart")
except:
    print ("An error has occurred. \nPLEASE WRITE NUMBERS NOT LETTERS! \nPress F5 To Restart!")
