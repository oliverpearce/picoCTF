# Tab, Tab, Attack

## Problem Statement

Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames: [Addadshashanammu.zip](./Addadshashanammu.zip)

## Information

**Point Value**: 20 points

**Category**: General Skills

## Hints

1. After `unzip`ing, this problem can be solved with 11 button-presses...(mostly Tab)...

## Solution

after downloading and unzipping the file, like the problem statement suggets, its a lot of using tab to autocomplete the file names. After continually using `cd` and pressing tab to autocomplete the directory name, we eventually stumble upon a file named `fang-of-haynekhtnamet`. 

using `file` to check what kind of file it is (ELF 64-bit LSB pie executable), we can simply use `strings` with a `grep` for picoCTF in order to get our flag! Using the command `strings fang-of-haynekhtnamet | grep picoCTF` yields 

```
*ZAP!* picoCTF{l3v3l_up!_t4k3_4_r35t!_f3553887}
```

## Flag

picoCTF{l3v3l_up!_t4k3_4_r35t!_f3553887}