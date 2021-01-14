def roll_dice():
    """
    This function simulates a two dice roll and returns the sum as output.

    @param: None.
    @return: Int - Sum of two dice roll.
    """

    import random


    # Roll dice.
    dice_1 = random.randrange(1, 7)
    dice_2 = random.randrange(1, 7)
    print(dice_1, dice_2)
    
    # Return the sum.
    return dice_1 + dice_2


def main():
    # Initialize variable
    results = dict()
    num_roll = 1000
    p_table = [0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]

    # Simulate dice roll and document num and frequency in results.
    for i in range(num_roll):
        num = roll_dice()
        if num in results.keys():
            results[num][0] += 1
        else:
            results[num] = [0, 0, 0]
            results[num][0] += 1
    print(results)
    # Calculate the simulated percentage and insert in results.
    for key, value in results.items():
        results[key][1] = round((value[0] / num_roll) * 100, 2)
        results[key][2] = round((p_table[int(key) - 1] / 36) * 100, 2)
    
    # Print results
    print(f'\nTotal\t\tSimulated\tExpected')
    print(f'\t\tPercent\t\tPercent')
    for key in sorted(results):
        print(f'{key}\t\t{results[key][1]}\t\t{results[key][2]}')


if __name__ == "__main__":
    main()