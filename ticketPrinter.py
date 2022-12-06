# this file is going to be used to format data to a human readable format, similiar to how tables are shown in the mysql terminal
# from classes import *
from persistData import *


# show all containers
def containerLine():
    cursor.execute("SELECT * FROM Containers")
    containers = cursor.fetchall()
    for i in containers:
        print(f"Container Number : {i[0]}    Number of Crates : {i[1]}")


def shortHandCrateSheet():
    # get all container IDS
    cursor.execute("SELECT ContainerID FROM Containers")
    containers = cursor.fetchall()
    for i in containers:
        formattedList = []
        cursor.execute("SELECT * FROM Crates WHERE ContainerID=?", i)
        crates = cursor.fetchall()
        print(f"Container {i[0]} contains: ", end="")
        tempSet = set(crates)
        for x in tempSet:
            tempDict = {"item": x[1], "count": crates.count(x)}
            formattedList.append(tempDict)
        # print(f"Container {i[0]} Contains : {formattedList}")
        for item in formattedList:
            print(f' {item["item"]} x{item["count"]} crate(s),', end="")
        print("")
        blankLine()


# Prints every crate but can be chosen whether or not to be called in favour of the shorthand
def crateSheet():
    flag = False
    while flag != True:
        choice = input("Compact view?: (Y/N) : ")
        if choice.upper() == "Y":
            flag = True
            shortHandCrateSheet()

        elif choice.upper() == "N":
            cursor.execute("SELECT * FROM Crates")
            crates = cursor.fetchall()
            for i in crates:
                print(f"Container Number : {i[0]}    Crate Contents: {i[1]}")
            flag = True
        elif choice.upper() != "Y" or choice.upper() != "N":
            print("Please choose either Y or N")


# want to find out if there is a nicer way to do this
def blankLine():
    print("----------------------------------------------")


def inventoryTicket():
    blankLine()
    print("Current Inventory")
    blankLine()
    containerLine()
    blankLine()
    crateSheet()
    blankLine()


if __name__ == "__main__":
    inventoryTicket()
