#!/usr/bin/env bash

# expect the log file to be in the same dir
# and to have the number of day on the first line
nb=$(head -n 1 ./log.md) 
# increase number of days
((nb++))
# replace number of days in the file
sed -i "1s/.*/$nb/" ./yeet
dateOfTheDay=$(date +%Y-%m-%d)
echo -e "\n# day $nb: $dateOfTheDay\n\n" >> ./log.md

