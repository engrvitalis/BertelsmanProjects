def createDeck():
    """
    This function generates a whole deck of cards.

    @param: None
    @return: A list of 52 cards represented by their abbreviations.
    eg. Ten of diamonds: Td, Jack of spades: Js etc.
    """

    # Initializing state variables.
    card_value_1 = [num for num in range(2, 10)]
    card_value_2 = ['T', 'J', 'Q', 'K', 'A']

    card_value = card_value_1 + card_value_2


    return card_value


def shuffle(deck):
    pass


def main():
    print(createDeck())


if __name__ == '__main__':
    main()