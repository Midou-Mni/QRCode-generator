# 📷 QR Code Generator - Python Desktop App

A simple and user-friendly Python desktop application to generate **QR Codes** from text or URLs. This app features a graphical interface built with **Tkinter** and supports live preview using the **Pillow** and **qrcode** libraries.

---

## ✅ Features

- Generate QR codes from any text or URL
- Live preview of the generated QR code
- Save the QR code as a PNG file
- Clean and modern GUI
- Error handling for empty input fields

---

## 🛠️ Requirements

Make sure you have Python 3 installed.

Install the required libraries using pip:

```bash
pip install qrcode[pil] Pillow
```

---

## ▶️ How to Run

1. Save the script as `qr_generator.py`.
2. Make sure you have an `icon.png` file in the same directory (or update the filename in the script).
3. Run the script using:

```bash
python qr_generator.py
```

---

## 🧠 How It Works

1. Enter a **Title** (used as the image file name).
2. Enter a **URL** or any text to be encoded.
3. Click **"Generate QR Code"**.
4. The app generates and saves the QR code as a PNG file.
5. A live preview of the QR code is shown in the application.

---

## 📌 GUI Overview

| Component       | Purpose                                  |
|----------------|-------------------------------------------|
| Title Field     | Name used to save the QR code image      |
| URL Field       | Text or URL to encode into the QR code   |
| Generate Button | Creates and displays the QR code image   |
| Image Viewer    | Displays the generated QR code           |
| Error Label     | Shows success or error messages          |

---

## 📦 Technologies Used

- **Python**
- **Tkinter** (GUI)
- **Pillow** (`PIL`) for image handling
- **qrcode** for generating QR codes

---

## ⚠️ Notes

- If `icon.png` is missing, you may get a `FileNotFoundError`. Replace or remove that line if needed.
- QR code image is saved with the name you provide in the title field.
- Make sure to enter both a title and a URL/text before clicking generate.

---

## 📄 License

This project is free to use and modify. No license restrictions.
