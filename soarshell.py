"""
This is the very first version of the SoarPro Shell.
It takes input from the user and then returns the appropriate 
result to the user.
"""

####################################################
#################### Import ########################
####################################################
from run import *

####################################################
#################### Shell #########################
####################################################

print("Welcome to XLang Version 1.0.0")
print("For more informations type 'help', 'about' or 'leave' to exit this shell")

while True:
    text = input(">> ")

    # This happens whenever the user inputs "help" without the quotef
    if text == "help":
        help = """
Welcome to the Xlang shell!
If you are new to using Xlang you can checkout the tutorial
on github at https://github.com.ng/XBid/XLang.

This shell is meant to be used for testing purposes only. If you
need to use it for more complex stuff check out the compiler! 
        """
        print(help)
    
    # This happens when the user inputs "about without quotes"
    elif text == "about":
        about = """
XLang is a compiled, high level and general purpose programming
language. The first intention of building this programming language
was to learn how it is been built we at XBid hopes some day it meets
production standard!!
        """
        print(about)

    # This happens when the user inputs "leave" it also stops the shell from running
    elif text == "leave":
        print("Thanks for using XLang... Have a nice day!")
        break

    # This happens if the user inputs a normal code. e.g: x = 32;
    else:
        result, error = run(text)

        if error:
            print(error.as_string())
        else:
            print(result)
