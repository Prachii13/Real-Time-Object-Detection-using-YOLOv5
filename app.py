import streamlit as st
import subprocess

st.title("📦 YOLOv5 Real-Time Object Detector")

option = st.radio("Choose Input Source", ["Webcam", "Image", "Video"])

if option == "Webcam":
    if st.button("Start Detection"):
        subprocess.run(["python", "yolov5/detect.py", "--source", "0", "--weights", "yolov5s.pt"])

elif option == "Image":
    file = st.file_uploader("Upload Image", type=["jpg", "png"])
    if file:
        with open("input.jpg", "wb") as f:
            f.write(file.read())
        if st.button("Detect"):
            subprocess.run(["python", "yolov5/detect.py", "--source", "input.jpg", "--weights", "yolov5s.pt"])
            st.image("runs/detect/exp/input.jpg")

elif option == "Video":
    file = st.file_uploader("Upload Video", type=["mp4"])
    if file:
        with open("input.mp4", "wb") as f:
            f.write(file.read())
        if st.button("Detect"):
            subprocess.run(["python", "yolov5/detect.py", "--source", "input.mp4", "--weights", "yolov5s.pt"])
            st.video("runs/detect/exp/input.mp4")
