import os
import webbrowser
url_direct = "https://www.youtube.com/watch?q="

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
	count_of_words = 0
	for word in words:
		count_of_words = count_of_words + 1
		if (webbrowser.open(url_direct + word,new=2)) == true:
			os.rename(word,word.replace("curse!"))
		print (word)
	print (count_of_words)

read_text()