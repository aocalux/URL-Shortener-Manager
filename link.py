import os as os

def create(linkDetails, folderPath):
    indexLoc = folderPath + "/" + linkDetails[0] + "/index.html"

    os.mkdir(folderPath + "/" + linkDetails[0])
    with open(indexLoc, "w") as index:
        index.write(getTemplate().replace("{link.destination}", linkDetails[1]))
    
    return 0


def getTemplate():
    text = ""

    with open("linktemplate.html", "r") as file:
        for line in file:
            text += line

    return text