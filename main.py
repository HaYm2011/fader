import os
import sys
import yt_dlp 

lib= "testmusic"

"""if the folder for the music does not exist this makes a new folder"""
if not os.path.exists("testmusic"):
    os.makedirs("testmusic")
def download_yt(vid_url: str):
    downloader_options= {}
    downloader_options["format"]="bestaudio/best"

    output_filename=os.path.join("testmusic","%(id)s.%(ext)s")
    downloader_options["outtmpl"]=output_filename
    converter= {
        "key":"FFmpegExtractAudio",
        "preferredcodec":"mp3",
        "preferredquality":"192"
    }
    downloader_options["postprocessors"]=[converter]
    downloader_options["quiet"]=False
    downloader_options["no_warnings"]=False
    #yt-dlp test:
    with yt_dlp.YoutubeDL(downloader_options) as ydl_instance:
        extracted_info=ydl_instance.extract_info(vid_url, download=True)
        unique_vid_id=extracted_info.get("id")
        song_name=extracted_info.get("title") 
        channel_author=extracted_info.get("uploader")

        if channel_author is None:
            channel_author = extracted_info.get("channnel")
        playback_duration_sec=extracted_info.get("duration")
        source_m4a_filename=unique_vid_id + ".m4a"
        target_mp4_filename=unique_vid_id + ".mp4"

        source_path=os.path.join("testmusic", source_m4a_filename)
        final_mp4_path=os.path.join("testmusic", target_mp4_filename)
        
        if os.path.exists(source_path):
            os.replace(source_path, final_mp4_path)
        metadata_payload={
            "id": unique_vid_id,
            "title": song_name,
            "artist": channel_author,
            "duration": playback_duration_sec,
            "filename": target_mp4_filename,
            "filepath":final_mp4_path
        }

        return metadata_payload

if __name__=="__main__":
    print("===================================================")
    print("         FADER AUDIO INGESTION *(MP4/AAC)*         ")
    print("===================================================")

    user_input=input("Enter song title").strip()

    if not user_input:
        print("Type the title of the song first")
        sys.exit(1)
    query_target=f"ytsearch1:{user_input}"
    track_data=download_yt(query_target)
    print(f"\nProcessing: {user_input}")
    print("download finished!!!🌟🌟🌟")