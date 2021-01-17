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


def disp(card):
    


print(bingo_card())
