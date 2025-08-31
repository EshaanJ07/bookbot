import sys
from stats import words_in_doc
from stats import character_count
from stats import sorted_ch_count
if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)



def get_book_text(file):
	with open(file) as f:
		file_string = f.read()
	return file_string

def main():
	book_path = sys.argv[1]
	book_string = get_book_text(book_path)	
	num_words = words_in_doc(book_string)
	count = character_count(book_string)
	ch_list_dict = sorted_ch_count(count)
	print(f"============ BOOKBOT ============\nAnalyzing book found at {book_path}")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words\n--------- Character Count -------")
	for d in ch_list_dict:
		if d["char"].isalpha():
			print(f"{d["char"]}: {d["num"]}")
	print("============= END ===============")
main()

