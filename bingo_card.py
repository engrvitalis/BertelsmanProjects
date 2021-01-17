def bingo_card():
    """
    This funtion generates and return dictionary as 
    Bingo card.

    @param: None
    @return: dictionary.
    """

    import random

    # Declare variables.
    char = ['B', 'I', 'N', 'G', 'O']
    card = dict()
    start = 1
    stop = 15

    # Populate card with key-value pair.
    for c in char:
        card[c] = random.sample(range(start, stop), 5)
        start += 15
        stop += 15

    # Return Bingo card as a dictionary.
    return card


def disp(card):
    """
    This function takes card, a dictionary as argument 
    and prints it as a bingo card.

    @param: dictionary
    @return: None
    """

    # Declare variables.
    card = bingo_card()
    i = 0

    # Print the card headers.
    for key in card.keys():
        print(key, end='\t')
    print('\n----------------------------------')

    # Print the card body.
    for j in range(len(card)):
        for key in card.keys():
            print(card[key][i], end='\t')
        i += 1
        print()


def main():
    # Create and display Bingo card.
    disp(bingo_card())



if __name__ == "__main__":
    main()
