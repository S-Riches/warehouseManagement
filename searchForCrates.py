from classes import *
from persistData import *


# allows the user to put in a list of what they want to search for
def searchForCrates(items):
    formattedList = []
    for x in items:
        try:
            # attempt to get the items from the db
            cursor.execute(
                f"SELECT * FROM Crates WHERE Contents='{x.lower()}'")
            result = cursor.fetchall()
            # convert to a set to count the unique results
            tempSet = set(result)
            for x in tempSet:
                tempDict = {"containerID": x[0],
                            "item": x[1], "count": result.count(x)}
                formattedList.append(tempDict)

        except Exception as e:
            print(e)
    return formattedList
