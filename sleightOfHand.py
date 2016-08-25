# sleightOfHand.py
#
# Copyright 2016 Stefan Reich
#
# Licensed under the MIT license

import random
import os
import re

while True:
    try:
        print("Enter end password length:")
        passwordLength = int(input())
        if (passwordLength > 0):
            break
    except:
        print("Number not entered")

# Since autohotkey input hotstrings can only be up to 40 characters max, we need to
# restrict how many characters the string to be replaced can be. Also, some characters
# could potentially break the outputted script, so we need to check that those are not
# used either.

excludedCharacters = '[:\'\"\{\[\(\)\]\}<>.,=`%]'
while True:
    print("Enter starting string between 1 and 40 characters long:")
    inputString = input()
    if (len(inputString) <=40) and (len(inputString) >= 1) and not (re.search(excludedCharacters, inputString)):
        break

# We'll simply put the outputted script in the same directory as this file.
currentDirectory = os.getcwd()
outFile = open( currentDirectory + '/password_replacement.ahk', 'w')

# SetKeyDelay sets the delay between "output" keystrokes. We'll set it as low as possible.
outFile.write("SetKeyDelay, 0\n")

# This sets up the user's inputted string to be replaced as soon as it is typed in.
outFile.write(":*:" + inputString + "::\n")

# Set of characters to be randomly selected. Did not include some special characters
# as some could potentially break the outputted script, and others could potentially
# help to trigger some sort of unintended SQL injection
characterList = ['!','#','$','&','*','+','-','/','2','3','4','5','6','7','8','9','?','@',
'A','B','C','D','E','F','G','H','J','K','L','M','N','O','P','R','S','T','U','V','W','X',
'Y','Z','^','_','a','b','c','d','e','f','g','h','i','j','k','m','n','o','p','q','r','s',
't','u','v','w','x','y','z','|','~']

# The next section is an emulated do-while loop that checks to see if the output string
# isn't somehow the same as the input string, which would cause an infinite loop if it was
outputString = ''
while True:
    for j in range(passwordLength):
        outputString += random.choice(characterList)
    if outputString != inputString:
        break

outFile.write("SendRaw, " + outputString + "\n")

# This will close the script once run, so you can use your input string again without
# being replaced by your password by accident.
outFile.write("ExitApp\n")
outFile.write("return\n")

outFile.close()