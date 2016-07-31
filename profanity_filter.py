def read_text():
	movies = open("curse_movies.txt")
	contents_of_file = movies.read()
	length_of_file = len(contents_of_file)
	print ("length of movie string is " + length_of_file)
	print (contents_of_file)
	movies.close()
read_text()