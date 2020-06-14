
with open("test_01.txt","r",encoding="utf-8") as f:
    test=f.read()
    test=test.split(" ")
    print(len(test))
    for x in range(len(test)):
        print("第%d个数组元素为:"%x+test[x])
