#!/usr/bin/python3

import coloredlogs
import logging
import re


def updateFile(fileToUpdate, regPattern, newString):
    newlines = []
    with open(fileToUpdate, 'r') as f:
        for line in f.readlines():
            if re.search(regPattern, line):
                newlines.append(re.sub(regPattern, newString, line))
            else:
                newlines.append(line)

    with open(fileToUpdate, 'w') as f:
        for line in newlines:
            f.write(line)


# Create a logger object.
# shellcheck disable=SC2034
logger = logging.getLogger(__name__)
coloredlogs.install()

newVersion = '0.5.7'
pattern = "([0-9]+.[0-9]+.[0-9]+)"

files = ['setup.py', 'aur/PKGBUILD', 'debian/changelog', 'rpmbuild/crazydiskmark.spec']

for file in files:
    logger.info(f'Update version in file [{file}]')
    updateFile(file, pattern, newVersion)

logger.info(f'All files was updated with version [{newVersion}]')
