#!/bin/sh

python3 xor.py < dump.hex > dump-xor.hex
xxd -ps -r < dump-xor.hex > dump-xor.bin
