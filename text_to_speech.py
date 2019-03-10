#coding:utf-8

from requests_toolbelt import SSLAdapter
import requests
import ssl
import sys
import random
import analyze_sentence as ana  #analyze_sentence.pyの読み込み

class TextToSpeech:
    def __init__(self, params):
        # パラメータの初期設定
        self.text = params["text"]
        self.speaker = params["speaker"]
        #self.emotion = params["emotion"]
        #self.emotion_level = params["emotion_level"]
        self.pitch = params["pitch"]
        self.speed = params["speed"]
        self.volume = params["volume"]

    def negaposi_count(self):
        analyze = ana.NaturalLanguageUnderstanding()
        result = analyze.negaposi_analyze(self.text)
        emotions = {"positive": 0, "negative": 0}
        for analyze_list in result:
            if analyze_list["label"] == "positive":
                emotions["positive"] += 1
            elif analyze_list["label"] == "negative":
                emotions["negative"] += 1
            else:
                print("うそだ！！！！！")
                print(analyze_list)

        print(emotions)
        return emotions

    def decide_emotion(self):
        info = self.negaposi_count()
        p = 0.5

        if info["positive"] > info["negative"]:
            self.emotion = "happiness"
        elif info["positive"] < info["negative"]:
            self.emotion = "sadness"
        else:
            if random.random() > p:
                self.emotion = "happiness"
            else:
                if random.random() > p:
                    self.emotion = "anger"
                else:
                    self.emotion = "sadness"

        print(self.emotion)

    def decide_emotion_level(self):
        info = self.negaposi_count()

        if info["positive"] == 0 and info["negative"] == 0:
            self.emotion_level = 1
            return

        if self.emotion == "happiness":
            level = info["positive"] / (info["positive"] + info["negative"])
        else:
            level = info["negative"] / (info["positive"] + info["negative"])

        print(level)

        if level >= 0.75:
            self.emotion_level = 4
        elif level >= 0.5:
            self.emotion_level = 3
        elif level >= 0.25:
            self.emotion_level = 2
        else:
            self.emotion_level = 1

        print(self.emotion_level)

    def text_to_speech(self):
        print("はいってるぞよ！！！")       # デバッグコメント
        url = 'https://api.voicetext.jp/v1/tts'     # apiのurl
        API_KEY = '6otvdxnu4z5liju0'                # API_KEY

        self.decide_emotion()
        self.decide_emotion_level()

        parameters = {                                 # パラメータ
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
        r = s.post(url, params=parameters, auth=(API_KEY,''))

        print("status code:", r.status_code)
        if r.status_code != 200:        # エラーが起きた時のprintデバッグ
            print("error:", r.json()['error']['message'])
            sys.exit()

        with open('./voice/test.wav', 'wb') as f:   # wavファイルの生成
            f.write(r.content)

if __name__ == "__main__":      # このファイルが直接実行されたときに以下を実行
    # 呼び出し例
    params = {
        "text": "おはようございました",     # 200文字以内
        "speaker": "santa",                                         # 話者名
        "emotion": "happiness",                                     # 感情
        "emotion_level": 4,                                         # 感情レベル
        "pitch": 100,                                               # 音の高さ
        "speed": 100,                                                # 音声の速度
        "volume": 100                                               # 音声の大きさ
    }
    speech = TextToSpeech(params)
    speech.text_to_speech()