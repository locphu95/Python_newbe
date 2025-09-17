import re
import pandas as pd
import csv
import json
#Lab 1: Viết chương trình quản lý danh bạ (thêm, sửa, xóa, lưu file)
print("day la bai hoc dau tien")

#khai bao kieu danh sach luu thong tin danh ba
Contacts = []

#khai bao mot function
def check_function(name):
    match int(name):
        case 1 :
            print("Ban da chon, tinh nang 1 Hien thi danh ba")
            countContact(Contacts)
        case 2 :
            print("Ban da chon, tinh nang 2 Tim danh ba")
            if len(Contacts) > 0 :      
                showContactFind(findContact())
            else:
                countContact(Contacts)
                print("Khong the tim kiem")
        case 3 :
            print("Ban da chon, tinh nang Them kiem danh ba")
            addNewContact() 
        case 4 :
            print("Ban da chon, tinh nang Dieu chinh danh ba")
            edit_contact() 
        case 5 :
            print("Ban da chon, tinh nang Xoa danh ba")
            delete_Contact()
        case 6 :
            print("Ban da chon, tinh nang Xuat danh ba")
            export_Contact()  
        case 7 :
            print("Ban da chon, Thoat")

def countContact(data):
    print(f"So luong danh ba la {len(data)}")
    if len(data) > 0 :
        showContactFind(data)

def validator_Input(type,value):
    if value.isdigit() and type =="int":
        print("Day la so nguyen (int).")
        return True
    elif value.replace('.', '', 1).isdigit():
        print("Day la so thuc (float).")
    elif value.lower() in ["true", "false"]:
        print("Day la boolean.")
    elif len(value) == 1:
        print("Day la ky tu.")
    else:
        print("Day la chuoi.")
    
    return False
    
    # data_check = False
    # if type =="int" : 
    #  data_check =   isinstance(int(value), int)
    # elif type =="string" :
    #   data_check = isinstance(value, str)
    # print(f"validator data is {data_check}")

def addNewContact() :
    print("\n Vui long nhap cac thong tin sau")
    name = input("Nhap ten: ")
    phone = input("Nhap sdt: ")

    while  validator_Input("int",phone) == False :
        phone = input("Vui long chi nhap so: ")
        continue
   
    while len(find_by_phone(phone)) > 0 :
        phone = input("So dien thoai da ton tai !!!!! \nVui long nhap so khac: ")
        continue
       
    email = input("Nhap Email: ")

    tempContact ={
        "ten" : name,
        "phone": phone,
        "email": email,
        "index": len(Contacts) + 1
    }

    Contacts.append(tempContact)
    print(f"Them thong tin lien he cua {name} thanh cong")
    countContact(Contacts)

def edit_contact() :
    data_find = findContact()
    if len(data_find) > 0 :
        for item in data_find:
            print(f"STT:{item.get('index')}. Ten:{item.get('ten')}, SDT:{item.get('phone')}")
        index_edit = input("Chon dong dieu chinh: ")
        while len(index_edit) > len(data_find) :
            index_edit = input("Dong dieu chinh khong duoc lon hon so dong tim duoc: ")
            continue
        print(f"Ban co muon dieu chinh lien he tai dong {index_edit} Khong?")
        confirm_action = input  ("1.Co \n2.Khong \nBan chon: ")
        if confirm_action =="2" :
            showMenu()
        else:
            try:
                selected_contact = Contacts[int(index_edit)-1]
                print("\nNhap thong tin moi (de trong neu khong muon sua):")
                new_name = input(f"Ten moi ({selected_contact.get('ten')}): ")

                new_phone = input(f"SDT moi ({selected_contact.get('phone')}): ")

                while len(find_by_phone(new_phone)) > 0 :
                    new_phone = input("So dien thoai da ton tai !!!!! \nVui long nhap so khac: ")
                    continue
                new_email = input(f"Email moi ({selected_contact.get('email')}): ")

                if new_name:
                    selected_contact['ten'] = new_name
                if new_phone:
                    selected_contact['phone'] = new_phone
                if new_email:
                    selected_contact['email'] = new_email
                print("Cap nhat thong tin thanh cong ! Thong tin sau khi cap nhat la")
                
                showContactFind(Contacts)
            except  ValueError:
                print("Vui long nhap so.")
    else :
        print("Khong the thuc hien tinh nang dieu chinh")

def delete_Contact() :
    data_find = findContact()
    if len(data_find) <= 0 :
        print("Khong the thuc hien tinh nang xoa")
    else :
        index_edit = input("\nChon liem he muon xoa")
        while len(index_edit) > len(data_find) :
            index_edit = input("\nLien he muon xoa khong duoc lon hon so dong tim duoc")
            continue
        print(f"\nBan co muon xoa lien he tai dong {index_edit} Khong?")
        confirm_action = input("\n1.Co \n2.Khong")
        if confirm_action =="2" :
            showMenu()
        else:
            try:
                Contacts.pop( int(index_edit)-1)
                print("Xoa thong tin danh ba thanh cong! Danh ba con lai.")
                showContactFind(Contacts)
            except  ValueError:
                print("Vui long nhap so.")

