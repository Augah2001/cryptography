const crypto = require('node:crypto')

class AES_CTR {

    constructor(key) {
        this.key = crypto.createHash('sha256').update(key).digest()
        this.algorithm = 'aes-256-ctr'
    }

    encrypt = (plainText) => {
        // generate initialization vector
        const iv = crypto.randomBytes(16)
        // create a cipher using the  aes-256-ctr
        const cipher = crypto.createCipheriv(this.algorithm, this.key, iv)
        // encrypt the text with input as utf-8 to output base64
        let encryptedText = cipher.update(plainText, 'utf-8', 'base64')
        // finalize the reamining part of the encrypted text
        encryptedText += cipher.final('base64')
        // concaatenate the iv to the cipher text
        const encodedBytes = Buffer.concat([iv, Buffer.from(encryptedText, 'base64')])
        // encode the bytes to a more transmittable format which is the base64 format 
        return encodedBytes.toString('base64')
    }
}

aes = new AES_CTR('1234')

console.log(aes.encrypt('wadii wangu'))