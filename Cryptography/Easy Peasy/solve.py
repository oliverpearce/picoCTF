#!.venv/bin/python
from Crypto.Cipher import DES
import binascii

# converts hex string to binary string
encrypted_flag = binascii.unhexlify("0345376e1e5406691d5c076c4050046e4000036a1a005c6b1904531d3941055d")

# my plaintext: 3939 -> pad the binary string to be used later
my_plaintext = binascii.unhexlify("3939").decode()

# returned ciphertext: 681a8366f637b9b9 -> get binary to use later
my_ciphertext = binascii.unhexlify("6f410a58")

# brute force all possible OTPs
# TODO
