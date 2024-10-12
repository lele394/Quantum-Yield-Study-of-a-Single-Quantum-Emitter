#!/bin/bash

python main.py

echo "Gold plate"
cd /home/leo/Desktop/OQA/Rsoft-project/data_ashar/gold_m
python python_code.py
echo
echo "Single nano antenna"
cd /home/leo/Desktop/OQA/Rsoft-project/data_ashar/one_gold
python python_code.py
echo
echo "Double nano antenna"
cd /home/leo/Desktop/OQA/Rsoft-project/data_ashar/two_gold
python python_code.py