from database import get_connection


def add_member():
    name = input("Üye adı: ")
    phone = input("Telefon: ")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO members (name, phone) VALUES (?, ?)",
        (name, phone)
    )

    connection.commit()
    connection.close()

    print("Üye başarıyla eklendi.")


def list_members():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM members")
    members = cursor.fetchall()

    connection.close()

    print("\n--- Üye Listesi ---")
    for member in members:
        print(f"ID: {member[0]} | Ad: {member[1]} | Telefon: {member[2]}")


def update_member():
    member_id = int(input("Güncellenecek üye ID: "))
    name = input("Yeni üye adı: ")
    phone = input("Yeni telefon: ")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE members SET name = ?, phone = ? WHERE id = ?",
        (name, phone, member_id)
    )

    connection.commit()
    connection.close()

    print("Üye başarıyla güncellendi.")


def delete_member():
    member_id = int(input("Silinecek üye ID: "))

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM members WHERE id = ?", (member_id,))

    connection.commit()
    connection.close()

    print("Üye başarıyla silindi.")