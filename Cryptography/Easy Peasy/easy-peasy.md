# Easy Peasy

## Problem Statement

> A one-time pad is unbreakable, but can you manage to recover the flag? (Wrap with picoCTF{}) ```nc mercury.picoctf.net 58913``` [otp.py](./otp.py)

## Information

**Category**: Cryptography

**Difficulty**: Medium

## Hints

1. Maybe there's a way to make this a 2x pad.

## Solution

the description specifies that it is a [one-time pad](./https://en.wikipedia.org/wiki/One-time_pad), and we can recognize that the attached script is what runs when we connect to the server.

we can use a man-in-the-middle attack to break this, as one time pad is only secure for one encryption, not multiple!

using our own plaintext of "3939", we get this response:
```
What data would you like to encrypt? 3939
Here ya go!
6f410a58
```

... to be continued

## Flag
picoCTF{grep_is_good_to_find_things_f77e0797}