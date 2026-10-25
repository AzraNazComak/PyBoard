import yt_dlp

def calculate_playlist_duration(playlist_url):
    settings = {
        'quiet': True,
        'extract_flat': True,
    }

    with yt_dlp.YoutubeDL(settings) as ydl:
        info = ydl.extract_info(playlist_url, download=False)
        print("The list information is being withdrawn from youtube, ıt may take some time...")
        total_duration = 0
        total_videos = 0

        if 'entries' not in info:
            print("No videos found in the playlist check the link!!")
            return
        

        for entry in info['entries']:
            if entry.get('duration'):
                total_videos += 1
                total_duration += entry['duration']
        saat = int(total_duration // 3600)
        dakika = int((total_duration % 3600) // 60)
        saniye = int(total_duration % 60)
        
        print('*' * 50)
        print(f"Total videos: {total_videos}")
        print(f"Total Duration: {saat} hours, {dakika} minutes, {saniye} seconds")
        print('*' * 50)


link = input("Enter the playlist's link: ")
calculate_playlist_duration(link)