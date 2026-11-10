import ui as ui

import loops as loop


def main():
    ui.startup()
    # folderPath = ui.getFolderPath()
    folder_path = "/Users/pri/Documents/GitHub/go.juliapri.pink/"

    while True:
        loop.loop(folder_path)


if __name__ == "__main__":
    main()
