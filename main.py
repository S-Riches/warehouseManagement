# main file to be run.
from loadFile import *
import classes
# running this automatically sets up the DB
from persistData import *


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
for x in warehouse:
    x.containerMemory()


