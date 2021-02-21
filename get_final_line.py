def get_final_line(file):


    """
    Takes file name as input and returns the last 
    line in the file.

    @param: str - file
    @return: str
    """

    with open(file) as f:
        # Initialize variable.
        last_line = None

        # Go through the lines in file and assign each to last_line.
        for line in f:
            last_line = line

    # Return the last encountered line.
    return last_line

def main():
    # This function is to be called from the command line.
    import sys

    try:
        file = sys.argv[1]
        print(get_final_line(file))
    except:
        print("Provide a valid file name!")


main()