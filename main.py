def main():
    def get_book_text(path):
        with open(path) as file:
            file_contents = file.read()
        return file_contents

    def num_words(file_contents):
        return len(file_contents.split())
    
    word_count = num_words(get_book_text("books/frankenstein.txt"))
        
    
    print(f"{word_count} words found in the document.")





main()