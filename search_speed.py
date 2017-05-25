from timeit import timeit

print("Set の検索: {0:4.3f} 秒".format(
    timeit('"b" in s', 's = {"a" * i for i in range(int(1e7))}', number=10)
    ))
print("List の検索: {0:4.3f} 秒".format(
    timeit('"b" in l', 'l = ["a" * i for i in range(int(1e7))]', number=10)
    ))
