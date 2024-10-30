# ReadMyCert

## Problem Statement

How about we take you on an adventure on exploring certificate signing requests
Take a look at this CSR file [here](./readmycert.csr).

## Information

**Category**: Cryptography

**Difficulty**: Medium

## Hints

1. Download the certificate signing request and try to read it.

## Solution

given the hint, trying to open the file using a text editor yields a code.

trying to open this file using a took like [openssl](https://linux.die.net/man/1/openssl), to get information about the .csr file, will allow us to get more information about the certificate.

running the command:
```
openssl req -text -in readmycert.csr 
```
yields this response:
```
Certificate Request:
    Data:
        Version: 1 (0x0)
        Subject: CN=picoCTF{read_mycert_57f58832}, name=ctfPlayer
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
               ...
```
where we can see the flag as the subject!

## Flag

picoCTF{read_mycert_57f58832}
