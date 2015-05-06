
''' 
Programmer: Vivek Aggarwal
Username: va713

filename: hw02.py

This program allows the user to input 2 characters and then give an output
string sequence multiplied by the difference between the characters.

constraints: none


assumtions: none

'''
from __future__ import print_function
import os

def getCheckeredLine():
    '''it prints a string sequence of two characters as many times equal to their diff in ascii values'''
    firstChar=str( raw_input("Enter First Char: "))
    secondChar=str(raw_input("Enter Second Char: "))
    print()
    firstCharNum=ord(firstChar)
    secondCharNum = ord(secondChar)
    diff = abs(firstCharNum - secondCharNum)
    string = firstChar+secondChar
    if diff > 12:
        diff = diff-12
        print()
        
    if diff > 12:
        diff = diff-12
        print()
        
    if diff > 12:
        
        diff = diff-12
        print()
        
    if diff > 12:
        diff = diff-12
        print()

    if diff > 12:
        diff = diff-12
        print()
        
    if diff > 12:
        diff = diff-12
        print()
        
    if diff > 12:
        diff = diff-12
        print()
        
    if diff < 12:
        print (string*diff)
    os.system
    
 
