from __future__ import print_function

'''
cs1114
Submission: hw08part1-3
Programmer: Vivek Aggarwal
Username: va713
File Name: hw08part1-3.py


this is the combination of three parts first to draw number of stars the user input.
second to generate power series list third to draw hyphens'''

def checkNum(num):
    '''this function checks if the num is positive or not'''
    return(num > 0)
    

def drawStar(num):
    '''it prints the number of stars based on the input'''
    if checkNum(num):
        for index in range(num):
            print('*', end = '')
    else:
        print("enter no grater than 0")


def getNumOfStars():
    '''it receives input of number of stars'''
    num=int(raw_input("enter the no. of stars you want to see"))
    return num



def powerList(start, end, exponent =2):
    '''it generates power series list with start num end num and expnential power'''
    power_list=[index**exponent for index in range(start, end+1)]
    return power_list

def draw_hyphens(listy):
    '''this function draws hyphens from list'''
    for item in listy:
        for i in range(item):
            print('-' , end='')
        print(item)

def getStartEndExponent():
    '''this function receives input for powerList function'''
    start= int(raw_input("enter the start Number for power Series? "))
    end= int(raw_input("enter the end Number for power Series? "))
    exponent= int(raw_input("enter the exponent for power Series? "))
    return start, end, exponent


def main():
    num=getNumOfStars()
    start, end, exponent= getStartEndExponent()
    power_list=powerList(start,end, exponent)
    draw_hyphens(power_list)
    drawStar(num)
    

main()




