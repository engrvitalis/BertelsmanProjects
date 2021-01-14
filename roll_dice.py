def roll_dice():
    """
    This function simulates a two dice roll and returns the sum as output.

    @param: None.
    @return: Int - Sum of two dice roll.
    """

    import random


    # Roll dice.
    dice_1 = random.randrange(1, 6)
    dice_2 = random.randrange(1, 6)

    # Return the sum.
    return dice_1 + dice_2


def main():
    # Initialize variable
    results = dict()

    # Simulate dice roll and document num and frequency in results.
    for i in range(1000):
        num = roll_dice()
        results[num] = results.get(num, 0) + 1

    print(results)

if __name__ == "__main__":
    main()