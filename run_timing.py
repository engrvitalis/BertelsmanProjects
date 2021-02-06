def run_timer():
    """
    This function will constantly prompt the user to provide 
    the time it took for the user to complete each 10 km in a race 
    until the end of the race. It will then return the average
    time it took to complete the whole race.
    
    @param: int or float
    @return: float
    """

    # Initialize variables
    total = 0
    count = 0

    while True:
        one_run = input("Enter 10 km run time: ")
        # Stop if blank line is entered.
        if not one_run:
            break
        else:
            # Catch non numeric entry by user.
            try:
                total += float(one_run) # Update total.
            except ValueError:
                print("\nInvalid Entry. It must be int or float or blank line to terminate!\n")
                continue
            count += 1  # Update entry count.
    
    return total, count
    

def main():
    # Start timer
    total, count = run_timer()
    # Catch error generated when the ended the program without any input.
    try:
        print(f'\nAverage of {round(total/count, 1)}, over {count} runs')
    except ZeroDivisionError:
        quit()


if __name__ == '__main__':
    main()