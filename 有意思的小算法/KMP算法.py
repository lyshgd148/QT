import sys


def Next(s):
    n = len(s)
    temp = list()
    temp.append(0)
    for i in range(1, n):
        if s[temp[i - 1]] == s[i]:
            temp.append(temp[i - 1] + 1)
        else:
            if s[temp[temp[i - 1] - 1]] == s[i]:
                temp.append(temp[temp[i - 1] - 1] + 1)
            else:
                temp.append(0)
    return temp


def Kmp(S, s, nxt, i=0, j=0):
    global result
    if s[j] == S[i]:
        i += 1
        j += 1
    else:
        if j == 0:
            i += 1
        else:
            j = nxt[j - 1]
    if j == len(s):
        j = 0
        result.append(i - len(s))
    if i == len(S):
        return
    Kmp(S, s, nxt, i, j)


result = list()
S = """一直以来，推动数学发展的动力很多都来自于对公式的推广，就是将公式的适用范围扩大。 例如，我们通常定义的阶乘只能应用在正整数上。你一定很好奇，如何对一个小数进行阶乘，比如3.5。 由于之前的定义对小数不适用了，我们需要找另外的方法来计算小数的阶乘并且需要同样适用于整数。

1730年欧拉发现了一种在实数和复数域上扩展的阶乘，被称为伽玛函数。 （参见 http://en.wikipedia.org/wiki/Gamma_function）

欧拉还发现了很多类似的扩展数学定义的函数，复指数函数就是其中之一。

通常指数的定义是重复的乘以自身， 例如 φ3=φ⋅φ⋅φ
 。 但是定义不能应用在非整数指数上。
然后我们发现，指数可以表示成幂级数的形式：
eφ=1+φ+φ2/2!+φ3/3!+...
这个定义就可以适用于任何实数，虚数以及复数了。如果我们使用一个纯虚数 iφ
 代入得到：
eiφ=1+iφ−φ2/2!−iφ3/3!+...
对上式的各项重新排列后，我们可以发现它等价于：
eiφ=cosφ+isinφ
这个公式被称为欧拉公式，详见 http://en.wikipedia.org/wiki/Euler’s_formula 它意味着 eiφ
 是一个模为1的复数，对应于复平面中单位圆上的一点， 而参数 φ
 就是这个点的向量与x轴（实轴）之间的夹角。
如果指数是一个复数的话，会得到：
ea+iφ=eaeiφ=Aeiφ
这里 A 表示幅值， eiφ
 是单位复指数，表示相角。
Numpy提供了 exp 方法来计算复指数:
>>> phi = 1.5
>>> z = np.exp(1j * phi)
>>> z
(0.0707+0.997j)
Python中使用 j 来表示单位虚数（就是上面使用的 i ）。一个以 j 结尾的数，表示了一个纯虚数， 例如， 1j 其实就是 i 。
当 np.exp 的参数是虚数或者复数的时候，其结果是也是一个复数类型（ np.complex128 ） ， 实际上就是两个分别代表实部和虚部的浮点数。这个例子中，结果为 0.0707+0.997j 。
复数有两个属性， real 和 imag ，分别代表它的实部和虚部:
>>> z.real
0.0707
>>> z.imag
0.997
可以使用Python内置的 abs 或是Numpy中的 np.absolute 来计算复数的模值:
>>> abs(z)
1.0
>>> np.absolute(z)
1.0
使用 np.angle 可以计算复数的相角:
>>> np.angle(z)
1.5
这个例子证明了 eiφ
 确实是一个模为1，相角为1.5弧度的复数。
7.2 复信号¶
如果 φ(t)
 变成时间的人工智能函数，那么 eiφ(t)
 也变成了时间的函数。 准确的说，可以写成：
eiφ(t)=cosφ(t)+isinφ(t)
这个式子描述了一个随时间变化的量，因此它是一个信号，准确的说叫做 复指数信号 。

这个例子中，信号的频率是一定的，如果把 φ(t)=2πft
 ，那么：
ei2πft=cos2πft+isin2πft
把初始相位 φ0
 加入后得到：
ei(2πft+φ0)
thinkdsp 中实现了复信号 - ComplexSinusoid
class ComplexSinusoid(Sinusoid):
    def evaluate(self, ts):
            phases = PI2 * self.freq * ts + self.offset
            ys = self.amp * np.exp(1j * phases)
            return ys
            
ComplexSinusoid 类继承了父类 Sinusoid 的构造函数，并复写了 evaluate 以计算信号的值， 它与 Sinusoid 相比只是用 np.exp 代替了 np.sin 。
一个复信号的值是复数的Numpy数组:
>>> signal = thinkdsp.ComplexSinusoid(freq=1, amp=0.6, offset=1)
>>> wave = signal.make_wave(duration=1, framerate=4)
>>> wave.ys
[ 0.324+0.505j -0.505+0.324j -0.324-0.505j  0.505-0.324j]
这个信号的频率是1Hz，幅值是0.6，初始相位是1弧度。例子中计算了从0~1s的四个采样点的值， 结果都是复数。
7.3 合成¶
与实的正弦信号一样，我们可以将不同频率和幅值的复信号加起来生成一个复合信号， 也就是复"""
s = "人工智能"
nxt = Next(s)
sys.setrecursionlimit(2*len(S))
Kmp(S, s, nxt)
print(result)

n = len(s)
m = len(S)
for i in range(len(result)):  # 将匹配到的字符串打印下来，并且多打印一个，便于判断
    if (result[i] + n) < m:
        print(S[result[i]:result[i] + n + 1])
    else:
        print(S[result[i]:result[i] + n])
