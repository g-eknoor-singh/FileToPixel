import os
import zipfile
from cryptography.fernet import Fernet
from PIL import Image
from tqdm import tqdm
import math

# === Folder Setup ===
os.makedirs("output/encoded", exist_ok=True)
os.makedirs("output/decoded", exist_ok=True)

# === Step 1: Zip Input Files ===
def create_input_zip():
    input_folder = "input_files"
    temp_zip = "output/encoded/input_data.zip"
    with zipfile.ZipFile(temp_zip, 'w') as zipf:
        for file in os.listdir(input_folder):
            full_path = os.path.join(input_folder, file)
            if os.path.isfile(full_path):
                zipf.write(full_path, arcname=file)
    print(f"✅ Zipped all input files into: {temp_zip}")
    return temp_zip

# === Step 2: Encrypt File ===
def encrypt_file(file_path, key_file):
    key = Fernet.generate_key()
    with open(key_file, "wb") as kf:
        kf.write(key)
    fernet = Fernet(key)

    with open(file_path, "rb") as f:
        data = f.read()

    encrypted = fernet.encrypt(data)
    print("🔒 File encrypted successfully!")
    return encrypted

# === Step 3: Convert Encrypted Data to Pixels ===
def data_to_image(data, output_img):
    pixel_data = list(data)
    total_pixels = math.ceil(len(pixel_data) / 3)
    img_size = math.ceil(total_pixels ** 0.5)
    pixels = []

    progress = tqdm(range(0, len(pixel_data), 3), desc="🧬 Converting to pixels", ncols=80)
    for i in progress:
        chunk = pixel_data[i:i+3]
        while len(chunk) < 3:
            chunk.append(0)
        pixels.append(tuple(chunk))

    img = Image.new("RGB", (img_size, img_size))
    img.putdata(pixels)
    img.save(output_img)
    print(f"🖼️ Image saved as: {output_img}")
    return img_size

# === Step 4: Package Final Output ===
def make_final_zip(image_path, key_path):
    final_zip = "output/encoded/final_encoded_package.zip"
    with zipfile.ZipFile(final_zip, "w") as zipf:
        zipf.write(image_path, arcname="encoded_image.png")
        zipf.write(key_path, arcname="encryption.key")
    print(f"📦 Final encoded ZIP created at: {final_zip}")
    return final_zip

# === MAIN ENCODER ===
def main():
    print("\n🚀 Starting Encoding Process...\n")

    # Step 1: Create input zip
    input_zip = create_input_zip()

    # Step 2: Encrypt and convert to image
    key_file = "output/encoded/encryption.key"
    output_img = "output/encoded/encoded_image.png"
    encrypted_data = encrypt_file(input_zip, key_file)
    data_to_image(encrypted_data, output_img)

    # Step 3: Create final zip containing only image + key
    make_final_zip(output_img, key_file)

    # Step 4: Cleanup temporary zip
    if os.path.exists(input_zip):
        os.remove(input_zip)
        print("🧹 Cleaned up temporary input ZIP.\n")

    print("✅ Encoding Complete! Final ZIP ready in /output/encoded/")

if __name__ == "__main__":
    main()
