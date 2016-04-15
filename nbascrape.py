import requests
from BeautifulSoup import BeautifulSoup

url = 'http://www.nba.com/gameline/20160331/'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('string', attrs={'class':'nbaMnQuScores'})
print table.prettify()