import tkinter
from tkinter import *
from tkinter import ttk
class Base(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        # ウィンドウサイズ
        master.geometry("900x720")
        master.title("伝説のあの人とついに会話できるようになりました。")

        

        # 入力用テキストボックス
        self.entryBox = tkinter.Entry(master=self)
        self.entryBox.pack()
        # テキストボックスの内容を表示するボタン
        self.button1 = tkinter.Button(master=self, text='テキストを送信する', width=30, bg='#5DB529')
        self.button1.bind("<ButtonRelease-1>", self.send_word)
        self.button1.pack()
    # def value_changed(*args):
    #     print('value = %d' % myval.get())



if __name__ == '__main__':
    root = tkinter.Tk()
    f = Base(master=root)
    f.pack()
    root.mainloop()
