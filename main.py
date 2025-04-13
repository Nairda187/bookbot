import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1) 
file_path = sys.argv[1]
contents = get_book_text(file_path)



def main():
    from stats import count_words
    from stats import count_characters
    from stats import sort_characters

   
    contents = get_book_text(file_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    
    # Word count section
    word_count = count_words(contents)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    
    # Character count section
    char_counts = count_characters(contents)
    sorted_chars = sort_characters(char_counts)
    
    print("--------- Character Count -------")
    # Print each character and its count, but only if it's alphabetical
    for char_dict in sorted_chars:
        char = char_dict["character"]
        if char.isalpha():  # Only print alphabetical characters
            count = char_dict["count"]
            print(f"{char}: {count}")
    
    print("============= END ===============")

main()