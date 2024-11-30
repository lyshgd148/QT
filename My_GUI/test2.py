import serial

# 打开串口
ser = serial.Serial('COM3', 9600, timeout=1)  # 串口名称和波特率

try:
    if ser.is_open:
        print("串口已打开")

    while True:
        # 读取数据
        data = ser.readline().decode('utf-8').strip()
        if data:
            print("接收到数据:", data)

except serial.SerialException as e:
    print("串口通讯出现异常:", e)

finally:
    # 关闭串口
    if ser.is_open:
        ser.close()
        print("串口已关闭")