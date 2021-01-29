def recurse_palindrome(word):
    """
    This program will a word as parameter and return 
    True it is a palindrome or False otherwise. It uses recursion 
    to solve this problem.

    @param: String
    @return: Boolean
    """

    # Empty string or a single character is a palindrome.
    if len(word) < 2:
        return True
    # Checking if the first and last characters are not the same.
    elif word[0] != word[-1]:
        return False
    else:
        # If the terminal characters are same, slice them off and call 
        # recurse_palindrome() on the remaining characters.
        return recurse_palindrome(word[1:len(word)-1])

def main():
    while True:
        word = input("\nEnter a word or blank line to stop: ")

        # Terminate program is blank line is entered.
        if word == "":
            print("Program Terminated.")
            break
        
        # Process only letters. Raise flag is special characters or numbers 
        # are encountered.
        if not word.isalpha():
            print("Enter characters only!")
            continue
        
        # Check if a word is a palindrome and display appropriate output.
        if recurse_palindrome(word.lower()):
            print(f"{word} is a palindrome")
        else:
            print(f"{word} is not a palindrome")



if __name__ == '__main__':
    main()
