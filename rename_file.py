import os

def rename_file():
    file_list = os.listdir(r"/Users/sunzheng-jie/Desktop/git/udacity/prank")
    #print(file_list)

    os.chdir("/Users/sunzheng-jie/Desktop/git/udacity/prank")

    for file_name in file_list:
        os.rename(file_name, file_name.lstrip("0123456789"))

rename_file()