import wave
import pyaudio
import matplotlib.pyplot as plt
import numpy as np


def Collect_voice(name):
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 1

    audio = pyaudio.PyAudio()
    print("Recording...")
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    list_data = np.frombuffer(b''.join(frames[:]), dtype=np.int16)
    time = np.linspace(0, len(list_data) / RATE, num=len(list_data))

    stream.stop_stream()
    stream.close()
    audio.terminate()

    waveFile = wave.open(name, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
    print("Successful")
    return time, list_data


def Play_void(name, RATE):
    wav_file = wave.open(name, 'rb')
    p = pyaudio.PyAudio()
    # 打开音频流
    stream = p.open(format=p.get_format_from_width(wav_file.getsampwidth()),
                    channels=wav_file.getnchannels(),
                    rate=wav_file.getframerate(),
                    output=True)

    data = wav_file.readframes(1024)
    list_data = list()
    list_data.append(data)

    while data:
        stream.write(data)
        data = wav_file.readframes(1024)
        list_data.append(data)
    list_data = np.frombuffer(b''.join(list_data), dtype=np.int16)
    time = np.linspace(0, len(list_data) / RATE, num=len(list_data))
    # 关闭流和PyAudio
    stream.stop_stream()
    stream.close()
    p.terminate()
    # 关闭音频文件
    wav_file.close()
    print("Play Over!")
    return time, list_data


def Date2voice(name, data):
    with wave.open(name, 'wb') as wav_file:
        # 配置 WAV 文件参数
        wav_file.setnchannels(1)  # 单声道
        wav_file.setsampwidth(2)  # 2 字节（16 位）
        wav_file.setframerate(44100)  # 采样频率
        wav_file.setnframes(len(data))  # 数据帧数
        wav_file.setcomptype('NONE', 'NONE')
        # 将 NumPy 数组中的数据写入 WAV 文件
        wav_file.writeframes(data.tobytes())


if __name__ == '__main__':
    # time, data = Collect_voice('./sound/test.wav')
    time1, data1 = Play_void('./sound/impulse.wav', 44100)

    # plt.figure()
    # plt.plot(time, data)

    plt.figure()
    plt.plot(time1, data1)

    # Date2voice('./sound/impulse.wav', data1[28224:])
    plt.show()
