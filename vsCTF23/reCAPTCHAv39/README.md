# reCAPTCHA v39
From vsCTF 23. Solution by tjcaul.

## Problem
Solve 100 CAPTCHAs that are tricky for a human--in 5 seconds each.
Specifically, find area of the image that's shaded. Because the shading's not
all black pixels, it was harder to differentiate (programatically) between
shaded and non-shaded.

## Solving
I tried some rudimentary edge detection and even considered writing a 'sliding
line' algorithm to find the corners, but realized that very few of the pixels
inside the shape were the same colour as the background. I used Python for the
first time ever for a CTF challenge, and it made life so much easier than shell
or C.

## Solution
1. Load image as array
2. Extract red channel (all channels were the same anyways)
3. Make all non-background-colour pixels pure black and background-colour
pixels white
4. Blacken all white pixels with few neighbours
5. Count number of black pixels
6. Divide by total pixels, multiply by area
7. Put it in a loop and connect stdout to clipboard with a shell script

## Running the solution
I couldn't be bothered to interface with the site programatically, so:
1. Start `solve.sh`
2. Start game
3. Drag image into Finder
4. `solve.(py|sh)` deletes image and puts area in clipboard
5. Paste into text box in game
6. GOTO 1 within 5 seconds
7. Restart `solve.sh` when it crashes, clean up the mess within 5 seconds
8. Heart rate go brrr
