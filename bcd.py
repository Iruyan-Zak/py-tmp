class BCDDigit:
    def __init__(self, upper_digit=None):
        self.value = 0
        self.upper_digit = upper_digit

    def shift_and_add(self, add_value=0):
        if self.value >= 5:
            self.value += 3

        self.value *= 2
        self.value += add_value

        carry_over = self.value // 16
        self.value %= 16

        if self.upper_digit:
            self.upper_digit.shift_and_add(carry_over)

    def __str__(self):
        s = ""
        val = self.value

        for _ in range(4):
            s = str(val % 2) + s
            val //= 2

        return s + f'({self.value})'

b = None
bcd = []
for i in range(3):
    b = BCDDigit(b)
    bcd.append(b)

for d in "10101010":
    bcd[2].shift_and_add(int(d))

for b in bcd:
    print(b, end=' ')
