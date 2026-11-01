# Shortcode witch are't allowed
DIR_BLACKLIST = [
    ".GIT",
    "STYLE",
    "404",
    "404.HTML",
    "CNAME",
    "INDEX",
    "INDEX.HTML",
    "README",
    "README.MD",
    "ROBOTS.TXT",
    "SECURITY.TXT",
]
SYS_COMMANDS = ["RAN"]
# if set to false only the internally used magic numbers will be blocked
BLACKLIST_NUMBERS_TO_99 = True

from MAGIC_NUMBERS import *


def getBlacklist():
    blist = DIR_BLACKLIST
    blist.append(" ")
    for command in SYS_COMMANDS:
        blist.append(command)
    if BLACKLIST_NUMBERS_TO_99:
        for i in range(100):
            blist.append(str(i))
    else:
        for i in range(MAX_NUMMBER):
            blist.append(str(i))

    for e in blist:
        e = e.upper()

    return blist
