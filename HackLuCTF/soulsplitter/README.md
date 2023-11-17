# soulsplitter
From Hack.lu CTF 2023. Solution by tjcaul.
 
## Problem
A secret is turned into a QR code, split into shards, encoded as text, zlib
compressed, then printed in base64. Our goal is to recover 20 secrets and send
them back to the server, at which point we receive a flag. For extra
difficulty, we only get 16 of the 17 shards.

## Solving
This was really just a programming chall. The tricky part was scanning the incomplete codes. Since QR codes have error correction and the ones in the chall were
turned up to the max, we don't have to worry about the missing data, but it was
necessary to fix the corner marker boxes. The solution doesn't have a 100%
success rate, but it's good enough to make it through all 20 in a few tries.

## Solution
1. Read the shards, decompress
2. Wrangle each shard into an array (each char represents multiple atoms)
3. OR the shards together to produce a QR code
4. Repair the corner markers
5. Scan the code
6. Send the code to the server
