def anagrams_for(comparison_word, list_of_words):
	# establishes list of strings that are anagrams of comparison word
	output_list = []
	word_list = list_of_words

	# function to convert word into a comparable string
	def string_sort(string):
		string = sorted(string.lower())
		string = ''.join(string)
		return string.strip()
	
	# function to compare the base word with each of the words from list by length, then letter by letter
	def str_comparison(word_one, word_two):
		if len(string_sort(word_one)) != len(string_sort(word_two)):
			return False
			for x in range(len(word_one)):
				if (word_one[x] != word_two[x]):
					return False
		return True
	
	# calls str_comparison function, which in turn calls the string_sort function for base word and each word in word_list
	# if str_comparison returns true, the word is appended to output_list and returned in list
	for words in word_list:
		if (str_comparison(comparison_word, words)):
			output_list.append(words)
	return output_list


list_of_words = ["threads", "trashed", "hardest", "hatreds", "hounds"]
print(anagrams_for("threads", list_of_words))
print(anagrams_for("apple", list_of_words))
print(anagrams_for("saltier", ["cognac", "saltier", "realist", "retails"]))

