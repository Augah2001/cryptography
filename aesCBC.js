const crypto = require('crypto')

class AESAlgorithm {
  constructor(key, blockSize) {
    this.key = crypto.createHash('sha256').update(key).digest()
    this.blockSize = blockSize;
    this.algorithm = 'aes-256-cbc'
  }

  add_padding = (plainText) => {
    const bytesToPad = this.blockSize - (plainText.length % this.blockSize);
    const asciiChar = String.fromCharCode(bytesToPad);
    const paddingString = asciiChar.repeat(bytesToPad);
    const paddedString = plainText + paddingString;
    return paddedString;
  };
  remove_padding = (txt) => {
    const numberOfBytes = txt.charCodeAt(txt.length -1)
    return txt.slice(0, -numberOfBytes)
  };

  encrypt = (plainText) => {
    // initializzation vector
    const iv = crypto.randomBytes(16)
    //  create a cipher
    const cipher = crypto.createCipheriv(this.algorithm, this.key, iv)
    // encrypt the text using the cipher
    let encrypted = cipher.update(plainText, 'utf-8', 'base64')
    encrypted += cipher.final('base64')
    const encodedBytes = Buffer.concat([iv,Buffer.from(encrypted, 'base64')])
    return encodedBytes.toString('base64')

  }
}

  

const aes = new AESAlgorithm('augah', 16)

console.log(aes.encrypt('augahhuighiuoiuhu'))