import sys
from collections import defaultdict


def main():
    word_positions = defaultdict(lambda: None)

    words_list = []

    for line in sys.stdin:
        for index, word in enumerate(line.split()):
            words_list.append(word)
            if word_positions[word] is None:
                word_positions[word] = len(words_list) - 1

    capital_words = [(word_positions[word], word) for word in word_positions if word[0].isupper()]

    capital_words_sorted = sorted(capital_words, key=lambda x: x[1])

    for pos, word in capital_words_sorted:
        print(f"{pos} - {word}")


if __name__ == "__main__":
    main()
