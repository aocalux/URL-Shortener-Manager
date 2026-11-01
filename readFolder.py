import os as os
import LINK_BLACKLIST as linkBlacklist

from MAGIC_NUMBERS import *

DIR_BALCKLIST = linkBlacklist.getBlacklist()


def getLinks(folderPath):
    print(folderPath)
    dirlist = os.listdir(folderPath)
    links = [dir for dir in dirlist if os.path.isdir(folderPath + "/" + dir)]
    links = [dir.lower() for dir in links if dir.upper() not in DIR_BALCKLIST]
    return links


def getDestination(link, folderPath):
    if link.upper() in DIR_BALCKLIST:
        return INVALID_LINK

    destination = ""

    with open(folderPath + "/" + link + "/index.html", "r") as file:
        for line in file:
            destination = line.replace("\n", "")
            break

    return destination
