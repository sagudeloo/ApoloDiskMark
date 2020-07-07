#!/bin/bash
hdparm -I $1 | awk '/\sModel.*$/ {print $3}'