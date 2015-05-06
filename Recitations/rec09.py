
#!C:\Python27\python.exe
from __future__ import print_function

'''
Program level docstring:

Student: Vivek Aggarwal
File Name: rec09.py

this is a menu driven program.

The following program is designed to gather family shopping list, check the input against
a pre-made list of dont buy items and generate shopping list based on available food items in store

It's a shopping list generator, designed to only gather and pretty print the input of the
user along with the quantity that they entered.

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
            dontBuyList.append(item)
            item = raw_input("Enter Food item")
            item= item.lower()
            print()
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

def shoppingList(item,shoppingListI, dontBuyList):
    '''this function is used to add item to shopping list'''
    global AVAILABLE_FOOD_ITEMS
    if item in AVAILABLE_FOOD_ITEMS:
        if item not in dontBuyList:
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

def createShoppingList(dontBuyList):
    ''' this function creats shopping list'''
    shoppingListI =[]
    item = getItem()
    while item != "done":
        shoooingListI =shoppingList(item,shoppingListI,dontBuyList)
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
        print ("%s\t\t%i"%(item[0],       item[1]))
    print()
        
def createList():
    '''this function creates the list on the whole'''
    
    printAvailableFood(AVAILABLE_FOOD_ITEMS)
    dontBuyList = dontBuyListG()
    shoppingListI =createShoppingList(dontBuyList)
    printList(shoppingListI)
    return shoppingListI, dontBuyList

def menu():
    ''' this function prints the menu for the user'''
    print()
    print("1 : add shop List")
    print("2 : create the dsper's wont buy list")
    print("3 : display in order")
    print("4 : quit and print shopping list in alphabetical order")
    choice = raw_input("Enter Your Choice:")
    return choice

def main():
    shoppingListI=[]
    counter =0
    while True:
        choice = menu()
        if choice=='1':
            if counter:
                shoppingListI = addShopList(shoppingListI, dontBuyList)
            else:
                print("please create the dsper's wont buy list first")
        if choice =='2':
            shoppingListI, dontBuyList=createList()
            counter =1
        if choice=='3':
            lists= quantityList(shoppingListI)
            printQuantityList(lists)
        if choice == '4':
            lists= quantityList(shoppingListI)
            printQuantityList(lists)
            break
      



main()      
