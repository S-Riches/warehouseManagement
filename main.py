# main file to be run.
from loadFile import *
import classes
# running this automatically sets up the DB
from persistData import *
import ticketPrinter
import shipOutCrates
import searchForCrates
# more useful for testing to avoid duplicates


def askBeforeReading():
    flag = False
    while flag != True:
        choice = input("Do you wish to load in the text file? : (Y/N) : ")
        if choice.upper() == "Y":
            flag = True
            loadInTextFile()
        elif choice.upper() == "N":
            flag = True
        elif choice.upper() != "Y" or choice.upper() != "N":
            print("Please choose either Y or N")


# containing function
def loadInTextFile():  # create data, needs to be inputted in the text file

    testList = loadInCrates()

    # holder for all of the containers
    warehouse = []

    counter = 0
    # initial container creation
    currentContainer = classes.Container()

    # load in data from the text file.
    for t in testList:
        if counter <= 11:
            tempCrate = classes.Crate(t)
            currentContainer.addCrates(tempCrate)
            counter += 1
        else:
            counter = 0
            warehouse.append(currentContainer)
            currentContainer = classes.Container()
    warehouse.append(currentContainer)
    # for each container in the warehouse
    for container in warehouse:
        # save the data in each container within its own memory
        container.containerMemory()
        # add the container to the sql db
        addContainer(container.listContents())
        # add each crates
        crates = container.listContents()
        # get the newest container id
        containerID = getContainerId()
        # add each crate to the container
        for crate in crates:
            addCrate(containerID, crate)


def mainOptions():
    # prompts the user if they want to load in the text file
    askBeforeReading()
    # flag boolean value to determine whether the user has decided to close the program or not
    isRunning = True
    while isRunning:
        ticketPrinter.blankLine()
        print("Please input an option :")
        print("1. View a ticket of the warehouse inventory")  # read
        print("2. Search for a specific item")  # search
        # delete and also update as the containers are updated after shipping out
        print("3. Ship out items")
        print("4. To exit the program")
        ticketPrinter.blankLine()
        while True:
            try:
                choice = int(input(" : "))
                break
            except Exception:
                print("Please input a number")
        if choice == 1:
            ticketPrinter.blankLine()
            ticketPrinter.inventoryTicket()
        elif choice == 2:
            inputList = []
            # create a list here to be put into the function
            while True:
                ticketPrinter.blankLine()
                inputList.append(input("Item Name :"))
                choice = input("Done? (Y/N) : ")
                if choice.upper() == "Y":
                    break
            result = searchForCrates.searchForCrates(inputList)
            if len(result) > 0:
                for item in result:
                    print(
                        f' x{item["count"]} crate(s) of {item["item"]} in container: {item["containerID"]}')
            else:
                ticketPrinter.blankLine()
                print("Sorry that item isn't in the warehouse")
        elif choice == 3:
            ticketPrinter.blankLine()
            shipOutCrates.mainShippingFunction()
        elif choice == 4:
            print("Goodbye!")
            break


if __name__ == "__main__":
    mainOptions()
