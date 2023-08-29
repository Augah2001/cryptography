const crypto = require("crypto");

class AESAlgorithm {
  constructor(key) {
    this.key = key;
    this.algorithm = "aes-256-cbc";
  }

  encrypt(plainText) {
    const keyBuffer = crypto.createHash("sha256").update(this.key).digest();
    const iv = crypto.randomBytes(16);
    const cipher = crypto.createCipheriv(this.algorithm, keyBuffer, iv);
    let encrypted = cipher.update(plainText, "utf8", "base64");
    encrypted += cipher.final("base64");
    const encodedBytes = Buffer.concat([iv, Buffer.from(encrypted, "base64")]);
    return encodedBytes.toString("base64");
  }
}

const aaes = new AESAlgorithm("augah");
console.log(aaes.encrypt("augah"));
