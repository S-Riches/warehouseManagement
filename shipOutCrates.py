from persistData import *
from ticketPrinter import *
from searchForCrates import *

# prompt the user to input what it ems, and how many need to be shipped out


def createShippingList():
    print("Welcome to shipping requests")
    # create a list of crates to be shipped it
    flag = False
    shippingList = []
    while flag == False:
        shippingList.append(input("Input item : "))
        endLoop = input("Finished? (Y/N) : ")
        try:
            if endLoop.upper() == "Y":
                flag = True
            else:
                flag == False
        except Exception as e:
            print(e)
    return shippingList


def createShippingTicket(shippingList):
    blankLine()
    print("Shipping ticket")
    blankLine()
    searchForCrates(shippingList)


shippingList = createShippingList()
createShippingTicket(shippingList)
