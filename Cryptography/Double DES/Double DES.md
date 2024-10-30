# Double DES

## Problem Statement

I wanted an encryption service that's more secure than regular DES, but not as slow as 3DES... The flag is not in standard format. nc mercury.picoctf.net 33425 [ddes.py](./ddes.py)

## Information

**Category**: Cryptography

**Difficulty**: Hard

## Hints

1. How large is the keyspace?

## Solution

connecting to the server through the given command greets us with this message:
```
Here is the flag:
4eded8343b646ff22c2d9f2a0556494d85e572ea4e31229b710abc9593d234fc670a662bf135336a
What data would you like to encrypt? 
```
to which we are greeted with the encrypted flag, and the ability to encrypt our own data!

this is known as a [man-in-the-middle attack](https://en.wikipedia.org/wiki/Meet-in-the-middle_attack), where we are able to input our own plaintext and get the corresponding ciphertext in order to break the encryption!

the specific encryption used is [data encryption standard (DES)](https://en.wikipedia.org/wiki/Data_Encryption_Standard), which is applied twice, hence the problem name (assumed, but likely true)

encrypting our own plaintext, "3939", we get this response
```
What data would you like to encrypt? 3939
d3ff61995ec2481d
```

following [this explanation](https://security.stackexchange.com/questions/122624/how-does-the-meet-in-the-middle-attack-work-on-double-des) on how to crack double DES with a man in the middle attack, i wrote a [script](./solve.py) in order to decrypt the original flag.

printing the flag my script yields:
`b'af5fa5d565081bac320f42feaf69b405        '`
to which i grab the middle portion of 
```
af5fa5d565081bac320f42feaf69b405
```
as our key!

## Flag

af5fa5d565081bac320f42feaf69b405
