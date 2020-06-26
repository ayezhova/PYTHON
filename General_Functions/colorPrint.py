class Colors:
    BLACK = '\033[30m'
    DARK_GREY = '\033[90m'
    LIGHT_GREY = '\033[37m'
    BLUE = '\033[34m'
    LIGHT_BLUE = '\033[94m'
    CYAN = '\033[36m'
    LIGHT_CYAN = '\033[96m'
    GREEN = '\033[32m'
    LIGHT_GREEN = '\033[92m'
    PURPLE = '\033[35m'
    RED = '\033[31m'
    LIGHT_RED = '\033[91m'
    PINK = '\033[95m'
    ORANGE = '\033[33m'
    YELLOW = '\033[93m'


def colorPrint(printStr = '', color = Colors.BLACK):
    RESET = '\033[00m'
    print(color, printStr, RESET)


def colorString(printStr = '', color = Colors.BLACK):
    RESET = '\033[00m'
    return color + str(printStr) + RESET
