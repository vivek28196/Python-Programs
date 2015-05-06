
#!C:\Python27\python.exe
from __future__ import print_function

'''
Program level docstring:

Student: Vivek Aggarwal
File Name: rec10.py

this is a menu driven program.

The following program is designed to gather family shopping list, check the input against
a pre-made lists of dont buy items made for the each family member and generate shopping list based on available food items in store


Assumption: user is family



'''
AVAILABLE_FOOD_ITEMS = ["milk", "chocolate covered cherries", "apple", "orange", "banana", "corn on the cob", "kampyo sushi", "asparagus", "avacado",
                      "alfalfa", "acorn squash", "almond package", "arugala bunch", "artichoke", "applesauce", "wasabi", "udon noodles", "tunafish can",
                      "apple juice", "avocado sushi", "bruscetta", "bagel", "barley", "bisque", "bluefish", "bread", "broccoli", "buritto", "babaganoosh",
                      "cabbage", "chocolate cake", "red velvet cake", "strawberry short cake", "carrots", "celery", "cheese", "catfish", "chowder", "clams",
                      "coffee", "corn", "crab", "curry", "cereal", "chimichanga", "dumpling", "donut", "egg", "enchilada", "eggroll", "english muffin",
                      "edimame", "eelSushi", "o toro sashimi", "fajita", "falafel", "fondu", "french toast", "french dip", "garlic", "ginger", "gnocchi",
                      "granola", "grape", "green bean", "guacamole", "gumbo", "grits", "graham crackers", "halibut", "honey", "huenos rancheros", "hash browns",
                      "hummus", "chocolate ice cream", "strawberry ice cream", "cherry garcia ice cream", "puri", "veggie kurma", "jambalaya", "kale", "ketchup",
                      "kiwi", "kidney beans pckg", "great northern beans pckg", "lobster", "linguine", "lasagna", "pepperoni pizza", "mushroom pizza",
                      "pancakes", "quesadilla", "quiche", "spinach", "spaghetti", "tater tots", "toast", "waffles", "walnuts", "peanuts", "hazelnuts", "cranberries",
                      "yogurt", "ziti", "zucchini", "canteloupe", "figs", "salt", "pepper", "nutmeg", "yucca", "shichimi"]





def dontBuyListG():
    '''this function creates the dont buy list for the shopping list'''
    global AVAILABLE_FOOD_ITEMS          
    print ("enter item for i wont buy list.")
    print()
    dontBuyList = []
    item = raw_input("Enter the item and write 'done' when complete")
    item= item.lower()
    while item != "done":
        if item in AVAILABLE_FOOD_ITEMS:
            if item not in dontBuyList:
                dontBuyList.append(item)
                item = raw_input("Enter Food item")
                item= item.lower()
                print()
            else:
                print("item already in list")
                print()
                item= raw_input("Enter Food item")
                
    print()
    return dontBuyList

def addShopList(shoppingListI, dontBuyList):
    '''this function is used to add the stuff to the shopping list after its made'''
    global AVAILABLE_FOOD_ITEM
    print()
    item = raw_input("Enter the item and write 'done' when complete")
    item= item.lower()
    while item != "done":
        shoppingList(item, shoppingListI, dontBuyList)
        item = raw_input("Enter Food item")
        item= item.lower()
    print()
    return shoppingListI

def shoppingList(item,shoppingListI, dontBuyDict, name):
    '''this function is used to add item to shopping list'''
    global AVAILABLE_FOOD_ITEMS
    
    if item in AVAILABLE_FOOD_ITEMS:
        if item not in dontBuyDict[name]:
            shoppingListI = shoppingListI.append(item)

    return shoppingListI

def getItem():
    '''this function gets input from the user'''
    print()
    item =raw_input("Enter an item to shop. enter done when complete")
    item =item.lower()
    print()
    return item

def printAvailableFood(AVAILABLE_FOOD_ITEMS):
    ''' this funtion prints available food items'''
    print ("AVAILABLE FOOD ITEMS TO PURCHASE")
    for index in AVAILABLE_FOOD_ITEMS:
        print (index)
    print()

def createShoppingList(dontBuyDict,name):
    ''' this function creats shopping list'''
    shoppingListI =[]
    item = getItem()
    while item != "done":
        shoooingListI =shoppingList(item,shoppingListI,dontBuyDict, name)
        item =getItem()
    return shoppingListI

def printList(lists):
    '''this function prints the lists passed to it'''
    print()
    for item in lists:
        print(item)
        

def quantityList(lists):
    '''this function arranges the food items categorised'''
    
    listLength = len(lists)
    newList = []
    for item in lists:
        if item not in newList:
            numberOfItems = lists.count(item)
            subList =[item, numberOfItems]
            newList.append(subList)
    for item in newList:
        num = newList.count(item)
        while num >1:
            newList.remove(item)
            num = newList.count(item)
    
    return newList

def printQuantityList(lists):
    '''this function sorts the list and print them'''
    lists.sort()
    print()
    print ("---Family Shopping List---")
    print ("Food          Quantity to Buy")
    for item in lists:
        print ("%s   \t\t%i"%(item[0],       item[1]))
    print()
        
def createList(dontBuyDict, name):
    '''this function creates the list on the whole'''
    
    shoppingListI =createShoppingList(dontBuyDict, name)
    printList(shoppingListI)
    return shoppingListI

def createDontBuyDict(AVAILABLE_FOOD_ITEMS):
    '''this function creates dont buy list for the family members'''
    dontBuyDict={}
    noOfMember=int(raw_input("enter the number of house members"))
    for index in range(noOfMember):
        nameOfMember=raw_input("enter Your Name")
        printAvailableFood(AVAILABLE_FOOD_ITEMS)
        shopping_list=dontBuyListG()
        dontBuyDict[nameOfMember]=shopping_list
    return dontBuyDict

def addDeleteDontBuy(dontBuyDict):
    '''this function allows user to add or delete item from their i wont buy list'''
    name=raw_input("Enter your name")
    lists=dontBuyDict[name]
    print()
    choice=raw_input("write A for Add and D for Delete")
    choice = choice.lower()
    if choice == 'a':
        item=raw_input("enter the item to add write done when complete")
        item=item.lower()
        while item != 'done':
            if item not in lists:
                lists.append(item)
            else:
                print("item already in list")
            item=raw_input("enter the item to add")
            item=item.lower()
    elif choice =='d':
        item=raw_input("enter the item to delete and write done when complete")
        item.lower()
        while item != 'done':
            if item in lists:
                lists.remove(item)
               
            else:
                print("item not in list")
            item=raw_input("enter the item to delete and write done when complete")
            item.lower()
    return dontBuyDict


def menu():
    ''' this function prints the menu for the user'''
    print()
    print("1 : print list in order")
    print("2 : quit ")
    print("3 : create a dont Buy lists for family members")
    print("4 : add or delte in dont buy dict")
    print("5 : create shopping list")
    choice = raw_input("Enter Your Choice:")
    return choice


def main():

    while True:
        choice= menu()
        if choice =='3':
            dontBuyDict = createDontBuyDict(AVAILABLE_FOOD_ITEMS)
            
        if choice =='4':
            
            dontBuyDict = addDeleteDontBuy(dontBuyDict)
            
        if choice =='2':
            exit()
            break
        if choice =='5':
            name=raw_input("Enter the name of the designated shopper")
            shoppingList=createList(dontBuyDict, name)
        
        if choice =='1':
            
            lists=quantityList(shoppingList)
            printQuantityList(lists)
    
    

    
   
main()      
