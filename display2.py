import requests
import json
import csv

name = 'toothlessg'
matchids = []

#check for key
def checkforkey(diction,key):
    if key in diction:
        return diction[key]
    else:
        #print("missing key")
        return 0


#Get ID from name
idr = requests.get('https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/'+name+'?api_key=28f2fa25-e664-4919-bd2e-2e61caf18c6f')
jsonidr = json.loads(idr.text)
sumid = str(jsonidr[name]['id'])
print ("ID=" + sumid)

#Get Game IDs from recent games
gamesr = requests.get('https://na.api.pvp.net/api/lol/na/v1.3/game/by-summoner/'+sumid+'/recent?api_key=28f2fa25-e664-4919-bd2e-2e61caf18c6f')
jgr = json.loads(gamesr.text)

for game in jgr['games']:
    matchids.append(game['gameId'])


#get match stats

for matchid in matchids:
    print(matchid)
    matchr = requests.get('https://na.api.pvp.net/api/lol/na/v2.2/match/' + str(matchid) + '?api_key=28f2fa25-e664-4919-bd2e-2e61caf18c6f')
    jmr = json.loads(matchr.text)

    mtime = jmr['matchDuration']

    print(round(mtime/60,2))





