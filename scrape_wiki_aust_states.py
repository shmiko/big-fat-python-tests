import sys
#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
#import the library used to query a website
import urllib2
#specify the url
wiki = "https://en.wikipedia.org/wiki/States_and_territories_of_Australia"
#Query the website and return the html to the variable 'page'
page = urllib2.urlopen(wiki)
#Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page)
#print page as HTML
    #print(soup.prettify())
#print title tag and inner.html
print soup.title
#print title string only
print soup.title.string
#print <a> tags
print soup.a
#print all a tags
print soup.find_all("a")
#print only links
all_links=soup.find_all("a")
for link in all_links:
  print link.get("href")
print "printed links"
#find all tables
all_tables=soup.find_all("table")
#using class attribute to find desired table
# inspect element to get class
desired_table=soup.find("table",class_="wikitable sortable")
print desired_table
print "printed table"
caption = soup.find("caption")
print caption.string
#extract the desired data from the table into a dataframe
#set up lists
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
H=[]
I=[]
#iterate over each row - tr - and assign each to a variable and append to a list
for row in desired_table.find_all("tr"):
  col = row.find_all("td")
  #extract table body not header
  # if len(cells)==8:
  #use find(text=True) to access element


  A.append(col[0].find(text=True))
  B.append(col[1].find(text=True))
  C.append(col[2].find(text=True))
  D.append(col[3].find(text=True))
  E.append(col[4].find(text=True))
  F.append(col[5].find(text=True))
  G.append(col[6].find(text=True))
  H.append(col[7].find(text=True))
  I.append(col[8].find(text=True))


#import pandas to convert list to data frame
import pandas as pd
df=pd.DataFrame(A,columns=["Flag"])
df["State/Territory"]=B
df["Abbrev"]=C
df["ISO"]=D
df["Postal"]=E
df["Type"]=F
df["Capital"]=G
df["Population"]=H
df["Area"]=I
print df
