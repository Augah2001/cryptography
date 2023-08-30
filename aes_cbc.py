import hashlib
from Cryptodome.Cipher import AES
from Cryptodome import Random 
from base64 import b64encode, b64decode


class AES_algorithm:

  def __init__(self, key):
    self.key = hashlib.sha256(key.encode()).digest()
    self.block_size = AES.block_size

  # padding method using PKCS7
  def add_padding(self,plain_text):
    bytes_to_pad = self.block_size - len(plain_text) % self.block_size
    ascii_string = chr(bytes_to_pad)
    return plain_text + ascii_string * bytes_to_pad

  # remove padding
  def remove_padding(self, txt):
    last_char = txt[-1]
    return txt[:-ord(last_char)]  

  
  def encrypt(self, plain_text):
    plain_text = self.add_padding(plain_text)
    # generate initialization vector 
    iv = Random.new().read(self.block_size)
    # cipher object
    cipher = AES.new(self.key, AES.MODE_CBC,iv)
    encrypted_text = cipher.encrypt(plain_text.encode())
    # encode into transmittable format: base64
    return b64encode(iv+encrypted_text).decode()
    

  def decrypt(self,encrypted_text):
    # decode from base64 format
    encrypted_text = b64decode(encrypted_text)
    # regenerate initialization vector and cipher text from e-text
    iv = encrypted_text[:self.block_size]
    cipher_text = encrypted_text[self.block_size:]
    # create cipher object
    cipher = AES.new(self.key, AES.MODE_CBC, iv)
    plain_text = cipher.decrypt(cipher_text).decode()
    # remove padding
    unpadded_text = self.remove_padding(plain_text)
    return unpadded_text

  





