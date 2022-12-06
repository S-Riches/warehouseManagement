from classes import *
from persistData import *


# allows the user to put in a list of what they want to search for
def searchForCrates(items):
    for x in items:
        formattedList = []
        try:
            cursor.execute(
                f"SELECT * FROM Crates WHERE Contents='{x.lower()}'")
            result = cursor.fetchall()
            tempSet = set(result)
            for x in tempSet:
                tempDict = {"item": x[1], "count": result.count(x)}
                formattedList.append(tempDict)
            for item in formattedList:
                print(f' {item["item"]} x{item["count"]} crate(s),', end="")
            print("")

        except Exception as e:
            print(e)
