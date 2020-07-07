#!/bin/bash
cat /proc/cpuinfo | sed -n '/^model\sname/p' | head -1 | cut -d " " -f 3-60