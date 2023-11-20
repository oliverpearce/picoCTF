# useless

## Problem Statement

There's an interesting script in the user's home directory
The work computer is running SSH. We've been given a script which performs some basic calculations, explore the script and find a flag.
Hostname: saturn.picoctf.net
Port:     59562
Username: picoplayer
Password: password

## Information

**Point Value**: 100 points

**Category**: General Skills

## Hints

(none)

## Solution

Using the information given to us in the instructions, we can ssh into the server using the following command:
```ssh saturn.picoctf.net -l picoplayer -p 59562```

and then entering `password` as the password gives us access to the "work computer"!

running the script file in the home directory yields the result `Read the code first`, which we then use `cat` to print the contents of the file to the console.

reading through the code, we find this nugget of information: 
```
else
	  echo "Read the manual"
```
using `man useless` yield the man page, and under the authors section we are able to find the flag!

```
Authors
     This script was designed and developed by Cylab Africa

     picoCTF{us3l3ss_ch4ll3ng3_3xpl0it3d_3823}
```

## Flag

picoCTF{us3l3ss_ch4ll3ng3_3xpl0it3d_3823}
