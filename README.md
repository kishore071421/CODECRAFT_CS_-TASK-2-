📌 Image Encryption Tool (Swap + XOR)

A powerful Python-based image encryption/decryption utility that supports:

XOR Pixel Encryption

Pixel Swap Encryption (Shuffle using seed)

Combined Encryption (Swap → XOR)

Combined Decryption (XOR → Swap)

This tool works with any image format supported by PIL and uses optional NumPy acceleration for fast XOR processing.

🚀 Features
🔐 1. XOR Encryption / Decryption

Encrypts or decrypts an image using a single-byte XOR key (0–255).
Fastest method, works with and without NumPy.

🔄 2. Pixel Swap Encryption

Shuffles all pixels in the image using a seed value.
Same seed is required to reverse the shuffle.

🔓 3. Pixel Swap Decryption

Reverses the shuffle using the same seed.
Restores the original image perfectly.

🔐🌀 4. Combined Encryption (Swap → XOR)

Applies pixel shuffle first, then XOR encryption.
More secure than using either method alone.

🔁🔓 5. Combined Decryption (XOR → Swap)

Reverses the combined encryption in the correct order.

📦 Requirements
Python Modules:

Pillow

numpy (optional, but speeds up XOR)

Standard Python libs: os, random

Install required packages:

pip install pillow numpy

📁 Project Structure
image_encryptor.py
README.md

▶️ Running the Program

Use:

python image_encryptor.py


You'll see an interactive menu:

=== Powerful Image Encryption Tool (Swap + XOR) ===

Menu:
1. XOR Encrypt/Decrypt
2. Swap Encrypt
3. Swap Decrypt
4. Combined Encrypt (Swap → XOR)
5. Combined Decrypt (XOR → Swap)
6. Exit


Enter the option number and follow prompts.

⚙️ Usage Example
XOR Encrypt:
Enter input image: sample.png
Enter output image: enc.png
Enter XOR key (0–255): 123

Swap Encrypt:
Enter input image: sample.png
Enter encrypted image path: swapped.png
Enter shuffle seed: 9999

Combined Encrypt:
Enter input image: sample.png
Enter combined encrypted path: combo.png
Enter shuffle seed: 555
Enter XOR key: 200

🧠 How Each Algorithm Works
🔐 XOR

Each pixel channel (R,G,B) is XORed:

new_value = original ^ key


XOR is reversible and symmetric.

🔄 Pixel Swap

Flatten image pixels

Shuffle using random.Random(seed)

Save shuffled output

Decryption rebuilds original order using inverse mapping.

🌀 Combined Method

Encrypt:

Shuffle pixels

XOR the shuffled image

Decrypt:

XOR the encrypted image

Unshuffle (reverse swap)

Keeps output unreadable even if one key is guessed.

🛠️ Error Handling

Invalid integer inputs → asks again

Missing file → asks again

Output directory auto-created

✨ Advantages

✔ Works for any image type
✔ Lossless (original image is fully restored)
✔ Optional NumPy acceleration
✔ Supports very large images
✔ Perfect for cybersecurity projects, cryptography learning, or steganography pipelines
