#!C:\Python26\python.exe
from __future__ import print_function

import money
import random

STAMP74 =0.74
STAMP32 =0.32
STAMP06 =0.06


'''
cs1114
Submission: hw08part4
Programmer: Vivek Aggarwal
Username: va713
File Name: hw08part4.py

this program is a advanced stamping machine which calculate the amount you owe
when you purchase different stamps and also tell the exact change to be given
back. it also gives the prizes based on the different conditions. it also
prints the random generated banner. this will run infinite times until you write Manager
in first name and last name for maintainace work and for the statistics of machine.

'''



def welcomeCustomer():
    ''' it prints the welcome message for the customer'''
    print('''
--------------------------------------------
-   Welcome to the snakeStamp Machine!     -
-We dispense only 74, 32 and 6 cent stamps.-
-We give only coins in change - (no bills).-
--------------------------------------------''')

def getCustomerName():
    ''' it takes the first name and last name from the user'''
    print()
    firstName = raw_input("What is your first name?")
    print()
    lastName  = raw_input("What is your last  name?")
    return firstName, lastName

def numberOfStamps():
    ''' it takes the number of each stamp you require'''
    print()
    stamp74 = getPositiveValue("How many 74 cent stamps would you like?")
    print()
    stamp32 = getPositiveValue("How many 32 cent stamps would you like?")
    print()
    stamp06 = getPositiveValue("How many 06 cent stamps would you like?")
    print()
    return stamp74, stamp32, stamp06

def calculate(stamp74, stamp32, stamp06):
    ''' it calculates the total amount of the stamps and total number of stamps purchased'''
    totalAmount = stamp74*STAMP74 + stamp32*STAMP32 + stamp06*STAMP06
    numberOfStamps = stamp74 + stamp32 + stamp06
    return totalAmount, numberOfStamps

def printAmount(numberOfStamp, totalAmount):
    '''it prints the number of stamps purchased and total amount owed'''
    print("The Price of Your %i stamps is $%0.2f" %(numberOfStamp, totalAmount))
    print()

def getDollarAmount(totalAmount):
    '''it receives the amount of dollar the user gives'''
    dollarAmount=int(raw_input("How many dollars will you be giving us?"))
    while dollarAmount < totalAmount:
        dollarAmount=int(raw_input("How many dollars will you be giving us?"))
    return dollarAmount
    print()
    return dollarAmount

def printChange(totalAmount, firstName, lastName):
    '''it prints the the exact change to be given to the customer in dollars, quaters, dimes , nickel and penny'''
    print("Thank You. just a moment please....")
    print()
    print("Thanks %s %s, your change is:" %(firstName, lastName))
    print()
    dollars, quarters, dimes, nickel, pennies = money.printAsCoins(round(totalAmount,2))
    money.printBill(dollars, quarters, dimes, nickel, pennies)

def getRandomNumber(firstName):
    '''it get the random ratigs from the user'''
    print("CONGRATULATIONS %s" %(firstName))
    print()
    print("You have been chosen to help us evaluate our machine.")
    print()
    randomNumber = int(raw_input("""please rate our machine by entring a number between1 and 10, \n
with 10 being really great and 1 being horible: """))
    return randomNumber
                     
def prizeMoney(totalAmount, randomNo):
    '''this function evaluates the prize amount given to the customer'''
    rand = random.randint(1,1000)
    print()
    if (rand == randomNo):
        print("you won $50")
    elif (randomNo in [2,4,7] or 17.25 < totalAmount < 58.42):
        print("you won 2 dollars and 33 cents")
    elif(totalAmount > 1.37):
        print("you win 37 cents")
    else:
        print("you win 3 cents")
    print()
    print("ThankYou for using our stamp machine")
    print()
    
def thankYou():
    ''' it prints the thank you message'''
    print("""
---=====================================---
---Thank You for Using our stamp machine---
---=====================================---
""")

def randomChar():
    '''this function generates the random char and the random num for random banner'''
    randomChar1=random.randint(97,122)
    randomChar1 = chr(randomChar1)
    randNum1=random.randint(4,6)
    return randomChar1, randNum1

def printBannerLine(fillChar1):
    '''this function prints the random generated line in the random banner'''
    randomChar1, randNum1 = randomChar()
    randomChar2, randNum2 = randomChar()
    randomChar3, randNum3 = randomChar()
    randomChar4, randNum4 = randomChar()
    randomChar5, randNum5 = randomChar()
    totalNoOfChar = randNum1 + randNum2 + randNum3 +randNum4 + randNum5

    

    if (totalNoOfChar<31):
        leftChar= 30 - totalNoOfChar 
        print(str(randomChar1*randNum1) + str(randomChar2*randNum2) + str(randomChar3*randNum3) + str(randomChar4*randNum4) + str(randomChar5*randNum5) + str(str(fillChar1)*leftChar))
    else:
        print(str(randomChar1*randNum1) + str(randomChar2*randNum2) + str(randomChar3*randNum3) + str(randomChar4*randNum4) + str(randomChar5*randNum5))

def randomBannerBorder():
    ''' it prints random banner border'''
    print("/\\"*15)

