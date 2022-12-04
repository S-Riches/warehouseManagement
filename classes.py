from loadFile import *

class Crate:
    # Crates store one type of item
    def __init__(self, paraType):
        self.crateType = paraType
    
    def crateInfo(self):
        print(f"Crate contains {self.crateType}")

class Container:
    # Containers hold 12 crates each
    def __init__(self):
        self.crateList = []
        self.storedMemory = []
    # get a list of dictionaries returning the count of different crates within the counter e.g. ("cheese" : 3, "foo" : 2) etc    
    def containerMemory(self):
        returnList = []
        # get a list of all the contents
        tempMemory = []
        for x in self.crateList:
            tempMemory.append(x.crateType)
        # sort them
        tempMemory.sort()
        # create a set to get unique items
        tempSet = set(tempMemory)
        # get how many times it is in the container
        for x in tempSet:
            tempDict = {x : tempMemory.count(x)}
            returnList.append(tempDict)
        print(returnList)
        self.storedMemory = returnList

    def addCrates(self, Crate):
        self.crateList.append(Crate)
        # sort after each added item
        # self.crateList.sort()

    def listContents(self):
        print(f"Current contents are: ")
        for y in self.crateList:
            y.crateInfo()


# populate the containers with test data
def testingFunc():
    counter = 0
    # stores all containers
    warehouse = []
    # create an initial container
    currentContainer = Container()
    
    dataList = loadInCrates()

    for i in dataList:
        if counter <= 11:
            testCrate = Crate(i)
            currentContainer.addCrates(testCrate)
            counter += 1
        else:
            counter = 0
            warehouse.append(currentContainer)
            currentContainer = Container()
    warehouse.append(currentContainer)
    for x in warehouse:
        # x.listContents()
        x.containerMemory()

if __name__ == "__main__":
    testingFunc()