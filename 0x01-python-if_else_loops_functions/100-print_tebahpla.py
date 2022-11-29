#!/usr/bin/python3

for index in range(0, 26):
    word = ord('z') - index
    if (index % 2 == 1):
        word = chr(word - ord('Y') + ord('z'))
    else:
        word = chr(word)
    print("{}".format(word), end='')
