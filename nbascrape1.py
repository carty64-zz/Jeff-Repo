import requests
from bs4 import BeautifulSoup

url = 'http://www.nba.com/gameline/20160331/'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, "lxml")
table = soup.find('h5', attrs={'class': 'nbaModTopTeamName awayteam'})
table1 = soup.find('h5', attrs={'class': 'nbaModTopTeamName hometeam'})
print table.prettify(),table1.prettify()

#############


#import requests
#from BeautifulSoup import BeautifulSoup

#url = 'http://stats.nba.com/scores#!/04/01/2016'
#response = requests.get(url)
#html = response.content

#soup = BeautifulSoup(html)
#table =  soup.findAll('h5', attrs={'class': 'nbaModTopTeamName hometeam'})
#print soup
#table = soup.findAll('tbody')
#print table

#for row in table.findAll('tr'):
#  for cell in row.findAll('td'):
#    print cell.text
