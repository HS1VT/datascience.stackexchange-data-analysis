#! /bin/bash
chmod a+x mapper3b.py reducer3b.py
cat Posts.xml | ./mapper3b.py | sort| ./reducer3b.py |more  
echo "It took $SECONDS seconds for this script to execute."

