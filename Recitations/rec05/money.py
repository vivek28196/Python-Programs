''' it is a module that deals wiht the money. i has 5 functions. they work they do is
print amount as usdollars, convert pesos to us dollars, print the amount as coins, print the bill,
print the quantity of coins
'''
from __future__ import print_function
import math

PESOS_TO_DOLLAR = 0.074

def  printAsUSDollars(amount):
    ''' it print the amount as USDamount. it also rounds off the amount to 2
decimal places'''
    amount = round(amount,2)
    print ("USD %0.2f" %( amount))
    return amount

def convertPesosToUSDollars(amount):
    '''it convert the peso amount to the us dollars'''
    pesoAmt = amount * PESOS_TO_DOLLAR  
    return pesoAmt

def printAsCoins(amount):
    '''it gives the amount in coins of dollar, quarter dimes, nickel, pennies'''
    amount = amount*100
    dollars = amount//100
    quarters= (amount%100)//25
    leftAmount = amount -(dollars*100+(quarters*25))
    dimes =leftAmount //10
    leftAmount = amount -(dollars*100 +(quarters*25)+ (dimes*10))
    nickel = leftAmount//5
    leftAmount = amount -(dollars*100 +(quarters*25)+ (dimes*10)+(nickel*05))
    pennies = leftAmount//1
    return dollars, quarters, dimes, nickel, pennies


def printBill(dollars, quarters, dimes, nickel, pennies):
    '''it prints the bill amount owed'''
    if (dollars != 0):
        print ("%i dollar(s)"  %(dollars))
    if (quarters !=0):
        print ("%i quarter(s)" %(quarters))
    if (dimes != 0):
        print ("%i dime(s)" %(dimes))
    if (nickel !=0):
        print ("%i nickel(s)"  %(nickel))
    if (pennies !=0):
        print ("%i penny(ies)" %(pennies))
def quantityOfCoins(amount):
    ''' this function calculates the amount in terms of dollars, quarters, dimes, nickel and pennies'''
    dollars, quarters, dimes, nickel, pennies = printAsCoins(amount)
    totalNoOfCoins = dollars+ quarters+ dimes+ nickel+ pennies
    print("total number of coins are: %i" %(totalNoOfCoins))
    return totalNoOfCoins
