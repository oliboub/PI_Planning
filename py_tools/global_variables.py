import os

def init():
    global DEBUG_OL
    DEBUG_OL=2

    # DEBUG_OL
    # 0 means no print
    # 1 means print call to function only
    # 2 means print all
    # -1 Special cases

    
    global FONT
    FONT='Helvetica 11'
    
    global THEME
    THEME = 'LightBlue2'
    
    global linespage # lines by pages when display lists
    linespage = 5
    
print(os.getcwd(),__name__,'imported')