import os

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def gettime():
    """Returns the current time."""
    import time
    return time.ctime()
