# HashingJobApp

## Problem Statement

If you want to hash with the best, beat this test!
Additional details will be available after launching your challenge instance.

## Information

**Point Value**: ?

**Category**: General Skills

## Hints

1. You can use a commandline tool or web app to hash text
2. Press Ctrl and c on your keyboard to close your connection and return to the command prompt.

## Solution

After launching the instance, we connect using the given command
```
nc saturn.picoctf.net 54955
```
and we are greeted with this message:
```
Please md5 hash the text between quotes, excluding the quotes: 'Hawaii'
```

Using tools like [this website](https://www.md5hashgenerator.com/) we continually copy and paste the codes to get the corresponding md5 hashes:
`Hawaii` -> `a85df3d66bde576d3b62caaf527f2daa`

`angry hornets` -> `456fdc871d3f9976046da83bcfdd52ff`

`having a baby` -> `e215dac50d263755ea60abc80a0f3437`
and finally are greeted with the message
```
picoCTF{4ppl1c4710n_r3c31v3d_674c1de2}
```

## Flag

picoCTF{4ppl1c4710n_r3c31v3d_674c1de2}
