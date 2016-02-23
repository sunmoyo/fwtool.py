from Crypto.Cipher import AES

# Sha1 keys for 1st gen firmware files
shaKey1 = '\x8D\xE5\xA8\x56\xD2\xEE\x76\xE0\x6C\x45\xDD\x9F\x57\x12\xC6\x3A\x0A\xDB\x05\xC1'
shaKey2 = '\xAF\x80\x8F\xC3\x97\x7B\x21\x87\x75\x22\x69\xDE\x83\xCC\xA6\xC6\x12\xF0\xDC\x49'

# AES key for 2nd & 3rd gen firmware files
cipherV2 = AES.AESCipher('\xE3\xB0\xC4\x42\x98\xFC\x1C\x14\x9A\xFB\xF4\xC8\x99\x6F\xB9\x24', AES.MODE_ECB)

# AES key for 3rd gen firmware files
cipherV3 = AES.AESCipher('\xE8\xB0\x88\x6D\x97\x18\x4F\x1F\x65\xC7\x67\xF7\x93\x99\x65\xBF', AES.MODE_ECB)

# Block sizes for different firmware file generations
blockSizeV1 = 1000
blockSizeV2 = 1024
blockSizeV3 = 1024
