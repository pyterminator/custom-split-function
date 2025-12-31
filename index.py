# https://youtube.com/@PyTerminator

def mysplit(s)-> list:
    my_list:list = []
    
    word = ""
    for ch in s:
        if ch == " ":
            if word != "":
                my_list.append(word)
            word = ""
            continue
        word += ch
    if word != "":
        my_list.append(word)
        word = ""
    
    
    return my_list


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
