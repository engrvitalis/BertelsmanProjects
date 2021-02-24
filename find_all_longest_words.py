import os

def find_all_longest_words(files):
    pass


def find_longest_word(file):
    with open(file) as f:
        for line in f:
            print(line)


def main():
    files = [os.path.join('Books', file) for file in os.listdir('Books')]
    file = files[0]
    print(find_longest_word(file))

if __name__ == '__main__':
    main()