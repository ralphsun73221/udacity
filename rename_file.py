import os

def rename_file():
    file_list = os.listdir(r"/Users/sunzheng-jie/Desktop/git/udacity/prank")
    #print(file_list)

    os.chdir("/Users/sunzheng-jie/Desktop/git/udacity/prank")
    #如果你把這程式跟想更改檔名的當按放在同一個資料夾其實就可以把這段也註解掉

    for file_name in file_list:
        print("Old Name - " + file_name)
        print("New Name - " + file_name.lstrip("0123456789"))
        #上面這兩串的用意在於讓你知道他執行的過程，同時會在終端出現舊的名字跟新的名字
        
        os.rename(file_name, file_name.lstrip("0123456789"))

rename_file()