#! /bin/bash
chmod a+x mapper7.py reducer7.py
chmod a+x mapper8.py
cat PostHistory.xml | ./mapper7.py |sort | ./reducer7.py | more > out_UserId.txt
cat Users.xml | ./mapper8.py | more > out_rep.txt
python3 q5.py
echo "It took $SECONDS seconds for this script to execute."
