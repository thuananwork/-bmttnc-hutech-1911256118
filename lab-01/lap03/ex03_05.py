def demSoLanSoHien(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict [item] += 1
        else:
            count_dict[item] = 1
    return count_dict

inputString = input ("Nhập danh sách các từ, cách nhau bằng dấu cách: ")
wordList = inputString.split ()

soLanXuatHien = demSoLanSoHien (wordList)
print ("Số lần xuất hiện của các phần từ:", soLanXuatHien)