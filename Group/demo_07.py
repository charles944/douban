# A = [0, 1, 2, 3, 4]
# B = [0, 1, 2, 3, 4,5,6,7,8,9,10,11,12,13,14]
# C=B[len(A):]
# print(type(C))
with open("test_02.txt","a+",encoding="utf-8") as f_02:
    # f.seek(0)
    # text=f.read()
    # print(text)
    # text=text.split(" ")
    # # print("现在已经爬取了%d个词语了"%len(text))
    # for x in text:
    #     print("这个元素是"+x)
    # f.write("我是你爸爸")
    with open("test_01.txt","r",encoding="utf-8") as f_01:
        text=f_01.read()
        text_arr=text.split(" ")
        for text_loso in text_arr:
            f_02.write("\n"+text_loso)