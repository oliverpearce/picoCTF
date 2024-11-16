# Wireshark twoo twooo two twoo... 

## Problem Statement

> Can you find the flag? [shark2.pcapng](./shark2.pcapng).

## Information

**Category**: Forensics

**Difficulty**: Medium

## Hints

1. Did you really find _the_ flag?
2. Look for traffic that seems suspicious.

## Solution

opening the file with wireshark, we are able to see a bunch of packets, some of which easily contains flags with the picoCTF format!

however, these flags are not real, and looking at the hints tell us that we should look for other suspicious traffic. finding dns packets that go to \[some text]reddshrimptandherring.com, we can filter them using this command:

```dns && ip.dst==8.8.8.8 && dns.qry.name contains local```

looking at all of these packets we look at the text before the url, which looks suspiciously like a base64 string!

sending the concatenations of these segments
(`cGljb0NURntkbnNfM3hmMWxfZnR3X2RlYWRiZWVmfQ==`) through a [decoder](https://www.base64decode.org/), we are able to get the flag!

## Flag

picoCTF{dns_3xf1l_ftw_deadbeef}