def printRandomBanner(fillChar1, fillChar2, fillChar3):
    '''this function prints the random banner'''
    randomBannerBorder()
    printBannerLine(fillChar1)
    printBannerLine(fillChar2)
    printBannerLine(fillChar3)
    randomBannerBorder()

def calculatTipAndThankAndAdjustBills(totalAmount, dollarAmount):
    '''it calculates the tip amount and displays it. it returns the difference
in owed amount and amount given'''
    difference = dollarAmount-totalAmount
    tip = difference//1
    difference = difference -tip
    print()
    print("ThankYou for the generous Tip of %i dollars" %(tip))
    print()
    return difference

def getPositiveValue(prompt):
    '''this function help in getting the positive value of the stamps'''
    stamp = int(raw_input(prompt))
    while stamp<0:
        stamp = int(raw_input(prompt))
    return stamp
    
    

def dealWithOneCustomer(firstName, lastName,a,NumOfCustomer, largestAmount, smallestAmount,SAME_STAMP,PURCHASETILLNOW, percentage_no):
    '''function contaning all the other function required to run the program successfully once.'''
    printRandomBanner('-','-','-')
    welcomeCustomer()
    stamp74, stamp32, stamp06 = numberOfStamps()
    totalAmount, numberOfStamp = calculate(stamp74, stamp32, stamp06)
    printAmount(numberOfStamp, totalAmount)
    dollarAmount=getDollarAmount(totalAmount)
    calcAmount = dollarAmount - totalAmount
    difference = calculatTipAndThankAndAdjustBills(totalAmount, dollarAmount)
    printChange(difference, firstName, lastName)
    thankYou()
    randomNumber = getRandomNumber(firstName)
    prizeMoney(totalAmount, randomNumber)
    printRandomBanner('-' , '-', '-')
    
    PURCHASETILLNOW = totalPurchase(totalAmount,PURCHASETILLNOW)
    largestAmount, smallestAmount = largestSmallestPurchase(totalAmount,largestAmount, smallestAmount,a)
    avg = averagePurchase(PURCHASETILLNOW,NumOfCustomer)
    SAME_STAMP = peopleWithSameStamp(stamp74,stamp32,stamp06,SAME_STAMP)
    percentage_no = percentage(NumOfCustomer,SAME_STAMP)


    return NumOfCustomer,PURCHASETILLNOW, smallestAmount, largestAmount,SAME_STAMP, avg, percentage_no 

def pauseFunction():
    '''this function prints the message after the program is quitted by manager'''
    print('''Do Your Maintainace work
...AND...
don't forget to restart this program.''')
        

def largestSmallestPurchase(amount,largestAmount, smallestAmount,a):
    '''this function selects the amount for largest and smallest stats'''
    if a==0:
        smallestAmount = amount
        a = 1 
    
    if amount > largestAmount:
        largestAmount=amount
    if amount < smallestAmount:
        smallestAmount=amount
    return largestAmount, smallestAmount

def totalPurchase(amount, PURCHASETILLNOW):
    '''this function calculates the total purchase.'''
    PURCHASETILLNOW = PURCHASETILLNOW + amount
    return PURCHASETILLNOW

def averagePurchase(PURCHASETILLNOW, number):
    '''this function calculates the average purchase of the day'''
    avg=PURCHASETILLNOW/number
    return avg

def peopleWithSameStamp(stamp1, stamp2, stamp3,SAME_STAMP):
    '''this function increase the SAME_STAMP counter by 1 if quantity of stamp 1 is equal to 2 or 3'''
    if stamp1 == stamp2:
       SAME_STAMP = SAME_STAMP + 1
    elif stamp1== stamp3:
       SAME_STAMP = SAME_STAMP + 1
    return SAME_STAMP


def percentage(totalCustomer, SAME_STAMP):
    '''this function calculates percentage for people with same number of stamp'''
    print (totalCustomer, SAME_STAMP)
    percent=(SAME_STAMP/totalCustomer)*100
    return percent



def printStats(customer, large, small, avg, percentage, PURCHASETILLNOW):
    '''this function prints statistics for the person who quits the program with legitimate input'''
    print('''Stats
Number of customer: %i
Largest purchase:   %.2f
smallest purchase:  %.2f
average purchase:   %.2f
percentage of people
with same number of
 cent as either
of the other stamps %.2f

%0.2f'''%(customer, large,small,avg,percentage,PURCHASETILLNOW))



def main():
    NumOfCustomer = 0
    PURCHASETILLNOW =0
    largestAmount =0
    smallestAmount =0
    SAME_STAMP =0
    NumOfCustomer =0
    percentage_no = 0
    avg=0
    a=0
    
    while True:
        firstName, lastName =getCustomerName()
        if(firstName=="Manager" and lastName=="Manager"):
            break
        NumOfCustomer +=1
        NumOfCustomer,PURCHASETILLNOW, smallestAmount, largestAmount,SAME_STAMP, avg, percentage_no = dealWithOneCustomer(firstName, lastName,a,NumOfCustomer, largestAmount, smallestAmount,SAME_STAMP,PURCHASETILLNOW,percentage_no)
                
    pauseFunction()
    printStats(NumOfCustomer, largestAmount, smallestAmount, avg, percentage_no,PURCHASETILLNOW)


main()
