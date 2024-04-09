def tinhTongSoChan(lst) :
    sum = 0
    for num in lst:
        if num % 2 == 0:
            sum += num
    return sum

inputList = input("Nhập danh sách các số, cách nhau bằng dấu phầy: ")
numbers = list(map(int, inputList.split(',')))

TongChan = tinhTongSoChan (numbers)
print ("Tổng các số chẵn trong List là:", TongChan)