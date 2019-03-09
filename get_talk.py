import json
import requests
# import get_appid
from datetime import datetime

# 関数の設定

# @app.route("/")
# def top()

APIKEY = 'APIKEY'

send_data = {
    'language':'ja-JP',
    'botId':'Chatting',
    'appId':'5a83b341-88ac-4be0-a5ca-2805803f0923',
    'voiceText':"",
    'clientData':{
        'option':{
            'nickname':'ヨウスケ',
            'nicknameY':'ヨウスケ',
            'sex':'男',
            'bloodtype':'B',
            'birthdateY':'1992',
            'birthdateM':'7',
            'birthdateD':'8',
            'age':'26',
            'constellations':'蟹座',
            'place':'東京',
            'mode':'',
            't':'kansai'
        }
    },
    'appRecvTime':"",
    'appSendTime':""
}

headers = {'ContentType':'application/json;charset=UTF-8'}

url = 'https://api.apigw.smt.docomo.ne.jp/naturalChatting/v1/dialogue?APIKEY={}'.format(APIKEY)

while True:
    # メッセージ入力
    send_text = input()

    # endで終了
    if(send_text == "end"):
        print("おしゃべりを終了します。")
        break
    
    send_data['voiceText'] = send_text
    send_time = datetime.now().strftime('%y-%m-%d %H:%M:%S')
    send_data['appSendTime'] = send_time

    # メッセージを送信
    r = requests.post(url,data=json.dumps(send_data),headers=headers)

    # 返信内容を取得
    return_data = r.json()
    return_message = return_data['systemText']['expression']
    print(return_message)
