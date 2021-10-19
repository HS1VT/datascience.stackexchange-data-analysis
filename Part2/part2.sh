#! /bin/bash
sed -i 's/"/ /g' Badges.xml
awk '{print $7}' Badges.xml > output.txt
sort -u output.txt > Unique_Badges.txt
wc -w Unique_Badges.txt > No_Of_Unique_Badges.txt
cat output.txt | xargs -n1 | sort | uniq -c > Badge_Count.txt
echo "It took $SECONDS seconds for this script to execute."

