from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.editor import VideoFileClip, concatenate_videoclips, clips_array


def cut_video(input_path, output_path, start_time, end_time):
    # Load the video clip
    video_clip = VideoFileClip(input_path)

    # Define the subclip based on the start and end times
    subclip = video_clip.subclip(start_time, end_time)

    # Write the subclip to the output file
    subclip.write_videofile(output_path, codec="libx264", audio_codec="aac")


def combine_vidoes_side_by_side(path1,path2):
    # Load the two video clips
    clip1 = VideoFileClip(path1)
    clip2 = VideoFileClip(path2)

    # Resize the clips to have the same height
    min_height = min(clip1.h, clip2.h)
    clip1 = clip1.resize(height=min_height)
    clip2 = clip2.resize(height=min_height)

    # Combine the clips side by side
    final_clip = clips_array([[clip1, clip2]])

    # Write the final clip to a file
    final_clip.write_videofile("test_case/combined_video.mp4")

def combine_videos(path1,path2):
    clip1 = VideoFileClip(path1)
    clip2 = VideoFileClip(path2)

    # Concatenate the video clips
    final_clip = concatenate_videoclips([clip1, clip2])

    # Write the final clip to a file
    final_clip.write_videofile("test_case/combined__video.mp4")

if __name__ == "__main__":
    # Replace 'input_video.mp4' with the path to your input video file
    input_video_path = "/home/ksuser/LS/29th Jan CCTV footage/KSNVR_ch6_20240129100007_20240129112749.avi"
    
    # Replace 'output_video_cut.mp4' with the desired output video file path
    output_video_path = "test_case/multi_camera_2.mp4"

    # Set the start and end times for the cut (in seconds)
    start_time = 1593 # 8:00 min
    end_time = 1650    # 8:20 min

    # Cut the video
    # cut_video(input_video_path, output_video_path, start_time, end_time)
    
    path1 ='test_case/multi_camera_1.mp4'
    path2 ='test_case/multi_camera_2.mp4'
    
    combine_videos(path1,path2)


# import moviepy.editor as moviepy
# clip = moviepy.VideoFileClip("/home/ksuser/LS/CH1/KSNVR_ch1_20240207162600_20240207172512.asf")
# clip.write_videofile("myvideo.mp4")


