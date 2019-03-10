# coding= utf-8
import tkinter as tk
# wavファイル再生モジュール
from pydub import AudioSegment
from pydub.playback import play

# wavファイル
wav_file = "se_maoudamashii_chime12.wav"

class Base(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        master.geometry("1200x1000")
        master.title("色々な人に声を変えられるよ")
        self.pack()
        self.create_widgets()
        img = tk.PhotoImage(file='./Santa.gif')
        # 画像ウィジェットの配置(1行1列)
        label1 = tk.Label(root, image=img)
        label1.pack()

        
    def create_widgets(self):
        label = tk.Label(master=self, text="モード選択", font=(u'ＭＳ ゴシック', 40,"bold"),bg="red")
        label.pack()

        self.secret_button = tk.Button(master=self, text='会話', width=30, bg='#5DB529')
        self.secret_button.bind("<ButtonRelease-1>", self.send_word)
        self.secret_button.pack()

        self.siritori_button = tk.Button(master=self, text='しりとり', width=30, bg='#5DB529')
        self.siritori_button.bind("<ButtonRelease-1>", self.send_word)
        self.siritori_button.pack()

        self.repeat_button = tk.Button(master=self, text='おうむ返し', width=30, bg='#5DB529')
        self.repeat_button.bind("<ButtonRelease-1>", self.send_word)
        self.repeat_button.pack()

        label = tk.Label(master=self, text="人物選択",font=(u'ＭＳ ゴシック', 40,"bold"),bg="green")
        label.pack()


        self.men_button = tk.Button(master=self, text='男性', width=30, bg='#5DB529')
        self.men_button.bind("<ButtonRelease-1>", self.send_word)
        self.men_button.pack()

        self.haruka_button = tk.Button(master=self, text='はるか(女性)', width=30, bg='#5DB529')
        self.haruka_button.bind("<ButtonRelease-1>", self.send_word)
        self.haruka_button.pack()

        self.hikari_button = tk.Button(master=self, text='ひかり(女性)', width=30, bg='#5DB529')
        self.hikari_button.bind("<ButtonRelease-1>", self.send_word)
        self.hikari_button.pack()

        self.ken_button = tk.Button(master=self, text='健(男性)', width=30, bg='#5DB529')
        self.ken_button.bind("<ButtonRelease-1>", self.send_word)
        self.ken_button.pack()

        self.santa_button = tk.Button(master=self, text='サンタさん', width=30, bg='#5DB529')
        self.santa_button.bind("<ButtonRelease-1>", self.send_word)
        self.santa_button.pack()

        self.bear_button = tk.Button(master=self, text='凶暴なクマ', width=30, bg='#5DB529')
        self.bear_button.bind("<ButtonRelease-1>", self.send_word)
        self.bear_button.pack()


        # テキストボックス
        self.entryBox = tk.Entry(master=self,width=80)
        self.entryBox.pack()

        # テキストボックスの内容を表示するボタン
        self.button1 = tk.Button(master=self, text='確定する', bg='#F0F8FF', fg='#FF4500', width=30)
        self.button1.bind("<ButtonRelease-1>", self.send_word)
        self.button1.pack()

                 

        # pitch
        c = tk.Label(text="テンポ",bg='yellow')
        c.place(x=500, y=440)
        self.pitch = tk.DoubleVar(master=self)
        # self.scale1 = tk.Scale(master=self, variable=self)
        self.scale1 = tk.Scale(master=self,command=self.pitch_value)
        self.scale1.pack(anchor=tk.CENTER)


        # speed
        a = tk.Label(text='速さ',bg='yellow')
        a.place(x=500, y=540)
        self.speed = tk.DoubleVar(master=self)
        self.scale2 = tk.Scale(master=self,command=self.speed_value)
        self.scale2.pack(anchor=tk.CENTER)

        # volume
        b = tk.Label(text='ボリューム',bg='yellow')
        b.place(x=500, y=640)
        self.volume = tk.DoubleVar(master=self)        
        self.scale3 = tk.Scale(master=self,command=self.volume_value)
        self.scale3.pack(anchor=tk.CENTER)


        # 音声再生ボタン
        self.hi_there = tk.Button(self,width=80)
        self.hi_there["text"] = "音声再生ボタン"
        self.hi_there["command"] = self.say
        self.hi_there.pack(side="top")


    def speed_value(self, val):
        print(val)
        speed_val = val
        return speed_val

    def pitch_value(self, val):
        print(val)
        pitch_val = val
        return pitch_val

    def volume_value(self, val):
        print(val)
        volume_val = val
        return volume_val
        

    def say(self):
        print("音声を流す")
        sound = AudioSegment.from_file(wav_file,"wav")
        play(sound)

    def select_mode():
        print("モードの選択")
    
    def send_word(self, event):
        print(self.entryBox.get())

        params = {
            "text": self.entryBox.get(),     # 200文字以内
            "speaker": "santa",                                         # 話者名
            "emotion": "happiness",                                     # 感情
            "emotion_level": 4,                                         # 感情レベル
            "pitch":  100,                                               # 音の高さ
            "speed": 100,                                                # 音声の速度
            "volume": 100                                              # 音声の大きさ
        }
        print(params)

root = tk.Tk()
app = Base(master=root)
app.mainloop()
