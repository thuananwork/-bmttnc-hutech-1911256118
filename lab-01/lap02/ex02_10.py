def daoNguocChuoi (chuoi) :
    return chuoi[ ::- 1]

inputString = input ("Nhập chuỗi cần đảo ngược: ")
print ("Chuỗi đào ngược là:", daoNguocChuoi (inputString))