#!/python3
import sys
import string
print('A programm that determines what proportion of the words use each letter of the alphabet')
# Opening the file
filename = input('Enter the filename: ')   
try:
    f = open(filename, 'r')
except Exception:
    quit()
text = f.read()
wlist = []
# Making a list that includes every word in the given file
for word in text.split():
    word = ''.join(filter(str.isalpha, word))
    # print(word)
    wlist.append(word)  
f.close()
# Making a dict that its keys are the letters of the alphabet
table = {}
for i in string.ascii_lowercase:
    table[i] = 0
# print(table)
# Removing duplicate letters from each word
for l in wlist:
    word = (l.lower()).strip()
    # print(word)
    word = ''.join(set(word))
    print(word)
    # Adding to the letter counter accordingly for every letter of a word
    for letter in word:
        table[letter] += 1
length = len(wlist)
# Printing the output
for k, v in table.items():
    v = str(round((v/length) * 100, 2)) + '%'
    print('letter ', k, ' was used ===> ', v)
# Finding the letter that was used the less
m = min(table, key=table.get)
print('The letter that was used the less is: ', m)