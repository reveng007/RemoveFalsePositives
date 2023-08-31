'''
import os
import sys

try:
    with open(sys.argv[1]) as file:
        
        Lines = file.readlines()

        count = 0
        # Strips the newline character
        for line in Lines:
            count += 1
            hook = line.split(' ')

            chars = list(hook[0])

            print("unsigned char s{}[] = {{ '{}',0x0 }};".format(hook[0], "','".join(map(str, chars))))

except:
    print("\nUsage: python3 %s <text file full of False Positive Hooked Functions>\n" %sys.argv[0])
    sys.exit()
'''
import os
import sys

try:
    with open(sys.argv[1]) as file:

        Lines = file.readlines()

        count = 0
        # Strips the newline character
        for line in Lines:
            count += 1
            hook = line.split(' ')

            chars = list(hook[0])

            print("const char s{}[] = {{ '{}', 0 }};".format(hook[0], "','".join(map(str, chars))))

except:
    print("\nUsage: python3 %s <text file full of False Positive Hooked Functions>\n" %sys.argv[0])
    sys.exit()
