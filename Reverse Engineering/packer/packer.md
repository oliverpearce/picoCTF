# packer

## Problem Statement

Reverse this linux executable?
[binary](./out)

## Information

**Point Value**: -

**Category**: Reverse Engineering

## Hints

1. What can we do to reduce the size of a binary after compiling it.

## Solution

with the given file, we first want to check what type of file it is using `file out`.
nothing seems out of the ordinary, so we move on to trying to see if the file has any "human readable" data.

using `strings out` to print all the readable strings in the binary, we find some strange line amidst the output: 
```
$Info: This file is packed with the UPX executable packer http://upx.sf.net $
$Id: UPX 3.95 Copyright (C) 1996-2018 the UPX Team. All Rights Reserved. $
``` 

one google later, we find out that UPX is an [executable file compressor](https://upx.github.io/). 
we uncompress the file with `upx -d out`, and checking the new file with `strings out` shows us that the file was uncompressed!

...


```
picoCTF{f1nd_15_f457_ab443fd1}
```

## Flag
picoCTF{f1nd_15_f457_ab443fd1}