import streamlit as st
import qrcode
import random
import io


def load_codes_from_file(file_path):
    """Load codes from the raw_data.txt file, excluding the header"""
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        # Skip the first line (header "codigo") and strip whitespace
        codes = [line.strip() for line in lines[1:] if line.strip()]
        return codes
    except FileNotFoundError:
        st.error("File raw_data.txt not found!")
        return []
    except Exception as e:
        st.error(f"Error reading file: {e}")
        return []


def generate_qr_code(data):
    """Generate QR code image from data"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create QR code image
    img = qr.make_image(fill_color="black", back_color="white")
    return img


def main():
    st.title("🔍 QR Code Generator")
    st.write("Generate QR codes from random codes in your data file")
    
    # Load codes from file
    codes = load_codes_from_file("raw_data.txt")
    
    if not codes:
        st.warning("No codes found in the file!")
        return
    
    st.success(f"Loaded {len(codes)} codes from file")
    
    # Initialize session state for the current code
    if 'current_code' not in st.session_state:
        st.session_state.current_code = random.choice(codes)
    
    # Display current code
    st.subheader("Current Code:")
    st.code(st.session_state.current_code, language=None)
    
    # Generate and display QR code
    st.subheader("QR Code:")
    qr_img = generate_qr_code(st.session_state.current_code)
    
    # Convert PIL image to bytes for streamlit
    img_buffer = io.BytesIO()
    qr_img.save(img_buffer, format='PNG')
    img_buffer.seek(0)
    
    # Display the QR code image
    st.image(img_buffer, caption=f"QR Code for: {st.session_state.current_code}", width=300)
    
    # Button to generate next QR code
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col2:
        if st.button("🔄 Next QR Code", type="primary", use_container_width=True):
            st.session_state.current_code = random.choice(codes)
            st.rerun()
    
    # Additional info
    st.divider()
    
    with st.expander("ℹ️ Information"):
        st.write(f"**Total codes available:** {len(codes)}")
        st.write(f"**Current code:** {st.session_state.current_code}")
        st.write("Click the 'Next QR Code' button to generate a new random QR code.")


if __name__ == "__main__":
    main()
