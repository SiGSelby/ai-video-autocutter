import whisper
from moviepy.editor import VideoFileClip, concatenate_videoclips

def transcribe_video(video_path):
    print("Loading AI Whisper Model...")
    model = whisper.load_model("base")
    
    print("Analyzing audio and extracting timestamps...")
    result = model.transcribe(video_path)
    return result["segments"]

def professional_auto_cut(video_path, segments):
    print("Processing video timeline...")
    video = VideoFileClip(video_path)
    valid_clips = []
    
    # Loop through segments where the AI actually detected speech
    for segment in segments:
        start = segment["start"]
        end = segment["end"]
        text = segment["text"].strip()
        
        # Filter out long awkward silences by only keeping spoken segments
        if text: 
            print(f"Keeping: [{start}s - {end}s] -> {text}")
            clip = video.subclip(start, end)
            valid_clips.append(clip)
            
    print("Stitching edited clips together...")
    final_video = concatenate_videoclips(valid_clips)
    return final_video

if __name__ == "__main__":
    input_file = "raw_footage.mp4" # Put a raw test video in your folder
    output_file = "ai_edited_output.mp4"
    
    # Run the automated pipeline
    speech_timestamps = transcribe_video(input_file)
    final_edit = professional_auto_cut(input_file, speech_timestamps)
    
    # Save the polished video
    final_edit.write_videofile(output_file, codec="libx264", audio_codec="aac")
    print(export_successful!)
