# https://cryptopals.com/sets/1/challenges/1
from binascii import hexlify, unhexlify
from base64 import b64encode, b64decode


hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"


b64_str = b64encode(unhexlify(hex))

assert b64_str == b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
