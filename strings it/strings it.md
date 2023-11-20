# strings it

## Problem Statement

Can you find the flag in [file](./strings) without running it? 

## Information

**Point Value**: 100 points

**Category**: General Skills

## Hints

1. [strings](https://linux.die.net/man/1/strings)

## Solution

Downloading the file named strings, we can use the `strings` command to print the printable characters in the file.

 In order to parse through the file, we use grep to search for the substring `picoCTF`, as that will be our flag!

running `strings strings | grep picoCTF` yields the result
```
picoCTF{5tRIng5_1T_d66c7bb7}
```
and thus our flag is found!

## Flag

picoCTF{5tRIng5_1T_d66c7bb7}