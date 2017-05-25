from itertools import takewhile

question = "Hello"

def generator():
    while True:
        print(question)
        yield input()

list(takewhile(question.__ne__, generator()))
print(True)
