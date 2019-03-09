#coding:utf-8

from requests_toolbelt import SSLAdapter
import requests
import ssl
import sys

class TextToSpeech:
    def __init__(self, params):
        # パラメータの初期設定
        self.text = params["text"]
        self.speaker = params["speaker"]
        self.emotion = params["emotion"]
        self.emotion_level = params["emotion_level"]
        self.pitch = params["pitch"]
        self.speed = params["speed"]
        self.volume = params["volume"]

    def text_to_speech(self):
        print("はいってるぞよ！！！")       # デバッグコメント
        url = 'https://api.voicetext.jp/v1/tts'     # apiのurl
        API_KEY = '6otvdxnu4z5liju0'                # API_KEY

        payload = {                                 # パラメータ
            'text': self.text,
            'speaker': self.speaker,
            "emotion": self.emotion,
            "emotion_level": self.emotion_level,
            "pitch": self.pitch,
            "speed": self.speed,
            "volume": self.volume
            }

        s = requests.Session()
        s.mount(url, SSLAdapter(ssl.PROTOCOL_TLSv1))
        r = s.post(url, params=payload, auth=(API_KEY,''))

        print("status code:", r.status_code)
        if r.status_code != 200:        # エラーが起きた時のprintデバッグ
            print("error:", r.json()['error']['message'])
            sys.exit()

        with open('./voice/test.wav', 'wb') as f:   # wavファイルの生成
            f.write(r.content)

if __name__ == "__main__":
    # 呼び出し例
    params = {
        "text": "こんばんは！！",
        "speaker": "santa",
        "emotion": "anger",
        "emotion_level": 4,
        "pitch": 100,
        "speed": 50,
        "volume": 100
    }
    speech = TextToSpeech(params)
    speech.text_to_speech()