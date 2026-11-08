import readFolder as readF
import ui as ui
import link as link
import random as random
import ALLOWED_CHARS as ALLOWED_CHARS

from MAGIC_NUMBERS import *

ALLOWED = ALLOWED_CHARS.get()


def main():
    ui.startup()
    # folderPath = ui.getFolderPath()
    folder_path = "/Users/pri/Documents/Code/go.juliapri.pink/"

    while True:
        links = readF.getLinks(folder_path)
        option = ui.options()
        if option == NEW_LINK:
            link_details = ui.newLink()
            if not check_link_details(link_details):
                continue
            if link_details[0] == RANDOM_LINK:
                link_len = RANDOM_LINK_LEN
                allowed_auto = ALLOWED
                for char in "-_ÄÖÜ":
                    allowed_auto = allowed_auto.replace(char, "")
                if RANDOM_LINK_LEN_VARIATION > 0:
                    if random.randint(0, 1) == 1:
                        link_len = RANDOM_LINK_LEN + random.randint(
                            0, RANDOM_LINK_LEN_VARIATION
                        )
                    else:
                        link_len = RANDOM_LINK_LEN - random.randint(
                            0, RANDOM_LINK_LEN_VARIATION
                        )
                ran_string = "".join(random.choices(allowed_auto, k=link_len)).lower()
                while link.checkBlacklist(ran_string) == INVALID_LINK:
                    ran_string = "".join(random.choices(allowed_auto, k=link_len)).lower()
                while ran_string in links:
                    ran_string = "".join(random.choices(allowed_auto, k=link_len)).lower()
                link_details[0] = ran_string
            if link_details[0] in links:
                ui.error(SHORTCODE_IN_USE)
                continue
            else:
                if link.create(link_details, folder_path) == INVALID_LINK:
                    ui.error(INVALID_LINK)
                else:
                    ui.showLink(link_details)
        elif option == EDIT_DESTINATION:
            link_details = ui.editLink(links)
            if not check_link_details(link_details):
                continue
            if link_details[0] not in links:
                ui.error(LINK_NOT_FOUND)
                continue
            else:
                if link.editLink(link_details, folder_path) == INVALID_LINK:
                    ui.error(INVALID_LINK)
        elif option == DEL_LINK:
            link_details = ui.delLink(links)
            if not check_link_details(link_details):
                continue
            if link_details is None:
                continue
            if link_details[0] not in links:
                ui.error(LINK_NOT_FOUND)
                continue
            if link.delLink(link_details, folder_path) == INVALID_LINK:
                ui.error(INVALID_LINK)
        elif option == EDIT_SHORTCODE:
            old_shortcode, new_shortcode = ui.editLinkShortcode(links)
            if not old_shortcode.strip():
                continue
            if not new_shortcode.strip():
                continue
            if new_shortcode in links:
                ui.error(SHORTCODE_IN_USE)
                continue
            if old_shortcode not in links:
                ui.error(LINK_NOT_FOUND)
                continue
            destination = readF.getDestination(old_shortcode, folder_path)
            if destination == INVALID_LINK:
                ui.error(INVALID_LINK)
                continue
            if (
                link.editShortcode(old_shortcode, new_shortcode, destination, folder_path)
                == INVALID_LINK
            ):
                ui.error(INVALID_LINK)
        elif option == SHOW_LINKS_AND_DESTINATION:
            link_table = []
            for linkv in links:
                link_table.append([linkv, readF.getDestination(linkv, folder_path)])

            ui.showlinks(link_table)
        elif option == SHOW_LINK_DESTINATION:
            shortcode = ui.showLinkDestination()
            if shortcode not in links:
                ui.error(LINK_NOT_FOUND)
                continue
            ui.showLink([shortcode, readF.getDestination(shortcode, folder_path)])


def check_link_details(link_details):
    if link_details[0].strip():
        return True
    return False


if __name__ == "__main__":
    main()
