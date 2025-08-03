"""
Word Occurrences
"""

def main():
    text = input("Text: ")
    words = text.split()
    word_to_count = {}

    for word in words:
        word = word.lower()
        word_to_count[word] = word_to_count.get(word, 0) + 1

    max_length = max(len(word) for word in word_to_count)

    for word in sorted(word_to_count):
        print(f"{word:{max_length}} : {word_to_count[word]}")


if __name__ == "__main__":
    main()
