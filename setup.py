import setuptools
import re

with open("README.md", "r") as fh:
    long_description = fh.read()

# update aboutdialog.ui with correct version
version = '0.4.5'
pattern = "([0-9]+.[0-9]+.[0-9]+)"
newlines = []
dialog_filename = 'crazydiskmark/aboutdialog.ui'
with open(dialog_filename, 'r') as f:
    for line in f.readlines():
        if re.search(pattern, line):
            newlines.append(re.sub(pattern, version, line))
        else:
            newlines.append(line)

with open(dialog_filename, 'w') as f:
    for line in newlines:
        f.write(line)

setuptools.setup(
    name="crazydiskmark",
    version=version,
    author="Fred Cox",
    author_email="fredcox@gmail.com",
    description="Linux disk benchmark tool like CrystalDiskMark",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fredcox/crazydiskmark",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.8',
    scripts=['bin/crazydiskmark'],

    install_requires=[
        'humanfriendly',
        'PyQt5',
        'coloredlogs'
    ],
    include_package_data=True,
    zip_safe=False,
)
