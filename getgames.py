import urllib2
import json
import requests
import datetime
import time

print time.time()
todays_date =  datetime.date.today().strftime("%Y%m%d")
#url = 'http://data.nba.com/data/json/nbacom/2016/gameline/%s/games.json' % (todays_date)
url = 'http://stats.nba.com/scores/GameID=0041400235&GameEventID;=308'
response = urllib2.urlopen(url)
data = response.read()
#data = json.loads(data)
print time.time() 

print data

#use this to load a local JSON file
#file = open('gamedata.json', 'r')
#data = file.read()
#gamedata = json.loads(data, encoding="utf-8")
#print gamedata

#game_ids = []

#for games in data['games']:
#  for teams in games['teams']:
#    game_ids.append(str(teams['scores']))
#    print teams['scores']

#for x in game_ids:
#  print x

#  if not team['is_nba_team']:
#    continue
#  teamnickname = team['team_nickname']
#  teamid = team['team_id']
#  team_ids[teamnickname]=teamid
#  status = gamedata['games']['prd']['s']
#print status
#print team_ids

#today =  datetime.date.today().strftime("%Y%m%d")
#url = 'http://data.nba.com/data/10s/json/nbacom/2015/gameline/%s/games.json' % today
#response = requests.get(url)
#data = response.content
#nbadata = json.loads(data, encoding="utf-8")

#matchup = []
#results = []

#for x in data['games']:
#  games = x['teams']
#  for z in games:
#    matchup.append(str(z.get('awayTeam') or z.get('homeTeam')))
#    results.append(z['scores'][0])

#for c1, c2 in zip(matchup, results):
#  print c1, c2
