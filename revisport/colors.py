# code from https://www.geeksforgeeks.org/print-colors-python-terminal/
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk),end='')
def inpYellow(skk): print("\x1b[93m{}" .format(skk))
def prWhite(skk): print("\033[00m {}\033[00m" .format(skk))
 
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
 
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))