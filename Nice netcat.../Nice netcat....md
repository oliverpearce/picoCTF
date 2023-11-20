# Nice netcat...

## Problem Statement

There is a nice program that you can talk to by using this command in a shell: `$ nc mercury.picoctf.net 22342`, but it doesn't speak English...

## Information

**Point Value**: 15 points

**Category**: General Skills

## Hints

1. You can practice using netcat with this picoGym problem: [what's a netcat?](https://play.picoctf.org/practice/challenge/34)
2. You can practice reading and writing ASCII with this picoGym problem: [Let's Warm Up](https://play.picoctf.org/practice/challenge/22)

## Solution

according to the instructions, we run the command `nc mercury.picoctf.net 22342`, which yields the following result
```
112 
105 
99 
111 
67 
84 
70 
123 
103 
48 
48 
100 
95 
107 
49 
116 
116 
121 
33 
95 
110 
49 
99 
51 
95 
107 
49 
116 
116 
121 
33 
95 
53 
102 
98 
53 
101 
53 
49 
100 
125 
10 
```

converting this into letters using an [ascii-text converter](https://www.duplichecker.com/ascii-to-text.php), we get the result
```
picoCTF{g00d_k1tty!_n1c3_k1tty!_5fb5e51d}
```

## Flag
picoCTF{g00d_k1tty!_n1c3_k1tty!_5fb5e51d}
