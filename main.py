import readFolder as readF
import ui as ui
import link as link
import random as random
import ALLOWED_CHARS as allowedChars

from MAGIC_NUMBERS import *

ALLOWED = allowedChars.get()

def main():
    ui.startup()
    # folderPath = ui.getFolderPath()
    folderPath = "/Users/pri/Documents/Code/go.juliapri.pink/"
    

    while True:
        links = readF.getLinks(folderPath)
        option = ui.options()
        if option == NEW_LINK:
            linkDetails = ui.newLink()
            if not checkLinkDetails(linkDetails): continue
            if linkDetails[0] == RANDOM_LINK:
                linkLen = RANDOM_LINK_LEN
                if RANDOM_LINK_LEN_VARIATION > 0:
                    if random.randint(0, 1) == 1:
                        linkLen = RANDOM_LINK_LEN + random.randint(0, RANDOM_LINK_LEN_VARIATION)
                    else:
                        linkLen = RANDOM_LINK_LEN - random.randint(0, RANDOM_LINK_LEN_VARIATION)
                ran_string = "".join(random.choices(ALLOWED, k=linkLen)).lower()
                while (link.checkBlacklist(ran_string) == INVALID_LINK):
                    ran_string = "".join(random.choices(ALLOWED, k=linkLen)).lower()
                while (ran_string in links):
                    ran_string = "".join(random.choices(ALLOWED, k=linkLen)).lower()
                linkDetails[0] = ran_string
            if linkDetails[0] in links:
                ui.error(SHORTCODE_IN_USE)
                continue
            else:
                if link.create(linkDetails, folderPath) == INVALID_LINK: ui.error(INVALID_LINK)
                else: ui.showLink(linkDetails)
        elif option == EDIT_DESTINATION:
            linkDetails = ui.editLink(links)
            if not checkLinkDetails(linkDetails): continue
            if linkDetails[0] not in links:
                ui.error(LINK_NOT_FOUND)
                continue
            else:
                if link.editLink(linkDetails, folderPath) == INVALID_LINK: ui.error(INVALID_LINK)
        elif option == DEL_LINK: 
            linkDetails = ui.delLink(links)
            if not checkLinkDetails(linkDetails): continue
            if linkDetails is None: continue
            if linkDetails[0] not in links:
                ui.error(LINK_NOT_FOUND)
                continue
            if link.delLink(linkDetails, folderPath) == INVALID_LINK: ui.error(INVALID_LINK)
        elif option == EDIT_SHORTCODE:
            oldShortcode, newShortcode = ui.editLinkShortcode(links)
            if not oldShortcode.strip(): continue
            if not newShortcode.strip(): continue
            if newShortcode in links: 
                ui.error(SHORTCODE_IN_USE)
                continue
            if oldShortcode not in links:
                ui.error(LINK_NOT_FOUND)
                continue
            destination = readF.getDestination(oldShortcode, folderPath)
            if destination == INVALID_LINK: 
                ui.error(INVALID_LINK)
                continue
            if link.editShortcode(oldShortcode, newShortcode, destination, folderPath) == INVALID_LINK: ui.error(INVALID_LINK)
        elif option == SHOW_LINKS_AND_DESTINATION:
            linkTable = []
            for linkv in links:
                linkTable.append([linkv, readF.getDestination(linkv, folderPath)])

            ui.showlinks(linkTable)
        elif option == SHOW_LINK_DESTINATION:
            shortcode = ui.showLinkDestination()
            if shortcode not in links:
                ui.error(LINK_NOT_FOUND)
                continue
            ui.showLink([shortcode, readF.getDestination(shortcode, folderPath)])



def checkLinkDetails(linkDetails):
    if linkDetails[0].strip():
        return True
    return False


if __name__ == "__main__":
    main()