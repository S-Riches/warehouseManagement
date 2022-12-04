# file to deal with sql interactions
import sqlite3 as sql

# connection
conn = sql.connect("./persist.db")

# cursor
cursor = conn.cursor()

# initialise the tables if not already there
try:
    # create the containers
    cursor.execute(
        """
        CREATE TABLE "Containers" (
            "ContainerID" INTEGER NOT NULL UNIQUE,
            "CrateCount" INTEGER,
            PRIMARY KEY ("ContainerID" AUTOINCREMENT)
        )

        """
    )

    # create the crates
    cursor.execute(
        """
        CREATE TABLE "Crates"(
            "ContainerID" INTEGER,
            "Contents" TEXT,
            FOREIGN KEY("ContainerID") REFERENCES "Containers"
        )

        """
    )
    # feedback to user to let them know the tables have been created.
    print("Created initial tables")

except Exception as e:
    pass

def addCrate(containerID, crateContents):
    insertionList = list(containerID, crateContents)
    cursor.execute("INSERT INTO Crates VALUES (?, ?)", insertionList)
    conn.commit()
    print(f"{crateContents} was inserted into container {containerID}")

# get the container ID from the table, to allow the crates to be inserted correctly.
def getContainerId():
    cursor.execute("SELECT ContainerID FROM Containers ORDER BY ContainerID DESC LIMIT 1")
    result = cursor.fetchall()
    # converts the result from [(n,)] to just n
    result = str(result).strip("[( ,)]")
    print(result)
    return result
    

# function to add container with amount of crates
def addContainer(container):
    containerCount = len(container)
    cursor.execute(f"INSERT INTO Containers VALUES(NULL, {containerCount}) ")
    conn.commit()
    containerId = getContainerId()
    return containerId


# testing
# con = [{'chairs': 8}, {'coca cola': 4}]
# addContainer(con)
# getContainerId()

