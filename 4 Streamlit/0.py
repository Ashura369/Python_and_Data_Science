import streamlit as st
import cv2 as cv
from ultralytics import YOLO
import tempfile

model = YOLO('yolov8n.pt')
rec_vid = st.file_uploader('Upload Video', type=['mp4', 'avi', 'mov'])

if rec_vid is not None:
    # 1. Write uploaded bytes to a temp file
    tfile = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
    tfile.write(rec_vid.read())
    tfile.close()

if st.button('n Start AI Detection'):
    cap = cv.VideoCapture(tfile.name)
    vid_placeholder = st.empty()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break


results = model(frame)
annotated_frame = results[0].plot()

rgb_frame = cv.cvtColor(annotated_frame, cv.COLOR_BGR2RGB)
vid_placeholder.image(rgb_frame, channels='RGB', use_container_width=True)
cap.release()

