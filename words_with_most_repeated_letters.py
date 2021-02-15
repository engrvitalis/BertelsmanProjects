def most_repeating_letter_count(word):
    from collections import Counter
    
    return Counter(word).most_common(1)[0][1]



def most_repeating_word(words):
    return max(words,key=most_repeating_letter_count)


def main():
    words = input("Enter words: ")
    
    print(most_repeating_word(words.split()))


main()