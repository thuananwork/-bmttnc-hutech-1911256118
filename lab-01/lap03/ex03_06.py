def xoaPhanTu(dictionary, key) :
    if key in dictionary:
        del dictionary[key]
        return True

    else:
        return False
# Sử dụng hàm và in kết quả
myDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
ketToDelete = 'b'
result = xoaPhanTu(myDict, ketToDelete)
if result:
    print ("Phần tử đã được xóa từ Dictionary:", myDict)
else:
    print ("Không tìm thấy phần tử cần xóa trong Dictionary.")