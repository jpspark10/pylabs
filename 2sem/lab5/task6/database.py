import sqlite3
import os

DB_NAME = "library.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    # Таблица пользователей: id, уникальный логин, хэш пароля
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    """)
    # Таблица книг: id, название, автор, год издания, жанр, путь к изображению
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER,
            genre TEXT,
            image_path TEXT
        )
    """)
    conn.commit()
    conn.close()


def register_user(login, password_hash):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (login, password_hash) VALUES (?, ?)", (login, password_hash))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()


def verify_user(login, password_hash):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE login=? AND password_hash=?", (login, password_hash))
    user = cursor.fetchone()
    conn.close()
    return user is not None


# Функции для работы с книгами:
def get_all_books():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()
    return books


def search_books_by_author(author):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE author LIKE ?", (f"%{author}%",))
    books = cursor.fetchall()
    conn.close()
    return books


def search_books_by_title(title):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE title LIKE ?", (f"%{title}%",))
    books = cursor.fetchall()
    conn.close()
    return books


def add_book(title, author, year, genre, image_path):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author, year, genre, image_path) VALUES (?, ?, ?, ?, ?)",
                   (title, author, year, genre, image_path))
    conn.commit()
    conn.close()


def update_book(book_id, title, author, year, genre, image_path):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE books SET title=?, author=?, year=?, genre=?, image_path=? WHERE id=?
    """, (title, author, year, genre, image_path, book_id))
    conn.commit()
    conn.close()


def delete_book(book_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
    conn.commit()
    conn.close()
