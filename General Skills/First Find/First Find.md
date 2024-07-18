# First Find

## Problem Statement

Unzip this archive and find the file named 'uber-secret.txt'
[Download zip file](./files.zip)

## Information

**Point Value**: 100 points

**Category**: General Skills

## Hints

(none)

## Solution

after downloading the zip file, we extract the contents to get a folder with various files.

using the `find` command to locate the file we run the command `file files -name uber-secret.txt` to get the output
```
files/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt
```

using cat on this filepath yields us the contents of `uber-secret.txt`!
```
picoCTF{f1nd_15_f457_ab443fd1}
```

## Flag
picoCTF{f1nd_15_f457_ab443fd1}