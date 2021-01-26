def redact_text(file, new_file, sensitive_file):


    # Initialize variable.
    sensitive_list = list()

    # Process sensitive words into a list, ls
    with open(sensitive_file) as f:
        for line in f:
            for word in line.split():
                sensitive_list.append(word.strip())

    print(sensitive_list)
                


def main():
    file = 'words2.txt'
    new_file = 'words3.txt'
    sensitive_words = 'sensitive_words.txt'

    redact_text(file, new_file, sensitive_words)




if __name__ == '__main__':
    main()
    