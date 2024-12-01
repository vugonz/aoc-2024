#! /bin/bash

set -e

if [ $# -eq 0 ]; then
    day=$(date +%d | sed 's/^0*//')
else 
    day=$1
fi

echo $day

if [[ ! $day =~ ^[0-9]+$ ]] || [ ! $day -ge 1 ] || [ ! "$day" -le 25 ]; then
    echo "Invalid day"
    exit
fi

mkdir -p $day

source .env
curl -sH "Cookie: session=$SESSION" https://adventofcode.com/2024/day/$day/input -o ./$day/input.txt

echo "All ready at $day/"