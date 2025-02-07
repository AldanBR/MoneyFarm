import json
import os
import requests

with open("/scripts/config.json", "r") as config_file:
    config = json.load(config_file)

# Obter lista de idiomas a serem postados no TikTok
postar_tiktok = config["postar_tiktok"]

VIDEO_DIR = "/videos"
tiktok_keys = config["tiktok"]

for lang in postar_tiktok:
    if lang not in tiktok_keys:
        continue

    video_path = f"{VIDEO_DIR}/charada_{lang}.mp4"
    files = {'video': open(video_path, 'rb')}

    response = requests.post(
        "https://open-api.tiktok.com/video/upload/",
        headers={"Authorization": f"Bearer {tiktok_keys[lang]}"},
        files=files
    )
    print(response.json())
