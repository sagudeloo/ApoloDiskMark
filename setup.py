import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
                 name="crazydiskmark-fredcox",
                 version="0.2.8",
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
                     "Operating System :: OS Independent",
                 ],
                 python_requires='>=3.8',
                 scripts=['bin/crazydiskmark'],

                 install_requires=[
                     'humanfriendly',
                     'PyQt5'
                 ],
                 include_package_data=True,
                 zip_safe=False,
                 )
