#coding:utf-8

from requests_toolbelt import SSLAdapter
import requests
import ssl
import sys

url = 'https://api.voicetext.jp/v1/tts'
API_KEY = 'YOUR API KEY'

payload = {
    'text': 'おはようございます',
    'speaker': 'hikari',
    }

s = requests.Session()
s.mount(url, SSLAdapter(ssl.PROTOCOL_TLSv1))
r = s.post(url, params=payload, auth=(API_KEY,''))

print "status code:", r.status_code
if r.status_code != 200:
    print "error:", r.json()['error']['message']
    sys.exit()

f = open("test.wav", 'wb')
f.write(r.content)
f.close()