# Bai lab 2 May tinh


# Tao menu tinh nang
class Init:
    
    def input_dynamic() :
        list_intput = []
        count_value = input("Ban muon thuc hien voi bao nhieu so")
        if  count_value.isdigit():
            count_value = int(count_value)
        for i in count_value :
            i = input(f"Nhap so thu {i+1}: ")
            list_intput.append(i)
        return list_intput
    
class Function:
    def add_(intput) :
        print("Day la phep cong")

def menu_Home() :
        print("Xin Chao ban den voi may tinh")
        print("Cac phep tinh")
        print("1.Phep cong")
        print("2.Phep tru")
        print("3.Phep nhan")
        print("4.Phep chia")
        print("5.Thoat")   
if __name__=="__main__":
    
    menu_Home() 
    print("Day la phep cong")