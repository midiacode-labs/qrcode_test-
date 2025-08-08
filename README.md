# QR Code Generator App

A Streamlit application that generates QR codes from random codes in your data file.

## Features

- 📁 Reads codes from `raw_data.txt`
- 🔍 Generates QR codes for random codes
- 🔄 "Next QR Code" button to generate new random QR codes
- 📱 Displays the QR code image on the web page
- ℹ️ Shows current code and total available codes

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Make sure you have `raw_data.txt` in the same directory as the app**

## Usage

1. **Run the application:**
   ```bash
   streamlit run qrcode_app.py
   ```

2. **Open your browser and navigate to:**
   - Local URL: `http://localhost:8501`
   - Network URL: `http://192.168.1.78:8501` (accessible from other devices on your network)

3. **Using the app:**
   - The app will automatically load a random code from your `raw_data.txt` file
   - A QR code will be generated and displayed
   - Click the "🔄 Next QR Code" button to generate a new random QR code
   - The current code and total available codes are shown

## Files

- `qrcode_app.py` - Main Streamlit application
- `requirements.txt` - Python dependencies
- `raw_data.txt` - Your data file with codes (one per line, first line is treated as header)

## Dependencies

- `streamlit` - Web app framework
- `qrcode[pil]` - QR code generation
- `Pillow` - Image processing

## Notes

- The first line in `raw_data.txt` is treated as a header and ignored
- Each subsequent line should contain one code
- QR codes are generated with standard settings (can be customized in the code)
- The app uses session state to maintain the current code between button clicks
