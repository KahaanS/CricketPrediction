import yaml
import sqlite3

files = open('filelist.txt')
fileNames = list()
balls = list()

sum = 0
fortySum = 0
thirtySum = 0
fortyWickets = 0
thirtyWickets = 0

conn = sqlite3.connect('matches.sqlite')
cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS matches''' )
cur.execute('''CREATE TABLE IF NOT EXISTS matches
    (File TEXT PRIMARY KEY, TeamA TEXT, TeamB TEXT, ThirtyScore INTEGER,
     FortyScore INTEGER, FiftyScore INTEGER, FortyWickets INTEGER, ThirtyWickets INTEGER, Date TEXT, Result TEXT)''')

for line in files:
    line = line.rstrip()
    names = line.split()
    for name in names:
        fileNames.append(name)

for file in fileNames:
    matchDict = yaml.load(open(file))
    print (file)

    teams = matchDict['info']['teams']
    print (teams[0], "VS", teams[1])

    date = matchDict['info']['dates'][0]
    print(date)

    try:
        result =  matchDict['info']['outcome']['result']
    except:
        result = matchDict['info']['outcome']['winner']

    print('Result:', result)

    if result != 'no result':
        for ball in matchDict['innings'][0]['1st innings']['deliveries']:
            key = list(ball.keys())[0]
            runs = int(ball[key]['runs']['total'])

            if key < 40.1 :
                fortySum = fortySum + runs

                try:
                    wicket = ball[key]['wicket']
                    fortyWickets = fortyWickets+1
                except:
                    fortyWickets = fortyWickets

            if key < 30.1 :
                thirtySum = thirtySum + runs

                try:
                    wicket = ball[key]['wicket']
                    thirtyWickets = thirtyWickets+1
                except:
                    thirtyWickets = thirtyWickets

            sum = sum + runs
    else:
        print ('---------')
        continue

    print ('30 overs:',thirtySum)
    print ('40 overs:',fortySum)
    print ('50 overs:',sum)
    percent = sum/fortySum*100
    print (percent)
    print ('Wickets at 30 overs:',thirtyWickets)
    print ('Wickets at 40 overs:',fortyWickets)

    if percent != 100:

        cur.execute('INSERT INTO matches (File, TeamA, TeamB, ThirtyScore, FortyScore, FiftyScore, FortyWickets, ThirtyWickets, Date, Result) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(file, teams[0], teams[1], thirtySum, fortySum, sum, fortyWickets, thirtyWickets, date, result))
        print ('Added')
        conn.commit()

    print ('---------')

    sum = 0
    fortySum = 0
    thirtySum = 0
    percent = 0
    fortyWickets = 0
    thirtyWickets = 0

conn.commit()
