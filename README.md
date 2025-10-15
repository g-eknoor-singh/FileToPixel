# FileToPixel 🔐🎨

A mini-project that converts any file(s) into an **encrypted pixel-based image**, which can later be decoded back using the key.

## ⚙️ Features
- Converts any file(s) into a single encrypted image.
- Uses AES (via Fernet) encryption for security.
- Supports multiple files (auto-zipped).
- Progress bar for visualization.
- Decoder reconstructs the exact original files.

## 🧠 How It Works
1. Input files → zipped → encrypted.
2. Encrypted bytes → converted to RGB pixels.
3. Image saved as `.png` and key stored separately.
4. Decoder reverses the process perfectly.

## 🧩 Folder Structure
FileToPixel/

│

├── encoder.

├── decoder.py

├── requirements.txt

├── README.md

├── /input_files/

└── /output/


## 🚀 How to Run
```bash
pip install -r requirements.txt
python encoder.py
python decoder.py

💡 Tech Stack

Python

Cryptography (Fernet)

Pillow (Image handling)

tqdm (Progress bar)

👤 Author

Developed by g-eknoor-singh
