# Vigenere

## Problem Statement

Can you decrypt this message?
Decrypt this [message](./cipher.txt) using this key "CYLAB".

## Information

**Point Value**: ?

**Category**: Cryptography

## Hints

1. https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher

## Solution

Given that the text file given has contents
```
rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_2951c89f}
```
we know that the beginning characters likely should read picoCTF, decoded via vigenere cipher with key CYLAB.

Plugging it into [a website](https://cryptii.com/pipes/vigenere-cipher) and using key CYLAB alongside selecting the "Variant Beaufort cipher", we find the decipherable text of: `picoCTF{D0NT_US3_V1G3N3R3_C1PH3R_2951a89h}`

## Flag

picoCTF{D0NT_US3_V1G3N3R3_C1PH3R_2951a89h}
