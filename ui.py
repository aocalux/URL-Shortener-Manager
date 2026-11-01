from MAGIC_NUMBERS import *


def startup():
    print("Hi!")


def getFolderPath():
    return input("URL-Shortener root: ")


def options():
    print("1 - New Link")
    print("2 - Edit Link destination")
    print("3 - Delete Link")
    print("4 - edit link shortcode")
    print("5 - show links and destinations")
    print("6 - show link destination")
    return int(input("Select an Option: "))


def showlinks(links):
    for link in links:
        print(link)


def editLinkShortcode(links):
    print(links)
    oldShortcode = input("Old Shortcode: ").lower()
    newShortcode = input("new shortcode: ").lower()
    return oldShortcode, newShortcode


def newLink():
    shortcode = input("Shortcode (ran - for random): ").lower()
    destination = input("Destination: ")
    return [shortcode, destination]


def showLinkDestination():
    shortcode = input("Shortcode: ").lower()
    return shortcode


def showLink(linkDetails):
    print("https://" + ROOT_DOMAIN + "/" + linkDetails[0] + " => " + linkDetails[1])


def editLink(links):
    print(links)
    link = input("link to edit: ").lower()
    newDestination = input("new destination: ")
    return [link, newDestination]


def delLink(links):
    print(links)
    link = input("link to del: ").lower()
    confirmLink = input(f"type {link} to confirm: ").lower()
    if link == confirmLink:
        return [link, ""]
    error(3)
    return None


def error(errorcode):
    if errorcode == SHORTCODE_IN_USE:
        print("Shortcode already in use!")
    elif errorcode == LINK_NOT_FOUND:
        print("Link not found!")
    elif errorcode == DEL_ABORT:
        print("del abort")
    elif errorcode == MISSING_ARGUMENT:
        print("missing argument")
    elif errorcode == INVALID_LINK:
        print("invalid link")
