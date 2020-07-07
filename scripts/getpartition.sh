#!/bin/bash
df -P ${1} | tail -1 | cut -d' ' -f 1