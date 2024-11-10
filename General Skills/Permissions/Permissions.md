# Permissions

## Problem Statement

> Can you read files in the root file?
The system admin has provisioned an account for you on the main server:
`ssh -p 54590 picoplayer@saturn.picoctf.net`
Password: `vCR2tuwCRm`
Can you login and read the root file?

## Information

**Category**: Forensics

**Difficulty**: Medium

## Hints

1. What permissions do you have?

## Solution

once logging in with the provided credentials, we run the command `sudo -l` to see what we are allowed to execute!

given that we are able to run the `vi` command as root, we can use this to escalate our privileges, through running `sudo vi gimme` and typing the following text:
```
:!/bin/bash
```
which allows us to run the bash terminal with the privileges of the root user!

after getting root access (which you can check with the `whoami` command), we navigate to the `/root` directory and run `ls -la` to see all the contents, to which we find a `.flag.txt`

the contents of the file are the flag, which is
```
picoCTF{uS1ng_v1m_3dit0r_ad091ce1}
```

## Flag

picoCTF{uS1ng_v1m_3dit0r_ad091ce1}
