"""
This program reads successive input of words from the user,
collect them in a list and format them by inserting appropriate 
punctuations and conjuction between them.

@params: String - words. Separate them by hitting return after each word.
         Hit return twice to end entry.
@return: String of words formatted as per specification.
"""

def list_formatter(ls):
    # Check for the number of words keyed in by the user if any
    # and join the words with the appropriate conjunction and punctuations
    # if more than one.
    if len(ls) < 1:
        return f'No input was provided!'
    elif len(ls) == 1:
        return ls[0]
    else:
        return (', '.join(ls[:-1]) + " and " + ls[-1])

def main():
    # Initialize state variables.
    ls = list()

    # Read input from user and save in ls.
    # Terminate if blank line is entered.
    while True:
        word = input("Enter a word or enter blank to stop: ")
        if word == "":
            break
        ls.append(word)

    # Format the content of ls and display the results.
    print(list_formatter(ls))

if __name__ == "__main__":
    main()