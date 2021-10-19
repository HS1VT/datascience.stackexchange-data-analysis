#! /bin/bash
chmod a+x mapper3a.py reducer3a.py
cat Posts.xml | ./mapper3a.py | sort| ./reducer3a.py |more > answer.txt
cat Posts.xml | ./mapper3a.py | sort| ./reducer3a.py |more 
echo "It took $SECONDS seconds for this script to execute."

