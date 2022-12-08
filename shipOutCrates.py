from persistData import *
from ticketPrinter import *
from searchForCrates import *

# prompt the user to input what they are wanting to ship
# we assume that the user wishes to send out all of one specified item.


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
    formattedList = searchForCrates(shippingList)
    for item in formattedList:
        #  format the shipping list
        print(
            f' x{item["count"]} crate(s) of {item["item"]} in container: {item["containerID"]}')
        blankLine()
    return formattedList


# remove the specified items from the database
def shipTheItems(itemList):
    for i in itemList:
        try:
            cursor.execute(
                f'DELETE FROM Crates WHERE ContainerID={i["containerID"]} AND Contents="{i["item"]}";')
            print(
                f'{i["item"]} x{i["count"]} from container {i["containerID"]} has been shipped!')
            conn.commit()
        except Exception as e:
            print("Item not in storage, please check your spelling and try again!")

    # cleanup empty containers and update the crate count.
    manageEmptyContainers()


def mainShippingFunction():
    # get items to be shipped out, then ask whether they are to be shipping them out
    shippingList = createShippingList()
    itemList = createShippingTicket(shippingList)
    flag = False
    while flag == False:
        endLoop = input("Are the items going to be shipped now? (Y/N) : ")
        try:
            if endLoop.upper() == "Y":
                blankLine()
                shipTheItems(itemList)
                flag = True
            else:
                flag == False
        except Exception as e:
            print(e)

    blankLine()
