
'''
Programmer: Vivek Aggarwal
Username: va713

rec12.py


constraints: none
assumptions: none

'''
from __future__ import print_function
import os
import random

def getNameFile():
    '''Asks the user for a name of a file to be read'''
    fName=str(raw_input("What is the name of the file to read? "))
    while(os.path.exists(fName) is False):
        fName=str(raw_input("File does not exist. Try again: "))

    fileHandle=open(fName, 'r')
        
    return (fName, fileHandle)

def getNameAndWriteFile():
    '''Asks the user to pick a name for the output file'''
    outfName=str(raw_input("What name do you want for the output file (do not bother with the extension)? "))
    orgName=outfName+".txt"
    while(os.path.exists(orgName)):
        decision=str(raw_input("Are you sure you want to overwrite the file? (Y/N) "))
        if (decision=="No" or decision=="N" or decision=="n" or decision=="no"):
            outfName=str(raw_input("Choose another name for the file (do not bother with the extension)? "))
            orgName=outfName+".txt"
            while(os.path.exists(orgName) is True):
                outfName=str(raw_input("Choose another name for the file (do not bother with the extension)? "))
                orgName=outfName+".txt"
            fileHandle=open(orgName,'w')

        elif(decision=="Yes" or decision=="Y" or decision=="yes" or decision=="y"):
            fileHandle=open(orgName,'w')
            break
    else:
        fileHandle=open(orgName,'w')
        
    return (orgName,fileHandle)
    
def createOutputFile(readFile,writeFile,bwString):
    ''' '''
    for line in readFile:
        splt=line.split()
        newString=bwString.join(splt)
        writeFile.write(newString+'\n')

    readFile.close()
    writeFile.close()

def reverseThing(readFile,writeFile,bwString):
    ''' '''
    for line in readFile:
        splt=line.split(bwString)
        btwStr=' '
        newString=btwStr.join(splt)
        writeFile.write(newString+'\n')

    readFile.close()
    writeFile.close()

def Stats(readFile,writeFile):
    ''' '''
    counter=0
    sum1=0
    splt=[]
    projectNum=''
    values=0
    j=0
        
    for line in readFile:
        for sth in line.split():
            splt.append(sth)
            counter+=1
            
    writeFile.write(splt[0]+'\n')
    
    for i in range(len(splt)-1):
        if(splt[i]=='*****'):
            projectNum=splt[i+1]
            writeFile.write(projectNum+'\n')
    for i in range(len(splt)-1):
        while(splt[i]!='*****'):
            j+=1
            values+=float(splt[j])
            break
        writeFile.write(str(values))


    
        

def main():
    fName,fileRead=getNameFile()
    orgName,fileWrite=getNameAndWriteFile()
    bwString=raw_input("Choose a string")
    createOutputFile(fileRead,fileWrite,bwString)
    print('''
                                REVERSE MODE
                                
                ''')
    secondfName,secondFileRead=getNameFile()
    secondorgName,secondFileWrite=getNameAndWriteFile()
    reverseThing(secondFileRead,secondFileWrite,bwString)
    Stats(fileRead,fileWrite)
    
    
if __name__ == "__main__":
    main()
