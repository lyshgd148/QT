import wave
import pyaudio

# 打开.wav文件
wav_file = wave.open("BadApple.wav", 'rb')

# 初始化PyAudio
p = pyaudio.PyAudio()

# 打开音频流
stream = p.open(format=p.get_format_from_width(wav_file.getsampwidth()),
                channels=wav_file.getnchannels(),
                rate=wav_file.getframerate(),
                output=True)

# 一次性读取整个文件并播放
data = wav_file.readframes(wav_file.getnframes())
stream.write(data)

# 停止流和PyAudio
stream.stop_stream()
stream.close()
p.terminate()

# 关闭.wav文件
wav_file.close()