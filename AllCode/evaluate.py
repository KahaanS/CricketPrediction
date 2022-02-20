import sqlite3

zeroCtr = 0
oneCtr = 0
twoCtr = 0
threeCtr = 0
fourCtr = 0
fiveCtr = 0
sixCtr = 0
sevenCtr = 0
eightCtr = 0
nineCtr = 0

zeroPercent = 0
onePercent = 0
twoPercent = 0
threePercent = 0
fourPercent = 0
fivePercent = 0
sixPercent = 0
sevenPercent = 0
eightPercent = 0
ninePercent = 0

conn = sqlite3.connect('matches.sqlite')
cur = conn.cursor()
matches = list()

items = cur.execute('SELECT * FROM matches')
for row in cur:
    matches.append(row)

for match in matches:
    wickets = match[5]
    forty = int(match[3])
    fifty = int(match[4])
    percent = fifty/forty*100
    year = int(match[6].split('-')[0])

    if year < 2015:
        continue

    print(year)

    if wickets == 0:
        zeroCtr = zeroCtr + 1
        zeroPercent = zeroPercent + percent
        print ('Wickets:',wickets)
        print (forty)
        print (fifty)
        print (percent)
        print ('---------')

    elif wickets == 1:
        oneCtr = oneCtr + 1
        onePercent = onePercent + percent
        print ('Wickets:',wickets)
        print (forty)
        print (fifty)
        print (percent)
        print ('---------')

    elif wickets == 2:
        twoCtr = twoCtr + 1
        twoPercent = twoPercent + percent
        print ('Wickets:',wickets)
        print (forty)
        print (fifty)
        print (percent)
        print ('---------')

    elif wickets == 3:
        threeCtr = threeCtr + 1
        threePercent = threePercent + percent
        print ('Wickets:',wickets)
        print (forty)
        print (fifty)
        print (percent)
        print ('---------')

    elif wickets == 4:
        fourCtr = fourCtr + 1
        fourPercent = fourPercent + percent
        print ('Wickets:',wickets)
        print (forty)
        print (fifty)
        print (percent)
        print ('---------')

    elif wickets == 5:
        fiveCtr = fiveCtr + 1
        fivePercent = fivePercent + percent
        print ('Wickets:',wickets)
        print (forty)
        print (fifty)
        print (percent)
        print ('---------')

    elif wickets == 6:
        sixCtr = sixCtr + 1
        sixPercent = sixPercent + percent
        print ('Wickets:',wickets)
        print (forty)
        print (fifty)
        print (percent)
        print ('---------')

    elif wickets == 7:
        sevenCtr = sevenCtr + 1
        sevenPercent = sevenPercent + percent
        print ('Wickets:',wickets)
        print (forty)
        print (fifty)
        print (percent)
        print ('---------')

    elif wickets == 8:
        eightCtr = eightCtr + 1
        eightPercent = eightPercent + percent
        print ('Wickets:',wickets)
        print (forty)
        print (fifty)
        print (percent)
        print ('---------')

    elif wickets == 9:
        nineCtr = nineCtr + 1
        ninePercent = ninePercent + percent
        print ('Wickets:',wickets)
        print (forty)
        print (fifty)
        print (percent)
        print ('---------')

print ('---------')
print ('Results:')
print ('Zero wicket:')
print ('Percentage:', zeroPercent/zeroCtr)
print ('Sample size:', zeroCtr)
print ('')

print ('One wicket:')
print ('Percentage:', onePercent/oneCtr)
print ('Sample size:', oneCtr)
print ('')

print ('Two wicket:')
print ('Percentage:', twoPercent/twoCtr)
print ('Sample size:', twoCtr)
print ('')

print ('Three wicket:')
print ('Percentage:', threePercent/threeCtr)
print ('Sample size:',threeCtr)
print ('')

print ('Four wicket:')
print ('Percentage:', fourPercent/fourCtr)
print ('Sample size:',fourCtr)
print ('')

print ('Five wicket:')
print ('Percentage:', fivePercent/fiveCtr)
print ('Sample size:',fiveCtr)
print ('')

print ('Six wicket:')
print ('Percentage:', sixPercent/sixCtr)
print ('Sample size:',sixCtr)
print ('')

print ('Seven wicket:')
print ('Percentage:', sevenPercent/sevenCtr)
print ('Sample size:',sevenCtr)
print ('')

print ('Eight wicket:')
print ('Percentage:', eightPercent/eightCtr)
print ('Sample size:',eightCtr)
print ('')

print ('Nine wicket:')
print ('Percentage:', ninePercent/nineCtr)
print ('Sample size:',nineCtr)
print ('')

fhand = open('results.txt', 'w')
fhand.write(str(zeroPercent/zeroCtr) + '\n')
fhand.write(str(onePercent/oneCtr) + '\n')
fhand.write(str(twoPercent/twoCtr) + '\n')
fhand.write(str(threePercent/threeCtr) + '\n')
fhand.write(str(fourPercent/fourCtr) + '\n')
fhand.write(str(fivePercent/fiveCtr) + '\n')
fhand.write(str(sixPercent/sixCtr) + '\n')
fhand.write(str(sevenPercent/sevenCtr) + '\n')
fhand.write(str(eightPercent/eightCtr) + '\n')
fhand.write(str(ninePercent/nineCtr) + '\n')
