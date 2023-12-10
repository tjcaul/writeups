# WindowsOfOpportunity
From University CTF 2023: Brains & Bytes. Solution by tjcaul.

## Problem
A simple reversing chall. We just need to find the key that unlocks the binary
and submit it as a flag. There are multiple possible flags, but the right one
should be of the form `HTB{.*}`.

## Solving
`r2dec` produced a decent decompilation of `main`. After manually fixing up the
produced C program, the algorithm was obvious: the sum of every pair of
characters (`k[0] + k[1], k[1] + k[2], ...`) had to match the corresponding
value in a hard-coded array.

## Solution
1. Dump the hard-coded array and clean the dump into a series of hex bytes
2. Run `keygen.sh`
3. Try a key: it works
4. grep the keys for one starting with `HTB`
