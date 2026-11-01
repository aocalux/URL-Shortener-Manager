ALLOW_LETTERS = True
ALLOW_NUMBERS = True
ALLOW_DASH = True
ALLOW_UNDERSCORE = True
ALLOW_SPACES = False
ALLOW_UMLAUTS = False


def get():
    allowed = ""
    if ALLOW_LETTERS:
        allowed += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if ALLOW_NUMBERS:
        allowed += "1234567890"
    if ALLOW_DASH:
        allowed += "-"
    if ALLOW_UNDERSCORE:
        allowed += "_"
    if ALLOW_SPACES:
        allowed += " "
    if ALLOW_UMLAUTS:
        allowed += "ÄÖÜ"
    print(allowed)
    return allowed
