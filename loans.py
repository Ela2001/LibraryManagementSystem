from datetime import date

from database import get_connection


def give_loan():
    book_id = int(input("Ödünç verilecek kitap ID: "))
    member_id = int(input("Üye ID: "))

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT stock FROM books WHERE id = ?", (book_id,))
    book = cursor.fetchone()

    if book is None:
        print("Kitap bulunamadı.")
        connection.close()
        return

    if book[0] <= 0:
        print("Bu kitabın stoğu yok.")
        connection.close()
        return

    loan_date = date.today().isoformat()

    cursor.execute(
        "INSERT INTO loans (book_id, member_id, loan_date, return_date) VALUES (?, ?, ?, ?)",
        (book_id, member_id, loan_date, None)
    )

    cursor.execute(
        "UPDATE books SET stock = stock - 1 WHERE id = ?",
        (book_id,)
    )

    connection.commit()
    connection.close()

    print("Kitap başarıyla ödünç verildi.")


def return_loan():
    loan_id = int(input("İade alınacak ödünç ID: "))

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT book_id, return_date FROM loans WHERE id = ?",
        (loan_id,)
    )
    loan = cursor.fetchone()

    if loan is None:
        print("Ödünç kaydı bulunamadı.")
        connection.close()
        return

    if loan[1] is not None:
        print("Bu kitap zaten iade edilmiş.")
        connection.close()
        return

    return_date = date.today().isoformat()
    book_id = loan[0]

    cursor.execute(
        "UPDATE loans SET return_date = ? WHERE id = ?",
        (return_date, loan_id)
    )

    cursor.execute(
        "UPDATE books SET stock = stock + 1 WHERE id = ?",
        (book_id,)
    )

    connection.commit()
    connection.close()

    print("Kitap başarıyla iade alındı.")


def list_loans():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            loans.id,
            books.title,
            members.name,
            loans.loan_date,
            loans.return_date
        FROM loans
        INNER JOIN books ON loans.book_id = books.id
        INNER JOIN members ON loans.member_id = members.id
    """)

    loans = cursor.fetchall()

    connection.close()

    print("\n--- Ödünç Listesi ---")
    for loan in loans:
        return_status = loan[4] if loan[4] is not None else "İade edilmedi"
        print(
            f"ID: {loan[0]} | Kitap: {loan[1]} | Üye: {loan[2]} | "
            f"Alış Tarihi: {loan[3]} | İade Tarihi: {return_status}"
        )