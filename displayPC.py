import tkinter
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
if __name__ == '__main__':
    root = tkinter.Tk()
    f = Base(master=root)
    f.pack()
    root.mainloop()
