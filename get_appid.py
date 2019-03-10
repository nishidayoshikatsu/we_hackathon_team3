import json
import requests

# 関数の設定
# ユーザーごとにappIdを取得する。
# appIdごとに会話状況を管理する。

class GetAppId:
    def getAppId(self):
        send_data = {
            "botId":"Chatting",     # 固定値
            "appKind":"Chatbot"     # 固定値
        }

        headers = {'ContentType':'application/json;charset=UTF-8'}

        APIKEY = '412f713264356f5168752e377a2f334d78552f2e6e54784176783442324e2f784973714962395177764d44'
        url = 'https://api.apigw.smt.docomo.ne.jp/naturalChatting/v1/registration?APIKEY={}'.format(APIKEY)

        r = requests.post(url,data=json.dumps(send_data),headers=headers)
        print(r.status_code)
        return_data = r.json()
        print(return_data)

        # return return_data
    
if __name__ == "__main__":
    appId = GetAppId()
    appId.getAppId()