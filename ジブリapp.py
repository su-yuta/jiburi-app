import streamlit as st
from PIL import Image
import requests
import pandas as pd
import time


st.title("*:green[Ghibrelux]*")
st.image('./jiburi_picture/アイコン.jpg',use_column_width=True)
#カテゴリーの選択
st.sidebar.write('絞り込み')

q1 = st.sidebar.selectbox(
    'Q1 新しい作品？古い作品？',
    ["N/A","New","Old"]
)
q2 = st.sidebar.selectbox(
    'Q2 どんな気分？',
    ["N/A","Sweet", "Bitter"]
)
q3 = st.sidebar.selectbox(
    'Q3 いつ見る？',
    ["N/A","Afternoon", "Night"]
)

hantei = q1 + q2 + q3

a = hantei

if a == "N/AN/A":
    y="ジブリ"
    z = "コーヒー"
elif a == "OldSweetNight":
    y="天空の城ラピュタ"
    img = Image.open('./jiburi_picture/laputa.jpg')
    z = "ナイトライト デカフェ"
    tips = 'パズーがシータの家でコーヒータイム'
elif a == "OldSweetAfternoon":
    y="魔女の宅急便"
    img = Image.open('./jiburi_picture/majotaku.jpg')
    z = "インスタントコーヒー"
    tips = 'おソノさんがキキにインスタントコーヒーを準備'
elif a == "OldBitterNight":
    y="もののけ姫"
    img = Image.open('./jiburi_picture/mononoke.jpg')
    z = "森のコーヒー"
    tips = 'アシタカとジコロがアコの家でコーヒータイム'
elif a == "OldBitterAfternoon":
    y="風の谷のナウシカ"
    img = Image.open('./jiburi_picture/nausicaa.jpg')
    z = "オーストラリアマウンテントップ2020"
    tips = 'ナウシカが、クリプトメリアの木の下でコーヒータイム'
elif a == "NewBitterNight":
    y="ハウルの動く城"
    img = Image.open('./jiburi_picture/howl.jpg')
    z = "チコリコーヒー"
    tips = 'ハウルがソフィーにコーヒーを出す。'
elif a == "NewBitterAfternoon":
    y="コクリコ坂から"
    img = Image.open('./jiburi_picture/kokurikozaka.jpg')
    z = "ウェスタンスタイル・コーヒー"
    tips = '誠が、カフェでウエスタンスタイルのコーヒーを飲む。'
elif a == "NewSweetNight":
    y="千と千尋の神隠し"
    img = Image.open('./jiburi_picture/chihiro.jpg')
    z = "台湾阿里山コーヒー"
    tips = '湯婆婆が千尋にコーヒーを出す。'
elif a == "NewSweetAfternoon":
    y="崖の上のポニョ"
    img = Image.open('./jiburi_picture/ponyo.jpg')
    z = "アメリカンブレンド"
    tips = '主人公の少年・佐藤が、母親の友人である藤崎先生の家でコーヒーを出してもらう。'

# elif a == "OldSweetAfternoon":
#     y="となりのトトロ"
#     img = Image.open('./jiburi_picture/totoro.jpg')
#     z = "コロンビアコーヒー"
#     tips = 'お母さんが、コーヒーを淹れながら父親に手紙を書く。'
# elif a == "NewBitterAfternoon":
#     y="紅の豚"
#     img = Image.open('./jiburi_picture/redpig.jpg')
#     z = "エスプレッソ"
#     tips = 'フィオがマダム・ジーナの家でコーヒーを淹れる。'

# ボタンが押されたかどうかを判定するフラグ
button_clicked = False

# Streamlitアプリのタイトルを設定
st.sidebar.title('ジブリの世界へ')

# ボタンを作成し、クリックされたかどうかをフラグに反映
if st.sidebar.button('入口'):
    button_clicked = True

# ボタンが押されたかどうかを表示
if button_clicked:
    st.write('### おすすめ作品は【' + y + ' 】です！')
    st.image(img,use_column_width=True)
    st.write('### ご一緒に【' + z + '】はいかがですか？')
    st.write('#### 実はこんなシーンが… ')
    st.write('####  「'+ tips + '」 ')
    coffee = z
else:
    st.write('ボタンが押されていません')

#楽天商品検索

REQUESTS_URL = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20220601'
APP_ID =  1001610610792400419

keyword = coffee

params = {
    'keyword':keyword,
    'applicationId':APP_ID,
    'format':'json',
    'sort':'-reviewAverage',
    'minPrice':100,
}

res = requests.get(REQUESTS_URL,params)
result = res.json()

items = result['Items']
items = [item['Item'] for item in items]

df = pd.DataFrame(items)[:5]
columns = ['itemName', 'itemPrice', 'availability','itemUrl','reviewAverage']

df=df[columns]
new_columns = ['商品名','価格','販売可','URL','レビュー']
df.columns = new_columns

st.write("### ↓購入はこちらから！↓")
st.markdown(df['URL'][0])