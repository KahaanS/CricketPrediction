import yaml

files = open('filelistsmall.txt')
fileNames = list()
balls = list()
sum = 0
fortySum = 0
ctr = 0
percentSum = 0

for line in files:
    line = line.rstrip()
    names = line.split()
    for name in names:
        fileNames.append(name)

for file in fileNames:
    matchDict = yaml.load(open(file))

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

            sum = sum + runs
    else:
        print ('---------')
        continue

    print (file)
    print ('40 overs:',fortySum)
    print ('50 overs:',sum)
    percent = sum/fortySum*100
    print (percent)
    print ('---------')

    if percent != 100:
        ctr = ctr+1
        percentSum = percentSum+percent

    sum = 0
    fortySum = 0
    percent = 0

print ('Average',percentSum/ctr)
