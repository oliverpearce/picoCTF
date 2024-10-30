#!.venv/bin/python
from Crypto.Cipher import DES
import binascii

# pad function taken from ddes.py
def pad(msg):
    block_len = 8
    over = len(msg) % block_len
    pad = block_len - over
    return (msg + " " * pad).encode()

# converts hex string to binary string
encrypted_flag = binascii.unhexlify("4eded8343b646ff22c2d9f2a0556494d85e572ea4e31229b710abc9593d234fc670a662bf135336a")

# my plaintext: 3939 -> pad the binary string to be used later
my_plaintext = pad(binascii.unhexlify("3939").decode())

# returned ciphertext: 681a8366f637b9b9 -> get binary to use later
my_ciphertext = binascii.unhexlify("d3ff61995ec2481d")

# brute force first encryption (encrypting to find XXX)
encryption_dict = {}
print("brute forcing first encryption...")
for key in range(999999):
    # pad the key as a string
    key = pad(str(key))
    cipher1 = DES.new(key, DES.MODE_ECB)
    ciphertext1 = cipher1.encrypt(my_plaintext)
    encryption_dict[ciphertext1] = key
print("\tdone!")

print("brute forcing second encryption...")
# brute force second encryption (decrypting to find XXX)
decryption_dict = {}
for key in range(999999):
    # pad the key as a string
    key = pad(str(key))
    cipher2 = DES.new(key, DES.MODE_ECB)
    ciphertext2 = cipher2.decrypt(my_ciphertext)
    decryption_dict[ciphertext2] = key
print("\tdone!")

# find the intersection between the two dicts (by using sets) and then that is the secret key!
encrypt_set = set(encryption_dict)
decrypt_set = set(decryption_dict)
print("finding intersection between both dicts...")

# this key is the XXX that is in both dictionaries! (all keys are in binary)
for key in encrypt_set.intersection(decrypt_set):
    print(f"intersection found: {key}")
    key1 = encryption_dict[key]
    key2 = decryption_dict[key]

print(f"key1 is: {key1}")
print(f"key2 is: {key2}")

# create both DES and decipher flag with it
cipher_round_1 = DES.new(key1, DES.MODE_ECB)
cipher_round_2 = DES.new(key2, DES.MODE_ECB)

# decrypt flag
almost_flag = cipher_round_2.decrypt(encrypted_flag)
flag = cipher_round_1.decrypt(almost_flag)
print(f"flag is: {flag}")
