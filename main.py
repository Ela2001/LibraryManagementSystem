from database import create_tables
from books import add_book, list_books, update_book, delete_book
from members import add_member, list_members, update_member, delete_member
from loans import give_loan, return_loan, list_loans


def book_menu():
    while True:
        print("\n--- Kitap İşlemleri ---")
        print("1- Kitap Ekle")
        print("2- Kitap Listele")
        print("3- Kitap Güncelle")
        print("4- Kitap Sil")
        print("5- Ana Menüye Dön")

        choice = input("Seçiminiz: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            list_books()
        elif choice == "3":
            update_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            break
        else:
            print("Geçersiz seçim.")


def member_menu():
    while True:
        print("\n--- Üye İşlemleri ---")
        print("1- Üye Ekle")
        print("2- Üye Listele")
        print("3- Üye Güncelle")
        print("4- Üye Sil")
        print("5- Ana Menüye Dön")

        choice = input("Seçiminiz: ")

        if choice == "1":
            add_member()
        elif choice == "2":
            list_members()
        elif choice == "3":
            update_member()
        elif choice == "4":
            delete_member()
        elif choice == "5":
            break
        else:
            print("Geçersiz seçim.")


def loan_menu():
    while True:
        print("\n--- Ödünç İşlemleri ---")
        print("1- Kitap Ödünç Ver")
        print("2- Kitap İade Al")
        print("3- Ödünç Listesi")
        print("4- Ana Menüye Dön")

        choice = input("Seçiminiz: ")

        if choice == "1":
            give_loan()
        elif choice == "2":
            return_loan()
        elif choice == "3":
            list_loans()
        elif choice == "4":
            break
        else:
            print("Geçersiz seçim.")


def main_menu():
    create_tables()

    while True:
        print("\n===== KÜTÜPHANE YÖNETİM SİSTEMİ =====")
        print("1- Kitap İşlemleri")
        print("2- Üye İşlemleri")
        print("3- Ödünç İşlemleri")
        print("4- Çıkış")

        choice = input("Seçiminiz: ")

        if choice == "1":
            book_menu()
        elif choice == "2":
            member_menu()
        elif choice == "3":
            loan_menu()
        elif choice == "4":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim.")


main_menu()