#! /bin/bash
chmod a+x mapper4.py reducer4.py 
cat Comments.xml | ./mapper4.py| sort| ./reducer4.py| more
echo "It took $SECONDS seconds for this script to execute."
