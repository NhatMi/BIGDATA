# Bài 6
# Sử dụng try except để bắt lỗi khi người dùng nhập sai
try:
    # Nhập số bộ test từ bàn phím ( 0 < bộ test <= 100)
    t = int(input("Nhập số bộ test: "))
    # Điều kiện để thực hiện chương trình là số bộ test phải lớn hơn 0 và nhỏ hơn hoặc bằng 100
    if(t > 0 and t <= 100):
        # Cho i chạy từ 0 đến số lượng bộ test đã nhập lúc đầu để nhập đúng số chuỗi mong muốn
        for i in range(t):
            # Nhập lần lượt các chuỗi cho mỗi bộ test
            Str = input(f"Chuỗi string thứ {i + 1}: ")
            # Nhập chuỗi old và new
            Old = input(f"Chuỗi old thứ {i+1}: ")
            New = input(f"Chuỗi new thứ {i+1}: ")
            # Sử dụng hàm replace(old, new) để thay thế chuỗi old bởi chuỗi new trong string
            # Sau đó in ra kết quả Dòng đầu có dạng Test i: Trong đó i là thứ tự bộ test tính từ 1
            # Dòng còn lại là chuỗi kết quả sau khi được thay thế
            print(f"Test {i+1}: {Str.replace(Old, New)}")
    else:
        # Thông báo nhập lại số bộ test cho đúng yêu cầu
        print("Vui lòng nhập lại số bộ test ( Số bộ test lớn 0 và nhỏ hơn 100)")
# Hiển thị ra thông báo khi người dùng nhập sai đầu vào
except:
    print("Bạn đã nhập sai!\nVui lòng nhập lại số bộ test ( Số bộ test lớn 0 và nhỏ hơn 100)!")