from Cryptodome.Cipher import AES
from Cryptodome import Random
from Cryptodome.Util import Counter
import hashlib
from base64 import b64decode, b64encode



class AES_CTR:

    def __init__(self, key):
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self,plain_text):
        # Generate random iv eg: nonce as a series of bytes 
        iv = Random.get_random_bytes(12)
        # creating a counter block  : first arg is the length of counter value to be
        # concated with nonce(prefix). The length of both combined should be equal to 128 bits
        counter = Counter.new(32, prefix= iv)
        # create a cipher with ctr mode using the cointer object
        cipher = AES.new(self.key, AES.MODE_CTR, counter= counter)
        # encrypt
        encrypted = cipher.encrypt(plain_text.encode())
        
        return b64encode(iv + encrypted).decode() 

    def decrypt(self, encrypted_text):

        # decode from the b64encoding
        encrypted_text  = b64decode(encrypted_text.encode())
        # generate prepended iv from the e-text and cipher text
        iv  = encrypted_text[:12]
        cipher_text = encrypted_text[12:]
        # create counter object
        counter = Counter.new(32, prefix = iv )
        cipher = AES.new(self.key, AES.MODE_CTR, counter = counter)
        plain_text = cipher.decrypt(cipher_text)
        return plain_text.decode()  


      

        



