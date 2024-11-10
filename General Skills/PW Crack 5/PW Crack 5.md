# PW Crack 5

## Problem Statement

> Can you crack the password to get the flag?
> Download the password checker [here](./level5.py) and you'll need the encrypted [flag](./level5.flag.txt.enc) and the [hash](./level5.hash.bin) in the same directory too. Here's a [dictionary](./dictionary.txt) with all possible passwords based on the password conventions we've seen so far.

## Information

**Category**: General Skills

**Difficulty**: Medium

## Hints

1. Opening a file in Python is crucial to using the provided dictionary.
2. You may need to trim the whitespace from the dictionary word before hashing. Look up the Python string function, `strip`
3. The `str_xor` function does not need to be reverse engineered for this challenge.

## Solution

Given the files, notably the `level5.py script`, we recognize that we have to find the correct password that matches with the hash in order to get the flag!

given the dictionary of potential passwords, we write some code (in level5.py) to read each line of the dictionary file and test if that password is correct--to which we are eventually able to find our flag with the response:
```
Welcome back... your flag, user:
picoCTF{h45h_sl1ng1ng_40f26f81}
```

## Flag

picoCTF{h45h_sl1ng1ng_40f26f81}
