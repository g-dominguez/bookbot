import sys
from stats import get_book_text, get_char_count, sort_characters

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    total_words = get_book_text(path)
    print(f"Found {total_words} total words")

    print("--------- Character Count -------")
    char_dict = get_char_count(path)
    sort_characters(char_dict)

    print("============= END ===============")


main()