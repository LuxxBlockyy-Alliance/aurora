#!/bin/bash

sudo rm -r "aurora"

git clone https://github.com/LuxxBlockyy-Alliance/aurora.git

echo ""
echo "--------------------- Starting Aurora ---------------------"
echo ""

python3 aurora/run.py

