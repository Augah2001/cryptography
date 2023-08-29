import hashlib
from Cryptodome.Cipher import AES
from Cryptodome import Random 
from base64 import b64encode, b64decode


class AES_algorithm:

  def __init__(self, key):
    self.key = hashlib.sha256(key.encode()).digest()
    self.block_size = AES.block_size

  def add_padding(self,plain_text):
    bytes_to_pad = self.block_size - len(plain_text) % self.block_size
    ascii_string = chr(bytes_to_pad)
    return plain_text + ascii_string * bytes_to_pad


  def remove_padding(txt):
    last_char = txt[-1]
    return txt[:-ord(last_char)]   

  def encrypt(self, plain_text):
    plain_text = self.add_padding(plain_text)
    iv = Random.new().read(self.block_size)
    cipher = AES.new(self.key, AES.MODE_CBC,iv)
    encrypted_text = cipher.encrypt(plain_text.encode())
    return b64encode(iv+encrypted_text).decode()



    

aaes = AES_algorithm('augah')

print(aaes.encrypt('augah'))



