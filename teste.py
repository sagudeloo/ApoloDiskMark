import re

version = '0.2.12'
pattern = "([0-9]+.[0-9]+.[0-9]+)"
newlines = []
filename = 'crazydiskmark/aboutdialog.ui'
with open(filename, 'r') as f:
    for line in f.readlines():
        if re.search(pattern, line):
            newlines.append(re.sub(pattern, version, line))
        else:
            newlines.append(line)

with open(filename, 'w') as f:
    for line in newlines:
        f.write(line)
