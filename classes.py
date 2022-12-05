class Crate:
    # Crates store one type of item
    def __init__(self, paraType):
        self.crateType = paraType

    def crateInfo(self):
        print(f"Crate contains {self.crateType}")
        return self.crateType


class Container:
    # Containers hold 12 crates each
    def __init__(self):
        self.crateList = []
        # self.containerId =
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
            tempDict = {x: tempMemory.count(x)}
            returnList.append(tempDict)
        print(returnList)
        self.storedMemory = returnList

    def addCrates(self, Crate):
        self.crateList.append(Crate)

    def listContents(self):
        print(f"Current contents are: ")
        returnList = []
        for y in self.crateList:
            returnList.append(y.crateInfo())
        return returnList
