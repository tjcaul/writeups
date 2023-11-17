#!/bin/sh

normal_output="Line 1: Line 2: Line 3: "

run_code(){
	for l in $(seq 1 3); do
		sed -n ${l}p $1
		sleep 0.1 #The chall expects a delay between lines
	done |
	nc vsc.tf 3093
	echo
}

solve_code(){
	while :; do
		out="$(run_code $1)"
		if ! echo "$out" | grep -E "^$normal_output\$" >/dev/null; then
			echo $out |
			sed "s/$normal_output//" |
			tr -d @
			break
		fi
	done
}

if [ -n "$1" ]; then
	echo '"""'
	cat $1
	echo '"""'
	solve_code $1
else
	for i in $(seq 0 38); do
		solve_code codes/code$i
	done
fi
