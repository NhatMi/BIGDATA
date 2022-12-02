# Bài 4

# dùng try except để bắt lỗi khi người dùng nhập sai
try:
    # nhập số dòng từ bàn phím ( 0< dòng <=100)
    t = int(input("Nhập số dòng muốn nhập: "))
    # điều kiện để thực hiện chương trình là số dòng phải lớn hơn 0 và nhỏ hơn hoặc bằng 100
    if(t > 0 and t <= 100):
        # tạo một danh sách để chứa các chuỗi được nhập từ bàn phím
        list_str = []
        # cho i chạy từ 0 đến số lượng dòng đã nhập để nhập đúng số chuỗi mong muốn
        for i in range(t):
            # nhập lần lượt các chuỗi cho mỗi dòng
            Str = input(f"Dòng thứ {i + 1}: ")
            # thêm chuỗi vào danh sách
            list_str.append(Str)
        # cho i chạy từ 0 đến độ dài của danh sách chuỗi
        for i in range(len(list_str)):
            # tạo biến chứa chuỗi là kết quả đầu ra
            output =""
            # list_str[i] dùng i để tham chiếu tới chuỗi trong danh sách
            # sử dụng hàm split() để tách list_str[i] thành các chuỗi con được phân tách bởi khoảng trắng
            # tạo biến String là danh sách chứa các chuỗi con
            String = list_str[i].split()
            # cho x chạy từ 0 đến độ dài danh sách String
            for x in range(len(String)):
                # String[x] truy tham chiếu tới chuỗi con trong danh sách String
                # thêm chuỗi con và khoảng trắng vào chuỗi đầu ra
                output += String[x] + " "
            # in ra dòng 1 dạng Test i (trong đó i là thứ tự bộ test tính từ 1)
            # dòng 2 hiển thị các từ theo thứ tự xuất hiện
            # sử dụng hàm rstrip() để xóa khoảng trắng cuối chuỗi
            print(f"Test {i + 1}:\n{output.rstrip()}")
    else:
        # thông báo nhập lại số dòng cho đúng yêu cầu
        print("Vui lòng nhập lại số dòng ( số dòng lớn 0 và nhỏ hơn 100)")
# hiển thị ra thông báo khi người dùng nhập sai đầu vào
except:
    print("Bạn đã nhập sai!\nVui lòng nhập lại số dòng ( số dòng lớn 0 và nhỏ hơn 100)!")