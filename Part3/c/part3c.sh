#! /bin/bash
chmod a+x mapper3c.py reducer3c.py
cat Posts.xml | ./mapper3c.py | sort| ./reducer3c.py |more
echo "It took $SECONDS seconds for this script to execute."

