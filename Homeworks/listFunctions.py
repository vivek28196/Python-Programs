from __future__ import print_function
import copy
'''
cs1114
Submission: hw08
Programmer: Vivek Aggarwal
Username: va713
File Name: listFunctions.py

this is a module listFunctions which contains various functions for the list


assumptions: list is numeric
'''
def printListByLine(lists):
    '''this function prints the list elements per line'''
    for item in lists:
        print(item)

def minimumValue(lists):
    ''' this function returns the minimum Value of the list passed to it'''
    temp=lists[0]
    for item in lists:
        if temp >item:
            temp = item
    return temp

def minimumValueIndex(lists):
    '''this functions returns the index of minimum value in the list passed'''
    temp=minimumValue(lists)
    index=lists.index(temp)
    return index

def deleteSubsequence(lists, startIndex, endIndex):
    '''this function delete subsequence for the list passed and the index given for start and end '''
    diff=endIndex-startIndex
    for index in range(diff+1):
        lists.pop(startIndex)
        

def intersectElements(lists1, lists2):
    '''this function returns the list which contains the common elements of lists passed to it'''
    lists3=[]

    for item in lists1:
        if item in lists2:
            if item not in lists3:
                lists3.append(item)
   
    return lists3


def reorderSortMix(list1 , list2):
    '''this function returns the list  '''
    lista=copy.deepcopy(list1)
    listb=copy.deepcopy(list2)
    lista.sort(reverse=True)
    minValueb=minimumValue(listb)
    a=0
    for element in lista:
        a +=1
        if element > minValueb:
            if  lista[a]<minValueb:
                length=len(listb)
                for x in range(length):
                    var=listb.pop(0)
                    print(var)
                    lista.insert(a+x,var)
            if lista[a]==minValueb:
                length=len(listb)
                for x in range(length):
                    var=listb.pop(0)
                    lista.insert(a+x+1,var)
    return lista

                
    







    
