# rotation

## Problem Statement

You will find the flag after decrypting this file
Download the encrypted flag [here](./encrypted.txt).

## Information

**Point Value**: ?

**Category**: Cryptography

## Hints

1. Sometimes rotation is right

## Solution

Given that the text file given has contents
```
xqkwKBN{z0bib1wv_l3kzgxb3l_949in1i1}
```
we know that the beginning characters likely should read picoCTF, by a rotation by a certain amount.

Plugging it into [a website](https://cryptii.com/pipes/caesar-cipher) and trying out different rotation shifts (brute-forcing it), we find that a rotation of 18 gives us the decipherable text of:
`picoCTF{r0tat1on_d3crypt3d_949af1a1}`

## Flag

picoCTF{r0tat1on_d3crypt3d_949af1a1}
