import json
import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Carregar configurações
with open("/scripts/config.json", "r") as config_file:
    config = json.load(config_file)

# Obter lista de idiomas a serem postados
postar_youtube = config["postar_youtube"]

VIDEO_DIR = "/videos"
youtube_keys = config["youtube"]

for lang in postar_youtube:
    if lang not in youtube_keys:
        continue

    youtube = build('youtube', 'v3', developerKey=youtube_keys[lang])

    title = json.load(open("/scripts/charadas.json"))[lang]["titulo"]
    video_path = f"{VIDEO_DIR}/charada_{lang}.mp4"

    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": "Charada do dia!",
                "tags": ["charada", "piada", "diversão"],
                "categoryId": "24"
            },
            "status": {
                "privacyStatus": "public"
            }
        },
        media_body=MediaFileUpload(video_path)
    )
    request.execute()
