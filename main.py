import sys
from stats import count_words, count_characters, sort_characters_dict

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def print_pretty_counts(listOfEntries):
    print("--------- Character Count -------")
    for entry in listOfEntries:
        character = entry["character"]
        count = entry["count"]
        if character.isalpha():
            print(f"{character}: {count}")
    print("============= END ===============")
    
def main():
    input = sys.argv
    if len(input) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        return
    
    pathToBook = input[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {pathToBook}...")
    contents = get_book_text(pathToBook)
    print("----------- Word Count ----------")
    word_count = count_words(contents)
    print(f"Found {word_count} total words")
    character_counts = count_characters(contents.lower())
    sorted_counts = sort_characters_dict(character_counts)
    print_pretty_counts(sorted_counts)

main()


#"character": entry, "count":