import streamlit as st

# Title of the application
st.title("Tennis Game Tracking")

# Layout setup: video display area on the left, buttons on the right
col1, col2 = st.columns([10,7])

# File uploader and buttons on the right side
with col2:
    # File uploader for selecting input file
    input_file = st.file_uploader("Select Input File", type=["mp4", "mov", "avi"])

    # Preview button
    preview_video = st.button("Preview Video")
    
    # Progress bar and label
    progress_bar = st.progress(0)
    progress_label = st.empty()  # To display percentage text

    # Process Video button
    if st.button("Process Video"):
        if input_file:
            # Simulate video processing by updating the progress bar
            for i in range(1, 101):
                progress_bar.progress(i)
                progress_label.text(f"{i}%")
        else:
            st.warning("Please select a video file to process.")

    # Show Output button
    if st.button("Show Output"):
        st.text("Output will be displayed here.")  # Placeholder for actual output

    # Download Output button
    if st.button("Download Output"):
        st.text("Download link will appear here.")  # Placeholder for download link

# Video display area in the larger left column
with col1:
    if preview_video and input_file:
        st.video(input_file)
    elif preview_video:
        st.warning("Please select a video file to preview.")