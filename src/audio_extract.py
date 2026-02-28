from moviepy import VideoFileClip


# Define the input video file and output audio file
def extract_audio(input, output):
    # Load the video clip
    video_clip = VideoFileClip(input)

    # Extract the audio from the video clip
    audio_clip = video_clip.audio

    # Write the audio to a separate file
    audio_clip.write_audiofile(output)

    # Close the video and audio clips
    audio_clip.close()
    video_clip.close()

    print("Audio extraction successful!")