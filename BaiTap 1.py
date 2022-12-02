# Bài 1

# dùng try except để bắt lỗi khi người dùng nhập sai
try:
    # nhập số dòng từ bàn phím ( 0< dòng <=100)
    t = int(input("Nhập số dòng muốn nhập: "))
    # điều kiện để thực hiện chương trình là số dòng phải lớn hơn 0 và nhỏ hơn hoặc bằng 100
    if t > 0 and t <= 100 :
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
            # lấy i làm chỉ mục danh sách để tham chiếu tới giá trị của chuỗi trong danh sách
            # sử dụng hàm title() để in hoa các chữ cái đầu của mỗi từ trong chuỗi
            # in ra Test i: (trong đó i tính từ 1) và kết quả biến đổi
            print(f"Test {i + 1}:\n {list_str[i].title()}")
    else:
        # thông báo nhập lại số dòng cho đúng yêu cầu
        print("Vui lòng nhập lại số dòng ( số dòng lớn 0 và nhỏ hơn 100)")
# hiển thị ra thông báo khi người dùng nhập sai đầu vào
except:
    print("Bạn đã nhập sai!\nVui lòng nhập lại số dòng ( số dòng lớn 0 và nhỏ hơn 100)!")