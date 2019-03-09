import tkinter
import text_to_speech as tts
class Base(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        # 入力用テキストボックス
        self.entryBox = tkinter.Entry(master=self)
        self.entryBox.pack()
        # テキストボックスの内容を表示するボタン
        self.button1 = tkinter.Button(master=self, text='show', width=20)
        self.button1.bind("<ButtonRelease-1>", self.show_word)
        self.button1.pack()

    def show_word(self, event):
        print(self.entryBox.get())
        params = {
            "text": self.entryBox.get(),     # 200文字以内
            "speaker": "santa",                                         # 話者名
            "emotion": "happiness",                                     # 感情
            "emotion_level": 4,                                         # 感情レベル
            "pitch": 100,                                               # 音の高さ
            "speed": 100,                                                # 音声の速度
            "volume": 100                                               # 音声の大きさ
        }
        speech = tts.TextToSpeech(params)
        speech.text_to_speech()

if __name__ == "__main__":      # このファイルが直接実行されたときに以下を実行
    root = tkinter.Tk()     # 始まり
    f = Base(master=root)
    f.pack()
    root.mainloop()         # 終わり