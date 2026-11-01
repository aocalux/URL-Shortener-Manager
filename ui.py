def startup():
    print("Hi!")


def getFolderPath():
    return input("URL-Shortener root: ")


def options():
    print("1 - New Link")
    return int(input("Select an Option: "))


def newLink():
    shortcode = input("Shortcode: ")
    destination = input("Destination: ")
    return [shortcode, destination]


def error(errorcode):
    if errorcode == 1:
        print("Shortcode already in use!")