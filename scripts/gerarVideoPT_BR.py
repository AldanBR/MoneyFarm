import json
from moviepy import TextClip, AudioFileClip, ImageClip, CompositeVideoClip

font = "times"
resolucaoShorts = (216, 480)

audio = AudioFileClip('./assets/audio-bg.mp3')

bgImg = ImageClip('./assets/img-bg.png', duration =audio.duration)

with open("charada.json", "r", encoding="utf-8") as f:
    data = json.load(f)

pergunta_charada = data["charada"]
resposta_charada = data["resposta"]

resposta = TextClip(
    font=font,
    font_size= 40,
    text_align='center',
    stroke_color="black",
    stroke_width=1,
    text=resposta_charada,
    size= resolucaoShorts,
    bg_color="#ffffff00",
    method="caption",
    color=(255, 255, 0, 200),
).with_position((10, 40)).with_start(9).with_duration((audio.duration) - 9)

pergunta = TextClip(
    font=font,
    text_align='center',
    stroke_color="black",
    stroke_width=1,
    font_size= 30,
    text=pergunta_charada,
    size= resolucaoShorts,
    bg_color="#ffffff00",
    method="caption",
    color=(255, 0, 0, 200),
).with_position('center')  

pergunta = pergunta.with_duration(audio.duration)
compose = CompositeVideoClip([bgImg, pergunta, resposta])
compose.audio = audio


compose.write_videofile("video_shorts.mp4", fps=24)