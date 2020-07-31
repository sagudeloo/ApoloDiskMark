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
Depends: python3:any, python3-pyqt5, libxcb1, fio
Maintainer: Fred Lins <fredcox@gmail.com>
Description: {description}
"""

# Directory configs
currentDir = os.getcwd()
debianDir = f'{currentDir}/{package}/DEBIAN'
binDir = f'{currentDir}/usr/bin'
dPackagesDir = f'{currentDir}/usr/lib/python3/dist-packages'
applicationsDir = f'{currentDir}/usr/share/applications'
distDebianDir = f'{currentDir}/dist-debian'
finalDebian = f'{package}-{version}_amd64.deb'

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
cmd = f'cp -Rv {currentDir}/{package} {dPackagesDir}'
logger.info(f'command: {cmd}')
os.system(cmd)

logger.info(f'Creating applications directory in {applicationsDir}')
os.system(f'mkdir -p {applicationsDir}')

logger.info('Copying desktop file to applications dir...')
os.system(f'cp {currentDir}/{package}/{package}.desktop {applicationsDir}')

logger.info(f'Moving usr structure directory to {currentDir}/{package}')
os.system(f'mv {currentDir}/usr {currentDir}/{package}')


logger.info('Make debian package')
os.system(f'dpkg-deb --build {package}')

logger.info('Rename package...')
os.system(f'mv {currentDir}/{package}.deb {currentDir}/{finalDebian}')

logger.info('Moving debian to debian-dist directory')
if not os.path.isdir(f'{distDebianDir}'):
    os.system(f'mkdir {distDebianDir}')

os.system(f'mv {finalDebian} {distDebianDir}')


# logger.info('Remove unecessary directories...')
shutil.rmtree(f'{debianDir}')
shutil.rmtree(f'{binDir}')
shutil.rmtree(f'{dPackagesDir}')
shutil.rmtree(f'{applicationsDir}')
shutil.rmtree(f'{currentDir}/usr')