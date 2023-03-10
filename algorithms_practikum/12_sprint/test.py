import sys


def main():
    print(sys._getframe().f_code.co_name)
    
a = main()

