from youtube_transcript_api import YouTubeTranscriptApi

def get_words_from_link(url):
    # Get just the video ID from the link
    if "v=" in url:
        video_id = url.split("v=")[1].split("&")[0]
    elif "youtu.be" in url:
        video_id = url.split("/")[-1]
    else:
        print("Bad link! Try again.")
        return None
    
    try:
        # Get the words
        words = YouTubeTranscriptApi.get_transcript(video_id)
        all_text = ""
        for part in words:
            all_text = all_text + part['text'] + " "
        return all_text
    except:
        print("Oops! No words found. The video might not have captions.")
        return None

while True:
    url = input("Type a YouTube link (or 'quit' to stop): ")
    if url == 'quit':
        break
    text = get_words_from_link(url)
    if text:
        print("Words from the video:", text)
        with open("video_words_v2.txt", "w", encoding="utf-8") as file:  # Added encoding="utf-8" and new file name
            file.write(text)
        print("Words saved to 'video_words_v2.txt'!")