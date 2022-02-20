#!/usr/bin/env python

import yaml

fortySum = 0
sum = 0
wickets = 0

matchDict = yaml.load(open('1144491.yaml'))
balls = list()

for ball in matchDict['innings'][0]['1st innings']['deliveries']:
    key = list(ball.keys())[0]
    runs = int(ball[key]['runs']['total'])
    result = matchDict['info']['outcome']['winner']
    print(result)

    if key < 40.1 :
        fortySum = fortySum + runs
        try:
            wicket = ball[key]['wicket']
            wickets = wickets+1
        except:
            wickets = wickets
    sum = sum + runs

year = str(matchDict['info']['dates'][0]).split('-')[0]
print (year)
print ('40 overs:',fortySum)
print ('50 overs:',sum)
percent = sum/fortySum*100
print(percent)
print(wickets)
#print(matchDict['innings'][0]['1st innings']['deliveries'])
