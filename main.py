import string


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    dict_char = get_char_amount(text)
    sorted_char = sorted(dict_char.items(), key=lambda item: item[1], reverse=True)

    print(f"Numbers of words: {num_words}")
    print("character amount:")
    for char, freq in sorted_char:
        print(f"The {char} character was found {freq} times")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_char_amount(text):
    lowered_text = text.lower()
    chars = {}
    exclude = string.punctuation + string.whitespace
    for character in lowered_text:
        if character not in exclude:
            chars[character] = chars.get(character, 0) + 1
    #        chars[character] = chars.get(character, 0) + 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
