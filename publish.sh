#!/bin/bash

rm -rfv dist/
rm -rfv build/
rm -rfv crazydiskmark.egg-info/

python3 setup.py sdist bdist_wheel
python3 -m twine upload dist/*


rm -rfv dist/
rm -rfv build/
rm -rfv crazydiskmark.egg-info/