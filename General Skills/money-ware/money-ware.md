# money-ware

## Problem Statement

Flag format: picoCTF{Malwarename}
The first letter of the malware name should be capitalized and the rest lowercase.
Your friend just got hacked and has been asked to pay some bitcoins to 1Mz7153HMuxXTuR2R1t78mGSdzaAtNbBWX. He doesn’t seem to understand what is going on and asks you for advice. Can you identify what malware he’s being a victim of?

## Information

**Point Value**: 100 points

**Category**: General Skills

## Hints

1. Some crypto-currencies abuse databases exist; check them out!
2. Maybe Google might help.

## Solution

according to the first hint, it says that crypto-currency abuse databases exist, to which I found
[chainabuse](https://www.chainabuse.com/) on google!

putting in the `1Mz7153HMuxXTuR2R1t78mGSdzaAtNbBWX` address yields numerous reports, and looking through the reports we find the last one to be "More information here: https://blog.avira.com/petya-strikes-back/"!

following this link, we find that the ransomware is petya, and inputting the flag in accordance to the instructions we get `picoCtf{Petya}`.

## Flag

picoCTF{Petya}