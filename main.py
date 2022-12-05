# main file to be run.
from loadFile import *
import classes
# running this automatically sets up the DB
from persistData import *


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
def loadInTextFile():

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


if __name__ == "__main__":
    askBeforeReading()
