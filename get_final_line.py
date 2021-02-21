def get_final_line(file):
    import sys


    """
    Takes file name as input and returns the last 
    line in the file.

    @param: str - file
    @return: str
    """

    with open(file) as f:
        last_line = None

        for line in f:
            last_line = line

    return last_line

import sys
file = sys.argv[1]

# Display the last line the file.
print(get_final_line(file))
