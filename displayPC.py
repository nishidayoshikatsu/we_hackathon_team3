import tkinter as tk

class Base(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        master.geometry("900x720")
        master.title("伝説のあの人とついに会話できるようになりました。")
        self.pack()
        self.create_widgets()
        
    def create_widgets(self):
       
        mb = tk.Menubutton(root, text="Subjects", relief=tk.RAISED)
        mb.grid()
        mb.menu = tk.Menu(mb, tearoff=0)
        mb["menu"] = mb.menu

        Var1 = tk.IntVar()
        Var2 = tk.IntVar()
        Var3 = tk.IntVar()
        Var4 = tk.IntVar()
        Var5 = tk.IntVar()
        Var6 = tk.IntVar()

        mb.menu.add_checkbutton(label="男性", variable=Var1)
        mb.menu.add_checkbutton(label="はるか(女性)", variable=Var2)
        mb.menu.add_checkbutton(label="ひかり(女性)", variable=Var3)
        mb.menu.add_checkbutton(label="健(男性)", variable=Var4)
        mb.menu.add_checkbutton(label="サンタさん", variable=Var5)
        mb.menu.add_checkbutton(label="凶暴なクマ", variable=Var6)
        mb.pack()


        # テキストボックス
        self.entryBox = tk.Entry(master=self)
        self.entryBox.pack()

        # テキストボックスの内容を表示するボタン
        self.button1 = tk.Button(master=self, text='テキストを送信する', width=30, bg='#5DB529')
        self.button1.bind("<ButtonRelease-1>", self.send_word)
        self.button1.pack()

                 
        # ファイル再生ボタン
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "音声再生ボタン"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        c = tk.Label(text="テンポ")
        c.place(x=100, y=200)
        # pitch
        var = tk.DoubleVar()
        scale = tk.Scale(root, variable=var)
        scale.pack(anchor=tk.CENTER)
        button = tk.Button(root, text="Get Scale Value")
        button.pack(anchor=tk.CENTER)
        label = tk.Label(root)
        label.pack(fill = 'x',side = 'left')
    # speed
        a = tk.Label(text='速さ')
        a.place(x=100, y=300)
        var = tk.DoubleVar()

        scale = tk.Scale(root, variable=var)
        scale.pack(anchor=tk.CENTER)
        button = tk.Button(root, text="Get Scale Value")
        button.pack(anchor=tk.CENTER)
        label = tk.Label(root)
        label.pack(fill = 'x', side = 'left')

        b = tk.Label(text='ボリューム')
        b.place(x=100, y=400)
    # volume
        var = tk.DoubleVar()
        
        scale = tk.Scale(root, variable=var)
        scale.pack(anchor=tk.CENTER)
        button = tk.Button(root, text="Get Scale Value")
        button.pack(anchor=tk.CENTER)
        label = tk.Label(root)
        label.pack(fill = 'x', side = 'left')


        
    def say_hi(self):
        print("hi there, everyone!")
    
    def send_word(self, event):
        print(self.entryBox.get())
        self.status = tk.Label(master=self, text="Now processing..",
        borderwidth=2, relief="groove")
        self.status.pack(side=tk.BOTTOM, fill=tk.X)

root = tk.Tk()
app = Base(master=root)
app.mainloop()
