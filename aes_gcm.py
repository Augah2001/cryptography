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

    def decrypt(self, encrypted_text):
        # decode encrypted text from transmittable b64encoding
        encrypted_text = b64decode(encrypted_text.encode())
        # generate nonce, tag and cipher_text from e-text
        nonce = encrypted_text[:12]
        tag = encrypted_text[12:28]
        cipher_text = encrypted_text[28:]
        # new cipher object
        cipher = AES.new(self.key, AES.MODE_GCM, nonce)
        # decrypt and verify the auth tags
        try: 
            plain_text = cipher.decrypt_and_verify(cipher_text,tag)
            return plain_text.decode()
        except ValueError:
            ValueError('Decryption failed or authentication tag mismatch')     



