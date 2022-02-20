results = list()
print('')

for line in open('results.txt'):
    line = line.replace('\n','')
    results.append(float(line))

while True:
    t_f = input('Please enter "t" for thirty overs or "f" for forty overs: ')
    if t_f == 't' or t_f == 'f':
        break
    print('')
    print('Please input "t" or "f"')
    print('')

print('')

if t_f == 'f':

    while True:
        runs = input('Input runs after 40 overs: ')

        try:
            runs = int(runs)
        except:
            print('')
            print ('Please enter a whole number of runs')
            print('')
            continue

        if runs < 0:
            print('')
            print('Please enter a positive number of runs')
            print('')
            continue

        break

    print('')

    while True:
        wickets = input('Input wickets after 40 overs: ')

        try:
            wickets = int(wickets)
        except:
            print('')
            print ('Please enter a whole number of wickets')
            print('')
            continue

        if wickets < 0 or wickets > 9:
            print('')
            print('Please enter wickets between 0 and 9')
            print('')
            continue

        break

    key = wickets+10
    percent = results[key]

    preRuns = round(percent*runs/100)

    print('')
    print('–––––––––––––––––––––––––––––––––––––––––––––––')
    print('The predicted total after 50 overs is:',preRuns,'runs')
    print('–––––––––––––––––––––––––––––––––––––––––––––––')
    print('')

if t_f == 't':

    while True:
        runs = input('Input runs after 30 overs: ')

        try:
            runs = int(runs)
        except:
            print('')
            print ('Please enter a whole number of runs')
            print('')
            continue

        if runs < 0:
            print('')
            print('Please enter a positive number of runs')
            print('')
            continue

        break

    print('')

    while True:
        wickets = input('Input wickets after 30 overs: ')

        try:
            wickets = int(wickets)
        except:
            print('')
            print ('Please enter a whole number of wickets')
            print('')
            continue

        if wickets < 0 or wickets > 9:
            print('')
            print('Please enter wickets between 0 and 9')
            print('')
            continue

        break

    percent = results[wickets]
    print(percent)

    pre40Runs = round(percent*runs/100)

    print('')
    print('–––––––––––––––––––––––––––––––––––––––––––––––')
    print('The predicted total after 40 overs is:',pre40Runs,'runs')
    print('–––––––––––––––––––––––––––––––––––––––––––––––')

    percent = results[wickets+10]

    preRuns = round(percent*pre40Runs/100)

    print('')
    print('–––––––––––––––––––––––––––––––––––––––––––––––')
    print('The predicted total, without loss of wickets till 40th over, after 50 overs is:',preRuns,'runs')
    print('–––––––––––––––––––––––––––––––––––––––––––––––')
    print('')
