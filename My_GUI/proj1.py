from tkinter import *
import socket
import queue
import threading


class ServerThread(threading.Thread):
    def __init__(self, queue1, queue2):
        threading.Thread.__init__(self)
        self.temperature = queue1
        self.temperature_set = queue2
        self.MCU_set_temperature_Flag = False
        self.temp = ""

    def run(self):
        server_ip = "0.0.0.0"
        server_port = 7898
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((server_ip, server_port))
        server_socket.listen(1)
        print("Waiting for connection...")
        self.client_socket, client_address = server_socket.accept()
        self.client_socket.settimeout(10)  # 设置超时时间为10秒
        print("Connected to:", client_address)
        while True:
            while not self.temperature_set.empty():
                self.client_socket.send(self.temperature_set.get().encode())

            try:
                data = self.client_socket.recv(1024).decode()
                if data[:3] == "set":
                    self.temperature_set.put(data)
                    self.MCU_set_temperature_Flag = True
                    self.temp = data[3:]
                    self.client_socket.send("ok1".encode())
                else:
                    self.temperature.put(data)
                    self.client_socket.send("ok2".encode())
            except socket.timeout:
                print("Socket timed out, re-establishing connection")
                self.client_socket.close()
                self.client_socket, client_address = server_socket.accept()

        client_socket.close()
        server_socket.close()


class Application(Frame):
    def __init__(self, master, width, height, queue):
        super().__init__(master)
        self.temperature_set = queue
        self.width = width
        self.height = height
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.canvas = Canvas(self.master, width=self.width, height=self.height, bg="white")
        self.canvas.pack()

        self.rect = None
        self.scale = 0.8
        self.canvas.bind(("<MouseWheel>"), self.on_mouse_wheel)

        Button(self.master, text="RestoreGraphic", command=self.restore).place(relx=0.25, rely=0.81)

        self.v = StringVar()
        self.v.set("36")
        Label(self.master, text="设定温度:", font=("Arial", 10)).place(relx=0.48, rely=0.82)
        Entry(self.master, textvariable=self.v, width=5).place(relx=0.6, rely=0.82)
        Button(self.master, text="确定", command=self.transmit).place(relx=0.7, rely=0.81)

    def restore(self):
        self.scale = 0.8
        self.draw(self.x, self.y, color=self.ccolor, width=self.cwidth)

    def draw(self, x, y, color="black", width=1):
        if x:
            self.x = x[:]
            self.y = y[:]
            self.cwidth = width
            self.ccolor = color

            self.canvas.delete("all")  # 清除画布！
            block = 80
            self.canvas.create_line((block, 0, block, self.height), fill="black")
            self.canvas.create_line((0, self.height - block, self.width, self.height - block), fill="black")

            original = (block, self.height - block)
            Max_x = max(x)
            Min_x = min(x)
            Max_y = max(y)
            Min_y = min(y)
            stepx = Max_x - Min_x
            stepy = Max_y - Min_y
            ls = []
            for i in range(len(x)):
                yy = original[1] - int((y[i]) / stepy * (self.height - block) * self.scale)
                xx = original[0] + int((x[i]) / stepx * (self.width - block) * self.scale)
                ls.append(xx)
                ls.append(yy)
            self.canvas.create_line(ls, fill=color, width=width)

    def on_mouse_wheel(self, event):
        if event.delta > 0:
            self.scale += 0.05
        else:
            self.scale -= 0.05
        self.draw(self.x, self.y, color=self.ccolor, width=self.cwidth)

    def transmit(self):
        data = self.v.get()
        self.temperature_set.put("set" + data)


if __name__ == "__main__":
    temperature = queue.Queue()
    temperature_set = queue.Queue()
    MCU_set_temperature_Flag = False
    temp = ""

    i = 1
    x = list()
    y = list()

    width = 500
    height = 500
    root = Tk()
    root.title("temperature")
    root.geometry(f"{width}x{height}+400+200")
    app = Application(root, width * 0.8, height * 0.8, temperature_set)

    server_thread = ServerThread(temperature, temperature_set)


    def update_plot():
        global i, x, y, MCU_set_temperature_Flag
        while not temperature.empty():
            dot = temperature.get()
            dot_index = [j for j, char in enumerate(dot) if char == '.']

            y.append(float(dot[:dot_index[0] + 2]))
            x.append(i)
            i += 1
            for k in range(1, len(dot_index)):
                y.append(float(dot[dot_index[k - 1] + 2:dot_index[k] + 2]))
                x.append(i)
                i += 1

        if i >= 5:
            app.draw(x, y)
        if server_thread.MCU_set_temperature_Flag == True:
            app.v.set(server_thread.temp)
            server_thread.MCU_set_temperature_Flag = False
        root.after(50, update_plot)


    update_plot()

    server_thread.start()

    root.mainloop()
