import coloredlogs
import logging
import os
import re

# Create a logger object.
# shellcheck disable=SC2034
logger = logging.getLogger(__name__)
coloredlogs.install()

logger.info('Preparing to submit AUR Package...')
os.chdir('crazydiskmark-aur/')
logger.info('Printing .SRCINFO...')
os.system('makepkg --printsrcinfo > .SRCINFO')
logger.info('add files PKGBUILD and .SRCINFO to repository...')
os.system('git add PKGBUILD .SRCINFO')

logger.info('Get current version...')
# update aboutdialog.ui with correct version
pattern = "([0-9]+.[0-9]+.[0-9]+)"
newlines = []
setup_filename = '../setup.py'
version = '0.0'
with open(setup_filename, 'r') as f:
    for line in f.readlines():
        group = re.search(pattern, line)
        if group:
            logger.info('I found version =====> {}'.format(group[0]))
            version = group[0]
            break


logger.info('Update the package with new version...')


logger.info('git pushing....')



#


#makepkg --printsrcinfo > .SRCINFO
#

#git commit -m "mensagem útil de commit"

os.system('cd ../')