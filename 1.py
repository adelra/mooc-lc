import nltk
with open("file.txt") as a:
	text=nltk.word_tokenize(a)
	nltk.pos_tag(a)