from PIL import Image
import random
import os

try:
    import numpy as np
    USE_NUMPY = True
except ImportError:
    USE_NUMPY = False


# ------------------------------------------------
# Utility Helpers
# ------------------------------------------------

def ensure_output_dir(path):
    """Create directory if it does not exist."""
    folder = os.path.dirname(path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder)


def get_int(prompt):
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Please enter a valid integer.")


def get_existing_path(prompt):
    while True:
        path = input(prompt).strip()
        if os.path.isfile(path):
            return path
        print("File not found. Try again.")


# ------------------------------------------------
# XOR Cipher (Fast Version)
# ------------------------------------------------

def xor_transform_image(in_path, out_path, key):
    key_byte = key & 0xFF
    img = Image.open(in_path).convert("RGB")
    ensure_output_dir(out_path)

    if USE_NUMPY:
        arr = np.array(img)
        arr ^= key_byte
        out = Image.fromarray(arr)
    else:
        w, h = img.size
        pixels = img.load()
        out = Image.new("RGB", (w, h))
        out_p = out.load()

        for y in range(h):
            for x in range(w):
                r, g, b = pixels[x, y]
                out_p[x, y] = (r ^ key_byte, g ^ key_byte, b ^ key_byte)

    out.save(out_path)


# ------------------------------------------------
# Pixel Swap Encryption
# ------------------------------------------------

def swap_encrypt_image(in_path, out_path, seed):
    img = Image.open(in_path).convert("RGB")
    w, h = img.size
    ensure_output_dir(out_path)

    pixels = list(img.getdata())
    n = len(pixels)

    rnd = random.Random(seed)
    indices = list(range(n))
    rnd.shuffle(indices)

    shuffled = [pixels[i] for i in indices]

    out = Image.new("RGB", (w, h))
    out.putdata(shuffled)
    out.save(out_path)


def swap_decrypt_image(in_path, out_path, seed):
    img = Image.open(in_path).convert("RGB")
    w, h = img.size
    ensure_output_dir(out_path)

    pixels = list(img.getdata())
    n = len(pixels)

    rnd = random.Random(seed)
    indices = list(range(n))
    rnd.shuffle(indices)

    inverse = [0] * n
    for new_pos, old_index in enumerate(indices):
        inverse[old_index] = new_pos

    recovered = [pixels[inverse[i]] for i in range(n)]

    out = Image.new("RGB", (w, h))
    out.putdata(recovered)
    out.save(out_path)


# ------------------------------------------------
# Combined Encryption (Swap + XOR)
# ------------------------------------------------

def combined_encrypt(in_path, out_path, seed, key):
    temp = out_path + ".tmp.png"

    swap_encrypt_image(in_path, temp, seed)
    xor_transform_image(temp, out_path, key)

    os.remove(temp)


def combined_decrypt(in_path, out_path, seed, key):
    temp = out_path + ".tmp.png"

    xor_transform_image(in_path, temp, key)
    swap_decrypt_image(temp, out_path, seed)

    os.remove(temp)


# ------------------------------------------------
# Menu System
# ------------------------------------------------

def main():
    print("=== Powerful Image Encryption Tool (Swap + XOR) ===")

    while True:
        print("\nMenu:")
        print("1. XOR Encrypt/Decrypt")
        print("2. Swap Encrypt")
        print("3. Swap Decrypt")
        print("4. Combined Encrypt (Swap → XOR)")
        print("5. Combined Decrypt (XOR → Swap)")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            in_path = get_existing_path("Enter input image: ")
            out_path = input("Enter output image: ").strip()
            key = get_int("Enter XOR key (0–255): ")
            xor_transform_image(in_path, out_path, key)
            print("XOR operation complete:", out_path)

        elif choice == "2":
            in_path = get_existing_path("Enter input image: ")
            out_path = input("Enter encrypted image path: ").strip()
            seed = get_int("Enter shuffle seed: ")
            swap_encrypt_image(in_path, out_path, seed)
            print("Swap encryption complete:", out_path)

        elif choice == "3":
            in_path = get_existing_path("Enter encrypted image: ")
            out_path = input("Enter decrypted image path: ").strip()
            seed = get_int("Enter same seed used for encryption: ")
            swap_decrypt_image(in_path, out_path, seed)
            print("Swap decryption complete:", out_path)

        elif choice == "4":
            in_path = get_existing_path("Enter input image: ")
            out_path = input("Enter combined encrypted path: ").strip()
            seed = get_int("Enter shuffle seed: ")
            key = get_int("Enter XOR key (0–255): ")
            combined_encrypt(in_path, out_path, seed, key)
            print("Combined encryption complete:", out_path)

        elif choice == "5":
            in_path = get_existing_path("Enter encrypted image: ")
            out_path = input("Enter decrypted output path: ").strip()
            seed = get_int("Enter shuffle seed: ")
            key = get_int("Enter XOR key: ")
            combined_decrypt(in_path, out_path, seed, key)
            print("Combined decryption complete:", out_path)

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
