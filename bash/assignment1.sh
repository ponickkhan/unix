#!/bin/bash

#Name : Md.Rafiuzzaman Khan
#ID   : 011161017
#Batch: CSE 45


    echo Find Common Word In Two Text Of Multiple Word
    echo "------------------First Text---------------------"

    # Ask the user for first text
    echo Enter First Text:
    read text1

    echo "------------------Second Text--------------------"
    # Ask the user for second text
    echo Enter Second Text:
    read text2
    echo "=====================Result======================"

       # Set space as the delimiter
	IFS=' '

	#Read the split words into an array based on space delimiter
	read -a string_array <<< "$text1"

        # Print each matching value of the array by using the loop
	for val in "${string_array[@]}";
	do
	if [[ "$text2" == *" $val"* ]]; then
         echo "$val"
        fi
	done