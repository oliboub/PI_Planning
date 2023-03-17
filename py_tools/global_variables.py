import os

def init():
    global DEBUG_OL
    DEBUG_OL=1

    # DEBUG_OL
    # 0 means no print
    # 1 means print call to function only
    # 2 means print all

    
    global FONT
    FONT='Helvetica 11'
    
    global THEME
    THEME = 'LightBlue2'
    
print(os.getcwd(),__name__,'imported')