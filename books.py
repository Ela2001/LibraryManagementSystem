from database import get_connection


def add_book():
    title = input("Kitap adı: ")
    author = input("Yazar: ")
    year = int(input("Yayın yılı: "))
    stock = int(input("Stok adedi: "))

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO books (title, author, year, stock) VALUES (?, ?, ?, ?)",
        (title, author, year, stock)
    )

    connection.commit()
    connection.close()

    print("Kitap başarıyla eklendi.")


def list_books():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    connection.close()

    print("\n--- Kitap Listesi ---")
    for book in books:
        print(f"ID: {book[0]} | Ad: {book[1]} | Yazar: {book[2]} | Yıl: {book[3]} | Stok: {book[4]}")


def update_book():
    book_id = int(input("Güncellenecek kitap ID: "))
    title = input("Yeni kitap adı: ")
    author = input("Yeni yazar: ")
    year = int(input("Yeni yayın yılı: "))
    stock = int(input("Yeni stok adedi: "))

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE books SET title = ?, author = ?, year = ?, stock = ? WHERE id = ?",
        (title, author, year, stock, book_id)
    )

    connection.commit()
    connection.close()

    print("Kitap başarıyla güncellendi.")


def delete_book():
    book_id = int(input("Silinecek kitap ID: "))

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))

    connection.commit()
    connection.close()

    print("Kitap başarıyla silindi.")