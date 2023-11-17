# babyfunge
From vsCTF 23. Solution by tjcaul.

## Problem
Modified befunge interpreter running on a network port.
The program executed is our three lines of input + a line of `@` + the flag.
`@` terminates the program in befunge, so we have to somehow get around it and
print the flag.

### Extra restrictions
- The usual code modification instructions have been removed
- We are allowed to enter only 7 instructions
- We are allowed to execute only 100 instructions
- Out code is limited to a 37*3 board

## Solving
It turns out the interpreter still allows two helpful instructions:
`#` (skip next instruction) and `"` (push the following chars to the stack).
Also, the interpreter's coordinate system is messed up and goes out of bounds
(classic `if x <= len(array)`). Execution is supposed to wrap around the board,
but this bug makes it crash when it hits the edge...unless we hit the negative
edge. Negative indexing for the win!
So all we have to do is start a quote, run execution over the `@` and the flag
char, end the quote, and print the chars with `,`.
With only 3 lines, that's actually tricky, but the `?` operator (redirect exec
in a random direction) saved the day. 2 out of 9 times (have fun with the
recursive probability equation!), it the program does the right thing and
prints `@c` or `c@`. Exploit: written. Also, with the magic of befunge, we can
move it around to select different characters.

## Solution
1. Write befunge code to exflitrate a character of the flag (see above)
2. Write shell program to try it until it works (randomness, remember?)
3. Generate all positions of the code to select all characters
4. Write shell script to run each code sequentially and get each character
5. Get frustrated because `*` in Bash doesn't order files numerically, fix that
6. Write edge case befunge codes for literal EDGE cases
7. Run, wait, and concatenate
