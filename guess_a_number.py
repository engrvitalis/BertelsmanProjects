def guess_a_number():
    """
    This program generates a secret number and request the 
    user to guess the correct number through series of input
    request.
    It will provide feedback to the user if the guess is higher,
    lower or same as the secret number. It will terminate if the 
    user correctly guesses the secret number.

    @param: Integer
    @return: None
    """

    import random

    # Generate a secret number.
    secret_number = random.randint(0, 100)

    print(f'\nI have chosen a number. Can you guess what it is?')
    while True:
        # Request guess from user and provide feedback.
        num = input("Enter your guess here: ")
        if num != "":
            num = int(num)
            if num < secret_number:
                print('Too low!')
            elif num > secret_number:
                print('Too high!')
            else:
                print('Just right!')
                break


def main():
    # Start guess a number game.
    guess_a_number()


if __name__ == '__main__':
    main()