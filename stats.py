def words_in_doc(file_string):
        return len(file_string.split())

def character_count(file_string):
	count = {}
	for ch in file_string:
		count[ch.lower()] = 1 + count.get(ch.lower(), 0)
	return count

def sort_on(items):
	return items["num"]

def sorted_ch_count(count):
	count_dicts = []
	for key in count:
		count_dicts.append({"char": key, "num": count[key]})
	count_dicts.sort(reverse=True, key=sort_on)
	return count_dicts
