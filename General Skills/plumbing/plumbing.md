# plumbing

## Problem Statement

Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to `jupiter.challenges.picoctf.org 14291`


## Information

**Point Value**: 200 points

**Category**: General Skills

## Hints

1. Remember the flag format is picoCTF{XXXX}
2. What's a pipe? No not that kind of pipe... This [kind](http://www.linfo.org/pipes.html)

## Solution

in order to connect to the provided server and port, we use the `nc` command.

running `nc jupiter.challenges.picoctf.org 14291` yields a lot of text result, to which we need to parse for the flag!

piping the output the `nc` command through a `grep` to search for strings with picoCTF in it, we get the flag!

basically, the command `nc jupiter.challenges.picoctf.org 14291 | grep picoCTF` yields picoCTF{digital_plumb3r_ea8bfec7}

## Flag
picoCTF{digital_plumb3r_ea8bfec7}
