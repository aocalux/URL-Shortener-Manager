import random as random

import link as link
import readFolder as readF
import ui as ui
from MAGIC_NUMBERS import *
from loop import ALLOWED


def new_link(links, folder_path):
    link_details = ui.newLink()
    if not link.check_link_details(link_details):
        return
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
        return
    else:
        if link.create(link_details, folder_path) == INVALID_LINK:
            ui.error(INVALID_LINK)
        else:
            ui.showLink(link_details)


def edit_destination(links, folder_path):
    link_details = ui.editLink(links)
    if not link.check_link_details(link_details):
        return
    if link_details[0] not in links:
        ui.error(LINK_NOT_FOUND)
        return
    else:
        if link.editLink(link_details, folder_path) == INVALID_LINK:
            ui.error(INVALID_LINK)


def del_link(links, folder_path):
    link_details = ui.delLink(links)
    if not link.check_link_details(link_details):
        return
    if link_details is None:
        return
    if link_details[0] not in links:
        ui.error(LINK_NOT_FOUND)
        return
    if link.delLink(link_details, folder_path) == INVALID_LINK:
        ui.error(INVALID_LINK)


def edit_shortcode(links, folder_path):
    old_shortcode, new_shortcode = ui.editLinkShortcode(links)
    if not old_shortcode.strip():
        return
    if not new_shortcode.strip():
        return
    if new_shortcode in links:
        ui.error(SHORTCODE_IN_USE)
        return
    if old_shortcode not in links:
        ui.error(LINK_NOT_FOUND)
        return
    destination = readF.getDestination(old_shortcode, folder_path)
    if destination == INVALID_LINK:
        ui.error(INVALID_LINK)
        return
    if (
            link.editShortcode(old_shortcode, new_shortcode, destination, folder_path)
            == INVALID_LINK
    ):
        ui.error(INVALID_LINK)


def show_links_and_destination(links, folder_path):
    link_table = []
    for linkv in links:
        link_table.append([linkv, readF.getDestination(linkv, folder_path)])

    ui.showlinks(link_table)


def show_link_destination(links, folder_path):
    shortcode = ui.showLinkDestination()
    if shortcode not in links:
        ui.error(LINK_NOT_FOUND)
        return
    ui.showLink([shortcode, readF.getDestination(shortcode, folder_path)])
