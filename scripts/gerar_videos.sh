#!/bin/bash
mkdir -p /videos

# Carregar as charadas e configurações do JSON
CHARADAS_JSON=$(cat /scripts/charadas.json)
CONFIG_JSON=$(cat /scripts/config.json)
VIDEO_CONFIG=$(cat /scripts/video_config.json)

# Obter configurações do vídeo
BACKGROUND=$(jq -r ".background" <<< "$VIDEO_CONFIG")
SOM=$(jq -r ".som" <<< "$VIDEO_CONFIG")
RESOLUCAO=$(jq -r ".resolucao" <<< "$VIDEO_CONFIG")
DURACAO=$(jq -r ".duracao" <<< "$VIDEO_CONFIG")

# Obter os idiomas que devem ser gerados
IDIOMAS=$(jq -r ".gerar[]" <<< "$CONFIG_JSON")

# Caminho da fonte (instale no container se necessário)
FONT_PATH="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

for lang in $IDIOMAS; do
    pergunta=$(jq -r ".${lang}.pergunta" <<< "$CHARADAS_JSON")
    resposta=$(jq -r ".${lang}.resposta" <<< "$CHARADAS_JSON")

    ffmpeg -loop 1 -i "$BACKGROUND" -vf "
    drawtext=text='$pergunta':fontfile=$FONT_PATH:fontsize=60:fontcolor=white:x=(w-text_w)/2:y=200,
    drawtext=text='$resposta':fontfile=$FONT_PATH:fontsize=60:fontcolor=yellow:x=(w-text_w)/2:y=400:enable='gte(t,5)'" \
    -t "$DURACAO" -s "$RESOLUCAO" -pix_fmt yuv420p -c:v libx264 -c:a aac -i "$SOM" -shortest /videos/charada_$lang.mp4
done
