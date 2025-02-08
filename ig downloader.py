import subprocess

def download_instagram_video(video_url, output_path="C:\\Users\\ZenAyush\\Downloads\\ig-vids"):
    """
    Downloads an Instagram video, reel, or post using yt-dlp.
    """
    command = f'yt-dlp -o "{output_path}/%(title)s.%(ext)s" {video_url}'
    subprocess.run(command, shell=True)
    print("✅ Download Completed!")

if __name__ == "__main__":
    video_url = input("Enter the Instagram video URL: ")
    download_instagram_video(video_url)
