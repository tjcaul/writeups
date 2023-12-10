# Great Old Talisman
From University CTF 2023: Brains & Bytes. Solution by tjcaul.

## Problem
We have a binary that takes in a number (supposed to be 0 or 1, but we can
input whatever we want, of course), interprets the number as an offset
multiplied by 8 bytes, then read two characters into the resulting address.
We can even use negative offsets, so that means arbitrary write access.
However, NX is enabled, so no shellcodes *or* patching here. And for extra
fun, `main()` ends with `exit()` right after the read instead of returning
like a nice function. That means no overwriting the return address, either.

## Solving
A quick `info proc mappings` in gdb shows us that one interesting mapping
is writeable. A look into that mapping shows it holds the `talis` object
(the thing the program is *supposed* to modify) and... the GOT.
A [helpful tutorial][1] made understanding and modifying the GOT effortless.
Overwriting `exit`'s entry with `main` let me call `main` recursively, so I
could change as many bytes as I wanted. I spent a couple of hours trying to
figure out how to read the flag or get a shell when I can only overwrite the
two least significant bytes in any qword, until I found it: `read_flag`.
Abbreviated `radare2` session documenting the discovery:
```
> aaaa
> s sym.imp.^I
...
sym.imp.open
> axt sym.imp.open
sym.read_flag 0x401389 [CALL] call sym.imp.open
```
All I had to do was call the function. Duh.

The lesson: CTFs aren't real life. Sometime's there's a `win` function.

## Solution
1. Find the address of `read_flag`
2. Find the address of the GOT entry for `exit`
3. Find the address of the `talis` object (it's in the `read()` call in `main`)
4. Calculate `(got.exit - &talis) / 8) = -4`
5. Send `-4`, then the last two bytes of `read_flag` (reversed)


[1]: https://www.exploit-db.com/papers/13203
