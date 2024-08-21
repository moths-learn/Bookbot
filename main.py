import string
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    dict_char = {}
    num_words, words = get_num_words(text)
    dict_char = get_num_characters(text)
    print(dict_char)

def get_num_words(text):
    words = text.split()
    return len(words), words()

def get_num_characters(words):
    lowered_words = words.lower()
    chars = {}
    exclude = string.punctuation + string.whitespace
    for character in lowered_words:
        if character not in exclude:
            chars[character] = chars.get(character, 0) + 1

    return chars

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()