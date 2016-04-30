import sys
#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
#import the library used to query a website
import urllib2
#specify the url
wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
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
#find all tables
all_tables=soup.find_all("table")
#using class attribute to find desired table
# inspect element to get class
desired_table=soup.find("table",class_="wikitable sortable plainrowheaders")
print desired_table
#extract the desired data from the table into a dataframe
#set up lists
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
#iterate over each row - tr - and assign each to a variable and append to a list
for row in desired_table.findAll("tr"):
  cells = row.findAll("td")
  #store 2nd column of data
  states = row.findAll("th")
  #extract table body not header
  if len(cells)==6:
    #use find(text=True) to access element
    A.append(cells[0].find(text=True))
    B.append(states[0].find(text=True))
    C.append(cells[1].find(text=True))
    D.append(cells[2].find(text=True))
    E.append(cells[3].find(text=True))
    F.append(cells[4].find(text=True))
    G.append(cells[5].find(text=True))
    #import pandas to convert list to data frame
    import pandas as pd
    df=pd.DataFrame(A,columns=["Number"])
    df["State/UT"]=B
    df["Admin_Capital"]=C
    df["Legislative_Capital"]=D
    df["Judiciary_Capital"]=E
    df["Year_Capital"]=F
    df["Former_capital"]=G
    print df
