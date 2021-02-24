import os

def find_all_longest_words(files):
    pass


def find_longest_word(file):
    longest_word = []
    with open(file, encoding="utf8") as f:
        for line in f:
            for word in line.split():
                if not word.startswith('http'):
                    word = clean_word(word)
                    if '-' in word or not word.isdigit():
                        print(word)
                    # print(word)
                    # if longest_word == []:
                    #     longest_word.append(word)
                    #     longest_word.append(len(word))
                    # elif longest_word[1] < len(word.strip()):
                    #     longest_word[0], longest_word[1] = word, len(word)
    return longest_word


def clean_word(word):
    word = word.strip('. :,-$?!;*&^%#@`~=_\"\'').lower()
    if '@' in word and len(word[:word.index('@')]) > 1:
        word = word.split('@')[0]

    return word

def main():
    files = [os.path.join('Books', file) for file in os.listdir('Books')]
    file = files[0]
    print(find_longest_word(file))

if __name__ == '__main__':
    main()