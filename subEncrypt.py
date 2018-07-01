

import random
import string



inp = input("Press E to encrypt a file or D to decrypt a file: ")

if inp == 'E':
    file = input("Enter the name of the file to encrypt: ")

    test = open(file).read().lower()
    abc = "abcdefghijklmnopqrstuvwxyz"
    key = "cdefghijklmnopqrstuvwxyzab"
    trans = str.maketrans(abc, key)
    output = test.translate(trans)

    file = open(file,'w')
    file.write(output)

if inp == 'D':
    file = input("Enter the name of the file to decrypt: ")

    test = open(file).read().lower()
    key = "abcdefghijklmnopqrstuvwxyz"
    abc = "cdefghijklmnopqrstuvwxyzab"
    trans = str.maketrans(abc, key)
    output = test.translate(trans)

    file = open(file,'w')
    file.write(output)
