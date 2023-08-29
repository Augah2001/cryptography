from Cryptodome.Cipher import AES
from Cryptodome import Random
import hashlib
from base64 import b64encode, b64decode


class AES_GCM:
    def __init__(self, key):
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, plain_text,):
        # generate the nonce. should be 96bit by convention
        nonce = Random.new().read(12)
        # create a GCM cipher
        cipher = AES.new(self.key, AES.MODE_GCM, nonce)
        # encrypt and generate a tag for authentication using GCM
        encrypted, tag = cipher.encrypt_and_digest(plain_text.encode())
        #  concatenate the plain text, tag and nonce and return them

        return b64encode(cipher.nonce + tag + encrypted).decode()


aes_instance = AES_GCM('PASSWORD123')

print(aes_instance.encrypt('Hello World'))
