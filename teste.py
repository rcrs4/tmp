import os
import sys

if len(sys.argv) < 3:
    print("Must have 2 arguments, Username Wordlist Path and Password Wordlist Path")
else:
    os.system(f"ffuf -w {sys.argv[1]}:FUZZ -w {sys.argv[2]}:ME -X POST -d \"username=FUZZ&pass=ME\" -fc 401 -o loginBrute.txt -t 3 -p 0.05 -u https://")
    output = open('loginBrute.txt')
    dictOutput = dict(output)
    print("Valid Usernames, Valid Passwords")
    print(dictOutput)