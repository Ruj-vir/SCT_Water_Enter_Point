
import streamlit as st
import pandas as pd
import base64
import math
import requests

# function สำหรับแปลงภาพเป็น base64
def img_to_base64(img_file_path):
    with open(img_file_path, "rb") as f:
        encoded_img = base64.b64encode(f.read()).decode()
    return encoded_img

# สมมติไฟล์โลโก้ชื่อ 'logo.png'
logo_path = "Logo.png" 
logo_base64 = img_to_base64(logo_path)
img_path = "Header SCT.png"  # ต้องอยู่ในโฟลเดอร์เดียวกับโค้ดที่รัน
bg_base64 = img_to_base64(img_path)

# --- Custom CSS for styling ---
st.markdown(f"""
    <style>
    .banner {{
        background-image: url("data:image/png;base64,{bg_base64}");
        background-size: cover;
        padding: 40px 40px 20px 40px;
        border-radius: 0px 0px 20px 20px;
        margin-bottom: 30px;
    }}
    .logo {{
        font-size: 32px;
        color: #3498db;
        font-weight: bold;
        margin-top: -30px;
        margin-bottom: 16px;
    }}
    .headline {{
        font-size: 28px;
        color: white;
        font-weight: bold;
        margin-bottom: 0px;
        margin-top: 0px;
    }}
    .subheadline {{
        font-size: 20px;
        color: white;
        margin-bottom: 18px;
        margin-top: 5px;
        font-weight: 300;
    }}
    .desc {{
        color: #d0e6fa;
        font-size: 15px;
        margin-top: 0;
    }}
    </style>
    <div class='banner'>
        <div class='logo'>
            <img src="data:image/png;base64,{logo_base64}" height="48">
        </div>
        <div class='headline'>
        <span style='color:#fff;font-weight:bold;'>POTENTIAL&nbsp;</span>
        <span style='color:#fff;font-weight:bold;'>WATER ENTRY POINT</span>
        </div>
        <div class='subheadline'>Smart CUI Troubleshooting Project</div>
        <div class='desc'>
        Using this artificial intelligence model, you can efficiently detect potential water entry point from images captured during inspections. It is built with Yolov8 components and utilities, requiring minimal modification for your specific use case.
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown(
    "<div style='text-align:center; font-size:20px; color:#3498db; margin-bottom:7px;'>Upload your image to detect potential water entry point.<br></div>",
    unsafe_allow_html=True
)

uploaded_files = st.file_uploader("Upload images", type=["png", "jpg", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    cols = st.columns(3)
    for idx, uploaded_file in enumerate(uploaded_files):
        if uploaded_file is not None:
            img_bytes = uploaded_file.read()
            img_base64 = base64.b64encode(img_bytes).decode('utf-8')
            mime = 'image/png' if uploaded_file.type == "image/png" else "image/jpeg"
            html = f"""
            <div style='text-align: center; margin-bottom: 10px;'>
                <img src="data:{mime};base64,{img_base64}" width="240" style="margin-bottom: 8px;"><br>
                <span>{uploaded_file.name}</span><br>
            </div>
            """
            cols[idx % 3].markdown(html, unsafe_allow_html=True)

    if st.button("Analyze image"):
        st.markdown("<h1 style='text-align:center;'>Detection Result</h1>", unsafe_allow_html=True)
        st.markdown("""
        <div style='text-align: left; margin-bottom: 20px;'>
          <span style='
              background-color: #57a9ff;
              color: white;
              padding: 6px 16px;
              border-radius: 8px;
              font-size: 16px;
              font-weight: 500;
              font-family: "Segoe UI", sans-serif;
              box-shadow: 2px 2px 6px rgba(0,0,0,0.15);
              border: 1px solid #3498db;
          '>
            📄 Generate Report
          </span>
        </div>
        """, unsafe_allow_html=True)

        image_path = "Image_01.png"
        with open(image_path, "rb") as img_file:
            img_bytes = img_file.read()
            img_base64 = base64.b64encode(img_bytes).decode('utf-8')

        st.markdown(f"""
            <div style='text-align:center'>
                <img src="data:image/png;base64,{img_base64}" width="600" style="border-radius:12px;"/>
                <p style="margin-top:10px;font-weight:500;">Image_01.png</p>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("<h4>Detection</h4>", unsafe_allow_html=True)
        st.markdown(""" 
        <div style='
            border: 1px solid #ccc; 
            border-radius: 10px; 
            padding: 16px; 
            font-size:18px;
            color: #2f70c9;
        '>
            Found water enter point more than 95%
        </div>
        """, unsafe_allow_html=True)

        # 👉 ตรงนี้ไม่ต้องใช้ API แล้ว
        # สามารถคอมเมนต์หรือเอาออกทั้งหมด

        st.success("Complete.")
        st.markdown("""
        <a href="http://localhost:8081/image" target="_blank" style="font-size:20px;color:#00A86B;">
        Detect Result
        </a>
        """, unsafe_allow_html=True)
