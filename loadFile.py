# allow the user to load in a file to be read and put into the warehouse

def loadInCrates(): 
    path = "testData.txt"
    data = open(path, "r")
    dataList = data.readlines()
    for x in dataList:
        dataList[dataList.index(x)] = x.strip()
    print(dataList)
    return dataList

if __name__ == "__main__":
    loadInCrates()