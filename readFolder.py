import os as os

DIR_BALCKLIST = [".git"]

def getLinks(folderPath):
    print(folderPath)
    dirlist = os.listdir(folderPath)
    links = [dir for dir in dirlist if os.path.isdir(folderPath + "/" + dir)]
    links = [dir for dir in links if dir not in DIR_BALCKLIST]
    return links