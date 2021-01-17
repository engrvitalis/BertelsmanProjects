def bingo_card():
    """
    This funtion generates and return dictionary as 
    Bingo card.

    @param: None
    @return: dictionary.
    """


    import random


    char = ['B', 'I', 'N', 'G', 'O']
    card = dict()
    start = 1
    stop = 15

    for c in char:
        card[c] = random.sample(range(start, stop), 5)
        start += 15
        stop += 15

    return card


def main():
    card = bingo_card()
    i = 0

    for key in card.keys():
        print(key, end='\t')
    print()

    for j in range(len(card)):
        for key in card.keys():
            print(card[key][i], end='\t')
        i += 1
        print()



if __name__ == "__main__":
    main()
