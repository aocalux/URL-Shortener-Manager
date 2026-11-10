import readFolder as readF
import ui as ui
import MAGIC_NUMBERS as MAGIC_NUMBERS
import ALLOWED_CHARS as ALLOWED_CHARS
import options as options

ALLOWED = ALLOWED_CHARS.get()


def loop(folder_path):
    links = readF.getLinks(folder_path)
    option = ui.options()

    match option:
        case MAGIC_NUMBERS.NEW_LINK:
            options.new_link(links, folder_path)

        case MAGIC_NUMBERS.EDIT_DESTINATION:
            options.edit_destination(links, folder_path)

        case MAGIC_NUMBERS.DEL_LINK:
            options.del_link(links, folder_path)

        case MAGIC_NUMBERS.EDIT_SHORTCODE:
            options.edit_shortcode(links, folder_path)

        case MAGIC_NUMBERS.SHOW_LINKS_AND_DESTINATION:
            options.show_links_and_destination(links, folder_path)

        case MAGIC_NUMBERS.SHOW_LINK_DESTINATION:
            options.show_link_destination(links, folder_path)

