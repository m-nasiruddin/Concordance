myDict = {}
myLines = {}
linenum = 0

f = open("data/file.txt", "r")
for line in f:
    # print(line.strip())
    line = line.strip()
    line = line.lower()
    line = line.split()
    linenum += 1
    for word in line:
        word = word.strip()
        word = word.lower()
        if not word in myDict:
            myDict[word] = []
        myDict[word].append(linenum)
        if not word in myLines:
            myLines[word] = []
        myLines[word].append(line)

print("%-15s %5s  %s" % ("Word", 'Count', "Line Numbers"))
for key in sorted(myDict):
    print('%-15s %5d: %s' % (key, len(myDict[key]), myDict[key]))
print("%-15s" % "Lines")
for key in sorted(myLines):
    print ('%-15s' % (myLines[key]))
