import os
import re
import coloredlogs
import logging
import shutil

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG')

package = 'crazydiskmark'
description = 'Crazy DiskMark is a utility to benchmark SSD disks on linux and produce results like CrystalDiskMark.'

version = ''
pattern = "([0-9]+.[0-9]+.[0-9]+)"
newlines = []
dialog_filename = f"{package}/aboutdialog.ui"
with open(dialog_filename, 'r') as f:
    for line in f.readlines():
        if re.search(pattern, line):
            version = re.search(pattern, line).group()
            break

# Global vars
controlContent = f"""Package: {package}
Version: {version}
Section: custom
Priority: optional
Architecture: all
Essential: no
Installed-Size: 1024
Maintainer: Fred Lins <fredcox@gmail.com>
Description: {description}
"""

# Directory configs
currentDir = os.getcwd()
debianDir = f'{currentDir}/{package}/DEBIAN'
binDir = f'{currentDir}/{package}/usr/bin'
dPackagesDir = f'{currentDir}/{package}/usr/lib/python3/dist-packages'
applicationsDir = f'{currentDir}/{package}/usr/share/applications'

logger.info(f"current dir is [ {currentDir} ]")

logger.info(f'binDir is {binDir}')

logger.info('Prepare to make deb package...')
logger.info(f"Creating {debianDir}/control file....")

if os.path.isdir(f"{debianDir}"):
    os.system(f"rm -rfv {debianDir}")

os.system(f"mkdir {debianDir}")

os.system(f'touch {debianDir}/control')

f = open(f"{debianDir}/control", 'w+')
f.write(controlContent)
f.close()

logger.info(f'Creating binDir: [{binDir}]')
os.system(f'mkdir -p {binDir}')
logger.info(f'Copying binary app to binDir...')
cmd = f'cp {currentDir}/bin/{package} {binDir}'
logger.debug(f'command: [{cmd}]')
os.system(cmd)

logger.info('Creating dist-packages dir')
os.system(f'mkdir -p {dPackagesDir}')

logger.info('Copying sources and necessary files to dist-packages dir')
cmd = f'ls {currentDir}/{package}'
logger.info(f'command: {cmd}')
os.system(cmd)

# logger.info(f'Creating applications directory in {applicationsDir}')
# os.system(f'mkdir -p {applicationsDir}')

# logger.info('Copying desktop file to applications directory....')
# os.system(f'cp {currentDir}/{package}/{package}.desktop {applicationsDir}')

# logger.info('Make debian package')
# os.system(f'dpkg-deb --build {package}')

# logger.info('Delete debian directory. No more necessary!')
# shutil.rmtree(f'{currentDir}/debian')
