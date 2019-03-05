import re


class Counter:
	def word_counter(self, sentences):
		l_of_words = sentences.split(' ')
		word_count = len(l_of_words)
		return word_count
	
	def character_counter(self, obj):
		s = str(obj)
		char_count = len(re.sub('[^A-Za-z0-9]+', '', s))
		# test = len(re.sub('\W', '', s))
		return char_count
