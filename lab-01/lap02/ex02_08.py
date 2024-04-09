def chia_het_cho_5(soNhiPhan) :
    soThapPhan = int (soNhiPhan, 2)
    if soThapPhan % 5 == 0:
        return True
    else:
        return False
chuoiSoNhiPhan = input ("Nhập chuỗi số nhị phân (phân tách bời dấu phẩy) : ")
soNhiPhanList = chuoiSoNhiPhan.split(',')
soChiaHetCho5 = [so for so in soNhiPhanList if chia_het_cho_5(so) ]

if len(soChiaHetCho5) > 0:
    ketQua = ','.join (soChiaHetCho5)
    print ("Các số nhị phân chia hết cho 5 :", ketQua)
else:
    print ("Không có so nhi phân nao chia hết cho 5 trong chuỗi đa nhập.")