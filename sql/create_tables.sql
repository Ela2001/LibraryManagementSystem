CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER,
    stock INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS members (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT
);

CREATE TABLE IF NOT EXISTS loans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER NOT NULL,
    member_id INTEGER NOT NULL,
    loan_date TEXT NOT NULL,
    return_date TEXT,
    FOREIGN KEY (book_id) REFERENCES books(id),
    FOREIGN KEY (member_id) REFERENCES members(id)
);

INSERT INTO books (title, author, year, stock)
SELECT 'Sefiller', 'Victor Hugo', 1862, 5
WHERE NOT EXISTS (
    SELECT 1 FROM books WHERE title = 'Sefiller' AND author = 'Victor Hugo'
);

INSERT INTO books (title, author, year, stock)
SELECT 'Suç ve Ceza', 'Fyodor Dostoyevski', 1866, 3
WHERE NOT EXISTS (
    SELECT 1 FROM books WHERE title = 'Suç ve Ceza' AND author = 'Fyodor Dostoyevski'
);

INSERT INTO members (name, phone)
SELECT 'Ali Yılmaz', '05551234567'
WHERE NOT EXISTS (
    SELECT 1 FROM members WHERE name = 'Ali Yılmaz' AND phone = '05551234567'
);

INSERT INTO members (name, phone)
SELECT 'Ayşe Demir', '05559876543'
WHERE NOT EXISTS (
    SELECT 1 FROM members WHERE name = 'Ayşe Demir' AND phone = '05559876543'
);
