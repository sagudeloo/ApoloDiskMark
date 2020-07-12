from setuptools import setup

setup(name='crazydiskmark',
      version='0.2.8',
      description='Linux disk benchmark tool like CrystalDiskMark',
      url='https://github.com/fredcox/crazydiskmark',
      author='Fred Lins',
      author_email='fredcox@gmail.com',
      license='MIT',
      scripts=['bin/crazydiskmark'],
      packages=['crazydiskmark'],
      install_requires=[
            'humanfriendly',
            'PyQt5'
      ],
      include_package_data=True,
      zip_safe=False)
