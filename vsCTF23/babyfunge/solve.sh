#!/bin/sh

echo 'Generating codes...' >&2
./gen-codes.sh

echo 'Running hack...' >&2
{
	echo v #hack.sh skips the first character but we know it's 'v'
	./hack.sh
} |
tr -d '\n'
echo
