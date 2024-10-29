# what's a netcat?

## Problem Statement

Using netcat (nc) is going to be pretty important. Can you connect to jupiter.challenges.picoctf.org at port 64287 to get the flag?

## Information

**Point Value**: ?

**Category**: General Skills

## Hints

1. nc [tutorial](https://linux.die.net/man/1/nc)

## Solution

looking at the page given to us in the hints, we learn that using the `nc` command with the `-p` flag allows us to specify a port to connect to.

running the command
```
nc jupiter.challenges.picoctf.org 64287
```
connects us to the given server at the correct port, returning this message
```
You're on your way to becoming the net cat master
picoCTF{nEtCat_Mast3ry_284be8f7}
```

## Flag

picoCTF{nEtCat_Mast3ry_284be8f7}
