import sys
#import pandas
import pandas as pd
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
print "printed caption"
#extract the desired data from the table into a dataframe
#set up lists
flag=[]
state=[]
abrev=[]
iso=[]
postal=[]
type_=[]
capital=[]
population=[]
area=[]
#iterate over each row - tr - and assign each to a variable and append to a list
for row in desired_table.find_all("tr")[1:]:
  col = row.find_all("td")
  # print "col"
  # print col
  col1 = col[0].string
  flag.append(col1)
  col2 = col[1].string
  state.append(col2)
  col3 = col[2].string
  abrev.append(col3)
  col4 = col[3].string
  iso.append(col4)
  col5 = col[4].string
  postal.append(col5)
  col6 = col[5].string
  type_.append(col6)
  col7 = col[6].string
  capital.append(col7)
  col8 = col[7].string
  population.append(col8)
  col9 = col[8].string
  area.append(col9)


#import pandas to convert list to data frame
columns = {'flag': flag, 'State': state, 'Abrev': abrev, 'ISO': iso, 'Postal': postal,'Type':type_,'Capital':capital,'Population':population,'Area':area}
df = pd.DataFrame(columns)
# df=pd.DataFrame(A,columns=["Flag"])
# df["State/Territory"]=B
# df["Abbrev"]=C
# df["ISO"]=D
# df["Postal"]=E
# df["Type"]=F
# df["Capital"]=G
# df["Population"]=H
# df["Area"]=I
print df
