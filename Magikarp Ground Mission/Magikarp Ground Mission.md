# Magikarp Ground Mission

## Problem Statement

Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin. Login via `ssh` as `ctf-player` with the password, `481e7b14`

## Information

**Point Value**: 30 points

**Category**: General Skills

## Hints

1. Finding a cheatsheet for bash would be really helpful!

## Solution

using the provided command `ssh ctf-player@venus.picoctf.net -p 54585` to ssh into ctf-player, and after entering the password `481e7b14`, we gain access to the server! 

using the `ls` command, we find a file called `1of3.flag.txt` which has the contents 
```
picoCTF{xxsh_
```

following the instructions in `instructions-to-2of3.txt`, we go to the root directory using `cd /` 
and print the contents of `2of3.flag.txt` giving us
```
0ut_0f_\/\/4t3r_
```

finally, following the instructions in `instructions-to-3of3.txt`, we go to the home directory using `cd ~` and print the contents of `3of3.flag.txt`!
```
1118a9a4}
```

## Flag
picoCTF{xxsh_0ut_0f_\/\/4t3r_1118a9a4}
