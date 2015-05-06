#!/c:python27/python.exe

from __future__ import print_function
import copy
import os

''' 
cs1114 

Submission: hw09 

Programmer: Vivek Aggarwal
Username: va713

Purpose of program, assumptions, constraints:

The program level documentation goes here

this progrma sorts the data of countries with the percent change in largest and smallest
and also gives the average
What the program does
Any special tricks
Any assumtions
Any constraints
etc..

'''

period1='1970-1990'
period2='1990-2007'
def getNameFile():
    '''it gets the existing name of file'''
    '''Asks the user for a name of a file to be read'''
    fName=str(raw_input("What is the name of the file to read? "))
    while(os.path.exists(fName) is False):
        fName=str(raw_input("File does not exist. Try again: "))

    return fName

def sortFilePeriod (fName):
    '''this sort the file according to two given periods'''
    
    listOfCountries1970to1990 = []
    listOfCountries1990to2007 = []
    fh=open(fName, 'r')
    lines=fh.readlines()
    
    for lists in lines:
        lists=lists.split()
        if period1 in lists:
            listOfCountries1970to1990.append (lists)
            
        elif period2 in lists:
            listOfCountries1990to2007.append (lists)
    fh.close()
    return listOfCountries1970to1990, listOfCountries1990to2007


def listToDict(lists):
    '''this converts list to dictionery'''
    dict1={}
    for item in lists:
        
        name=item[0].strip(',')
        percentage = item[-1]
        dict1[percentage]=name

    values1=dict1.keys()
    values1.sort()
    


    return dict1, values1
    
def maxx(dict1, values):
    '''it gives the 3 largest change in country with names'''
    name1=dict1[values[-1]]
    large1=values[-1]
    name2=dict1[values[-2]]
    large2=values[-2]
    name3=dict1[values[-3]]
    large3=values[-3]
    
    return (name1, large1, name2, large2, name3, large3)

def minn(dict1, values):
     '''it gives the 3 smallest change in country with names'''
     names1=dict1[values[1]]
     small1=values[1]
     names2=dict1[values[2]]
     small2=values[2]
     names3=dict1[values[3]]
     small3=values[3]
     return (names1, small1, names2, small2, names3, small3)

def avg(lists):
    '''this gives the average of change values'''
    counter=0
    accumulator=0
    
    for items in lists:
        items1=items.strip('%')
        counter +=1
        accumulator += float(items1)
    avg=float(accumulator)/counter
    
    return avg

def writeData(prompt,avg1,largestChange, smallestChange ):
    '''this function wirtes data in new file'''
    (names1, small1, names2, small2, names3, small3)=smallestChange
    (name1, large1, name2, large2, name3, large3)=largestChange
    fh=open(prompt+"_summary.txt", 'w')
 
    fh.write('\t'+prompt+" Summary Report\n")
    fh.write("\n")
    fh.write("average percent change overall %0.3f\n" %(avg1))
    fh.write("\n")
    fh.write("The three countries or regions with the largest change:\n")
    fh.write("\n")
    fh.write(name1+ "  "+ large1 +"  " + name2 + "  " + large2 + "  " + name3 + "  " + large3 )
    fh.write("\n")
    fh.write("\n")
    fh.write("The three countries or regions with the smallest change:\n")
    fh.write("\n")
    fh.write(names1+ "  "+ small1 + "  " + names2 + "  "  + small2 + "  " + names3 +  "  " + small3)
    fh.close()

def main():
    fName = getNameFile()
    listOfCountries1970to1990, listOfCountries1990to2007=sortFilePeriod(fName)
    dict1970,values1970=listToDict(listOfCountries1970to1990)
    dict1990,values1990=listToDict(listOfCountries1990to2007)
    largestChange = maxx(dict1970,values1970)
    smallestChange=minn(dict1970,values1970)
    avg1=avg(values1970)
    writeData('1970_1990',avg1,largestChange, smallestChange)
    
    name1, large1, name2, large2, name3, large3 = maxx(dict1990,values1990)
    names1, small1, names2, small2, names3, small3=minn(dict1990,values1990)
    avg1=avg(values1990)
    writeData('1990_2007',avg1, largestChange, smallestChange)
main()


    





