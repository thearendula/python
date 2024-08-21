'''

Implement a function that takes a string that consists of lowercase letters and digits and
returns a string that consists of all digits and lowercase English letters that are not present in the string.
The digits should come first, in ascending order, followed by characters, also in ascending order.

Example :

s= "7985interdisciplinary12"

returned string - "0346bfghjkmoquvwxz"

'''


def missingCharacters(s):

    l = []
    newL = []
    revString = ''

    defaultString = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                     'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ]
    s = s.lower()

    for i in s:
        l.append(i)

    for i in defaultString:
        if i not in l:
            newL.append(i)

    #print(newL)

    for i in newL:
        revString = revString.__add__(i)

    return revString


print(missingCharacters("0346bfghjkmoquvwxz"))
