#!C:\Python26\python.exe
from __future__ import print_function
import os

''' 
cs1114 

Submission: hw01

Programmer: Vivek Aggarwal
Username: va713

In this program only the main function is defined by the programmer. other rest of the functions are not defined by the programmer. this programme is used to let know the understanding of execution of the progaramme


assumtions: none
constraints: none


'''
def main():
    firstName = getStrFromUser("What is your first name?")
    lastName = getStrFromUser("What is your last name?")
    boxChar= getStrFromUser("What character to use for the box?")
    fillChar = getStrFromUser("What character to use to fill in the box?")
    drawBoxAroundStr(firstName , boxChar , fillChar)
    drawBoxAroundStr(lastName , boxChar , fillChar)
    pythonicPause()
    




if __name__ == '__main__':
    main()
    
