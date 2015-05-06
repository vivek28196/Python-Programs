#!/c:python27/python.exe
from __future__ import print_function
'''
cs1114

name vivek aggarwal
username va713
filename: rec11.py

this prog has file functions to read from file and write an html file



'''




def readFileToLs():
    lists=[]
    filename=raw_input("enter the file name")
    if filename.endswith('.txt'):
        fh=open(filename)
    else :
        fh=open(filename+".txt")
    for line in fh:
        line.strip()
        a=line.split()
        for element in a:
            lists.append(element)
    print lists
    return lists

def createHTML():
    
      
    nameOfFile=raw_input("enter the name of the file")
    split1=nameOfFile.split('.')
    filename=split1[0]
    filename+='.html'
    while test=os.exist(filename):
        filename=print("file exist enter another name")
        split1=nameOfFile.split('.')
        filename=split1[0]
        filename+='.html'
        fh=open(nameOfFile , 'w')
    return fh



def modifyHtml(filename):

    fh=createHTML()
    fColor= open("colors.txt", 'r')
    title=raw_input("enter the title")
    headline=raw_input("enter the headline")
    size=raw_input("enter the heading size")

    



    



    
