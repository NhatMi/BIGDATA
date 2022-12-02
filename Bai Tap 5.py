# Bài 5
def chuoi_s2(a1, a2):
   # Sử dụng toán tử in để kiểm tra sự xuất hiện của chuỗi S2
   if a2 in a1:
       # Sử dụng phương thức count() để đếm số lần xuất hiện của chuỗi S2
       print(a1.count(a2))
   else:
       # format() được tích hợp sẵn trong Python để định dạng một giá trị truyền vào thành một định dạng cụ thể
       print('Chuỗi "{}" không xuất hiện trong chuỗi "{}"'.format(a2, a1))


t = int(input("Nhập vào số lần bạn muốn kiểm tra: "))
if 0 < t <= 100:
    for i in range(t):
        print(f"test {i + 1}:")
        s1 = input(f"Nhập chuỗi S1: ")
        s2 = input(f"Nhập chuỗi S2: ")
        print(f"test {i + 1}:", end="\n")
        chuoi_s2(s1, s2)
