#!/usr/bin/python3
import coloredlogs
import logging
import sys
import os

# Create a logger object.
# shellcheck disable=SC2034
logger = logging.getLogger(__name__)
coloredlogs.install()

if len(sys.argv) == 1:
    logger.info('Please, specify the version from command line!')
    sys.exit(0)

version = sys.argv[1]
cmd = f'copr-cli build crazydiskmark rpmbuild/crazydiskmark-{version}.fc32.src.rpm'
os.system(cmd)
