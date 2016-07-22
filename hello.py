#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""A tiny Python program to check that Python is working.
Try running this program from the command line like this:
  python hello.py
  python hello.py Alice
That should print:
  Hello World -or- Hello Alice
Try changing the 'Hello' to 'Howdy' and run again.
Once you have that working, you're ready for class -- you can edit
and run Python code; now you just need to learn Python!
"""

import sys

# # Define a main() function that prints a little greeting.
def main():
#   # Get the name from the command line, using 'World' as a fallback.
#   if len(sys.argv) >= 2:
#     name = len(sys.argv[1])
#   else:
#     name = len('World'
  print 'Hello', name

# # This is the standard boilerplate that calls the main() function.
# if __name__ == '__main__':
#   main()
def main():
  print repeat('Yay',False)
  print repeat('Woo Hoo', True)


def repeat(s,exlaim):
  result = "s * 3"
  if exclaim:
    result = result + '!!!'
  return result

#ll
def main():
    if name == 'Guido':
        print repeeeet(name) + '!!!'
    else:
        print repeat(name)

s = 'hi'
print s[1]
print len(s)
print s + ' more'

# import sys

sys.exit(0)
#

#sys - access to exit(),argv,stdin,stdout
#re - regex
#os - os interface, file system
p1 = 3.14
## the vlue is pi
text = 'the value io pie is' + str(p1)

raw = r'this\t\n and that'
print raw     ## this\t\n and that
    
multi = """It was the best of times.
It was the worst of times."""
print multi
# s.lower(),s.uper()
# s.strip() - removes whitespace
# s.isalpha()/s.isdidgit(),s.isspace() - test is string chars are in character class
# s.startswith('other'),s.endwith('other') - test for start or end of string
# s.find('other') - searches for 'other' within s, returns 1st index if found otherwise -1
# s.replace('old','new') - resturns replacedment string
# s.split('delim') - returns substrings split by delim - no args splits on whitespace
# s.join(list) - opposite of split ( array ) joins elements
# slice.s[start:end] - refer to sub parts of sequences 0 strings and lists
#    H E L L O 
#    0 1 2 3 4
#   -5-4-3-2-1
# % operator
text = "%d little pigs come out or I'll %s and %s and %s" % (3, 'huff', 'puff', 'blow down')
print text
 # add parens to make the long-line work:
text = ("%d little pigs come out or I'll %s and %s and i'll %s your house %s" %
    (3, 'huff', 'puff', 'blow', 'down'))
print text



