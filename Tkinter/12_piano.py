from tkinter import *

root = Tk()
root.geometry("800x220")

f1 = Frame(root)
f1.pack()

f2 = Frame(root)
f2.pack()

btnText = ["流行风", "中国风", "日本风", "重金属", "轻音乐"]

for i in range(len(btnText)):
    Button(f1, text=btnText[i]).pack(side="left", padx=10, pady=5)

for i in range(20):
    Label(f2, width=5, height=10, borderwidth=1, relief="solid", bg="black" if i % 2 == 0 else "white") \
        .pack(side="left", padx=1)

root.mainloop()
