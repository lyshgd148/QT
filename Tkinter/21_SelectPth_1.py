from tkinter import *
# from tkinter.colorchooser import *
from tkinter.filedialog import *

root = Tk()
root.geometry("530x300")


def test():
    f = askopenfilename(title="上传文件", initialdir="F:\OpenCV", filetypes=[("hahha", ".mp4")])
    show["text"] = f


show = Label(root, width=40, height=1, bg='pink')
show.pack()
Button(root, text="ChangeBG", command=test).pack()
mainloop()
