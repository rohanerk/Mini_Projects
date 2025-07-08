#! python3
# mapIt.py - Launches a map in the browser using an address from the command line or clipboard

import webbrowser,sys,pyperclip

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:]) # sys.argv variable stores a list of program's file name and command line arguments
                                     # if the list has more than 1, that means len(sys.argv) > 1
                                     # Command line arguments are separated by spaces, but for the URL, we want it as a single string. So pass it to a join() method which returns a single value
                                     # To remove the program name from the string, sys.argv[1:] is used

# TODO : Get address from clipboard

else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
