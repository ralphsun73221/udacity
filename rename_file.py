import os

def rename_file():
    file_list = os.listdir(r"/Users/sunzheng-jie/Desktop/git/udacity/prank")
    #print(file_list)

    os.chdir("/Users/sunzheng-jie/Desktop/git/udacity/prank")
    #如果你把這程式跟想更改檔名的當按放在同一個資料夾其實就可以把這段也註解掉

    for file_name in file_list:
        os.rename(file_name, file_name.lstrip("0123456789"))

rename_file()