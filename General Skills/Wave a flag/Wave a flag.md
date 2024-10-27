# Wave a flag

## Problem Statement

Can you invoke help flags for a tool or binary? [This program](./warm) has extraordinarily helpful information...

## Information

**Point Value**: ?

**Category**: General Skills

## Hints

1. This program will only work in the webshell or another Linux computer.
2. To get the file accessible in your shell, enter the following in the Terminal prompt: `$ wget https://mercury.picoctf.net/static/b28b6021d6040b086c2226ebeb913bc2/warm`
3. Run this program by entering the following in the Terminal prompt: `$ ./warm`, but you'll first have to make it executable with `$ chmod +x warm`
4. -h and --help are the most common arguments to give to programs to get more information from them!
5. Not every program implements help features like -h and --help.

## Solution

running the `file` command on the file given to us, we get this result
```
warm: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=b11c22752c901adc13ba1ce86eda9d5516f22763, with debug_info, not stripped
```
which tells us that it is an [ELF binary](https://www.baeldung.com/linux/executable-and-linkable-format-file#elf) 

trying to run this file with `./warm` tells us we don't have sufficient permissions, so we change that with the `chmod` command as so:
```
chmod +x warm
```
to give us execute permissions

now properly executing the file, we receive a message telling us to use the -h flag, which yields the key!
```
Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_30e77291}
```


## Flag

picoCTF{us3l3ss_ch4ll3ng3_3xpl0it3d_3823}
