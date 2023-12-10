#!/bin/bash

chr(){
	printf "\x$(printf '%x' $1)"
}

for last in $(seq 0 127); do
	chr $last
	for n in $(cat arr.txt); do
		dec=$(
			echo "obase=10; ibase=16; $(echo $n | tr a-f A-F)" | bc
		)
		c=$((dec-last))
		chr $c
		last=$c
	done
	echo
done
