def bingo_card():
    """
    This funtion generates and return dictionary as 
    Bingo card.

    @param: None
    @return: dictionary - Bingo card.
    """


    import random


    char = ['B', 'I', 'N', 'G', 'O']
    card = {}
    start = 1
    stop = 15

    for c in char:
        card[c] = random.sample(range(start, stop), 5)
        start += 15
        stop += 15

    return card


print(bingo_card())
