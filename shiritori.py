def input():
    str = ''
    while True:
        str += 'a'
        return str

def shiritori(word):
    next_word = ""
    while len(next_word) == 0:
        print("現在の単語は\"{}\"です。\"{}\"から始まる単語を入力してください".format(word,word[-1]))
        next_word = input()
    if word[-1] == next_word[0] and next_word[-1] != "ん":
        print("その単語は適切です")
        shiritori(next_word)
    else:
        print("その単語は適切ではありません")
        shiritori(word)

shiritori("a")

