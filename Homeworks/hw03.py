
'''
cs1114
Submission: hw03
Programmer: Vivek Aggarwal
Username: va713
File Name: hw03.py

this is a hit and match game
'''


import random


def welcomeMessage():
    '''this function prints welcome message and waits until user presses any key'''
    print ("Welcome to the Hit && Match Game")
    raw_input ("hit any key to start playing")
    
def randomDigitGenerator():
    '''this function generates random number between 0 and 9'''
    num = int(random.randint(0,9))
    return num

def houseDigit():
    ''' this function assignes three variable with random numbers for house and returns them'''
    leftPosNum = randomDigitGenerator()
    middlePosNum = randomDigitGenerator()
    rightPosNum = randomDigitGenerator()
    return leftPosNum, middlePosNum, rightPosNum

def twoDigitChecker(Num1, Num2 , Num3, hOrU):
    '''this function checks if any of two pair are equal in the given trio of numbers'''
    if (hOrU == 'House'):
        if(Num1 in (Num2, Num3)):
            printHouseNumberSameError()        
            return False
        elif(Num2 in (Num1, Num3)):
            printHouseNumberSameError()
            return False
        elif (Num3 in (Num1, Num2)):
            printHouseNumberSameError()
            return False
        else:
            return True
    else:
        if(Num1 in (Num2, Num3)):
             printUserNumberSameError()
             return False
        elif(Num2 in (Num1, Num3)):
            printUserNumberSameError()
            return False
        elif (Num3 in (Num1, Num2)):
            printUserNumberSameError()
            return False
        else:
            return True

    
def threeDigitChecker(Num1, Num2, Num3, hOrU):
    '''this function checks if the all three numbers are equal'''
    if (hOrU == 'House'):
        if (Num1 ==  Num2 == Num3):
            printHouseNumberSameError()
            return False
        else:
            return True
        
    else:
        if (Num1 ==  Num2 == Num3):
            printUserNumberSameError()
            return False
        else:
            return True

def printHouseNumberSameError():
    '''it prints error message if the random generated house number are equal'''
    print('''We are sorry but the game has malfunctioned.
Ending...

Traceback...
...
SystemExit: -777777''')

def printUserNumberSameError():
    '''it prints error message if the user entered numbers are equal'''
    print('''Sorry, that is an invalid try.''')

def inputNum(prompt):
    '''this function lets take input from the user for different prompts'''
    Num = int(raw_input(prompt))
    return Num

def userNum():
    '''this function assigns three variable the value user enters'''
    leftPosNumUser = inputNum("Enter digit for left position: ")
    middlePosNumUser = inputNum("Enter digit for middle position: ")
    rightPosNumUser = inputNum("Enter digit for right position: ")
    return leftPosNumUser, middlePosNumUser, rightPosNumUser
    
def comeBackMessage():
    '''it prints come back and play again sometime message'''
    print("Come back and play again sometime")


def hitC(num1, num2):
    '''this function returns true if two numbers given are equal.'''
    return num1 == num2
def hitChecker(userNum1,userNum2, userNum3, houseNum1, houseNum2, houseNum3):
    '''this function check if there is any hit in the numbers entered by the user and house'''
    HIT =0
    sub =0
    if hitC(userNum1 , houseNum1):
        HIT = HIT +1
        sub +=1 
    if hitC(userNum2, houseNum2):
        HIT = HIT +1
        sub +=1
    if hitC(userNum3, houseNum3):
        HIT = HIT +1
        sub+=1
    return HIT, sub


def match(userNum1,userNum2, userNum3, houseNum1, houseNum2, houseNum3):
    '''this function check if there is any match in the given set of numbers
first three numbers are user entered and last 3 numbers are house generated'''
    MATCH =0
    if (userNum1 in (houseNum1, houseNum2, houseNum3)):
        MATCH = MATCH +1
    if (userNum2 in (houseNum1, houseNum2, houseNum3)):
        MATCH = MATCH +1
    if (userNum3 in (houseNum1, houseNum2, houseNum3)):
        MATCH = MATCH +1
    return MATCH

def printHitAndMatch(hit, match):
    '''this prints the number of hit and matches'''
    print(' %i Hits'%(hit))
    print(' %i Match'%(match))

def playOneHitAndMatchGame():
    '''this function lets the user play hit and match game once'''
    welcomeMessage()
    print
    numLeft, numMiddle, numRight =  houseDigit()
    
    if twoDigitChecker(numLeft, numMiddle, numRight, 'House'):
        if threeDigitChecker(numLeft, numMiddle, numRight, 'House'):
            userNumLeft, userNumMiddle, userNumRight = userNum()
            if twoDigitChecker(userNumLeft, userNumMiddle, userNumRight, 'User'):
                if threeDigitChecker(userNumLeft, userNumMiddle, userNumRight, 'User'):
                    numberOfHit, sub=  hitChecker(userNumLeft, userNumMiddle, userNumRight, numLeft, numMiddle, numRight)
                    numberOfMatch = match(userNumLeft, userNumMiddle, userNumRight, numLeft, numMiddle, numRight)
                    numberOfMatch = numberOfMatch - sub
                    print
                    printHitAndMatch(numberOfHit, numberOfMatch)
    comeBackMessage()
    print

def main():
    while True:
        playOneHitAndMatchGame()

if __name__ == '__main__':
    main()
