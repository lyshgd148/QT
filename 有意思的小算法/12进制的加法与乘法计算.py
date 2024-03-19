# 12进制:0,1,2,3,4,5,6,7,8,9,a,b
import copy


class Twelve_binary(object):
    def __init__(self, num1, num2):
        self.num1 = str(num1)
        self.num2 = str(num2)
        self.num1 = list(map(str, self.num1))
        self.num2 = list(map(str, self.num2))
        self.num11 = copy.copy(self.num1)
        self.num22 = copy.copy(self.num2)
        self.len_num1 = len(self.num1)
        self.len_num2 = len(self.num2)
        self.add_result_list = [0] * (max(self.len_num1, self.len_num2) + 1)
        self.mult_result_list = [0] * (self.len_num1 + self.len_num2)
        self.twelve_map = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6',
                           7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b'}
        self.twelve_map_reverse = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                                   '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11}
        if self.len_num1 > self.len_num2:
            for i in range(self.len_num1 - self.len_num2):
                self.num22.insert(0, '0')
        elif self.len_num1 < self.len_num2:
            for i in range(self.len_num2 - self.len_num1):
                self.num11.insert(0, '0')

    def twelve_add(self):
        carry = 0
        s = ''
        for i in range(len(self.num11)):
            x = self.twelve_map_reverse[self.num11[len(self.num11) - i - 1]]
            y = self.twelve_map_reverse[self.num22[len(self.num22) - i - 1]]
            z = x + y + carry
            carry = z // 12
            z = z % 12
            self.add_result_list[len(self.num11) - i] = self.twelve_map[z]
        self.add_result_list[0] = carry
        index = 0 if self.add_result_list[0] != 0 else 1
        result = self.add_result_list[index:]
        result = ''.join(list(map(str, result)))
        print(f'十二进制相加{s.join(self.num1)}+{s.join(self.num2)}:', result)
        return result

    # 用卷积来计算乘法
    def twelve_mult(self):
        s = ''
        for i in range(self.len_num1 - 1, -1, -1):
            x = self.twelve_map_reverse[self.num1[i]]
            for j in range(self.len_num2 - 1, -1, -1):
                y = self.twelve_map_reverse[self.num2[j]]
                self.mult_result_list[i + j + 1] += (x * y) * 12 ** (-i - j - 2 + self.len_num1 + self.len_num2)
        num_sum = sum(self.mult_result_list)
        length = self.len_num2 + self.len_num1
        while True:
            x = num_sum % 12
            num_sum = num_sum // 12
            self.mult_result_list[length - 1] = self.twelve_map[x]
            length -= 1
            if length == 0:
                break
        index = 0 if self.mult_result_list[0] != '0' else 1
        result = ''.join(self.mult_result_list[index:])
        print(f'十二进制相乘{s.join(self.num1)}*{s.join(self.num2)}:', result)
        return result

    def main(self):
        self.twelve_add()
        self.twelve_mult()


if __name__ == '__main__':
    test = Twelve_binary("1a", '2b')
    test.main()
