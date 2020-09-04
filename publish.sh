#!/bin/bash

rm -rfv dist/
rm -rfv build/
rm -rfv crazydiskmark.egg-info/

pandoc -r markdown -w plain -o README.me README.md
pandoc --standalone --to man README.md -o crazydiskmark.1

python3 setup.py sdist bdist_wheel
python3 -m twine upload dist/*


rm -rfv dist/
rm -rfv build/
rm -rfv crazydiskmark.egg-info/
