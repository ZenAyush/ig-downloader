import subprocess

# folder location example: C:\\Users\\AYUSH\\Downloads\\ig-vids
def download_instagram_video(video_url, output_path="PASTE THE FOLDER LOCATION"):
    """
    Downloads an Instagram video, reel, or post using yt-dlp.
    """
    # Add unique ID in filename to avoid overwrite
    command = f'yt-dlp -o "{output_path}/%(uploader)s - %(id)s.%(ext)s" {video_url}'
    subprocess.run(command, shell=True)
    print("✅ Download Completed!")

if __name__ == "__main__":
    video_url = input("Enter the Instagram video URL: ")
    download_instagram_video(video_url)
