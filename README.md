<p align="center">
  <img src="assets/banner.png" alt="PixelCrypt Banner" width="600"/>
</p>

<h1 align="center">PixelCrypt 🔐</h1>
<p align="center">A simple image encryption tool using pixel manipulation.</p>

# 🔐 PixelCrypt

A simple image encryption and decryption tool using pixel manipulation (XOR logic).

## 💡 Features
- Encrypt and decrypt JPG, PNG, BMP images
- Custom key-based XOR encryption
- Fast and lightweight

## 📦 Install Dependencies

```bash
pip install -r requirements.txt
 
🔒 Encrypt
bash
Copy code
python pixelcrypt_app.py encrypt input.jpg encrypted.png --key 123


🔓 Decrypt
bash
Copy code
python pixelcrypt_app.py decrypt encrypted.png output.jpg --key 123