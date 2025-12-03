# Advent of code 2025

This year, I decided to post my solutions to my GH. \
The assignments are from [Advent of code 2025](https://adventofcode.com/2025)

## Day 1
[assignment](https://adventofcode.com/2025/day/1)
### Part 1
For this I implemented a simple counting approach. Nothing special really.
### Part 2
I did not manage to get the counting approach to work so i decided on bruteforce. Not the cleanest, I know, but it still runs in under a second even in python.

## Day 2

### Part 1

For this day I used a regex formula to find the repeating pattern. The regex establishes a group of however many digits and then references that group immediately using the `\<group num>` notation. I bashed my head against the wall as my code overcounted (it later turned out that it overcouned by millions of entries). After I realized that i was only supposed to include entries that were only a repeated sequence of characters and have no other chars the regex worked fine. So I had the regex developed and now i just needed the data to let it shread through. I decided the best approach was just to 'unwrap' the intervals into a huge text file (2259342 lines to be exact) and run the regex in line mode.

### Part 2

For part 2 I literally just added a single `+` character to my regex formula to reference the group more than once

## Day 3

### Part 1

I was stumped a bit at first and did not know what to do with the problem. Then i realized that it was just about taking two `max` operations on the numbers in the banks. The code finds the max number in the bank in any place except the last spot (because that couldn't be the start of a 2 digit number). Then, it looked for the second max value, but this time it cut off all numbers before and including the first instance of the number i had just found \

\

so `1119012345` would find 9 as the largest and then search for the other max in `012347` and find 7, thus resulting in 97

### Part 2

This part required 12 numbers instead of 2, so I generalized the algorythm for all possible values. It still does the find max (excluding any spots too far to the right), cut the left side approach, it just did it in a loop and decreased the right exclusion zone.