# BioBundle
From University CTF 2023: Brains & Bytes. Solution by tjcaul.

## Problem
We have a reversing chall in which the key checking algorithm is loaded from
an external dynamic library, only the library isn't linked and doesn't exist.

## Solving
`r2dec` + manual cleanup of the C code results in a pretty simple program.
It loads a function `_` from a handle (produced by `get_handle()`), reads
a key, then calls `_` to check the key.
The interesting part is `get_handle`. It creates an anonymous file in memory,
XOR-decrypts a block of data into it, then *loads it as a dynamic library*.
All we have to do is dump the data, decrypt it ourselves with the simple key
`0x37`, and analyze it. Sure enough, it's a dynamic library with a `_`
function. Printing the disassembly in radare2 shows the fragments of the flag,
so we don't even need to reverse the function.

## Solution
1. Dump `0x3e07` bytes at `0x4080`
2. Clean up the dump into a format that's easy to work with in Python
3. XOR-decrypt it with key `0x37`
4. Convert it back into a real file with `xxd -r`
5. Analyze it in radare2
