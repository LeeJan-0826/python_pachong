import os
jpgfile = "C:\\Users\\LeeJan\\Desktop\\test_2\\test_2"
keymap_1 = {"皖": 0,"沪": 1,"津": 2,"渝": 3,"冀": 4,"晋": 5,"蒙": 6,"辽": 7,"吉": 8,"黑": 9,"苏": 10,"浙": 11,"京": 12,"闽": 13,"赣": 14,"鲁": 15,"豫": 16,"鄂": 17,"湘": 18,"粤": 19,"桂": 20,"琼": 21,"川": 22,"贵": 23,"云": 24,"西": 25,"陕": 26,"甘": 27,"青": 28,"宁": 29,"新": 30}
keymap_2 = { "a" : 0, "b" : 1, "c" : 2, "d" : 3, "e" : 4, "f" : 5, "g" : 6,"h" : 7,"j" : 8, "k" : 9, "l" : 10, "m" : 11,"n" : 12,"p" : 13, "q" : 14, "r" : 15, "s" :16, "t" : 17, "u" : 18, "v" : 19, "w" : 20,"x": 21,"y" : 22, "z" : 23,"0" : 24, "1" : 25, "2" : 26, "3" : 27, "4" : 28, "5" : 29, "6" : 30, "7" : 31, "8" : 32, "9" : 33}
def readname():
    name = os.listdir(jpgfile)
    return name
def findSubStrIndex(substr, str, time):
    times = str.count(substr)
    if (times == 0) or (times < time):
        pass
    else:
        i = 0
        index = -1
        while i < time:
            index = str.find(substr, index+1)
            i+=1
        return index
def change_name(str):
    i = 0
    str_return = []
    if(str[1] == '_'):
        str_return.append(list(keymap_1.keys())[list(keymap_1.values()).index(int(str[0]))])
        i = 2
    else:
        str_return.append(list(keymap_1.keys())[list(keymap_1.values()).index(int(str[0:2]))])
        i = 3
    # 改keymap_2的对应数字
    # str[i+1]!= '-' or str[i+2]!= '-'
    while(i<len(str)):
        if(str[i+1]=='_' or str[i+1]=='-'):
            str_return.append(list(keymap_2.keys())[list(keymap_2.values()).index(int(str[i]))])
            i = i + 2
        else:
            str_return.append(list(keymap_2.keys())[list(keymap_2.values()).index(int(str[i:i+2]))])
            i = i + 3
        print(str_return)
    str_return.append('.jpg')   # 列表追加
    str_res = ''.join(str_return)
    return str_res.upper()    #将小写变成大写

def rename(filename):
    # 找出'-'位置
    print(filename)
    str = os.path.basename(filename)
    num1 = findSubStrIndex('-', str, 4)
    num2 = findSubStrIndex('-', str, 5)
    str_1 = str[num1+1:num2+1]
    print(str_1)
    new_filename = change_name(str_1)
    print(new_filename)
    os.rename("C:\\Users\\LeeJan\\Desktop\\test_2\\test_2\\" + filename, "C:\\Users\\LeeJan\\Desktop\\test_2\\test_2\\" + new_filename)

if __name__=="__main__":
    list_main = readname()
    for jpgfile_name in list_main:
        rename(jpgfile_name)
