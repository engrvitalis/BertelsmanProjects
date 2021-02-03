def guess_a_number():
    """
    This program

    import random


    secret_number = random.randint(0, 101)

    print(f'\nI have chosen a number. Can you guess what it is?')
    while True:
        num = int(input("Enter your guess here: "))
        if num < secret_number:
            print('Too low!')
        elif num > secret_number:
            print('Too high!')
        else:
            print('Just right!')
            break


def main():
    guess_a_number()


if __name__ == '__main__':
    main()