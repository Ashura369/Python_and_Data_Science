import streamlit as st
import sys
import numpy as np
import cv2 as cv
from ultralytics import YOLO                # to use obj detection model
from streamlit.web.cli import main
from streamlit.web import cli as stcli
from PIL import Image
import tempfile                             # for video preprocessing

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# PAGE LAYOUT
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
st.set_page_config('objDetection', layout='wide')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# HEADINGS
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

st.title("Object Detection Model")
st.write("Model used - yolo26n.pt (by ultralytics)")
st.markdown("---")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# MODEL
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@st.cache_resource
def load_model():
    return YOLO("yolov8n.pt")

model = load_model()

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# MAIN BUTTON SECTION
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

btn_sec1, btn_sec2 = st.columns([1,1])

with btn_sec1:
    button = st.selectbox('Select Input Source', options=['Image', 'Recorded Video', 'Live webcam'], index=None)

st.divider()

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 'IMAGE' BUTTON
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

if button == 'Image':
    with btn_sec2:
        img_btn = st.selectbox('Select Image Input', options=['Open Camera', 'Upload image'], index=None)


    img_format = ['.jpg','.jpeg','.png','.gif','.webp']
    btn_sec1, btn_sec2 = st.columns([1, 1])

    if img_btn == 'Open Camera':
        with btn_sec1:
            img_clicked = st.camera_input("Take live picture")                              # used for clicking image

        if img_clicked is not None:
            img = Image.open(img_clicked)                                                   # converting image buffer to opencv format

                # Converts Raw Bytes to a PIL Image: Uses Python's Pillow library (PIL.Image) to read and decode the raw byte stream from 'img_clicked' into a workable PIL Image object.
                # Prepares for Processing: Once it is a PIL image, you can easily convert it to a NumPy array (np.array(img)), pass it into computer vision models (like YOLO), or perform transformations (resizing, filtering, etc.).

            img_array = np.array(img)           # converting the img into a numpy array

            # sending the numpy array into the model
            result = model(img_array)

            with btn_sec2:
                st.subheader("Detected Objects in the Image")
                st.image(result[0].plot(), caption='detected objects')
        else:
            with btn_sec2:
                st.info("Snap a photo on the left to see detections here")
    elif img_btn == 'Upload image':
        with btn_sec1:
            st.write("Select image from files")
            imgs_uploaded = st.file_uploader('Select image / images', type=img_format, accept_multiple_files=True)         # accepting multiple image files

            if imgs_uploaded:
                with btn_sec2:
                    st.subheader("Detected Objects in the Image")

                for img in imgs_uploaded:

                    img = Image.open(img)
                    img_array = np.array(img)

                    result = model(img_array)

                    with btn_sec2:
                        st.image(result[0].plot())
            else:
                with btn_sec2:
                    st.info("Select a photo from the files to see detections here")


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 'RECORDED VIDEO' BUTTON
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


elif button == 'Recorded Video':
    vid_format = [".mp4", ".avi", ".mov", ".mkv", ".webm"]
    btn_sec1, btn_sec2 = st.columns([1, 1])


    with btn_sec1:
        rec_vid = st.file_uploader('Upload Video (one video only)', type=vid_format)
        

    with btn_sec2:
        if rec_vid is not None:
            # saving the uploaded video bytes to a file on a disk with mp4 format
            tfile = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
            tfile.write(rec_vid.read())
            tfile.close()                   # closing the file so 'OpenCV' can read it

            if st.button('Generate'):
                cap = cv.VideoCapture(tfile.name)

                width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
                height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
                total_frames = int(cap.get(cv.CAP_PROP_FRAME_COUNT)) or 100
                fps = 30

                out_tfile = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
                fourcc = cv.VideoWriter_fourcc(*'mp4v')
                out = cv.VideoWriter(out_tfile.name, fourcc, fps, (width, height))

                # making a progressbar for the download button 
                progress_bar = st.progress(0, text='Processing the video to download')
                vid_play = st.empty()
                current_frame = 0
                
                while cap.isOpened():
                    ret, frames = cap.read()
                    if not ret:
                        print('ERROR')
                        break

                    results = model(frames)
                    out.write(results[0].plot())

                    rgb_vid = cv.cvtColor(results[0].plot(), cv.COLOR_BGR2RGB)
                    vid_play.image(rgb_vid, channels='RGB')

                    # updating progressbar by each frame processed
                    current_frame += 1
                    progress = min(current_frame / total_frames, 1.0)
                    progress_bar.progress(
                        progress,
                        text=f"Processing download : frame {current_frame} of {total_frames} ({int(progress * 100)} %)"
                    )


                cap.release()
                out.release()
                st.toast('Video processing complete !!!')

                # making a download button for the generated video
                with open(out_tfile.name, 'rb') as f:
                    video_bytes = f.read()

                st.download_button(
                    label='Download',
                    data=video_bytes,
                    file_name="yolo_detected_video.mp4",
                    mime="video/mp4"
                )
        else:
            st.info('Upload a video file to see object detection')

        # make the download button available















# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



























# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    if st.runtime.exists():
        pass
    else:
        sys.argv = ['streamlit', 'run', sys.argv[0]]
        sys.exit(stcli.main())

