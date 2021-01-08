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

    import random

    # Initialize variable.
    control_list = [num for num in range(len(deck))]
    new_deck = []
    
    while len(control_list) != 0:
        # Generate random index
        index = random.randrange(0, len(control_list))
        # Randomly select card in deck and add to new deck.
        new_deck.append(deck[control_list[index]])
        # Remove used index from pool of index to select from to avoid duplicates.
        control_list.pop(index)


    return new_deck


def main():
    # Display deck before and after shuffle.
    print()
    print(f"Deck before shuffle:\n{createDeck()}")
    print(f"\nDeck after shuffle:\n{shuffle(createDeck())}")


if __name__ == '__main__':
    main()