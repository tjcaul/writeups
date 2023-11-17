#!/bin/sh

mkdir -p codes

for i in $(seq 0 33); do
	{
		python3 -c "print('v'+' '*$i+'\"')"
		python3 -c "print('>'+' '*$i+'?,,')"
		python3 -c "print(' '+' '*$i+'\"')"
	} > codes/code$i
done
for i in $(seq 34 35); do #special case to prevent overlong lines
	{
		python3 -c "print('v'+' '*$i+'\"')"
		python3 -c "print('>'+' '*$((i-2))+',,?')"
		python3 -c "print(' '+' '*$i+'\"')"
	} > codes/code$i
done
