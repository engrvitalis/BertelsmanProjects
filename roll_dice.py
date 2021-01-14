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
    return sum(dice_1 + dice_2)