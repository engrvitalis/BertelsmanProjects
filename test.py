import functools


def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")
        return value
    return wrapper_debug

######################################################################

from typing import List

@debug
def how_many_different_numbers(s: List[int]) -> int:
    """ returns the number of unique elements in list s"""
    return len(set(s))

if __name__ == "__main__":
    # testing
    how_many_different_numbers([1, 2, 4, 1, 2, 4, 5])
    print('\n')
    how_many_different_numbers([1])
    print('\n')
    how_many_different_numbers([])
    print('\n')
    how_many_different_numbers([1, 1, 1, 1, 1, 1])



# from random import randint

# def guess_num():
#     ''' guess a random number between 0 and 100. while users guess is equal to the number provide clues'''
#     num = randint(0,100)
#     while True:
#         try:
#             # get the number and check
#             guess = int(input('enter your guess: '))
#             if num > guess:
#                 print('too low')
#             elif num < guess:
#                 print('too high')
#             else:
#                 print('That is correct. You won')
#                 break
#         except Exception as e:
#             print('Did you enter a valid number? The number must be between 0 and 100')
    


# def main():
#     print("Guessing Game\nCan you guess my number?\nIt's between 0 and 100")
#     guess_num()

# if __name__ == '__main__':
#     main()


# # Find and display the names of Python functions that are not immediately preceded by a
# # comment.
# #
# from sys import argv
# # Verify that at least one file name has been provided as a command line argument
# if len(argv) == 1:
#     print("At least one filename must be provided as a", \
#         "command line argument.")
#     print("Quitting...")
#     quit()
# # Process each file provided as a command line argument
# for fname in argv[1 : len(argv)]:
#     # Attempt to process the file
#     try:
#         inf = open(fname, "r")
#         # As we move through the file we need to keep a copy of the previous line so that we
#         # can check to see if it starts with a comment character. We also need to keep track
#         # of the line number within the file.
#         prev = " "
#         lnum = 1
#         # Check each line in the current file
#         for line in inf:
#             # If the line is a function definition and the previous line is not a comment
#             if line.startswith("def ") and prev[0] != "#":
#                 # Find the first ( on the line so that we know where the function name ends
#                 bracket_pos = line.index("(")
#                 name = line[4 : bracket_pos]
#                 # Display information about the function that is missing its comment
#                 print("%s line %d: %s" % (fname, lnum, name))
#             # Save the current line and update the line counter
#             prev = line
#             lnum = lnum + 1
#         # Close the current file
#         inf.close()
#     except:
#         print("A problem was encountered with file '%s'." % fname)
#         print("Moving on to the next file...")

# import re

# O_FILE = 'words2.txt' # input('Enter original text file name: ')
# W_FILE = 'sensitive_words.txt' #input('Enter sensitive words file name: ')
# R_FILE = 'me.txt' # input('Enter redacted file name: ')

# print(O_FILE)
# #open original file
# original= open(O_FILE, "r")
# text = ''
# for line in original:
#     text += ''.join(line) 
# original.close()

# #list of sensitive words
# with open(W_FILE) as f:
#     sensitive_words = [line.rstrip('\n') for line in f]

# #create a new file
# redacted = open(R_FILE, 'w')

# #working with regex in order to replace sensitive word (insensitive manner with IGNORECASE)
# for word in sensitive_words:
#     text = re.sub(word, '*'*len(word), text, flags=re.IGNORECASE)
    
# redacted.write(text)
# redacted.close()



# import os
# import glob
# import pandas as pd


# def get_merged_csv(flist, **kwargs):
#     return pd.concat([pd.read_csv(f, **kwargs) for f in flist], ignore_index=True)

# path = "./BabyNames"

# # find by names (boys/girls) and merge
# fmask = os.path.join(path, '*_GirlsNames.txt')
# df_merge_g = get_merged_csv(glob.glob(fmask), index_col=None,  sep=" ", header=None)

# # print(df_merge_g)

# df_merge_g.columns = ["name", "count"]



# fmask = os.path.join(path, '*_BoysNames.txt')
# df_merge_b = get_merged_csv(glob.glob(fmask), index_col=None,  sep=" ", header=None)
# df_merge_b.columns = ["name", "count"]

# #group by names and sum
# final_result_girls = df_merge_g.groupby(['name'],as_index=False)['count'].sum()
# final_result_boys = df_merge_b.groupby(['name'],as_index=False)['count'].sum()

# # top 5 popular names
# print('POPULAR NAMES GIRLS')
# print(final_result_girls.sort_values(by=['count'], ascending=False).head().to_string(index=False))
# print()
# print('POPULAR NAMES BOYS')
# print(final_result_boys.sort_values(by=['count'], ascending=False).head().to_string(index=False))


# #!/python3
# import sys
# import string
# print('A programm that determines what proportion of the words use each letter of the alphabet')
# # Opening the file
# filename = input('Enter the filename: ')   
# try:
#     f = open(filename, 'r')
# except Exception:
#     quit()
# text = f.read()
# wlist = []
# # Making a list that includes every word in the given file
# for word in text.split():
#     word = ''.join(filter(str.isalpha, word))
#     # print(word)
#     wlist.append(word)  
# f.close()
# # Making a dict that its keys are the letters of the alphabet
# table = {}
# for i in string.ascii_lowercase:
#     table[i] = 0
# # print(table)
# # Removing duplicate letters from each word
# for l in wlist:
#     word = (l.lower()).strip()
#     # print(word)
#     word = ''.join(set(word))
#     print(word)
#     # Adding to the letter counter accordingly for every letter of a word
#     for letter in word:
#         table[letter] += 1
# length = len(wlist)
# # Printing the output
# for k, v in table.items():
#     v = str(round((v/length) * 100, 2)) + '%'
#     print('letter ', k, ' was used ===> ', v)
# # Finding the letter that was used the less
# m = min(table, key=table.get)
# print('The letter that was used the less is: ', m)


# # The baby names data set consists of over 200 files (data sets are attached to this message). Each file contains a
# # list of 100 names, along with the number of times each name was used. Entries in the files are ordered from most
# # frequently used to least frequently used. There are two files for each year: one containing names used for girls
# # and the other containing names used for boys. The data set includes data for every year from 1900 to 2012.
# # Write a program that reads every file in the data set and identifies all of the names that were most popular in at
# # least one year. Your program should output two lists: one containing the most popular names for boys and the other
# # containing the most popular names for girls. Neither of your lists should include any repeated values.

# from os import scandir


# def baby_names():
#     try:
#         files = scandir('BabyNames')
#         b_names = []
#         g_names = []
#         for file in files:
#             with open(file, 'r') as f:
#                 name = f.readline().split()
#                 if f.name.count("Boys") > 0:
#                     b_names.append(name[0])
#                 else:
#                     g_names.append(name[0])
#         print(f"The most popular names for for boys from 1900 to 2012 are: {list(set(b_names))}")
#         print(f"The most popular names for for girls from 1900 to 2012 are: {list(set(g_names))}")
#     except FileNotFoundError:
#         print("Path specified cannot be found")
#     except IOError:
#         print("File not found")


# if __name__ == '__main__':
#     baby_names()




