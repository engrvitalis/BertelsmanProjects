"""
Project: Palindrome
Description: This program returns True or False depending whether a word or phrase is palindromic or not.

Input: String
Output: String
"""

string = input("Enter a word or phrase: ")
string_copy = string[:]
string = string.lower().strip(' ')
rev_ind = -1
flag = True

for ind in range(0, len(string)//2):
    if string[ind] != string[rev_ind]:
        flag = False
    rev_ind -= 1

if flag:
    print(f'The string "{string_copy}" is a Palindrome')
else:
    print(f'The string "{string_copy}" is not a Palindrome')