def read_text():
	movies = open("curse_movies.txt")
	contents_of_file = movies.read()
	length_of_file = len(contents_of_file)
	print (length_of_file)
	print (contents_of_file)
	movies.close()
	find_curse_words(contents_of_file)

def find_curse_words(text):
	#split the text into an array
	words = text.split(" ")
	for word in words:
		print (word)


read_text()