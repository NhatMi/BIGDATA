# Bài 2
# Sử dụng try except để bắt lỗi nếu người dùng nhập sai
try:
    t = int(input("Nhập số dòng: "))
    if t > 0 and t <= 100 :                 #Điều kiện khi nhập số dòng là phải lớn hơn 0 và nhỏ hơn hoặc bằng 100
        ds_chuoi = []
        for i in range(t):                  #Vòng lặp cho i chạy từ 0 đến số lượng dòng đã nhập ở trên
            chuoi = input(f"Nhập dòng thứ {i + 1}: ")
            ds_chuoi.append(chuoi)          #Dùng append để thêm chuỗi vào trong danh sách
        for i in range(len(ds_chuoi)):      #Vòng lặp cho i chạy đến độ dài của danh sách chuỗi
            na = 0
            pa = 0
            for j in ds_chuoi[i]:           #Vòng lặp cho j chạy đến phần tử trong danh sách chuỗi i
            #Điều kiện để đếm các nguyên âm kể cả chữ in hoa trong danh sách đã nhập
                if (j == "a" or j == "e" or j == "i" or j == "o" or j == "u" or
                        j == "A" or j == "E" or j == "I" or j == "O" or j == "U"):
                            na += 1
                elif(j == ' '):         #Nếu có khoảng trắng thì tiếp tục chạy và không đếm
                    continue
                else:
                    pa += 1             #Cộng thêm 1 nếu vòng lặp chạy đến 1 phụ âm
            print(f"Test {i + 1}:\n{na}\n{pa}")     # In ra kết quả theo thứ tự của bộ Test i (i tính từ 1)
    else:
        #Thông báo khi người dùng nhập sai số dòng so với điều kiện
        print("Nhập sai! số dòng phải lớn hơn 0 và nhỏ hơn hoặc bằng 100)")
except:
    print("Số dòng bạn nhập không đúng!")       #Thông báo lỗi khi nhập sai input