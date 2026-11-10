import ui as ui

import loops as loop
import threading
import webserver as web
from MAGIC_NUMBERS import WEB_SERVER_PORT

PORT = WEB_SERVER_PORT


def main():
    ui.startup()
    # folderPath = ui.getFolderPath()
    folder_path = "/Users/pri/Documents/GitHub/go.juliapri.pink/"
    # run_server_noblock(folder_path)

    while True:
        loop.loop(folder_path)


def run_server_noblock(folder_path):
    server_thread = threading.Thread(
        target=web.run_server,
        args=(
            PORT,
            folder_path,
        ),
        daemon=True,
    )
    server_thread.start()


if __name__ == "__main__":
    main()
