import streamlit as st

from PIL import Image


st.title("Create a Greyscale Image")

camera_image=st.camera_input("Camera")

if camera_image:
    img=Image.open(camera_image)
    gray_img=img.convert("L")
    st.write("Generated greyscale image")
    st.image(gray_img)
