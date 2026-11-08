import os as os
import shutil as shutil
import LINK_BLACKLIST as linkBlacklist
import ALLOWED_CHARS as allowedChars

from MAGIC_NUMBERS import *

DIR_BALCKLIST = linkBlacklist.getBlacklist()
ALLOWED = allowedChars.get()


def create(linkDetails, folderPath):
    if checkBlacklist(linkDetails[0]) == INVALID_LINK:
        return INVALID_LINK

    indexLoc = folderPath + "/" + linkDetails[0] + "/index.html"

    os.mkdir(folderPath + "/" + linkDetails[0])
    with open(indexLoc, "w") as index:
        index.write(getTemplate().replace("{link.destination}", linkDetails[1]))


def editLink(linkDetails, folderPath):
    if checkBlacklist(linkDetails[0]) == INVALID_LINK:
        return INVALID_LINK

    delLink(linkDetails, folderPath)
    create(linkDetails, folderPath)


def delLink(linkDetails, folderPath):
    if checkBlacklist(linkDetails[0]) == INVALID_LINK:
        return INVALID_LINK

    path = folderPath + linkDetails[0]
    shutil.rmtree(path)


def editShortcode(oldShortcode, newShortcode, destination, folderPath):
    if checkBlacklist(oldShortcode) == INVALID_LINK:
        return INVALID_LINK
    if checkBlacklist(newShortcode) == INVALID_LINK:
        return INVALID_LINK

    print(oldShortcode, newShortcode, destination)
    create([newShortcode, destination], folderPath)
    delLink([oldShortcode, ""], folderPath)


def getTemplate():
    text = ""

    with open("linktemplate.html", "r") as file:
        for line in file:
            text += line

    return text


def checkBlacklist(link):
    if link.upper() in DIR_BALCKLIST:
        return INVALID_LINK
    if not checkBlacklistHelper(link.upper()):
        print(ALLOWED)
        return INVALID_LINK


def checkBlacklistHelper(link):
    allowedChars = list(ALLOWED)
    print(allowedChars)
    print(link)
    for char in link.upper():
        if char not in allowedChars:
            print(char)
            return False
    return True
