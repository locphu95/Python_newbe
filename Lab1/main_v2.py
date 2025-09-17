import re
import json
import csv
import logging
from pathlib import Path
from typing import List, Dict
import pandas as pd


# --- Setup logging ---
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


class Contact:
    """Model for a contact entry."""

    def __init__(self, name: str, phone: str, email: str, index: int):
        self.name = name
        self.phone = phone
        self.email = email
        self.index = index

    def to_dict(self) -> Dict:
        return {"index": self.index, "name": self.name, "phone": self.phone, "email": self.email}

    def __repr__(self) -> str:
        return f"[{self.index}] {self.name} - {self.phone} - {self.email}"


class ContactManager:
    """Manager to handle CRUD operations on contacts."""

    def __init__(self):
        self.contacts: List[Contact] = []

    def add_contact(self, name: str, phone: str, email: str) -> None:
        if any(c.phone == phone for c in self.contacts):
            raise ValueError("Phone already exists")

        index = len(self.contacts) + 1
        contact = Contact(name, phone, email, index)
        self.contacts.append(contact)
        logging.info("Added new contact: %s", contact)

    def find(self, keyword: str, by: str = "name") -> List[Contact]:
        keyword = keyword.lower()
        if by == "name":
            return [c for c in self.contacts if keyword in c.name.lower()]
        elif by == "phone":
            return [c for c in self.contacts if keyword in c.phone.lower()]
        elif by == "email":
            return [c for c in self.contacts if keyword in c.email.lower()]
        return []

    def edit_contact(self, index: int, name: str = None, phone: str = None, email: str = None) -> None:
        try:
            contact = self.contacts[index - 1]
        except IndexError:
            raise ValueError("Contact not found")

        if phone and any(c.phone == phone and c.index != index for c in self.contacts):
            raise ValueError("Phone already exists")

        if name:
            contact.name = name
        if phone:
            contact.phone = phone
        if email:
            contact.email = email
        logging.info("Updated contact: %s", contact)

    def delete_contact(self, index: int) -> None:
        try:
            removed = self.contacts.pop(index - 1)
            logging.info("Deleted contact: %s", removed)
        except IndexError:
            raise ValueError("Contact not found")

    def export(self, fmt: str, file_name: str = None) -> Path:
        if not self.contacts:
            raise ValueError("No contacts to export")

        data = [c.to_dict() for c in self.contacts]
        fmt = fmt.lower()
        file_map = {
            "excel": Path("contacts.xlsx"),
            "csv": Path("contacts.csv"),
            "json": Path("contacts.json"),
            "txt": Path("contacts.txt"),
        }

        file_path = file_map.get(fmt)
        if not file_path:
            raise ValueError("Unsupported export format")

        if fmt == "excel":
            pd.DataFrame(data).to_excel(file_path, index=False)
        elif fmt == "csv":
            pd.DataFrame(data).to_csv(file_path, index=False, encoding="utf-8")
        elif fmt == "json":
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        elif fmt == "txt":
            with open(file_path, "w", encoding="utf-8") as f:
                for c in self.contacts:
                    f.write(str(c) + "\n")

        logging.info("Exported contacts to %s", file_path)
        return file_path


def main():
    manager = ContactManager()

    while True:
        print("\n--- MENU ---")
        print("1. Show contacts")
        print("2. Add contact")
        print("3. Search contact")
        print("4. Edit contact")
        print("5. Delete contact")
        print("6. Export contacts")
        print("7. Exit")

        choice = input("Choose (1-7): ").strip()
        try:
            if choice == "1":
                for c in manager.contacts:
                    print(c)

            elif choice == "2":
                name = input("Name: ")
                phone = input("Phone: ")
                email = input("Email: ")
                manager.add_contact(name, phone, email)

            elif choice == "3":
                key = input("Search by (name/phone/email): ").strip().lower()
                value = input("Keyword: ")
                results = manager.find(value, by=key)
                for c in results:
                    print(c)

            elif choice == "4":
                idx = int(input("Contact index to edit: "))
                name = input("New name (blank to skip): ")
                phone = input("New phone (blank to skip): ")
                email = input("New email (blank to skip): ")
                manager.edit_contact(idx, name or None, phone or None, email or None)

            elif choice == "5":
                idx = int(input("Contact index to delete: "))
                manager.delete_contact(idx)

            elif choice == "6":
                fmt = input("Format (excel/csv/json/txt): ")
                manager.export(fmt)

            elif choice == "7":
                break

            else:
                print("Invalid choice")

        except Exception as e:
            logging.error(e)


if __name__ == "__main__":
    main()
