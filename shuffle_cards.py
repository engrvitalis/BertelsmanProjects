def createDeck():
    """
    This function generates a whole deck of cards.

    @param: None
    @return: A list of 52 cards represented by their abbreviations.
    eg. Ten of diamonds: Td, Jack of spades: Js etc.
    """

    # Initializing state variables.
    card_value_1 = [str(num) for num in range(2, 10)]
    card_value_2 = ['T', 'J', 'Q', 'K', 'A']
    card_suit = {'spade': 's', 'hearts': 'h', 'diamonds': 'd', 'clubs': 'c'}

    # Generate a complete list of card values.
    card_value = card_value_1 + card_value_2

    # Generate a complete deck of cards by concatenating the values and the suits appropriately.
    deck = [(j + card_suit[i]) for i in card_suit.keys() for j in card_value]

    return deck


def shuffle(deck):
    """This program will randomly shuffle the positions of the cards in the deck.
    
    @params: List - Original deck of cards.
    @return: List - Shuffled deck of cards.
    """


def main():
    print(createDeck())


if __name__ == '__main__':
    main()