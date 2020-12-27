"""
This function capitalizes the appropriate characters in a string based on some specifications.

Input: String
Output: String
"""

def capitalize_it(string):
    # Declare state variables.
    special_char = ['.', ',', '!', '?']
    result = []

    # Convert string to list.
    result_list = string.split()
    # Capitalize the first word.
    result.append(result_list[0].capitalize())
    
    # Move through the rest of the list and capitalize as per specification.
    for elem in result_list[1:]:
        if result[-1][-1] in special_char:
            result.append(elem.capitalize()) # Capitalize words followed by special character.
        elif elem == 'i':
            result.append(elem.capitalize()) # Capitalize 'i' surrounded by spaces.
        else:
            result.append(elem)
    
    return ' '.join([str(elem) for elem in result]) # Convert back to string and return.

if __name__ == "__main__":
    # Request user input.
    string = input('Enter your sentence or phrase: ')

    # Call Capitalize_it function and display the result.
    print(capitalize_it(string))