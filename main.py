import sys
from stats import get_num_words, get_num_characters, sort_num_characters

def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  report = ""
  text = get_book_text(sys.argv[1]) # "./books/frankenstein.txt"
  num_words = get_num_words(text)
  num_characters = get_num_characters(text)
  sorted_num_characters = sort_num_characters(num_characters)
  print("============ BOOKBOT ============")
  print("Analyzing book found at books/frankenstein.txt...")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")
  for char_dict in sorted_num_characters:
    char = char_dict["char"]
    count = char_dict["count"]
    if char.isalpha():
      print(f"{char}: {count}")
  print("============= END ===============")

main()