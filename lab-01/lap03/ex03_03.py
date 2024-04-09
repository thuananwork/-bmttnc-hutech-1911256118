def taoTupleTuList(lst):
    return tuple(lst)

input_list = input ("Nhập danh sách các số, cách nhau bằng dấu phầy: ")
numbers = list (map(int, input_list.split(',')))

my_tuple = taoTupleTuList (numbers)
print ("List: ", numbers)
print ("Tuple tù List:", my_tuple)