# GDB Test Drive

## Problem Statement

Can you get the flag?
Download this [binary](/gdbme).
Here's the test drive instructions:
```
$ chmod +x gdbme
$ gdb gdbme
(gdb) layout asm
(gdb) break *(main+99)
(gdb) run
(gdb) jump *(main+104)
```

## Information

**Category**: Reverse Engineering

**Difficulty**: Medium

## Hints

(None)

## Solution

after downloading the file, we use the provided commands to do a "test run" for gdb, and we are able to get the flag!
```
picoCTF{grep_is_good_to_find_things_f77e0797}
```

## Flag
picoCTF{grep_is_good_to_find_things_f77e0797}