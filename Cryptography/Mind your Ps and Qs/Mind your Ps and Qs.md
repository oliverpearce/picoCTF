# Mind your Ps and Qs

## Problem Statement

In RSA, a small e value can be problematic, but what about N? Can you decrypt this? values

## Information

**Category**: Cryptography

**Difficulty**: Medium

## Hints

1. Bits are expensive, I used only a little bit over 100 to save money

## Solution

the values given are as follows;
```
Decrypt my super sick RSA:
c: 8533139361076999596208540806559574687666062896040360148742851107661304651861689
n: 769457290801263793712740792519696786147248001937382943813345728685422050738403253
e: 65537
```

putting these numbers into a decrypter such as [this website](https://www.dcode.fr/rsa-cipher) yields the flag:
```
picoCTF{sma11_N_n0_g0od_45369387}
```

This can also be solved with a python tool such as [RsaCtfTool](https://github.com/RsaCtfTool/RsaCtfTool)

## Flag

picoCTF{sma11_N_n0_g0od_45369387}
