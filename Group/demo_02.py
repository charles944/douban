
with open("test_01.txt","a+",encoding="utf-8") as f:
    f.seek(0)
    words=f.read()
    print(words)
    # print(f.tell())
    # f.write("")
    # words=f.read()
    # print(words)
    f.write(" 哈哈")