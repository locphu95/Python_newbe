# Bai lab 2 May tinh


# Tao menu tinh nang
from typing import List


    
    
    
class Function:
    def __init__(self):
        self.inputs: list[int] = []

    def input_dynamic(self):
        count_value = input("Bạn muốn thực hiện với bao nhiêu số: ")
        if count_value.isdigit():
            count_value = int(count_value)
            for i in range(count_value):
                value = input(f"Nhập số thứ {i+1}: ")
                if value.isdigit():
                    self.inputs.append(int(value))
                else:
                    print(f"Giá trị '{value}' không hợp lệ, bỏ qua.")
            return self.inputs
        else:
            print("Giá trị không hợp lệ, mặc định là 0")
        return []

        
    
    
    def add_(self,data) :
        print("Day la phep cong")
        return sum(data)
    
    def subtract_(self,data):
        print("Day la phep tru")
        if not data:
            print("Khong co thong tin de thuc hien")
        result = data[0]
        for num in data[1:]:
            result-=num
        return result
    
    def multiply_(self,data):
        print("Đây là phép nhân")
        result = 1
        for num in data:
            result *= num
        print(f"Kết quả là: {result}")
        return result

    def divide_(self,data):
        print("Đây là phép chia")
        if not data:
            print("Không có dữ liệu để chia")
            return None
        result = data[0]
        try:
            for num in data[1:]:
                result /= num
            print(f"Kết quả là: {result}")
            return result
        except ZeroDivisionError:
            print("Lỗi: chia cho 0")
            return None


def menu_Home() :
        print("Xin Chao ban den voi may tinh")
        print("Cac phep tinh")
        print("1.Phep cong")
        print("2.Phep tru")
        print("3.Phep nhan")
        print("4.Phep chia")
        print("5.Thoat")   
if __name__=="__main__":
    _funct = Function()
    menu_Home() 
    while True:
        choice = input("Choose (1-7): ").strip()
        try:
            if choice == "1":
                data = _funct.input_dynamic()
                print(f"Tong la: {_funct.add_(data)}")
                print("\n" + "="*30)
            if choice =="2":
                data = _funct.input_dynamic()
                print(f"Hieu la: {_funct.subtract_(data)}")
                print("\n" + "="*30)
            if choice == "3":
                data = _funct.input_dynamic()
                print(f"Thuong la: {_funct.multiply_(data)}")
                print("\n" + "="*30)
            if choice == "4":
                data = _funct.input_dynamic()
                print(f"Tich la: {_funct.divide_(data)}")
                print("\n" + "="*30)
            if choice =="5":
                print("\n" + "="*30)
                break
        except:
            print("da xay ra loi")
        


