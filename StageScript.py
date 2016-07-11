values = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O']
index = ['1','2','3','4','5','6','7','8','9','J','K','L','M','N','O']

for i in values:
    for n in index:

        print(";"+ i + n+":")
        print('PSSC:GOTO:Cell=' + i + n)
        print('WAIT::DURATION=5')
        print('DC:CollectSingleScan')
        print("")

