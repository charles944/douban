
# with open("keywords.txt","r",encoding="utf-8-sig") as f:
#     test=f.read();
#     test=test.split(" ")
#     for x in test:
#         print(x)

with open("test_02.txt","r",encoding="utf-8-sig") as f:
    test=f.read();
    test=test.split("\n")
    print(len(test))
    for x in test:
        print(x)