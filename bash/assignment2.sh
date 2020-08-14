#!/bin/bash

#Name  : Md.Rafiuzzaman Khan
#ID    : 011161017
#Batch : CSE 45
file='result.txt'

#Declaring an associative array
declare -A resultArray

n=0
while read line;
do
# reading each line
if [ $n -gt 0 ] #ignoring the first line

then
	#Getting the cgpa from end of the line
	CGPA=$(echo "$line" | rev | cut -d" " -f1  | rev )

	Info=$( echo "$line" | cut -d' ' -f2- | sed 's/ *$//g')

	if [ ! -z "$line" ] # ignoring empty lines
    then

       resultArray+=(["$CGPA"]=$Info)

    fi

fi

n=$((n+1))

done < $file