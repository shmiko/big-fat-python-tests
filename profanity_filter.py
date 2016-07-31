def read_text():
	movies = open("curse_movies.txt")
	contents_of_file = movies.read()
	print (contents_of_file)
	movies.close()
read_text()