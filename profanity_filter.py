import os
import urllib
url_direct = "http://www.wdylike.appspot.com/?q="

def read_text():
	movies = open("curse_movies.txt")
	contents_of_file = movies.read()
	length_of_file = len(contents_of_file)
	print (length_of_file)
	print (contents_of_file)
	movies.close()
	# find_curse_words(contents_of_file)
	check_profanity(contents_of_file)

#check whole file
def check_profanity(text_to_check):
	connection = urllib.urlopen(url_direct + text_to_check)
	output = connection.read()
	print(output)
	connection.close()
	if "true" in output:
		print("Profanity Alert!!")
	elif "false" in output:
		print("This document has no curse words")
	else:
		print("This document cannot be scanned properly")
		
#check each word in file
def find_curse_words(text):
	#split the text into an array
	words = text.split(" ")
	count_of_words = 0
	for word in words:
		count_of_words = count_of_words + 1
		connection = urllib.urlopen(url_direct + word)
		output = connection.read()
		print(output)
		connection.close()
		# if (urllib.urlopen(url_direct + word).read()):
		if "true" in output:
			new_word = word.replace(word,"curse!")
			print("Profanity Alert!!")
			print ("old word was ",word," and the new word is ",new_word)
		elif "false" in output:
			print("This document has no curse words")
		else:
			print("This document cannot be scanned properly")
	print (count_of_words)

read_text()