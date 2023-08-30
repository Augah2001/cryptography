const crypto = require("node:crypto");

class AES_GCM {
  constructor(key) {
    this.key = crypto.createHash("sha256").update(key).digest();
    this.algorithm = "aes-256-gcm";
  }

  encrypt(plainText) {
    const nonce = crypto.randomBytes(12);

    const cipher = crypto.createCipheriv(this.algorithm, this.key, nonce);
    let encrypted = cipher.update(plainText, "utf-8", "base64");
    encrypted += cipher.final("base64");

    const tag = cipher.getAuthTag();
    const encodedBytes = Buffer.concat([
      Buffer.from(encrypted, "base64"),
      nonce,
      tag    ]);

    return encodedBytes.toString("base64");
  }
}

const aesInstance = new AES_GCM("password123");

console.log(aesInstance.encrypt("augah"))
