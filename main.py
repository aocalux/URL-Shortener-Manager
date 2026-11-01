import readFolder as readF
import ui as ui
import link as link

def main():
    ui.startup()
    # folderPath = ui.getFolderPath()
    folderPath = "/Users/pri/Documents/Code/go.juliapri.pink"
    links = readF.getLinks(folderPath)

    print(links)

    option = ui.options()
    if option == 1:
        linkDetails = ui.newLink()
        if linkDetails[0] in links:
            ui.error(1)
        else:
            if link.create(linkDetails, folderPath) == 0: print("link created")


if __name__ == "__main__":
    main()