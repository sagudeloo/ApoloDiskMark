#!/bin/bash
TARGET="$1"
me=`basename "$0"`

fio --loops=1 --size=1024m --filename="$TARGET/fiomark.tmp" --stonewall --ioengine=libaio --direct=1 \
--name="$me" --iodepth=8 --numjobs=1 --rw=read --output-format=json

rm "$TARGET/fiomark.tmp"