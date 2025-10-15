import os
from cryptography.fernet import Fernet
from PIL import Image
from tqdm import tqdm

os.makedirs("output/encoded", exist_ok=True)
os.makedirs("output/decoded", exist_ok=True)

def image_to_data(img_path):
    img = Image.open(img_path)
    pixels = list(img.getdata())
    data = bytearray()

    progress = tqdm(pixels, desc="🔓 Extracting pixels", ncols=80)
    for r, g, b in progress:
        data.extend([r, g, b])

    return bytes(data)

def decrypt_data(encrypted_data, key_file):
    with open(key_file, "rb") as kf:
        key = kf.read()
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_data)

def save_output_zip(decrypted_data):
    output_path = "output/decoded/decoded_output.zip"
    with open(output_path, "wb") as f:
        f.write(decrypted_data)
    print(f"📦 Decoded ZIP saved at: {output_path}")
    return output_path

def main():
    print("\n🧩 Starting Decoding Process...\n")
    img_path = "output/encoded/encoded_image.png"
    key_file = "output/encoded/encryption.key"

    encrypted_data = image_to_data(img_path)
    decrypted = decrypt_data(encrypted_data, key_file)
    save_output_zip(decrypted)

    print("\n✅ Decoding Complete! You can extract the ZIP in /output/decoded/")

if __name__ == "__main__":
    main()
