from collections import Counter
from math import sqrt


def pow_int1(n, p):
    return int(pow(n, p))


def pow_int2(n, p):
    product = 1

    while p > 0:
        if p % 2 != 0:
            product *= n
        p //= 2
        n *= n

    return product


def pow_int3(n, p):
    product = 1
    for _ in range(p):
        product *= n
    return product


def limit1(n):
    return int(sqrt(n)) + 1


def limit2(n):
    return n // 2 + 1


class SumOfProperDivisor1:
    def calculate_sum_of_proper_divisors(self, num):
        # 簡単のため、約数の和の計算部分を関数として切り出す。
        def calc(n):
            for i in range(2, self.limit(n)):
                if n % i == 0:
                    # (n/i) は i じゃない方の約数
                    another_i = n // i
                    # i じゃない方の約数が持つ約数情報
                    another_counter = self.prime_factors_counter[another_i]

                    # i で割り切れるなら、素因数情報は i じゃない方の素因数情報に i を加えたもので良い。
                    counter = Counter(another_counter)
                    counter[i] += 1

                    # 約数の和の公式(https://ja.wikipedia.org/wiki/%E7%B4%84%E6%95%B0#.E7.B4.84.E6.95.B0.E3.81.AE.E5.92.8C)を利用
                    sum_of_divisor = self.sums_of_divisors[another_i]

                    hoge = n // self.power(i, counter[i])
                    fuga = self.power(i, counter[i])
                    sum_of_divisor += self.sums_of_divisors[hoge] * fuga

                    return counter, sum_of_divisor, sum_of_divisor - n

            return Counter({n: 1}), n + 1, 1

        # num の約数の和がまだ計算されてなかったら、 num までの素因数情報をすべて計算し、 num までの約数の和情報を計算する。
        for n in range(len(self.prime_factors_counter), num+1):
            counter, sum_of_divisor, sum_of_proper_divisor = calc(n)
            self.prime_factors_counter.append(counter)
            self.sums_of_divisors.append(sum_of_divisor)
            self.sums_of_proper_divisors.append(sum_of_proper_divisor)

    def __init__(self, num=10000, limit_func=limit1, power_func=pow_int1):
        self.limit = limit_func
        self.power = power_func
        # 約数の和を計算するために、約数ではなく素因数の情報を構築する。
        self.prime_factors_counter = [{}, {}]
        self.sums_of_divisors = [1, 1]
        self.sums_of_proper_divisors = [0, 0]
        self.calculate_sum_of_proper_divisors(num)


class SumOfProperDivisor1_2:
    def calculate_sum_of_proper_divisors(self, num):
        for n in range(2, num+1):
            counter, sum_of_divisor = Counter({n: 1}), n + 1
            for i in range(2, self.limit(n)):
                if n % i == 0:
                    # (n/i) は i じゃない方の約数
                    another_i = n // i
                    # i じゃない方の約数が持つ約数情報
                    another_counter = self.prime_factors_counter[another_i]

                    # i で割り切れるなら、素因数情報は i じゃない方の素因数情報に i を加えたもので良い。
                    counter = another_counter.copy()
                    counter[i] += 1

                    # 約数の和の公式(https://ja.wikipedia.org/wiki/%E7%B4%84%E6%95%B0#.E7.B4.84.E6.95.B0.E3.81.AE.E5.92.8C)を利用
                    sum_of_divisor = self.sums_of_divisors[another_i]

                    hoge = n // self.power(i, counter[i])
                    fuga = self.power(i, counter[i])
                    sum_of_divisor += self.sums_of_divisors[hoge] * fuga

                    break

            self.prime_factors_counter[n] = counter
            self.sums_of_divisors[n] = sum_of_divisor
            self.sums_of_proper_divisors[n] = sum_of_divisor - n

    def __init__(self, num=10000, limit_func=limit1, power_func=pow_int1):
        self.limit = limit_func
        self.power = power_func

        self.prime_factors_counter = [None] * (num + 1)
        self.prime_factors_counter[1] = Counter()
        self.sums_of_divisors = [1] * (num + 1)
        self.sums_of_proper_divisors = [0] * (num + 1)
        self.calculate_sum_of_proper_divisors(num)


class SumOfProperDivisor2:
    def calculate_sum_of_proper_divisors(self, num):
        for i in range(2, num + 1):
            counter = self.prime_factors_counter[i]
            if counter:
                self.prime_factors_counter[i] = self.prime_factors_counter[i // counter].copy()
                self.prime_factors_counter[i][counter] += 1
                n = self.power(counter, self.prime_factors_counter[i][counter])
                self.sums_of_divisors[i] = self.sums_of_divisors[i // n]
                self.sums_of_divisors[i] *= (n * counter - 1) // (counter - 1)
                self.sums_of_proper_divisors[i] = self.sums_of_divisors[i] - i
            else:
                self.prime_factors_counter[i] = Counter({i: 1})
                self.sums_of_divisors[i] = i + 1
                self.sums_of_proper_divisors[i] = 1

                for kn in range(i * i, num+1, i):
                    if not self.prime_factors_counter[kn]:
                        self.prime_factors_counter[kn] = i

    def __init__(self, num=10000, limit_func=limit1, power_func=pow_int1):
        self.limit = limit_func
        self.power = power_func

        self.prime_factors_counter = [None] * (num + 1)
        self.prime_factors_counter[1] = Counter()
        self.sums_of_divisors = [1] * (num + 1)
        self.sums_of_proper_divisors = [0] * (num + 1)
        self.calculate_sum_of_proper_divisors(num)


def amicable_numbers(calculator):
    amicable_numbers = []
    n = len(calculator.sums_of_proper_divisors)
    for i in range(1, n):
        sum_of_proper_divisors = calculator.sums_of_proper_divisors[i]
        if i == sum_of_proper_divisors or sum_of_proper_divisors >= n:
            continue
        if i == calculator.sums_of_proper_divisors[sum_of_proper_divisors]\
                and (sum_of_proper_divisors, i) not in amicable_numbers:
            amicable_numbers.append((i, sum_of_proper_divisors))

    return amicable_numbers


num = 300000
calculator = SumOfProperDivisor2(num=num)
print(amicable_numbers(calculator))
calculator = SumOfProperDivisor1_2(num=num)
print(amicable_numbers(calculator))
calculator = SumOfProperDivisor1(num=num)
print(amicable_numbers(calculator))
