import json
import requests
from datetime import datetime
import text_to_speech as txsp

# 関数の設定

class GetTalk:
    def __init__(self, params):
        # パラメータの初期設定
        self.send_text = params["send_text"]
        self.send_text = params["send_text"]
        self.nickname = params["nickname"]
        self.nicknameY = params["nicknameY"]
        self.sex = params["sex"]
        self.bloodtype = params["bloodtype"]
        self.birthdateY = params["birthdateY"]
        self.birthdateM = params["birthdateM"]
        self.birthdateD = params["birthdateD"]
        self.age = params["age"]
        self.constellations = params["constellations"]
        self.place = params["place"]
        self.mode = params["mode"]
        self.t = params["t"]

    def getTalk(self):
        APIKEY = '412f713264356f5168752e377a2f334d78552f2e6e54784176783442324e2f784973714962395177764d44'

        send_data = {
            'language':'ja-JP',
            'botId':'Chatting',
            'appId':'5a83b341-88ac-4be0-a5ca-2805803f0923',
            'voiceText':"",
            'clientData':{
                'option':{
                        'nickname':self.nickname,                                           # ニックネーム
                        'nicknameY':self.nicknameY,                                         # ニックネーム（読み）
                        'sex':self.sex,                                                     # 性別
                        'bloodtype':self.bloodtype,                                         # 血液型
                        'birthdateY':self.birthdateY,                                       # 誕生日（年）
                        'birthdateM':self.birthdateM,                                       # 誕生日（月）
                        'birthdateD':self.birthdateD,                                       # 誕生日（日）
                        'age':self.age,                                                     # 年齢
                        'constellations':self.constellations,                               # 星座
                        'place':self.place,                                                 # 地域
                        'mode':self.mode,                                                   # 対話モード（通常：dialog or しりとり：srtr）
                        't':self.t                                                          # キャラクタ（デフォルト：指定なし or 関西弁：kansai or 赤ちゃん：akachan）
                }
            },
            'appRecvTime':"",
            'appSendTime':""
        }

        headers = {'ContentType':'application/json;charset=UTF-8'}

        url = 'https://api.apigw.smt.docomo.ne.jp/naturalChatting/v1/dialogue?APIKEY={}'.format(APIKEY)

        while True:
            # メッセージ入力
            # send_text = input()

            # endで終了
            if(self.send_text == "end"):
                print("おしゃべりを終了します。")
                break
            
            send_data['voiceText'] = self.send_text
            send_time = datetime.now().strftime('%y-%m-%d %H:%M:%S')
            send_data['appSendTime'] = send_time

            # メッセージを送信
            r = requests.post(url,data=json.dumps(send_data),headers=headers)

            # 返信内容を取得
            return_data = r.json()
            return_message = return_data['systemText']['utterance']
            print(return_message)

            params = {
                "text": return_message,                                     # 200文字以内
                "speaker": "santa",                                         # 話者名
                # "emotion": "happiness",                                   # 感情
                # "emotion_level": 4,                                       # 感情レベル
                "pitch": 100,                                               # 音の高さ
                "speed": 100,                                               # 音声の速度
                "volume": 100                                               # 音声の大きさ
            }
            speech = txsp.TextToSpeech(params)
            speech.text_to_speech()



if __name__ == "__main__":
    params = {
            'nickname':'ヨウスケ',                                          # ニックネーム
            'nicknameY':'ヨウスケ',                                         # ニックネーム（読み）
            'sex':'男',                                                     # 性別
            'bloodtype':'B',                                                # 血液型
            'birthdateY':'1992',                                            # 誕生日（年）
            'birthdateM':'7',                                               # 誕生日（月）
            'birthdateD':'8',                                               # 誕生日（日）
            'age':'26',                                                     # 年齢
            'constellations':'蟹座',                                        # 星座
            'place':'東京',                                                 # 地域
            'mode':'',                                                      # 対話モード（通常：dialog or しりとり：srtr）
            't':'kansai'                                                    # キャラクタ（デフォルト：指定なし or 関西弁：kansai or 赤ちゃん：akachan）
    }

    getTalk = GetTalk(params)
    getTalk.getTalk()