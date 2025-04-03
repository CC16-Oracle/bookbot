import sys
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    pass
    sys.exit(1)
def main():
    def get_book_text(path):
        with open(path) as file:
            file_contents = file.read()
        return file_contents


    from stats import get_num_words, get_letter_frequency
    char_freq = get_letter_frequency(get_book_text(sys.argv[1]))
    
        
    
    print(f"{get_num_words(get_book_text(sys.argv[1]))} words found in the document.")
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(get_book_text(sys.argv[1]))} total words")
    print("--------- Character Count -------")
    for i in range(0, len(char_freq)):
        print(f"{char_freq[i][0]}: {char_freq[i][1]}")
    print("============= END ===============")







main()