def export_Contact ():
    data_find = findContact()
    if len(data_find) <= 0 :
        print("Khong the thuc hien tinh nang xuat danh ba lien lac")
    else :
        type_export = input("Chon loai dinh dang can xuat danh ba \n1.Excel \n2.Txt \n3.Csv \n4.Json \nBan chon dinh dang: ")
        while int(type_export) > 4 :
            type_export = print("Dinh dang khong duoc ho tro xin chon lai dinh dang duoc ho tro: ")
            continue
        
        match type_export:
            case "1": #la excel
                file_Name = "danhba.xlsx"
                df = pd.DataFrame(Contacts)
                df.to_excel(file_Name, index=False)
                print(f"Xuat thanh cong {file_Name}")
            case "2": #la TXT               
                file_Name = "danhba.txt"
                with open(file_Name, "w", encoding="utf-8") as f:
                    for c in Contacts:
                        f.write(f"Tên: {c['ten']}, SĐT: {c['phone']}, Email: {c['email']}\n")
                print(f"Xuat thanh cong {file_Name}")
            case "3": #la CSV
                file_Name = "danhba.csv"
                keys = Contacts[0].keys()
                with open(file_Name, "w", newline="", encoding="utf-8") as f:
                    writer = csv.DictWriter(f, fieldnames=keys)
                    writer.writeheader()
                    writer.writerows(Contacts)
                print(f"Xuat thanh cong {file_Name}")
            case "4": #la json
                file_Name = "danhba.json"
                with open(file_Name, "w", encoding="utf-8") as f:
                    json.dump(Contacts, f, ensure_ascii=False, indent=4)
                print(f"Xuat thanh cong {file_Name}")

def find_by_phone(phone) :
    temp = []
    for i_contact in Contacts :
        if phone.lower() in i_contact.get('phone','').lower():
            temp.append(i_contact)
    return temp

def find_by_name(ten) :
    temp = []
    for i_contact in Contacts :
        if ten.lower() in i_contact.get('ten','').lower():
            temp.append(i_contact)
        else :
            continue
    return temp

def find_by_mail(mail) :
    temp = []
    for i_contact in Contacts :
        if mail.lower() in i_contact.get('mail','').lower():
            temp.append(i_contact)
        else :
            continue
    return temp

def filter_search() :
    print("Vui long chon thong tin can tim kiem: \n1. Theo ten \n2. Theo sdt \n3. Theo email ")
    find_by_key = input("Chon: ")
    print("Vui long Nhap thong tin can tim")
    find_by_value = input("Nhap: ")
    return find_by_key,find_by_value


def findContact():
    if len(Contacts) <= 0 :
        print("Khong co thong tin nao trong danh sach. Vui long them moi")
        return []    
        
    find_by_key, find_by_value = filter_search() 

    tempFind = []
    if find_by_key == "1" :           
        tempFind = find_by_name(find_by_value) 
    elif find_by_key == "2":
        tempFind = find_by_phone(find_by_value)
    elif find_by_key == "3":
        tempFind = find_by_mail(find_by_value)
    elif find_by_key == "0" :
        tempFind = Contacts
    if len(tempFind) < 0 :
        print(f'Khong tim duoc thong tin lien lac theo tu khoa {find_by_value}')
    else :
        print(f"tim duoc {len(tempFind)} thong tin lien lac")
    return tempFind       
       

def showContactFind(data) :
    for i in data :
        print(i)

def showMenu() :
    print("\n" + "="*30)
    print("Menu tac vu")
    print("0. Hien lai menu")
    print("1. Hien thi danh ba")
    print("2. Tim kiem danh ba")
    print("3. Them moi danh ba")
    print("4. Dieu chinh dah ba")
    print("5. Xoa danh danh ba")
    print("6. Xuat danh ba")
    print("7. Ram dom thong tin")
    print("8. Dung lai")
    

    


if __name__ == "__main__":
    print("________Running_______")
    showMenu() 
    while True:      
        luachontinhnang = input("Chon tinh nang tu 1->7: ").strip()
        if(int(luachontinhnang) == 3) :
            soluong = input("Nhap so lan thuc hien")
        if(int(luachontinhnang) == 0) :
            showMenu()
        if int(luachontinhnang) == 1:
            print("\n" + "="*30)
            check_function(int(luachontinhnang))
        elif int(luachontinhnang) == 2:
            print("\n" + "="*30)
            check_function(int(luachontinhnang))   
        elif int(luachontinhnang) == 3:
            print("\n" + "="*30)
            check_function(int(luachontinhnang))
        elif int(luachontinhnang) == 4:
            print("\n" + "="*30)
            check_function(int(luachontinhnang))
        elif int(luachontinhnang) == 5:
            print("\n" + "="*30)
            check_function(int(luachontinhnang))
        elif int(luachontinhnang) == 6:
            print("\n" + "="*30)
            check_function(int(luachontinhnang))
        if int(luachontinhnang) == 7 :
            print("\n" + "="*30)
            print("Cam on ban da su dung chuong trinh")
            break
        else :
            print("vui long chon tu 1 -> 7")
    

    

