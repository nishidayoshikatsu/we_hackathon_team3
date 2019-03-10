import tkinter as tk



class Base(tk.Frame):
    pitch_value = 0
    speed_value = 0
    volume_value = 0
    def __init__(self, master=None):
        super().__init__(master)
        master.geometry("1200x1000")
        master.title("伝説のあの人とついに会話できるようになりました。")
        self.pack()
        self.create_widgets()
        
    def create_widgets(self):

        label = tk.Label(master=self, text="会話モード選択")
        label.pack()
        self.siritori_button = tk.Button(master=self, text='しりとり', width=30, bg='#5DB529')
        self.siritori_button.bind("<ButtonRelease-1>", self.send_word)
        self.siritori_button.pack()

        self.repeat_button = tk.Button(master=self, text='おうむ返し', width=30, bg='#5DB529')
        self.repeat_button.bind("<ButtonRelease-1>", self.send_word)
        self.repeat_button.pack()

        self.seacret_button = tk.Button(master=self, text='シークレット', width=30, bg='#5DB529')
        self.seacret_button.bind("<ButtonRelease-1>", self.send_word)
        self.seacret_button.pack()

        label = tk.Label(master=self, text="人物選択")
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
        self.entryBox = tk.Entry(master=self)
        self.entryBox.pack()

        # テキストボックスの内容を表示するボタン
        self.button1 = tk.Button(master=self, text='確定する', width=30, bg='#5DB529')
        self.button1.bind("<ButtonRelease-1>", self.send_word)
        self.button1.pack()

                 

        # pitch
        c = tk.Label(text="テンポ")
        c.place(x=500, y=390)
        self.pitch = tk.DoubleVar(master=self)
        # self.scale1 = tk.Scale(master=self, variable=self)
        self.scale1 = tk.Scale(master=self,command=self.pitch_value)
        self.scale1.pack(anchor=tk.CENTER)


        # speed
        a = tk.Label(text='速さ')
        a.place(x=500, y=480)
        self.speed = tk.DoubleVar(master=self)
        self.scale2 = tk.Scale(master=self,command=self.speed_value)
        self.scale2.pack(anchor=tk.CENTER)

        # volume
        b = tk.Label(text='ボリューム')
        b.place(x=500, y=580)
        self.volume = tk.DoubleVar(master=self)        
        self.scale3 = tk.Scale(master=self,command=self.volume_value)
        self.scale3.pack(anchor=tk.CENTER)


        # 音声再生ボタン
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "音声再生ボタン"
        self.hi_there["command"] = self.say
        self.hi_there.pack(side="top")


    def speed_value(self, val):
        print(val)
        speed_val = val
    def pitch_value(self, val):
        print(val)
        pitch_val = val
    def volume_value(self, val):
        print(val)
        volume_val = val

    def say(self):
        print("音声を流す")

    def select_mode():
        print("モードの選択")
    
    def send_word(self, event):
        print(self.entryBox.get())
        print(self.volume.get())

        params = {
            "text": self.entryBox.get(),     # 200文字以内
            "speaker": "santa",                                         # 話者名
            "emotion": "happiness",                                     # 感情
            "emotion_level": 4,                                         # 感情レベル
            "pitch": self.pitch_value,                                               # 音の高さ
            "speed": self.speed_value,                                                # 音声の速度
            "volume": self.volume_value                                               # 音声の大きさ
        }
        print(params)

root = tk.Tk()
app = Base(master=root)
app.mainloop()
