#!/bin/bash

for i in data/*
do

	if test -f "$i"
	then
		echo "processing $0"
		cat "$i" | python clean_data.py >> Processed_data.txt
		echo "process $0 done"
	fi
done
