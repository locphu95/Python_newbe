import re
import pandas as pd
import csv
import json

Contacts = []

def check_function(choice):
    match choice:
        case 1:
            print("Ban da chon: Hien thi danh ba")
            countContact(Contacts)
        case 2:
            print("Ban da chon: Tim danh ba")
            if len(Contacts) > 0:
                showContactFind(findContact())
            else:
                countContact(Contacts)
                print("Khong the tim kiem")
        case 3:
            print("Ban da chon: Them danh ba")
            addNewContact()
        case 4:
            print("Ban da chon: Dieu chinh danh ba")
            edit_contact()
        case 5:
            print("Ban da chon: Xoa danh ba")
            delete_Contact()
        case 6:
            print("Ban da chon: Xuat danh ba")
            export_Contact()
        case 7:
            print("Ban da chon: Thoat")

def countContact(data):
    print(f"So luong danh ba: {len(data)}")
    if len(data) > 0:
        showContactFind(data)

def validator_Input(type, value):
    if value.isdigit() and type == "int":
        return True
    return False

def addNewContact():
    print("\nNhap thong tin lien he")
    name = input("Nhap ten: ")
    phone = input("Nhap so dien thoai: ")

    while not validator_Input("int", phone):
        phone = input("Chi nhap so: ")

    while len(find_by_phone(phone)) > 0:
        phone = input("So dien thoai da ton tai, vui long nhap so khac: ")

    email = input("Nhap email: ")

    tempContact = {
        "ten": name,
        "phone": phone,
        "email": email,
        "index": len(Contacts) + 1
    }
    Contacts.append(tempContact)
    print(f"Them lien he {name} thanh cong")
    countContact(Contacts)

def edit_contact():
    data_find = findContact()
    if len(data_find) > 0:
        for item in data_find:
            print(f"STT:{item.get('index')}. Ten:{item.get('ten')}, SDT:{item.get('phone')}")
        index_edit = input("Chon dong can sua: ")

        try:
            selected_contact = Contacts[int(index_edit) - 1]
            print("\nNhap thong tin moi (bo trong neu khong muon sua):")
            new_name = input(f"Ten moi ({selected_contact.get('ten')}): ")
            new_phone = input(f"SDT moi ({selected_contact.get('phone')}): ")

            while len(find_by_phone(new_phone)) > 0:
                new_phone = input("So dien thoai da ton tai, vui long nhap so khac: ")

            new_email = input(f"Email moi ({selected_contact.get('email')}): ")

            if new_name:
                selected_contact['ten'] = new_name
            if new_phone:
                selected_contact['phone'] = new_phone
            if new_email:
                selected_contact['email'] = new_email
            print("Cap nhat thanh cong")
            showContactFind(Contacts)
        except ValueError:
            print("Vui long nhap so.")
    else:
        print("Khong tim thay de sua")

def delete_Contact():
    data_find = findContact()
    if len(data_find) > 0:
        index_edit = input("Chon dong muon xoa: ")
        try:
            Contacts.pop(int(index_edit) - 1)
            print("Xoa thanh cong")
            showContactFind(Contacts)
        except ValueError:
            print("Vui long nhap so.")
    else:
        print("Khong co du lieu de xoa")

def export_Contact():
    if len(Contacts) == 0:
        print("Khong co du lieu de xuat")
        return
    type_export = input("Chon dinh dang: \n1.Excel \n2.Txt \n3.Csv \n4.Json \nNhap: ")
    match type_export:
        case "1":
            file_name = "danhba.xlsx"
            pd.DataFrame(Contacts).to_excel(file_name, index=False)
        case "2":
            file_name = "danhba.txt"
            with open(file_name, "w", encoding="utf-8") as f:
                for c in Contacts:
                    f.write(f"Ten: {c['ten']}, SDT: {c['phone']}, Email: {c['email']}\n")
        case "3":
            file_name = "danhba.csv"
            with open(file_name, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=Contacts[0].keys())
                writer.writeheader()
                writer.writerows(Contacts)
        case "4":
            file_name = "danhba.json"
            with open(file_name, "w", encoding="utf-8") as f:
                json.dump(Contacts, f, ensure_ascii=False, indent=4)
    print(f"Xuat file {file_name} thanh cong")

def find_by_phone(phone):
    return [c for c in Contacts if phone in c.get("phone", "")]

def find_by_name(name):
    return [c for c in Contacts if name.lower() in c.get("ten", "").lower()]

def find_by_mail(mail):
    return [c for c in Contacts if mail.lower() in c.get("email", "").lower()]

def filter_search():
    print("Tim kiem theo: \n1.Ten \n2.SDT \n3.Email ")
    key = input("Chon: ")
    value = input("Nhap tu khoa: ")
    return key, value

def findContact():
    if len(Contacts) == 0:
        print("Danh ba rong")
        return []
    key, value = filter_search()
    if key == "1":
        return find_by_name(value)
    elif key == "2":
        return find_by_phone(value)
    elif key == "3":
        return find_by_mail(value)
    return []

def showContactFind(data):
    for c in data:
        print(c)

def showMenu():
    print("\n===== MENU =====")
    print("1. Hien thi danh ba")
    print("2. Tim kiem danh ba")
    print("3. Them moi danh ba")
    print("4. Sua danh ba")
    print("5. Xoa danh ba")
    print("6. Xuat danh ba")
    print("7. Thoat")

def main():
    showMenu()
    while True:
        choice = input("Chon chuc nang (1-7): ")
        if choice.isdigit():
            choice = int(choice)
            if choice in range(1, 8):
                if choice == 7:
                    print("Tam biet!")
                    break
                check_function(choice)
            else:
                print("Chi nhap tu 1 den 7")
        else:
            print("Chi nhap so")

if __name__ == "__main__":
    main()
