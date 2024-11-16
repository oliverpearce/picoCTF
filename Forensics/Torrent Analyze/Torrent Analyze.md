# Torrent Analyze

## Problem Statement

> SOS, someone is torrenting on our network.
One of your colleagues has been using torrent to download some files on the company’s network. Can you identify the file(s) that were downloaded? The file name will be the flag, like `picoCTF{filename}`. [Captured traffic.](./torrent.pcap)

## Information

**Category**: Forensics

**Difficulty**: Medium

## Hints

1. Download and open the file with a packet analyzer like [Wireshark](https://www.wireshark.org/).
2. You may want to enable BitTorrent protocol (BT-DHT, etc.) on Wireshark. Analyze -> Enabled Protocols
3. Try to understand peers, leechers and seeds. [Article](https://www.techworm.net/2017/03/seeds-peers-leechers-torrents-language.html)
4. The file name ends with `.iso`

## Solution

using wireshark, we are able to look through the provided [pcap file](./torrent.pcap), to which we specifically look for the downloaded files. As given in the hints, we need to enable the BitTorrent protocol if it isn't enabled already, and we limit our search to BT-DHT packets. 

after doing this, we search for the string "pico" in all of these packets, and find a packet with the `info_hash` of `e2467cbf021192c241367b892230dc1e05c0580e`. Since this info_hash is consistent across many of the torrent packets, this is likely due to the download of a file! Searching this hash online, we are able to find out that it is in reference to `ubuntu-19.10-desktop-amd64.iso`, which is our answer! 

## Flag

picoCTF{ubuntu-19.10-desktop-amd64.iso}
