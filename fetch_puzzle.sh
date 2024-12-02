#! /bin/bash

set -e

if [ $# -eq 0 ]; then
    day=$(date +%d)
else 
    day=$1
fi

mkdir -p q$day

source .env
curl -sH "Cookie: session=$SESSION" https://adventofcode.com/2024/day/$(echo $day | sed 's/^0*//')/input -o ./q$day/input.txt

echo "All ready at $day/"
