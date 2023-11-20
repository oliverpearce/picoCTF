# First Grep

## Problem Statement

Can you find the flag in [file](./file)? This would be really tedious to look through manually, something tells me there is a better way.

## Information

**Point Value**: 100 points

**Category**: General Skills

## Hints

1. grep [tutorial](https://ryanstutorials.net/linuxtutorial/grep.php)

## Solution

after downloading the file, we use cat to first print the contents to the screen, and pipe that output through grep, which is able to search for substrings!

using the `|` character to represent piping output from one function as input to another, running `cat file | grep picoCTF` yields 
```
picoCTF{grep_is_good_to_find_things_f77e0797}
```

## Flag
picoCTF{grep_is_good_to_find_things_f77e0797}