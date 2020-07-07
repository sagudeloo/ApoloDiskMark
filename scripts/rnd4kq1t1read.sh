#!/bin/bash
TARGET="$1"
me=`basename "$0"`

fio --loops=1 --size=512k --filename="$TARGET/fiomark.tmp" --stonewall --ioengine=libaio --direct=1 \
--name="$me" --bs=4k --iodepth=1 --numjobs=1 --rw=randread --output-format=json

rm "$TARGET/fiomark.tmp"