VERSION="0.2.4"
sed -i "s/[0-9]\.[0-9]\.[0-9]/${VERSION}/g" aboutdialog.ui

pyinstaller crazydiskmark.py

rm -rfv build/

cp -Rv images/ dist/crazydiskmark/
cp -Rv scripts/ dist/crazydiskmark/
cp -Rv *.ui dist/crazydiskmark/

cp dist/crazydiskmark/images/icon.png dist/crazydiskmark/Application.png

cp crazydiskmark.desktop dist/crazydiskmark/

cp AppRun dist/crazydiskmark/

appimagetool-x86_64.AppImage -v dist/crazydiskmark/

rm -rfv dist/

mv Crazy_DiskMark-x86_64.AppImage release/Crazy_DiskMark-${VERSION}-x86_64.AppImage

chmod -x release/Crazy_DiskMark-${VERSION}-x86_64.AppImage

