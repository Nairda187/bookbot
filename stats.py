def count_words(text):
    words = text.split()
    total_words = len(words)
    return total_words

def count_characters(text):
        counts = {}
        for char in text.lower():
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        return counts

def sort_characters(char_count_dict):
    chars_list = []

    # First, create a list of dictionaries
    for char, count in char_count_dict.items():
        char_dict = {"character": char, "count": count}
        chars_list.append(char_dict)
    
    # Define a function that tells sort() which value to use for comparison
    def sort_on(dict):
        return dict["count"]
    
    # Sort the list after all items are added
    chars_list.sort(reverse=True, key=sort_on)

    return chars_list